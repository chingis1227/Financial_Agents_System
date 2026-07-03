"""Deterministic output-quality checks for QUICK answers.

TASK-010 keeps QUICK validation rule-based: no LLM judge, no network calls,
and no Evidence Collector claims. The checks here evaluate whether a generated
Quick Take is safe to display as a user-facing answer.
"""

from __future__ import annotations

import re
from typing import Any

OUTPUT_QUALITY_SCHEMA_VERSION = "quick_output_quality.v1"
OUTPUT_QUALITY_REQUIRED_CHECKS = {
    "source_note_present",
    "freshness_note_present",
    "risk_specificity_ok",
    "no_hidden_action_language",
    "no_overconfidence",
    "status_matches_data_quality",
    "limitations_visible",
    "final_ic_action_unavailable",
    "no_report_or_audit_claim",
    "no_agent_execution_claim",
}

DIRECT_ACTION_PATTERN = re.compile(
    r"(?i)\b(buy|sell|hold|add|trim|exit|buying|selling|holding|adding|trimming|exiting)\b"
)
ACTION_BOX_PATTERN = re.compile(r"(?i)\bAction\s+Box\b|^\s*(Recommendation|Final Action)\s*:", re.MULTILINE)
SIZING_PATTERN = re.compile(
    r"(?i)\b\d+(?:\.\d+)?\s*(?:%|percent|shares?)\b|\$\s*\d|\b(?:allocate|allocation|position sizing|position size|exact sizing)\b"
)
REPORT_AUDIT_PATTERN = re.compile(
    r"(?i)\binvestment_report\.md\b|\baudit/\b|\baudit\\\b|\baudit\s+folder\b|\baudit\s+directory\b"
)
AGENT_CLAIM_PATTERN = re.compile(
    r"(?i)\b(full\s+)?AGENT\b.*\b(ran|executed|completed|finished)\b|"
    r"\bsub[- ]?agents?\b.*\b(ran|executed|completed|finished)\b"
)
HIDDEN_ACTION_PATTERN = re.compile(
    r"(?i)\b(start\s+a\s+position|build\s+a\s+position|scale\s+into|accumulate|good\s+entry|"
    r"entry\s+point|reduce\s+exposure|increase\s+exposure|avoid\b|not\s+investable|"
    r"suitable\s+to\s+own\s+now|worth\s+owning|worth\s+accumulating)\b"
)
OVERCONFIDENCE_HARD_PATTERN = re.compile(
    r"(?i)\b(guaranteed|risk[- ]?free|definitely|certainly|safe\s+choice|cannot\s+lose)\b"
)
OVERCONFIDENCE_SOFT_PATTERN = re.compile(
    r"(?i)\b(attractive|compelling|strong\s+opportunity|strong\s+setup|favorable|high\s+conviction|should\s+outperform)\b"
)
GENERIC_RISK_PATTERN = re.compile(
    r"(?i)\b(markets?\s+can\s+go\s+down|invest(?:ing|ments?)\s+(?:has|have|carry|carries)\s+risk|"
    r"volatility\s+exists|prices?\s+may\s+change)\b"
)

TICKER_RISK_KEYWORDS = {
    "MSFT": [
        "ai capex",
        "azure",
        "cloud",
        "valuation multiple",
        "enterprise software",
        "software demand",
        "capex expectations",
    ],
    "SPY": [
        "broad equity",
        "index concentration",
        "mega-cap",
        "multiple risk",
        "equity drawdown",
    ],
    "BTC": [
        "crypto volatility",
        "regulatory",
        "custody",
        "liquidity",
        "drawdown",
    ],
    "TLT": [
        "duration",
        "rate path",
        "long rates",
        "inflation",
        "term premium",
        "curve",
    ],
    "GLD": [
        "real yields",
        "usd",
        "gold price",
        "commodity exposure",
        "gold etf",
        "real-rate",
    ],
    "MSFT-SPY-BTC": [
        "company-specific equity risk",
        "broad equity beta",
        "crypto volatility",
        "cross-asset",
    ],
}

ASSET_CLASS_RISK_KEYWORDS = {
    "equity": ["equity", "valuation", "earnings", "multiple", "company", "software", "cloud"],
    "etf": ["etf", "index", "fund", "equity", "concentration", "drawdown"],
    "crypto": ["crypto", "volatility", "regulatory", "custody", "liquidity", "drawdown"],
    "bond_etf": ["duration", "rates", "rate", "yield", "curve", "inflation", "bond"],
    "commodity_etf": ["commodity", "gold", "real yields", "usd", "real-rate"],
    "multi_asset_comparison": ["comparison", "cross-asset", "equity", "crypto", "beta"],
}


