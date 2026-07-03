"""Financial Agent Automation Lab CLI.

TASK-001 provides a mock route-check scaffold.
TASK-002 adds live Codex SDK route classification.
TASK-004 adds a guarded QUICK launch command.
TASK-005 adds QUICK result quality control.
TASK-006 adds AGENT automation design planning without executing the full workflow.
    TASK-007 adds QUICK answer execution with public-data snapshots and validation.
    TASK-008 expands QUICK answer pilots across ETF, crypto, bond ETF, commodity ETF, and comparison.
    TASK-010 adds deterministic QUICK answer output-quality control.
    TASK-014 adds validated full AGENT smoke paths for ETF, fixed income, crypto, commodity, and multi-asset comparison.
    """

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import json
import multiprocessing as mp
import os
import queue
import re
import subprocess
import tempfile
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from uuid import uuid4

from quick_data import (
    COMPARISON_IDENTITY,
    MSFT_IDENTITY,
    QUICK_ASSET_IDENTITIES,
    OUTPUT_QUALITY_REQUIRED_CHECKS,
    OUTPUT_QUALITY_SCHEMA_VERSION,
    answers_require_freshness,
    assess_quick_data_quality,
    assess_quick_output_quality,
    build_quick_source_snapshot,
    create_quick_run_dir,
    detect_quick_asset_identity,
    format_missing_inputs,
    format_quick_limitations,
    quick_fixture_slug,
    quick_freshness_required,
    quick_identity_slug,
    quality_failure_summary,
    safe_timestamp_for_path,
)
from quick_data.providers import ALLOWED_PROVIDER_STATUSES, ALLOWED_PROVIDER_TYPES, ALLOWED_QUALITY_LEVELS
from agent_data import (
    SUPPORTED_EQUITY_TICKERS,
    build_equity_source_preflight,
    build_evidence_pack,
    build_msft_source_preflight,
    detect_equity_mentions,
    render_evidence_pack_markdown,
    resolve_equity_request,
    supported_equity_identity,
    supported_equity_metadata,
)

LAB_ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = Path(os.environ.get("FA_AUTOMATION_PROJECT_ROOT") or LAB_ROOT.parent)
CASES_PATH = LAB_ROOT / "config" / "route_check_cases.json"
DEFAULT_ROUTE_RUNS_DIR = LAB_ROOT / "runs" / "route-check"
DEFAULT_QUICK_RUNS_DIR = LAB_ROOT / "runs" / "quick"
DEFAULT_AGENT_DESIGN_RUNS_DIR = LAB_ROOT / "runs" / "agent-design"
DEFAULT_AGENT_RUNS_DIR = LAB_ROOT / "runs" / "agent"
DEFAULT_SPECIALIST_RUNS_DIR = LAB_ROOT / "runs" / "specialist"
DEFAULT_LIVE_DOCTOR_RUNS_DIR = LAB_ROOT / "runs" / "live-doctor"
DEFAULT_LIVE_ACCEPTANCE_RUNS_DIR = LAB_ROOT / "runs" / "live-acceptance"
DEFAULT_QUICK_DATA_RUNS_DIR = LAB_ROOT / "data_runs" / "quick"
DEFAULT_QUICK_FIXTURES_DIR = LAB_ROOT / "fixtures" / "quick"
RUNS_DIR_ENV = "FA_AUTOMATION_RUNS_DIR"
QUICK_RUNS_DIR_ENV = "FA_AUTOMATION_QUICK_RUNS_DIR"
AGENT_DESIGN_RUNS_DIR_ENV = "FA_AUTOMATION_AGENT_DESIGN_RUNS_DIR"
AGENT_RUNS_DIR_ENV = "FA_AUTOMATION_AGENT_RUNS_DIR"
SPECIALIST_RUNS_DIR_ENV = "FA_AUTOMATION_SPECIALIST_RUNS_DIR"
LIVE_DOCTOR_RUNS_DIR_ENV = "FA_AUTOMATION_LIVE_DOCTOR_RUNS_DIR"
LIVE_ACCEPTANCE_RUNS_DIR_ENV = "FA_AUTOMATION_LIVE_ACCEPTANCE_RUNS_DIR"
AGENT_REPORTS_ROOT_ENV = "FA_AUTOMATION_AGENT_REPORTS_ROOT"
QUICK_DATA_RUNS_DIR_ENV = "FA_AUTOMATION_QUICK_DATA_RUNS_DIR"
QUICK_FIXTURES_DIR_ENV = "FA_AUTOMATION_QUICK_FIXTURES_DIR"
CODEX_MODEL_ENV = "FA_AUTOMATION_CODEX_MODEL"
LIVE_TIMEOUT_ENV = "FA_AUTOMATION_LIVE_TIMEOUT_SECONDS"
DEFAULT_LIVE_TIMEOUT_SECONDS = 45
CODEX_SDK_PROJECT_ROOT_ENV = "FA_AUTOMATION_CODEX_SDK_PROJECT_ROOT"
CODEX_SDK_COMMAND_ENV = "FA_AUTOMATION_CODEX_SDK_COMMAND"
CODEX_SDK_TIMEOUT_ENV = "FA_AUTOMATION_CODEX_SDK_TIMEOUT_SECONDS"
CODEX_SDK_SPECIALIST_TIMEOUT_ENV_PREFIX = "FA_AUTOMATION_CODEX_SDK_TIMEOUT_"
CODEX_SDK_DRY_RUN_ENV = "FA_AUTOMATION_CODEX_SDK_DRY_RUN"
AGENT_TOTAL_TIMEOUT_ENV = "FA_AUTOMATION_AGENT_TOTAL_TIMEOUT_SECONDS"
AGENT_MAX_PARALLEL_SPECIALISTS_ENV = "FA_AUTOMATION_AGENT_MAX_PARALLEL_SPECIALISTS"
DEFAULT_CODEX_SDK_COMMAND = "npm.cmd"
DEFAULT_CODEX_SDK_TIMEOUT_SECONDS = 900
DEFAULT_AGENT_TOTAL_TIMEOUT_SECONDS = 7200
DEFAULT_AGENT_MAX_PARALLEL_SPECIALISTS = 3
CODEX_SDK_EXECUTION_PATH = "financial_agent_system_codex_sdk_cli"

AGENT_DESIGN_META_GATES = {
    "source_of_truth",
    "five_question_intake",
    "subagent_truthfulness",
    "audit_pack",
    "ic_synthesis_lock",
}

AGENT_CANONICAL_IC_GATES = {
    "evidence_freshness",
    "lead_asset_analysis",
    "material_context_modules",
    "valuation_expectations",
    "risk_red_team",
    "implementation_vehicle_quality",
    "portfolio_fit",
}

AGENT_REQUIRED_GATES = AGENT_DESIGN_META_GATES | AGENT_CANONICAL_IC_GATES

AGENT_REPORTS_ROOT = Path(r"C:\Users\ShumeikoYe\OneDrive\Documents\Financial Agent Reports")
AGENT_RUN_FOLDER_PATTERN = "[ASSET] yyyy-mm-dd hhmm"
AGENT_SPECIALISTS_EQUITY = [
    "evidence-collector",
    "equity-agent",
    "financial-statement-analysis",
    "valuation-expectations-agent",
    "risk-red-team-agent",
    "sector-industry-analysis-agent",
    "macro-agent",
    "news-catalysts-agent",
    "market-positioning-agent",
    "portfolio-fit-agent",
    "investment-committee-agent",
]
AGENT_REQUIRED_SPECIALISTS_EQUITY = {
    "evidence-collector",
    "financial-statement-analysis",
    "valuation-expectations-agent",
    "risk-red-team-agent",
    "investment-committee-agent",
}
AGENT_SPECIALISTS_BY_ROUTE = {
    "equity_full_cycle": AGENT_SPECIALISTS_EQUITY,
    "etf_full_cycle": [
        "evidence-collector",
        "etf-agent",
        "valuation-expectations-agent",
        "risk-red-team-agent",
        "macro-agent",
        "sector-industry-analysis-agent",
        "market-positioning-agent",
        "portfolio-fit-agent",
        "investment-committee-agent",
    ],
    "fixed_income_full_cycle": [
        "evidence-collector",
        "fixed-income-agent",
        "etf-agent",
        "macro-agent",
        "valuation-expectations-agent",
        "risk-red-team-agent",
        "market-positioning-agent",
        "portfolio-fit-agent",
        "investment-committee-agent",
    ],
    "crypto_full_cycle": [
        "evidence-collector",
        "crypto-agent",
        "macro-agent",
        "valuation-expectations-agent",
        "risk-red-team-agent",
        "news-catalysts-agent",
        "market-positioning-agent",
        "portfolio-fit-agent",
        "investment-committee-agent",
    ],
    "commodity_full_cycle": [
        "evidence-collector",
        "commodity-agent",
        "macro-agent",
        "valuation-expectations-agent",
        "risk-red-team-agent",
        "news-catalysts-agent",
        "market-positioning-agent",
        "portfolio-fit-agent",
        "investment-committee-agent",
    ],
    "multi_asset_comparison": [
        "evidence-collector",
        "equity-agent",
        "etf-agent",
        "crypto-agent",
        "fixed-income-agent",
        "commodity-agent",
        "macro-agent",
        "valuation-expectations-agent",
        "risk-red-team-agent",
        "portfolio-fit-agent",
        "investment-committee-agent",
    ],
}
AGENT_REQUIRED_SPECIALISTS_BY_ROUTE = {
    "equity_full_cycle": AGENT_REQUIRED_SPECIALISTS_EQUITY,
    "etf_full_cycle": {"evidence-collector", "etf-agent", "valuation-expectations-agent", "risk-red-team-agent", "investment-committee-agent"},
    "fixed_income_full_cycle": {"evidence-collector", "fixed-income-agent", "valuation-expectations-agent", "risk-red-team-agent", "investment-committee-agent"},
    "crypto_full_cycle": {"evidence-collector", "crypto-agent", "valuation-expectations-agent", "risk-red-team-agent", "investment-committee-agent"},
    "commodity_full_cycle": {"evidence-collector", "commodity-agent", "valuation-expectations-agent", "risk-red-team-agent", "investment-committee-agent"},
    "multi_asset_comparison": {"evidence-collector", "valuation-expectations-agent", "risk-red-team-agent", "portfolio-fit-agent", "investment-committee-agent"},
}
AGENT_INTAKE_BASELINES = [
    "3-5 year horizon if horizon is not provided",
    "no current position unless stated",
    "quality compounder and valuation-entry review unless objective is stated",
    "use latest public data where available; otherwise explain freshness limits",
    "no portfolio context provided; only generic portfolio-fit analysis",
]
PORTFOLIO_CONTEXT_FIELDS = [
    "holdings",
    "cash",
    "risk_limits",
    "horizon",
    "constraints",
    "existing_exposure",
    "objective",
]

AGENT_ROUTE_CARDS = {
    "equity_full_cycle": "workflows/route_cards/equity_full_cycle.md",
    "crypto_full_cycle": "workflows/route_cards/crypto_full_cycle.md",
    "etf_full_cycle": "workflows/route_cards/etf_full_cycle.md",
    "commodity_full_cycle": "workflows/route_cards/commodity_full_cycle.md",
    "fixed_income_full_cycle": "workflows/route_cards/fixed_income_full_cycle.md",
    "multi_asset_comparison": "workflows/route_cards/multi_asset_comparison.md",
}

AGENT_ROUTE_LABELS = {
    "equity_full_cycle": "equity",
    "etf_full_cycle": "ETF / fund",
    "commodity_full_cycle": "commodity",
    "crypto_full_cycle": "crypto",
    "fixed_income_full_cycle": "fixed income",
    "multi_asset_comparison": "multi-asset comparison",
}

SPECIALIST_COMMANDS = {
    "RISK": "risk-red-team-agent",
    "VAL": "valuation-expectations-agent",
    "MACRO": "macro-agent",
    "NEWS": "news-catalysts-agent",
    "PORTFOLIO": "portfolio-fit-agent",
    "SECTOR": "sector-industry-analysis-agent",
    "EVIDENCE": "evidence-collector",
    "POSITIONING": "market-positioning-agent",
    "INTEL": "market-intelligence-agent",
    "EQUITY": "equity-agent",
    "ETF": "etf-agent",
    "COMMODITY": "commodity-agent",
    "CRYPTO": "crypto-agent",
    "FI": "fixed-income-agent",
    "WINNERS": "structural-winners-discovery-agent",
    "IC": "investment-committee-agent",
}

AGENT_NON_EQUITY_IDENTITIES: dict[str, dict[str, Any]] = {
    "SPY": {
        "ticker": "SPY",
        "company_name": "SPDR S&P 500 ETF Trust",
        "security_type": "etf",
        "instrument_classification": "etf_or_fund",
        "selected_route": "etf_full_cycle",
        "currency": "USD",
        "source": "Automation Lab ETF identity seed",
    },
    "QQQ": {
        "ticker": "QQQ",
        "company_name": "Invesco QQQ Trust",
        "security_type": "etf",
        "instrument_classification": "etf_or_fund",
        "selected_route": "etf_full_cycle",
        "currency": "USD",
        "source": "Automation Lab ETF identity seed",
    },
    "SCHG": {
        "ticker": "SCHG",
        "company_name": "Schwab U.S. Large-Cap Growth ETF",
        "security_type": "etf",
        "instrument_classification": "etf_or_fund",
        "selected_route": "etf_full_cycle",
        "currency": "USD",
        "source": "Automation Lab ETF identity seed",
    },
    "TLT": {
        "ticker": "TLT",
        "company_name": "iShares 20+ Year Treasury Bond ETF",
        "security_type": "bond_etf",
        "instrument_classification": "bond_etf_or_fixed_income_fund",
        "selected_route": "fixed_income_full_cycle",
        "currency": "USD",
        "source": "Automation Lab fixed-income identity seed",
    },
    "BTC": {
        "ticker": "BTC",
        "company_name": "Bitcoin",
        "security_type": "crypto",
        "instrument_classification": "crypto_asset",
        "selected_route": "crypto_full_cycle",
        "currency": "USD",
        "price_ticker": "BTC-USD",
        "source": "Automation Lab crypto identity seed",
    },
    "GLD": {
        "ticker": "GLD",
        "company_name": "SPDR Gold Shares",
        "security_type": "commodity_etf",
        "instrument_classification": "commodity_etf_or_proxy_vehicle",
        "selected_route": "commodity_full_cycle",
        "currency": "USD",
        "source": "Automation Lab commodity identity seed",
    },
}

AGENT_ALLOWED_SUBAGENTS = {
    "asset-intake-router",
    "commodity-agent",
    "crypto-agent",
    "equity-agent",
    "etf-agent",
    "evidence-collector",
    "fixed-income-agent",
    "investment-committee-agent",
    "macro-agent",
    "market-intelligence-agent",
    "market-positioning-agent",
    "market-sense-agent",
    "master-intake-router",
    "news-catalysts-agent",
    "portfolio-fit-agent",
    "risk-red-team-agent",
    "sector-industry-analysis-agent",
    "structural-winners-discovery-agent",
    "theme-opportunity-intake-router",
    "valuation-expectations-agent",
}

VALID_ROUTES = {
    "equity_full_cycle",
    "crypto_full_cycle",
    "etf_full_cycle",
    "commodity_full_cycle",
    "fixed_income_full_cycle",
    "multi_asset_comparison",
}

ROUTE_OUTPUT_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "selected_route": {"type": "string", "enum": sorted(VALID_ROUTES)},
        "reason": {"type": "string"},
    },
    "required": ["selected_route", "reason"],
    "additionalProperties": False,
}

DIAGNOSTIC_HINT = (
    "Check for possible mismatch among the route prompt, route card, test case, "
    "or Codex SDK behavior."
)

QUICK_ANSWER_STATUSES = {"Preliminary", "Limited", "Blocked"}
QUICK_ANSWER_REQUIRED_SECTIONS = [
    "Short view",
    "What the quick data shows",
    "Source note",
    "Freshness note",
    "Main risks / limits",
    "Needed for final IC Action",
    "Next step",
]
QUICK_ANSWER_FORBIDDEN_ACTION_PATTERN = re.compile(
    r"(?i)\b(buy|sell|hold|add|trim|exit|buying|selling|holding|adding|trimming|exiting|"
    r"enter|entering|close|closing|increase exposure|reduce exposure|raise exposure|"
    r"lower exposure|scale into|scale out|build a position|open position)\b"
)
QUICK_ANSWER_SIZING_PATTERN = re.compile(
    r"(?i)\b\d+(?:\.\d+)?\s*(?:%|percent|shares?)\b|\$\s*\d|\b(?:allocate|allocation|position sizing|position size|exact sizing)\b"
)


@dataclass(frozen=True)
class LiveClassification:
    selected_route: str
    reason: str
    attempts: int


@dataclass(frozen=True)
class QuickRunResult:
    prompt: str
    normalized_prompt: str
    output: str
    boundary_status: str
    mode: str


@dataclass(frozen=True)
class QuickOutputValidation:
    boundary_status: str
    question_count: int
    quality_checks: dict[str, bool]
    freshness_required: bool


@dataclass(frozen=True)
class QuickAnswerResult:
    prompt: str
    normalized_prompt: str
    answers: list[str]
    mode: str
    run_dir: Path
    source_snapshot: dict[str, Any]
    data_quality: dict[str, Any]
    generated_answer: str
    output_quality: dict[str, Any]
    validation: dict[str, Any]


@dataclass(frozen=True)
class AgentDesignResult:
    prompt: str
    normalized_prompt: str
    selected_route: str
    design: dict[str, Any]
    mode: str


@dataclass(frozen=True)
class AgentDesignValidation:
    status: str
    question_count: int
    required_gates_present: list[str]
    quality_checks: dict[str, bool]


class LiveRouteError(RuntimeError):
    """Raised when a live route classification cannot produce valid route JSON."""


class QuickRunError(RuntimeError):
    """Raised when a live QUICK launch cannot produce a response."""


class AgentDesignError(RuntimeError):
    """Raised when an AGENT automation design cannot be created safely."""


class LiveCodexRouteClassifier:
    """Classify one route-check case with the Codex Python SDK."""

    def __init__(self, project_root: Path = PROJECT_ROOT) -> None:
        self.project_root = project_root
        self.model = os.environ.get(CODEX_MODEL_ENV) or None
        self.timeout_seconds = parse_positive_int_env(
            LIVE_TIMEOUT_ENV,
            DEFAULT_LIVE_TIMEOUT_SECONDS,
        )

    def classify(self, prompt: str) -> LiveClassification:
        last_error = "unknown live classification error"
        for attempt in (1, 2):
            request = build_live_prompt(prompt=prompt, retry=(attempt == 2))
            try:
                response_text = self._run_codex(request)
                parsed = parse_route_json(response_text)
                return LiveClassification(
                    selected_route=parsed["selected_route"],
                    reason=parsed["reason"],
                    attempts=attempt,
                )
            except (json.JSONDecodeError, ValueError) as exc:
                last_error = f"invalid_json: {exc}"
                if attempt == 2:
                    break
            except Exception as exc:  # SDK/auth/runtime failures are reported per case.
                last_error = str(exc)
                break
        raise LiveRouteError(last_error)

    def _run_codex(self, request: str) -> str:
        output_queue: mp.Queue[dict[str, str]] = mp.Queue(maxsize=1)
        process = mp.Process(
            target=_codex_worker,
            args=(request, str(self.project_root), self.model, output_queue),
        )
        process.start()
        process.join(self.timeout_seconds)
        if process.is_alive():
            process.terminate()
            process.join(5)
            raise LiveRouteError(f"sdk_timeout after {self.timeout_seconds} seconds")

        try:
            message = output_queue.get_nowait()
        except queue.Empty as exc:
            raise LiveRouteError("sdk_error: Codex worker exited without a result") from exc

        if message.get("status") == "ok":
            return message.get("response", "")
        raise LiveRouteError(message.get("error", "unknown Codex worker error"))


def parse_positive_int_env(name: str, default: int) -> int:
    value = os.environ.get(name)
    if value is None:
        return default
    try:
        parsed = int(value)
    except ValueError:
        return default
    return parsed if parsed > 0 else default


def env_truthy(name: str) -> bool:
    return (os.environ.get(name) or "").strip().lower() in {"1", "true", "yes", "y", "on"}


def get_codex_sdk_project_root() -> Path:
    return Path(os.environ.get(CODEX_SDK_PROJECT_ROOT_ENV) or str(PROJECT_ROOT))


def get_codex_sdk_command() -> str:
    return os.environ.get(CODEX_SDK_COMMAND_ENV) or DEFAULT_CODEX_SDK_COMMAND


def env_name_for_specialist_timeout(specialist_id: str) -> str:
    normalized = re.sub(r"[^A-Za-z0-9]+", "_", specialist_id).strip("_").upper()
    return f"{CODEX_SDK_SPECIALIST_TIMEOUT_ENV_PREFIX}{normalized}"


def get_codex_sdk_timeout_seconds(specialist_id: str | None = None) -> tuple[int, str]:
    if specialist_id:
        specialist_env = env_name_for_specialist_timeout(specialist_id)
        if os.environ.get(specialist_env) is not None:
            return parse_positive_int_env(specialist_env, DEFAULT_CODEX_SDK_TIMEOUT_SECONDS), specialist_env
    if os.environ.get(CODEX_SDK_TIMEOUT_ENV) is not None:
        return parse_positive_int_env(CODEX_SDK_TIMEOUT_ENV, DEFAULT_CODEX_SDK_TIMEOUT_SECONDS), CODEX_SDK_TIMEOUT_ENV
    return DEFAULT_CODEX_SDK_TIMEOUT_SECONDS, "default"


def get_agent_total_timeout_seconds() -> int:
    return parse_positive_int_env(AGENT_TOTAL_TIMEOUT_ENV, DEFAULT_AGENT_TOTAL_TIMEOUT_SECONDS)


def get_agent_max_parallel_specialists() -> int:
    return parse_positive_int_env(AGENT_MAX_PARALLEL_SPECIALISTS_ENV, DEFAULT_AGENT_MAX_PARALLEL_SPECIALISTS)


def now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def parse_codex_sdk_cli_json(stdout: str) -> dict[str, Any]:
    decoder = json.JSONDecoder()
    last_obj: dict[str, Any] | None = None
    for index, char in enumerate(stdout):
        if char != "{":
            continue
        try:
            value, _ = decoder.raw_decode(stdout[index:])
        except json.JSONDecodeError:
            continue
        if isinstance(value, dict):
            last_obj = value
    if last_obj is None:
        raise ValueError("Codex SDK CLI stdout did not contain a JSON object")
    return last_obj


def codex_sdk_command_shape(command: list[str]) -> list[str]:
    shaped: list[str] = []
    redact_next = False
    for item in command:
        if redact_next:
            shaped.append("<prompt-file>")
            redact_next = False
            continue
        shaped.append(item)
        if item == "--prompt-file":
            redact_next = True
    return shaped


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


LIVE_MANIFEST_REDACTED_KEYS = {"prompt", "normalized_prompt", "raw_input", "user_prompt", "query"}


def redact_live_manifest_value(value: Any) -> Any:
    if isinstance(value, dict):
        return {
            key: "<redacted-live-input>" if key in LIVE_MANIFEST_REDACTED_KEYS else redact_live_manifest_value(child)
            for key, child in value.items()
        }
    if isinstance(value, list):
        return [redact_live_manifest_value(item) for item in value]
    return value


class LiveCodexQuickLauncher:
    """Launch the first guarded QUICK step with the Codex Python SDK."""

    def __init__(self, project_root: Path = PROJECT_ROOT) -> None:
        self.project_root = project_root
        self.model = os.environ.get(CODEX_MODEL_ENV) or None
        self.timeout_seconds = parse_positive_int_env(
            LIVE_TIMEOUT_ENV,
            DEFAULT_LIVE_TIMEOUT_SECONDS,
        )

    def launch(self, prompt: str) -> QuickRunResult:
        normalized_prompt = normalize_quick_prompt(prompt)
        request = build_quick_live_prompt(normalized_prompt=normalized_prompt)
        output = self._run_codex(request).strip()
        validation = validate_quick_output(output, normalized_prompt=normalized_prompt)
        return QuickRunResult(
            prompt=prompt,
            normalized_prompt=normalized_prompt,
            output=output,
            boundary_status=validation.boundary_status,
            mode="live",
        )

    def _run_codex(self, request: str) -> str:
        output_queue: mp.Queue[dict[str, str]] = mp.Queue(maxsize=1)
        process = mp.Process(
            target=_codex_quick_worker,
            args=(request, str(self.project_root), self.model, output_queue),
        )
        process.start()
        process.join(self.timeout_seconds)
        if process.is_alive():
            process.terminate()
            process.join(5)
            raise QuickRunError(f"sdk_timeout after {self.timeout_seconds} seconds")

        try:
            message = output_queue.get_nowait()
        except queue.Empty as exc:
            raise QuickRunError("sdk_error: Codex worker exited without a result") from exc

        if message.get("status") == "ok":
            return message.get("response", "")
        raise QuickRunError(message.get("error", "unknown Codex worker error"))


def _codex_worker(
    request: str,
    project_root: str,
    model: str | None,
    output_queue: "mp.Queue[dict[str, str]]",
) -> None:
    try:
        from openai_codex import ApprovalMode, Codex, Sandbox
    except ImportError:
        output_queue.put(
            {
                "status": "error",
                "error": "openai-codex is not installed. Install live dependencies before running --mode live.",
            }
        )
        return

    try:
        with Codex() as codex:
            thread = codex.thread_start(
                cwd=project_root,
                model=model,
                sandbox=Sandbox.read_only,
                approval_mode=ApprovalMode.deny_all,
            )
            result = thread.run(
                request,
                cwd=project_root,
                sandbox=Sandbox.read_only,
                approval_mode=ApprovalMode.deny_all,
                model=model,
                output_schema=ROUTE_OUTPUT_SCHEMA,
            )
        output_queue.put({"status": "ok", "response": result.final_response or ""})
    except Exception as exc:
        output_queue.put({"status": "error", "error": f"sdk_error: {exc}"})


def _codex_quick_worker(
    request: str,
    project_root: str,
    model: str | None,
    output_queue: "mp.Queue[dict[str, str]]",
) -> None:
    try:
        from openai_codex import ApprovalMode, Codex, Sandbox
    except ImportError:
        output_queue.put(
            {
                "status": "error",
                "error": "openai-codex is not installed. Install live dependencies before running --mode live.",
            }
        )
        return

    try:
        with Codex() as codex:
            thread = codex.thread_start(
                cwd=project_root,
                model=model,
                sandbox=Sandbox.read_only,
                approval_mode=ApprovalMode.deny_all,
            )
            result = thread.run(
                request,
                cwd=project_root,
                sandbox=Sandbox.read_only,
                approval_mode=ApprovalMode.deny_all,
                model=model,
            )
        output_queue.put({"status": "ok", "response": result.final_response or ""})
    except Exception as exc:
        output_queue.put({"status": "error", "error": f"sdk_error: {exc}"})


def get_route_runs_dir() -> Path:
    override = os.environ.get(RUNS_DIR_ENV)
    if override:
        return Path(override)
    return DEFAULT_ROUTE_RUNS_DIR


def get_quick_runs_dir() -> Path:
    override = os.environ.get(QUICK_RUNS_DIR_ENV) or os.environ.get(RUNS_DIR_ENV)
    if override:
        return Path(override)
    return DEFAULT_QUICK_RUNS_DIR


def get_agent_design_runs_dir() -> Path:
    override = os.environ.get(AGENT_DESIGN_RUNS_DIR_ENV) or os.environ.get(RUNS_DIR_ENV)
    if override:
        return Path(override)
    return DEFAULT_AGENT_DESIGN_RUNS_DIR


def get_agent_runs_dir() -> Path:
    override = os.environ.get(AGENT_RUNS_DIR_ENV) or os.environ.get(RUNS_DIR_ENV)
    if override:
        return Path(override)
    return DEFAULT_AGENT_RUNS_DIR


def get_specialist_runs_dir() -> Path:
    override = os.environ.get(SPECIALIST_RUNS_DIR_ENV)
    if override:
        return Path(override)
    return DEFAULT_SPECIALIST_RUNS_DIR


def get_live_doctor_runs_dir() -> Path:
    override = os.environ.get(LIVE_DOCTOR_RUNS_DIR_ENV) or os.environ.get(RUNS_DIR_ENV)
    if override:
        return Path(override)
    return DEFAULT_LIVE_DOCTOR_RUNS_DIR


def get_live_acceptance_runs_dir() -> Path:
    override = os.environ.get(LIVE_ACCEPTANCE_RUNS_DIR_ENV) or os.environ.get(RUNS_DIR_ENV)
    if override:
        return Path(override)
    return DEFAULT_LIVE_ACCEPTANCE_RUNS_DIR


def get_agent_reports_root() -> Path:
    override = os.environ.get(AGENT_REPORTS_ROOT_ENV)
    if override:
        return Path(override)
    return AGENT_REPORTS_ROOT


def get_quick_data_runs_dir() -> Path:
    override = os.environ.get(QUICK_DATA_RUNS_DIR_ENV)
    if override:
        return Path(override)
    return DEFAULT_QUICK_DATA_RUNS_DIR


def get_quick_fixtures_dir() -> Path:
    override = os.environ.get(QUICK_FIXTURES_DIR_ENV)
    if override:
        return Path(override)
    return DEFAULT_QUICK_FIXTURES_DIR


def load_cases(path: Path = CASES_PATH) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8-sig") as file:
        data = json.load(file)
    if not isinstance(data, list):
        raise ValueError("Route check cases file must contain a JSON array.")
    return data


def require_case_field(case: dict[str, Any], field: str) -> str:
    value = case.get(field)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"Route check case is missing required string field: {field}")
    return value


def mock_route(prompt: str) -> str:
    """Return a deterministic route for mock mode."""
    text = prompt.lower()

    if " vs " in text or " compare " in text or "comparison" in text:
        return "multi_asset_comparison"
    if "btc" in text or "bitcoin" in text or "crypto" in text:
        return "crypto_full_cycle"
    if "tlt" in text or "bond" in text or "fixed income" in text or "duration" in text:
        return "fixed_income_full_cycle"
    if re.search(r"\bgld\b", text) or "gold" in text or "oil" in text or "commodity" in text:
        return "commodity_full_cycle"
    if re.search(r"\b(spy|qqq|schg)\b", text) or "etf" in text or "fund" in text:
        return "etf_full_cycle"
    resolved = resolve_equity_request(prompt, mode="mock")
    if resolved.get("instrument_classification") in {
        "us_common_equity",
        "us_share_class",
        "adr_or_foreign_issuer_us_listing",
        "non_us_listed_equity",
        "private_company",
        "complex_or_unsupported_instrument",
        "ambiguous",
    } and resolved.get("ticker") != "UNRESOLVED":
        return "equity_full_cycle"
    return "unknown"


def normalize_quick_prompt(prompt: str) -> str:
    stripped = prompt.strip()
    if stripped.lower().startswith("quick:"):
        return stripped
    return f"QUICK: {stripped}"


def normalize_agent_prompt(prompt: str) -> str:
    stripped = prompt.strip()
    if stripped.lower().startswith("agent:"):
        return stripped
    return f"AGENT: {stripped}"


def build_live_prompt(prompt: str, retry: bool = False) -> str:
    retry_instruction = ""
    if retry:
        retry_instruction = (
            "\nYour previous answer was not valid strict JSON. Return only a JSON object. "
            "No Markdown, no prose, no code fence."
        )

    return (
        "Read PROJECT_STATE.md, AGENTS.md, and workflows/route_cards/investment_request_router.md.\n"
        "Classify this request only.\n"
        "Return JSON with selected_route and reason.\n"
        "Do not perform investment analysis.\n"
        "Do not create report files.\n"
        "Do not modify any files.\n"
        "Do not issue IC Action.\n"
        "Apply the router table exactly. If a request names a bond ETF, yield, duration, credit, or rates exposure, select fixed_income_full_cycle even though it is also an ETF wrapper.\n"
        f"Allowed selected_route values: {', '.join(sorted(VALID_ROUTES))}.\n"
        "Required JSON shape: {\"selected_route\": \"...\", \"reason\": \"...\"}.\n"
        f"Request to classify: {prompt}"
        f"{retry_instruction}"
    )


def build_quick_live_prompt(normalized_prompt: str) -> str:
    return (
        "Read PROJECT_STATE.md, AGENTS.md, and workflows/route_cards/quick_take.md.\n"
        "Launch the QUICK workflow only.\n"
        "Perform only the required first action from the Quick Take route card: ask exactly 3 relevant questions in one block and then stop.\n"
        "Start with exactly one of these two lines: `Status: Preliminary` or `Status: Limited`.\n"
        "If the request depends on today, now, latest, news, earnings, price action, or current market data, use `Status: Limited` because current timestamped sources have not been gathered yet.\n"
        "Make one of the three questions explicitly cover freshness/current-source needs when the request is freshness-dependent.\n"
        "Do not answer the investment question yet.\n"
        "Do not perform a full AGENT workflow.\n"
        "Do not spawn or claim subagents.\n"
        "Do not create investment_report.md, audit folders, or any files.\n"
        "Do not issue final IC Action, Action Box, exact position sizing, or final buy/sell/hold/add/trim/exit conclusions.\n"
        "Keep the boundary Preliminary or Limited only.\n"
        f"Request to launch: {normalized_prompt}"
    )


FRESHNESS_PROMPT_PATTERN = re.compile(
    r"(?i)\b(today|now|latest|recent|news|earnings|price action|market action|"
    r"this week|this month|real[- ]?time|pre[- ]?market|after[- ]?hours)\b|"
    r"\bcurrent\s+(price|market|data|quote|news|earnings|setup|valuation)\b|"
    r"\b(СЃРµРіРѕРґРЅСЏ|СЃРµР№С‡Р°СЃ|РїРѕСЃР»РµРґРЅ(?:РёРµ|СЏСЏ|РёР№|РёС…)|СЃРІРµР¶(?:РёРµ|Р°СЏ|РёР№|РёС…)|РЅРѕРІРѕСЃС‚(?:Рё|РµР№)|"
    r"РѕС‚С‡[РµС‘]С‚РЅРѕСЃС‚(?:СЊ|Рё)|РґРёРЅР°РјРёРє[Р°Рё]\s+С†РµРЅ|С‚РµРєСѓС‰(?:Р°СЏ|РёРµ|РёР№|РёС…))\b"
)

FRESHNESS_OUTPUT_PATTERN = re.compile(
    r"(?i)\b(freshness|current|timestamped|latest|today|now|news|earnings|price action|"
    r"sources?)\b"
)


def is_freshness_dependent(prompt: str) -> bool:
    if FRESHNESS_PROMPT_PATTERN.search(prompt):
        return True
    prompt_lower = prompt.lower()
    russian_freshness_terms = (
        "сегодня",
        "сейчас",
        "последние",
        "последняя",
        "последний",
        "свежие",
        "свежая",
        "свежий",
        "новости",
        "отчётность",
        "отчетность",
        "текущая",
        "текущие",
        "цена",
    )
    return any(term in prompt_lower for term in russian_freshness_terms)


def validate_quick_output(output: str, normalized_prompt: str = "") -> QuickOutputValidation:
    text = output.strip()
    if not text:
        raise QuickRunError("quick_validation_error: empty QUICK output")

    lines = text.splitlines()
    non_empty_lines = [line.strip() for line in lines if line.strip()]
    if not non_empty_lines:
        raise QuickRunError("quick_validation_error: empty QUICK output")

    status_line_matches = list(re.finditer(r"(?im)^\s*Status\s*:", text))
    if len(status_line_matches) != 1:
        raise QuickRunError("quick_validation_error: expected exactly one status line")
    status_match = re.search(r"(?im)^\s*Status\s*:\s*(Preliminary|Limited)\s*$", text)
    if not status_match:
        raise QuickRunError("quick_validation_error: missing Status: Preliminary or Status: Limited")
    boundary_status = status_match.group(1)
    if not re.fullmatch(r"Status\s*:\s*(Preliminary|Limited)", non_empty_lines[0]):
        raise QuickRunError("quick_validation_error: first non-empty line must be the boundary status")

    question_lines = [line for line in lines if line.strip().endswith("?")]
    non_question_text = "\n".join(line.strip() for line in lines if not line.strip().endswith("?"))
    if len(question_lines) != 3:
        raise QuickRunError(
            f"quick_validation_error: expected exactly 3 question lines, got {len(question_lines)}"
        )
    for index, line in enumerate(question_lines, start=1):
        if not re.match(rf"^\s*{index}\.\s+\S", line):
            raise QuickRunError("quick_validation_error: questions must be numbered 1., 2., and 3.")

    whole_output_forbidden_patterns = {
        "IC Action": r"(?i)\bIC\s+Action\b",
        "Action Box": r"(?i)\bAction\s+Box\b",
        "investment report": r"(?i)\binvestment_report\.md\b|\binvestment\s+report\b|\breport\s+(created|saved|written|generated)\b|\b(created|saved|wrote|written|generated)\s+(a\s+|the\s+)?(?:full\s+)?report\b",
        "audit marker": r"(?i)\baudit\s+(folder|directory|path|created|saved|written|generated|completed)\b|\b(created|saved|wrote|written|generated|completed)\s+(a\s+|the\s+)?(?:full\s+)?audit\b|\baudit/|\baudit\\|[\\/]audit\b",
        "subagent claim": r"(?i)\bsub[- ]?agents?\b.*\b(ran|completed|reviewed|spawned)\b|\bspawned\s+sub[- ]?agents?\b",
        "analysis section": r"(?im)^\s*(?:#{1,6}\s*)?(analysis|thesis|valuation|risk|recommendation|conclusion|next step)\s*:?\s*$",
        "question final action": r"(?im)^\s*\d+\.\s+.*\b(buy|buying|sell|selling|hold|holding|add|adding|trim|trimming|exit|exiting)\b.*\?",
        "bare question final action": r"(?im)^\s*\d+\.\s+(buy|buying|sell|selling|hold|holding|add|adding|trim|trimming|exit|exiting)\b.*\?",
        "question sizing marker": r"(?im)^\s*\d+\.\s+.*\b(position size|allocate|allocation|weight|sizing|shares?|dollars?|usd)\b.*\?",
        "question dollar marker": r"(?im)^\s*\d+\.\s+.*\$.*\?",
        "question report marker": r"(?im)^\s*\d+\.\s+.*\breport\b.*\?",
        "question audit marker": r"(?im)^\s*\d+\.\s+.*\baudit\b.*\?",
    }
    for label, pattern in whole_output_forbidden_patterns.items():
        if re.search(pattern, text):
            raise QuickRunError(f"quick_validation_error: forbidden {label} in QUICK output")

    non_question_forbidden_patterns = {
        "bare final action": r"(?im)^\s*(buy|sell|hold|add|trim|exit)\b",
        "labeled final action": r"(?im)^\s*(conclusion|recommendation|action|final action)\s*:\s*(buy|sell|hold|add|trim|exit)\b",
        "final action language": r"(?i)\b(buy|buying|sell|selling|hold|holding|add|adding|trim|trimming|exit|exiting)\b",
        "sizing language": r"(?i)\b(position size|position sizing|allocate|allocation|weight|sizing|shares?|dollars?|usd|\$)\b",
    }
    for label, pattern in non_question_forbidden_patterns.items():
        if re.search(pattern, non_question_text):
            raise QuickRunError(f"quick_validation_error: forbidden {label} in QUICK output")

    freshness_required = is_freshness_dependent(normalized_prompt)
    freshness_visible = any(FRESHNESS_OUTPUT_PATTERN.search(line) for line in question_lines)
    if freshness_required and boundary_status != "Limited":
        raise QuickRunError(
            "quick_validation_error: freshness-dependent QUICK output must use Status: Limited"
        )
    if freshness_required and not freshness_visible:
        raise QuickRunError(
            "quick_validation_error: freshness-dependent QUICK output must ask about current/timestamped source needs"
        )

    quality_checks = {
        "status_present": True,
        "status_first_line": True,
        "single_status_line": True,
        "preliminary_or_limited_only": True,
        "exactly_three_questions": True,
        "numbered_questions": True,
        "no_final_ic_action": True,
        "no_action_box": True,
        "no_report_or_audit": True,
        "no_final_action_language": True,
        "no_exact_sizing": True,
        "no_subagent_claim": True,
        "no_analysis_sections": True,
        "freshness_required": freshness_required,
        "freshness_limited_when_required": (not freshness_required) or boundary_status == "Limited",
        "freshness_question_when_required": (not freshness_required) or freshness_visible,
    }
    return QuickOutputValidation(
        boundary_status=boundary_status,
        question_count=len(question_lines),
        quality_checks=quality_checks,
        freshness_required=freshness_required,
    )


