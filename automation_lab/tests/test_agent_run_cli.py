from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from unittest import mock
from datetime import date
from pathlib import Path

LAB_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LAB_ROOT))

import fa_automation
from agent_data import build_evidence_pack, build_equity_source_preflight, build_msft_source_preflight
from agent_data.equity_preflight import summarize_preflight


class AgentRunTask011Tests(unittest.TestCase):
    def run_cli(self, args: list[str], reports_root: Path, runs_dir: Path | None = None) -> subprocess.CompletedProcess[str]:
        env = os.environ.copy()
        env["FA_AUTOMATION_AGENT_REPORTS_ROOT"] = str(reports_root)
        env["FA_AUTOMATION_AGENT_RUNS_DIR"] = str(runs_dir or reports_root / "runs")
        env["FA_AUTOMATION_SPECIALIST_RUNS_DIR"] = str(reports_root / "specialist-runs")
        env["FA_AUTOMATION_LIVE_DOCTOR_RUNS_DIR"] = str(reports_root / "live-doctor-runs")
        env["FA_AUTOMATION_LIVE_ACCEPTANCE_RUNS_DIR"] = str(reports_root / "live-acceptance-runs")
        env["FA_AUTOMATION_QUICK_DATA_RUNS_DIR"] = str(reports_root / "quick-data")
        return subprocess.run(
            [sys.executable, "fa_automation.py", *args],
            cwd=LAB_ROOT,
            text=True,
            capture_output=True,
            check=False,
            env=env,
        )

    def latest_report_dir(self, reports_root: Path, ticker: str = "MSFT") -> Path:
        candidates = sorted(reports_root.glob(f"{ticker} *"), key=lambda path: path.stat().st_mtime)
        self.assertTrue(candidates)
        return candidates[-1]

    def latest_specialist_dir(self, reports_root: Path, prefix: str) -> Path:
        candidates = sorted((reports_root / "_specialists").glob(f"{prefix}-*"), key=lambda path: path.stat().st_mtime)
        self.assertTrue(candidates)
        return candidates[-1]

    def test_agent_intake_asks_exactly_five_and_stops(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            reports_root = Path(temp_dir)
            completed = self.run_cli(["agent-intake", "--prompt", "MSFT for 3 years"], reports_root)

            self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
            numbered = [line for line in completed.stdout.splitlines() if line[:2] in {"1.", "2.", "3.", "4.", "5."}]
            self.assertEqual(len(numbered), 5)
            self.assertFalse(list(reports_root.glob("MSFT *")))

    def test_agent_intake_aapl_asks_exactly_five_and_stops(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            reports_root = Path(temp_dir)
            completed = self.run_cli(["agent-intake", "--prompt", "AAPL for 3 years"], reports_root)

            self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
            numbered = [line for line in completed.stdout.splitlines() if line[:2] in {"1.", "2.", "3.", "4.", "5."}]
            self.assertEqual(len(numbered), 5)
            self.assertIn("AAPL workflow", completed.stdout)
            self.assertFalse(list(reports_root.glob("AAPL *")))

    def test_agent_intake_dynamic_us_ticker_asks_exactly_five_and_stops(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            reports_root = Path(temp_dir)
            completed = self.run_cli(["agent-intake", "--prompt", "NVDA for 3 years"], reports_root)

            self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
            numbered = [line for line in completed.stdout.splitlines() if line[:2] in {"1.", "2.", "3.", "4.", "5."}]
            self.assertEqual(len(numbered), 5)
            self.assertIn("NVDA workflow", completed.stdout)
            self.assertFalse(list(reports_root.glob("NVDA *")))

    def test_agent_run_without_answers_prints_intake_and_creates_no_report(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            reports_root = Path(temp_dir)
            completed = self.run_cli(["agent-run", "--prompt", "MSFT for 3 years", "--mode", "mock"], reports_root)

            self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
            self.assertIn("No report or audit was created", completed.stdout)
            self.assertFalse(list(reports_root.glob("MSFT *")))

    def test_agent_run_mock_creates_report_audit_and_validates(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            reports_root = Path(temp_dir)
            completed = self.run_cli(
                [
                    "agent-run",
                    "--prompt",
                    "MSFT for 3 years",
                    "--answer",
                    "3 years",
                    "--answer",
                    "No current position",
                    "--answer",
                    "Quality compounder and valuation entry",
                    "--answer",
                    "Use latest public data if available",
                    "--answer",
                    "No portfolio context provided",
                    "--mode",
                    "mock",
                ],
                reports_root,
            )

            self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
            run_dir = self.latest_report_dir(reports_root)
            report = run_dir / "investment_report.md"
            audit = run_dir / "audit"
            self.assertTrue(report.is_file())
            self.assertTrue(audit.is_dir())
            self.assertTrue((audit / "source_preflight.json").is_file())
            self.assertTrue((audit / "evidence_pack.md").is_file())
            self.assertTrue((audit / "specialists" / "investment-committee-agent" / "handoff.json").is_file())
            report_text = report.read_text(encoding="utf-8")
            self.assertTrue(report_text.startswith("Report status:"))
            self.assertIn("Report status:", report_text)
            self.assertIn("Preparation date:", report_text)
            self.assertIn("Freshness and source note:", report_text)
            self.assertIn("Decision confidence:", report_text)
            self.assertIn("What is still needed for a personal final decision", report_text)
            self.assertIn("Evidence Status Summary", report_text)
            self.assertNotIn("IC Action Status", report_text)
            self.assertNotIn("Action Box", report_text)
            self.assertNotIn("decision_prep_memo.md", report_text)
            self.assertIn("What the specialist checks added", report_text)
            self.assertIn(str(report), completed.stdout)

            ic_handoff = json.loads(
                (audit / "specialists" / "investment-committee-agent" / "handoff.json").read_text(encoding="utf-8")
            )
            self.assertIn("financial-statement-analysis", ic_handoff["consumed_handoff_ids"])
            self.assertEqual(ic_handoff["consumed_handoff_count"], 10)

            validate = self.run_cli(["validate-agent-run", "--run-dir", str(run_dir)], reports_root)
            self.assertEqual(validate.returncode, 0, validate.stderr + validate.stdout)
            validation = json.loads((audit / "agent_run_validation.json").read_text(encoding="utf-8"))
            self.assertTrue(validation["checks"]["subject_consistent_intake_preflight_manifest"])
            self.assertTrue(validation["checks"]["subject_consistent_report_folder"])
            self.assertTrue(validation["checks"]["subject_consistent_report_title"])

    def test_agent_run_mock_aapl_russian_report_validates(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            reports_root = Path(temp_dir)
            completed = self.run_cli(
                [
                    "agent-run",
                    "--prompt",
                    "AAPL на 3 года",
                    "--answer",
                    "3 года",
                    "--answer",
                    "Нет текущей позиции",
                    "--answer",
                    "Качество бизнеса и оценка входа",
                    "--answer",
                    "Используй свежие публичные данные если доступны",
                    "--answer",
                    "Портфельный контекст не предоставлен",
                    "--mode",
                    "mock",
                ],
                reports_root,
            )

            self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
            run_dir = self.latest_report_dir(reports_root, "AAPL")
            audit = run_dir / "audit"
            report_text = (run_dir / "investment_report.md").read_text(encoding="utf-8")
            self.assertTrue(report_text.startswith("Дата подготовки:"))
            self.assertIn("Статус отчёта:", report_text)
            self.assertIn("Свежесть и источники:", report_text)
            self.assertIn("Уверенность вывода:", report_text)
            self.assertIn("# AAPL — инвестиционный разбор", report_text)
            self.assertIn("Ключевые источники", report_text)
            self.assertIn("Статус доказательной базы", report_text)
            self.assertNotIn("????", report_text)

            validate = self.run_cli(["validate-agent-run", "--run-dir", str(run_dir)], reports_root)
            self.assertEqual(validate.returncode, 0, validate.stderr + validate.stdout)
            validation = json.loads((audit / "agent_run_validation.json").read_text(encoding="utf-8"))
            self.assertTrue(validation["checks"]["subject_consistent_intake_preflight_manifest"])
            self.assertTrue(validation["checks"]["subject_consistent_report_folder"])
            self.assertTrue(validation["checks"]["subject_consistent_report_title"])
            self.assertIn("AGENT run validation passed", validate.stdout)

    def test_reader_report_validator_rejects_old_shallow_heading_report(self) -> None:
        old_report = """Дата подготовки: 2026-07-02
Статус отчёта: подготовительный инвестиционный разбор.
Свежесть и источники: использованы публичные источники.
Уверенность вывода: средняя.

# MSFT — инвестиционный разбор

## Короткий вывод
MSFT выглядит качественной компанией.

## Рабочий вывод IC
- Компания хорошая, но оценка важна.

## Финансовый снимок
| Метрика | Значение | Период |
|---|---:|---|
| Выручка | н/д | н/д |

## Итог IC-сборки
- Можно рассмотреть.

## Ключевые источники
- SEC company facts
"""
        validation = fa_automation.validate_reader_report_text(old_report)
        self.assertEqual(validation["status"], "fail")
        self.assertFalse(validation["checks"]["has_financial_snapshot_table"])
        self.assertFalse(validation["checks"]["has_decision_prep_substance"])
        self.assertFalse(validation["checks"]["russian_language_policy_no_obvious_run_glish"])

    def test_failed_ic_attempt_does_not_emit_completed_ic_synthesis(self) -> None:
        specialists = [
            {"specialist_id": specialist_id, "status": "ok", "handoff": {"consumed_handoff_ids": []}}
            for specialist_id in fa_automation.AGENT_SPECIALISTS_EQUITY
            if specialist_id != "investment-committee-agent"
        ]
        specialists.append(
            {
                "specialist_id": "investment-committee-agent",
                "status": "error",
                "handoff": {"consumed_handoff_ids": [sid for sid in fa_automation.AGENT_SPECIALISTS_EQUITY if sid != "investment-committee-agent"]},
            }
        )
        lines = fa_automation.reader_ic_synthesis(
            specialists,
            "ru",
            {"ticker": "MSFT"},
            {"evidence_readiness": "Complete"},
        )
        text = "\n".join(lines)
        self.assertIn("не выполнена", text)
        self.assertNotIn("IC-сборка считает", text)
        self.assertFalse(fa_automation.ic_completed_with_expected_handoffs(specialists))

    def test_agent_run_mock_aapl_creates_report_audit_and_validates(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            reports_root = Path(temp_dir)
            completed = self.run_cli(
                [
                    "agent-run",
                    "--prompt",
                    "AAPL for 3 years",
                    "--answer",
                    "3 years",
                    "--answer",
                    "No current position",
                    "--answer",
                    "Quality compounder and valuation entry",
                    "--answer",
                    "Use latest public data if available",
                    "--answer",
                    "No portfolio context provided",
                    "--mode",
                    "mock",
                ],
                reports_root,
            )

            self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
            run_dir = self.latest_report_dir(reports_root, "AAPL")
            report = run_dir / "investment_report.md"
            audit = run_dir / "audit"
            self.assertTrue(report.is_file())
            self.assertTrue(audit.is_dir())
            for required in [
                "intake.json",
                "source_preflight.json",
                "evidence_pack.json",
                "evidence_pack.md",
                "pre_ic_evidence_lock.json",
                "run_manifest.json",
            ]:
                self.assertTrue((audit / required).is_file(), required)
            self.assertTrue((audit / "specialists" / "investment-committee-agent" / "handoff.json").is_file())
            report_text = report.read_text(encoding="utf-8")
            self.assertIn("# AAPL Investment Review", report_text)
            self.assertIn("Apple Inc.", report_text)
            self.assertNotIn("Azure", report_text)
            self.assertNotIn("Microsoft screens", report_text)

            preflight = json.loads((audit / "source_preflight.json").read_text(encoding="utf-8"))
            self.assertEqual(preflight["subject_identity"]["ticker"], "AAPL")
            self.assertEqual(preflight["subject_identity"]["cik"], "0000320193")
            source_validation = fa_automation.validate_source_preflight(preflight)
            self.assertTrue(source_validation["checks"]["sec_identity_matches_subject"])

            manifest = json.loads((audit / "run_manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(manifest["subject"], "AAPL")
            self.assertFalse(manifest["production_real_subagents"])

            validate = self.run_cli(["validate-agent-run", "--run-dir", str(run_dir)], reports_root)
            self.assertEqual(validate.returncode, 0, validate.stderr + validate.stdout)

    def test_validate_agent_run_defaults_to_latest_supported_equity(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            reports_root = Path(temp_dir)
            completed = self.run_cli(
                [
                    "agent-run",
                    "--prompt",
                    "AAPL for 3 years",
                    "--answer",
                    "3 years",
                    "--answer",
                    "No current position",
                    "--answer",
                    "Quality compounder and valuation entry",
                    "--answer",
                    "Use latest public data if available",
                    "--answer",
                    "No portfolio context provided",
                    "--mode",
                    "mock",
                ],
                reports_root,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)

            validate = self.run_cli(["validate-agent-run"], reports_root)
            self.assertEqual(validate.returncode, 0, validate.stderr + validate.stdout)
            self.assertIn("AAPL", validate.stdout)

    def test_dynamic_us_equities_mock_validate(self) -> None:
        for ticker, expected_classification in [
            ("NVDA", "us_common_equity"),
            ("GOOGL", "us_share_class"),
            ("GOOG", "us_share_class"),
            ("BRK.B", "us_share_class"),
            ("BRK-B", "us_share_class"),
        ]:
            with self.subTest(ticker=ticker), tempfile.TemporaryDirectory() as temp_dir:
                reports_root = Path(temp_dir)
                completed = self.run_cli(
                    ["agent-run", "--prompt", f"{ticker} for 3 years", "--continue-with-baseline", "--mode", "mock"],
                    reports_root,
                )
                self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
                canonical = "BRK.B" if ticker == "BRK-B" else ticker
                run_dir = self.latest_report_dir(reports_root, canonical)
                preflight = json.loads((run_dir / "audit" / "source_preflight.json").read_text(encoding="utf-8"))
                self.assertEqual(preflight["subject_identity"]["ticker"], canonical)
                self.assertEqual(preflight["subject_identity"]["instrument_classification"], expected_classification)
                validate = self.run_cli(["validate-agent-run", "--run-dir", str(run_dir)], reports_root)
                self.assertEqual(validate.returncode, 0, validate.stderr + validate.stdout)

    def test_adr_and_non_us_mock_paths_validate_with_gates(self) -> None:
        for ticker, expected_classification, expected_limit in [
            ("BABA", "adr_or_foreign_issuer_us_listing", "ADR or foreign-issuer US listing"),
            ("ASML.AS", "non_us_listed_equity", "direct non-US listed equity"),
        ]:
            with self.subTest(ticker=ticker), tempfile.TemporaryDirectory() as temp_dir:
                reports_root = Path(temp_dir)
                completed = self.run_cli(
                    ["agent-run", "--prompt", f"{ticker} for 3 years", "--continue-with-baseline", "--mode", "mock"],
                    reports_root,
                )
                self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
                run_dir = self.latest_report_dir(reports_root, ticker)
                report_text = (run_dir / "investment_report.md").read_text(encoding="utf-8")
                preflight = json.loads((run_dir / "audit" / "source_preflight.json").read_text(encoding="utf-8"))
                manifest = json.loads((run_dir / "audit" / "run_manifest.json").read_text(encoding="utf-8"))
                self.assertEqual(preflight["subject_identity"]["instrument_classification"], expected_classification)
                self.assertEqual(manifest["instrument_classification"], expected_classification)
                self.assertIn(expected_limit, report_text)
                self.assertTrue((run_dir / "audit" / "provider_results.json").is_file())
                if expected_classification == "adr_or_foreign_issuer_us_listing":
                    adr_gate = preflight["subject_identity"]["adr_gate"]
                    for field in [
                        "underlying_issuer",
                        "issuer_country",
                        "trading_currency",
                        "reporting_basis",
                        "liquidity_check",
                        "regulatory_delisting_risk",
                    ]:
                        self.assertIn(field, adr_gate)
                validate = self.run_cli(["validate-agent-run", "--run-dir", str(run_dir)], reports_root)
                self.assertEqual(validate.returncode, 0, validate.stderr + validate.stdout)

    def test_partial_answers_use_baseline_assumptions(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            reports_root = Path(temp_dir)
            completed = self.run_cli(
                [
                    "agent-run",
                    "--prompt",
                    "MSFT for 3 years",
                    "--answer",
                    "3 years",
                    "--answer",
                    "No current position",
                    "--mode",
                    "mock",
                ],
                reports_root,
            )

            self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
            intake = json.loads((self.latest_report_dir(reports_root) / "audit" / "intake.json").read_text(encoding="utf-8"))
            self.assertEqual(intake["answers_provided_count"], 2)
            self.assertTrue(intake["baseline_used"])
            self.assertEqual(len(intake["unanswered"]), 3)

    def test_continue_with_baseline_allows_zero_answers(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            reports_root = Path(temp_dir)
            completed = self.run_cli(
                ["agent-run", "--prompt", "MSFT for 3 years", "--continue-with-baseline", "--mode", "mock"],
                reports_root,
            )

            self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
            intake = json.loads((self.latest_report_dir(reports_root) / "audit" / "intake.json").read_text(encoding="utf-8"))
            self.assertEqual(intake["answers_provided_count"], 0)
            self.assertEqual(intake["baseline_reason"], "explicit --continue-with-baseline")

    def test_answers_json_is_accepted(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            reports_root = Path(temp_dir)
            completed = self.run_cli(
                [
                    "agent-run",
                    "--prompt",
                    "MSFT for 3 years",
                    "--answers-json",
                    '["3 years", "No position", "Valuation", "Latest public data", "No portfolio context"]',
                    "--mode",
                    "mock",
                ],
                reports_root,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)

    def test_structured_portfolio_context_json_is_audited_and_validates(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            reports_root = Path(temp_dir)
            context = {
                "holdings": [{"ticker": "MSFT", "weight": "4%"}, {"ticker": "SPY", "weight": "35%"}],
                "cash": "8%",
                "risk_limits": {"max_single_name_weight": "7%", "max_drawdown_tolerance": "15%"},
                "horizon": "3 years",
                "constraints": ["USD portfolio", "no leverage"],
                "existing_exposure": "large-cap technology already meaningful through SPY",
                "objective": "quality growth with controlled concentration",
            }
            completed = self.run_cli(
                [
                    "agent-run",
                    "--prompt",
                    "MSFT for 3 years",
                    "--continue-with-baseline",
                    "--portfolio-context-json",
                    json.dumps(context),
                    "--mode",
                    "mock",
                ],
                reports_root,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
            run_dir = self.latest_report_dir(reports_root)
            audit = run_dir / "audit"
            intake = json.loads((audit / "intake.json").read_text(encoding="utf-8"))
            portfolio_context = json.loads((audit / "portfolio_context.json").read_text(encoding="utf-8"))
            manifest = json.loads((audit / "run_manifest.json").read_text(encoding="utf-8"))
            report_text = (run_dir / "investment_report.md").read_text(encoding="utf-8")
            self.assertTrue(intake["portfolio_context_provided"])
            self.assertEqual(portfolio_context["status"], "provided")
            self.assertEqual(set(portfolio_context["provided_fields"]), set(fa_automation.PORTFOLIO_CONTEXT_FIELDS))
            self.assertFalse(portfolio_context["personal_action_unlocked"])
            self.assertEqual(manifest["portfolio_context_status"], "provided")
            self.assertIn("Structured portfolio context supplied", report_text)
            self.assertIn("quality growth with controlled concentration", report_text)
            validate = self.run_cli(["validate-agent-run", "--run-dir", str(run_dir)], reports_root)
            self.assertEqual(validate.returncode, 0, validate.stderr + validate.stdout)
            validation = json.loads((audit / "agent_run_validation.json").read_text(encoding="utf-8"))
            self.assertTrue(validation["checks"]["portfolio_context_audit_present"])
            self.assertTrue(validation["checks"]["portfolio_context_truthful"])
            self.assertTrue(validation["checks"]["portfolio_context_no_personal_action_unlock"])

    def test_structured_portfolio_context_file_is_accepted(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            reports_root = Path(temp_dir)
            context_path = Path(temp_dir) / "portfolio-context.json"
            context_path.write_text(
                json.dumps(
                    {
                        "objective": "income ballast",
                        "horizon": "5 years",
                        "constraints": ["low drawdown preference"],
                    }
                ),
                encoding="utf-8",
            )
            completed = self.run_cli(
                [
                    "agent-run",
                    "--prompt",
                    "TLT bond ETF",
                    "--continue-with-baseline",
                    "--portfolio-context-file",
                    str(context_path),
                    "--mode",
                    "mock",
                ],
                reports_root,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
            run_dir = self.latest_report_dir(reports_root, "TLT")
            portfolio_context = json.loads((run_dir / "audit" / "portfolio_context.json").read_text(encoding="utf-8"))
            self.assertEqual(portfolio_context["source"], "cli_file")
            self.assertEqual(portfolio_context["status"], "partial")

    def test_empty_structured_portfolio_context_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            reports_root = Path(temp_dir)
            completed = self.run_cli(
                [
                    "agent-run",
                    "--prompt",
                    "MSFT for 3 years",
                    "--continue-with-baseline",
                    "--portfolio-context-json",
                    "{}",
                    "--mode",
                    "mock",
                ],
                reports_root,
            )
            self.assertNotEqual(completed.returncode, 0)
            self.assertIn("portfolio context input did not contain", completed.stdout)
            self.assertFalse(list(reports_root.glob("MSFT *")))

    def test_unsupported_unresolved_non_equity_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            reports_root = Path(temp_dir)
            completed = self.run_cli(["agent-run", "--prompt", "ETF for 3 years", "--continue-with-baseline", "--mode", "mock"], reports_root)

            self.assertNotEqual(completed.returncode, 0)
            self.assertIn("no supported ETF / fund identity was resolved", completed.stdout)
            self.assertFalse(list(reports_root.glob("*")))

    def test_private_companies_and_complex_instruments_are_rejected(self) -> None:
        for prompt, expected in [
            ("OpenAI for 3 years", "private companies are not ordinary public listed equity targets"),
            ("SpaceX for 3 years", "private companies are not ordinary public listed equity targets"),
            ("Stripe for 3 years", "private companies are not ordinary public listed equity targets"),
            ("AAPL warrants", "complex equity-like instruments are not ordinary equity targets"),
            ("MSFT preferred shares", "complex equity-like instruments are not ordinary equity targets"),
            ("BABA options", "complex equity-like instruments are not ordinary equity targets"),
        ]:
            with self.subTest(prompt=prompt), tempfile.TemporaryDirectory() as temp_dir:
                reports_root = Path(temp_dir)
                completed = self.run_cli(["agent-run", "--prompt", prompt, "--continue-with-baseline", "--mode", "mock"], reports_root)
                self.assertNotEqual(completed.returncode, 0)
                self.assertIn(expected, completed.stdout)

    def test_complex_guard_does_not_block_ordinary_risk_words(self) -> None:
        for prompt in [
            "AAPL human rights risk for 3 years",
            "UAL United Airlines for 3 years",
        ]:
            with self.subTest(prompt=prompt), tempfile.TemporaryDirectory() as temp_dir:
                reports_root = Path(temp_dir)
                completed = self.run_cli(["agent-intake", "--prompt", prompt], reports_root)
                self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
                self.assertIn("AGENT intake", completed.stdout)

    def test_numeric_non_us_public_tickers_resolve_and_validate_in_mock(self) -> None:
        for ticker in ["7203.T", "9988.HK"]:
            with self.subTest(ticker=ticker), tempfile.TemporaryDirectory() as temp_dir:
                reports_root = Path(temp_dir)
                completed = self.run_cli(
                    ["agent-run", "--prompt", f"{ticker} for 3 years", "--continue-with-baseline", "--mode", "mock"],
                    reports_root,
                )
                self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
                run_dir = self.latest_report_dir(reports_root, ticker)
                preflight = json.loads((run_dir / "audit" / "source_preflight.json").read_text(encoding="utf-8"))
                self.assertEqual(preflight["subject_identity"]["ticker"], ticker)
                self.assertEqual(preflight["subject_identity"]["instrument_classification"], "non_us_listed_equity")
                validate = self.run_cli(["validate-agent-run", "--run-dir", str(run_dir)], reports_root)
                self.assertEqual(validate.returncode, 0, validate.stderr + validate.stdout)

    def test_ambiguous_multiple_supported_equities_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            reports_root = Path(temp_dir)
            completed = self.run_cli(
                ["agent-run", "--prompt", "AAPL and MSFT for 3 years", "--continue-with-baseline", "--mode", "mock"],
                reports_root,
            )

            self.assertNotEqual(completed.returncode, 0)
            self.assertIn("Single-equity AGENT runs support one equity at a time", completed.stdout)
            self.assertFalse(list(reports_root.glob("AAPL *")))
            self.assertFalse(list(reports_root.glob("MSFT *")))

    def test_mock_mode_is_not_production_real_subagents(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            reports_root = Path(temp_dir)
            completed = self.run_cli(["agent-run", "--prompt", "MSFT", "--continue-with-baseline", "--mode", "mock"], reports_root)
            self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
            manifest_path = self.latest_report_dir(reports_root) / "audit" / "run_manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            self.assertFalse(manifest["production_real_subagents"])
            self.assertIn("Mock specialist outputs", manifest["mock_mode_notice"])

    def test_live_codex_sdk_bridge_uses_financial_system_cli(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            project_root = Path(temp_dir)
            sdk_log = str(project_root / "sdk-log").replace("\\", "\\\\")
            completed = subprocess.CompletedProcess(
                args=[],
                returncode=0,
                stdout=(
                    "> financial-agent-system@0.1.0 codex:run\n"
                    '{\n'
                    '  "status": "completed",\n'
                    '  "threadId": "thread-123",\n'
                    '  "finalResponse": "# Specialist handoff\\nComplete",\n'
                    f'  "logDir": "{sdk_log}"\n'
                    "}\n"
                ),
                stderr="",
            )
            with mock.patch.dict(
                os.environ,
                {
                    "FA_AUTOMATION_CODEX_SDK_PROJECT_ROOT": str(project_root),
                    "FA_AUTOMATION_CODEX_SDK_COMMAND": "npm.cmd",
                    "FA_AUTOMATION_CODEX_SDK_TIMEOUT_SECONDS": "7",
                },
                clear=False,
            ), mock.patch.object(fa_automation.subprocess, "run", return_value=completed) as run_mock:
                result = fa_automation.run_live_specialist_codex("equity-agent", "specialist prompt")

            self.assertEqual(result["status"], "ok")
            self.assertEqual(result["sdk_thread_id"], "thread-123")
            self.assertEqual(result["codex_execution_path"], "financial_agent_system_codex_sdk_cli")
            self.assertEqual(result["timeout_seconds"], 7)
            command = run_mock.call_args.args[0]
            self.assertEqual(command[:4], ["npm.cmd", "run", "codex:run", "--"])
            self.assertIn("--prompt-file", command)
            self.assertNotIn("specialist prompt", command)
            self.assertIn("--live", command)
            self.assertIn("--workspace", command)
            self.assertIn("read_only", command)
            prompt_path = Path(command[command.index("--prompt-file") + 1])
            self.assertFalse(prompt_path.exists())
            self.assertEqual(result["prompt_transport"], "prompt_file")
            self.assertIn("--prompt-file", result["command_shape"])
        self.assertIn("<prompt-file>", result["command_shape"])
        self.assertNotIn("specialist prompt", json.dumps(result))

    def test_live_codex_sdk_completed_without_thread_id_is_error(self) -> None:
        completed_without_thread = subprocess.CompletedProcess(
            args=[],
            returncode=0,
            stdout='{"status":"completed","finalResponse":"# Handoff\\nComplete"}',
            stderr="",
        )
        with tempfile.TemporaryDirectory() as temp_dir, mock.patch.dict(
            os.environ,
            {"FA_AUTOMATION_CODEX_SDK_PROJECT_ROOT": temp_dir},
            clear=False,
        ), mock.patch.object(fa_automation.subprocess, "run", return_value=completed_without_thread):
            result = fa_automation.run_live_specialist_codex("equity-agent", "specialist prompt")
        self.assertEqual(result["status"], "error")
        self.assertEqual(result["sdk_thread_id"], "")
        self.assertIn("threadId", result["error"])

    def test_live_codex_sdk_subprocess_timeout_is_capped_by_remaining_agent_budget(self) -> None:
        completed = subprocess.CompletedProcess(
            args=[],
            returncode=0,
            stdout='{"status":"completed","threadId":"thread-budget","finalResponse":"# Handoff\\nComplete"}',
            stderr="",
        )
        with tempfile.TemporaryDirectory() as temp_dir, mock.patch.dict(
            os.environ,
            {
                "FA_AUTOMATION_CODEX_SDK_PROJECT_ROOT": temp_dir,
                "FA_AUTOMATION_CODEX_SDK_TIMEOUT_SECONDS": "900",
            },
            clear=False,
        ), mock.patch.object(fa_automation.subprocess, "run", return_value=completed) as run_mock:
            result = fa_automation.run_live_specialist_codex("equity-agent", "specialist prompt", max_timeout_seconds=2.25)
        self.assertEqual(result["status"], "ok")
        self.assertEqual(result["timeout_seconds"], 2.25)
        self.assertIn("FA_AUTOMATION_AGENT_TOTAL_TIMEOUT_SECONDS", result["timeout_source"])
        self.assertAlmostEqual(run_mock.call_args.kwargs["timeout"], 2.25, places=2)

    def test_live_codex_sdk_bridge_failure_and_timeout_are_limited_inputs(self) -> None:
        failed = subprocess.CompletedProcess(
            args=[],
            returncode=1,
            stdout='{"status":"failed","error":"boom"}',
            stderr="",
        )
        with tempfile.TemporaryDirectory() as temp_dir, mock.patch.dict(
            os.environ,
            {"FA_AUTOMATION_CODEX_SDK_PROJECT_ROOT": temp_dir, "FA_AUTOMATION_CODEX_SDK_TIMEOUT_SECONDS": "3"},
            clear=False,
        ), mock.patch.object(fa_automation.subprocess, "run", return_value=failed):
            result = fa_automation.run_live_specialist_codex("risk-red-team-agent", "SECRET_PROMPT_MARKER_FAILURE")
        self.assertEqual(result["status"], "error")
        self.assertEqual(result["sdk_thread_id"], "")
        self.assertEqual(result["subprocess_exit_code"], 1)
        self.assertIn("boom", result["sdk_error"])
        self.assertEqual(result["prompt_transport"], "prompt_file")

        with tempfile.TemporaryDirectory() as temp_dir, mock.patch.dict(
            os.environ,
            {"FA_AUTOMATION_CODEX_SDK_PROJECT_ROOT": temp_dir, "FA_AUTOMATION_CODEX_SDK_TIMEOUT_SECONDS": "3"},
            clear=False,
        ), mock.patch.object(
            fa_automation.subprocess,
            "run",
            side_effect=subprocess.TimeoutExpired(cmd="npm.cmd", timeout=3),
        ):
            timeout_result = fa_automation.run_live_specialist_codex("risk-red-team-agent", "SECRET_PROMPT_MARKER_TIMEOUT")
        self.assertEqual(timeout_result["status"], "error")
        self.assertIn("timed out", timeout_result["error"])
        self.assertEqual(timeout_result["timeout_seconds"], 3)
        self.assertEqual(timeout_result["prompt_transport"], "prompt_file")
        self.assertNotIn("SECRET_PROMPT_MARKER_TIMEOUT", json.dumps(timeout_result))

    def test_live_timeout_policy_default_global_and_specialist_override(self) -> None:
        with mock.patch.dict(os.environ, {}, clear=True):
            self.assertEqual(fa_automation.get_codex_sdk_timeout_seconds("equity-agent"), (900, "default"))
            self.assertEqual(fa_automation.get_agent_total_timeout_seconds(), 7200)
            self.assertEqual(fa_automation.get_agent_max_parallel_specialists(), 3)

        with mock.patch.dict(
            os.environ,
            {
                "FA_AUTOMATION_CODEX_SDK_TIMEOUT_SECONDS": "111",
                "FA_AUTOMATION_CODEX_SDK_TIMEOUT_EQUITY_AGENT": "222",
                "FA_AUTOMATION_AGENT_TOTAL_TIMEOUT_SECONDS": "3333",
                "FA_AUTOMATION_AGENT_MAX_PARALLEL_SPECIALISTS": "2",
            },
            clear=True,
        ):
            self.assertEqual(fa_automation.get_codex_sdk_timeout_seconds("risk-red-team-agent"), (111, "FA_AUTOMATION_CODEX_SDK_TIMEOUT_SECONDS"))
            self.assertEqual(fa_automation.get_codex_sdk_timeout_seconds("equity-agent"), (222, "FA_AUTOMATION_CODEX_SDK_TIMEOUT_EQUITY_AGENT"))
            self.assertEqual(fa_automation.get_agent_total_timeout_seconds(), 3333)
            self.assertEqual(fa_automation.get_agent_max_parallel_specialists(), 2)

        with mock.patch.dict(
            os.environ,
            {
                "FA_AUTOMATION_CODEX_SDK_TIMEOUT_EQUITY_AGENT": "not-an-int",
                "FA_AUTOMATION_AGENT_MAX_PARALLEL_SPECIALISTS": "0",
            },
            clear=True,
        ):
            self.assertEqual(fa_automation.get_codex_sdk_timeout_seconds("equity-agent"), (900, "FA_AUTOMATION_CODEX_SDK_TIMEOUT_EQUITY_AGENT"))
            self.assertEqual(fa_automation.get_agent_max_parallel_specialists(), 3)

    def test_staged_parallel_execution_runs_evidence_then_parallel_then_ic(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir, mock.patch.dict(
            os.environ,
            {"FA_AUTOMATION_AGENT_MAX_PARALLEL_SPECIALISTS": "2"},
            clear=False,
        ):
            run_dir = Path(temp_dir)
            (run_dir / "audit").mkdir()
            preflight = build_msft_source_preflight("MSFT", ["3 years"], "mock")
            evidence_pack = build_evidence_pack(preflight, freshness_required=False)
            intake = fa_automation.build_agent_intake_payload("MSFT for 3 years", ["3 years"], False)
            call_order: list[str] = []
            ic_prior_counts: list[int] = []
            active = 0
            peak = 0
            lock = threading.Lock()
            non_ic = {
                sid
                for sid in fa_automation.AGENT_SPECIALISTS_EQUITY
                if sid not in {"evidence-collector", "investment-committee-agent"}
            }

            def fake_writer(run_dir, specialist_id, mode, intake, evidence_pack, preflight, prior_handoffs=None, deadline_monotonic=None):
                nonlocal active, peak
                with lock:
                    call_order.append(specialist_id)
                    if specialist_id in non_ic:
                        active += 1
                        peak = max(peak, active)
                    if specialist_id == "investment-committee-agent":
                        ic_prior_counts.append(len(prior_handoffs or []))
                time.sleep(0.01)
                with lock:
                    if specialist_id in non_ic:
                        active -= 1
                return {
                    "specialist_id": specialist_id,
                    "status": "ok",
                    "thread_or_run_id": f"mock-{specialist_id}",
                    "sdk_thread_id": "",
                    "attempt_history": [{"attempt_no": 1, "status": "ok"}],
                    "handoff": {"Produced by": specialist_id, "Artifact": f"{specialist_id}.md", "consumed_handoff_ids": [h.get("Produced by") for h in (prior_handoffs or [])]},
                }

            with mock.patch.object(fa_automation, "write_specialist_artifacts", side_effect=fake_writer):
                results = fa_automation.run_agent_specialists(run_dir, "mock", intake, evidence_pack, preflight)

            self.assertEqual(call_order[0], "evidence-collector")
            self.assertEqual(call_order[-1], "investment-committee-agent")
            self.assertLessEqual(peak, 2)
            self.assertEqual(ic_prior_counts, [10])
            self.assertEqual([item["specialist_id"] for item in results], fa_automation.AGENT_SPECIALISTS_EQUITY)
            self.assertTrue((run_dir / "audit" / "specialist_stage_execution.json").is_file())

    def test_agent_total_timeout_stops_remaining_parallel_waves_before_ic(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir, mock.patch.dict(
            os.environ,
            {
                "FA_AUTOMATION_AGENT_TOTAL_TIMEOUT_SECONDS": "1",
                "FA_AUTOMATION_AGENT_MAX_PARALLEL_SPECIALISTS": "3",
            },
            clear=False,
        ):
            run_dir = Path(temp_dir)
            (run_dir / "audit").mkdir()
            preflight = build_msft_source_preflight("MSFT", ["3 years"], "mock")
            evidence_pack = build_evidence_pack(preflight, freshness_required=False)
            intake = fa_automation.build_agent_intake_payload("MSFT for 3 years", ["3 years"], False)
            max_timeouts_seen: list[float | None] = []

            def slow_ok(specialist_id, prompt, max_timeout_seconds=None):
                max_timeouts_seen.append(max_timeout_seconds)
                time.sleep(0.4)
                return {
                    "status": "ok",
                    "response": f"# {specialist_id}\nComplete",
                    "sdk_thread_id": f"thread-{specialist_id}",
                    "codex_execution_path": "financial_agent_system_codex_sdk_cli",
                    "codex_sdk_project_root": str(fa_automation.PROJECT_ROOT),
                    "codex_sdk_log_dir": str(run_dir / "sdk-log"),
                    "sdk_error": None,
                    "subprocess_exit_code": 0,
                    "timeout_seconds": max(0, int(max_timeout_seconds or 0)),
                    "timeout_source": "test",
                    "started_at": fa_automation.now_iso(),
                    "completed_at": fa_automation.now_iso(),
                    "duration_seconds": 0.4,
                    "prompt_transport": "prompt_file",
                    "command_shape": ["npm.cmd", "--prompt-file", "<prompt-file>"],
                }

            start = time.monotonic()
            with mock.patch.object(fa_automation, "run_live_specialist_codex", side_effect=slow_ok):
                results = fa_automation.run_agent_specialists(run_dir, "live", intake, evidence_pack, preflight)
            elapsed = time.monotonic() - start
            specialist_ids = [item["specialist_id"] for item in results]
            self.assertIn("evidence-collector", specialist_ids)
            self.assertNotIn("investment-committee-agent", specialist_ids)
            self.assertLess(len(specialist_ids), len(fa_automation.AGENT_SPECIALISTS_EQUITY))
            self.assertLess(elapsed, 2.5)
            self.assertTrue(all(value is None or value <= 1.0 for value in max_timeouts_seen))
            stage_execution = json.loads((run_dir / "audit" / "specialist_stage_execution.json").read_text(encoding="utf-8"))
            aggregate = next(event for event in stage_execution["events"] if event["stage"] == "parallel_non_ic_specialists")
            self.assertTrue(aggregate["not_started_specialists"])

    def test_all_success_live_manifest_complete_semantics(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            run_dir = Path(temp_dir)
            (run_dir / "audit").mkdir()
            preflight = build_msft_source_preflight("MSFT", ["3 years"], "mock")
            evidence_pack = build_evidence_pack(preflight, freshness_required=False)
            intake = fa_automation.build_agent_intake_payload("MSFT for 3 years", ["3 years"], False)
            upstream = [sid for sid in fa_automation.AGENT_SPECIALISTS_EQUITY if sid != "investment-committee-agent"]
            specialists = []
            for sid in fa_automation.AGENT_SPECIALISTS_EQUITY:
                consumed = upstream if sid == "investment-committee-agent" else []
                specialists.append(
                    {
                        "specialist_id": sid,
                        "status": "ok",
                        "thread_or_run_id": f"thread-{sid}",
                        "sdk_thread_id": f"thread-{sid}",
                        "attempt_history": [{"attempt_no": 1, "status": "ok", "sdk_thread_id": f"thread-{sid}"}],
                        "handoff": {"Produced by": sid, "Artifact": f"{sid}.md", "consumed_handoff_ids": consumed},
                    }
                )

            fa_automation.write_run_manifest(run_dir, "MSFT for 3 years", "live", intake, preflight, evidence_pack, specialists)
            manifest = json.loads((run_dir / "audit" / "run_manifest.json").read_text(encoding="utf-8"))
            self.assertTrue(manifest["workflow_complete"])
            self.assertEqual(manifest["analysis_status"], "Complete")
            self.assertTrue(manifest["ic_final_owner"])
            self.assertTrue(manifest["production_real_subagents"])
            self.assertEqual(manifest["failed_required_specialists"], [])
            self.assertEqual(len(manifest["actual_subagents_run"]), len(fa_automation.AGENT_SPECIALISTS_EQUITY))
            report = fa_automation.generate_investment_report("MSFT for 3 years", intake, preflight, evidence_pack, specialists)
            self.assertTrue(report.splitlines()[0].startswith("Report status: Complete"))

    def test_required_specialist_timeout_stops_before_ic_and_stays_limited(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            run_dir = Path(temp_dir)
            (run_dir / "audit").mkdir()
            preflight = build_msft_source_preflight("MSFT", ["3 years"], "mock")
            evidence_pack = build_evidence_pack(preflight, freshness_required=False)
            intake = fa_automation.build_agent_intake_payload("MSFT for 3 years", ["3 years"], False)

            def fake_writer(run_dir, specialist_id, mode, intake, evidence_pack, preflight, prior_handoffs=None, deadline_monotonic=None):
                status = "error" if specialist_id == "financial-statement-analysis" else "ok"
                return {
                    "specialist_id": specialist_id,
                    "status": status,
                    "thread_or_run_id": f"thread-{specialist_id}" if status == "ok" else "",
                    "sdk_thread_id": f"thread-{specialist_id}" if status == "ok" else "",
                    "error": "timed out" if status == "error" else None,
                    "attempt_history": [{"attempt_no": 1, "status": status, "thread_or_run_id": "" if status == "error" else f"thread-{specialist_id}"}],
                    "handoff": {"Produced by": specialist_id, "Artifact": f"{specialist_id}.md", "consumed_handoff_ids": []},
                }

            with mock.patch.object(fa_automation, "write_specialist_artifacts", side_effect=fake_writer):
                results = fa_automation.run_agent_specialists(run_dir, "live", intake, evidence_pack, preflight)
            self.assertNotIn("investment-committee-agent", [item["specialist_id"] for item in results])
            fa_automation.write_run_manifest(run_dir, "MSFT for 3 years", "live", intake, preflight, evidence_pack, results)
            manifest = json.loads((run_dir / "audit" / "run_manifest.json").read_text(encoding="utf-8"))
            self.assertFalse(manifest["workflow_complete"])
            self.assertEqual(manifest["analysis_status"], "Limited")
            self.assertIn("financial-statement-analysis", manifest["failed_required_specialists"])
            self.assertIn("financial-statement-analysis", manifest["stop_reason"])
            self.assertNotIn("financial-statement-analysis", [item["specialist_id"] for item in manifest["actual_subagents_run"]])
            report = fa_automation.generate_investment_report("MSFT for 3 years", intake, preflight, evidence_pack, results)
            self.assertTrue(report.splitlines()[0].startswith("Report status: Limited"))

    def test_live_specialist_success_and_failure_manifest_truthfulness(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            run_dir = Path(temp_dir)
            (run_dir / "audit").mkdir()
            preflight = build_msft_source_preflight("MSFT", ["3 years"], "mock")
            evidence_pack = build_evidence_pack(preflight, freshness_required=False)
            intake = fa_automation.build_agent_intake_payload("MSFT for 3 years", ["3 years"], False)
            with mock.patch.object(
                fa_automation,
                "run_live_specialist_codex",
                return_value={
                    "status": "ok",
                    "response": "# Evidence handoff\nComplete",
                    "sdk_thread_id": "thread-ok",
                    "codex_execution_path": "financial_agent_system_codex_sdk_cli",
                    "codex_sdk_project_root": str(fa_automation.PROJECT_ROOT),
                    "codex_sdk_log_dir": str(run_dir / "sdk-log"),
                    "sdk_error": None,
                    "subprocess_exit_code": 0,
                    "timeout_seconds": 300,
                    "prompt_transport": "prompt_file",
                },
            ):
                success = fa_automation.write_specialist_artifacts(
                    run_dir,
                    "evidence-collector",
                    "live",
                    intake,
                    evidence_pack,
                    preflight,
                )
            with mock.patch.object(
                fa_automation,
                "run_live_specialist_codex",
                return_value={
                    "status": "error",
                    "error": "sdk failed",
                    "response": "",
                    "sdk_thread_id": "",
                    "codex_execution_path": "financial_agent_system_codex_sdk_cli",
                    "codex_sdk_project_root": str(fa_automation.PROJECT_ROOT),
                    "codex_sdk_log_dir": "",
                    "sdk_error": "sdk failed",
                    "subprocess_exit_code": 1,
                    "timeout_seconds": 300,
                    "prompt_transport": "prompt_file",
                },
            ):
                failure = fa_automation.write_specialist_artifacts(
                    run_dir,
                    "valuation-expectations-agent",
                    "live",
                    intake,
                    evidence_pack,
                    preflight,
                )
            fa_automation.write_run_manifest(run_dir, "MSFT for 3 years", "live", intake, preflight, evidence_pack, [success, failure])
            manifest = json.loads((run_dir / "audit" / "run_manifest.json").read_text(encoding="utf-8"))
            self.assertEqual([item["specialist_id"] for item in manifest["actual_subagents_run"]], ["evidence-collector"])
            self.assertEqual(manifest["attempted_subagents"][1]["thread_or_run_id"], "")
            self.assertEqual(manifest["attempted_subagents"][0]["thread_or_run_id"], "thread-ok")
            self.assertEqual(manifest["analysis_status"], "Limited")
            self.assertFalse(manifest["workflow_complete"])
            self.assertIn("sdk failed", manifest["sdk_errors"])
            self.assertEqual(manifest["prompt_transports"], ["prompt_file"])
            report = fa_automation.generate_investment_report(
                "MSFT for 3 years",
                intake,
                preflight,
                evidence_pack,
                [success, failure],
            )
            self.assertIn("Report status: Limited", report.splitlines()[0])

    def test_live_retry_history_preserves_failed_first_attempt_when_second_succeeds(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            run_dir = Path(temp_dir)
            (run_dir / "audit").mkdir()
            preflight = build_msft_source_preflight("MSFT", ["3 years"], "mock")
            evidence_pack = build_evidence_pack(preflight, freshness_required=False)
            intake = fa_automation.build_agent_intake_payload("MSFT for 3 years", ["3 years"], False)
            with mock.patch.object(
                fa_automation,
                "run_live_specialist_codex",
                side_effect=[
                    {
                        "status": "error",
                        "error": "first failed",
                        "response": "",
                        "sdk_thread_id": "",
                        "codex_execution_path": "financial_agent_system_codex_sdk_cli",
                        "codex_sdk_project_root": str(fa_automation.PROJECT_ROOT),
                        "codex_sdk_log_dir": "",
                        "sdk_error": "first failed",
                        "subprocess_exit_code": 1,
                        "timeout_seconds": 300,
                        "prompt_transport": "prompt_file",
                    },
                    {
                        "status": "ok",
                        "response": "# Evidence handoff\nComplete",
                        "sdk_thread_id": "thread-retry-ok",
                        "codex_execution_path": "financial_agent_system_codex_sdk_cli",
                        "codex_sdk_project_root": str(fa_automation.PROJECT_ROOT),
                        "codex_sdk_log_dir": str(run_dir / "sdk-log"),
                        "sdk_error": None,
                        "subprocess_exit_code": 0,
                        "timeout_seconds": 300,
                        "prompt_transport": "prompt_file",
                    },
                ],
            ):
                result = fa_automation.write_specialist_artifacts(
                    run_dir,
                    "evidence-collector",
                    "live",
                    intake,
                    evidence_pack,
                    preflight,
                )
            fa_automation.write_run_manifest(run_dir, "MSFT for 3 years", "live", intake, preflight, evidence_pack, [result])
            manifest = json.loads((run_dir / "audit" / "run_manifest.json").read_text(encoding="utf-8"))
            attempted = manifest["attempted_subagents"][0]
            self.assertEqual(attempted["status"], "ok")
            self.assertEqual(attempted["thread_or_run_id"], "thread-retry-ok")
            self.assertEqual([item["status"] for item in attempted["attempt_history"]], ["error", "ok"])
            self.assertEqual(attempted["attempt_history"][0]["thread_or_run_id"], "")
            self.assertEqual(attempted["attempt_history"][1]["thread_or_run_id"], "thread-retry-ok")
            self.assertEqual([item["specialist_id"] for item in manifest["actual_subagents_run"]], ["evidence-collector"])

    def test_timeout_audit_does_not_leak_full_prompt(self) -> None:
        secret_marker = "UNIQUE_PRIVATE_PROMPT_MARKER_12345"
        with tempfile.TemporaryDirectory() as temp_dir, mock.patch.dict(
            os.environ,
            {"FA_AUTOMATION_CODEX_SDK_PROJECT_ROOT": temp_dir, "FA_AUTOMATION_CODEX_SDK_TIMEOUT_SECONDS": "2"},
            clear=False,
        ), mock.patch.object(
            fa_automation.subprocess,
            "run",
            side_effect=subprocess.TimeoutExpired(cmd="npm.cmd", timeout=2),
        ):
            run_dir = Path(temp_dir) / "run"
            (run_dir / "audit").mkdir(parents=True)
            preflight = build_msft_source_preflight("MSFT", ["3 years"], "mock")
            preflight["subject_identity"]["raw_input"] = secret_marker
            preflight["resolver_result"]["raw_input"] = secret_marker
            evidence_pack = build_evidence_pack(preflight, freshness_required=False)
            intake = fa_automation.build_agent_intake_payload(f"MSFT for 3 years {secret_marker}", ["3 years"], False)
            result = fa_automation.write_specialist_artifacts(
                run_dir,
                "evidence-collector",
                "live",
                intake,
                evidence_pack,
                preflight,
            )
            fa_automation.write_run_manifest(
                run_dir,
                f"MSFT for 3 years {secret_marker}",
                "live",
                intake,
                preflight,
                evidence_pack,
                [result],
            )
            audit_text = "\n".join(
                [
                    (run_dir / "audit" / "specialists" / "evidence-collector" / "handoff.json").read_text(encoding="utf-8"),
                    (run_dir / "audit" / "specialists" / "evidence-collector" / "validation.json").read_text(encoding="utf-8"),
                    (run_dir / "audit" / "run_manifest.json").read_text(encoding="utf-8"),
                    json.dumps(result),
                ]
            )
            self.assertNotIn(secret_marker, audit_text)
            self.assertIn("<prompt-file>", audit_text)

    def test_ic_ok_without_consumed_handoffs_stays_preparatory(self) -> None:
        preflight = build_msft_source_preflight("MSFT", ["3 years"], "mock")
        evidence_pack = build_evidence_pack(preflight, freshness_required=False)
        intake = fa_automation.build_agent_intake_payload("MSFT на 3 года", ["3 года"], False)
        specialists = [
            {
                "specialist_id": "investment-committee-agent",
                "status": "ok",
                "handoff": {"consumed_handoff_ids": []},
            }
        ]
        report = fa_automation.generate_investment_report("MSFT на 3 года", intake, preflight, evidence_pack, specialists)
        self.assertIn("Что нужно для IC-сборки", report)
        self.assertNotIn("Итог IC-сборки", report)
        english_intake = fa_automation.build_agent_intake_payload("MSFT for 3 years", ["3 years"], False)
        english_report = fa_automation.generate_investment_report(
            "MSFT for 3 years",
            english_intake,
            preflight,
            evidence_pack,
            specialists,
        )
        self.assertIn("What is still needed for final assembly", english_report)
        self.assertIn("Preparatory view", english_report)
        self.assertNotIn("## IC synthesis", english_report)
        self.assertNotIn("## IC working view", english_report)
        self.assertNotIn("IC question", english_report)
        self.assertNotIn("IC working view", english_report)

    def test_reader_specialist_takeaways_filters_analysis_status_metadata(self) -> None:
        specialists = [
            {
                "specialist_id": "investment-committee-agent",
                "status": "ok",
                "handoff": {
                    "Produced by": "investment-committee-agent",
                    "main_findings": [
                        "Analysis Status: Limited - metadata should not appear in reader report.",
                        "The synthesis completed with all upstream handoffs and preserved the no-sizing boundary.",
                    ],
                },
            }
        ]
        takeaways = fa_automation.reader_specialist_takeaways(specialists, "en")
        self.assertEqual(len(takeaways), 1)
        self.assertNotIn("Analysis Status", takeaways[0])
        self.assertIn("synthesis completed", takeaways[0])

    def test_source_preflight_and_evidence_pack_shape(self) -> None:
        preflight = build_msft_source_preflight("MSFT", ["3 years"], "mock")
        validation = fa_automation.validate_source_preflight(preflight)
        pack = build_evidence_pack(preflight, freshness_required=True)

        self.assertEqual(validation["status"], "pass")
        self.assertTrue(preflight["summary"]["hard_gate_passed"])
        self.assertIn("claim_support_matrix", pack)
        self.assertIn("pre_ic_evidence_lock", pack)
        self.assertTrue(pack["claim_support_matrix"])
        self.assertTrue(all(record.get("retrieved_at") for record in preflight["source_records"]))

    def test_aapl_source_preflight_and_evidence_pack_shape(self) -> None:
        preflight = build_equity_source_preflight("AAPL", ["3 years"], "mock", ticker="AAPL")
        validation = fa_automation.validate_source_preflight(preflight)
        pack = build_evidence_pack(preflight, freshness_required=True)

        self.assertEqual(validation["status"], "pass")
        self.assertEqual(preflight["subject_identity"]["ticker"], "AAPL")
        self.assertEqual(preflight["subject_identity"]["cik"], "0000320193")
        self.assertTrue(validation["checks"]["sec_identity_matches_subject"])
        self.assertIn("AAPL AGENT workflow", pack["claim_support_matrix"][0]["claim"])
        self.assertTrue(preflight["summary"]["hard_gate_passed"])

    def test_mock_freshness_sensitive_dates_are_stamped_currently(self) -> None:
        preflight = build_equity_source_preflight("AAPL latest", ["Use latest public data if available"], "mock", ticker="AAPL")
        current_price = next(record for record in preflight["source_records"] if record["source_id"] == "current_price")
        public_news = next(record for record in preflight["source_records"] if record["source_id"] == "public_news")

        self.assertEqual(current_price["source_date"], date.today().isoformat())
        self.assertEqual(public_news["source_date"], date.today().isoformat())
        fa_automation.annotate_preflight_freshness(preflight, freshness_required=True)
        validation = fa_automation.validate_source_preflight(preflight)
        self.assertEqual(validation["status"], "pass")

    def test_live_non_us_proxy_sources_are_limited_not_fake_complete(self) -> None:
        preflight = build_equity_source_preflight("ASML.AS for 3 years", ["3 years"], "live", ticker="ASML.AS")
        validation = fa_automation.validate_source_preflight(preflight)
        pack = build_evidence_pack(preflight, freshness_required=False)

        self.assertEqual(validation["status"], "pass")
        self.assertIn("latest_10k", validation["partial_required"])
        self.assertIn("company_facts", validation["partial_required"])
        self.assertEqual(pack["evidence_readiness"], "Limited")
        provider_ids = [item["provider_id"] for item in preflight["provider_results"]]
        self.assertIn("stooq_history", provider_ids)
        self.assertIn("official_exchange_or_issuer_quote", provider_ids)

    def test_missing_required_source_blocks_preflight_validation(self) -> None:
        preflight = build_msft_source_preflight("MSFT", ["3 years"], "mock")
        for record in preflight["source_records"]:
            if record["source_id"] == "current_price":
                record["status"] = "error"
                record["error"] = "fixture failure"
        preflight["summary"] = {"missing_required": ["current_price"], "missing_important": [], "hard_gate_passed": False}
        validation = fa_automation.validate_source_preflight(preflight)
        self.assertEqual(validation["status"], "fail")
        self.assertIn("current_price", validation["missing_required"])

    def test_stale_current_price_blocks_freshness_dependent_preflight(self) -> None:
        preflight = build_msft_source_preflight("MSFT", ["latest"], "mock")
        for record in preflight["source_records"]:
            if record["source_id"] == "current_price":
                record["source_date"] = "2020-01-01"
        fa_automation.annotate_preflight_freshness(preflight, freshness_required=True)
        validation = fa_automation.validate_source_preflight(preflight)
        self.assertEqual(validation["status"], "fail")
        self.assertFalse(validation["checks"]["freshness_window_ok"])
        self.assertIn("current_price", validation["missing_required"])

    def test_stale_important_source_limits_but_does_not_hard_block(self) -> None:
        preflight = build_msft_source_preflight("MSFT", ["latest"], "mock")
        for record in preflight["source_records"]:
            if record["source_id"] == "public_news":
                record["source_date"] = "2020-01-01"
        fa_automation.annotate_preflight_freshness(preflight, freshness_required=True)
        validation = fa_automation.validate_source_preflight(preflight)
        pack = build_evidence_pack(preflight, freshness_required=True)

        self.assertEqual(validation["status"], "pass")
        self.assertFalse(validation["checks"]["freshness_window_ok"])
        self.assertIn("public_news", validation["missing_important"])
        self.assertEqual(pack["evidence_readiness"], "Limited")

    def test_missing_recent_8k_alone_does_not_block(self) -> None:
        preflight = build_equity_source_preflight("NVDA for 3 years", ["3 years"], "mock", ticker="NVDA")
        for record in preflight["source_records"]:
            if record["source_id"] == "recent_8k":
                record["status"] = "missing"
        preflight["summary"] = summarize_preflight(preflight)
        validation = fa_automation.validate_source_preflight(preflight)
        pack = build_evidence_pack(preflight, freshness_required=False)

        self.assertEqual(validation["status"], "pass")
        self.assertNotIn("recent_8k", validation["missing_required"])
        self.assertIn(pack["evidence_readiness"], {"Complete", "Limited"})

    def test_required_source_failure_stops_before_reader_report(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            reports_root = Path(temp_dir)
            old_reports = os.environ.get("FA_AUTOMATION_AGENT_REPORTS_ROOT")
            old_runs = os.environ.get("FA_AUTOMATION_AGENT_RUNS_DIR")
            original_preflight = fa_automation.build_equity_source_preflight

            def broken_preflight(*args, **kwargs):
                preflight = build_msft_source_preflight("MSFT", ["3 years"], "mock")
                for record in preflight["source_records"]:
                    if record["source_id"] == "current_price":
                        record["status"] = "error"
                        record["error"] = "fixture failure"
                preflight["summary"] = {
                    "missing_required": ["current_price"],
                    "missing_important": [],
                    "hard_gate_passed": False,
                }
                return preflight

            try:
                os.environ["FA_AUTOMATION_AGENT_REPORTS_ROOT"] = str(reports_root)
                os.environ["FA_AUTOMATION_AGENT_RUNS_DIR"] = str(reports_root / "runs")
                fa_automation.build_equity_source_preflight = broken_preflight
                exit_code = fa_automation.run_agent_run(
                    "MSFT for 3 years",
                    "mock",
                    [
                        "3 years",
                        "No current position",
                        "Quality compounder and valuation entry",
                        "Use latest public data if available",
                        "No portfolio context provided",
                    ],
                    None,
                    False,
                )
            finally:
                fa_automation.build_equity_source_preflight = original_preflight
                if old_reports is None:
                    os.environ.pop("FA_AUTOMATION_AGENT_REPORTS_ROOT", None)
                else:
                    os.environ["FA_AUTOMATION_AGENT_REPORTS_ROOT"] = old_reports
                if old_runs is None:
                    os.environ.pop("FA_AUTOMATION_AGENT_RUNS_DIR", None)
                else:
                    os.environ["FA_AUTOMATION_AGENT_RUNS_DIR"] = old_runs

            self.assertEqual(exit_code, 1)
            run_dir = self.latest_report_dir(reports_root)
            self.assertTrue((run_dir / "investment_report.md").is_file())
            self.assertTrue((run_dir / "audit" / "evidence_gap_memo.md").is_file())

    def test_non_equity_agent_routes_create_report_audit_and_validate(self) -> None:
        cases = [
            ("SPY for 5 years", "SPY", "etf_full_cycle", "etf-agent"),
            ("BTC for 3 years", "BTC", "crypto_full_cycle", "crypto-agent"),
            ("TLT bond ETF", "TLT", "fixed_income_full_cycle", "fixed-income-agent"),
            ("GLD gold ETF", "GLD", "commodity_full_cycle", "commodity-agent"),
            ("MSFT vs SPY vs BTC", "MSFT-SPY-BTC", "multi_asset_comparison", "portfolio-fit-agent"),
        ]
        for prompt, ticker, route, required_specialist in cases:
            with self.subTest(prompt=prompt), tempfile.TemporaryDirectory() as temp_dir:
                reports_root = Path(temp_dir)
                completed = self.run_cli(
                    ["agent-run", "--prompt", prompt, "--continue-with-baseline", "--mode", "mock"],
                    reports_root,
                )
                self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
                run_dir = self.latest_report_dir(reports_root, ticker)
                audit = run_dir / "audit"
                report_text = (run_dir / "investment_report.md").read_text(encoding="utf-8")
                manifest = json.loads((audit / "run_manifest.json").read_text(encoding="utf-8"))
                preflight = json.loads((audit / "source_preflight.json").read_text(encoding="utf-8"))

                self.assertEqual(manifest["selected_route"], route)
                self.assertEqual(preflight["selected_route"], route)
                self.assertTrue((audit / "evidence_pack.md").is_file())
                self.assertTrue((audit / "source_preflight.json").is_file())
                self.assertTrue((audit / "provider_results.json").is_file())
                self.assertTrue((audit / "specialists" / required_specialist / "handoff.json").is_file())
                self.assertIn("AGENT Workflow Review", report_text)
                self.assertIn("Evidence Status Summary", report_text)
                self.assertNotIn("Action Box", report_text)
                self.assertFalse(manifest["production_real_subagents"])

                validate = self.run_cli(["validate-agent-run", "--run-dir", str(run_dir)], reports_root)
                self.assertEqual(validate.returncode, 0, validate.stderr + validate.stdout)
                validation = json.loads((audit / "agent_run_validation.json").read_text(encoding="utf-8"))
                self.assertIn(validation["status"], {"pass", "limited"})
                self.assertTrue(validation["checks"]["subject_consistent_intake_preflight_manifest"])

    def test_agent_intake_spy_asks_exactly_five_and_stops(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            reports_root = Path(temp_dir)
            completed = self.run_cli(["agent-intake", "--prompt", "SPY for 5 years"], reports_root)

            self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
            numbered = [line for line in completed.stdout.splitlines() if line[:2] in {"1.", "2.", "3.", "4.", "5."}]
            self.assertEqual(len(numbered), 5)
            self.assertIn("etf_full_cycle", completed.stdout)
            self.assertFalse(list(reports_root.glob("SPY *")))

    def test_direct_specialist_run_routes_one_specialist_and_validates(self) -> None:
        cases = [
            ("RISK: Nvidia", "RISK", "risk-red-team-agent"),
            ("VAL: MSFT", "VAL", "valuation-expectations-agent"),
            ("ETF: SPY", "ETF", "etf-agent"),
            ("CRYPTO: BTC", "CRYPTO", "crypto-agent"),
            ("FI: TLT", "FI", "fixed-income-agent"),
            ("IC: MSFT", "IC", "investment-committee-agent"),
        ]
        for prompt, prefix, specialist_id in cases:
            with self.subTest(prompt=prompt), tempfile.TemporaryDirectory() as temp_dir:
                reports_root = Path(temp_dir)
                completed = self.run_cli(["specialist-run", "--prompt", prompt, "--mode", "mock"], reports_root)

                self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
                run_dir = self.latest_specialist_dir(reports_root, prefix)
                report_text = (run_dir / "specialist_report.md").read_text(encoding="utf-8")
                manifest = json.loads((run_dir / "audit" / "specialist_manifest.json").read_text(encoding="utf-8"))

                self.assertIn("Boundary: Not an IC Action", report_text)
                self.assertNotIn("Action Box", report_text)
                self.assertEqual(manifest["workflow"], "direct_specialist")
                self.assertEqual(manifest["prefix"], prefix)
                self.assertEqual(manifest["specialist_id"], specialist_id)
                self.assertEqual(len(manifest["attempted_specialists"]), 1)
                self.assertEqual(manifest["attempted_specialists"][0]["specialist_id"], specialist_id)
                self.assertFalse(manifest["final_action_allowed"])
                self.assertFalse(manifest["production_real_subagent"])
                self.assertTrue((run_dir / "audit" / "specialists" / specialist_id / "handoff.json").is_file())

                validate = self.run_cli(["validate-specialist-run", "--run-dir", str(run_dir)], reports_root)
                self.assertEqual(validate.returncode, 0, validate.stderr + validate.stdout)
                validation = json.loads((run_dir / "audit" / "specialist_run_validation.json").read_text(encoding="utf-8"))
                self.assertEqual(validation["status"], "pass")
                self.assertTrue(validation["checks"]["output_one_specialist_only"])

    def test_direct_specialist_rejects_missing_prefix(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            reports_root = Path(temp_dir)
            completed = self.run_cli(["specialist-run", "--prompt", "Nvidia risk", "--mode", "mock"], reports_root)

            self.assertNotEqual(completed.returncode, 0)
            self.assertIn("prompt must start with a supported specialist prefix", completed.stdout)
            self.assertFalse((reports_root / "_specialists").exists())

    def test_live_doctor_checks_prerequisites_and_writes_log(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            reports_root = Path(temp_dir)
            completed = self.run_cli(["live-doctor", "--skip-sdk-doctor"], reports_root)

            self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
            self.assertIn("Automation Lab live doctor: pass", completed.stdout)
            logs = sorted((reports_root / "live-doctor-runs").glob("*-live-doctor-*.json"))
            self.assertTrue(logs)
            report = json.loads(logs[-1].read_text(encoding="utf-8"))
            self.assertEqual(report["schema_version"], "automation_live_doctor.v1")
            self.assertEqual(report["status"], "pass")
            check_names = {item["name"] for item in report["checks"]}
            self.assertIn("Financial Agent System root exists", check_names)
            self.assertIn("Financial Agent Reports root writable", check_names)
            self.assertIn("Live specialist prompt transport is prompt-file", check_names)
            self.assertIn("agent-run", report["live_modes_covered"])
            self.assertIn("specialist-run", report["live_modes_covered"])

    def test_live_acceptance_manifest_tracks_smoke_and_live_gaps(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            reports_root = Path(temp_dir)
            doctor_dir = reports_root / "live-doctor-runs"
            doctor_dir.mkdir()
            (doctor_dir / "20260702T000000p0000-live-doctor-test.json").write_text(
                json.dumps({"schema_version": "automation_live_doctor.v1", "status": "pass"}),
                encoding="utf-8",
            )

            quick_root = reports_root / "quick-data"
            for ticker in ["MSFT", "SPY", "BTC", "TLT", "GLD", "MSFT-SPY-BTC"]:
                run_dir = quick_root / ticker
                run_dir.mkdir(parents=True)
                (run_dir / "source_snapshot.json").write_text(
                    json.dumps({"identity": {"ticker": ticker}, "mode": "mock", "timestamp": "2026-07-02T00:00:00+00:00"}),
                    encoding="utf-8",
                )
                (run_dir / "quick_answer.json").write_text(
                    json.dumps({"ticker": ticker, "mode": "mock", "status": "Limited"}),
                    encoding="utf-8",
                )
                (run_dir / "output_quality.json").write_text(json.dumps({"status": "pass"}), encoding="utf-8")

            for route in fa_automation.AGENT_ROUTE_CARDS:
                run_dir = reports_root / f"{route} 2026-07-02 0000"
                audit = run_dir / "audit"
                audit.mkdir(parents=True)
                (run_dir / "investment_report.md").write_text("Report status: Limited\n", encoding="utf-8")
                (audit / "run_manifest.json").write_text(
                    json.dumps(
                        {
                            "workflow": "agent_run",
                            "mode": "mock",
                            "selected_route": route,
                            "subject": route,
                            "workflow_complete": True,
                            "analysis_status": "Complete",
                            "production_real_subagents": False,
                            "sdk_thread_ids": [],
                            "created_at": "2026-07-02T00:00:00+00:00",
                        }
                    ),
                    encoding="utf-8",
                )
                (audit / "agent_run_validation.json").write_text(json.dumps({"status": "pass"}), encoding="utf-8")

            specialist_root = reports_root / "_specialists"
            for prefix, specialist_id in fa_automation.SPECIALIST_COMMANDS.items():
                run_dir = specialist_root / f"{prefix}-SUBJECT 2026-07-02 0000"
                audit = run_dir / "audit"
                audit.mkdir(parents=True)
                (run_dir / "specialist_report.md").write_text("Boundary: Not an IC Action\n", encoding="utf-8")
                (audit / "specialist_manifest.json").write_text(
                    json.dumps(
                        {
                            "workflow": "direct_specialist",
                            "mode": "mock",
                            "prefix": prefix,
                            "specialist_id": specialist_id,
                            "actual_specialists_run": [{"specialist_id": specialist_id, "status": "ok", "sdk_thread_id": ""}],
                            "production_real_subagent": False,
                            "boundary": "Not an IC Action",
                        }
                    ),
                    encoding="utf-8",
                )
                (audit / "specialist_run_validation.json").write_text(json.dumps({"status": "pass"}), encoding="utf-8")

            completed = self.run_cli(["live-acceptance"], reports_root)
            self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
            self.assertIn("Live acceptance status: Limited", completed.stdout)
            logs = sorted((reports_root / "live-acceptance-runs").glob("*-live-acceptance-*.json"))
            self.assertTrue(logs)
            report = json.loads(logs[-1].read_text(encoding="utf-8"))
            self.assertEqual(report["schema_version"], "automation_live_acceptance.v1")
            self.assertEqual(report["status"], "pass")
            self.assertEqual(report["live_acceptance_status"], "Limited")
            self.assertFalse(report["smoke_gaps"])
            self.assertIn("agent_route:equity_full_cycle", report["live_gaps"])
            self.assertIn("specialist_prefix:RISK", report["live_gaps"])

            require_live = self.run_cli(["live-acceptance", "--require-live"], reports_root)
            self.assertNotEqual(require_live.returncode, 0)
            self.assertIn("Live acceptance status: Limited", require_live.stdout)


if __name__ == "__main__":
    unittest.main()