def _section_text(answer: str, section: str) -> str:
    pattern = re.compile(
        rf"(?ims)^\s*{re.escape(section)}\s*$\s*(.*?)(?=^\s*[A-Z][A-Za-z /]+?\s*$|\Z)"
    )
    match = pattern.search(answer.strip())
    return match.group(1).strip() if match else ""


def _line_value(answer: str, label: str) -> str:
    match = re.search(rf"(?im)^\s*{re.escape(label)}\s*$", answer)
    if match:
        return _section_text(answer, label)
    return ""


def _contains_any(text: str, keywords: list[str]) -> bool:
    lowered = text.lower()
    return any(keyword.lower() in lowered for keyword in keywords)


def _identity_slug(identity: dict[str, Any]) -> str:
    ticker = str(identity.get("ticker") or "").upper()
    if identity.get("security_type") == "multi_asset_comparison":
        components = identity.get("components") or []
        tickers = [str(component.get("ticker", "")).upper() for component in components if isinstance(component, dict)]
        return "-".join(tickers) or ticker
    return ticker


def _risk_specificity(risk_text: str, identity: dict[str, Any]) -> str:
    if not risk_text.strip():
        return "missing"
    if GENERIC_RISK_PATTERN.search(risk_text):
        return "generic"
    slug = _identity_slug(identity)
    if slug in TICKER_RISK_KEYWORDS and _contains_any(risk_text, TICKER_RISK_KEYWORDS[slug]):
        return "ticker_specific"
    security_type = str(identity.get("security_type") or "")
    if _contains_any(risk_text, ASSET_CLASS_RISK_KEYWORDS.get(security_type, [])):
        return "asset_class_specific"
    return "generic"


def _specificity_ok(actual: str, required: str) -> bool:
    if required == "ticker_specific":
        return actual == "ticker_specific"
    if required == "asset_class_specific":
        return actual in {"ticker_specific", "asset_class_specific"}
    return actual not in {"missing", "generic"}


def _status_matches_data_quality(answer_status: str | None, source_snapshot: dict[str, Any], data_quality: dict[str, Any]) -> bool:
    if answer_status != data_quality.get("status"):
        return False
    if answer_status == "Preliminary":
        missing = set(data_quality.get("missing_inputs") or [])
        if missing:
            return False
        if data_quality.get("freshness_limitations"):
            return False
        if source_snapshot.get("answer_freshness_required"):
            return False
        freshness_by_component = data_quality.get("freshness_by_component") or {}
        price_status = (freshness_by_component.get("price") or {}).get("status")
        if price_status in {"Unknown", "Stale but Usable", "Not Found"}:
            return False
    if answer_status == "Limited":
        return bool(data_quality.get("missing_inputs") or data_quality.get("freshness_limitations"))
    if answer_status == "Blocked":
        return bool(data_quality.get("reason_for_status"))
    return answer_status in {"Preliminary", "Limited", "Blocked"}


def _limitations_visible(answer: str, data_quality: dict[str, Any]) -> bool:
    text = answer.lower()
    if data_quality.get("status") in {"Limited", "Blocked"}:
        return bool(data_quality.get("reason_for_status")) and (
            "missing" in text or "freshness" in text or "limited" in text or "blocked" in text
        )
    return "quick" in text and ("not evidence collector" in text or "not an evidence collector" in text)


def _final_ic_action_unavailable(answer: str) -> bool:
    return bool(re.search(r"(?im)^Final IC Action:\s*Unavailable in QUICK\.\s*$", answer))