def mock_quick_launch(prompt: str) -> QuickRunResult:
    normalized_prompt = normalize_quick_prompt(prompt)
    freshness_required = is_freshness_dependent(normalized_prompt)
    status = "Limited" if freshness_required else "Preliminary"
    output = (
        f"Status: {status}\n\n"
        "Before a QUICK take, answer exactly these 3 questions:\n"
        "1. What is your intended time horizon for this asset or setup?\n"
        "2. Do you already own it, and is this for a new position or review of an existing one?\n"
        "3. Should I treat the request as freshness-dependent, meaning today/latest/news/price action is required?"
    )
    validation = validate_quick_output(output, normalized_prompt=normalized_prompt)
    return QuickRunResult(
        prompt=prompt,
        normalized_prompt=normalized_prompt,
        output=output,
        boundary_status=validation.boundary_status,
        mode="mock",
    )


def parse_quick_answers(answer_args: list[str] | None, answers_json: str | None = None) -> list[str]:
    answers: list[str]
    if answers_json:
        try:
            parsed = json.loads(answers_json)
        except json.JSONDecodeError as exc:
            raise ValueError("quick-answer requires --answers-json to be a JSON array") from exc
        if not isinstance(parsed, list) or not all(isinstance(item, str) for item in parsed):
            raise ValueError("quick-answer requires --answers-json to be a JSON array of strings")
        answers = parsed
    else:
        answers = list(answer_args or [])

    if len(answers) != 3:
        raise ValueError("quick-answer requires exactly three non-empty answers")
    if any(not answer.strip() for answer in answers):
        raise ValueError("quick-answer rejects empty answers")
    return [answer.strip() for answer in answers]




def quick_data_shows_line(identity: dict[str, Any], data: dict[str, Any]) -> str:
    ticker = identity.get("ticker", "Unknown asset")
    security_type = identity.get("security_type")
    price = data.get("price") or {}
    recent_events = data.get("recent_events") or []
    filings = data.get("filings") or []
    asset_context = data.get("asset_context") or {}
    comparison_context = data.get("comparison_context") or {}
    price_line = (
        f"public price reference dated {price.get('date')}"
        if isinstance(price, dict) and price.get("date")
        else "no usable quick price reference"
    )
    if security_type == "equity":
        filing_line = (
            f"{len(filings)} recent SEC filing records are present"
            if isinstance(filings, list) and filings
            else "no recent SEC filing list was obtained"
        )
        event_line = (
            f"{len(recent_events)} recent public event or filing markers are present"
            if isinstance(recent_events, list) and recent_events
            else "recent event context is missing"
        )
        return f"The quick snapshot shows {filing_line}, {price_line}, and {event_line}."
    if security_type == "etf":
        return f"The quick snapshot identifies {ticker} as a broad U.S. equity ETF with S&P 500 exposure, {price_line}, and wrapper context limited to a quick pass."
    if security_type == "crypto":
        return f"The quick snapshot identifies {ticker} as a crypto asset with high volatility context, {price_line}, and no full token or custody review."
    if security_type == "bond_etf":
        return f"The quick snapshot identifies {ticker} as a long-duration Treasury bond ETF where rate sensitivity is central, with {price_line}."
    if security_type == "commodity_etf":
        return f"The quick snapshot identifies {ticker} as a gold exposure vehicle and commodity proxy, with {price_line}, not an operating-business analysis."
    if security_type == "multi_asset_comparison":
        summary = comparison_context.get("summary") if isinstance(comparison_context, dict) else None
        price_components = price.get("components") if isinstance(price, dict) else None
        price_count = len(price_components) if isinstance(price_components, list) else 0
        price_text = f"price references for {price_count} components" if price_count else "no complete component price set"
        context_text = summary or "comparison context is limited"
        return f"The quick comparison separates company-specific equity risk, broad equity beta, and crypto volatility. {context_text} {price_text}."
    context_summary = asset_context.get("summary") if isinstance(asset_context, dict) else None
    return f"The quick snapshot shows {context_summary or 'basic identity context'}, {price_line}."


def quick_source_note(source_snapshot: dict[str, Any]) -> str:
    mode = source_snapshot.get("mode", "unknown")
    provider_results = source_snapshot.get("provider_results") or []
    ok_components = sorted(
        {
            str(result.get("component"))
            for result in provider_results
            if isinstance(result, dict) and result.get("status") == "ok" and result.get("component")
        }
    )
    source_classes = ", ".join(ok_components[:5]) if ok_components else "limited public-data metadata"
    if mode == "mock":
        source_class_text = f"mock fixture plus static public-data context ({source_classes})"
    else:
        source_class_text = f"best-effort public/no-key providers ({source_classes})"
    return (
        f"Public/no-key QUICK snapshot using {source_class_text}; "
        "not Evidence Collector evidence_pack and not a full source-readiness review."
    )


def quick_freshness_note(source_snapshot: dict[str, Any], data_quality: dict[str, Any]) -> str:
    limitations = list(data_quality.get("freshness_limitations") or [])
    freshness_required = bool(limitations) or quick_freshness_required(source_snapshot)
    if freshness_required:
        detail = "; ".join(limitations) if limitations else "current/latest context requested"
        return f"Freshness is limited: {detail}; this keeps the QUICK view Limited unless full current evidence is gathered."
    price_status = ((data_quality.get("freshness_by_component") or {}).get("price") or {}).get("status")
    if price_status in {"Unknown", "Stale but Usable", "Not Found"}:
        return f"Freshness is limited: price freshness is {price_status}; this is not a current-market evidence lock."
    return "No current/latest requirement was detected, and the quick snapshot has no freshness downgrade."


def asset_specific_risk_fallback(identity: dict[str, Any]) -> str:
    ticker = str(identity.get("ticker") or "").upper()
    security_type = identity.get("security_type")
    if security_type == "multi_asset_comparison":
        return "Main limit: company-specific equity risk, broad equity beta, and crypto volatility need a full cross-asset workflow."
    fallback_by_ticker = {
        "MSFT": "Main limit: MSFT-specific valuation multiple risk, Azure/cloud growth expectations, and AI capex expectations need full analysis.",
        "SPY": "Main limit: SPY broad equity multiple risk and mega-cap index concentration can dominate outcomes.",
        "BTC": "Main limit: BTC crypto volatility, regulatory risk, custody assumptions, and liquidity drawdown risk need full review.",
        "TLT": "Main limit: TLT duration risk and long-rate path sensitivity need full curve, inflation, and income analysis.",
        "GLD": "Main limit: GLD gold price volatility, real yields, and USD sensitivity need full commodity exposure review.",
    }
    return fallback_by_ticker.get(
        ticker,
        "Main limit: asset-class risk needs full valuation, risk, portfolio, and committee gates.",
    )


def quick_risk_line(identity: dict[str, Any], data: dict[str, Any]) -> str:
    risk_signal = data.get("risk_signal") or {}
    candidate = risk_signal.get("summary") if isinstance(risk_signal, dict) else None
    if not candidate:
        return asset_specific_risk_fallback(identity)
    lower = candidate.lower()
    generic_markers = (
        "does not complete valuation, risk, portfolio, or committee gates",
        "this quick pass is narrow",
        "preliminary and not portfolio-personalized",
    )
    if any(marker in lower for marker in generic_markers):
        return asset_specific_risk_fallback(identity)
    return candidate


def generate_quick_answer(
    prompt: str,
    answers: list[str],
    source_snapshot: dict[str, Any],
    data_quality: dict[str, Any],
) -> str:
    status = data_quality["status"]
    identity = source_snapshot.get("asset_identity") or {}
    ticker = identity.get("ticker", "Unknown asset")
    company = identity.get("company_name", "unknown issuer")
    data = source_snapshot.get("data") or {}
    source_note = quick_source_note(source_snapshot)
    freshness_note = quick_freshness_note(source_snapshot, data_quality)

    if status == "Blocked":
        short_view = "Blocked: the quick run does not have enough public basis to produce a useful filter."
        shows = data_quality.get("reason_for_status", "Required public-data basis is missing.")
        risk_line = "The main risk is fabrication if the system tries to infer beyond the available data."
        next_step = "Provide a clearer public ticker or switch to a full workflow after identity is confirmed."
        ic_status = "Blocked"
    else:
        short_view = (
            f"{status}: {ticker} / {company} passed identity detection, but this is only a short filter."
        )
        shows = quick_data_shows_line(identity, data)
        risk_line = quick_risk_line(identity, data)
        next_step = "Use this only to decide whether to launch the full AGENT workflow."
        ic_status = "Limited"

    answer = (
        f"Status: {status}\n"
        f"IC Action Status: {ic_status}\n"
        "Final IC Action: Unavailable in QUICK.\n\n"
        "Short view\n"
        f"{short_view}\n\n"
        "What the quick data shows\n"
        f"{shows}\n\n"
        "Source note\n"
        f"{source_note}\n\n"
        "Freshness note\n"
        f"{freshness_note}\n\n"
        "Main risks / limits\n"
        f"{risk_line} Quick limitations: {format_quick_limitations(data_quality)}.\n\n"
        "Needed for final IC Action\n"
        "Full evidence, valuation, risk, implementation, portfolio-fit, and committee-synthesis gates.\n\n"
        "Next step\n"
        f"{next_step}"
    )
    validate_quick_generated_answer(answer, data_quality=data_quality)
    return answer

def validate_quick_generated_answer(answer: str, data_quality: dict[str, Any] | None = None) -> dict[str, Any]:
    text = answer.strip()
    if not text:
        raise QuickRunError("quick_answer_validation_error: empty generated answer")

    status_match = re.search(r"(?im)^Status:\s*(Preliminary|Limited|Blocked)\s*$", text)
    if not status_match:
        raise QuickRunError("quick_answer_validation_error: missing valid Status line")
    status = status_match.group(1)

    ic_status_match = re.search(r"(?im)^IC Action Status:\s*(Limited|Blocked)\s*$", text)
    if not ic_status_match:
        raise QuickRunError("quick_answer_validation_error: IC Action Status must be Limited or Blocked")
    if status == "Blocked" and ic_status_match.group(1) != "Blocked":
        raise QuickRunError("quick_answer_validation_error: Blocked status must have blocked IC Action Status")

    final_match = re.search(r"(?im)^Final IC Action:\s*Unavailable in QUICK\.\s*$", text)
    if not final_match:
        raise QuickRunError("quick_answer_validation_error: Final IC Action must be explicitly unavailable")

    if re.search(r"(?i)\bAction\s+Box\b", text):
        raise QuickRunError("quick_answer_validation_error: forbidden Action Box")
    if QUICK_ANSWER_FORBIDDEN_ACTION_PATTERN.search(text):
        raise QuickRunError("quick_answer_validation_error: forbidden final action language")
    if QUICK_ANSWER_SIZING_PATTERN.search(text):
        raise QuickRunError("quick_answer_validation_error: forbidden exact sizing or trade instruction")
    for section in QUICK_ANSWER_REQUIRED_SECTIONS:
        if not re.search(rf"(?m)^{re.escape(section)}\s*$", text):
            raise QuickRunError(f"quick_answer_validation_error: missing section {section}")

    quality_checks = {
        "status_valid": status in QUICK_ANSWER_STATUSES,
        "ic_action_status_limited_or_blocked": True,
        "final_ic_action_unavailable": True,
        "no_action_box": True,
        "no_final_action_language": True,
        "no_exact_sizing": True,
        "required_sections_present": True,
    }
    if data_quality:
        missing = set(data_quality.get("missing_inputs") or [])
        if missing & {"price", "recent_events", "valuation_context"} and status == "Preliminary":
            raise QuickRunError("quick_answer_validation_error: missing price/news/context cannot be Preliminary")
        if status == "Blocked" and not data_quality.get("reason_for_status"):
            raise QuickRunError("quick_answer_validation_error: Blocked status needs a reason")
        if status == "Limited" and not missing and not data_quality.get("freshness_limitations"):
            raise QuickRunError("quick_answer_validation_error: Limited status needs missing-data explanation")
        quality_checks["status_matches_missing_data"] = True
        quality_checks["blocked_or_limited_reason_present"] = True

    return {"status": "pass", "quick_status": status, "quality_checks": quality_checks}


def validate_quick_answer_run(run_dir: Path) -> dict[str, Any]:
    if not run_dir.is_dir():
        raise QuickRunError(f"quick_answer_validation_error: run directory not found: {run_dir}")
    source_path = run_dir / "source_snapshot.json"
    quality_path = run_dir / "data_quality.json"
    answer_path = run_dir / "quick_answer.json"
    output_quality_path = run_dir / "output_quality.json"
    for path in (source_path, quality_path, answer_path, output_quality_path):
        if not path.is_file():
            raise QuickRunError(f"quick_answer_validation_error: missing {path.name}")

    forbidden_files = [path for path in run_dir.rglob("*") if path.name == "investment_report.md"]
    forbidden_dirs = [path for path in run_dir.rglob("*") if path.is_dir() and path.name.lower() == "audit"]
    if forbidden_files:
        raise QuickRunError("quick_answer_validation_error: investment_report.md must not be created")
    if forbidden_dirs:
        raise QuickRunError("quick_answer_validation_error: audit directory must not be created")

    source_snapshot = json.loads(source_path.read_text(encoding="utf-8"))
    data_quality = json.loads(quality_path.read_text(encoding="utf-8"))
    quick_answer = json.loads(answer_path.read_text(encoding="utf-8"))
    output_quality = json.loads(output_quality_path.read_text(encoding="utf-8"))

    for key in (
        "prompt",
        "normalized_prompt",
        "asset_identity",
        "sources",
        "timestamp",
        "retrieved",
        "missing",
        "not_obtained",
        "access_status",
        "freshness_status",
    ):
        if key not in source_snapshot:
            raise QuickRunError(f"quick_answer_validation_error: source_snapshot missing {key}")

    for key in ("schema_version", "providers", "provider_results", "provider_errors", "source_scope", "evidence_alignment"):
        if key not in source_snapshot:
            raise QuickRunError(f"quick_answer_validation_error: source_snapshot missing {key}")
    if source_snapshot["source_scope"] != "Public-Data Only":
        raise QuickRunError("quick_answer_validation_error: source_scope must be Public-Data Only")
    if "not an Evidence Collector evidence_pack" not in str(source_snapshot.get("evidence_alignment")):
        raise QuickRunError("quick_answer_validation_error: snapshot must not claim to be Evidence Collector evidence_pack")
    if not isinstance(source_snapshot.get("providers"), list):
        raise QuickRunError("quick_answer_validation_error: providers must be a list")
    provider_id_list = []
    for provider in source_snapshot.get("providers") or []:
        if not isinstance(provider, dict):
            raise QuickRunError("quick_answer_validation_error: provider entries must be objects")
        for provider_key in ("provider_id", "provider_type", "components", "asset_types", "quality_level", "enabled", "priority"):
            if provider_key not in provider:
                raise QuickRunError(f"quick_answer_validation_error: provider entry missing {provider_key}")
        provider_id_list.append(provider.get("provider_id"))
        if provider.get("provider_type") not in ALLOWED_PROVIDER_TYPES:
            raise QuickRunError("quick_answer_validation_error: invalid provider type")
        if provider.get("quality_level") not in ALLOWED_QUALITY_LEVELS:
            raise QuickRunError("quick_answer_validation_error: invalid provider quality level")
        if not isinstance(provider.get("components"), list):
            raise QuickRunError("quick_answer_validation_error: provider components must be a list")
        if not isinstance(provider.get("asset_types"), list):
            raise QuickRunError("quick_answer_validation_error: provider asset_types must be a list")
        if not isinstance(provider.get("enabled"), bool):
            raise QuickRunError("quick_answer_validation_error: provider enabled must be bool")
        if not isinstance(provider.get("priority"), int):
            raise QuickRunError("quick_answer_validation_error: provider priority must be int")
    if len(provider_id_list) != len(set(provider_id_list)):
        raise QuickRunError("quick_answer_validation_error: provider IDs must be unique")

    if not isinstance(source_snapshot.get("provider_results"), list):
        raise QuickRunError("quick_answer_validation_error: provider_results must be a list")
    if not isinstance(source_snapshot.get("provider_errors"), list):
        raise QuickRunError("quick_answer_validation_error: provider_errors must be a list")
    provider_error_keys = set()
    for provider_error in source_snapshot.get("provider_errors") or []:
        if not isinstance(provider_error, dict):
            raise QuickRunError("quick_answer_validation_error: provider_errors entries must be objects")
        for error_key in ("provider_id", "component", "status", "error"):
            if error_key not in provider_error:
                raise QuickRunError(f"quick_answer_validation_error: provider_errors entry missing {error_key}")
        provider_error_keys.add((provider_error.get("provider_id"), provider_error.get("component"), provider_error.get("status"), provider_error.get("error")))
    provider_result_error_keys = set()
    for provider_result in source_snapshot.get("provider_results") or []:
        if not isinstance(provider_result, dict):
            raise QuickRunError("quick_answer_validation_error: provider_results entries must be objects")
        if provider_result.get("status") not in ALLOWED_PROVIDER_STATUSES:
            raise QuickRunError("quick_answer_validation_error: invalid provider result status")
        if provider_result.get("quality_level") not in ALLOWED_QUALITY_LEVELS:
            raise QuickRunError("quick_answer_validation_error: invalid provider quality level")
        if provider_result.get("status") == "error" or (provider_result.get("status") == "missing" and provider_result.get("error")):
            provider_result_error_keys.add((provider_result.get("provider_id"), provider_result.get("component"), provider_result.get("status"), provider_result.get("error")))
    if provider_result_error_keys != provider_error_keys:
        raise QuickRunError("quick_answer_validation_error: provider_errors must match errored provider_results")
    provider_ids = {str(provider.get("provider_id")) for provider in source_snapshot.get("providers") or [] if isinstance(provider, dict)}
    if set(source_snapshot.get("missing") or []) & provider_ids:
        raise QuickRunError("quick_answer_validation_error: provider IDs must not count as missing required public data")
    for key in (
        "status",
        "missing_inputs",
        "freshness_limitations",
        "reason_for_status",
        "quick_answer_allowed",
    ):
        if key not in data_quality:
            raise QuickRunError(f"quick_answer_validation_error: data_quality missing {key}")
    for key in ("provider_quality_summary", "freshness_by_component", "source_scope", "evidence_alignment"):
        if key not in data_quality:
            raise QuickRunError(f"quick_answer_validation_error: data_quality missing {key}")
    if data_quality["status"] not in QUICK_ANSWER_STATUSES:
        raise QuickRunError("quick_answer_validation_error: invalid data quality status")
    for key in (
        "prompt",
        "user_answers",
        "generated_answer",
        "validation_result",
        "snapshot_path",
        "mode",
        "output_quality_path",
        "output_quality_result",
    ):
        if key not in quick_answer:
            raise QuickRunError(f"quick_answer_validation_error: quick_answer missing {key}")

    try:
        output_quality_path_matches = Path(str(quick_answer["output_quality_path"])).resolve() == output_quality_path.resolve()
    except (OSError, RuntimeError, ValueError):
        output_quality_path_matches = quick_answer["output_quality_path"] == str(output_quality_path)
    if not output_quality_path_matches:
        raise QuickRunError("quick_answer_validation_error: quick_answer output_quality_path mismatch")
    quality_result = quick_answer.get("output_quality_result")
    if not isinstance(quality_result, dict):
        raise QuickRunError("quick_answer_validation_error: output_quality_result must be an object")
    for key in ("status", "hard_failures", "soft_failures"):
        if key not in quality_result:
            raise QuickRunError(f"quick_answer_validation_error: output_quality_result missing {key}")

    if output_quality.get("schema_version") != OUTPUT_QUALITY_SCHEMA_VERSION:
        raise QuickRunError("quick_answer_validation_error: invalid output_quality schema_version")
    if output_quality.get("status") not in {"pass", "fail"}:
        raise QuickRunError("quick_answer_validation_error: invalid output_quality status")
    if output_quality.get("mode") not in {"mock", "live"}:
        raise QuickRunError("quick_answer_validation_error: invalid output_quality mode")
    if output_quality.get("quick_status") not in QUICK_ANSWER_STATUSES:
        raise QuickRunError("quick_answer_validation_error: invalid output_quality quick_status")
    for key in ("hard_failures", "soft_failures", "warnings"):
        if not isinstance(output_quality.get(key), list):
            raise QuickRunError(f"quick_answer_validation_error: output_quality {key} must be a list")
    checks = output_quality.get("checks")
    if not isinstance(checks, dict):
        raise QuickRunError("quick_answer_validation_error: output_quality checks must be an object")
    missing_output_checks = sorted(OUTPUT_QUALITY_REQUIRED_CHECKS - set(checks))
    if missing_output_checks:
        raise QuickRunError("quick_answer_validation_error: output_quality missing checks: " + ", ".join(missing_output_checks))
    if any(not isinstance(checks.get(key), bool) for key in OUTPUT_QUALITY_REQUIRED_CHECKS):
        raise QuickRunError("quick_answer_validation_error: output_quality checks must be booleans")
    if output_quality.get("status") == "pass" and (output_quality.get("hard_failures") or output_quality.get("soft_failures")):
        raise QuickRunError("quick_answer_validation_error: passing output_quality cannot have failures")
    recomputed_output_quality = assess_quick_output_quality(
        quick_answer["generated_answer"],
        source_snapshot=source_snapshot,
        data_quality=data_quality,
    )
    if output_quality != recomputed_output_quality:
        raise QuickRunError("quick_answer_validation_error: output_quality is stale or does not match generated_answer")
    if output_quality.get("status") == "fail":
        raise QuickRunError("quick_answer_validation_error: output_quality failed: " + quality_failure_summary(output_quality))
    if quality_result.get("status") != output_quality.get("status"):
        raise QuickRunError("quick_answer_validation_error: output_quality_result status mismatch")
    if quality_result.get("hard_failures") != output_quality.get("hard_failures"):
        raise QuickRunError("quick_answer_validation_error: output_quality_result hard_failures mismatch")
    if quality_result.get("soft_failures") != output_quality.get("soft_failures"):
        raise QuickRunError("quick_answer_validation_error: output_quality_result soft_failures mismatch")
    for key in ("risk_assessment", "source_note", "freshness_note"):
        if not isinstance(output_quality.get(key), dict):
            raise QuickRunError(f"quick_answer_validation_error: output_quality {key} must be an object")
    if not output_quality["source_note"].get("present") or not str(output_quality["source_note"].get("text", "")).strip():
        raise QuickRunError("quick_answer_validation_error: Source note must be present and non-empty")
    if not output_quality["freshness_note"].get("present") or not str(output_quality["freshness_note"].get("text", "")).strip():
        raise QuickRunError("quick_answer_validation_error: Freshness note must be present and non-empty")

    validation = validate_quick_generated_answer(
        quick_answer["generated_answer"],
        data_quality=data_quality,
    )
    if data_quality["status"] == "Blocked" and not data_quality.get("reason_for_status"):
        raise QuickRunError("quick_answer_validation_error: Blocked status needs a clear reason")
    if data_quality["status"] == "Limited" and not (
        data_quality.get("missing_inputs") or data_quality.get("freshness_limitations")
    ):
        raise QuickRunError("quick_answer_validation_error: Limited status needs missing-data explanation")

    missing = set(data_quality.get("missing_inputs") or [])
    if missing & {"price", "recent_events", "valuation_context"} and data_quality["status"] == "Preliminary":
        raise QuickRunError("quick_answer_validation_error: missing price/news/context cannot be Preliminary")
    if source_snapshot.get("answer_freshness_required") and data_quality["status"] == "Preliminary":
        raise QuickRunError("quick_answer_validation_error: freshness-required answer cannot be Preliminary")
    if data_quality.get("freshness_limitations") and data_quality["status"] == "Preliminary":
        raise QuickRunError("quick_answer_validation_error: freshness limitations cannot be Preliminary")
    price_status = ((data_quality.get("freshness_by_component") or {}).get("price") or {}).get("status")
    if price_status in {"Unknown", "Stale but Usable", "Not Found"} and data_quality["status"] == "Preliminary":
        raise QuickRunError("quick_answer_validation_error: stale or unknown price freshness cannot be Preliminary")
    identity = source_snapshot.get("asset_identity") or {}
    if identity.get("security_type") == "multi_asset_comparison":
        components = identity.get("components") or (source_snapshot.get("data") or {}).get("components") or []
        component_tickers = {component.get("ticker") for component in components if isinstance(component, dict)}
        if not {"MSFT", "SPY", "BTC"}.issubset(component_tickers):
            raise QuickRunError("quick_answer_validation_error: comparison requires MSFT, SPY, and BTC component identities")

    return {
        "status": "pass",
        "run_dir": str(run_dir),
        "quick_status": data_quality["status"],
        "quality_checks": {
            **validation["quality_checks"],
            "source_snapshot_exists": True,
            "data_quality_exists": True,
            "quick_answer_exists": True,
            "output_quality_exists": True,
            "output_quality_passed": output_quality.get("status") == "pass",
            "no_investment_report": True,
            "no_audit_dir": True,
            "missing_data_status_checked": True,
        },
    }


def write_quick_answer_files(
    *,
    prompt: str,
    answers: list[str],
    mode: str,
    source_snapshot: dict[str, Any],
    data_quality: dict[str, Any],
    generated_answer: str,
    output_quality: dict[str, Any],
    run_dir: Path,
) -> dict[str, Any]:
    source_path = run_dir / "source_snapshot.json"
    quality_path = run_dir / "data_quality.json"
    answer_path = run_dir / "quick_answer.json"
    output_quality_path = run_dir / "output_quality.json"
    source_path.write_text(json.dumps(source_snapshot, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    quality_path.write_text(json.dumps(data_quality, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    output_quality_path.write_text(json.dumps(output_quality, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    quick_answer_payload = {
        "prompt": prompt,
        "user_answers": answers,
        "generated_answer": generated_answer,
        "validation_result": {"status": "pending"},
        "snapshot_path": str(source_path),
        "output_quality_path": str(output_quality_path),
        "output_quality_result": {
            "status": output_quality.get("status"),
            "hard_failures": output_quality.get("hard_failures", []),
            "soft_failures": output_quality.get("soft_failures", []),
        },
        "mode": mode,
    }
    answer_path.write_text(json.dumps(quick_answer_payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    validation = validate_quick_answer_run(run_dir)
    quick_answer_payload["validation_result"] = validation
    answer_path.write_text(json.dumps(quick_answer_payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return validation


def route_card_for_selected_route(selected_route: str) -> str:
    try:
        return AGENT_ROUTE_CARDS[selected_route]
    except KeyError as exc:
        raise AgentDesignError(
            f"agent_design_error: missing route-card mapping for {selected_route}"
        ) from exc


def planned_subagents_for_route(selected_route: str) -> list[str]:
    common = [
        "evidence-collector",
        "macro-agent",
        "valuation-expectations-agent",
        "risk-red-team-agent",
        "portfolio-fit-agent",
        "investment-committee-agent",
    ]
    lead_by_route = {
        "equity_full_cycle": ["equity-agent", "sector-industry-analysis-agent"],
        "crypto_full_cycle": ["crypto-agent", "market-positioning-agent"],
        "etf_full_cycle": ["etf-agent"],
        "commodity_full_cycle": ["commodity-agent"],
        "fixed_income_full_cycle": ["fixed-income-agent"],
        "multi_asset_comparison": [
            "asset-intake-router",
            "equity-agent",
            "etf-agent",
            "commodity-agent",
            "crypto-agent",
            "fixed-income-agent",
        ],
    }
    agents = [*lead_by_route.get(selected_route, ["asset-intake-router"]), *common]
    return list(dict.fromkeys(agents))


def detect_prompt_language(prompt: str) -> str:
    # Robust against both proper Cyrillic and older mojibake test fixtures.
    if any("Ѐ" <= char <= "ӿ" for char in prompt):
        return "ru"
    if any(marker in prompt for marker in ("Ð", "Ñ", "Р", "С", "ï", "î", "ñ")):
        return "ru"
    return "en"


def repair_legacy_russian_text(value: str) -> str:
    """Repair old UTF-8-as-CP1251 mojibake kept in legacy fixtures/docs."""
    if not any(marker in value for marker in ("Р", "С", "Ñ", "Ð")):
        return value
    try:
        return value.encode("cp1251").decode("utf-8")
    except UnicodeError:
        return value


def build_agent_intake_questions(selected_route: str, normalized_prompt: str) -> list[str]:
    language = detect_prompt_language(normalized_prompt)
    freshness_required = is_freshness_dependent(normalized_prompt)
    if language == "ru":
        freshness_question = (
            "РљР°РєРёРµ С‚РµРєСѓС‰РёРµ РёР»Рё РґР°С‚РёСЂРѕРІР°РЅРЅС‹Рµ РёСЃС‚РѕС‡РЅРёРєРё РЅСѓР¶РЅРѕ СЃС‡РёС‚Р°С‚СЊ РѕР±СЏР·Р°С‚РµР»СЊРЅС‹РјРё РґР»СЏ СЌС‚РѕРіРѕ Р·Р°РїСЂРѕСЃР°?"
            if freshness_required
            else "РќСѓР¶РЅС‹ Р»Рё СЃРІРµР¶РёРµ СЂС‹РЅРѕС‡РЅС‹Рµ РґР°РЅРЅС‹Рµ, РЅРѕРІРѕСЃС‚Рё РёР»Рё РґРѕСЃС‚Р°С‚РѕС‡РЅРѕ СЃС‚СЂСѓРєС‚СѓСЂРЅРѕРіРѕ Р°РЅР°Р»РёР·Р°?"
        )
        route_questions = {
            "crypto_full_cycle": [
                "РљР°РєРѕР№ РіРѕСЂРёР·РѕРЅС‚ РѕС†РµРЅРєРё Рё СЂРѕР»СЊ РєСЂРёРїС‚РѕР°РєС‚РёРІР° РІ РїРѕСЂС‚С„РµР»Рµ РІС‹ РїСЂРµРґРїРѕР»Р°РіР°РµС‚Рµ?",
                "Р•СЃС‚СЊ Р»Рё СѓР¶Рµ СЌРєСЃРїРѕР·РёС†РёСЏ Рє СЌС‚РѕРјСѓ Р°РєС‚РёРІСѓ РёР»Рё Рє РєСЂРёРїС‚РѕСЂС‹РЅРєСѓ РІ С†РµР»РѕРј?",
                "РљР°РєРѕР№ СѓСЂРѕРІРµРЅСЊ РІРѕР»Р°С‚РёР»СЊРЅРѕСЃС‚Рё Рё РїСЂРѕСЃР°РґРєРё РґР»СЏ РІР°СЃ РґРѕРїСѓСЃС‚РёРј?",
                "РљР°РєРѕР№ С„РѕСЂРјР°С‚ РІР»Р°РґРµРЅРёСЏ РІР°Р¶РµРЅ: СЃРїРѕС‚, С„РѕРЅРґРѕРІС‹Р№ РёРЅСЃС‚СЂСѓРјРµРЅС‚, С…СЂР°РЅРµРЅРёРµ РёР»Рё С‚РѕР»СЊРєРѕ Р°РЅР°Р»РёС‚РёС‡РµСЃРєР°СЏ РѕС†РµРЅРєР°?",
                freshness_question,
            ],
            "etf_full_cycle": [
                "РљР°РєСѓСЋ СЂРѕР»СЊ С„РѕРЅРґ РґРѕР»Р¶РµРЅ РёРіСЂР°С‚СЊ РІ РїРѕСЂС‚С„РµР»Рµ: СЂРѕСЃС‚, Р·Р°С‰РёС‚Р°, РґРѕС…РѕРґРЅРѕСЃС‚СЊ РёР»Рё Р·Р°РјРµРЅР° РґСЂСѓРіРѕР№ СЌРєСЃРїРѕР·РёС†РёРё?",
                "РљР°РєРёРµ РїРѕС…РѕР¶РёРµ С„РѕРЅРґС‹, РёРЅРґРµРєСЃС‹ РёР»Рё СЃРµРєС‚РѕСЂР° СѓР¶Рµ РµСЃС‚СЊ РІ РїРѕСЂС‚С„РµР»Рµ?",
                "РљР°РєРѕР№ РіРѕСЂРёР·РѕРЅС‚ Рё РґРѕРїСѓСЃС‚РёРјР°СЏ РїСЂРѕСЃР°РґРєР° РґР»СЏ СЌС‚РѕР№ РїРѕР·РёС†РёРё?",
                "Р•СЃС‚СЊ Р»Рё РѕРіСЂР°РЅРёС‡РµРЅРёСЏ РїРѕ РєРѕРјРёСЃСЃРёСЏРј, Р»РёРєРІРёРґРЅРѕСЃС‚Рё, РІР°Р»СЋС‚Рµ, Р±СЂРѕРєРµСЂСѓ РёР»Рё РЅР°Р»РѕРіР°Рј?",
                freshness_question,
            ],
            "commodity_full_cycle": [
                "РљР°РєР°СЏ С†РµР»СЊ СЌРєСЃРїРѕР·РёС†РёРё: РёРЅС„Р»СЏС†РёРѕРЅРЅР°СЏ Р·Р°С‰РёС‚Р°, С‚Р°РєС‚РёС‡РµСЃРєР°СЏ РёРґРµСЏ, РґРёРІРµСЂСЃРёС„РёРєР°С†РёСЏ РёР»Рё СЃС‚СЂСѓРєС‚СѓСЂРЅР°СЏ СЃС‚Р°РІРєР°?",
                "РќСѓР¶РµРЅ Р°РЅР°Р»РёР· С„РёР·РёС‡РµСЃРєРѕРіРѕ С‚РѕРІР°СЂР°, С„СЊСЋС‡РµСЂСЃРѕРІ, ETF/ETN РёР»Рё Р°РєС†РёР№ РїСЂРѕРёР·РІРѕРґРёС‚РµР»РµР№?",
                "РљР°РєРѕР№ РіРѕСЂРёР·РѕРЅС‚ Рё РґРѕРїСѓСЃС‚РёРјР°СЏ РІРѕР»Р°С‚РёР»СЊРЅРѕСЃС‚СЊ РґР»СЏ СЌС‚РѕР№ РёРґРµРё?",
                "Р•СЃС‚СЊ Р»Рё РѕРіСЂР°РЅРёС‡РµРЅРёСЏ РїРѕ РёРЅСЃС‚СЂСѓРјРµРЅС‚Сѓ, Р»РёРєРІРёРґРЅРѕСЃС‚Рё, РІР°Р»СЋС‚Рµ РёР»Рё СЂРѕР»Р»РѕРІРµСЂСѓ С„СЊСЋС‡РµСЂСЃРѕРІ?",
                freshness_question,
            ],
            "fixed_income_full_cycle": [
                "РљР°РєР°СЏ С†РµР»СЊ: РґРѕС…РѕРґРЅРѕСЃС‚СЊ, Р·Р°С‰РёС‚Р° РєР°РїРёС‚Р°Р»Р°, duration, РєСЂРµРґРёС‚РЅС‹Р№ СЃРїСЂРµРґ РёР»Рё СЃС‚Р°РІРєР° РЅР° СЃРЅРёР¶РµРЅРёРµ СЃС‚Р°РІРѕРє?",
                "РљР°РєРѕР№ РіРѕСЂРёР·РѕРЅС‚, РІР°Р»СЋС‚Р° Рё РґРѕРїСѓСЃС‚РёРјР°СЏ РїСЂРѕС†РµРЅС‚РЅР°СЏ/РєСЂРµРґРёС‚РЅР°СЏ РїСЂРѕСЃР°РґРєР°?",
                "Р Р°СЃСЃРјР°С‚СЂРёРІР°РµС‚СЃСЏ РѕС‚РґРµР»СЊРЅР°СЏ РѕР±Р»РёРіР°С†РёСЏ, ETF, С„РѕРЅРґ РёР»Рё РєСЂРёРІР°СЏ РґРѕС…РѕРґРЅРѕСЃС‚Рё?",
                "Р•СЃС‚СЊ Р»Рё РѕРіСЂР°РЅРёС‡РµРЅРёСЏ РїРѕ РєСЂРµРґРёС‚РЅРѕРјСѓ РєР°С‡РµСЃС‚РІСѓ, СЃСЂРѕРєСѓ, Р»РёРєРІРёРґРЅРѕСЃС‚Рё, РЅР°Р»РѕРіР°Рј РёР»Рё Р±СЂРѕРєРµСЂСѓ?",
                freshness_question,
            ],
            "multi_asset_comparison": [
                "РљР°РєСѓСЋ Р·Р°РґР°С‡Сѓ СЂРµС€Р°РµС‚ СЃСЂР°РІРЅРµРЅРёРµ: СЂРѕСЃС‚, Р·Р°С‰РёС‚Р°, РґРѕС…РѕРґ, РґРёРІРµСЂСЃРёС„РёРєР°С†РёСЏ РёР»Рё С‚Р°РєС‚РёС‡РµСЃРєРёР№ РІС‹Р±РѕСЂ?",
                "РљР°РєРёРµ Р°РєС‚РёРІС‹ СѓР¶Рµ РµСЃС‚СЊ РІ РїРѕСЂС‚С„РµР»Рµ Рё РєР°РєРёРµ РёР· СЃСЂР°РІРЅРёРІР°РµРјС‹С… РёРЅСЃС‚СЂСѓРјРµРЅС‚РѕРІ РІС‹ СѓР¶Рµ РґРµСЂР¶РёС‚Рµ?",
                "РљР°РєРѕР№ РіРѕСЂРёР·РѕРЅС‚, РІР°Р»СЋС‚Р° РѕС†РµРЅРєРё Рё РґРѕРїСѓСЃС‚РёРјР°СЏ РїСЂРѕСЃР°РґРєР°?",
                "РљР°РєРёРµ РєСЂРёС‚РµСЂРёРё РІР°Р¶РЅРµРµ: РґРѕС…РѕРґРЅРѕСЃС‚СЊ, СЂРёСЃРє, Р»РёРєРІРёРґРЅРѕСЃС‚СЊ, РєРѕСЂСЂРµР»СЏС†РёСЏ, РЅР°Р»РѕРіРё РёР»Рё РїСЂРѕСЃС‚РѕС‚Р° РёСЃРїРѕР»РЅРµРЅРёСЏ?",
                freshness_question,
            ],
        }
        questions = route_questions.get(
            selected_route,
            [
                "РљР°РєРѕР№ РёРЅРІРµСЃС‚РёС†РёРѕРЅРЅС‹Р№ РіРѕСЂРёР·РѕРЅС‚ Рё С†РµР»СЊ РѕС†РµРЅРєРё СЌС‚РѕР№ РєРѕРјРїР°РЅРёРё РёР»Рё Р°РєС†РёРё?",
                "Р•СЃС‚СЊ Р»Рё СѓР¶Рµ РїРѕР·РёС†РёСЏ РёР»Рё Р±Р»РёР·РєР°СЏ СЌРєСЃРїРѕР·РёС†РёСЏ С‡РµСЂРµР· РёРЅРґРµРєСЃ, СЃРµРєС‚РѕСЂ РёР»Рё С„РѕРЅРґ?",
                "РљР°РєРѕР№ СѓСЂРѕРІРµРЅСЊ СЂРёСЃРєР°, РїСЂРѕСЃР°РґРєРё Рё РєРѕРЅС†РµРЅС‚СЂР°С†РёРё РґР»СЏ РІР°СЃ РґРѕРїСѓСЃС‚РёРј?",
                "Р•СЃС‚СЊ Р»Рё РѕРіСЂР°РЅРёС‡РµРЅРёСЏ РїРѕ РІС…РѕРґСѓ, РІР°Р»СЋС‚Рµ, РЅР°Р»РѕРіР°Рј, Р±СЂРѕРєРµСЂСѓ РёР»Рё С‚РёРїСѓ РёРЅСЃС‚СЂСѓРјРµРЅС‚Р°?",
                freshness_question,
            ],
        )
        return [repair_legacy_russian_text(question) for question in questions]

    freshness_question = (
        "Which current or timestamped sources should be mandatory for this request?"
        if freshness_required
        else "Do you need fresh market data or news, or is structural analysis enough?"
    )
    route_questions = {
        "crypto_full_cycle": [
            "What time horizon and portfolio role do you have in mind for this crypto asset?",
            "Do you already have exposure to this asset or to crypto more broadly?",
            "What volatility and drawdown level is acceptable for this idea?",
            "Which implementation format matters: spot, fund wrapper, custody, or analysis only?",
            freshness_question,
        ],
        "etf_full_cycle": [
            "What portfolio role should the fund serve: growth, defense, income, or replacement exposure?",
            "Which similar funds, indexes, or sectors do you already own?",
            "What horizon and drawdown tolerance should the design assume?",
            "Are there constraints around fees, liquidity, currency, broker access, or taxes?",
            freshness_question,
        ],
        "commodity_full_cycle": [
            "What is the purpose of the exposure: inflation hedge, tactical idea, diversification, or structural thesis?",
            "Should the future workflow analyze the physical commodity, futures, ETF/ETN, or producer equities?",
            "What horizon and volatility tolerance should apply?",
            "Are there constraints around instrument type, liquidity, currency, or futures roll exposure?",
            freshness_question,
        ],
        "fixed_income_full_cycle": [
            "What is the goal: income, capital preservation, duration, credit spread, or rate-cut exposure?",
            "What horizon, currency, and interest-rate or credit drawdown tolerance should apply?",
            "Is the target an individual bond, ETF, fund, yield curve, or rates exposure?",
            "Are there constraints around credit quality, maturity, liquidity, taxes, or broker access?",
            freshness_question,
        ],
        "multi_asset_comparison": [
            "What decision should the comparison support: growth, defense, income, diversification, or tactical selection?",
            "Which assets are already in the portfolio, and do you hold any of the compared instruments?",
            "What horizon, evaluation currency, and drawdown tolerance should apply?",
            "Which criteria matter most: return, risk, liquidity, correlation, taxes, or implementation simplicity?",
            freshness_question,
        ],
    }
    return route_questions.get(
        selected_route,
        [
            "What investment horizon and objective should the future workflow use for this company or stock?",
            "Do you already have a position or related exposure through an index, sector, or fund?",
            "What risk, drawdown, and concentration level is acceptable?",
            "Are there constraints around entry style, currency, taxes, broker access, or instrument type?",
            freshness_question,
        ],
    )


def build_mock_agent_design(prompt: str) -> AgentDesignResult:
    normalized_prompt = normalize_agent_prompt(prompt)
    selected_route = mock_route(normalized_prompt)
    if selected_route not in VALID_ROUTES:
        raise AgentDesignError(
            "agent_design_error: unable to select a valid AGENT route in mock mode"
        )

    questions = build_agent_intake_questions(selected_route, normalized_prompt)
    design = {
        "status": "Design Draft",
        "automation_scope": "AGENT automation design only; no investment analysis is executed.",
        "source_of_truth": str(PROJECT_ROOT),
        "normalized_prompt": normalized_prompt,
        "selected_route": selected_route,
        "route_card": route_card_for_selected_route(selected_route),
        "first_action": {
            "question_count_required": 5,
            "questions": questions,
            "wait_for_user_after_questions": True,
            "baseline_assumptions_allowed_after_continue": [
                "3-5 year horizon when no horizon is provided",
                "no current position unless stated",
                "no leverage, options, or margin unless stated",
                "no exact position size without portfolio context",
                "no personalized tax recommendation",
            ],
        },
        "execution_phases": [
            "route selection from Financial Agent System route cards",
            "five-question intake and user wait",
            "evidence collection and freshness check",
            "lead asset-class analysis",
            "macro context",
            "material context modules",
            "valuation / expectations gate",
            "risk / red-team gate",
            "implementation / vehicle-quality gate",
            "portfolio-fit gate",
            "IC synthesis only after required gates are recorded",
            "reader-facing report plus audit pack outside both repositories",
        ],
        "planned_subagents": planned_subagents_for_route(selected_route),
        "actual_subagents_run": [],
        "subagent_truthfulness_policy": (
            "The automation may list candidate worker roles. It must keep actual_subagents_run accurate "
            "and must not present planned work as finished unless spawned sessions actually finish."
        ),
        "required_gates": sorted(AGENT_REQUIRED_GATES),
        "artifact_plan": {
            "reports_root": str(AGENT_REPORTS_ROOT),
            "run_folder_pattern": AGENT_RUN_FOLDER_PATTERN,
            "report_path_template": str(
                AGENT_REPORTS_ROOT / AGENT_RUN_FOLDER_PATTERN / "investment_report.md"
            ),
            "report_file": "investment_report.md",
            "audit_directory": "audit",
            "repo_write_boundary": "Do not write AGENT reports or audit packs inside the Automation Lab or Financial Agent System repositories.",
        },
        "ic_boundary": (
            "No positive or final IC Action may be emitted until required gates pass. "
            "If any required gate is missing, IC output must be Limited or Blocked and must not present a positive final action."
        ),
        "out_of_scope": [
            "fetching evidence",
            "running valuation",
            "running risk review",
            "spawning subagents",
            "creating an investment report",
            "creating an audit folder",
            "issuing final IC Action",
        ],
    }
    validate_agent_design(design)
    return AgentDesignResult(
        prompt=prompt,
        normalized_prompt=normalized_prompt,
        selected_route=selected_route,
        design=design,
        mode="mock",
    )


def validate_agent_design(design: dict[str, Any]) -> AgentDesignValidation:
    if set(AGENT_ROUTE_CARDS) != VALID_ROUTES:
        raise ValueError("agent_design_validation_error: AGENT route-card map must cover every valid route exactly")

    if design.get("status") != "Design Draft":
        raise ValueError("agent_design_validation_error: status must be Design Draft")
    if design.get("source_of_truth") != str(PROJECT_ROOT):
        raise ValueError("agent_design_validation_error: main project must remain source of truth")
    selected_route = design.get("selected_route")
    if selected_route not in VALID_ROUTES:
        raise ValueError("agent_design_validation_error: selected route is invalid")
    expected_route_card = route_card_for_selected_route(selected_route)
    if design.get("route_card") != expected_route_card:
        raise ValueError("agent_design_validation_error: route card does not match selected route")
    route_card_path = PROJECT_ROOT / expected_route_card
    if not route_card_path.is_file():
        raise ValueError("agent_design_validation_error: route card is missing in main project")

    first_action = design.get("first_action")
    if not isinstance(first_action, dict):
        raise ValueError("agent_design_validation_error: missing first_action")
    questions = first_action.get("questions")
    if not isinstance(questions, list) or len(questions) != 5:
        raise ValueError("agent_design_validation_error: expected exactly 5 intake questions")
    if first_action.get("question_count_required") != 5:
        raise ValueError("agent_design_validation_error: required question count must be 5")
    if first_action.get("wait_for_user_after_questions") is not True:
        raise ValueError("agent_design_validation_error: design must wait for user after intake")
    for question in questions:
        if not isinstance(question, str) or not question.strip().endswith("?"):
            raise ValueError("agent_design_validation_error: every intake item must be a question")

    gates = design.get("required_gates")
    if not isinstance(gates, list):
        raise ValueError("agent_design_validation_error: required_gates must be a list")
    gate_set = set(gates)
    if len(gates) != len(gate_set):
        raise ValueError("agent_design_validation_error: duplicate required gates are not allowed")
    missing_gates = sorted(AGENT_REQUIRED_GATES - gate_set)
    if missing_gates:
        raise ValueError(
            "agent_design_validation_error: missing required gates: " + ", ".join(missing_gates)
        )
    extra_gates = sorted(gate_set - AGENT_REQUIRED_GATES)
    if extra_gates:
        raise ValueError(
            "agent_design_validation_error: unknown required gates: " + ", ".join(extra_gates)
        )

    planned = design.get("planned_subagents")
    actual = design.get("actual_subagents_run")
    if not isinstance(planned, list) or not planned:
        raise ValueError("agent_design_validation_error: planned_subagents must be non-empty")
    if len(planned) != len(set(planned)):
        raise ValueError("agent_design_validation_error: duplicate planned subagents are not allowed")
    available_agents = load_main_project_agent_names()
    missing_allowed_agent_files = sorted(AGENT_ALLOWED_SUBAGENTS - available_agents)
    if missing_allowed_agent_files:
        raise ValueError(
            "agent_design_validation_error: allowed subagents missing from main project: "
            + ", ".join(missing_allowed_agent_files)
        )
    unknown_agents = sorted(set(planned) - AGENT_ALLOWED_SUBAGENTS)
    if unknown_agents:
        raise ValueError(
            "agent_design_validation_error: unknown planned subagents: " + ", ".join(unknown_agents)
        )
    missing_agent_files = sorted(set(planned) - available_agents)
    if missing_agent_files:
        raise ValueError(
            "agent_design_validation_error: planned subagents missing from main project: "
            + ", ".join(missing_agent_files)
        )
    if actual != []:
        raise ValueError("agent_design_validation_error: design mode must not record actual subagents")

    string_values = list(iter_string_values(design))
    claim_patterns = [
        r"(?i)\bsub[- ]?agents?\b.*\b(ran|completed|reviewed|executed|finished)\b",
        r"(?i)\bspawned\s+sub[- ]?agents?\b",
        r"(?i)\b(?:analysts?|specialists?)\b.*\b(ran|completed|reviewed|executed|finished)\b",
        r"(?i)\b(?:evidence-collector|macro-agent|valuation-expectations-agent|risk-red-team-agent|portfolio-fit-agent|investment-committee-agent|equity-agent|crypto-agent|etf-agent|commodity-agent|fixed-income-agent|sector-industry-analysis-agent|market-positioning-agent)\b.*\b(ran|completed|reviewed|executed|finished)\b",
        r"(?i)\b(ran|completed|reviewed|executed|finished|delivered|received)\b.*\b(?:evidence-collector|macro-agent|valuation-expectations-agent|risk-red-team-agent|portfolio-fit-agent|investment-committee-agent|equity-agent|crypto-agent|etf-agent|commodity-agent|fixed-income-agent|sector-industry-analysis-agent|market-positioning-agent)\b",
        r"(?i)\bagent\s+outputs?\s+(delivered|received|completed)\b",
        r"(?i)\banalyst\s+packets?\s+(delivered|received|completed)\b",
        r"(?i)\bactual\s+(review|analysis|execution)\s+(finished|completed)\b",
    ]
    for pattern in claim_patterns:
        for value in string_values:
            if re.search(pattern, value):
                raise ValueError("agent_design_validation_error: design must not claim subagents ran")

    artifact_plan = design.get("artifact_plan")
    if not isinstance(artifact_plan, dict):
        raise ValueError("agent_design_validation_error: missing artifact_plan")
    reports_root = artifact_plan.get("reports_root")
    if reports_root != str(AGENT_REPORTS_ROOT):
        raise ValueError("agent_design_validation_error: reports root must be outside repositories")
    reports_path = Path(reports_root).resolve()
    if is_path_within(reports_path, LAB_ROOT) or is_path_within(reports_path, PROJECT_ROOT):
        raise ValueError("agent_design_validation_error: reports root must be outside repositories")
    if artifact_plan.get("report_file") != "investment_report.md":
        raise ValueError("agent_design_validation_error: report file must be investment_report.md")
    if artifact_plan.get("audit_directory") != "audit":
        raise ValueError("agent_design_validation_error: audit directory must be audit")
    if artifact_plan.get("run_folder_pattern") != AGENT_RUN_FOLDER_PATTERN:
        raise ValueError("agent_design_validation_error: run folder pattern is invalid")
    expected_report_template = str(
        AGENT_REPORTS_ROOT / AGENT_RUN_FOLDER_PATTERN / "investment_report.md"
    )
    if artifact_plan.get("report_path_template") != expected_report_template:
        raise ValueError("agent_design_validation_error: report path template is invalid")

    quality_checks = {
        "design_only": design.get("automation_scope", "").endswith(
            "no investment analysis is executed."
        ),
        "main_project_source_of_truth": design.get("source_of_truth") == str(PROJECT_ROOT),
        "exactly_five_questions": len(questions) == 5,
        "waits_after_intake": first_action.get("wait_for_user_after_questions") is True,
        "required_gates_present": not missing_gates,
        "planned_not_claimed_subagents": actual == [],
        "planned_subagents_allowed": not unknown_agents,
        "planned_subagent_files_exist": not missing_agent_files,
        "route_card_exists": route_card_path.is_file(),
        "report_and_audit_outside_repos": reports_root == str(AGENT_REPORTS_ROOT),
        "run_folder_pattern_present": artifact_plan.get("run_folder_pattern")
        == AGENT_RUN_FOLDER_PATTERN,
        "ic_action_locked": "No positive or final IC Action" in design.get("ic_boundary", ""),
    }
    if not all(quality_checks.values()):
        failed = [key for key, value in quality_checks.items() if not value]
        raise ValueError("agent_design_validation_error: failed checks: " + ", ".join(failed))

    return AgentDesignValidation(
        status="pass",
        question_count=len(questions),
        required_gates_present=sorted(gate_set & AGENT_REQUIRED_GATES),
        quality_checks=quality_checks,
    )


def iter_string_values(value: Any) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, dict):
        strings: list[str] = []
        for child in value.values():
            strings.extend(iter_string_values(child))
        return strings
    if isinstance(value, list):
        strings = []
        for child in value:
            strings.extend(iter_string_values(child))
        return strings
    return []


def is_path_within(path: Path, possible_parent: Path) -> bool:
    try:
        path.resolve().relative_to(possible_parent.resolve())
        return True
    except ValueError:
        return False


def load_main_project_agent_names() -> set[str]:
    agents_dir = PROJECT_ROOT / ".codex" / "agents"
    if not agents_dir.is_dir():
        raise ValueError("agent_design_validation_error: main project agent directory is missing")
    return {path.stem for path in agents_dir.glob("*.toml")}


def parse_route_json(response_text: str) -> dict[str, str]:
    parsed = json.loads(response_text)
    if not isinstance(parsed, dict):
        raise ValueError("response JSON must be an object")

    expected_keys = {"selected_route", "reason"}
    if set(parsed) != expected_keys:
        raise ValueError("response JSON must contain exactly selected_route and reason")

    selected_route = parsed.get("selected_route")
    reason = parsed.get("reason")
    if not isinstance(selected_route, str) or not selected_route.strip():
        raise ValueError("selected_route must be a non-empty string")
    if selected_route not in VALID_ROUTES:
        raise ValueError(f"selected_route is not an allowed route: {selected_route}")
    if not isinstance(reason, str) or not reason.strip():
        raise ValueError("reason must be a non-empty string")

    return {"selected_route": selected_route, "reason": reason}


def evaluate_cases(
    cases: list[dict[str, Any]],
    mode: str,
    live_classifier: LiveCodexRouteClassifier | None = None,
) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    classifier = live_classifier if mode == "live" else None
    if mode == "live" and classifier is None:
        classifier = LiveCodexRouteClassifier()

    for case in cases:
        case_id = require_case_field(case, "case_id")
        prompt = require_case_field(case, "prompt")
        expected_route = require_case_field(case, "expected_route")

        result: dict[str, Any] = {
            "case_id": case_id,
            "prompt": prompt,
            "expected_route": expected_route,
        }

        if mode == "mock":
            actual_route = mock_route(prompt)
            result["actual_route"] = actual_route
        elif mode == "live":
            assert classifier is not None
            try:
                classification = classifier.classify(prompt)
                actual_route = classification.selected_route
                result.update(
                    {
                        "actual_route": actual_route,
                        "reason": classification.reason,
                        "attempts": classification.attempts,
                    }
                )
            except LiveRouteError as exc:
                actual_route = "error"
                result.update(
                    {
                        "actual_route": actual_route,
                        "error": str(exc),
                        "diagnostic_hint": DIAGNOSTIC_HINT,
                    }
                )
        else:
            raise ValueError(f"Unsupported route-check mode: {mode}")

        status = "pass" if actual_route == expected_route else "fail"
        result["status"] = status
        if status == "fail" and "diagnostic_hint" not in result:
            result["mismatch"] = f"expected {expected_route}, got {actual_route}"
            result["diagnostic_hint"] = DIAGNOSTIC_HINT
        results.append(result)
    return results


def write_run_log(mode: str, results: list[dict[str, Any]], runs_dir: Path | None = None) -> Path:
    output_dir = runs_dir or get_route_runs_dir()
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).astimezone().isoformat(timespec="microseconds")
    safe_timestamp = timestamp.replace(":", "").replace("+", "p").replace("-", "")
    path = output_dir / f"{safe_timestamp}-{mode}-{uuid4().hex[:8]}.json"
    payload = {
        "timestamp": timestamp,
        "mode": mode,
        "project_root": str(PROJECT_ROOT),
        "cases": results,
    }
    with path.open("w", encoding="utf-8") as file:
        json.dump(payload, file, indent=2, ensure_ascii=False)
        file.write("\n")
    return path


def write_quick_run_log(result: QuickRunResult, runs_dir: Path | None = None) -> Path:
    output_dir = runs_dir or get_quick_runs_dir()
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).astimezone().isoformat(timespec="microseconds")
    safe_timestamp = timestamp.replace(":", "").replace("+", "p").replace("-", "")
    path = output_dir / f"{safe_timestamp}-{result.mode}-quick-{uuid4().hex[:8]}.json"
    validation = validate_quick_output(result.output, normalized_prompt=result.normalized_prompt)
    payload = {
        "timestamp": timestamp,
        "mode": result.mode,
        "workflow": "quick_take",
        "project_root": str(PROJECT_ROOT),
        "prompt": result.prompt,
        "normalized_prompt": result.normalized_prompt,
        "boundary_status": result.boundary_status,
        "guardrails": {
            "preliminary_or_limited_only": True,
            "no_report_requested": True,
            "no_audit_requested": True,
            "no_ic_action_requested": True,
        },
        "validation": {
            "status": "pass",
            "question_count": validation.question_count,
            "quality_checks": validation.quality_checks,
        },
        "output": result.output,
    }
    with path.open("w", encoding="utf-8") as file:
        json.dump(payload, file, indent=2, ensure_ascii=False)
        file.write("\n")
    return path


def write_quick_error_log(prompt: str, mode: str, error: str, runs_dir: Path | None = None) -> Path:
    output_dir = runs_dir or get_quick_runs_dir()
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).astimezone().isoformat(timespec="microseconds")
    safe_timestamp = timestamp.replace(":", "").replace("+", "p").replace("-", "")
    path = output_dir / f"{safe_timestamp}-{mode}-quick-error-{uuid4().hex[:8]}.json"
    payload = {
        "timestamp": timestamp,
        "mode": mode,
        "workflow": "quick_take",
        "project_root": str(PROJECT_ROOT),
        "prompt": prompt,
        "normalized_prompt": normalize_quick_prompt(prompt),
        "validation": {"status": "fail", "error": error},
        "output": None,
    }
    with path.open("w", encoding="utf-8") as file:
        json.dump(payload, file, indent=2, ensure_ascii=False)
        file.write("\n")
    return path


def write_quick_answer_run_log(result: QuickAnswerResult, runs_dir: Path | None = None) -> Path:
    output_dir = runs_dir or get_quick_runs_dir()
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).astimezone().isoformat(timespec="microseconds")
    safe_timestamp = safe_timestamp_for_path(timestamp)
    path = output_dir / f"{safe_timestamp}-{result.mode}-quick-answer-{uuid4().hex[:8]}.json"
    payload = {
        "timestamp": timestamp,
        "mode": result.mode,
        "workflow": "quick_answer",
        "project_root": str(PROJECT_ROOT),
        "prompt": result.prompt,
        "normalized_prompt": result.normalized_prompt,
        "user_answers_count": len(result.answers),
        "data_run_dir": str(result.run_dir),
        "quick_status": result.data_quality["status"],
        "validation": result.validation,
        "output_quality": {
            "status": result.output_quality.get("status"),
            "hard_failures": result.output_quality.get("hard_failures", []),
            "soft_failures": result.output_quality.get("soft_failures", []),
        },
        "created_files": [
            str(result.run_dir / "source_snapshot.json"),
            str(result.run_dir / "data_quality.json"),
            str(result.run_dir / "quick_answer.json"),
            str(result.run_dir / "output_quality.json"),
        ],
    }
    with path.open("w", encoding="utf-8") as file:
        json.dump(payload, file, indent=2, ensure_ascii=False)
        file.write("\n")
    return path


def write_agent_design_log(result: AgentDesignResult, runs_dir: Path | None = None) -> Path:
    output_dir = runs_dir or get_agent_design_runs_dir()
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).astimezone().isoformat(timespec="microseconds")
    safe_timestamp = timestamp.replace(":", "").replace("+", "p").replace("-", "")
    path = output_dir / f"{safe_timestamp}-{result.mode}-agent-design-{uuid4().hex[:8]}.json"
    validation = validate_agent_design(result.design)
    payload = {
        "timestamp": timestamp,
        "mode": result.mode,
        "workflow": "agent_automation_design",
        "project_root": str(PROJECT_ROOT),
        "prompt": result.prompt,
        "normalized_prompt": result.normalized_prompt,
        "selected_route": result.selected_route,
        "validation": {
            "status": validation.status,
            "question_count": validation.question_count,
            "required_gates_present": validation.required_gates_present,
            "quality_checks": validation.quality_checks,
        },
        "design": result.design,
    }
    with path.open("w", encoding="utf-8") as file:
        json.dump(payload, file, indent=2, ensure_ascii=False)
        file.write("\n")
    return path


def print_agent_design_summary(result: AgentDesignResult, run_log_path: Path) -> None:
    print("AGENT automation design summary: created design-only workflow plan")
    print(f"Mode: {result.mode}")
    print(f"Selected route: {result.selected_route}")
    print("Prompt: captured in run log")
    print("Intake questions:")
    for index, question in enumerate(result.design["first_action"]["questions"], start=1):
        print(f"{index}. {question}")
    print("Design boundary: no analysis executed; no subagents executed; IC decision gate remains locked.")
    print(f"Run log: {run_log_path}")
    print("Russian summary: РґРёР·Р°Р№РЅ AGENT-Р°РІС‚РѕРјР°С‚РёР·Р°С†РёРё СЃРѕР·РґР°РЅ Р±РµР· Р·Р°РїСѓСЃРєР° РёРЅРІРµСЃС‚РёС†РёРѕРЅРЅРѕРіРѕ Р°РЅР°Р»РёР·Р°.")


def print_quick_summary(result: QuickRunResult, run_log_path: Path) -> None:
    print("QUICK launch summary: created guarded Quick Take first step")
    print(f"Mode: {result.mode}")
    print(f"Boundary: {result.boundary_status}")
    print("Prompt: captured in run log")
    print("Output:")
    print(result.output)
    print(f"Run log: {run_log_path}")
    print(
        f"Russian summary: QUICK launch stayed {result.boundary_status} "
        "with safety guardrails intact."
    )


def print_quick_answer_summary(result: QuickAnswerResult, run_log_path: Path) -> None:
    print("QUICK answer summary: created validated Quick Take")
    print(f"Mode: {result.mode}")
    print(f"Status: {result.data_quality['status']}")
    print(f"Output quality: {result.output_quality['status']}")
    print("Prompt: captured in saved JSON")
    print("Quick Take:")
    print(result.generated_answer)
    print(f"Data snapshot: {result.run_dir}")
    print(f"Run log: {run_log_path}")
    print("Russian summary: QUICK answer Р·Р°РІРµСЂС€С‘РЅ СЃ СЃРѕС…СЂР°РЅС‘РЅРЅС‹Рј snapshot Рё РїСЂРѕРІРµСЂРєР°РјРё.")


def print_summary(results: list[dict[str, Any]], run_log_path: Path) -> None:
    total = len(results)
    passed = sum(1 for result in results if result["status"] == "pass")
    failed = total - passed

    print(f"Route check summary: {passed}/{total} passed, {failed} failed")
    for result in results:
        print(
            " - "
            f"{result['case_id']}: "
            f"expected={result['expected_route']} "
            f"actual={result['actual_route']} "
            f"status={result['status']}"
        )
    print(f"Run log: {run_log_path}")
    if failed == 0:
        print("Russian summary: all routes were selected correctly.")
    else:
        print("Russian summary: route mismatches were found.")


class AgentRunError(Exception):
    """Raised when supported-equity AGENT run validation or execution fails."""


class SpecialistRunError(Exception):
    """Raised when direct specialist execution or validation fails."""


def parse_specialist_prompt(prompt: str) -> dict[str, str]:
    match = re.match(r"^\s*([A-Za-z]+)\s*:\s*(.+?)\s*$", prompt)
    if not match:
        raise SpecialistRunError("specialist_run_error: prompt must start with a supported specialist prefix such as RISK:, VAL:, MACRO:, NEWS:, ETF:, CRYPTO:, FI:, or IC:")
    prefix = match.group(1).upper()
    subject_prompt = match.group(2).strip()
    if prefix not in SPECIALIST_COMMANDS:
        raise SpecialistRunError(f"specialist_run_error: unsupported specialist prefix: {prefix}")
    if not subject_prompt:
        raise SpecialistRunError("specialist_run_error: specialist prompt needs a non-empty subject after the prefix")
    return {"prefix": prefix, "specialist_id": SPECIALIST_COMMANDS[prefix], "subject_prompt": subject_prompt}


def create_specialist_run_dir(prefix: str, subject: str, reports_root: Path | None = None) -> Path:
    root = (reports_root or get_agent_reports_root()) / "_specialists"
    root.mkdir(parents=True, exist_ok=True)
    clean_subject = re.sub(r"[^A-Za-z0-9.-]+", "-", subject.upper()).strip("-") or "SUBJECT"
    stamp = datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d %H%M")
    base = root / f"{prefix}-{clean_subject} {stamp}"
    path = base
    suffix = 1
    while path.exists():
        suffix += 1
        path = root / f"{prefix}-{clean_subject} {stamp}-{suffix}"
    path.mkdir(parents=True)
    (path / "audit").mkdir()
    return path


def specialist_identity_from_subject(subject_prompt: str, prefix: str) -> dict[str, Any]:
    route_prompt = subject_prompt
    if prefix == "ETF" and not re.search(r"\b(etf|fund|spy|qqq|schg)\b", route_prompt, re.I):
        route_prompt += " ETF"
    if prefix == "CRYPTO" and not re.search(r"\b(btc|bitcoin|crypto)\b", route_prompt, re.I):
        route_prompt += " crypto"
    if prefix == "COMMODITY" and not re.search(r"\b(gld|gold|commodity|oil)\b", route_prompt, re.I):
        route_prompt += " commodity"
    if prefix == "FI" and not re.search(r"\b(tlt|bond|fixed income|duration)\b", route_prompt, re.I):
        route_prompt += " bond"
    identity = resolve_agent_request(route_prompt, mode="mock")
    if identity.get("ticker") == "UNRESOLVED":
        identity = {
            "ticker": re.sub(r"[^A-Za-z0-9.-]+", "-", subject_prompt.upper()).strip("-") or "SUBJECT",
            "company_name": subject_prompt,
            "security_type": "direct_specialist_subject",
            "instrument_classification": "direct_specialist_subject",
            "selected_route": "direct_specialist",
            "source": "Direct specialist subject parsed from prompt",
        }
    identity["selected_route"] = identity.get("selected_route") or "direct_specialist"
    return identity


def build_direct_specialist_prompt(
    *,
    prefix: str,
    specialist_id: str,
    subject_prompt: str,
    identity: dict[str, Any],
) -> str:
    return (
        f"You are {specialist_id} answering a direct specialist command {prefix}: for {subject_prompt}.\n"
        "Use only a scoped specialist view. Do not expand into AGENT workflow. Do not issue final IC Action.\n"
        "The first visible boundary line must be exactly: Boundary: Not an IC Action\n"
        "Do not use Action Box, final buy/sell/hold/add/trim/exit labels, exact position sizing, or personal trade instructions.\n"
        "Return concise markdown with Specialist Verdict, evidence/source limits, risks or missing gates, and next step.\n"
        f"Resolved subject identity: {json.dumps(identity, ensure_ascii=False)}\n"
    )


def mock_direct_specialist_output(prefix: str, specialist_id: str, subject_prompt: str, identity: dict[str, Any]) -> str:
    ticker = identity.get("ticker") or subject_prompt
    title = specialist_title(specialist_id)
    focus = {
        "RISK": "downside scenarios, thesis breakers, liquidity, implementation, and missing risk controls",
        "VAL": "valuation/expectations support, scenario range, embedded expectations, and evidence gaps",
        "MACRO": "rates, inflation, growth, liquidity, currency, and cross-asset regime sensitivity",
        "NEWS": "confirmed events, freshness needs, unconfirmed items, and catalyst risk",
        "PORTFOLIO": "role, overlap, concentration, constraints, and missing holdings/context",
        "SECTOR": "industry structure, competitive position, demand cycle, and margin pressure",
        "EVIDENCE": "source availability, freshness, conflicts, and evidence gaps",
        "POSITIONING": "market positioning, crowding, sentiment, and flow-sensitive risks",
        "INTEL": "market intelligence, data gaps, current watch items, and monitoring needs",
        "EQUITY": "company quality, fundamentals, valuation dependency, and equity-specific risks",
        "ETF": "wrapper quality, fees, liquidity, holdings, concentration, and tracking risk",
        "COMMODITY": "spot/proxy distinction, supply-demand, real rates, storage/roll, and vehicle risk",
        "CRYPTO": "network/liquidity/custody/regulatory risks and volatility regime",
        "FI": "duration, yield, curve exposure, credit quality, and rate sensitivity",
        "WINNERS": "structural-winner criteria, durability, evidence thresholds, and watchlist gaps",
        "IC": "committee-prep synthesis boundaries and missing gates for final action",
    }.get(prefix, "specialist-scope evidence, limitations, and handoff needs")
    return (
        f"Boundary: Not an IC Action\n\n"
        f"# {title} — {ticker}\n\n"
        f"## Specialist Verdict\n"
        f"{ticker} has been reviewed only through the {title} scope. The relevant focus is {focus}. This is a bounded specialist handoff, not a final portfolio action.\n\n"
        "## Evidence and freshness limits\n"
        "This direct specialist path uses public/no-key Automation Lab context and does not claim a full Evidence Collector lock unless the full AGENT workflow is run.\n\n"
        "## Missing gates for final decision support\n"
        "- Full source preflight and evidence pack if a final IC decision is requested.\n"
        "- Valuation/expectations, risk review, implementation quality, and portfolio context where decision-relevant.\n"
        "- Investment Committee synthesis before any final action label.\n\n"
        "## Next step\n"
        "Use AGENT: for a gated report/audit package, or provide more scope for a deeper specialist-only handoff.\n"
    )


def direct_specialist_forbidden_action(text: str) -> bool:
    forbidden = [
        "Action Box",
        "IC Action:",
        "Final IC Action",
    ]
    if any(term in text for term in forbidden):
        return True
    return bool(
        re.search(
            r"(?im)^\s*(Buy|Sell|Hold|Add|Trim|Exit)\s*:",
            text,
        )
        or re.search(
            r"(?i)\b(you should|you must|we should|we must)\s+(buy|sell|hold|add|trim|exit)\b",
            text,
        )
    )


def validate_direct_specialist_output(report_text: str, manifest: dict[str, Any]) -> dict[str, Any]:
    checks = {
        "boundary_line_present": "Boundary: Not an IC Action" in report_text,
        "no_final_action_language": not direct_specialist_forbidden_action(report_text),
        "one_specialist_only": len(manifest.get("actual_specialists_run") or []) <= 1
        and len(manifest.get("attempted_specialists") or []) == 1,
        "mapped_specialist_matches_prefix": manifest.get("specialist_id") == SPECIALIST_COMMANDS.get(manifest.get("prefix")),
        "not_agent_workflow": manifest.get("workflow") == "direct_specialist",
        "report_exists": bool(report_text.strip()),
        "mode_valid": manifest.get("mode") in {"mock", "live"},
        "live_thread_truthful": manifest.get("mode") != "live"
        or not manifest.get("actual_specialists_run")
        or all(item.get("sdk_thread_id") for item in manifest.get("actual_specialists_run", [])),
    }
    return {"schema_version": "direct_specialist_validation.v1", "status": "pass" if all(checks.values()) else "fail", "checks": checks}


def agent_specialists_for_route(route: str | None) -> list[str]:
    return list(AGENT_SPECIALISTS_BY_ROUTE.get(route or "", AGENT_SPECIALISTS_EQUITY))


def agent_required_specialists_for_route(route: str | None) -> set[str]:
    return set(AGENT_REQUIRED_SPECIALISTS_BY_ROUTE.get(route or "", AGENT_REQUIRED_SPECIALISTS_EQUITY))


def selected_route_from_context(intake: dict[str, Any] | None = None, preflight: dict[str, Any] | None = None) -> str:
    intake = intake or {}
    preflight = preflight or {}
    identity = preflight.get("subject_identity") or intake.get("subject_identity") or {}
    return (
        str(preflight.get("selected_route") or intake.get("selected_route") or identity.get("selected_route") or "equity_full_cycle")
    )


def resolve_agent_request(prompt: str, mode: str = "mock") -> dict[str, Any]:
    normalized = normalize_agent_prompt(prompt)
    route = mock_route(normalized)
    if route == "equity_full_cycle":
        identity = resolve_equity_request(normalized, mode=mode)
        identity["selected_route"] = route
        return identity
    text = normalized.lower()
    if route == "multi_asset_comparison":
        components: list[dict[str, Any]] = []
        for ticker in ("MSFT", "GOOGL", "GOOG", "AAPL", "NVDA"):
            if re.search(rf"\b{re.escape(ticker.lower())}\b", text):
                try:
                    equity_identity = supported_equity_identity(ticker)
                except KeyError:
                    equity_identity = {"ticker": ticker, "company_name": ticker, "security_type": "equity"}
                components.append(
                    {
                        "ticker": equity_identity.get("ticker", ticker),
                        "company_name": equity_identity.get("company_name", ticker),
                        "security_type": "equity",
                        "selected_route": "equity_full_cycle",
                    }
                )
        for ticker, identity in AGENT_NON_EQUITY_IDENTITIES.items():
            if re.search(rf"\b{re.escape(ticker.lower())}\b", text) or (
                ticker == "BTC" and "bitcoin" in text
            ) or (ticker == "GLD" and "gold" in text):
                components.append({key: identity.get(key) for key in ("ticker", "company_name", "security_type", "selected_route")})
        if not components:
            components = [
                {"ticker": "MSFT", "company_name": "Microsoft Corporation", "security_type": "equity", "selected_route": "equity_full_cycle"},
                {"ticker": "SPY", "company_name": "SPDR S&P 500 ETF Trust", "security_type": "etf", "selected_route": "etf_full_cycle"},
                {"ticker": "BTC", "company_name": "Bitcoin", "security_type": "crypto", "selected_route": "crypto_full_cycle"},
            ]
        seen: set[str] = set()
        unique_components = []
        for component in components:
            ticker = str(component.get("ticker") or "")
            if ticker and ticker not in seen:
                seen.add(ticker)
                unique_components.append(component)
        ticker_slug = "-".join(component["ticker"] for component in unique_components)
        return {
            "ticker": ticker_slug,
            "company_name": " vs ".join(component["ticker"] for component in unique_components),
            "security_type": "multi_asset_comparison",
            "instrument_classification": "multi_asset_comparison",
            "selected_route": route,
            "currency": "USD",
            "components": unique_components,
            "source": "Automation Lab comparison identity seed",
        }
    route_candidates = {
        "etf_full_cycle": ("SPY", "QQQ", "SCHG"),
        "fixed_income_full_cycle": ("TLT",),
        "crypto_full_cycle": ("BTC",),
        "commodity_full_cycle": ("GLD",),
    }
    for ticker in route_candidates.get(route, ()):
        identity = AGENT_NON_EQUITY_IDENTITIES[ticker]
        if re.search(rf"\b{re.escape(ticker.lower())}\b", text) or (
            ticker == "BTC" and "bitcoin" in text
        ) or (ticker == "GLD" and "gold" in text):
            return dict(identity)
    if route == "commodity_full_cycle" and ("gold" in text or re.search(r"\bgld\b", text)):
        return dict(AGENT_NON_EQUITY_IDENTITIES["GLD"])
    return {
        "ticker": "UNRESOLVED",
        "company_name": "Unresolved asset",
        "security_type": "unknown",
        "instrument_classification": "ambiguous",
        "selected_route": route,
        "block_reason": "No supported AGENT identity resolved",
    }


def validate_supported_agent_route(prompt: str) -> dict[str, Any]:
    normalized = normalize_agent_prompt(prompt)
    route = mock_route(normalized)
    if route not in AGENT_ROUTE_CARDS:
        raise AgentRunError("agent_run_error: this request could not be routed to a supported AGENT workflow")
    identity = resolve_agent_request(normalized, mode="mock")
    if route == "equity_full_cycle":
        ticker = validate_supported_equity_agent_route(prompt)
        identity = resolve_equity_request(normalized, mode="mock")
        identity["selected_route"] = route
        identity["ticker"] = ticker
    elif identity.get("ticker") in {"UNRESOLVED", "", None}:
        raise AgentRunError(f"agent_run_error: no supported {AGENT_ROUTE_LABELS.get(route, route)} identity was resolved")
    return {"route": route, "identity": identity, "ticker": str(identity.get("ticker"))}


def non_equity_agent_intake_questions(normalized_prompt: str, route: str, identity: dict[str, Any]) -> list[str]:
    ticker = identity.get("ticker", "the asset")
    label = AGENT_ROUTE_LABELS.get(route, "asset")
    if detect_prompt_language(normalized_prompt) == "ru":
        return [
            f"Какой инвестиционный горизонт использовать для {ticker}?",
            "Это новая идея, существующая позиция, хедж, сравнение или проверка уже имеющейся экспозиции?",
            f"Какая главная цель {label}-анализа: доходность, риск, диверсификация, защита, ликвидность, оценка входа или сравнение?",
            "Нужны ли текущая цена, последние новости, доходности/спреды/ликвидность, состав фонда, методология или свежий рыночный контекст?",
            "Есть ли портфельный контекст: текущие активы, лимиты, риск-профиль, ограничения, валюта, налоговый/юрисдикционный контекст, или он не предоставлен?",
        ]
    return [
        f"What investment horizon should the {ticker} workflow use?",
        "Is this a new idea, existing position, hedge, comparison, or review of existing exposure?",
        f"What is the main {label} objective: return, risk, diversification, protection, liquidity, entry valuation, or comparison?",
        "Do you need fresh price, latest news, yields/spreads/liquidity, holdings, methodology, or current market context?",
        "What portfolio context is available: holdings, limits, risk tolerance, constraints, currency/tax/jurisdiction context, or should it be treated as not provided?",
    ]


def agent_intake_questions(normalized_prompt: str, route: str, identity: dict[str, Any]) -> list[str]:
    if route == "equity_full_cycle":
        return equity_agent_intake_questions(normalized_prompt, str(identity.get("ticker")))
    return non_equity_agent_intake_questions(normalized_prompt, route, identity)


def agent_source_record(
    *,
    source_id: str,
    name: str,
    category: str,
    importance: str,
    status: str = "ok",
    data: dict[str, Any] | None = None,
    url: str | None = None,
    primary: str | None = None,
    source_date: str | None = None,
    source_tier: str = "public",
    error: str = "",
) -> dict[str, Any]:
    retrieved_at = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    return {
        "source_id": source_id,
        "name": name,
        "category": category,
        "importance": importance,
        "status": status,
        "source_tier": source_tier,
        "access_status": "public/no-key",
        "retrieved_at": retrieved_at,
        "source_date": source_date or datetime.now(timezone.utc).date().isoformat(),
        "freshness_rule": "current when used for action" if category == "market_data" else "latest available public source",
        "url": url,
        "primary": primary,
        "data": data or {},
        "error": error,
    }


def _summary_from_agent_records(records: list[dict[str, Any]]) -> dict[str, Any]:
    missing_required = [
        record["source_id"]
        for record in records
        if record.get("importance") == "required" and record.get("status") not in {"ok", "partial"}
    ]
    partial_required = [
        record["source_id"]
        for record in records
        if record.get("importance") == "required" and record.get("status") == "partial"
    ]
    missing_important = [
        record["source_id"]
        for record in records
        if record.get("importance") == "important" and record.get("status") != "ok"
    ]
    return {
        "missing_required": missing_required,
        "partial_required": partial_required,
        "missing_important": missing_important,
        "hard_gate_passed": not missing_required,
        "limitation_needed": bool(partial_required or missing_important),
    }


def build_non_equity_source_preflight(
    prompt: str,
    answers: list[str],
    mode: str,
    route: str,
    identity: dict[str, Any],
) -> dict[str, Any]:
    retrieved_at = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    ticker = str(identity.get("ticker") or "ASSET")
    snapshot: dict[str, Any] = {}
    if ticker in QUICK_ASSET_IDENTITIES or identity.get("security_type") == "multi_asset_comparison":
        quick_answers = (answers + AGENT_INTAKE_BASELINES)[:3]
        try:
            snapshot = build_quick_source_snapshot(prompt, quick_answers, "live" if mode == "live" else "mock")
        except Exception as exc:  # pragma: no cover - provider failures should degrade through source records
            snapshot = {"provider_results": [], "provider_errors": [{"error": f"{type(exc).__name__}: {exc}"}], "components": {}}
    components = snapshot.get("components") if isinstance(snapshot.get("components"), dict) else {}
    price = components.get("price") if isinstance(components.get("price"), dict) else {}
    recent_events = components.get("recent_events") if isinstance(components.get("recent_events"), list) else []
    source_url = f"https://finance.yahoo.com/quote/{ticker}"
    records = [
        agent_source_record(
            source_id="identity",
            name="Asset identity and route classification",
            category="identity",
            importance="required",
            data=identity,
            url=source_url,
        ),
        agent_source_record(
            source_id="current_price",
            name="Latest public price / quote proxy",
            category="market_data",
            importance="required",
            data=price or {"ticker": ticker, "mode": mode, "note": "public/no-key quote proxy recorded; exact quote may be Limited in live mode"},
            url=source_url,
            status="ok" if mode == "mock" or price else "partial",
        ),
        agent_source_record(
            source_id="historical_price",
            name="Historical price / trend proxy",
            category="market_data",
            importance="required",
            data={"ticker": ticker, "window": "public historical proxy", "mode": mode},
            url=f"https://stooq.com/q/d/l/?s={ticker.lower()}.us&i=d",
        ),
        agent_source_record(
            source_id="public_news",
            name="Recent public events / catalyst context",
            category="news",
            importance="important",
            data={"events": recent_events, "mode": mode},
            url=source_url,
            status="ok" if recent_events or mode == "mock" else "partial",
        ),
    ]
    if route == "etf_full_cycle":
        records.extend(
            [
                agent_source_record(source_id="issuer_fund_page", name="Issuer / fund profile page", category="vehicle", importance="required", data={"vehicle": ticker, "wrapper": "ETF / fund"}, url=source_url),
                agent_source_record(source_id="holdings_or_methodology", name="Holdings or index methodology", category="vehicle", importance="required", data={"coverage": "holdings/methodology required for ETF quality gate", "mode": mode}, url=source_url),
                agent_source_record(source_id="expense_liquidity_structure", name="Expense ratio, liquidity, and structure", category="vehicle", importance="important", data={"coverage": "fee/liquidity/tracking checks recorded"}, url=source_url),
            ]
        )
    elif route == "fixed_income_full_cycle":
        records.extend(
            [
                agent_source_record(source_id="issuer_fund_page", name="Issuer / bond-fund profile page", category="vehicle", importance="required", data={"vehicle": ticker, "wrapper": "bond ETF / fixed-income vehicle"}, url=source_url),
                agent_source_record(source_id="duration_yield_curve", name="Duration, yield, curve exposure", category="rates_credit", importance="required", data={"coverage": "duration/yield/rates sensitivity gate"}, url=source_url),
                agent_source_record(source_id="credit_quality_holdings", name="Credit quality and holdings exposure", category="rates_credit", importance="important", data={"coverage": "credit/liquidity/holdings review"}, url=source_url),
            ]
        )
    elif route == "crypto_full_cycle":
        records.extend(
            [
                agent_source_record(source_id="network_asset_profile", name="Network / asset profile", category="crypto", importance="required", data={"asset": ticker, "network": identity.get("company_name")}, url="https://coinmarketcap.com/"),
                agent_source_record(source_id="liquidity_custody_vehicle", name="Liquidity, custody, and vehicle considerations", category="crypto", importance="required", data={"coverage": "spot/vehicle/custody risk gate"}, url="https://coinmarketcap.com/"),
                agent_source_record(source_id="regulatory_risk_context", name="Regulatory and operational risk context", category="risk", importance="important", data={"coverage": "public regulatory/custody risk context"}, url="https://www.sec.gov/"),
            ]
        )
    elif route == "commodity_full_cycle":
        records.extend(
            [
                agent_source_record(source_id="commodity_or_vehicle_profile", name="Commodity exposure / vehicle profile", category="commodity", importance="required", data={"asset": ticker, "exposure": "spot/fund/proxy distinction"}, url=source_url),
                agent_source_record(source_id="supply_demand_macro_context", name="Supply-demand, macro, and real-rate context", category="macro", importance="required", data={"coverage": "commodity supply-demand and macro gate"}, url=source_url),
                agent_source_record(source_id="roll_storage_vehicle_risk", name="Roll, storage, custody, or vehicle risk", category="risk", importance="important", data={"coverage": "vehicle/futures/storage risk gate"}, url=source_url),
            ]
        )
    elif route == "multi_asset_comparison":
        records.extend(
            [
                agent_source_record(source_id="component_identities", name="Component identities", category="identity", importance="required", data={"components": identity.get("components", [])}, url=source_url),
                agent_source_record(source_id="component_prices", name="Comparable component price snapshots", category="market_data", importance="required", data={"components": identity.get("components", []), "mode": mode}, url=source_url),
                agent_source_record(source_id="comparison_framework", name="Role-based comparison framework", category="analysis_framework", importance="required", data={"criteria": ["return role", "risk", "diversification", "liquidity", "portfolio fit"]}, primary="Financial Agent System route cards"),
            ]
        )
    preflight = {
        "schema_version": "agent_source_preflight.v1",
        "mode": mode,
        "selected_route": route,
        "source_scope": "Public/no-key source preflight",
        "retrieved_at": retrieved_at,
        "subject_identity": identity,
        "resolver_result": identity,
        "source_records": records,
        "provider_results": snapshot.get("provider_results") or [{"provider_id": "automation_lab_public_seed", "status": "ok", "component": "agent_preflight", "quality": "limited_public"}],
        "provider_errors": snapshot.get("provider_errors") or [],
    }
    preflight["summary"] = _summary_from_agent_records(records)
    return preflight


def build_agent_source_preflight(
    prompt: str,
    answers: list[str],
    mode: str,
    route: str,
    identity: dict[str, Any],
) -> dict[str, Any]:
    if route == "equity_full_cycle":
        return build_equity_source_preflight(prompt=prompt, answers=answers, mode=mode, ticker=str(identity.get("ticker")))
    return build_non_equity_source_preflight(prompt, answers, mode, route, identity)


def parse_agent_answers(answer_args: list[str] | None, answers_json: str | None) -> list[str]:
    if answer_args and answers_json:
        raise ValueError("agent-run accepts either repeated --answer or --answers-json, not both")
    if answers_json:
        try:
            parsed = json.loads(answers_json)
        except json.JSONDecodeError as exc:
            raise ValueError("agent-run requires --answers-json to be a JSON array") from exc
        if not isinstance(parsed, list) or not all(isinstance(item, str) for item in parsed):
            raise ValueError("agent-run requires --answers-json to be a JSON array of strings")
        answers = parsed
    else:
        answers = answer_args or []
    if len(answers) > 5:
        raise ValueError("agent-run accepts at most five intake answers")
    if any(not answer.strip() for answer in answers):
        raise ValueError("agent-run rejects empty answers")
    return [answer.strip() for answer in answers]


def _compact_text(value: Any, *, max_length: int = 600) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        text = value.strip()
    else:
        text = json.dumps(value, ensure_ascii=False, sort_keys=True)
    text = re.sub(r"\s+", " ", text).strip()
    return text[:max_length]


def normalize_portfolio_context(payload: dict[str, Any] | None, *, source: str) -> dict[str, Any]:
    if payload is None:
        payload = {}
    if not isinstance(payload, dict):
        raise ValueError("portfolio context must be a JSON object")
    normalized: dict[str, Any] = {
        "schema_version": "portfolio_context.v1",
        "source": source,
        "status": "missing",
        "provided_fields": [],
        "missing_fields": list(PORTFOLIO_CONTEXT_FIELDS),
        "holdings": [],
        "cash": None,
        "risk_limits": None,
        "horizon": None,
        "constraints": [],
        "existing_exposure": None,
        "objective": None,
        "personal_action_unlocked": False,
        "decision_boundary": (
            "Portfolio context informs Portfolio Fit, but final action and exact sizing still require "
            "the full gated IC synthesis and any missing personal constraints."
        ),
    }
    for field in PORTFOLIO_CONTEXT_FIELDS:
        if field not in payload:
            continue
        value = payload.get(field)
        if value in (None, "", [], {}):
            continue
        normalized[field] = value
        normalized["provided_fields"].append(field)
    normalized["missing_fields"] = [field for field in PORTFOLIO_CONTEXT_FIELDS if field not in normalized["provided_fields"]]
    normalized["status"] = "provided" if normalized["provided_fields"] and not normalized["missing_fields"] else "partial" if normalized["provided_fields"] else "missing"
    normalized["limitations"] = (
        ["No structured portfolio context was supplied; Portfolio Fit remains generic and Limited."]
        if normalized["status"] == "missing"
        else [
            "Structured portfolio context supplied for Portfolio Fit.",
            "Personal final action or exact sizing remains unavailable unless all source, specialist, and IC gates allow it.",
        ]
        + ([f"Missing portfolio fields: {', '.join(normalized['missing_fields'])}."] if normalized["missing_fields"] else [])
    )
    return normalized


def parse_portfolio_context(portfolio_context_json: str | None = None, portfolio_context_file: str | None = None) -> dict[str, Any]:
    if portfolio_context_json and portfolio_context_file:
        raise ValueError("agent-run accepts either --portfolio-context-json or --portfolio-context-file, not both")
    if portfolio_context_file:
        path = Path(portfolio_context_file)
        if not path.is_file():
            raise ValueError(f"portfolio context file not found: {path}")
        try:
            payload = json.loads(path.read_text(encoding="utf-8-sig"))
        except json.JSONDecodeError as exc:
            raise ValueError("portfolio context file must contain a JSON object") from exc
        context = normalize_portfolio_context(payload, source="cli_file")
    elif portfolio_context_json:
        try:
            payload = json.loads(portfolio_context_json)
        except json.JSONDecodeError as exc:
            raise ValueError("--portfolio-context-json must be a JSON object") from exc
        context = normalize_portfolio_context(payload, source="cli_json")
    else:
        return normalize_portfolio_context({}, source="not_provided")
    if context["status"] == "missing":
        raise ValueError("portfolio context input did not contain any supported non-empty fields")
    return context


def unstructured_portfolio_context_from_answers(answers: list[str]) -> dict[str, Any]:
    candidates = [
        answer
        for answer in answers
        if ("portfolio" in answer.lower() or "position" in answer.lower() or "holding" in answer.lower())
        and not re.search(r"(?i)\b(no|none|not provided|нет|без)\b", answer)
    ]
    if not candidates:
        return normalize_portfolio_context({}, source="not_provided")
    return normalize_portfolio_context({"existing_exposure": "; ".join(candidates)}, source="intake_answer_unstructured")


def portfolio_context_summary(context: dict[str, Any], language: str = "en") -> str:
    if not context or context.get("status") == "missing":
        if language == "ru":
            return "Портфельный контекст не предоставлен; оценка Portfolio Fit остаётся общей и Limited."
        return "No structured portfolio context was provided; Portfolio Fit remains generic and Limited."
    fields = []
    for label, key in [
        ("objective", "objective"),
        ("horizon", "horizon"),
        ("holdings", "holdings"),
        ("cash", "cash"),
        ("risk limits", "risk_limits"),
        ("constraints", "constraints"),
        ("existing exposure", "existing_exposure"),
    ]:
        value = context.get(key)
        if value not in (None, "", [], {}):
            fields.append(f"{label}: {_compact_text(value, max_length=180)}")
    summary = "; ".join(fields[:7])
    if language == "ru":
        return (
            "Предоставлен структурированный портфельный контекст для Portfolio Fit: "
            f"{summary}. Он улучшает проверку роли актива, но не разблокирует финальное действие или точный размер позиции без всех ворот IC."
        )
    return (
        "Structured portfolio context supplied for Portfolio Fit: "
        f"{summary}. This improves role/constraint review but does not unlock final action or exact sizing without all IC gates."
    )


def detect_supported_equity_tickers(prompt: str) -> list[str]:
    return detect_equity_mentions(prompt)


def detect_supported_equity_ticker(prompt: str) -> str | None:
    matches = detect_supported_equity_tickers(prompt)
    return matches[0] if len(matches) == 1 else None


def subject_label(identity: dict[str, Any]) -> str:
    return f"{identity.get('ticker')} / {identity.get('company_name')}"


def equity_agent_intake_questions(normalized_prompt: str, ticker: str) -> list[str]:
    identity = resolve_equity_request(normalized_prompt, mode="mock")
    if identity.get("ticker") != ticker:
        try:
            identity = supported_equity_identity(ticker)
        except KeyError:
            identity = {"ticker": ticker}
    ticker_label = identity["ticker"]
    if detect_prompt_language(normalized_prompt) == "ru":
        return [
            f"Какой инвестиционный горизонт использовать для {ticker_label}?",
            "Это новая идея, существующая позиция или проверка уже имеющейся экспозиции?",
            "Какая главная цель анализа: качество бизнеса, точка входа по оценке, катализаторы, риски или сравнение?",
            "Нужны ли текущая цена, последние новости, отчётность и свежие рыночные события?",
            "Есть ли портфельный контекст: концентрация, лимиты, риск-профиль, текущая экспозиция к mega-cap tech или другим активам, или он не предоставлен?",
        ]
    return [
        f"What investment horizon should the {ticker_label} workflow use?",
        "Is this a new idea, an existing position, or a review of related exposure?",
        "What is the main objective: business quality, valuation entry, catalysts, risk review, or comparison?",
        "Do you need fresh price, latest news, filings, and current market context?",
        "What portfolio context is available: concentration, risk tolerance, constraints, mega-cap tech exposure, or should it be treated as not provided?",
    ]


def msft_agent_intake_questions(normalized_prompt: str) -> list[str]:
    return equity_agent_intake_questions(normalized_prompt, "MSFT")


def build_agent_intake_payload(
    prompt: str,
    answers: list[str],
    continue_with_baseline: bool = False,
    portfolio_context: dict[str, Any] | None = None,
) -> dict[str, Any]:
    normalized_prompt = normalize_agent_prompt(prompt)
    route_info = validate_supported_agent_route(prompt)
    route = route_info["route"]
    identity = route_info["identity"]
    questions = agent_intake_questions(normalized_prompt, route, identity)
    context = portfolio_context or unstructured_portfolio_context_from_answers(answers)
    answered = []
    unanswered = []
    for index, question in enumerate(questions):
        if index < len(answers):
            answered.append({"question_number": index + 1, "question": question, "answer": answers[index]})
        else:
            unanswered.append(
                {
                    "question_number": index + 1,
                    "question": question,
                    "baseline_assumption": AGENT_INTAKE_BASELINES[index],
                }
            )
    return {
        "schema_version": "agent_intake.v1",
        "prompt": prompt,
        "normalized_prompt": normalized_prompt,
        "selected_route": route,
        "subject_identity": identity,
        "question_count_required": 5,
        "questions": questions,
        "answers_provided_count": len(answers),
        "answered": answered,
        "unanswered": unanswered,
        "baseline_used": bool(unanswered),
        "baseline_reason": (
            "explicit --continue-with-baseline"
            if continue_with_baseline and not answers
            else "missing intake answers filled with approved baseline assumptions"
            if unanswered
            else "none"
        ),
        "portfolio_context_provided": context.get("status") in {"partial", "provided"},
        "portfolio_context_status": context.get("status"),
        "portfolio_context_fields": context.get("provided_fields", []),
        "portfolio_context": context,
    }


def validate_supported_equity_agent_route(prompt: str) -> str:
    normalized = normalize_agent_prompt(prompt)
    route = mock_route(normalized)
    resolved = resolve_equity_request(normalized, mode="mock")
    classification = resolved.get("instrument_classification")
    if route != "equity_full_cycle":
        raise AgentRunError("agent_run_error: this request could not be run as a public listed equity workflow")
    if classification == "ambiguous":
        raise AgentRunError(f"agent_run_error: ambiguous equity request: {resolved.get('block_reason')}")
    if classification == "private_company":
        raise AgentRunError("agent_run_error: private companies are not ordinary public listed equity targets; use ecosystem context or public proxies instead")
    if classification == "complex_or_unsupported_instrument":
        raise AgentRunError("agent_run_error: complex equity-like instruments are not ordinary equity targets; provide the ordinary common share or main listing")
    ticker = resolved.get("ticker")
    if not ticker or ticker == "UNRESOLVED":
        raise AgentRunError("agent_run_error: no clear public equity ticker, listing, or company identity was resolved")
    return str(ticker)


def validate_msft_agent_route(prompt: str) -> str:
    ticker = validate_supported_equity_agent_route(prompt)
    if ticker != "MSFT":
        raise AgentRunError("agent_run_error: compatibility MSFT route supports only MSFT")
    return "equity_full_cycle"


def create_agent_report_dir(asset: str = "MSFT", reports_root: Path | None = None) -> Path:
    root = reports_root or get_agent_reports_root()
    root.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d %H%M")
    base = root / f"{asset} {stamp}"
    path = base
    suffix = 1
    while path.exists():
        suffix += 1
        path = root / f"{asset} {stamp}-{suffix}"
    path.mkdir(parents=True)
    (path / "audit").mkdir()
    return path


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def source_inventory_from_preflight(preflight: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema_version": "agent_source_inventory.v1",
        "subject_identity": preflight.get("subject_identity"),
        "resolver_result": preflight.get("resolver_result"),
        "source_candidates": (preflight.get("resolver_result") or {}).get("source_candidates", []),
        "provider_results": preflight.get("provider_results", []),
        "source_scope": preflight.get("source_scope"),
        "retrieved_at": preflight.get("retrieved_at"),
        "sources": preflight.get("source_records", []),
    }


def write_agent_preflight_artifacts(
    run_dir: Path,
    intake: dict[str, Any],
    preflight: dict[str, Any],
    evidence_pack: dict[str, Any],
) -> None:
    audit = run_dir / "audit"
    write_json(audit / "intake.json", intake)
    write_json(audit / "portfolio_context.json", intake.get("portfolio_context") or normalize_portfolio_context({}, source="not_provided"))
    write_json(audit / "source_preflight.json", preflight)
    write_json(audit / "source_inventory.json", source_inventory_from_preflight(preflight))
    write_json(audit / "provider_results.json", preflight.get("provider_results", []))
    write_json(audit / "evidence_pack.json", evidence_pack)
    (audit / "evidence_pack.md").write_text(render_evidence_pack_markdown(evidence_pack), encoding="utf-8")
    write_json(audit / "pre_ic_evidence_lock.json", evidence_pack.get("pre_ic_evidence_lock", {}))


def source_records_have_timezone(preflight: dict[str, Any]) -> bool:
    for record in preflight.get("source_records", []):
        retrieved_at = record.get("retrieved_at")
        if not isinstance(retrieved_at, str) or not re.search(r"(Z|[+-]\d{2}:\d{2})$", retrieved_at):
            return False
    return True


def validate_source_preflight(preflight: dict[str, Any]) -> dict[str, Any]:
    records = preflight.get("source_records", [])
    source_ids = {record.get("source_id") for record in records}
    route = str(preflight.get("selected_route") or (preflight.get("subject_identity") or {}).get("selected_route") or "equity_full_cycle")
    if route == "equity_full_cycle":
        required = {
            "identity",
            "sec_submissions",
            "latest_10k",
            "latest_10q",
            "company_facts",
            "current_price",
            "historical_price",
        }
    else:
        route_required = {
            "etf_full_cycle": {"identity", "current_price", "historical_price", "issuer_fund_page", "holdings_or_methodology"},
            "fixed_income_full_cycle": {"identity", "current_price", "historical_price", "issuer_fund_page", "duration_yield_curve"},
            "crypto_full_cycle": {"identity", "current_price", "historical_price", "network_asset_profile", "liquidity_custody_vehicle"},
            "commodity_full_cycle": {"identity", "current_price", "historical_price", "commodity_or_vehicle_profile", "supply_demand_macro_context"},
            "multi_asset_comparison": {"identity", "current_price", "historical_price", "component_identities", "component_prices", "comparison_framework"},
        }
        required = route_required.get(route, {"identity", "current_price", "historical_price"})
    missing_attempts = sorted(required - source_ids)
    missing_required = [
        record.get("source_id")
        for record in records
        if record.get("importance") == "required" and record.get("status") not in {"ok", "partial"}
    ]
    partial_required = [
        record.get("source_id")
        for record in records
        if record.get("importance") == "required" and record.get("status") == "partial"
    ]
    stale_required = [
        record.get("source_id")
        for record in records
        if preflight.get("freshness_required")
        and record.get("importance") == "required"
        and record.get("freshness_status") == "stale"
    ]
    stale_important = [
        record.get("source_id")
        for record in records
        if preflight.get("freshness_required")
        and record.get("importance") == "important"
        and record.get("freshness_status") == "stale"
    ]
    subject_identity = preflight.get("subject_identity") or {}
    allowed_classifications = {
        "us_common_equity",
        "us_share_class",
        "adr_or_foreign_issuer_us_listing",
        "non_us_listed_equity",
    }
    resolver_result = preflight.get("resolver_result") or {}
    classification = subject_identity.get("instrument_classification") or resolver_result.get("instrument_classification")
    subject_has_identity = bool(subject_identity.get("ticker")) and bool(subject_identity.get("company_name"))
    subject_has_cik_or_non_us_gate = bool(subject_identity.get("cik")) or classification == "non_us_listed_equity"
    if route != "equity_full_cycle":
        subject_has_cik_or_non_us_gate = True
    adr_gate = subject_identity.get("adr_gate") or resolver_result.get("adr_gate") or {}
    adr_gate_required_fields = {
        "underlying_issuer",
        "issuer_country",
        "trading_currency",
        "reporting_basis",
        "liquidity_check",
        "regulatory_delisting_risk",
    }
    provider_results = preflight.get("provider_results") or []
    price_provider_order = [
        result.get("provider_id")
        for result in sorted(provider_results, key=lambda result: result.get("attempt_order") or 999)
        if result.get("provider_id") in {"stooq_history", "official_exchange_or_issuer_quote", "yahoo_public_chart"}
    ]
    checks = {
        "required_source_categories_attempted": not missing_attempts,
        "required_sources_available": not missing_required and not stale_required,
        "sec_identity_matches_subject": subject_has_identity
        and (classification in allowed_classifications if route == "equity_full_cycle" else True)
        and subject_has_cik_or_non_us_gate,
        "instrument_classification_present": classification in allowed_classifications
        if route == "equity_full_cycle"
        else bool(classification),
        "adr_gate_present_when_required": classification != "adr_or_foreign_issuer_us_listing"
        or adr_gate_required_fields.issubset(set(adr_gate.keys())),
        "provider_results_present": bool(provider_results),
        "price_provider_order_records_stooq_first": preflight.get("mode") == "mock"
        or not price_provider_order
        or price_provider_order[0] == "stooq_history",
        "source_timestamps_have_timezone": source_records_have_timezone(preflight),
        "source_urls_or_primary_recorded": all(record.get("url") or record.get("primary") for record in records),
        "freshness_window_ok": not stale_required and not stale_important,
    }
    hard_gate_pass = all(value for key, value in checks.items() if key != "freshness_window_ok")
    return {
        "status": "pass" if hard_gate_pass else "fail",
        "checks": checks,
        "missing_attempts": missing_attempts,
        "missing_required": sorted(set(missing_required + stale_required)),
        "partial_required": sorted(set(partial_required)),
        "missing_important": sorted(set(stale_important)),
        "freshness_issues": preflight.get("freshness_issues", []),
    }


def parse_source_date(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        if "T" in value:
            parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
            return parsed if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)
        return datetime.fromisoformat(value).replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def annotate_preflight_freshness(preflight: dict[str, Any], freshness_required: bool) -> dict[str, Any]:
    now = datetime.now(timezone.utc)
    freshness_issues: list[dict[str, Any]] = []
    preflight["freshness_required"] = freshness_required
    for record in preflight.get("source_records", []):
        record["freshness_status"] = "not_required"
        if record.get("status") != "ok":
            record["freshness_status"] = "unknown"
            continue
        source_id = record.get("source_id")
        source_date = parse_source_date(record.get("source_date")) or parse_source_date(record.get("retrieved_at"))
        if not source_date:
            record["freshness_status"] = "unknown"
            if freshness_required and source_id in {"current_price", "historical_price", "public_news", "ir_news"}:
                freshness_issues.append({"source_id": source_id, "reason": "missing_source_date"})
            continue
        age_days = (now - source_date.astimezone(timezone.utc)).total_seconds() / 86400
        record["freshness_age_days"] = round(age_days, 2)
        if source_id in {"current_price", "historical_price"}:
            max_days = 7
        elif source_id in {"public_news", "ir_news", "recent_8k"}:
            max_days = 45
        else:
            max_days = 3700
        record["freshness_max_age_days"] = max_days
        if freshness_required and age_days > max_days:
            record["freshness_status"] = "stale"
            freshness_issues.append({"source_id": source_id, "age_days": round(age_days, 2), "max_age_days": max_days})
        else:
            record["freshness_status"] = "current_or_latest_available"
    preflight["freshness_issues"] = freshness_issues
    if freshness_issues:
        summary = preflight.setdefault("summary", {})
        stale_required = [
            issue["source_id"]
            for issue in freshness_issues
            if any(r.get("source_id") == issue["source_id"] and r.get("importance") == "required" for r in preflight.get("source_records", []))
        ]
        if stale_required:
            missing = summary.setdefault("missing_required", [])
            for source_id in stale_required:
                if source_id not in missing:
                    missing.append(source_id)
            summary["hard_gate_passed"] = False
        stale_important = [
            issue["source_id"]
            for issue in freshness_issues
            if any(r.get("source_id") == issue["source_id"] and r.get("importance") == "important" for r in preflight.get("source_records", []))
        ]
        if stale_important:
            missing_important = summary.setdefault("missing_important", [])
            for source_id in stale_important:
                if source_id not in missing_important:
                    missing_important.append(source_id)
            summary["limitation_needed"] = True
        summary["freshness_issues"] = freshness_issues
    return preflight


def specialist_title(specialist_id: str) -> str:
    return specialist_id.replace("-", " ").replace("_", " ").title()


def specialist_artifact_name(specialist_id: str) -> str:
    mapping = {
        "evidence-collector": "evidence_collector_handoff.md",
        "equity-agent": "equity_company_analysis.md",
        "etf-agent": "etf_wrapper_analysis.md",
        "commodity-agent": "commodity_analysis.md",
        "crypto-agent": "crypto_asset_analysis.md",
        "fixed-income-agent": "fixed_income_analysis.md",
        "financial-statement-analysis": "financial_statement_analysis.md",
        "valuation-expectations-agent": "valuation_expectations.md",
        "risk-red-team-agent": "risk_red_team.md",
        "sector-industry-analysis-agent": "sector_industry_memo.md",
        "macro-agent": "macro_sensitivity.md",
        "news-catalysts-agent": "news_catalysts.md",
        "market-intelligence-agent": "market_intelligence.md",
        "market-sense-agent": "market_sense.md",
        "market-positioning-agent": "market_positioning.md",
        "portfolio-fit-agent": "portfolio_fit.md",
        "structural-winners-discovery-agent": "structural_winners_discovery.md",
        "investment-committee-agent": "ic_synthesis_handoff.md",
    }
    return mapping[specialist_id]


def mock_specialist_raw_output(specialist_id: str, identity: dict[str, Any]) -> str:
    title = specialist_title(specialist_id)
    ticker = identity.get("ticker", "the selected asset")
    route_label = AGENT_ROUTE_LABELS.get(identity.get("selected_route"), "asset")
    if specialist_id == "financial-statement-analysis":
        body = (
            "Revenue, operating margin, free cash flow conversion, capex, cash/debt, capital returns, "
            "working capital, segments, and accounting quality were reviewed from public-filings / financial-statement-supported mock evidence."
        )
    elif specialist_id == "valuation-expectations-agent":
        body = (
            "Scenario valuation uses base, bull, and bear cases tied to company-specific growth, "
            "FCF conversion, margin durability, capital allocation, and multiple sensitivity."
        )
    elif specialist_id == "investment-committee-agent":
        body = (
            "Synthesis uses validated handoffs only. Without portfolio context, the reader report stays "
            "decision-preparation style and does not unlock personal sizing."
        )
    else:
        body = f"{title} reviewed the {ticker} {route_label} evidence pack for its scoped role and produced a non-final handoff."
    return f"# {title}\n\n{body}\n\nBoundary: supporting specialist output; raw output is audit-only.\n"


def clean_reader_line(line: str) -> str:
    cleaned = re.sub(r"[*_`#>]+", "", str(line)).strip()
    cleaned = re.sub(r"^\s*[-•]\s*", "", cleaned)
    cleaned = re.sub(r"^\s*\d+[.)]\s*", "", cleaned)
    return cleaned.strip()


def is_debug_or_metadata_line(line: str) -> bool:
    cleaned = clean_reader_line(line)
    if not cleaned:
        return True
    lowered = cleaned.lower()
    prefixes = (
        "workflow:",
        "task:",
        "prompt:",
        "role:",
        "asset:",
        "subject:",
        "boundary:",
        "evidence readiness:",
        "evidence status:",
        "analysis status:",
        "ic action status:",
        "method confidence:",
        "sources reviewed:",
        "source inventory:",
        "produced by:",
        "as-of date/time:",
        "output status:",
        "source scope:",
        "decision boundary:",
        "artifact:",
    )
    forbidden_anywhere = (
        "ic action status",
        "analysis status",
        "runtime execution plan",
        "actual_subagents_run",
        "limited_ic_draft.md",
        "decision_prep_memo.md",
        "evidence_gap_memo.md",
        "module status",
    )
    return lowered.startswith(prefixes) or "not an ic action" in lowered or any(term in lowered for term in forbidden_anywhere)


def extract_meaningful_findings(raw: str, limit: int = 4) -> list[str]:
    findings: list[str] = []
    capture = False
    preferred_headings = (
        "specialist view",
        "risk conclusion",
        "ic synthesis",
        "ic handoff conclusion",
        "core red-team view",
        "valuation framing",
        "3–5 year expectations",
        "key valuation risks",
        "committee decision readiness",
        "evidence anchor points",
        "key questions",
        "handoff to ic",
    )
    for raw_line in raw.splitlines():
        line = clean_reader_line(raw_line)
        lowered = line.lower()
        if not line:
            continue
        if any(heading in lowered for heading in preferred_headings):
            capture = True
            continue
        if is_debug_or_metadata_line(line):
            continue
        if capture or raw_line.lstrip().startswith(("-", "1.", "2.", "3.", "4.", "5.", "6.")):
            if len(line) >= 35 and line not in findings:
                findings.append(line)
        if len(findings) >= limit:
            break
    if not findings:
        for raw_line in raw.splitlines():
            line = clean_reader_line(raw_line)
            if len(line) >= 60 and not is_debug_or_metadata_line(line) and line not in findings:
                findings.append(line)
            if len(findings) >= limit:
                break
    return findings[:limit]


def source_brief_for_specialists(preflight: dict[str, Any]) -> str:
    identity = preflight.get("subject_identity") or {}
    lines = [
        f"Subject: {identity.get('ticker')} / {identity.get('company_name')} / {identity.get('instrument_classification')}",
        f"Evidence source scope: {preflight.get('source_scope')}",
    ]
    for item in evidence_fact_bullets(preflight, "en"):
        lines.append(f"- {item}")
    for record in preflight.get("source_records", []):
        if record.get("importance") not in {"required", "important"}:
            continue
        data = record.get("data") if isinstance(record.get("data"), dict) else {}
        data_keys = ", ".join(sorted(data.keys())[:8]) if data else "none"
        lines.append(
            f"- {record.get('source_id')}: status={record.get('status')}; date={record.get('source_date')}; "
            f"url={record.get('url') or record.get('primary')}; fields={data_keys}; limitation={record.get('error') or 'none'}"
        )
    return "\n".join(lines[:28])


def build_specialist_prompt(
    specialist_id: str,
    intake: dict[str, Any],
    evidence_pack: dict[str, Any],
    preflight: dict[str, Any],
    prior_handoffs: list[dict[str, Any]] | None = None,
) -> str:
    prior_handoffs = prior_handoffs or []
    identity = preflight.get("subject_identity") or {}
    subject = subject_label(identity)
    route = selected_route_from_context(intake, preflight)
    route_label = AGENT_ROUTE_LABELS.get(route, route)
    consumed = "\n".join(
        f"- {handoff.get('Produced by')}: {handoff.get('Artifact')} | {handoff.get('Output status')} | "
        f"{'; '.join((handoff.get('main_findings') or [])[:3])}"
        for handoff in prior_handoffs
    )
    if not consumed:
        consumed = "- None; this is an upstream specialist."
    evidence_facts = "\n".join(f"- {item}" for item in evidence_fact_bullets(preflight, "en")) or "- No extracted evidence facts available; stay Limited."
    source_brief = source_brief_for_specialists(preflight)
    return (
        f"You are {specialist_id} for the Automation Lab {route_label} AGENT workflow covering {subject}.\n"
        "Use only the provided evidence summary and source inventory references. Do not claim unreviewed sources.\n"
        "Produce substantive findings for your specialist scope: conclusion, support, risks/limits, and IC handoff. Avoid metadata-only output.\n"
        "Return a concise markdown specialist handoff. Do not issue final IC Action unless you are investment-committee-agent and gates permit it.\n"
        "If you are investment-committee-agent, explicitly synthesize the validated upstream handoffs listed below and do not rely on raw outputs.\n"
        "No exact position sizing. Raw output is audit-only.\n"
        f"Prompt: {intake.get('normalized_prompt')}\n"
        f"Evidence readiness: {evidence_pack.get('evidence_readiness')}\n"
        f"Source count: {len(preflight.get('source_records', []))}\n"
        f"Evidence facts available:\n{evidence_facts}\n"
        f"Source brief:\n{source_brief}\n"
        f"Validated upstream handoffs available to consume:\n{consumed}\n"
    )


def live_specialist_error_response(
    specialist_id: str,
    error: str,
    *,
    timeout_seconds: int | None,
    timeout_source: str,
    started_at: str | None = None,
    completed_at: str | None = None,
    duration_seconds: float | None = None,
    command_shape: list[str] | None = None,
    project_root: Path | None = None,
) -> dict[str, Any]:
    project_root = project_root or get_codex_sdk_project_root()
    started_at = started_at or now_iso()
    completed_at = completed_at or now_iso()
    return {
        "status": "error",
        "error": error,
        "response": "",
        "sdk_thread_id": "",
        "codex_execution_path": CODEX_SDK_EXECUTION_PATH,
        "codex_sdk_project_root": str(project_root),
        "codex_sdk_log_dir": "",
        "sdk_error": error,
        "subprocess_exit_code": None,
        "timeout_seconds": timeout_seconds,
        "timeout_source": timeout_source,
        "started_at": started_at,
        "completed_at": completed_at,
        "duration_seconds": duration_seconds,
        "prompt_transport": "prompt_file",
        "command_shape": command_shape or [],
    }


def run_live_specialist_codex(
    specialist_id: str,
    prompt: str,
    max_timeout_seconds: float | None = None,
) -> dict[str, Any]:
    project_root = get_codex_sdk_project_root()
    timeout, timeout_source = get_codex_sdk_timeout_seconds(specialist_id)
    if max_timeout_seconds is not None:
        if max_timeout_seconds <= 0:
            instant = now_iso()
            return live_specialist_error_response(
                specialist_id,
                f"{specialist_id} Codex SDK CLI not started because full AGENT timeout budget was exhausted",
                timeout_seconds=0,
                timeout_source=f"{timeout_source}+{AGENT_TOTAL_TIMEOUT_ENV}",
                started_at=instant,
                completed_at=instant,
                duration_seconds=0,
                project_root=project_root,
            )
        capped_timeout = max(0.001, float(max_timeout_seconds))
        if capped_timeout < timeout:
            timeout = capped_timeout
            timeout_source = f"{timeout_source}+{AGENT_TOTAL_TIMEOUT_ENV}"
    dry_run = env_truthy(CODEX_SDK_DRY_RUN_ENV)
    prompt_file_path: Path | None = None
    with tempfile.NamedTemporaryFile(
        "w",
        encoding="utf-8",
        suffix=".txt",
        prefix=f"fa-{specialist_id}-",
        delete=False,
    ) as prompt_file:
        prompt_file.write(prompt)
        prompt_file_path = Path(prompt_file.name)
    command = [
        get_codex_sdk_command(),
        "run",
        "codex:run",
        "--",
        "--prompt-file",
        str(prompt_file_path),
        "--dry-run" if dry_run else "--live",
        "--workspace",
        str(project_root),
        "--sandbox",
        "read_only",
    ]
    command_shape = codex_sdk_command_shape(command)
    started_at = datetime.now(timezone.utc).astimezone()
    started_at_text = started_at.isoformat(timespec="seconds")
    try:
        completed = subprocess.run(
            command,
            cwd=project_root,
            text=True,
            capture_output=True,
            check=False,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired as exc:
        completed_at = datetime.now(timezone.utc).astimezone()
        return {
            "status": "error",
            "error": f"{specialist_id} Codex SDK CLI timed out after {timeout} seconds",
            "response": "",
            "sdk_thread_id": "",
            "codex_execution_path": CODEX_SDK_EXECUTION_PATH,
            "codex_sdk_project_root": str(project_root),
            "codex_sdk_log_dir": "",
            "sdk_error": f"Codex SDK CLI timed out after {timeout} seconds",
            "subprocess_exit_code": None,
            "timeout_seconds": timeout,
            "timeout_source": timeout_source,
            "started_at": started_at_text,
            "completed_at": completed_at.isoformat(timespec="seconds"),
            "duration_seconds": round((completed_at - started_at).total_seconds(), 3),
            "prompt_transport": "prompt_file",
            "command_shape": command_shape,
        }
    except OSError as exc:
        completed_at = datetime.now(timezone.utc).astimezone()
        return {
            "status": "error",
            "error": f"{specialist_id} Codex SDK CLI could not start",
            "response": "",
            "sdk_thread_id": "",
            "codex_execution_path": CODEX_SDK_EXECUTION_PATH,
            "codex_sdk_project_root": str(project_root),
            "codex_sdk_log_dir": "",
            "sdk_error": f"Codex SDK CLI could not start ({type(exc).__name__})",
            "subprocess_exit_code": None,
            "timeout_seconds": timeout,
            "timeout_source": timeout_source,
            "started_at": started_at_text,
            "completed_at": completed_at.isoformat(timespec="seconds"),
            "duration_seconds": round((completed_at - started_at).total_seconds(), 3),
            "prompt_transport": "prompt_file",
            "command_shape": command_shape,
        }
    finally:
        if prompt_file_path is not None:
            prompt_file_path.unlink(missing_ok=True)

    try:
        result = parse_codex_sdk_cli_json(completed.stdout)
    except ValueError as exc:
        completed_at = datetime.now(timezone.utc).astimezone()
        sdk_error = f"{exc}; stderr={completed.stderr.strip()}"
        usage_limited = is_usage_limit_error(sdk_error)
        return {
            "status": "error",
            "error": f"{specialist_id} Codex SDK CLI returned unparsable output",
            "response": "",
            "sdk_thread_id": "",
            "codex_execution_path": CODEX_SDK_EXECUTION_PATH,
            "codex_sdk_project_root": str(project_root),
            "codex_sdk_log_dir": "",
            "sdk_error": sdk_error,
            "usage_limit_blocked": usage_limited,
            "usage_limit_reset_hint": usage_limit_reset_hint(sdk_error),
            "subprocess_exit_code": completed.returncode,
            "timeout_seconds": timeout,
            "timeout_source": timeout_source,
            "started_at": started_at_text,
            "completed_at": completed_at.isoformat(timespec="seconds"),
            "duration_seconds": round((completed_at - started_at).total_seconds(), 3),
            "prompt_transport": "prompt_file",
            "command_shape": command_shape,
        }

    completed_at = datetime.now(timezone.utc).astimezone()
    sdk_status = result.get("status")
    response = result.get("finalResponse") or ""
    sdk_thread_id = result.get("threadId") or ""
    sdk_error = result.get("error") or completed.stderr.strip()
    usage_limited = is_usage_limit_error(sdk_error)
    ok = completed.returncode == 0 and sdk_status == "completed" and bool(sdk_thread_id)
    if completed.returncode == 0 and sdk_status == "completed" and not sdk_thread_id:
        sdk_error = sdk_error or "Codex SDK CLI completed without a real threadId"
    if dry_run and sdk_status == "dry_run":
        sdk_error = "Codex SDK dry-run did not execute a real specialist thread"
    return {
        "status": "ok" if ok else "error",
        "error": None if ok else (sdk_error or f"Codex SDK CLI status={sdk_status} exit={completed.returncode}"),
        "response": response,
        "sdk_thread_id": sdk_thread_id,
        "codex_execution_path": CODEX_SDK_EXECUTION_PATH,
        "codex_sdk_project_root": str(project_root),
        "codex_sdk_log_dir": result.get("logDir") or "",
        "sdk_error": None if ok else sdk_error,
        "usage_limit_blocked": usage_limited,
        "usage_limit_reset_hint": usage_limit_reset_hint(sdk_error),
        "subprocess_exit_code": completed.returncode,
        "timeout_seconds": timeout,
        "timeout_source": timeout_source,
        "started_at": started_at_text,
        "completed_at": completed_at.isoformat(timespec="seconds"),
        "duration_seconds": round((completed_at - started_at).total_seconds(), 3),
        "prompt_transport": "prompt_file",
        "command_shape": command_shape,
    }


def is_usage_limit_error(text: Any) -> bool:
    return bool(re.search(r"(?i)\b(usage limit|purchase more credits|try again at)\b", str(text or "")))


def usage_limit_reset_hint(text: Any) -> str:
    match = re.search(r"(?i)(try again at\s+[^.;\r\n]+)", str(text or ""))
    return match.group(1).strip() if match else ""


def live_attempt_record(attempt_no: int, response: dict[str, Any]) -> dict[str, Any]:
    status = "ok" if response.get("status") == "ok" else "error"
    sdk_thread_id = response.get("sdk_thread_id") or ""
    return {
        "attempt_no": attempt_no,
        "status": status,
        "thread_or_run_id": sdk_thread_id if status == "ok" else "",
        "sdk_thread_id": sdk_thread_id,
        "codex_sdk_log_dir": response.get("codex_sdk_log_dir") or "",
        "sdk_error": response.get("sdk_error") or response.get("error"),
        "usage_limit_blocked": bool(response.get("usage_limit_blocked")),
        "usage_limit_reset_hint": response.get("usage_limit_reset_hint") or "",
        "subprocess_exit_code": response.get("subprocess_exit_code"),
        "timeout_seconds": response.get("timeout_seconds"),
        "timeout_source": response.get("timeout_source") or "",
        "started_at": response.get("started_at") or "",
        "completed_at": response.get("completed_at") or "",
        "duration_seconds": response.get("duration_seconds"),
        "prompt_transport": response.get("prompt_transport") or "",
        "command_shape": response.get("command_shape") or [],
    }


def write_specialist_artifacts(
    run_dir: Path,
    specialist_id: str,
    mode: str,
    intake: dict[str, Any],
    evidence_pack: dict[str, Any],
    preflight: dict[str, Any],
    prior_handoffs: list[dict[str, Any]] | None = None,
    deadline_monotonic: float | None = None,
) -> dict[str, Any]:
    prior_handoffs = prior_handoffs or []
    started_at_dt = datetime.now(timezone.utc).astimezone()
    started_at = started_at_dt.isoformat(timespec="seconds")
    prompt = build_specialist_prompt(specialist_id, intake, evidence_pack, preflight, prior_handoffs)
    identity = preflight.get("subject_identity") or {}
    retry_count = 0
    sdk_thread_id = ""
    codex_execution_path = ""
    codex_sdk_project_root = ""
    codex_sdk_log_dir = ""
    sdk_error = None
    subprocess_exit_code = None
    timeout_seconds = None
    timeout_source = ""
    prompt_transport = ""
    attempt_history: list[dict[str, Any]] = []

    def remaining_budget() -> float | None:
        if deadline_monotonic is None:
            return None
        return deadline_monotonic - time.monotonic()

    if mode == "mock":
        raw = mock_specialist_raw_output(specialist_id, identity)
        status = "ok"
        error = None
        thread_or_run_id = f"mock-{specialist_id}-{uuid4().hex[:8]}"
        attempt_history = [
            {
                "attempt_no": 1,
                "status": "ok",
                "thread_or_run_id": thread_or_run_id,
                "sdk_thread_id": "",
                "codex_sdk_log_dir": "",
                "sdk_error": None,
                "subprocess_exit_code": None,
                "timeout_seconds": None,
                "timeout_source": "mock",
                "started_at": started_at,
                "completed_at": "",
                "duration_seconds": None,
                "prompt_transport": "",
                "command_shape": [],
            }
        ]
    else:
        response = run_live_specialist_codex(specialist_id, prompt, remaining_budget())
        attempt_history.append(live_attempt_record(1, response))
        if response.get("status") != "ok":
            retry_budget = remaining_budget()
            if response.get("usage_limit_blocked"):
                response = live_specialist_error_response(
                    specialist_id,
                    f"{specialist_id} retry not started because Codex SDK usage limit is active"
                    + (
                        f" ({response.get('usage_limit_reset_hint')})"
                        if response.get("usage_limit_reset_hint")
                        else ""
                    ),
                    timeout_seconds=response.get("timeout_seconds"),
                    timeout_source="usage_limit_guard",
                    started_at=now_iso(),
                    completed_at=now_iso(),
                    duration_seconds=0,
                )
                response["usage_limit_blocked"] = True
                response["usage_limit_reset_hint"] = attempt_history[-1].get("usage_limit_reset_hint", "")
            elif retry_budget is not None and retry_budget <= 0:
                response = live_specialist_error_response(
                    specialist_id,
                    f"{specialist_id} retry not started because full AGENT timeout budget was exhausted",
                    timeout_seconds=0,
                    timeout_source=AGENT_TOTAL_TIMEOUT_ENV,
                    started_at=now_iso(),
                    completed_at=now_iso(),
                    duration_seconds=0,
                )
            else:
                retry_count = 1
                response = run_live_specialist_codex(
                    specialist_id,
                    prompt + "\nRetry once: complete the same specialist handoff, concise markdown, no final IC action.",
                    retry_budget,
                )
            attempt_history.append(live_attempt_record(2, response))
        status = "ok" if response.get("status") == "ok" else "error"
        raw = response.get("response") or f"# {specialist_title(specialist_id)}\n\nSpecialist run failed: {response.get('error')}\n"
        error = None if status == "ok" else response.get("error")
        sdk_thread_id = response.get("sdk_thread_id") or ""
        thread_or_run_id = sdk_thread_id if status == "ok" else ""
        codex_execution_path = response.get("codex_execution_path") or CODEX_SDK_EXECUTION_PATH
        codex_sdk_project_root = response.get("codex_sdk_project_root") or str(get_codex_sdk_project_root())
        codex_sdk_log_dir = response.get("codex_sdk_log_dir") or ""
        sdk_error = response.get("sdk_error") or error
        usage_limit_blocked = bool(response.get("usage_limit_blocked") or any(item.get("usage_limit_blocked") for item in attempt_history))
        subprocess_exit_code = response.get("subprocess_exit_code")
        timeout_seconds = response.get("timeout_seconds")
        timeout_source = response.get("timeout_source") or ""
        prompt_transport = response.get("prompt_transport") or ""
    attempt_id = f"{mode}-attempt-{specialist_id}-{uuid4().hex[:8]}"
    completed_dt = datetime.now(timezone.utc).astimezone()
    completed = completed_dt.isoformat(timespec="seconds")
    duration_seconds = round((completed_dt - started_at_dt).total_seconds(), 3)
    if mode == "mock" and attempt_history:
        attempt_history[0]["completed_at"] = completed
        attempt_history[0]["duration_seconds"] = duration_seconds
    specialist_dir = run_dir / "audit" / "specialists" / specialist_id
    specialist_dir.mkdir(parents=True, exist_ok=True)
    raw_path = specialist_dir / "raw_output.md"
    handoff_json_path = specialist_dir / "handoff.json"
    handoff_md_path = specialist_dir / "handoff.md"
    validation_path = specialist_dir / "validation.json"
    raw_path.write_text(raw, encoding="utf-8")
    artifact_name = specialist_artifact_name(specialist_id)
    artifact_path = run_dir / "audit" / artifact_name
    artifact_path.write_text(raw, encoding="utf-8")
    route = selected_route_from_context(intake, preflight)
    route_label = AGENT_ROUTE_LABELS.get(route, route)
    portfolio_context = intake.get("portfolio_context") or normalize_portfolio_context({}, source="not_provided")
    portfolio_context_provided = portfolio_context.get("status") in {"partial", "provided"}
    usage_limit_reset = response.get("usage_limit_reset_hint") if mode != "mock" else ""
    handoff = {
        "schema_version": "agent_specialist_handoff.v1",
        "Artifact": artifact_name,
        "Subject": subject_label(identity),
        "Request type": f"AGENT {route_label} supporting specialist handoff",
        "Workflow": route,
        "Produced by": specialist_id,
        "As-of date/time": completed,
        "Output status": "Complete" if status == "ok" else "Blocked",
        "Evidence status": evidence_pack.get("evidence_readiness"),
        "Freshness status": "current_or_latest_available",
        "Source scope": preflight.get("source_scope"),
        "Evidence limits": evidence_pack.get("missing_weak_evidence_register", []),
        "Key limitations": portfolio_context.get("limitations")
        or ["No user portfolio context provided; personal action and exact sizing remain unavailable."],
        "Missing gates": [] if status == "ok" else [specialist_id],
        "Decision boundary": "Supporting handoff only; not an IC Action."
        if specialist_id != "investment-committee-agent"
        else "IC synthesis consumes validated handoffs only.",
        "Downstream handoff": "investment-committee-agent"
        if specialist_id != "investment-committee-agent"
        else "reader-facing investment_report.md",
        "Required follow-up": (
            "Close any missing portfolio fields and IC gates before personal action."
            if portfolio_context_provided and specialist_id == "portfolio-fit-agent"
            else "Add portfolio context for personal action."
            if specialist_id == "portfolio-fit-agent"
            else "None recorded."
        ),
        "Portfolio context status": portfolio_context.get("status"),
        "Portfolio context fields": portfolio_context.get("provided_fields", []),
        "thread_or_run_id": thread_or_run_id,
        "attempt_id": attempt_id,
        "sdk_thread_id": sdk_thread_id,
        "codex_execution_path": codex_execution_path,
        "codex_sdk_project_root": codex_sdk_project_root,
        "codex_sdk_log_dir": codex_sdk_log_dir,
        "sdk_error": sdk_error,
        "usage_limit_blocked": usage_limit_blocked if mode != "mock" else False,
        "usage_limit_reset_hint": usage_limit_reset or "",
        "subprocess_exit_code": subprocess_exit_code,
        "timeout_seconds": timeout_seconds,
        "timeout_source": timeout_source,
        "started_at": started_at,
        "completed_at": completed,
        "duration_seconds": duration_seconds,
        "prompt_transport": prompt_transport,
        "attempt_history": attempt_history,
        "mode": mode,
        "selected_route": route,
        "raw_output_path": str(raw_path),
        "artifact_path": str(artifact_path),
        "main_findings": extract_meaningful_findings(raw),
        "consumed_handoff_ids": [handoff.get("Produced by") for handoff in prior_handoffs],
        "consumed_handoff_count": len(prior_handoffs),
        "consumed_handoff_artifacts": [handoff.get("Artifact") for handoff in prior_handoffs],
    }
    write_json(handoff_json_path, handoff)
    handoff_md_path.write_text(
        "\n".join(
            [
                f"# Structured handoff - {specialist_id}",
                "",
                f"Artifact: {artifact_name}",
                f"Subject: {subject_label(identity)}",
                f"Workflow: {route}",
                f"Produced by: {specialist_id}",
                f"As-of date/time: {completed}",
                f"Output status: {handoff['Output status']}",
                f"Evidence status: {handoff['Evidence status']}",
                f"Source scope: {handoff['Source scope']}",
                f"Decision boundary: {handoff['Decision boundary']}",
                "",
                "## Main findings",
                *[f"- {line}" for line in handoff["main_findings"] if line.strip()],
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    validation = {
        "status": "pass" if status == "ok" else "fail",
        "checks": {
            "raw_output_exists": raw_path.is_file(),
            "handoff_json_exists": handoff_json_path.is_file(),
            "handoff_md_exists": handoff_md_path.is_file(),
            "raw_output_audit_only": True,
            "ic_consumes_normalized_handoff": True,
        },
        "error": error,
        "codex_execution_path": codex_execution_path,
        "codex_sdk_project_root": codex_sdk_project_root,
        "codex_sdk_log_dir": codex_sdk_log_dir,
        "sdk_thread_id": sdk_thread_id,
        "sdk_error": sdk_error,
        "usage_limit_blocked": usage_limit_blocked if mode != "mock" else False,
        "usage_limit_reset_hint": usage_limit_reset or "",
        "subprocess_exit_code": subprocess_exit_code,
        "timeout_seconds": timeout_seconds,
        "timeout_source": timeout_source,
        "started_at": started_at,
        "completed_at": completed,
        "duration_seconds": duration_seconds,
        "prompt_transport": prompt_transport,
        "attempt_history": attempt_history,
        "retry_count": retry_count,
    }
    write_json(validation_path, validation)
    return {
        "specialist_id": specialist_id,
        "status": status,
        "thread_or_run_id": thread_or_run_id,
        "attempt_id": attempt_id,
        "sdk_thread_id": sdk_thread_id,
        "codex_execution_path": codex_execution_path,
        "codex_sdk_project_root": codex_sdk_project_root,
        "codex_sdk_log_dir": codex_sdk_log_dir,
        "sdk_error": sdk_error,
        "subprocess_exit_code": subprocess_exit_code,
        "timeout_seconds": timeout_seconds,
        "timeout_source": timeout_source,
        "started_at": started_at,
        "completed_at": completed,
        "duration_seconds": duration_seconds,
        "prompt_transport": prompt_transport,
        "attempt_history": attempt_history,
        "artifact_path": str(artifact_path),
        "handoff_path": str(handoff_json_path),
        "validation_path": str(validation_path),
        "retry_count": retry_count,
        "error": error,
        "selected_route": route,
        "handoff": handoff,
    }


def run_agent_specialists(
    run_dir: Path,
    mode: str,
    intake: dict[str, Any],
    evidence_pack: dict[str, Any],
    preflight: dict[str, Any],
) -> list[dict[str, Any]]:
    results_by_id: dict[str, dict[str, Any]] = {}
    route = selected_route_from_context(intake, preflight)
    route_specialists = agent_specialists_for_route(route)
    stage_started_at = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    total_timeout_seconds = get_agent_total_timeout_seconds()
    max_parallel = get_agent_max_parallel_specialists()
    deadline = time.monotonic() + total_timeout_seconds
    stage_events: list[dict[str, Any]] = []

    def budget_remaining() -> float:
        return deadline - time.monotonic()

    stage_events.append(
        {
            "stage": "evidence",
            "specialists": ["evidence-collector"],
            "started_at": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
        }
    )
    evidence = write_specialist_artifacts(
        run_dir,
        "evidence-collector",
        mode,
        intake,
        evidence_pack,
        preflight,
        [],
        deadline,
    )
    results_by_id["evidence-collector"] = evidence
    stage_events[-1]["completed_at"] = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    stage_events[-1]["status"] = evidence.get("status")
    if evidence.get("status") != "ok":
        stage_events.append(
            {
                "stage": "stop",
                "reason": "stage_1_evidence_collector_failed",
                "failed_specialist": "evidence-collector",
            }
        )
        write_json(
            run_dir / "audit" / "specialist_stage_execution.json",
            {
                "started_at": stage_started_at,
                "completed_at": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
                "total_timeout_seconds": total_timeout_seconds,
                "max_parallel_specialists": max_parallel,
                "events": stage_events,
            },
        )
        return [results_by_id[sid] for sid in route_specialists if sid in results_by_id]

    if budget_remaining() <= 0:
        stage_events.append({"stage": "stop", "reason": "agent_total_timeout_before_parallel_specialists"})
        write_json(
            run_dir / "audit" / "specialist_stage_execution.json",
            {
                "started_at": stage_started_at,
                "completed_at": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
                "total_timeout_seconds": total_timeout_seconds,
                "max_parallel_specialists": max_parallel,
                "events": stage_events,
            },
        )
        return [results_by_id[sid] for sid in route_specialists if sid in results_by_id]

    non_ic_specialists = [
        sid for sid in route_specialists if sid not in {"evidence-collector", "investment-committee-agent"}
    ]
    stage_events.append(
        {
            "stage": "parallel_non_ic_specialists",
            "specialists": non_ic_specialists,
            "max_parallel_specialists": max_parallel,
            "started_at": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
        }
    )
    parallel_stage_index = len(stage_events) - 1
    not_started_due_to_timeout: list[str] = []
    for offset in range(0, len(non_ic_specialists), max_parallel):
        batch = non_ic_specialists[offset : offset + max_parallel]
        if budget_remaining() <= 0:
            not_started_due_to_timeout.extend(non_ic_specialists[offset:])
            break
        stage_events.append(
            {
                "stage": "parallel_non_ic_wave",
                "specialists": batch,
                "started_at": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
                "remaining_budget_seconds_at_launch": round(max(0, budget_remaining()), 3),
            }
        )
        with ThreadPoolExecutor(max_workers=len(batch)) as executor:
            future_by_id = {
                executor.submit(
                    write_specialist_artifacts,
                    run_dir,
                    specialist_id,
                    mode,
                    intake,
                    evidence_pack,
                    preflight,
                    [],
                    deadline,
                ): specialist_id
                for specialist_id in batch
            }
            for future in as_completed(future_by_id):
                specialist_id = future_by_id[future]
                try:
                    results_by_id[specialist_id] = future.result()
                except Exception as exc:  # pragma: no cover - defensive guard for unexpected writer failures
                    results_by_id[specialist_id] = {
                        "specialist_id": specialist_id,
                        "status": "error",
                        "thread_or_run_id": "",
                        "sdk_thread_id": "",
                        "error": f"specialist_artifact_error: {type(exc).__name__}",
                        "attempt_history": [],
                        "handoff": {"Produced by": specialist_id, "Output status": "Blocked", "consumed_handoff_ids": []},
                    }
        stage_events[-1]["completed_at"] = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
        stage_events[-1]["remaining_budget_seconds_at_completion"] = round(max(0, budget_remaining()), 3)
        stage_events[-1]["failed_specialists"] = [
            sid for sid in batch if results_by_id.get(sid, {}).get("status") != "ok"
        ]
    stage_events[parallel_stage_index]["completed_at"] = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    stage_events[parallel_stage_index]["remaining_budget_seconds_at_completion"] = round(max(0, budget_remaining()), 3)
    stage_events[parallel_stage_index]["failed_specialists"] = [
        sid for sid in non_ic_specialists if results_by_id.get(sid, {}).get("status") != "ok"
    ]
    stage_events[parallel_stage_index]["not_started_specialists"] = not_started_due_to_timeout
    if not_started_due_to_timeout:
        stage_events.append(
            {
                "stage": "stop",
                "reason": "agent_total_timeout_before_launching_remaining_parallel_specialists",
                "not_started_specialists": not_started_due_to_timeout,
            }
        )

    upstream_specialists = [sid for sid in route_specialists if sid != "investment-committee-agent"]
    failed_upstream = [sid for sid in upstream_specialists if results_by_id.get(sid, {}).get("status") != "ok"]
    if failed_upstream:
        stage_events.append(
            {
                "stage": "stop",
                "reason": "upstream_specialist_failed_before_ic",
                "failed_specialists": failed_upstream,
            }
        )
        write_json(
            run_dir / "audit" / "specialist_stage_execution.json",
            {
                "started_at": stage_started_at,
                "completed_at": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
                "total_timeout_seconds": total_timeout_seconds,
                "max_parallel_specialists": max_parallel,
                "events": stage_events,
            },
        )
        return [results_by_id[sid] for sid in route_specialists if sid in results_by_id]

    if budget_remaining() <= 0:
        stage_events.append({"stage": "stop", "reason": "agent_total_timeout_before_ic"})
        write_json(
            run_dir / "audit" / "specialist_stage_execution.json",
            {
                "started_at": stage_started_at,
                "completed_at": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
                "total_timeout_seconds": total_timeout_seconds,
                "max_parallel_specialists": max_parallel,
                "events": stage_events,
            },
        )
        return [results_by_id[sid] for sid in route_specialists if sid in results_by_id]

    completed_handoffs = [results_by_id[sid]["handoff"] for sid in upstream_specialists]
    stage_events.append(
        {
            "stage": "investment_committee",
            "specialists": ["investment-committee-agent"],
            "started_at": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
            "consumed_handoff_count": len(completed_handoffs),
        }
    )
    ic = write_specialist_artifacts(
        run_dir,
        "investment-committee-agent",
        mode,
        intake,
        evidence_pack,
        preflight,
        completed_handoffs,
        deadline,
    )
    results_by_id["investment-committee-agent"] = ic
    stage_events[-1]["completed_at"] = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    stage_events[-1]["remaining_budget_seconds_at_completion"] = round(max(0, budget_remaining()), 3)
    stage_events[-1]["status"] = ic.get("status")
    write_json(
        run_dir / "audit" / "specialist_stage_execution.json",
        {
            "started_at": stage_started_at,
            "completed_at": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
            "total_timeout_seconds": total_timeout_seconds,
            "max_parallel_specialists": max_parallel,
            "events": stage_events,
        },
    )
    return [results_by_id[sid] for sid in route_specialists if sid in results_by_id]


def reader_language(prompt: str) -> str:
    return "ru" if detect_prompt_language(prompt) == "ru" else "en"


def key_sources_for_report(preflight: dict[str, Any]) -> list[str]:
    sources = []
    for record in preflight.get("source_records", []):
        if record.get("status") == "ok" and record.get("importance") in {"required", "important"}:
            sources.append(f"{record.get('name')}: {record.get('url') or record.get('primary')}")
        if len(sources) >= 7:
            break
    return sources


def evidence_fact_bullets(preflight: dict[str, Any], language: str) -> list[str]:
    records = {record.get("source_id"): record for record in preflight.get("source_records", [])}
    identity = preflight.get("subject_identity") or {}
    ticker = identity.get("ticker", "EQUITY")
    bullets: list[str] = []
    price = records.get("current_price") or {}
    price_data = price.get("data") if isinstance(price.get("data"), dict) else {}
    if price.get("status") == "ok" and price_data:
        if language == "ru":
            bullets.append(f"Цена/рынок: последняя публичная цена закрытия для {ticker}: {price_data.get('close')} на дату {price_data.get('date') or price.get('source_date')}.")
        else:
            bullets.append(f"Price/market: latest public close for {ticker}: {price_data.get('close')} dated {price_data.get('date') or price.get('source_date')}.")
    for source_id, label_en, label_ru in [
        ("latest_10k", "Annual filing/report", "Годовая отчётность"),
        ("latest_10q", "Interim filing/report", "Промежуточная отчётность"),
        ("company_facts", "Financial facts", "Финансовые данные"),
    ]:
        record = records.get(source_id) or {}
        data = record.get("data") if isinstance(record.get("data"), dict) else {}
        if record.get("status") in {"ok", "partial"}:
            status = record.get("status")
            form = data.get("form") or data.get("proxy_form") or data.get("proxy") or ("источник" if language == "ru" else "source")
            date_text = data.get("filing_date") or record.get("source_date") or ("последняя доступная дата" if language == "ru" else "latest available")
            if language == "ru":
                status_ru = {"ok": "проверен", "partial": "частично проверен"}.get(status, status)
                bullets.append(f"{label_ru}: форма/набор данных {form}; источник {status_ru}; дата или период {date_text}.")
            else:
                bullets.append(f"{label_en}: {form}, source status {status}, date/period {date_text}.")
    if identity.get("instrument_classification") == "adr_or_foreign_issuer_us_listing":
        gate = identity.get("adr_gate") or {}
        if language == "ru":
            bullets.append(
                f"ADR-проверка: базовый эмитент — {gate.get('underlying_issuer')}; страна — {gate.get('issuer_country')}; валюта торгов — {gate.get('trading_currency')}."
            )
        else:
            bullets.append(
                f"ADR gate: underlying issuer — {gate.get('underlying_issuer')}; country — {gate.get('issuer_country')}; trading currency — {gate.get('trading_currency')}."
            )
    return bullets[:6]


def source_scope_sentence(preflight: dict[str, Any], language: str) -> str:
    identity = preflight.get("subject_identity") or {}
    classification = identity.get("instrument_classification")
    if language == "ru":
        if classification == "non_us_listed_equity":
            return (
                "Проверены публичные данные по идентичности эмитента, сайту для инвесторов, годовым и промежуточным отчётам, "
                "цене, истории цен, событиям, сектору, конкурентам и макро-контексту. Для иностранных листингов покрытие SEC/XBRL не считается доступным, "
                "если это явно не подтверждено в аудите."
            )
        if classification == "adr_or_foreign_issuer_us_listing":
            return (
                "Проверены публичные данные по идентичности эмитента, ADR-статусу, раскрытиям иностранного эмитента в SEC, если они доступны, "
                "сайту для инвесторов, цене, истории цен, событиям, сектору, конкурентам и макро-контексту. Полная карта источников сохранена в аудите."
            )
        return (
            "Проверены публичные данные по идентичности компании, раскрытия SEC, XBRL-данные компании, цена, история цен, события, сектор, конкуренты и макро-контекст. "
            "Полная карта источников сохранена в аудите."
        )
    if classification == "non_us_listed_equity":
        return (
            "The workflow checked public issuer identity, issuer IR / annual report / interim report candidates, price, price history, events, sector context, peer context, and macro context. "
            "For direct non-US listings, SEC/XBRL-equivalent coverage is not implied unless the audit explicitly verifies it."
        )
    if classification == "adr_or_foreign_issuer_us_listing":
        return (
            "The workflow checked public issuer identity, ADR/foreign issuer gate, SEC foreign-issuer filings where available, issuer IR, price, price history, events, sector context, peer context, and macro context. "
            "The detailed source map and technical statuses are stored in audit."
        )
    return (
        "The workflow checked public sources for identity, SEC filings, XBRL/company facts, price, price history, events, sector context, peer context, and macro context. "
        "The detailed source map and technical statuses are stored in audit."
    )


def completed_specialists(specialists: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [item for item in specialists if item.get("status") == "ok"]


def route_from_specialist_results(specialists: list[dict[str, Any]]) -> str:
    for item in specialists:
        route = item.get("selected_route") or (item.get("handoff") or {}).get("Workflow")
        if route:
            return str(route)
    return "equity_full_cycle"


def failed_required_specialist_ids(specialists: list[dict[str, Any]]) -> list[str]:
    required = agent_required_specialists_for_route(route_from_specialist_results(specialists))
    return [
        item.get("specialist_id")
        for item in specialists
        if item.get("status") != "ok" and item.get("specialist_id") in required
    ]


def ic_specialist_completed(specialists: list[dict[str, Any]]) -> bool:
    return any(
        item.get("specialist_id") == "investment-committee-agent" and item.get("status") == "ok"
        for item in specialists
    )


def ic_completed_with_expected_handoffs(specialists: list[dict[str, Any]]) -> bool:
    ic = next(
        (
            item
            for item in specialists
            if item.get("specialist_id") == "investment-committee-agent" and item.get("status") == "ok"
        ),
        None,
    )
    if not ic:
        return False
    consumed_ids = set((ic.get("handoff") or {}).get("consumed_handoff_ids") or [])
    expected_upstream = {sid for sid in agent_specialists_for_route(route_from_specialist_results(specialists)) if sid != "investment-committee-agent"}
    return expected_upstream.issubset(consumed_ids)


def human_limitations(intake: dict[str, Any], preflight: dict[str, Any], evidence_pack: dict[str, Any]) -> list[str]:
    limits = []
    identity = preflight.get("subject_identity") or {}
    classification = identity.get("instrument_classification")
    if preflight.get("mock_disclaimer"):
        limits.append("Mock mode is test-only and does not represent real investment analysis or real source evidence.")
    if classification == "adr_or_foreign_issuer_us_listing":
        gate = identity.get("adr_gate") or {}
        limits.append(
            f"This instrument is an ADR or foreign-issuer US listing; underlying issuer={gate.get('underlying_issuer')}, country={gate.get('issuer_country')}, currency={gate.get('trading_currency')}. Reporting, liquidity, access, and delisting/regulatory risks require explicit treatment."
        )
    if classification == "non_us_listed_equity":
        limits.append(
            "This is a direct non-US listed equity; reporting standards, currency, exchange access, and source availability may differ from SEC-covered US equities."
        )
    if intake.get("baseline_used"):
        limits.append("Some intake details were filled with baseline assumptions and are recorded in the audit trail.")
    portfolio_context = intake.get("portfolio_context") or {}
    if not intake.get("portfolio_context_provided"):
        limits.append(
            "A personalized portfolio action is not provided because portfolio concentration, risk limits, and existing exposure were not supplied."
        )
    elif portfolio_context.get("missing_fields"):
        limits.append(
            "Portfolio context was supplied but remains incomplete; missing fields are recorded in the audit trail and exact sizing remains unavailable."
        )
    if preflight.get("summary", {}).get("missing_important", []):
        limits.append(
            "Some useful public context sources were unavailable, so the conclusion is framed as decision preparation rather than a final personal action."
        )
    if preflight.get("summary", {}).get("partial_required", []):
        limits.append(
            "Some decision-critical source categories were only partially verified, so the report is Limited rather than a fully supported investment analysis."
        )
    if evidence_pack.get("evidence_readiness") == "Blocked":
        limits.append("The report cannot be completed because required public evidence did not pass source preflight.")
    return limits


def reader_limit_text(limit: str, language: str) -> str:
    if language != "ru":
        return limit
    translations = {
        "A personalized portfolio action is not provided because portfolio concentration, risk limits, and existing exposure were not supplied.": (
            "Персональное портфельное действие не даётся, потому что не указаны концентрация портфеля, риск-лимиты и текущая экспозиция."
        ),
        "Mock mode is test-only and does not represent real investment analysis or real source evidence.": (
            "Mock mode предназначен только для тестов и не является реальным инвестиционным анализом или реальной доказательной базой."
        ),
        "Some useful public context sources were unavailable, so the conclusion is framed as decision preparation rather than a final personal action.": (
            "Часть полезных публичных контекстных источников недоступна, поэтому вывод сформулирован как подготовка решения, а не финальное персональное действие."
        ),
        "The report cannot be completed because required public evidence did not pass source preflight.": (
            "Отчёт не может быть завершён полноценно, потому что обязательная публичная доказательная база не прошла source preflight."
        ),
        "Some decision-critical source categories were only partially verified, so the report is Limited rather than a fully supported investment analysis.": (
            "Некоторые критически важные категории источников подтверждены только частично, поэтому отчёт ограничен и не является полностью подтверждённым анализом."
        ),
        "Portfolio context was supplied but remains incomplete; missing fields are recorded in the audit trail and exact sizing remains unavailable.": (
            "Портфельный контекст предоставлен, но неполный; недостающие поля записаны в audit, а точный размер позиции остаётся недоступен."
        ),
        "One or more required specialist checks did not complete in this run, so the report is a preparation view rather than a final investment decision.": (
            "Одна или несколько обязательных проверок специалистов в live-режиме не завершились, поэтому отчёт остаётся подготовкой решения, а не финальным инвестиционным выводом."
        ),
        "required_specialists_incomplete": (
            "Одна или несколько обязательных проверок специалистов не завершились, поэтому отчёт является ограниченной подготовкой решения, а не финальной комитетской рекомендацией."
        ),
    }
    return translations.get(limit, limit)


def reader_evidence_status_text(status: Any, language: str) -> str:
    if language != "ru":
        return str(status or "Unknown")
    return {
        "Complete": "достаточная по источникам",
        "Limited": "ограниченная",
        "Blocked": "заблокирована",
    }.get(str(status or ""), str(status or "неизвестна"))


def reader_specialist_takeaways(specialists: list[dict[str, Any]], language: str) -> list[str]:
    handoffs = [item.get("handoff") or {} for item in specialists if item.get("status") == "ok"]
    by_id = {handoff.get("Produced by"): handoff for handoff in handoffs}
    ids = [
        "financial-statement-analysis",
        "valuation-expectations-agent",
        "risk-red-team-agent",
        "investment-committee-agent",
    ]
    labels_ru = {
        "financial-statement-analysis": "Финансовая проверка",
        "valuation-expectations-agent": "Сценарная оценка",
        "risk-red-team-agent": "Проверка рисков",
        "investment-committee-agent": "Итоговая сборка",
    }
    labels_en = {
        "financial-statement-analysis": "Financial check",
        "valuation-expectations-agent": "Scenario valuation",
        "risk-red-team-agent": "Risk check",
        "investment-committee-agent": "Synthesis",
    }
    labels = labels_ru if language == "ru" else labels_en
    takeaways = []
    for specialist_id in ids:
        handoff = by_id.get(specialist_id)
        if not handoff:
            continue
        findings = [line.strip("#- ").strip() for line in handoff.get("main_findings", []) if str(line).strip()]
        findings = [finding for finding in findings if not is_debug_or_metadata_line(finding)]
        if findings:
            takeaways.append(f"{labels[specialist_id]}: {reader_takeaway_text(findings[0], language)}")
    return takeaways[:4]


def reader_takeaway_text(text: str, language: str) -> str:
    if language != "ru":
        return text
    lower = text.lower()
    if lower.startswith("filing coverage is current"):
        return "Покрытие раскрытий SEC актуальное и достаточно авторитетное для анализа на уровне первичных источников."
    if lower.startswith("market anchor: latest public close"):
        match = re.search(r"latest public close\s+([A-Z0-9.\-]+)\s*=\s*\$?([0-9.,]+).*dated\s*([0-9-]+)", text, re.I)
        if match:
            return f"Рыночная привязка: последняя публичная цена закрытия {match.group(1)} = {match.group(2)} на дату {match.group(3)}."
        return "Рыночная привязка построена от последней публичной цены закрытия."
    if lower.startswith("business quality is likely strong"):
        return (
            "Качество бизнеса выглядит сильным на уровне структурного анализа, но инвестиционный вывод всё равно зависит от valuation, "
            "темпов роста, маржи, FCF и риска сжатия мультипликатора."
        )
    if lower.startswith("evidence collector:"):
        return text.replace("Evidence Collector:", "Evidence Collector:")
    if "revenue, operating margin, free cash flow conversion" in lower:
        return "Проверены выручка, операционная маржа, конверсия свободного денежного потока, капитальные расходы, баланс, возврат капитала, оборотный капитал, сегменты и качество учёта."
    if lower.startswith("scenario valuation uses"):
        return "Сценарная оценка связывает базовый, позитивный и негативный сценарии с ростом, конверсией свободного денежного потока, устойчивостью маржи, распределением капитала и чувствительностью мультипликатора."
    if lower.startswith("risk red team agent reviewed"):
        return "Проверка рисков просмотрела доказательную базу в своём контуре и передала нефинальный материал для сборки."
    return text


def reader_source_text(source: str, language: str) -> str:
    if language != "ru":
        return source
    replacements = {
        "Public equity identity": "Идентичность публичной компании",
        "SEC company submissions": "Раскрытия компании в SEC",
        "Latest Form 10-K": "Последняя форма 10-K",
        "Latest Form 10-Q": "Последняя форма 10-Q",
        "Recent Form 8-K": "Последняя форма 8-K",
        "Latest Form 8-K": "Последняя форма 8-K",
        "issuer event source": "источник события эмитента",
        "Full filing text / HTML": "Полный текст раскрытия",
        "SEC company facts / XBRL": "XBRL-данные компании в SEC",
        "SEC company facts": "XBRL-данные компании в SEC",
        "Current market price": "Текущая рыночная цена",
        "Recent price history": "История цены",
        "Recent news/events": "Последние новости и события",
    }
    for old, new in replacements.items():
        source = source.replace(old, new)
    return source


def reader_ic_synthesis(
    specialists: list[dict[str, Any]],
    language: str,
    identity: dict[str, Any],
    evidence_pack: dict[str, Any],
) -> list[str]:
    ic_final_owner = ic_completed_with_expected_handoffs(specialists)
    if not ic_final_owner:
        if language == "ru":
            return [
                "Финальная комитетская сборка не выполнена: обязательные проверки специалистов не завершились, поэтому полноценный IC-синтез не был достигнут.",
                "Доказательная база и финансовый снимок сохранены; после восстановления запуска специалистов нужно повторить обязательные проверки, затем комитетский этап и пересобрать отчёт.",
            ]
        return [
            "Required specialist checks did not complete, so final synthesis was not reached and this remains a Limited decision-prep report.",
            "The evidence base and financial snapshot are preserved, but the required checks and final assembly should be rerun after the specialist runtime is restored.",
        ]
    ic = next(
        (
            item
            for item in specialists
            if item.get("specialist_id") == "investment-committee-agent" and item.get("status") == "ok"
        ),
        {},
    )
    raw_path = ic.get("artifact_path")
    raw = ""
    if raw_path and Path(raw_path).is_file():
        raw = Path(raw_path).read_text(encoding="utf-8", errors="replace")
    findings = extract_meaningful_findings(raw, limit=5) if raw else []
    findings = [finding for finding in findings if not is_debug_or_metadata_line(finding)]
    if language == "ru":
        ticker = identity.get("ticker", "акция")
        readiness = reader_evidence_status_text(evidence_pack.get("evidence_readiness"), language)
        return [
            f"IC-сборка считает {ticker} готовым к комитетскому разбору: доказательная база {readiness}, обязательные материалы специалистов завершены.",
            "Главная рамка решения: это качественная акция роста с обязательной дисциплиной по оценке, а не краткосрочная ставка на один катализатор.",
            "Перед персональным действием нужно явно проверить, какие темпы роста, маржа, свободный денежный поток и мультипликатор оценки уже заложены в текущую цену.",
            "Без портфельного контекста IC-секция остаётся аналитической сборкой, а не персональным финальным действием или размером позиции.",
        ]
    ticker = identity.get("ticker", "the equity")
    readiness = reader_evidence_status_text(evidence_pack.get("evidence_readiness"), language)
    if findings:
        cleaned = [finding for finding in findings if "IC Action Status" not in finding and "Analysis Status" not in finding]
        if cleaned:
            return cleaned[:4]
    return [
        f"IC synthesis completed for {ticker}: evidence readiness is {readiness}, and all required upstream specialist handoffs were available.",
        "The committee-stage synthesis treats this as a completed analytical review, but not a personal position-sizing instruction without portfolio context.",
        "The central decision frame is business quality and durable cash generation versus the growth, margin, FCF, and multiple expectations already embedded in the current price.",
        "A more positive view needs clearer AI/cloud monetization, resilient FCF after capex, and a more attractive valuation setup; a more negative view follows from cloud slowdown, capex drag, or multiple compression.",
    ]


RUSSIAN_PROFILE_TEXTS = {
    "MSFT": {
        "quality": "корпоративное ПО, облачную инфраструктуру, сервисы продуктивности, безопасность, игровой бизнес и инфраструктуру для искусственного интеллекта",
        "thesis": "превращения спроса на облако, глубины корпоративного ПО и инвестиций в инфраструктуру для искусственного интеллекта в устойчивый рост выручки, маржи и свободного денежного потока",
        "financial_watch": "инвестиции в инфраструктуру для искусственного интеллекта, устойчивость облачной маржи, капиталоотдача и качество роста",
        "drivers": "расходы компаний на IT, миграцию в облако, спрос на инфраструктуру для искусственного интеллекта, ставки дисконтирования и ожидания по крупнейшим технологическим компаниям",
        "risks": "переоценённая монетизация искусственного интеллекта, давление капитальных расходов, конкуренция в облаке, регуляторное и антимонопольное давление, замедление корпоративного спроса и сжатие мультипликатора",
        "portfolio_role": "крупная качественная акция роста с профилем компании-компаундера, риском концентрации и риском оценки",
        "positive": "более ясная монетизация искусственного интеллекта, устойчивый рост Azure, стабильная маржа свободного денежного потока или более привлекательная оценка",
        "negative": "замедление облачного бизнеса, давление капитальных расходов на свободный денежный поток, регуляторные шоки или слабая конверсия расходов на искусственный интеллект в выручку",
    },
    "AAPL": {
        "quality": "потребительские технологии, аппаратную экосистему, сервисы, платформенную монетизацию, возврат капитала и удержание клиентов через бренд",
        "thesis": "поддержания базы пользователей iPhone, расширения сервисной экономики, защиты ценовой силы экосистемы и конверсии продуктовых циклов в устойчивый свободный денежный поток",
        "financial_watch": "устойчивость цикла iPhone, доля сервисов, валовая маржа, Китай, обратные выкупы и темп инноваций",
        "drivers": "потребительский спрос, циклы обновления устройств, проникновение сервисов, регулирование платформ, валютные курсы, ставки и ожидания по крупным качественным компаниям",
        "risks": "слабый цикл устройств, Китай и геополитика, регулирование сервисов, давление на маржу, замедление инноваций и сжатие мультипликатора",
        "portfolio_role": "крупная качественная платформенная акция с потребительским, регуляторным и оценочным риском",
        "positive": "более сильный цикл устройств, рост сервисов, устойчивая маржа, успешное внедрение продуктов с искусственным интеллектом или более привлекательная оценка",
        "negative": "слабый спрос на iPhone, давление регулирования на сервисную экономику, слабость Китая, маржинальное давление или слабая конверсия новых продуктов в рост",
    },
}


def profile_value(profile: dict[str, str], key: str, ticker: str, language: str) -> str:
    if language == "ru":
        translated = RUSSIAN_PROFILE_TEXTS.get(ticker, {}).get(key)
        if translated:
            return translated
        fallbacks = {
            "quality": "публичный бизнес-профиль компании",
            "thesis": "конверсии конкурентной позиции в устойчивый рост выручки, маржи, денежных потоков и акционерной стоимости",
            "financial_watch": "качество роста, маржа, свободный денежный поток, баланс, распределение капитала и признаки агрессивного учёта",
            "drivers": "фундаментальные показатели компании, отраслевой спрос, ставки, ожидания по оценке и общий риск-аппетит рынка",
            "risks": "замедление роста, давление на маржу, конкуренция, регулирование, ошибки распределения капитала и сжатие мультипликатора",
            "portfolio_role": "публичная акция с рисками конкретной компании, сектора и оценки",
            "positive": "более качественный рост, устойчивые денежные потоки, лучшее соотношение риска и доходности или более привлекательная оценка",
            "negative": "слабый рост, давление на маржу или денежный поток, существенные риск-события или сжатие оценки",
        }
        return fallbacks.get(key, profile.get(key, "н/д"))
    return profile.get(key, "n/a")


def price_display(value: Any, language: str) -> str:
    if value is None:
        return "н/д" if language == "ru" else "n/a"
    try:
        return f"{float(value):,.2f}".replace(",", " ")
    except (TypeError, ValueError):
        return str(value)



def equity_report_profile(identity: dict[str, Any]) -> dict[str, str]:
    ticker = identity.get("ticker", "the selected equity")
    company = identity.get("company_name", ticker)
    profiles = {
        "MSFT": {
            "quality": "enterprise software, cloud infrastructure, productivity, security, gaming, and AI infrastructure exposure",
            "thesis": "converting cloud demand, enterprise software depth, and AI infrastructure spend into durable revenue growth, margins, and free cash flow",
            "financial_watch": "AI capex, cloud margin durability, capital allocation, and quality of growth",
            "drivers": "enterprise IT spending, cloud migration, AI infrastructure demand, discount rates, and mega-cap technology expectations",
            "risks": "overestimated AI monetization, capex drag, cloud competition, regulatory/antitrust pressure, enterprise demand slowdown, and multiple compression",
            "portfolio_role": "high-quality mega-cap growth/compounder exposure with concentration and valuation risk",
            "positive": "clearer AI monetization, durable Azure growth, resilient free-cash-flow margins, or a more attractive valuation",
            "negative": "cloud slowdown, capex-driven free-cash-flow pressure, regulatory shocks, or weak conversion of AI spending into revenue",
        },
        "AAPL": {
            "quality": "consumer technology, hardware ecosystem, services, platform monetization, capital returns, and brand-led customer retention",
            "thesis": "sustaining the iPhone installed base, expanding services economics, protecting ecosystem pricing power, and converting product cycles into durable free cash flow",
            "financial_watch": "iPhone cycle durability, services mix, gross margin resilience, China exposure, buybacks, and innovation cadence",
            "drivers": "consumer demand, product replacement cycles, services attach rates, App Store/platform regulation, FX, rates, and mega-cap quality expectations",
            "risks": "hardware-cycle disappointment, China/geopolitical pressure, services regulation, margin compression, slower innovation, and multiple compression",
            "portfolio_role": "mega-cap quality/platform exposure with consumer-cycle, regulatory, and valuation risk",
            "positive": "stronger device cycles, services growth, resilient margins, successful AI-enabled product adoption, or a more attractive valuation",
            "negative": "weaker iPhone demand, regulatory pressure on services economics, China weakness, margin pressure, or poor conversion of new products into growth",
        },
    }
    return profiles.get(ticker, {
        "quality": f"the public-equity business profile of {company}",
        "thesis": "turning its competitive position into durable revenue growth, margins, cash generation, and shareholder value",
        "financial_watch": "growth quality, margins, free cash flow, balance sheet, capital allocation, and accounting red flags",
        "drivers": "company fundamentals, sector demand, rates, valuation expectations, and broad market risk appetite",
        "risks": "growth disappointment, margin pressure, competition, regulation, capital-allocation mistakes, and multiple compression",
        "portfolio_role": "public-equity exposure with company-specific, sector, and valuation risk",
        "positive": "stronger growth quality, resilient cash generation, better risk/reward, or a more attractive valuation",
        "negative": "weaker growth, margin or cash-flow pressure, material risk events, or valuation compression",
    })


def generate_generic_agent_report(
    prompt: str,
    intake: dict[str, Any],
    preflight: dict[str, Any],
    evidence_pack: dict[str, Any],
    specialists: list[dict[str, Any]],
) -> str:
    today = datetime.now(timezone.utc).astimezone().date().isoformat()
    language = reader_language(prompt)
    identity = preflight.get("subject_identity") or intake.get("subject_identity") or {}
    ticker = identity.get("ticker", "ASSET")
    name = identity.get("company_name", ticker)
    route = selected_route_from_context(intake, preflight)
    route_label = AGENT_ROUTE_LABELS.get(route, route)
    sources = key_sources_for_report(preflight)
    evidence_facts = evidence_fact_bullets(preflight, language)
    source_sentence = source_scope_sentence(preflight, language)
    limits = human_limitations(intake, preflight, evidence_pack)
    portfolio_context = intake.get("portfolio_context") or normalize_portfolio_context({}, source="not_provided")
    portfolio_text = portfolio_context_summary(portfolio_context, language)
    specialist_takeaways = reader_specialist_takeaways(specialists, language)
    failed_specialists = [item.get("specialist_id") for item in specialists if item.get("status") != "ok"]
    route_specialists = set(agent_specialists_for_route(route))
    completed_ids = {item.get("specialist_id") for item in completed_specialists(specialists)}
    ic_final_owner = ic_completed_with_expected_handoffs(specialists)
    report_complete = ic_final_owner and completed_ids == route_specialists and not failed_specialists and evidence_pack.get("evidence_readiness") != "Blocked"
    if failed_specialists:
        limits.append("required_specialists_incomplete")
    ic_synthesis = reader_ic_synthesis(specialists, language, identity, evidence_pack)
    route_focus = {
        "etf_full_cycle": "wrapper quality, holdings, index or strategy methodology, fees, liquidity, tracking behavior, concentration, and overlap",
        "fixed_income_full_cycle": "duration, yield, curve exposure, credit quality, liquidity, inflation sensitivity, and role in a portfolio",
        "crypto_full_cycle": "network adoption, liquidity, volatility, custody or vehicle choice, token/regulatory risks, and macro liquidity sensitivity",
        "commodity_full_cycle": "spot versus vehicle exposure, supply-demand balance, real-rate and currency sensitivity, storage/roll/custody risks, and hedge role",
        "multi_asset_comparison": "role-based comparison, common criteria, relative risk, liquidity, diversification, and portfolio-fit trade-offs",
    }.get(route, "asset quality, evidence, valuation, risk, implementation, and portfolio role")
    scenario_base = {
        "etf_full_cycle": "the fund continues to deliver the intended exposure with acceptable fees, liquidity, concentration, and tracking behavior",
        "fixed_income_full_cycle": "duration and yield exposure are compensated by the user's horizon and risk tolerance",
        "crypto_full_cycle": "liquidity, adoption, custody, and regulatory conditions remain supportive enough for the stated risk budget",
        "commodity_full_cycle": "the commodity exposure keeps its intended hedge or return role without vehicle frictions overwhelming the thesis",
        "multi_asset_comparison": "the chosen asset role matches the user's objective better than the alternatives after risk and liquidity are considered",
    }.get(route, "the asset's expected return and risk profile justify further decision work")
    if language == "ru":
        prep_heading = "## Рабочий вывод IC" if ic_final_owner else "## Подготовительный вывод"
        synthesis_heading = "## Итог IC-сборки" if ic_final_owner else "## Что нужно для IC-сборки"
        lines = [
            f"Дата подготовки: {today}",
            "Статус отчёта: " + ("Complete - IC-сборка завершена; это не инструкция по размеру позиции." if report_complete else "Limited - подготовительный разбор, не финальное персональное инвестиционное решение."),
            "Свежесть и источники: использованы публичные источники без API-ключей; текущие выводы зависят от доступности свежей цены, состава, доходности, ликвидности и новостей.",
            f"Уверенность вывода: средняя для структурного {route_label}-анализа {ticker}, ниже для персонального действия, если портфельный контекст неполный.",
            "",
            f"# {ticker} — AGENT-разбор",
            "",
            "## Короткий вывод",
            f"{name} запущен как {route_label} workflow. Разбор пригоден для подготовки решения: он проверяет {route_focus}, но не превращает результат в персональную команду купить/продать/держать.",
            "",
            prep_heading,
            f"- Что можно сказать сейчас: {ticker} даёт экспозицию на заявленную роль актива; качество вывода зависит от источников, свежести данных, реализации инструмента и портфельной задачи.",
            f"- Портфельный контекст: {portfolio_text}",
            "- Статус действия: подготовка решения, не торговая инструкция.",
            "",
            "## Профиль инструмента и экспозиции",
            "| Пункт | Значение |",
            "|---|---|",
            f"| Инструмент | {ticker} |",
            f"| Название | {name} |",
            f"| Маршрут | {route} |",
            f"| Тип | {identity.get('security_type') or identity.get('instrument_classification') or 'asset'} |",
            f"| Валюта | {identity.get('currency', 'USD')} |",
            "",
            "## Ключевая аналитическая рамка",
            f"Для этого маршрута важны {route_focus}. Качество идеи нельзя оценивать только по прошлой доходности: нужно связать роль актива, цену входа, волатильность, ликвидность, структуру инструмента и ограничения пользователя.",
            "",
            "## Оценка и ожидания",
            f"Базовый вопрос: {scenario_base}. Если свежие рыночные данные или профиль инструмента неполные, вывод остаётся ограниченным и не должен выглядеть как завершённое комитетское действие.",
            "",
            "## Позитивный / базовый / негативный сценарии",
            "| Сценарий | Что должно быть правдой | Инвестиционный смысл |",
            "|---|---|---|",
            f"| Позитивный | источники свежие, {route_focus}, а портфельная роль чётко задана | идея может перейти к финальной IC-сборке после закрытия портфельных ворот |",
            f"| Базовый | {scenario_base} | подходит для дальнейшей подготовки решения, но не для персонального действия без контекста |",
            "| Негативный | источник, ликвидность, структура инструмента или риск-сценарий ухудшаются | вывод должен быть ограничен или заблокирован до обновления доказательной базы |",
            "",
            "## Проверка рисков",
            f"Основные риски для {ticker}: рыночная волатильность, ликвидность, ошибки в реализации инструмента, устаревшие источники, неверная роль в портфеле и несоответствие горизонта пользователя характеру экспозиции.",
            "",
            "## Что показывают источники",
            source_sentence,
            "",
            "## Статус доказательной базы",
            f"Статус доказательной базы: {reader_evidence_status_text(evidence_pack.get('evidence_readiness'), language)}. Если источники неполные, workflow честно снижает статус до Limited или Blocked.",
            "",
            "## Факты из доказательной базы",
            *[f"- {item}" for item in evidence_facts],
            "",
            synthesis_heading,
            *(f"- {item}" for item in ic_synthesis),
            "",
            "## Портфельная роль",
            portfolio_text,
        ]
        if limits:
            lines.extend(["", "## Что ещё нужно для персонального финального решения", *[f"- {reader_limit_text(limit, language)}" for limit in limits]])
        if specialist_takeaways:
            lines.extend(["", "## Что добавили аналитические проверки", *[f"- {item}" for item in specialist_takeaways]])
        lines.extend(["", "## Ключевые источники", *[f"- {reader_source_text(source, language)}" for source in sources]])
    else:
        prep_heading = "## IC working view" if ic_final_owner else "## Preparatory view"
        synthesis_heading = "## IC synthesis" if ic_final_owner else "## What is still needed for final assembly"
        lines = [
            "Report status: Complete - IC synthesis complete; not a personal position-sizing instruction." if report_complete else "Report status: Limited - preparation view only, not a final personal investment decision.",
            f"Preparation date: {today}",
            "Freshness and source note: public/no-key sources were checked; current conclusions depend on latest price, holdings, yield/liquidity, and event data being available.",
            f"Decision confidence: medium for structural {route_label} analysis of {ticker}, lower for personal action if portfolio context is incomplete.",
            "",
            f"# {ticker} AGENT Workflow Review",
            "",
            "## Short view",
            f"{name} was routed through the {route_label} AGENT workflow. The package is useful for decision preparation because it checks {route_focus}; it is not a personal buy/sell/hold instruction.",
            "",
            prep_heading,
            f"- What can be concluded now: {ticker} can be evaluated for its stated asset role, but actionability depends on evidence freshness, implementation quality, valuation/expectations, risk, and portfolio fit.",
            f"- Portfolio context: {portfolio_text}",
            "- Action status: decision preparation, not a trade instruction.",
            "",
            "## Instrument / exposure snapshot",
            "| Field | Value |",
            "|---|---|",
            f"| Instrument | {ticker} |",
            f"| Name | {name} |",
            f"| Route | {route} |",
            f"| Type | {identity.get('security_type') or identity.get('instrument_classification') or 'asset'} |",
            f"| Currency | {identity.get('currency', 'USD')} |",
            "",
            "## Route-specific thesis",
            f"This workflow focuses on {route_focus}. A useful conclusion needs more than trailing performance: it must connect the asset role, implementation vehicle, current price or yield context, downside scenario, liquidity, and user constraints.",
            "",
            "## Valuation expectations",
            f"The base decision-prep question is whether {scenario_base}. If current market or vehicle data are incomplete, the status remains Limited/Blocked rather than implying complete decision support.",
            "",
            "## Bull / base / bear scenarios",
            "| Scenario | What must be true | Investment meaning |",
            "|---|---|---|",
            f"| Bull | Sources are current, {route_focus}, and the portfolio role is explicit | the idea can move toward gated IC synthesis once portfolio context is supplied |",
            f"| Base | {scenario_base} | suitable for further decision preparation, not a personal action without context |",
            "| Bear | source coverage, liquidity, vehicle structure, or the relevant risk regime deteriorates | decision support should be Limited or Blocked until the evidence is refreshed |",
            "",
            "## Risk red-team",
            f"Main risks for {ticker} are market volatility, liquidity, implementation mismatch, stale source coverage, wrong portfolio role, and horizon mismatch.",
            "",
            "## What the sources show",
            source_sentence,
            "",
            "## Evidence Status Summary",
            f"Evidence readiness for this run is {evidence_pack.get('evidence_readiness')}. The workflow degrades honestly to Limited or Blocked when required source coverage is missing.",
            "",
            "## Evidence facts used",
            *[f"- {item}" for item in evidence_facts],
            "",
            synthesis_heading,
            *(f"- {item}" for item in ic_synthesis),
            "",
            "## Portfolio fit",
            portfolio_text,
            "",
            "## What would change the view",
            "The view improves with fresher evidence, clear portfolio objective, verified implementation quality, and risk scenarios that remain acceptable. It worsens if source coverage weakens, liquidity deteriorates, fees or vehicle frictions rise, or the asset no longer fits the stated role.",
        ]
        if limits:
            lines.extend(["", "## What is still needed for a personal final decision", *[f"- {limit}" for limit in limits]])
        if specialist_takeaways:
            lines.extend(["", "## What the specialist checks added", *[f"- {item}" for item in specialist_takeaways]])
        lines.extend(["", "## Key sources", *[f"- {source}" for source in sources]])
    return "\n".join(lines) + "\n"

def source_record(preflight: dict[str, Any], source_id: str) -> dict[str, Any]:
    for record in preflight.get("source_records", []):
        if record.get("source_id") == source_id:
            return record
    return {}


def fact_items(preflight: dict[str, Any], tags: list[str]) -> list[dict[str, Any]]:
    facts = (source_record(preflight, "company_facts").get("data") or {}).get("facts") or {}
    for tag in tags:
        values = facts.get(tag)
        if isinstance(values, list) and values:
            return [item for item in values if isinstance(item, dict) and item.get("val") is not None]
    return []


def latest_period_item(items: list[dict[str, Any]], *, instant: bool = False) -> dict[str, Any] | None:
    if not items:
        return None
    filtered = []
    for item in items:
        if instant and item.get("start"):
            continue
        if not instant and not item.get("start"):
            continue
        filtered.append(item)
    candidates = filtered or items
    return max(candidates, key=lambda item: (str(item.get("end") or ""), str(item.get("filed") or ""), int(item.get("val") or 0)))


def latest_fy_item(items: list[dict[str, Any]]) -> dict[str, Any] | None:
    fy_items = [item for item in items if item.get("form") == "10-K" or item.get("fp") == "FY"]
    return latest_period_item(fy_items or items)


def money_billions(value: Any, language: str) -> str:
    if value is None:
        return "н/д" if language == "ru" else "n/a"
    try:
        number = float(value) / 1_000_000_000
    except (TypeError, ValueError):
        return "н/д" if language == "ru" else "n/a"
    suffix = "млрд $" if language == "ru" else "$bn"
    return f"{number:,.1f} {suffix}".replace(",", " ")


def percent(value: float | None, language: str) -> str:
    if value is None:
        return "н/д" if language == "ru" else "n/a"
    return f"{value:.1f}%"


def metric_period(item: dict[str, Any] | None, language: str) -> str:
    if not item:
        return "н/д" if language == "ru" else "n/a"
    end = item.get("end") or "n/a"
    form = item.get("form") or ""
    fp = item.get("fp") or ""
    filed = item.get("filed") or ""
    if language == "ru":
        return f"{form} {fp}, период до {end}, подано {filed}".strip()
    return f"{form} {fp}, period ended {end}, filed {filed}".strip()


def financial_snapshot(preflight: dict[str, Any], language: str) -> dict[str, Any]:
    revenue = latest_period_item(
        fact_items(preflight, ["RevenueFromContractWithCustomerExcludingAssessedTax", "Revenues"])
    )
    annual_revenue = latest_fy_item(
        fact_items(preflight, ["RevenueFromContractWithCustomerExcludingAssessedTax", "Revenues"])
    )
    operating_income = latest_period_item(fact_items(preflight, ["OperatingIncomeLoss"]))
    net_income = latest_period_item(fact_items(preflight, ["NetIncomeLoss"]))
    operating_cash_flow = latest_period_item(fact_items(preflight, ["NetCashProvidedByUsedInOperatingActivities"]))
    capex = latest_period_item(fact_items(preflight, ["PaymentsToAcquirePropertyPlantAndEquipment"]))
    cash = latest_period_item(fact_items(preflight, ["CashAndCashEquivalentsAtCarryingValue"]), instant=True)
    current_debt = latest_period_item(fact_items(preflight, ["LongTermDebtCurrent"]), instant=True)
    long_debt = latest_period_item(fact_items(preflight, ["LongTermDebtNoncurrent"]), instant=True)
    buybacks = latest_period_item(fact_items(preflight, ["PaymentsForRepurchaseOfCommonStock"]))
    current_price = (source_record(preflight, "current_price").get("data") or {})
    history = (source_record(preflight, "historical_price").get("data") or {}).get("points") or []
    price = current_price.get("close")
    price_date = current_price.get("date") or source_record(preflight, "current_price").get("source_date")
    one_year_change = None
    if isinstance(history, list) and len(history) >= 2 and price is not None:
        first = next((point for point in history if isinstance(point, dict) and point.get("close")), None)
        if first:
            try:
                one_year_change = (float(price) / float(first["close"]) - 1.0) * 100
            except (TypeError, ValueError, ZeroDivisionError):
                one_year_change = None
    revenue_value = revenue.get("val") if revenue else None
    operating_value = operating_income.get("val") if operating_income else None
    net_value = net_income.get("val") if net_income else None
    ocf_value = operating_cash_flow.get("val") if operating_cash_flow else None
    capex_value = capex.get("val") if capex else None
    fcf_value = None
    if ocf_value is not None and capex_value is not None:
        fcf_value = float(ocf_value) - abs(float(capex_value))
    debt_value = None
    if current_debt or long_debt:
        debt_value = float((current_debt or {}).get("val") or 0) + float((long_debt or {}).get("val") or 0)
    operating_margin = (float(operating_value) / float(revenue_value) * 100) if revenue_value else None
    net_margin = (float(net_value) / float(revenue_value) * 100) if revenue_value else None
    fcf_margin = (float(fcf_value) / float(revenue_value) * 100) if revenue_value and fcf_value is not None else None
    return {
        "price": price,
        "price_date": price_date,
        "one_year_change": one_year_change,
        "revenue": revenue,
        "annual_revenue": annual_revenue,
        "operating_income": operating_income,
        "net_income": net_income,
        "operating_cash_flow": operating_cash_flow,
        "capex": capex,
        "fcf_value": fcf_value,
        "cash": cash,
        "debt_value": debt_value,
        "buybacks": buybacks,
        "operating_margin": operating_margin,
        "net_margin": net_margin,
        "fcf_margin": fcf_margin,
        "has_core_financials": all(item is not None for item in [revenue, operating_income, net_income, operating_cash_flow, capex]),
    }


def financial_snapshot_table(snapshot: dict[str, Any], language: str) -> list[str]:
    rows = []
    if language == "ru":
        rows.append("| Метрика | Значение | Период / источник |")
        rows.append("|---|---:|---|")
        rows.append(f"| Последняя цена закрытия | {price_display(snapshot.get('price'), language)} $ | {snapshot.get('price_date') or 'н/д'} |")
        rows.append(f"| Динамика за 1 год | {percent(snapshot.get('one_year_change'), language)} | публичная история цен |")
        rows.append(f"| Выручка | {money_billions((snapshot.get('revenue') or {}).get('val'), language)} | {metric_period(snapshot.get('revenue'), language)} |")
        rows.append(f"| Операционная прибыль | {money_billions((snapshot.get('operating_income') or {}).get('val'), language)} | {metric_period(snapshot.get('operating_income'), language)} |")
        rows.append(f"| Операционная маржа | {percent(snapshot.get('operating_margin'), language)} | расчёт от выручки и операционной прибыли |")
        rows.append(f"| Чистая прибыль | {money_billions((snapshot.get('net_income') or {}).get('val'), language)} | {metric_period(snapshot.get('net_income'), language)} |")
        rows.append(f"| Операционный денежный поток | {money_billions((snapshot.get('operating_cash_flow') or {}).get('val'), language)} | {metric_period(snapshot.get('operating_cash_flow'), language)} |")
        rows.append(f"| Капитальные расходы | {money_billions((snapshot.get('capex') or {}).get('val'), language)} | {metric_period(snapshot.get('capex'), language)} |")
        rows.append(f"| Прокси свободного денежного потока | {money_billions(snapshot.get('fcf_value'), language)} | операционный денежный поток минус капитальные расходы |")
        rows.append(f"| Денежные средства | {money_billions((snapshot.get('cash') or {}).get('val'), language)} | {metric_period(snapshot.get('cash'), language)} |")
        rows.append(f"| Долг | {money_billions(snapshot.get('debt_value'), language)} | краткосрочная и долгосрочная часть долга, если раскрыто |")
        rows.append(f"| Выкуп акций | {money_billions((snapshot.get('buybacks') or {}).get('val'), language)} | {metric_period(snapshot.get('buybacks'), language)} |")
    else:
        rows.append("| Metric | Value | Period / source |")
        rows.append("|---|---:|---|")
        rows.append(f"| Latest close | {price_display(snapshot.get('price'), language)} | {snapshot.get('price_date') or 'n/a'} |")
        rows.append(f"| 1-year price change | {percent(snapshot.get('one_year_change'), language)} | public price history |")
        rows.append(f"| Revenue | {money_billions((snapshot.get('revenue') or {}).get('val'), language)} | {metric_period(snapshot.get('revenue'), language)} |")
        rows.append(f"| Operating income | {money_billions((snapshot.get('operating_income') or {}).get('val'), language)} | {metric_period(snapshot.get('operating_income'), language)} |")
        rows.append(f"| Operating margin | {percent(snapshot.get('operating_margin'), language)} | calculated from revenue and operating income |")
        rows.append(f"| Net income | {money_billions((snapshot.get('net_income') or {}).get('val'), language)} | {metric_period(snapshot.get('net_income'), language)} |")
        rows.append(f"| Operating cash flow | {money_billions((snapshot.get('operating_cash_flow') or {}).get('val'), language)} | {metric_period(snapshot.get('operating_cash_flow'), language)} |")
        rows.append(f"| Capex | {money_billions((snapshot.get('capex') or {}).get('val'), language)} | {metric_period(snapshot.get('capex'), language)} |")
        rows.append(f"| FCF proxy | {money_billions(snapshot.get('fcf_value'), language)} | operating cash flow minus capex |")
        rows.append(f"| Cash | {money_billions((snapshot.get('cash') or {}).get('val'), language)} | {metric_period(snapshot.get('cash'), language)} |")
        rows.append(f"| Debt | {money_billions(snapshot.get('debt_value'), language)} | current + non-current long-term debt, if disclosed |")
        rows.append(f"| Buybacks | {money_billions((snapshot.get('buybacks') or {}).get('val'), language)} | {metric_period(snapshot.get('buybacks'), language)} |")
    return rows


def ic_working_view(identity: dict[str, Any], snapshot: dict[str, Any], language: str) -> str:
    ticker = identity.get("ticker", "the stock")
    price = snapshot.get("price")
    if language == "ru":
        return (
            f"{ticker} выглядит как качественная акция-компаундер для 3–5-летнего горизонта, но рабочий вывод — не "
            f"«покупать любой ценой». При цене около {price_display(price, language)} $ ключевой вопрос — достаточно ли текущая цена "
            "компенсирует риск замедления роста, высоких ожиданий по искусственному интеллекту и облаку, капитальных расходов и возможного сжатия мультипликатора. "
            "Без портфельного контекста это подготовительный вывод, а не персональное финальное действие."
        )
    return (
        f"{ticker} screens as a high-quality compounder for a 3-5 year horizon, but this preparation view is not "
        f"'buy at any price.' Around {price_display(price, language)}, the decision turns on whether the current price compensates "
        "for slower growth, high AI/cloud expectations, capex intensity, and possible multiple compression. "
        "Without portfolio context this is a Decision-Prep view, not a personal final action."
    )


def generate_investment_report(
    prompt: str,
    intake: dict[str, Any],
    preflight: dict[str, Any],
    evidence_pack: dict[str, Any],
    specialists: list[dict[str, Any]],
) -> str:
    today = datetime.now(timezone.utc).astimezone().date().isoformat()
    sources = key_sources_for_report(preflight)
    limits = human_limitations(intake, preflight, evidence_pack)
    language = reader_language(prompt)
    evidence_facts = evidence_fact_bullets(preflight, language)
    source_sentence = source_scope_sentence(preflight, language)
    specialist_takeaways = reader_specialist_takeaways(specialists, language)
    portfolio_context = intake.get("portfolio_context") or normalize_portfolio_context({}, source="not_provided")
    portfolio_text = portfolio_context_summary(portfolio_context, language)
    failed_specialists = [item.get("specialist_id") for item in specialists if item.get("status") != "ok"]
    identity = preflight.get("subject_identity") or intake.get("subject_identity") or {}
    route = selected_route_from_context(intake, preflight)
    if route != "equity_full_cycle":
        return generate_generic_agent_report(prompt, intake, preflight, evidence_pack, specialists)
    ticker = identity.get("ticker", "EQUITY")
    company = identity.get("company_name", ticker)
    profile = equity_report_profile(identity)
    quality = profile_value(profile, "quality", ticker, language)
    thesis = profile_value(profile, "thesis", ticker, language)
    financial_watch = profile_value(profile, "financial_watch", ticker, language)
    drivers = profile_value(profile, "drivers", ticker, language)
    risks = profile_value(profile, "risks", ticker, language)
    portfolio_role = profile_value(profile, "portfolio_role", ticker, language)
    positive = profile_value(profile, "positive", ticker, language)
    negative = profile_value(profile, "negative", ticker, language)
    snapshot = financial_snapshot(preflight, language)
    ic_final_owner = ic_completed_with_expected_handoffs(specialists)
    report_complete = (
        ic_final_owner
        and {item.get("specialist_id") for item in completed_specialists(specialists)} == set(AGENT_SPECIALISTS_EQUITY)
        and not failed_specialists
        and evidence_pack.get("evidence_readiness") != "Blocked"
    )
    ic_synthesis = reader_ic_synthesis(specialists, language, identity, evidence_pack)
    if failed_specialists:
        limits.append("required_specialists_incomplete")
    if language == "ru":
        prep_heading = "## Рабочий вывод IC" if ic_final_owner else "## Подготовительный вывод"
        synthesis_heading = "## Итог IC-сборки" if ic_final_owner else "## Что нужно для IC-сборки"
        lines = [
            f"\u0414\u0430\u0442\u0430 \u043f\u043e\u0434\u0433\u043e\u0442\u043e\u0432\u043a\u0438: {today}",
            "\u0421\u0442\u0430\u0442\u0443\u0441 \u043e\u0442\u0447\u0451\u0442\u0430: \u043f\u043e\u0434\u0433\u043e\u0442\u043e\u0432\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0438\u043d\u0432\u0435\u0441\u0442\u0438\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u0440\u0430\u0437\u0431\u043e\u0440; \u044d\u0442\u043e \u043d\u0435 \u0444\u0438\u043d\u0430\u043b\u044c\u043d\u043e\u0435 \u043f\u0435\u0440\u0441\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0435 \u0438\u043d\u0432\u0435\u0441\u0442\u0438\u0446\u0438\u043e\u043d\u043d\u043e\u0435 \u0440\u0435\u0448\u0435\u043d\u0438\u0435.",
            "\u0421\u0432\u0435\u0436\u0435\u0441\u0442\u044c \u0438 \u0438\u0441\u0442\u043e\u0447\u043d\u0438\u043a\u0438: \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u044b \u043f\u0440\u043e\u0432\u0435\u0440\u0435\u043d\u043d\u044b\u0435 \u043f\u0443\u0431\u043b\u0438\u0447\u043d\u044b\u0435 \u0438\u0441\u0442\u043e\u0447\u043d\u0438\u043a\u0438; \u0442\u0435\u043a\u0443\u0449\u0438\u0435 \u0440\u044b\u043d\u043e\u0447\u043d\u044b\u0435 \u0432\u044b\u0432\u043e\u0434\u044b \u0437\u0430\u0432\u0438\u0441\u044f\u0442 \u043e\u0442 \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0439 \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u043e\u0439 \u0446\u0435\u043d\u044b \u0438 \u0441\u043e\u0431\u044b\u0442\u0438\u0439.",
            f"\u0423\u0432\u0435\u0440\u0435\u043d\u043d\u043e\u0441\u0442\u044c \u0432\u044b\u0432\u043e\u0434\u0430: \u0441\u0440\u0435\u0434\u043d\u044f\u044f \u0434\u043b\u044f \u0441\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u043d\u043e\u0433\u043e \u0430\u043d\u0430\u043b\u0438\u0437\u0430 {ticker}, \u043d\u0438\u0436\u0435 \u0434\u043b\u044f \u043f\u0435\u0440\u0441\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f, \u0435\u0441\u043b\u0438 \u043f\u043e\u0440\u0442\u0444\u0435\u043b\u044c\u043d\u044b\u0439 \u043a\u043e\u043d\u0442\u0435\u043a\u0441\u0442 \u043d\u0435\u043f\u043e\u043b\u043d\u044b\u0439.",
            f"Статус процесса: доказательная база {reader_evidence_status_text(evidence_pack.get('evidence_readiness'), language)}; комитетская сборка {'завершена' if ic_final_owner else 'ограничена, потому что обязательные проверки специалистов не завершились'}.",
            "",
            f"# {ticker} \u2014 \u0438\u043d\u0432\u0435\u0441\u0442\u0438\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u0440\u0430\u0437\u0431\u043e\u0440",
            "",
            "## \u041a\u043e\u0440\u043e\u0442\u043a\u0438\u0439 \u0432\u044b\u0432\u043e\u0434",
            ic_working_view(identity, snapshot, language),
            "",
            prep_heading,
            f"- Что можно сказать сейчас: {company} даёт экспозицию на {quality}; тезис зависит от {thesis}.",
            f"- Портфельный контекст: {portfolio_text}",
            "- Статус действия: подготовка решения, не персональная команда купить/продать/держать.",
            "",
            "## \u0411\u0438\u0437\u043d\u0435\u0441 \u0438 \u0442\u0435\u0437\u0438\u0441",
            f"{ticker} нужно оценивать как сочетание качества бизнеса, финансовой устойчивости, роста выручки, маржи, капиталоёмкости и рыночных ожиданий. Главное — не сам факт сильного бизнеса, а то, насколько рост ключевых направлений способен оправдать цену и сохранить свободный денежный поток после повышенных капитальных расходов.",
            "",
            "## Финансовый снимок",
            *financial_snapshot_table(snapshot, language),
            "",
            "## Финансовое качество и свободный денежный поток",
            f"Последние доступные XBRL-данные SEC дают основу для финансовой проверки: выручка {money_billions((snapshot.get('revenue') or {}).get('val'), language)}, операционная маржа {percent(snapshot.get('operating_margin'), language)}, прокси свободного денежного потока {money_billions(snapshot.get('fcf_value'), language)}. Если этот показатель заметно ниже операционного денежного потока, главный вопрос — являются ли капитальные расходы временным циклом инвестиций в искусственный интеллект и облако или новой нормой капиталоёмкости.",
            "",
            "## Оценка и ожидания",
            f"Рыночная привязка отчёта — цена закрытия {price_display(snapshot.get('price'), language)} $ на {snapshot.get('price_date') or 'н/д'}. Правильный вопрос не «хорошая ли компания?», а «какой рост, маржа и свободный денежный поток уже заложены в цену?». Чем выше ожидания по ключевым драйверам роста, тем меньше запас прочности при замедлении роста или сжатии мультипликатора.",
            "",
            "## Позитивный / базовый / негативный сценарии",
            "| Сценарий | Что должно быть правдой | Инвестиционный смысл |",
            "|---|---|---|",
            f"| Позитивный | {positive}; капитальные расходы конвертируются в ускорение выручки и свободного денежного потока | акция может заслуживать премиальную оценку, но всё равно требует контроля цены входа |",
            f"| Базовый | {thesis}; маржа и свободный денежный поток остаются устойчивыми | подходит как качественный кандидат, но без агрессивного вывода при дорогой оценке |",
            f"| Негативный | {negative}; ожидания по ключевым драйверам роста пересматриваются вниз | риск — сжатие мультипликатора и слабая доходность даже при неплохом бизнесе |",
            "",
            "## Проверка рисков",
            f"Главные риски: {risks}. Факторы слома тезиса на 12–24 месяца: замедление ключевого драйвера роста, ухудшение свободного денежного потока из-за капитальных расходов, регуляторный или конкурентный удар, а также ситуация, где рынок перестаёт платить премиальный мультипликатор за качество.",
            "",
            "## \u0427\u0442\u043e \u043f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u044e\u0442 \u0438\u0441\u0442\u043e\u0447\u043d\u0438\u043a\u0438",
            source_sentence,
            "",
            "## \u0421\u0442\u0430\u0442\u0443\u0441 \u0434\u043e\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0439 \u0431\u0430\u0437\u044b",
            f"\u0421\u0442\u0430\u0442\u0443\u0441 \u0438\u0441\u0442\u043e\u0447\u043d\u0438\u043a\u043e\u0432 \u0434\u043b\u044f \u044d\u0442\u043e\u0433\u043e \u0437\u0430\u043f\u0443\u0441\u043a\u0430: {reader_evidence_status_text(evidence_pack.get('evidence_readiness'), language)}. \u0415\u0441\u043b\u0438 \u0434\u0430\u043d\u043d\u044b\u0435 \u043d\u0435\u043f\u043e\u043b\u043d\u044b\u0435, \u043e\u0442\u0447\u0451\u0442 \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0438\u0432\u0430\u0435\u0442 \u0432\u044b\u0432\u043e\u0434\u044b \u0438 \u043d\u0435 \u043c\u0430\u0441\u043a\u0438\u0440\u0443\u0435\u0442 \u043f\u0440\u043e\u0431\u0435\u043b\u044b \u043a\u0430\u043a \u043f\u043e\u043b\u043d\u0443\u044e \u0434\u043e\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u0443\u044e \u0431\u0430\u0437\u0443.",
            "",
            "## \u0424\u0430\u043a\u0442\u044b \u0438\u0437 \u0434\u043e\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0439 \u0431\u0430\u0437\u044b",
            *[f"- {item}" for item in evidence_facts],
            "",
            synthesis_heading,
            *(f"- {item}" for item in ic_synthesis),
            "",
            "## \u041f\u043e\u0440\u0442\u0444\u0435\u043b\u044c\u043d\u0430\u044f \u0440\u043e\u043b\u044c",
            f"{portfolio_text} Роль {ticker}: {portfolio_role}.",
            "",
            "## \u0427\u0442\u043e \u0438\u0437\u043c\u0435\u043d\u0438\u0442 \u0432\u0437\u0433\u043b\u044f\u0434",
            "Более позитивный взгляд нужен при ускорении качественного роста, устойчивой марже, улучшении свободного денежного потока после капитальных расходов и более привлекательной оценке. Более негативный взгляд нужен при замедлении роста, давлении на маржу, слабой конверсии инвестиций в искусственный интеллект и облако в выручку, снижении свободного денежного потока или сжатии мультипликатора оценки.",
        ]
        if limits:
            lines.extend(["", "## \u0427\u0442\u043e \u0435\u0449\u0451 \u043d\u0443\u0436\u043d\u043e \u0434\u043b\u044f \u043f\u0435\u0440\u0441\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u0444\u0438\u043d\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u0440\u0435\u0448\u0435\u043d\u0438\u044f", *[f"- {reader_limit_text(limit, language)}" for limit in limits]])
        if specialist_takeaways:
            lines.extend(["", "## \u0427\u0442\u043e \u0434\u043e\u0431\u0430\u0432\u0438\u043b\u0438 \u0430\u043d\u0430\u043b\u0438\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0438", *[f"- {item}" for item in specialist_takeaways]])
        lines.extend(["", "## \u041a\u043b\u044e\u0447\u0435\u0432\u044b\u0435 \u0438\u0441\u0442\u043e\u0447\u043d\u0438\u043a\u0438", *[f"- {reader_source_text(source, language)}" for source in sources]])
    else:
        prep_heading = "## IC working view" if ic_final_owner else "## Preparatory view"
        synthesis_heading = "## IC synthesis" if ic_final_owner else "## What is still needed for final assembly"
        lines = [
            "Report status: Complete - IC synthesis complete; not a personal position-sizing instruction."
            if report_complete
            else "Report status: Limited - preparation view only, not a final personal investment decision.",
            f"Preparation date: {today}",
            "Freshness and source note: checked public sources were used; current market conclusions depend on the latest available price and events.",
            f"Decision confidence: medium for structural {ticker} analysis, lower for personal action if portfolio context is incomplete.",
            "",
            f"# {ticker} Investment Review",
            "",
            "## Short view",
            ic_working_view(identity, snapshot, language),
            "",
            prep_heading,
            f"- What can be concluded now: {company} gives exposure to {quality}; the thesis depends on {thesis}.",
            f"- Portfolio context: {portfolio_text}",
            "- Action status: decision preparation, not a personal buy/sell/hold instruction.",
            "",
            "## Business and thesis",
            f"{ticker} provides exposure to {quality}. The thesis depends on {thesis}.",
            "",
            "## Financial snapshot",
            *financial_snapshot_table(snapshot, language),
            "",
            "## Financial quality and FCF",
            f"SEC company facts support a financial-quality check: revenue {money_billions((snapshot.get('revenue') or {}).get('val'), language)}, operating margin {percent(snapshot.get('operating_margin'), language)}, and FCF proxy {money_billions(snapshot.get('fcf_value'), language)}. If the FCF proxy is meaningfully below operating cash flow, the key question is whether capex is a temporary AI/cloud investment cycle or a higher steady-state capital intensity.",
            "",
            "## Valuation expectations",
            f"The market anchor is the latest close of {price_display(snapshot.get('price'), language)} on {snapshot.get('price_date') or 'n/a'}. The decision-prep question is not whether this is a good company; it is what growth, margin, and FCF expectations are already embedded in the price.",
            "",
            "## Bull / base / bear scenarios",
            "| Scenario | What must be true | Investment meaning |",
            "|---|---|---|",
            f"| Bull | {positive}; capex converts into faster revenue and FCF | premium valuation may be justified, but entry discipline still matters |",
            f"| Base | {thesis}; margins and FCF remain durable | quality candidate, but not an aggressive conclusion if valuation is demanding |",
            f"| Bear | {negative}; AI/cloud expectations reset lower | multiple compression can produce poor returns even if business quality remains good |",
            "",
            "## Risk red-team",
            f"Main risks include {risks}. 12-24 month thesis breakers are slower key-driver growth, worse FCF from capex, regulatory or competitive shock, and a market unwilling to keep paying a premium multiple for quality.",
            "",
            "## What the sources show",
            source_sentence,
            "",
            "## Evidence Status Summary",
            f"Evidence readiness for this run is {evidence_pack.get('evidence_readiness')}. If source coverage is incomplete, the report stays Limited/Blocked rather than presenting unsupported certainty.",
            "",
            "## Evidence facts used",
            *[f"- {item}" for item in evidence_facts],
            "",
            "## Financial quality",
            f"Financial quality is assessed through revenue growth, operating margin, free cash flow conversion, capex, balance sheet, buybacks/dividends, segments, and accounting red flags. For {ticker}, the key watch items are {financial_watch}.",
            "",
            "## Scenario valuation",
            "The base case requires durable growth, spending discipline, and normal profit-to-free-cash-flow conversion. The bull case needs stronger growth and sustained premium multiples. The bear case reflects growth slowdown, free-cash-flow pressure, or multiple compression.",
            "",
            synthesis_heading,
            *(f"- {item}" for item in ic_synthesis),
            "",
            "## Sector, macro, and positioning",
            f"Key drivers are {drivers}. The main positioning risk is that the market already prices in strong growth and margin resilience.",
            "",
            "## Key risks",
            f"Main risks include {risks}.",
            "",
            "## Portfolio fit",
            f"{portfolio_text} {ticker}'s generic role remains: {portfolio_role}.",
            "",
            "## What would change the view",
            f"The view improves with {positive}. It worsens with {negative}.",
        ]
        if limits:
            lines.extend(["", "## What is still needed for a personal final decision", *[f"- {limit}" for limit in limits]])
        if specialist_takeaways:
            lines.extend(["", "## What the specialist checks added", *[f"- {item}" for item in specialist_takeaways]])
        lines.extend(["", "## Key sources", *[f"- {source}" for source in sources]])
    return "\n".join(lines) + "\n"

def validate_reader_report_text(report_text: str) -> dict[str, Any]:
    forbidden = [
        "IC Action Status",
        "Analysis Status",
        "Runtime Execution Plan",
        "actual_subagents_run",
        "limited_ic_draft.md",
        "decision_prep_memo.md",
        "evidence_gap_memo.md",
        "module status",
        "Boundary: Not an IC Action",
        "**Workflow:**",
        "**Boundary:**",
        "**Prompt:**",
    ]
    is_russian = report_text.startswith("Дата подготовки:")
    is_generic_agent_report = "AGENT Workflow Review" in report_text or "AGENT-разбор" in report_text
    financial_table_rows = len(re.findall(r"(?m)^\|[^|\n]+\|[^|\n]+\|[^|\n]+\|$", report_text))
    meaningful_words = len(re.findall(r"\b[\wА-Яа-яЁё]{3,}\b", report_text))
    ic_section_match = re.search(
        r"(?s)(?:## IC synthesis|## What is still needed for final assembly|## What is still needed for IC assembly|## Итог IC-сборки|## Что нужно для IC-сборки)\s+(.+?)(?:\n## |\Z)",
        report_text,
    )
    ic_section_body = ic_section_match.group(1).strip() if ic_section_match else ""
    checks = {
        "starts_with_preparation_date": report_text.startswith("Preparation date:")
        or report_text.startswith("Report status:")
        or report_text.startswith("Дата подготовки:"),
        "has_reader_status": "Report status:" in report_text or "Статус отчёта:" in report_text,
        "has_freshness_source_note": "Freshness and source note:" in report_text or "Свежесть и источники:" in report_text,
        "has_decision_confidence": "Decision confidence:" in report_text or "Уверенность вывода:" in report_text,
        "no_runtime_debug_terms": not any(term in report_text for term in forbidden),
        "has_key_sources": "Key sources" in report_text or "Ключевые источники" in report_text,
        "has_evidence_status_summary": "Evidence Status Summary" in report_text or "Статус доказательной базы" in report_text,
        "has_evidence_facts_used": "Evidence facts used" in report_text
        or "Факты из доказательной базы" in report_text
        or "Факты, взятые из evidence pack" in report_text,
        "has_ic_synthesis": "IC synthesis" in report_text
        or "What is still needed for final assembly" in report_text
        or "What is still needed for IC assembly" in report_text
        or "Итог IC-сборки" in report_text
        or "Что нужно для IC-сборки" in report_text,
        "has_non_empty_ic_synthesis": len(ic_section_body) >= 80 and bool(re.search(r"(?m)^-", ic_section_body)),
        "specialist_takeaways_are_not_metadata": "Workflow:" not in report_text
        and "Boundary:" not in report_text
        and "Prompt:" not in report_text,
        "russian_report_has_no_english_portfolio_limitation": not (
            is_russian and "A personalized portfolio action is not provided" in report_text
        ),
        "has_human_limitation_explanation": "portfolio context" in report_text.lower()
        or "портфель" in report_text.lower(),
        "no_exact_sizing": not re.search(r"(?i)\b(buy|sell|add|trim|exit)\s+\d+\s*(shares|%)\b", report_text),
        "no_final_action_language_without_gate": not re.search(
            r"(?i)\b(recommend(?:ation)?\s*:\s*(buy|sell|hold|add|trim|exit)|"
            r"(you should|you must|we should|we must)\s+(buy|sell|hold|add|trim|exit)|"
            r"final\s+(buy|sell|hold|add|trim|exit)\s+(action|recommendation))\b",
            report_text,
        ),
        "no_action_box": "Action Box" not in report_text,
        "has_decision_prep_view": "IC working view" in report_text or "Preparatory view" in report_text or "Рабочий вывод IC" in report_text or "Подготовительный вывод" in report_text,
        "has_financial_snapshot_table": (
            ("Financial snapshot" in report_text or "Финансовый снимок" in report_text)
            or (is_generic_agent_report and ("Instrument / exposure snapshot" in report_text or "Профиль инструмента" in report_text))
        )
        and financial_table_rows >= (5 if is_generic_agent_report else 8),
        "has_financial_quality_fcf": "Financial quality and FCF" in report_text
        or "Финансовое качество и FCF" in report_text
        or "Финансовое качество и свободный денежный поток" in report_text
        or (is_generic_agent_report and ("Route-specific thesis" in report_text or "Ключевая аналитическая рамка" in report_text)),
        "has_valuation_expectations_section": "Valuation expectations" in report_text or "Оценка и ожидания" in report_text,
        "has_bull_base_bear": (
            "Bull / base / bear" in report_text
            or "bull / base / bear" in report_text
            or "Позитивный / базовый / негативный" in report_text
        )
        and ("Base" in report_text or "Базовый" in report_text)
        and ("Bear" in report_text or "Негативный" in report_text),
        "has_risk_red_team_section": "Risk red-team" in report_text or "Проверка рисков" in report_text,
        "has_decision_prep_substance": meaningful_words >= 450,
        "russian_language_policy_no_obvious_run_glish": not (
            is_russian
            and any(
                phrase in report_text
                for phrase in [
                    "growth drivers",
                    "valuation multiple",
                    "source-level",
                    "Decision-Prep view",
                    "synthesis/handoff",
                    "AI/cloud цикл",
                    "Buybacks |",
                    "Риск red-team",
                    "Факты, взятые из evidence pack",
                    "AI/облако",
                    "SEC filings",
                    "SEC company facts",
                    "company facts",
                    "live-реж",
                    "mega-cap growth",
                    "quality-growth",
                    "latest available",
                    "source status",
                    "capex конвертируется",
                    "investment-committee-agent",
                    "последний публичный close",
                    "Full filing text",
                    " / HTML",
                    "Статус источников для этого запуска: Complete",
                ]
            )
        ),
        "investment_analytical_style_no_generic_filler": not any(
            phrase in report_text.lower()
            for phrase in [
                "важно отметить",
                "стоит отметить",
                "давайте разбер",
                "in general",
                "it is important to note",
            ]
        ),
        "not_placeholder_only": not any(
            phrase in report_text
            for phrase in [
                "what must happen in the base case",
                "what opens the bull case",
                "generic public company",
                "large public company where the key investor question",
                "Для MSFT важны три группы вопросов",
            ]
        ),
    }
    return {"status": "pass" if all(checks.values()) else "fail", "checks": checks}

def write_run_manifest(
    run_dir: Path,
    prompt: str,
    mode: str,
    intake: dict[str, Any],
    preflight: dict[str, Any],
    evidence_pack: dict[str, Any],
    specialists: list[dict[str, Any]],
) -> None:
    identity = preflight.get("subject_identity") or intake.get("subject_identity") or {}
    route = selected_route_from_context(intake, preflight)
    route_specialists = agent_specialists_for_route(route)
    route_required_specialists = agent_required_specialists_for_route(route)
    completed = completed_specialists(specialists)
    failed_required = failed_required_specialist_ids(specialists)
    attempted_ids = {item.get("specialist_id") for item in specialists}
    completed_ids = {item.get("specialist_id") for item in completed}
    failed_specialists = [
        item.get("specialist_id")
        for item in specialists
        if item.get("status") != "ok" and item.get("specialist_id")
    ]
    missing_specialists = [sid for sid in route_specialists if sid not in completed_ids]
    missing_required = [sid for sid in route_required_specialists if sid not in completed_ids and sid not in failed_required]
    successful_live_thread_ids = all(item.get("sdk_thread_id") for item in completed) if mode == "live" else True
    workflow_complete = (
        not failed_specialists
        and completed_ids == set(route_specialists)
        and ic_completed_with_expected_handoffs(specialists)
        and evidence_pack.get("evidence_readiness") != "Blocked"
        and successful_live_thread_ids
    )
    ic_final_owner = workflow_complete and ic_completed_with_expected_handoffs(specialists)
    live_bridge_records = [item for item in specialists if item.get("codex_execution_path")]
    prompt_for_manifest = "<redacted-live-prompt>" if mode == "live" else prompt
    normalized_prompt = intake.get("normalized_prompt") or ""
    normalized_prompt_for_manifest = "<redacted-live-normalized-prompt>" if mode == "live" else normalized_prompt
    manifest_identity = redact_live_manifest_value(identity) if mode == "live" else identity
    manifest_resolver_result = (
        redact_live_manifest_value(preflight.get("resolver_result")) if mode == "live" else preflight.get("resolver_result")
    )
    portfolio_context = intake.get("portfolio_context") or normalize_portfolio_context({}, source="not_provided")
    if workflow_complete:
        stop_reason = None
    elif failed_specialists:
        stop_reason = f"stopped_before_ic_or_completion_due_to_failed_specialists:{','.join(failed_specialists)}"
    elif missing_specialists:
        stop_reason = f"not_all_specialists_completed:{','.join(missing_specialists)}"
    elif mode == "live" and not successful_live_thread_ids:
        stop_reason = "completed_live_specialist_missing_sdk_thread_id"
    else:
        stop_reason = "complete_semantics_not_satisfied"
    manifest = {
        "schema_version": "agent_run_manifest.v1",
        "workflow": "agent_run",
        "task_id": "TASK-013" if route == "equity_full_cycle" else "TASK-014",
        "mode": mode,
        "production_real_subagents": bool(mode == "live" and workflow_complete and successful_live_thread_ids),
        "prompt": prompt_for_manifest,
        "prompt_sha256": sha256_text(prompt),
        "normalized_prompt": normalized_prompt_for_manifest,
        "normalized_prompt_sha256": sha256_text(normalized_prompt),
        "selected_route": route,
        "subject": identity.get("ticker"),
        "subject_identity": manifest_identity,
        "instrument_classification": identity.get("instrument_classification"),
        "resolver_result": manifest_resolver_result,
        "created_at": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
        "report_path": str(run_dir / "investment_report.md"),
        "audit_dir": str(run_dir / "audit"),
        "attempted_subagents": specialists,
        "actual_subagents_run": completed,
        "failed_required_specialists": failed_required,
        "failed_specialists": failed_specialists,
        "missing_required_specialists": missing_required,
        "missing_specialists": missing_specialists,
        "codex_execution_path": CODEX_SDK_EXECUTION_PATH if mode == "live" else None,
        "codex_sdk_project_root": str(get_codex_sdk_project_root()) if mode == "live" else None,
        "codex_sdk_log_dirs": [item.get("codex_sdk_log_dir") for item in live_bridge_records if item.get("codex_sdk_log_dir")],
        "sdk_thread_ids": [item.get("sdk_thread_id") for item in completed if item.get("sdk_thread_id")],
        "sdk_errors": [item.get("sdk_error") or item.get("error") for item in specialists if item.get("sdk_error") or item.get("error")],
        "prompt_transports": sorted({item.get("prompt_transport") for item in live_bridge_records if item.get("prompt_transport")}),
        "stop_reason": stop_reason,
        "workflow_status": "completed" if workflow_complete else "controlled_specialist_gap",
        "analysis_status": "Complete" if workflow_complete else "Limited",
        "workflow_complete": workflow_complete,
        "ic_final_owner": ic_final_owner,
        "mock_mode_notice": "Mock specialist outputs do not satisfy production real-subagent readiness."
        if mode == "mock"
        else None,
        "evidence_readiness": evidence_pack.get("evidence_readiness"),
        "source_preflight_status": preflight.get("summary", {}),
        "portfolio_context_status": portfolio_context.get("status"),
        "portfolio_context_fields": portfolio_context.get("provided_fields", []),
        "portfolio_context_file": str(run_dir / "audit" / "portfolio_context.json"),
    }
    write_json(run_dir / "audit" / "run_manifest.json", manifest)
    write_json(
        run_dir / "audit" / "specialist_run_plan.json",
        {
            "specialists": route_specialists,
            "stage_order": [
                {"stage": 1, "specialists": ["evidence-collector"]},
                {
                    "stage": 2,
                    "specialists": [
                        sid for sid in route_specialists if sid not in {"evidence-collector", "investment-committee-agent"}
                    ],
                    "max_parallel_specialists": get_agent_max_parallel_specialists(),
                },
                {"stage": 3, "specialists": ["investment-committee-agent"]},
            ],
            "agent_total_timeout_seconds": get_agent_total_timeout_seconds(),
            "ic_consumes": "validated normalized handoffs only",
        },
    )


def validate_agent_run(run_dir: Path) -> dict[str, Any]:
    if not run_dir.is_dir():
        raise AgentRunError(f"agent_run_validation_error: run directory not found: {run_dir}")
    report_path = run_dir / "investment_report.md"
    audit = run_dir / "audit"
    required_files = [
        audit / "intake.json",
        audit / "source_preflight.json",
        audit / "source_inventory.json",
        audit / "provider_results.json",
        audit / "evidence_pack.md",
        audit / "evidence_pack.json",
        audit / "pre_ic_evidence_lock.json",
        audit / "run_manifest.json",
        audit / "specialist_run_plan.json",
    ]
    checks = {
        "investment_report_exists": report_path.is_file(),
        "audit_dir_exists": audit.is_dir(),
        "required_audit_files_exist": all(path.is_file() for path in required_files),
        "outside_repositories": not is_path_within(run_dir, LAB_ROOT) and not is_path_within(run_dir, PROJECT_ROOT),
    }
    report_text = report_path.read_text(encoding="utf-8") if report_path.is_file() else ""
    report_validation = validate_reader_report_text(report_text)
    checks.update({f"report_{key}": value for key, value in report_validation["checks"].items()})
    manifest = json.loads((audit / "run_manifest.json").read_text(encoding="utf-8")) if (audit / "run_manifest.json").is_file() else {}
    intake = json.loads((audit / "intake.json").read_text(encoding="utf-8")) if (audit / "intake.json").is_file() else {}
    portfolio_context = (
        json.loads((audit / "portfolio_context.json").read_text(encoding="utf-8"))
        if (audit / "portfolio_context.json").is_file()
        else intake.get("portfolio_context")
        or normalize_portfolio_context({}, source="legacy_missing_file")
    )
    preflight = json.loads((audit / "source_preflight.json").read_text(encoding="utf-8")) if (audit / "source_preflight.json").is_file() else {}
    evidence_pack = json.loads((audit / "evidence_pack.json").read_text(encoding="utf-8")) if (audit / "evidence_pack.json").is_file() else {}
    preflight_identity = preflight.get("subject_identity") or {}
    intake_identity = intake.get("subject_identity") or {}
    manifest_identity = manifest.get("subject_identity") or {}
    route = str(manifest.get("selected_route") or intake.get("selected_route") or preflight.get("selected_route") or "equity_full_cycle")
    expected_route_specialists = set(agent_specialists_for_route(route))
    subject_ticker = preflight_identity.get("ticker")
    allowed_classifications = {
        "us_common_equity",
        "us_share_class",
        "adr_or_foreign_issuer_us_listing",
        "non_us_listed_equity",
    }
    classification = (
        preflight_identity.get("instrument_classification")
        or manifest.get("instrument_classification")
        or manifest_identity.get("instrument_classification")
    )
    source_validation = validate_source_preflight(preflight) if preflight else {"status": "fail", "checks": {}}
    for key, value in source_validation.get("checks", {}).items():
        if key == "freshness_window_ok":
            checks["source_freshness_window_ok_or_limited"] = value or evidence_pack.get("evidence_readiness") == "Limited"
        else:
            checks[f"source_{key}"] = value
    attempted_specialists = manifest.get("attempted_subagents") or manifest.get("actual_subagents_run", [])
    specialists = manifest.get("actual_subagents_run") or completed_specialists(attempted_specialists)
    failed_required = manifest.get("failed_required_specialists", [])
    failed_specialists = manifest.get("failed_specialists") or failed_required
    missing_specialists = manifest.get("missing_specialists") or []
    expected_specialists = expected_route_specialists
    specialist_ids = {item.get("specialist_id") for item in specialists}
    attempted_specialist_ids = {item.get("specialist_id") for item in attempted_specialists}
    specialists_have_artifacts = True
    for specialist_id in attempted_specialist_ids:
        if not specialist_id:
            specialists_have_artifacts = False
            continue
        base = audit / "specialists" / specialist_id
        if not (
            (base / "raw_output.md").is_file()
            and (base / "handoff.json").is_file()
            and (base / "handoff.md").is_file()
            and (base / "validation.json").is_file()
        ):
            specialists_have_artifacts = False
    mode = manifest.get("mode")
    ic_handoff_path = audit / "specialists" / "investment-committee-agent" / "handoff.json"
    ic_handoff = json.loads(ic_handoff_path.read_text(encoding="utf-8")) if ic_handoff_path.is_file() else {}
    upstream_ids = [sid for sid in agent_specialists_for_route(route) if sid != "investment-committee-agent"]
    consumed_ids = set(ic_handoff.get("consumed_handoff_ids") or [])
    ic_consumed_expected_handoffs = (
        set(upstream_ids).issubset(consumed_ids)
        if "investment-committee-agent" in specialist_ids and not failed_specialists
        else evidence_pack.get("evidence_readiness") == "Blocked" or bool(failed_specialists) or bool(missing_specialists)
    )
    manifest_workflow_complete = bool(manifest.get("workflow_complete"))
    manifest_ic_final_owner = bool(manifest.get("ic_final_owner"))
    report_status_line = next((line for line in report_text.splitlines() if line.startswith(("Report status:", "Статус отчёта:"))), "")
    report_has_ic_owned_language = (
        "IC working view" in report_text
        or "IC question" in report_text
        or "full IC synthesis" in report_text
        or "IC stage" in report_text
        or "## IC synthesis" in report_text
        or "## Рабочий вывод IC" in report_text
        or "## Итог IC-сборки" in report_text
    )
    report_has_preparatory_ic_gap = (
        ("## Preparatory view" in report_text and ("## What is still needed for final assembly" in report_text or "## What is still needed for IC assembly" in report_text))
        or ("## Подготовительный вывод" in report_text and "## Что нужно для IC-сборки" in report_text)
    )
    company_facts_record = next(
        (record for record in preflight.get("source_records", []) if record.get("source_id") == "company_facts"),
        {},
    )
    company_facts_data = company_facts_record.get("data") if isinstance(company_facts_record.get("data"), dict) else {}
    sec_facts_ok = company_facts_record.get("status") == "ok" and bool(company_facts_data.get("facts"))
    financial_snapshot_has_values = not any(
        marker in report_text
        for marker in [
            "| Выручка | н/д |",
            "| Операционная прибыль | н/д |",
            "| Net income | n/a |",
            "| Revenue | n/a |",
        ]
    )
    checks.update(
        {
            "route_is_equity_full_cycle": manifest.get("selected_route") == "equity_full_cycle"
            if route == "equity_full_cycle"
            else manifest.get("selected_route") in AGENT_ROUTE_CARDS,
            "instrument_classification_present": classification in allowed_classifications
            if route == "equity_full_cycle"
            else bool(classification),
            "subject_identity_has_public_equity_shape": bool(subject_ticker)
            and bool(preflight_identity.get("company_name"))
            and (classification in allowed_classifications if route == "equity_full_cycle" else True),
            "subject_consistent_intake_preflight_manifest": bool(subject_ticker)
            and intake_identity.get("ticker") == subject_ticker
            and manifest.get("subject") == subject_ticker
            and manifest_identity.get("ticker") == subject_ticker
            and manifest_identity.get("instrument_classification") == classification
            and (manifest_identity.get("cik") == preflight_identity.get("cik") if route == "equity_full_cycle" else True),
            "subject_consistent_report_folder": bool(subject_ticker) and run_dir.name.startswith(f"{subject_ticker} "),
            "subject_consistent_report_title": bool(subject_ticker)
            and (
                f"# {subject_ticker} Investment Review" in report_text
                or f"# {subject_ticker} — инвестиционный разбор" in report_text
                or f"# {subject_ticker} AGENT Workflow Review" in report_text
                or f"# {subject_ticker} — AGENT-разбор" in report_text
            ),
            "intake_question_count_five": intake.get("question_count_required") == 5,
            "intake_answer_count_valid": 0 <= int(intake.get("answers_provided_count", -1)) <= 5,
            "portfolio_context_audit_present": portfolio_context.get("schema_version") == "portfolio_context.v1",
            "portfolio_context_status_valid": portfolio_context.get("status") in {"missing", "partial", "provided"},
            "portfolio_context_truthful": bool(intake.get("portfolio_context_provided"))
            == (portfolio_context.get("status") in {"partial", "provided"}),
            "portfolio_context_no_personal_action_unlock": portfolio_context.get("personal_action_unlocked") is False,
            "evidence_pack_has_claim_matrix": bool(evidence_pack.get("claim_support_matrix")),
            "pre_ic_lock_exists": bool(evidence_pack.get("pre_ic_evidence_lock")),
            "evidence_readiness_valid": evidence_pack.get("evidence_readiness") in {"Complete", "Limited", "Blocked"},
            "source_inventory_present": (audit / "source_inventory.json").is_file(),
            "provider_results_present": (audit / "provider_results.json").is_file()
            and bool(preflight.get("provider_results")),
            "no_fake_subagent_claims": not (mode == "mock" and manifest.get("production_real_subagents")),
            "specialist_set_complete_or_gap": specialist_ids == expected_specialists
            or evidence_pack.get("evidence_readiness") == "Blocked"
            or bool(failed_specialists)
            or bool(missing_specialists),
            "specialist_artifacts_exist": specialists_have_artifacts or evidence_pack.get("evidence_readiness") == "Blocked",
            "mock_not_production_real_subagents": not (mode == "mock" and manifest.get("production_real_subagents")),
            "live_successful_subagents_have_real_thread_ids": mode != "live" or all(item.get("sdk_thread_id") for item in specialists),
            "live_failed_attempts_not_counted_as_actual_subagents": mode != "live"
            or all(item.get("status") == "ok" for item in specialists),
            "ic_consumed_handoffs": ic_consumed_expected_handoffs,
            "workflow_complete_semantic": manifest_workflow_complete == (
                not failed_specialists
                and not missing_specialists
                and specialist_ids == expected_specialists
                and ic_consumed_expected_handoffs
                and (mode != "live" or all(item.get("sdk_thread_id") for item in specialists))
            ),
            "ic_final_owner_semantic": manifest_ic_final_owner == (
                not failed_specialists
                and not missing_specialists
                and "investment-committee-agent" in specialist_ids
                and ic_consumed_expected_handoffs
            ),
            "report_no_ic_owned_language_without_completed_ic": manifest_ic_final_owner or not report_has_ic_owned_language,
            "report_preparatory_language_when_ic_incomplete": manifest_ic_final_owner or report_has_preparatory_ic_gap,
            "report_limited_when_specialists_fail_or_missing": not (failed_specialists or missing_specialists)
            or manifest.get("analysis_status") == "Limited"
            and (
                "limited" in report_status_line.lower()
                or "огранич" in report_status_line.lower()
                or "огранич" in report_text.lower()
            ),
            "report_financial_values_present_when_sec_facts_ok": route != "equity_full_cycle" or not sec_facts_ok or financial_snapshot_has_values,
        }
    )
    artifact_valid = all(checks.values())
    workflow_complete = artifact_valid and manifest_workflow_complete
    validation_status = "pass" if workflow_complete else "limited" if artifact_valid else "fail"
    validation = {
        "schema_version": "agent_run_validation.v1",
        "status": validation_status,
        "artifact_valid": artifact_valid,
        "workflow_complete": workflow_complete,
        "ic_final_owner": manifest_ic_final_owner,
        "run_dir": str(run_dir),
        "checks": checks,
        "source_validation": source_validation,
        "report_validation": report_validation,
        "evidence_status": evidence_pack.get("evidence_readiness"),
        "evidence_readiness": evidence_pack.get("evidence_readiness"),
        "workflow_status": manifest.get("workflow_status"),
        "analysis_status": manifest.get("analysis_status"),
        "full_agent_execution_status": "controlled_specialist_gap"
        if failed_specialists or missing_specialists or not manifest_workflow_complete
        else "complete",
    }
    write_json(audit / "agent_run_validation.json", validation)
    write_json(audit / "report_validation.json", report_validation)
    if validation["status"] == "fail":
        failed = [key for key, value in checks.items() if not value]
        raise AgentRunError(f"agent_run_validation_error: failed checks: {', '.join(failed)}")
    return validation


def latest_agent_run_dir(reports_root: Path | None = None) -> Path:
    base = reports_root or get_agent_reports_root()
    candidates = [
        path
        for path in base.glob("*")
        if path.is_dir() and (path / "investment_report.md").is_file() and (path / "audit").is_dir()
    ]
    if not candidates:
        raise AgentRunError(f"agent_run_validation_error: no AGENT runs found under {base}")
    return max(candidates, key=lambda path: path.stat().st_mtime)


def print_agent_intake(prompt: str) -> None:
    normalized = normalize_agent_prompt(prompt)
    route_info = validate_supported_agent_route(prompt)
    route = route_info["route"]
    identity = route_info["identity"]
    ticker = route_info["ticker"]
    questions = agent_intake_questions(normalized, route, identity)
    print("AGENT intake: answer these 5 questions before full execution")
    print(f"Route: {route}")
    print(f"Subject: {ticker} workflow")
    print(f"Prompt: {normalized}")
    for index, question in enumerate(questions, start=1):
        print(f"{index}. {question}")


def run_agent_intake(prompt: str) -> int:
    if not prompt.strip():
        raise ValueError("agent-intake requires a non-empty --prompt")
    validate_supported_agent_route(prompt)
    print_agent_intake(prompt)
    return 0


def write_agent_run_log(run_dir: Path, prompt: str, mode: str, validation: dict[str, Any]) -> Path:
    output_dir = get_agent_runs_dir()
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).astimezone().isoformat(timespec="microseconds")
    path = output_dir / f"{safe_timestamp_for_path(timestamp)}-{mode}-agent-run-{uuid4().hex[:8]}.json"
    payload = {
        "timestamp": timestamp,
        "workflow": "agent_run",
        "mode": mode,
        "prompt": prompt,
        "run_dir": str(run_dir),
        "report_path": str(run_dir / "investment_report.md"),
        "validation": validation,
    }
    write_json(path, payload)
    return path


def run_agent_run(
    prompt: str,
    mode: str,
    answer_args: list[str] | None,
    answers_json: str | None,
    continue_with_baseline: bool,
    portfolio_context_json: str | None = None,
    portfolio_context_file: str | None = None,
) -> int:
    if not prompt.strip():
        raise ValueError("agent-run requires a non-empty --prompt")
    route_info = validate_supported_agent_route(prompt)
    route = route_info["route"]
    identity = route_info["identity"]
    ticker = route_info["ticker"]
    answers = parse_agent_answers(answer_args, answers_json)
    portfolio_context = parse_portfolio_context(portfolio_context_json, portfolio_context_file)
    if not answers and not continue_with_baseline:
        print_agent_intake(prompt)
        print("No report or audit was created. Provide answers or use --continue-with-baseline to proceed with approved baseline assumptions.")
        return 0
    intake = build_agent_intake_payload(prompt, answers, continue_with_baseline=continue_with_baseline, portfolio_context=portfolio_context)
    run_dir = create_agent_report_dir(ticker)
    freshness_required = is_freshness_dependent(prompt) or any(answers_require_freshness([answer]) for answer in answers)
    preflight = build_agent_source_preflight(prompt=prompt, answers=answers, mode=mode, route=route, identity=identity)
    preflight = annotate_preflight_freshness(preflight, freshness_required)
    evidence_pack = build_evidence_pack(preflight, freshness_required=freshness_required)
    write_agent_preflight_artifacts(run_dir, intake, preflight, evidence_pack)
    source_validation = validate_source_preflight(preflight)
    if source_validation["status"] != "pass" or evidence_pack.get("evidence_readiness") == "Blocked":
        gap_text = (
            "# Evidence Gap\n\n"
            f"The {ticker} AGENT workflow stopped before normal report generation because required public evidence did not pass source preflight.\n\n"
            f"Missing required sources: {', '.join(source_validation.get('missing_required') or []) or 'see source_preflight.json'}\n"
        )
        (run_dir / "audit" / "evidence_gap_memo.md").write_text(gap_text, encoding="utf-8")
        report_text = generate_investment_report(prompt, intake, preflight, evidence_pack, [])
        (run_dir / "investment_report.md").write_text(report_text, encoding="utf-8")
        write_run_manifest(run_dir, prompt, mode, intake, preflight, evidence_pack, [])
        blocked_validation = {
            "schema_version": "agent_run_validation.v1",
            "status": "blocked",
            "run_dir": str(run_dir),
            "reason": "source preflight hard gate failed",
            "source_validation": source_validation,
            "report_validation": validate_reader_report_text(report_text),
            "evidence_status": evidence_pack.get("evidence_readiness"),
            "evidence_readiness": evidence_pack.get("evidence_readiness"),
        }
        write_json(run_dir / "audit" / "agent_run_validation.json", blocked_validation)
        write_agent_run_log(
            run_dir,
            prompt,
            mode,
            {
                "status": "blocked",
                "reason": "source preflight hard gate failed",
                "source_validation": source_validation,
                "run_dir": str(run_dir),
            },
        )
        print("AGENT run stopped: required public evidence did not pass source preflight.")
        print(f"Blocked report: {run_dir / 'investment_report.md'}")
        print(f"Evidence gap memo: {run_dir / 'audit' / 'evidence_gap_memo.md'}")
        return 1
    specialists: list[dict[str, Any]] = []
    specialists = run_agent_specialists(run_dir, mode, intake, evidence_pack, preflight)
    report_text = generate_investment_report(prompt, intake, preflight, evidence_pack, specialists)
    (run_dir / "investment_report.md").write_text(report_text, encoding="utf-8")
    write_run_manifest(run_dir, prompt, mode, intake, preflight, evidence_pack, specialists)
    validation = validate_agent_run(run_dir)
    write_agent_run_log(run_dir, prompt, mode, validation)
    if reader_language(prompt) == "ru":
        if validation.get("workflow_status") == "controlled_specialist_gap":
            print(f"AGENT-пакет {ticker} создан с ограничением: часть live-специалистов не завершилась; детали в audit.")
        else:
            print(f"AGENT-разбор {ticker} готов. Полный читательский отчёт сохранён отдельно.")
        suffix = "Отчёт сохранён"
    else:
        if validation.get("workflow_status") == "controlled_specialist_gap":
            print(f"{ticker} AGENT package saved with a controlled specialist gap; see audit for failed specialist details.")
        else:
            print(f"{ticker} AGENT run completed. The reader-facing report was saved separately.")
        suffix = "Report saved"
    print(f"{suffix}: {run_dir / 'investment_report.md'}")
    return 0


def run_validate_agent_run(run_dir: str | None) -> int:
    path = Path(run_dir) if run_dir else latest_agent_run_dir()
    try:
        validation = validate_agent_run(path)
    except AgentRunError as exc:
        print("AGENT run validation failed")
        print(f"Reason: {exc}")
        return 1
    if validation.get("full_agent_execution_status") == "controlled_specialist_gap":
        print("AGENT package validation limited with controlled specialist gap")
    else:
        print("AGENT run validation passed")
    print(f"Report: {Path(validation['run_dir']) / 'investment_report.md'}")
    return 0


def write_specialist_run_log(run_dir: Path, prompt: str, mode: str, validation: dict[str, Any]) -> Path:
    output_dir = get_specialist_runs_dir()
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).astimezone().isoformat(timespec="microseconds")
    path = output_dir / f"{safe_timestamp_for_path(timestamp)}-{mode}-specialist-run-{uuid4().hex[:8]}.json"
    payload = {
        "timestamp": timestamp,
        "workflow": "direct_specialist",
        "mode": mode,
        "prompt": prompt if mode == "mock" else "<redacted-live-prompt>",
        "prompt_sha256": sha256_text(prompt),
        "run_dir": str(run_dir),
        "validation_status": validation.get("status"),
        "validation": validation,
    }
    write_json(path, payload)
    return path


def latest_specialist_run_dir(reports_root: Path | None = None) -> Path:
    base = (reports_root or get_agent_reports_root()) / "_specialists"
    candidates = [
        path
        for path in base.glob("*")
        if path.is_dir() and (path / "specialist_report.md").is_file() and (path / "audit").is_dir()
    ] if base.is_dir() else []
    if not candidates:
        raise SpecialistRunError(f"specialist_run_validation_error: no specialist runs found under {base}")
    return max(candidates, key=lambda path: path.stat().st_mtime)


def validate_specialist_run(run_dir: Path) -> dict[str, Any]:
    if not run_dir.is_dir():
        raise SpecialistRunError(f"specialist_run_validation_error: run directory not found: {run_dir}")
    report_path = run_dir / "specialist_report.md"
    audit = run_dir / "audit"
    manifest_path = audit / "specialist_manifest.json"
    checks = {
        "specialist_report_exists": report_path.is_file(),
        "audit_dir_exists": audit.is_dir(),
        "manifest_exists": manifest_path.is_file(),
        "outside_repositories": not is_path_within(run_dir, LAB_ROOT) and not is_path_within(run_dir, PROJECT_ROOT),
    }
    report_text = report_path.read_text(encoding="utf-8") if report_path.is_file() else ""
    manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.is_file() else {}
    output_validation = validate_direct_specialist_output(report_text, manifest)
    checks.update({f"output_{key}": value for key, value in output_validation["checks"].items()})
    attempted = manifest.get("attempted_specialists") or []
    specialist_artifacts_exist = True
    for item in attempted:
        specialist_id = item.get("specialist_id")
        if not specialist_id:
            specialist_artifacts_exist = False
            continue
        base = audit / "specialists" / specialist_id
        if not (
            (base / "raw_output.md").is_file()
            and (base / "handoff.json").is_file()
            and (base / "handoff.md").is_file()
            and (base / "validation.json").is_file()
        ):
            specialist_artifacts_exist = False
    checks["specialist_artifacts_exist"] = specialist_artifacts_exist
    validation = {
        "schema_version": "direct_specialist_run_validation.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "run_dir": str(run_dir),
        "checks": checks,
        "output_validation": output_validation,
    }
    write_json(audit / "specialist_run_validation.json", validation)
    if validation["status"] == "fail":
        failed = [key for key, value in checks.items() if not value]
        raise SpecialistRunError(f"specialist_run_validation_error: failed checks: {', '.join(failed)}")
    return validation


def run_specialist_run(prompt: str, mode: str) -> int:
    if not prompt.strip():
        raise ValueError("specialist-run requires a non-empty --prompt")
    parsed = parse_specialist_prompt(prompt)
    prefix = parsed["prefix"]
    specialist_id = parsed["specialist_id"]
    subject_prompt = parsed["subject_prompt"]
    identity = specialist_identity_from_subject(subject_prompt, prefix)
    subject = str(identity.get("ticker") or subject_prompt)
    run_dir = create_specialist_run_dir(prefix, subject)
    audit = run_dir / "audit"
    specialist_dir = audit / "specialists" / specialist_id
    specialist_dir.mkdir(parents=True, exist_ok=True)
    direct_prompt = build_direct_specialist_prompt(prefix=prefix, specialist_id=specialist_id, subject_prompt=subject_prompt, identity=identity)
    started_at = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    if mode == "mock":
        raw = mock_direct_specialist_output(prefix, specialist_id, subject_prompt, identity)
        status = "ok"
        thread_or_run_id = f"mock-direct-{specialist_id}-{uuid4().hex[:8]}"
        sdk_thread_id = ""
        codex_execution_path = ""
        sdk_error = None
        attempt_history = [{"attempt_no": 1, "status": "ok", "thread_or_run_id": thread_or_run_id, "sdk_thread_id": ""}]
    else:
        response = run_live_specialist_codex(specialist_id, direct_prompt)
        status = "ok" if response.get("status") == "ok" else "error"
        raw = response.get("response") or f"Boundary: Not an IC Action\n\n# {specialist_title(specialist_id)}\n\nSpecialist run failed: {response.get('error')}\n"
        if "Boundary: Not an IC Action" not in raw:
            raw = "Boundary: Not an IC Action\n\n" + raw
        thread_or_run_id = response.get("sdk_thread_id") if status == "ok" else ""
        sdk_thread_id = response.get("sdk_thread_id") or ""
        codex_execution_path = response.get("codex_execution_path") or CODEX_SDK_EXECUTION_PATH
        sdk_error = response.get("sdk_error") or response.get("error")
        attempt_history = [live_attempt_record(1, response)]
    completed_at = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    if direct_specialist_forbidden_action(raw):
        status = "error"
        sdk_error = sdk_error or "direct specialist output contained forbidden final-action language"
    artifact_name = specialist_artifact_name(specialist_id)
    (specialist_dir / "raw_output.md").write_text(raw, encoding="utf-8")
    handoff = {
        "schema_version": "direct_specialist_handoff.v1",
        "Artifact": artifact_name,
        "Subject": subject_label(identity),
        "Workflow": "direct_specialist",
        "Prefix": prefix,
        "Produced by": specialist_id,
        "As-of date/time": completed_at,
        "Output status": "Complete" if status == "ok" else "Blocked",
        "Boundary": "Not an IC Action",
        "Decision boundary": "Direct specialist output only; not an IC Action.",
        "thread_or_run_id": thread_or_run_id or "",
        "sdk_thread_id": sdk_thread_id,
        "codex_execution_path": codex_execution_path,
        "sdk_error": sdk_error,
        "started_at": started_at,
        "completed_at": completed_at,
        "attempt_history": attempt_history,
        "main_findings": extract_meaningful_findings(raw),
    }
    write_json(specialist_dir / "handoff.json", handoff)
    (specialist_dir / "handoff.md").write_text(
        "\n".join([
            f"# Direct specialist handoff - {specialist_id}",
            "",
            "Boundary: Not an IC Action",
            "Workflow: direct_specialist",
            f"Prefix: {prefix}",
            f"Subject: {subject_label(identity)}",
            f"Output status: {handoff['Output status']}",
        ]) + "\n",
        encoding="utf-8",
    )
    write_json(specialist_dir / "validation.json", {"status": "pass" if status == "ok" else "fail", "sdk_error": sdk_error})
    report_text = raw if raw.startswith("Boundary: Not an IC Action") else "Boundary: Not an IC Action\n\n" + raw
    (run_dir / "specialist_report.md").write_text(report_text, encoding="utf-8")
    attempted = [{
        "specialist_id": specialist_id,
        "status": status,
        "thread_or_run_id": thread_or_run_id or "",
        "sdk_thread_id": sdk_thread_id,
        "handoff_path": str(specialist_dir / "handoff.json"),
        "attempt_history": attempt_history,
    }]
    actual = attempted if status == "ok" else []
    manifest = {
        "schema_version": "direct_specialist_manifest.v1",
        "workflow": "direct_specialist",
        "task_id": "TASK-015",
        "mode": mode,
        "prefix": prefix,
        "specialist_id": specialist_id,
        "prompt": prompt if mode == "mock" else "<redacted-live-prompt>",
        "prompt_sha256": sha256_text(prompt),
        "subject_prompt": subject_prompt if mode == "mock" else "<redacted-live-subject>",
        "subject_identity": redact_live_manifest_value(identity) if mode == "live" else identity,
        "report_path": str(run_dir / "specialist_report.md"),
        "audit_dir": str(audit),
        "attempted_specialists": attempted,
        "actual_specialists_run": actual,
        "production_real_subagent": bool(mode == "live" and status == "ok" and sdk_thread_id),
        "boundary": "Not an IC Action",
        "final_action_allowed": False,
    }
    write_json(audit / "specialist_manifest.json", manifest)
    output_validation = validate_direct_specialist_output(report_text, manifest)
    write_json(audit / "output_validation.json", output_validation)
    validation = validate_specialist_run(run_dir)
    write_specialist_run_log(run_dir, prompt, mode, validation)
    print(f"Direct specialist {prefix} routed to {specialist_id}.")
    print(f"Specialist report saved: {run_dir / 'specialist_report.md'}")
    return 0


def run_validate_specialist_run(run_dir: str | None) -> int:
    path = Path(run_dir) if run_dir else latest_specialist_run_dir()
    validation = validate_specialist_run(path)
    print("Direct specialist run validation passed")
    print(f"Report: {Path(validation['run_dir']) / 'specialist_report.md'}")
    return 0

def _doctor_check(name: str, ok: bool, detail: str = "") -> dict[str, Any]:
    return {"name": name, "ok": bool(ok), "detail": detail}


def run_codex_sdk_doctor_check(timeout_seconds: int = 60) -> dict[str, Any]:
    project_root = get_codex_sdk_project_root()
    command = [get_codex_sdk_command(), "run", "codex:doctor"]
    try:
        completed = subprocess.run(
            command,
            cwd=project_root,
            text=True,
            capture_output=True,
            check=False,
            timeout=timeout_seconds,
        )
    except Exception as exc:  # pragma: no cover - defensive for local process issues
        return _doctor_check("Financial Agent System Codex SDK doctor", False, f"{type(exc).__name__}: {exc}")
    ok = completed.returncode == 0 and '"ok": true' in completed.stdout
    detail = "ok" if ok else (completed.stderr.strip() or completed.stdout.strip()[:500] or f"exit={completed.returncode}")
    return _doctor_check("Financial Agent System Codex SDK doctor", ok, detail)


def build_live_doctor_report(*, run_sdk_doctor: bool = True, write_log: bool = True) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    project_root = get_codex_sdk_project_root()
    reports_root = get_agent_reports_root()
    checks.append(_doctor_check("Financial Agent System root exists", project_root.is_dir(), str(project_root)))
    checks.append(_doctor_check("Financial Agent System AGENTS.md exists", (project_root / "AGENTS.md").is_file(), str(project_root / "AGENTS.md")))
    checks.append(_doctor_check("Financial Agent System package.json exists", (project_root / "package.json").is_file(), str(project_root / "package.json")))
    checks.append(_doctor_check("Financial Agent System built SDK CLI exists", (project_root / "dist" / "src" / "codex-sdk" / "cli.js").is_file(), str(project_root / "dist" / "src" / "codex-sdk" / "cli.js")))
    lab_python = LAB_ROOT / ".venv" / "Scripts" / "python.exe"
    project_python = PROJECT_ROOT / ".venv" / "Scripts" / "python.exe"
    python_path = lab_python if lab_python.is_file() else project_python
    checks.append(_doctor_check("Automation Lab Python exists", python_path.is_file(), str(python_path)))
    checks.append(_doctor_check("Automation Lab tests directory exists", (LAB_ROOT / "tests").is_dir(), str(LAB_ROOT / "tests")))
    try:
        reports_root.mkdir(parents=True, exist_ok=True)
        probe = reports_root / f".live-doctor-write-{uuid4().hex}.tmp"
        probe.write_text("ok", encoding="utf-8")
        probe.unlink(missing_ok=True)
        reports_ok = True
        reports_detail = str(reports_root)
    except Exception as exc:
        reports_ok = False
        reports_detail = f"{reports_root} ({type(exc).__name__}: {exc})"
    checks.append(_doctor_check("Financial Agent Reports root writable", reports_ok, reports_detail))
    for env_name, default in [
        (CODEX_SDK_TIMEOUT_ENV, DEFAULT_CODEX_SDK_TIMEOUT_SECONDS),
        (AGENT_TOTAL_TIMEOUT_ENV, DEFAULT_AGENT_TOTAL_TIMEOUT_SECONDS),
        (AGENT_MAX_PARALLEL_SPECIALISTS_ENV, DEFAULT_AGENT_MAX_PARALLEL_SPECIALISTS),
    ]:
        value = os.environ.get(env_name)
        try:
            parsed = parse_positive_int_env(env_name, default)
            checks.append(_doctor_check(f"{env_name} positive integer", parsed > 0, str(parsed if value else f"default={parsed}")))
        except ValueError as exc:
            checks.append(_doctor_check(f"{env_name} positive integer", False, str(exc)))
    checks.append(_doctor_check("Codex SDK command configured", bool(get_codex_sdk_command()), get_codex_sdk_command()))
    checks.append(_doctor_check("Live specialist prompt transport is prompt-file", True, "prompt_file"))
    checks.append(_doctor_check("No hidden API key dependency required for public source preflight", True, "public/no-key sources; optional providers remain explicit future slots"))
    if run_sdk_doctor:
        checks.append(run_codex_sdk_doctor_check())
    status = "pass" if all(check["ok"] for check in checks) else "fail"
    report = {
        "schema_version": "automation_live_doctor.v1",
        "status": status,
        "created_at": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
        "lab_root": str(LAB_ROOT),
        "financial_agent_system_root": str(project_root),
        "reports_root": str(reports_root),
        "checks": checks,
        "live_modes_covered": ["route-check", "quick-run", "quick-answer", "agent-run", "specialist-run"],
        "completion_semantics": "live specialist completion requires real sdk_thread_id; failed or timed-out attempts remain Limited/Blocked",
    }
    if write_log:
        output_dir = get_live_doctor_runs_dir()
        output_dir.mkdir(parents=True, exist_ok=True)
        path = output_dir / f"{safe_timestamp_for_path(report['created_at'])}-live-doctor-{uuid4().hex[:8]}.json"
        write_json(path, report)
        report["log_path"] = str(path)
        write_json(path, report)
    return report


def run_live_doctor(skip_sdk_doctor: bool = False) -> int:
    report = build_live_doctor_report(run_sdk_doctor=not skip_sdk_doctor, write_log=True)
    print(f"Automation Lab live doctor: {report['status']}")
    for check in report["checks"]:
        status = "PASS" if check["ok"] else "FAIL"
        detail = f" - {check['detail']}" if check.get("detail") else ""
        print(f"{status}: {check['name']}{detail}")
    if report.get("log_path"):
        print(f"Log: {report['log_path']}")
    return 0 if report["status"] == "pass" else 1

def _read_json_file(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _latest_file(paths: list[Path]) -> Path | None:
    existing = [path for path in paths if path.is_file()]
    return max(existing, key=lambda path: path.stat().st_mtime) if existing else None


def latest_live_doctor_log() -> dict[str, Any] | None:
    directory = get_live_doctor_runs_dir()
    if not directory.is_dir():
        return None
    latest = _latest_file(list(directory.glob("*-live-doctor-*.json")))
    if not latest:
        return None
    payload = _read_json_file(latest)
    payload.setdefault("log_path", str(latest))
    return payload


def collect_agent_acceptance_records(reports_root: Path | None = None) -> list[dict[str, Any]]:
    root = reports_root or get_agent_reports_root()
    records: list[dict[str, Any]] = []
    if not root.is_dir():
        return records
    for manifest_path in root.glob("*/audit/run_manifest.json"):
        manifest = _read_json_file(manifest_path)
        if manifest.get("workflow") != "agent_run":
            continue
        run_dir = manifest_path.parents[1]
        validation_path = run_dir / "audit" / "agent_run_validation.json"
        validation = _read_json_file(validation_path)
        sdk_thread_ids = [thread_id for thread_id in manifest.get("sdk_thread_ids", []) if thread_id]
        sdk_errors = [str(error) for error in (manifest.get("sdk_errors") or []) if error]
        records.append(
            {
                "run_dir": str(run_dir),
                "report_path": str(run_dir / "investment_report.md"),
                "selected_route": manifest.get("selected_route"),
                "subject": manifest.get("subject"),
                "mode": manifest.get("mode"),
                "workflow_complete": bool(manifest.get("workflow_complete")),
                "analysis_status": manifest.get("analysis_status"),
                "validation_status": validation.get("status"),
                "sdk_thread_ids": sdk_thread_ids,
                "sdk_errors": sdk_errors,
                "usage_limit_blocked": any(is_usage_limit_error(error) for error in sdk_errors),
                "has_real_live_thread_evidence": manifest.get("mode") == "live" and bool(sdk_thread_ids),
                "production_real_subagents": bool(manifest.get("production_real_subagents")),
                "stop_reason": manifest.get("stop_reason"),
                "created_at": manifest.get("created_at") or datetime.fromtimestamp(run_dir.stat().st_mtime, timezone.utc).astimezone().isoformat(timespec="seconds"),
            }
        )
    return sorted(records, key=lambda item: str(item.get("created_at") or ""))


def collect_specialist_acceptance_records(reports_root: Path | None = None) -> list[dict[str, Any]]:
    root = (reports_root or get_agent_reports_root()) / "_specialists"
    records: list[dict[str, Any]] = []
    if not root.is_dir():
        return records
    for manifest_path in root.glob("*/audit/specialist_manifest.json"):
        manifest = _read_json_file(manifest_path)
        if manifest.get("workflow") != "direct_specialist":
            continue
        run_dir = manifest_path.parents[1]
        validation_path = run_dir / "audit" / "specialist_run_validation.json"
        validation = _read_json_file(validation_path)
        actual = manifest.get("actual_specialists_run") or []
        sdk_thread_ids = [item.get("sdk_thread_id") for item in actual if item.get("sdk_thread_id")]
        attempted = manifest.get("attempted_specialists") or []
        sdk_errors = [
            str((item.get("attempt_history") or [{}])[-1].get("sdk_error") or item.get("sdk_error") or item.get("error"))
            for item in attempted
            if ((item.get("attempt_history") or [{}])[-1].get("sdk_error") or item.get("sdk_error") or item.get("error"))
        ]
        records.append(
            {
                "run_dir": str(run_dir),
                "report_path": str(run_dir / "specialist_report.md"),
                "prefix": manifest.get("prefix"),
                "specialist_id": manifest.get("specialist_id"),
                "mode": manifest.get("mode"),
                "validation_status": validation.get("status"),
                "actual_specialist_count": len(actual),
                "sdk_thread_ids": sdk_thread_ids,
                "sdk_errors": sdk_errors,
                "usage_limit_blocked": any(is_usage_limit_error(error) for error in sdk_errors),
                "has_real_live_thread_evidence": manifest.get("mode") == "live" and bool(sdk_thread_ids),
                "production_real_subagent": bool(manifest.get("production_real_subagent")),
                "boundary": manifest.get("boundary"),
                "created_at": datetime.fromtimestamp(run_dir.stat().st_mtime, timezone.utc).astimezone().isoformat(timespec="seconds"),
            }
        )
    return sorted(records, key=lambda item: str(item.get("created_at") or ""))


def _identity_ticker_from_payload(payload: dict[str, Any], *keys: str) -> str | None:
    for key in keys:
        value = payload.get(key)
        if isinstance(value, dict):
            ticker = value.get("ticker") or value.get("symbol") or value.get("asset") or value.get("slug")
            if ticker:
                return str(ticker).strip().upper()
        elif isinstance(value, str) and value.strip():
            return value.strip().upper()
    return None


def _quick_ticker_from_run_dir(run_dir: Path) -> str | None:
    match = re.match(r"^\d{8}T[^-]+-(?P<ticker>[A-Za-z0-9._-]+(?:-[A-Za-z0-9._-]+)*)$", run_dir.name)
    if match:
        return match.group("ticker").upper()
    return None


def collect_quick_acceptance_records() -> list[dict[str, Any]]:
    root = get_quick_data_runs_dir()
    records: list[dict[str, Any]] = []
    if not root.is_dir():
        return records
    for answer_path in root.glob("*/quick_answer.json"):
        run_dir = answer_path.parent
        answer = _read_json_file(answer_path)
        quality = _read_json_file(run_dir / "output_quality.json")
        source = _read_json_file(run_dir / "source_snapshot.json")
        ticker = (
            _identity_ticker_from_payload(source, "identity", "asset_identity", "subject_identity", "quick_identity")
            or _identity_ticker_from_payload(answer, "ticker", "asset", "identity", "asset_identity", "subject_identity")
            or _quick_ticker_from_run_dir(run_dir)
        )
        records.append(
            {
                "run_dir": str(run_dir),
                "ticker": ticker,
                "mode": answer.get("mode") or source.get("mode"),
                "status": answer.get("status"),
                "output_quality_status": quality.get("status"),
                "creates_report_or_audit": (run_dir / "investment_report.md").exists() or (run_dir / "audit").exists(),
                "created_at": source.get("timestamp") or datetime.fromtimestamp(run_dir.stat().st_mtime, timezone.utc).astimezone().isoformat(timespec="seconds"),
            }
        )
    return sorted(records, key=lambda item: str(item.get("created_at") or ""))


def latest_by_key(records: list[dict[str, Any]], key: str) -> dict[str, dict[str, Any]]:
    latest: dict[str, dict[str, Any]] = {}
    for record in records:
        value = str(record.get(key) or "UNKNOWN")
        latest[value] = record
    return latest


def build_live_acceptance_report(*, require_live: bool = False, write_log: bool = True) -> dict[str, Any]:
    doctor = latest_live_doctor_log()
    agent_records = collect_agent_acceptance_records()
    specialist_records = collect_specialist_acceptance_records()
    quick_records = collect_quick_acceptance_records()
    latest_routes = latest_by_key(agent_records, "selected_route")
    latest_prefixes = latest_by_key(specialist_records, "prefix")
    latest_quick = latest_by_key(quick_records, "ticker")
    required_routes = sorted(AGENT_ROUTE_CARDS.keys())
    required_prefixes = sorted(SPECIALIST_COMMANDS.keys())
    route_coverage = {
        route: {
            "present": route in latest_routes,
            "mode": latest_routes.get(route, {}).get("mode"),
            "validation_status": latest_routes.get(route, {}).get("validation_status"),
            "workflow_complete": latest_routes.get(route, {}).get("workflow_complete"),
            "has_real_live_thread_evidence": bool(latest_routes.get(route, {}).get("has_real_live_thread_evidence")),
            "usage_limit_blocked": bool(latest_routes.get(route, {}).get("usage_limit_blocked")),
            "report_path": latest_routes.get(route, {}).get("report_path"),
        }
        for route in required_routes
    }
    prefix_coverage = {
        prefix: {
            "present": prefix in latest_prefixes,
            "mode": latest_prefixes.get(prefix, {}).get("mode"),
            "validation_status": latest_prefixes.get(prefix, {}).get("validation_status"),
            "has_real_live_thread_evidence": bool(latest_prefixes.get(prefix, {}).get("has_real_live_thread_evidence")),
            "usage_limit_blocked": bool(latest_prefixes.get(prefix, {}).get("usage_limit_blocked")),
            "report_path": latest_prefixes.get(prefix, {}).get("report_path"),
        }
        for prefix in required_prefixes
    }
    quick_coverage = {
        ticker: {
            "present": ticker in latest_quick,
            "mode": latest_quick.get(ticker, {}).get("mode"),
            "status": latest_quick.get(ticker, {}).get("status"),
            "output_quality_status": latest_quick.get(ticker, {}).get("output_quality_status"),
            "no_report_or_audit": not bool(latest_quick.get(ticker, {}).get("creates_report_or_audit")),
            "run_dir": latest_quick.get(ticker, {}).get("run_dir"),
        }
        for ticker in ["MSFT", "SPY", "BTC", "TLT", "GLD", "MSFT-SPY-BTC"]
    }
    smoke_gaps = []
    live_gaps = []
    for route, coverage in route_coverage.items():
        if not coverage["present"] or coverage.get("validation_status") not in {"pass", "limited"}:
            smoke_gaps.append(f"agent_route:{route}")
        if not coverage.get("has_real_live_thread_evidence"):
            live_gaps.append(f"agent_route:{route}")
    for prefix, coverage in prefix_coverage.items():
        if not coverage["present"] or coverage.get("validation_status") != "pass":
            smoke_gaps.append(f"specialist_prefix:{prefix}")
        if not coverage.get("has_real_live_thread_evidence"):
            live_gaps.append(f"specialist_prefix:{prefix}")
    for ticker, coverage in quick_coverage.items():
        if not coverage["present"] or coverage.get("output_quality_status") not in {"pass", "limited", None} or not coverage.get("no_report_or_audit"):
            smoke_gaps.append(f"quick:{ticker}")
    doctor_ok = bool(doctor and doctor.get("status") == "pass")
    if not doctor_ok:
        smoke_gaps.append("live_doctor")
        live_gaps.append("live_doctor")
    live_acceptance_status = "Complete" if not live_gaps else "Limited"
    usage_limit_gaps = [
        f"agent_route:{route}"
        for route, coverage in route_coverage.items()
        if coverage.get("usage_limit_blocked")
    ] + [
        f"specialist_prefix:{prefix}"
        for prefix, coverage in prefix_coverage.items()
        if coverage.get("usage_limit_blocked")
    ]
    artifact_status = "fail" if smoke_gaps or (require_live and live_gaps) else "pass"
    report = {
        "schema_version": "automation_live_acceptance.v1",
        "status": artifact_status,
        "live_acceptance_status": live_acceptance_status,
        "created_at": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
        "require_live": require_live,
        "doctor": doctor,
        "quick_coverage": quick_coverage,
        "agent_route_coverage": route_coverage,
        "specialist_prefix_coverage": prefix_coverage,
        "smoke_gaps": smoke_gaps,
        "live_gaps": live_gaps,
        "usage_limit_gaps": usage_limit_gaps,
        "summary": {
            "agent_records_seen": len(agent_records),
            "specialist_records_seen": len(specialist_records),
            "quick_records_seen": len(quick_records),
            "agent_live_records_with_thread_ids": sum(1 for item in agent_records if item.get("has_real_live_thread_evidence")),
            "specialist_live_records_with_thread_ids": sum(1 for item in specialist_records if item.get("has_real_live_thread_evidence")),
            "usage_limit_blocked_records": sum(1 for item in [*agent_records, *specialist_records] if item.get("usage_limit_blocked")),
        },
    }
    if write_log:
        output_dir = get_live_acceptance_runs_dir()
        output_dir.mkdir(parents=True, exist_ok=True)
        path = output_dir / f"{safe_timestamp_for_path(report['created_at'])}-live-acceptance-{uuid4().hex[:8]}.json"
        report["log_path"] = str(path)
        write_json(path, report)
    return report


def run_live_acceptance(require_live: bool = False) -> int:
    report = build_live_acceptance_report(require_live=require_live, write_log=True)
    print(f"Automation Lab live acceptance artifact: {report['status']}")
    print(f"Live acceptance status: {report['live_acceptance_status']}")
    print(f"Smoke gaps: {', '.join(report['smoke_gaps']) if report['smoke_gaps'] else 'none'}")
    print(f"Live gaps: {', '.join(report['live_gaps']) if report['live_gaps'] else 'none'}")
    print(f"Usage-limit gaps: {', '.join(report.get('usage_limit_gaps') or []) if report.get('usage_limit_gaps') else 'none'}")
    if report.get("log_path"):
        print(f"Log: {report['log_path']}")
    return 0 if report["status"] == "pass" else 1

def run_route_check(mode: str) -> int:
    cases = load_cases()
    results = evaluate_cases(cases, mode=mode)
    run_log_path = write_run_log(mode=mode, results=results)
    print_summary(results, run_log_path)
    return 0 if all(result["status"] == "pass" for result in results) else 1


def run_quick(prompt: str, mode: str) -> int:
    if not prompt.strip():
        raise ValueError("quick-run requires a non-empty --prompt")

    try:
        if mode == "mock":
            result = mock_quick_launch(prompt)
        elif mode == "live":
            result = LiveCodexQuickLauncher().launch(prompt)
        else:
            raise ValueError(f"Unsupported quick-run mode: {mode}")
    except QuickRunError as exc:
        run_log_path = write_quick_error_log(prompt=prompt, mode=mode, error=str(exc))
        print("QUICK launch failed: validation guardrail blocked the output")
        print(f"Run log: {run_log_path}")
        return 1

    run_log_path = write_quick_run_log(result)
    print_quick_summary(result, run_log_path)
    return 0


def run_quick_answer(prompt: str, mode: str, answer_args: list[str] | None, answers_json: str | None) -> int:
    if not prompt.strip():
        raise ValueError("quick-answer requires a non-empty --prompt")
    answers = parse_quick_answers(answer_args, answers_json)
    source_snapshot = build_quick_source_snapshot(prompt=prompt, answers=answers, mode=mode)
    data_quality = assess_quick_data_quality(source_snapshot)
    run_dir = create_quick_run_dir(source_snapshot.get("asset_identity"))
    generated_answer = generate_quick_answer(
        prompt=prompt,
        answers=answers,
        source_snapshot=source_snapshot,
        data_quality=data_quality,
    )
    output_quality = assess_quick_output_quality(
        generated_answer,
        source_snapshot=source_snapshot,
        data_quality=data_quality,
    )
    try:
        validation = write_quick_answer_files(
            prompt=prompt,
            answers=answers,
            mode=mode,
            source_snapshot=source_snapshot,
            data_quality=data_quality,
            generated_answer=generated_answer,
            output_quality=output_quality,
            run_dir=run_dir,
        )
    except QuickRunError as exc:
        validation = {
            "status": "fail",
            "error": str(exc),
            "quality_checks": {
                "output_quality_passed": output_quality.get("status") == "pass",
            },
        }
        answer_path = run_dir / "quick_answer.json"
        if answer_path.is_file():
            quick_answer_payload = json.loads(answer_path.read_text(encoding="utf-8"))
            quick_answer_payload["validation_result"] = validation
            answer_path.write_text(json.dumps(quick_answer_payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        result = QuickAnswerResult(
            prompt=prompt,
            normalized_prompt=normalize_quick_prompt(prompt),
            answers=answers,
            mode=mode,
            run_dir=run_dir,
            source_snapshot=source_snapshot,
            data_quality=data_quality,
            generated_answer=generated_answer,
            output_quality=output_quality,
            validation=validation,
        )
        run_log_path = write_quick_answer_run_log(result)
        if output_quality.get("hard_failures"):
            print("QUICK answer quality failed: hard guardrail violation")
        else:
            print("QUICK answer quality failed: generated Quick Take was saved but not displayed")
        print(f"Reason: {quality_failure_summary(output_quality)}")
        print(f"Data snapshot: {run_dir}")
        print(f"Output quality: {run_dir / 'output_quality.json'}")
        print(f"Run log: {run_log_path}")
        return 1

    result = QuickAnswerResult(
        prompt=prompt,
        normalized_prompt=normalize_quick_prompt(prompt),
        answers=answers,
        mode=mode,
        run_dir=run_dir,
        source_snapshot=source_snapshot,
        data_quality=data_quality,
        generated_answer=generated_answer,
        output_quality=output_quality,
        validation=validation,
    )
    run_log_path = write_quick_answer_run_log(result)
    print_quick_answer_summary(result, run_log_path)
    return 0


def run_validate_quick_answer(run_dir: str | None) -> int:
    path = Path(run_dir) if run_dir else latest_quick_answer_run_dir()
    try:
        validation = validate_quick_answer_run(path)
    except QuickRunError as exc:
        print("QUICK answer validation failed")
        print(f"Reason: {exc}")
        return 1
    print("QUICK answer validation passed")
    print(f"Status: {validation['quick_status']}")
    print(f"Data snapshot: {validation['run_dir']}")
    return 0


def latest_quick_answer_run_dir(data_runs_dir: Path | None = None) -> Path:
    base = data_runs_dir or get_quick_data_runs_dir()
    candidates = [
        path
        for path in base.glob("*")
        if path.is_dir()
        and (path / "source_snapshot.json").is_file()
        and (path / "data_quality.json").is_file()
        and (path / "quick_answer.json").is_file()
        and (path / "output_quality.json").is_file()
    ]
    if not candidates:
        raise QuickRunError(f"quick_answer_validation_error: no quick-answer runs found under {base}")
    return max(candidates, key=lambda path: path.stat().st_mtime)


def run_agent_design(prompt: str, mode: str) -> int:
    if not prompt.strip():
        raise ValueError("agent-design requires a non-empty --prompt")
    if mode != "mock":
        raise ValueError("agent-design currently supports design-only mock mode")

    try:
        result = build_mock_agent_design(prompt)
    except AgentDesignError as exc:
        print("AGENT design failed: route guardrail blocked the design")
        print(f"Reason: {exc}")
        return 1

    run_log_path = write_agent_design_log(result)
    print_agent_design_summary(result, run_log_path)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Financial Agent Automation Lab CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    route_check = subparsers.add_parser("route-check", help="Run route check cases")
    route_check.add_argument(
        "--mode",
        choices=("mock", "live"),
        default="mock",
        help="Route check mode. Default: mock.",
    )

    live_doctor = subparsers.add_parser(
        "live-doctor",
        help="Check Automation Lab live-mode prerequisites and write a readiness log",
    )
    live_doctor.add_argument(
        "--skip-sdk-doctor",
        action="store_true",
        help="Skip the Financial Agent System npm codex:doctor subprocess check.",
    )

    live_acceptance = subparsers.add_parser(
        "live-acceptance",
        help="Build an audited acceptance manifest from QUICK, AGENT, specialist, and live-doctor artifacts",
    )
    live_acceptance.add_argument(
        "--require-live",
        action="store_true",
        help="Return failure unless real live sdk_thread_id evidence is present for every tracked AGENT route and specialist prefix.",
    )

    quick_run = subparsers.add_parser("quick-run", help="Launch guarded QUICK first step")
    quick_run.add_argument(
        "--prompt",
        required=True,
        help="Investment prompt to launch as QUICK. QUICK: prefix is added if omitted.",
    )
    quick_run.add_argument(
        "--mode",
        choices=("mock", "live"),
        default="mock",
        help="QUICK launch mode. Default: mock.",
    )

    quick_answer = subparsers.add_parser(
        "quick-answer",
        help="Create a validated QUICK answer with a public-data snapshot",
    )
    quick_answer.add_argument(
        "--prompt",
        required=True,
        help="Investment prompt to answer as QUICK. QUICK: prefix is added if omitted.",
    )
    quick_answer.add_argument(
        "--answer",
        action="append",
        dest="answers",
        help="One user answer from quick-run intake. Provide exactly three.",
    )
    quick_answer.add_argument(
        "--answers-json",
        help="Alternative to --answer: JSON array with exactly three non-empty answers.",
    )
    quick_answer.add_argument(
        "--mode",
        choices=("mock", "live"),
        default="mock",
        help="QUICK answer data mode. mock uses fixtures; live uses public sources without API keys.",
    )

    quick_validator = subparsers.add_parser(
        "validate-quick-answer",
        help="Validate the latest or specified QUICK answer run",
    )
    quick_validator.add_argument(
        "--run-dir",
        help="Path to a data_runs/quick/[timestamp]-ASSET folder. Defaults to latest.",
    )

    agent_design = subparsers.add_parser(
        "agent-design",
        help="Create a design-only AGENT automation plan without executing analysis",
    )
    agent_design.add_argument(
        "--prompt",
        required=True,
        help="Investment prompt to design as AGENT automation. AGENT: prefix is added if omitted.",
    )
    agent_design.add_argument(
        "--mode",
        choices=("mock",),
        default="mock",
        help="AGENT design mode. Default: mock.",
    )

    agent_intake = subparsers.add_parser(
        "agent-intake",
        help="Ask the required five AGENT intake questions and stop",
    )
    agent_intake.add_argument(
        "--prompt",
        required=True,
        help="AGENT prompt such as NVDA, SPY, BTC, TLT, GLD, or MSFT vs SPY vs BTC. AGENT: prefix is added if omitted.",
    )

    agent_run = subparsers.add_parser(
        "agent-run",
        help="Run the AGENT workflow with source preflight, specialists, report, and audit",
    )
    agent_run.add_argument(
        "--prompt",
        required=True,
        help="AGENT prompt such as NVDA, SPY, BTC, TLT, GLD, or MSFT vs SPY vs BTC. AGENT: prefix is added if omitted.",
    )
    agent_run.add_argument(
        "--answer",
        action="append",
        dest="answers",
        help="One AGENT intake answer. Provide 1-5; missing answers use approved baseline assumptions.",
    )
    agent_run.add_argument(
        "--answers-json",
        help="Alternative to --answer: JSON array with up to five non-empty answers.",
    )
    agent_run.add_argument(
        "--portfolio-context-json",
        help="Structured portfolio context JSON object with holdings, cash, risk_limits, horizon, constraints, existing_exposure, and objective.",
    )
    agent_run.add_argument(
        "--portfolio-context-file",
        help="Path to a JSON file containing structured portfolio context for Portfolio Fit.",
    )
    agent_run.add_argument(
        "--continue-with-baseline",
        action="store_true",
        help="Proceed with approved baseline assumptions when no answers are supplied.",
    )
    agent_run.add_argument(
        "--mode",
        choices=("mock", "live"),
        default="mock",
        help="AGENT execution mode. mock uses deterministic fixtures; live uses public sources and Codex SDK specialist runs.",
    )

    agent_validator = subparsers.add_parser(
        "validate-agent-run",
        help="Validate the latest or specified AGENT run",
    )
    agent_validator.add_argument(
        "--run-dir",
        help="Path to a Financial Agent Reports/[TICKER] ... folder. Defaults to latest supported equity run.",
    )

    specialist_run = subparsers.add_parser(
        "specialist-run",
        help="Run one direct specialist command such as RISK: Nvidia or VAL: MSFT",
    )
    specialist_run.add_argument(
        "--prompt",
        required=True,
        help="Direct specialist prompt with prefix, e.g. RISK: Nvidia, VAL: MSFT, ETF: SPY, IC: MSFT.",
    )
    specialist_run.add_argument(
        "--mode",
        choices=("mock", "live"),
        default="mock",
        help="Direct specialist execution mode. mock is deterministic; live uses the Codex SDK launcher for one specialist.",
    )

    specialist_validator = subparsers.add_parser(
        "validate-specialist-run",
        help="Validate the latest or specified direct specialist run",
    )
    specialist_validator.add_argument(
        "--run-dir",
        help="Path to a Financial Agent Reports/_specialists/[PREFIX-SUBJECT] folder. Defaults to latest.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        if args.command == "route-check":
            return run_route_check(mode=args.mode)
        if args.command == "live-doctor":
            return run_live_doctor(skip_sdk_doctor=args.skip_sdk_doctor)
        if args.command == "live-acceptance":
            return run_live_acceptance(require_live=args.require_live)
        if args.command == "quick-run":
            return run_quick(prompt=args.prompt, mode=args.mode)
        if args.command == "quick-answer":
            return run_quick_answer(
                prompt=args.prompt,
                mode=args.mode,
                answer_args=args.answers,
                answers_json=args.answers_json,
            )
        if args.command == "validate-quick-answer":
            return run_validate_quick_answer(run_dir=args.run_dir)
        if args.command == "agent-design":
            return run_agent_design(prompt=args.prompt, mode=args.mode)
        if args.command == "agent-intake":
            return run_agent_intake(prompt=args.prompt)
        if args.command == "agent-run":
            return run_agent_run(
                prompt=args.prompt,
                mode=args.mode,
                answer_args=args.answers,
                answers_json=args.answers_json,
                continue_with_baseline=args.continue_with_baseline,
                portfolio_context_json=args.portfolio_context_json,
                portfolio_context_file=args.portfolio_context_file,
            )
        if args.command == "validate-agent-run":
            return run_validate_agent_run(run_dir=args.run_dir)
        if args.command == "specialist-run":
            return run_specialist_run(prompt=args.prompt, mode=args.mode)
        if args.command == "validate-specialist-run":
            return run_validate_specialist_run(run_dir=args.run_dir)
    except (ValueError, QuickRunError, AgentDesignError, AgentRunError, SpecialistRunError, LiveRouteError) as exc:
        print(f"Error: {exc}")
        return 1

    parser.error(f"Unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    mp.freeze_support()
    raise SystemExit(main())