def assess_quick_output_quality(
    answer: str,
    source_snapshot: dict[str, Any],
    data_quality: dict[str, Any],
) -> dict[str, Any]:
    """Return a deterministic quality card for a generated Quick Take."""
    hard_failures: list[str] = []
    soft_failures: list[str] = []
    warnings: list[str] = []

    text = answer.strip()
    status_match = re.search(r"(?im)^Status:\s*(Preliminary|Limited|Blocked)\s*$", text)
    quick_status = status_match.group(1) if status_match else data_quality.get("status")
    mode = str(source_snapshot.get("mode") or "")
    identity = source_snapshot.get("asset_identity") or {}

    source_note_text = _line_value(text, "Source note")
    freshness_note_text = _line_value(text, "Freshness note")
    risk_text = _section_text(text, "Main risks / limits")
    required_specificity = "ticker_specific" if mode == "mock" else "asset_class_specific"
    specificity = _risk_specificity(risk_text, identity)
    risk_specificity_ok = True if quick_status == "Blocked" else _specificity_ok(specificity, required_specificity)

    if ACTION_BOX_PATTERN.search(text):
        hard_failures.append("forbidden_action_box_or_action_label")
    direct_action_text = re.sub(r"(?im)^Final IC Action:\s*Unavailable in QUICK\.\s*$", "", text)
    if DIRECT_ACTION_PATTERN.search(direct_action_text):
        hard_failures.append("forbidden_direct_final_action_language")
    if SIZING_PATTERN.search(text):
        hard_failures.append("forbidden_exact_sizing_or_trade_instruction")
    if REPORT_AUDIT_PATTERN.search(text):
        hard_failures.append("forbidden_report_or_audit_claim")
    if AGENT_CLAIM_PATTERN.search(text):
        hard_failures.append("forbidden_agent_execution_claim")
    if OVERCONFIDENCE_HARD_PATTERN.search(text):
        hard_failures.append("hard_overconfidence_language")

    if not source_note_text:
        soft_failures.append("missing_source_note")
    elif "public" not in source_note_text.lower() or "not evidence collector" not in source_note_text.lower():
        soft_failures.append("source_note_missing_public_or_evidence_boundary")

    if not freshness_note_text:
        soft_failures.append("missing_freshness_note")
    elif data_quality.get("freshness_limitations") and "freshness" not in freshness_note_text.lower():
        soft_failures.append("freshness_note_missing_limitation")

    if not risk_specificity_ok:
        soft_failures.append("risk_not_specific_enough")

    if HIDDEN_ACTION_PATTERN.search(text):
        soft_failures.append("hidden_action_language")
    if OVERCONFIDENCE_SOFT_PATTERN.search(text):
        soft_failures.append("soft_overconfidence_language")
    if not _status_matches_data_quality(quick_status, source_snapshot, data_quality):
        soft_failures.append("status_mismatch_with_data_quality")
    if not _limitations_visible(text, data_quality):
        soft_failures.append("limitations_not_visible")
    if not _final_ic_action_unavailable(text):
        hard_failures.append("final_ic_action_not_explicitly_unavailable")

    checks = {
        "source_note_present": bool(source_note_text),
        "freshness_note_present": bool(freshness_note_text),
        "risk_specificity_ok": risk_specificity_ok,
        "no_hidden_action_language": not HIDDEN_ACTION_PATTERN.search(text),
        "no_overconfidence": not (OVERCONFIDENCE_HARD_PATTERN.search(text) or OVERCONFIDENCE_SOFT_PATTERN.search(text)),
        "status_matches_data_quality": _status_matches_data_quality(quick_status, source_snapshot, data_quality),
        "limitations_visible": _limitations_visible(text, data_quality),
        "final_ic_action_unavailable": _final_ic_action_unavailable(text),
        "no_report_or_audit_claim": not REPORT_AUDIT_PATTERN.search(text),
        "no_agent_execution_claim": not AGENT_CLAIM_PATTERN.search(text),
    }
    status = "pass" if not hard_failures and not soft_failures else "fail"
    reason = "Output quality checks passed." if status == "pass" else quality_failure_summary(
        {"hard_failures": hard_failures, "soft_failures": soft_failures}
    )

    return {
        "schema_version": OUTPUT_QUALITY_SCHEMA_VERSION,
        "status": status,
        "mode": mode,
        "quick_status": quick_status,
        "hard_failures": hard_failures,
        "soft_failures": soft_failures,
        "warnings": warnings,
        "checks": checks,
        "risk_assessment": {
            "risk_text": risk_text,
            "specificity": specificity,
            "required_specificity": required_specificity,
        },
        "source_note": {
            "present": bool(source_note_text),
            "text": source_note_text,
        },
        "freshness_note": {
            "present": bool(freshness_note_text),
            "text": freshness_note_text,
        },
        "reason": reason,
    }


def is_output_quality_pass(output_quality: dict[str, Any]) -> bool:
    return output_quality.get("status") == "pass" and not output_quality.get("hard_failures") and not output_quality.get("soft_failures")


def quality_failure_summary(output_quality: dict[str, Any]) -> str:
    hard = list(output_quality.get("hard_failures") or [])
    soft = list(output_quality.get("soft_failures") or [])
    if hard:
        return "Hard output-quality failure: " + ", ".join(map(str, hard))
    if soft:
        return "Soft output-quality failure: " + ", ".join(map(str, soft))
    return "No output-quality failures."
