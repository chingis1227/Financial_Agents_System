"""Quality, status, and freshness rules for QUICK snapshots."""

from __future__ import annotations

import re
from datetime import datetime, timezone
from typing import Any

ANSWER_FRESHNESS_POSITIVE_PATTERN = re.compile(
    r"(?i)\b(?:use|need|needs|require|requires|required|include|prefer|pull|check)\b"
    r".{0,50}\b(?:current|latest|fresh|today|news|price|timestamped|public current)\b|"
    r"\b(?:current|latest|fresh|today|news|price|timestamped)\b"
    r".{0,50}\b(?:required|needed|sources?|data|context|available)\b|"
    r"\byes\b.{0,50}\b(?:current|latest|fresh|today|news|price|timestamped)\b"
)

ANSWER_FRESHNESS_NEGATIVE_PATTERN = re.compile(
    r"(?i)\b(?:no|not|without|don't|do not|none)\s+"
    r"(?:need\s+|require\s+)?(?:current|latest|fresh|today|timestamped)"
    r".{0,25}\b(?:data|sources?|context|freshness|need|requirement|market data)\b|"
    r"\bnot\s+freshness-dependent\b"
)

FRESHNESS_PROMPT_PATTERN = re.compile(
    r"(?i)\b(today|now|latest|recent|news|earnings|price action|market action|"
    r"this week|this month|real[- ]?time|pre[- ]?market|after[- ]?hours)\b|"
    r"\bcurrent\s+(price|market|data|quote|news|earnings|setup|valuation)\b|"
    r"\b(сегодня|сейчас|последн(?:ие|яя|ий|их)|свеж(?:ие|ая|ий|их)|новост(?:и|ей)|"
    r"отч[её]тност(?:ь|и)|динамик[аи]\s+цен|текущ(?:ая|ие|ий|их))\b"
)


def is_freshness_dependent(prompt: str) -> bool:
    return bool(FRESHNESS_PROMPT_PATTERN.search(prompt))


def answers_require_freshness(answers: list[str]) -> bool:
    """Return True when any individual answer asks for current/latest data.

    Evaluate per answer so text such as "No current position" cannot suppress a
    separate answer like "Need latest public data". A negative answer only cancels
    freshness when it appears in the same answer that mentions freshness.
    """
    for answer in answers:
        if ANSWER_FRESHNESS_POSITIVE_PATTERN.search(answer) and not ANSWER_FRESHNESS_NEGATIVE_PATTERN.search(answer):
            return True
    return False


def quick_freshness_required(source_snapshot: dict[str, Any]) -> bool:
    prompt = source_snapshot.get("normalized_prompt", "")
    return is_freshness_dependent(prompt) or bool(source_snapshot.get("answer_freshness_required"))


def _parse_date(value: Any) -> datetime | None:
    if not isinstance(value, str) or not value.strip():
        return None
    try:
        return datetime.fromisoformat(value[:10]).replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def _price_freshness_from_date(price_date: Any) -> dict[str, Any]:
    parsed_price_date = _parse_date(price_date)
    if parsed_price_date is None:
        return {"status": "Unknown", "reason": "price date missing", "source_date": price_date}
    age_days = (datetime.now(timezone.utc).date() - parsed_price_date.date()).days
    if age_days <= 7:
        return {"status": "Current", "reason": f"price date is {age_days} calendar days old", "source_date": price_date}
    return {"status": "Stale but Usable", "reason": f"price date is {age_days} calendar days old", "source_date": price_date}


def _roll_up_price_status(component_statuses: list[dict[str, Any]]) -> dict[str, Any]:
    if not component_statuses:
        return {"status": "Unknown", "reason": "component prices missing", "source_date": None, "components": []}
    statuses = {component.get("status") for component in component_statuses}
    if "Unknown" in statuses:
        status = "Unknown"
    elif "Stale but Usable" in statuses:
        status = "Stale but Usable"
    else:
        status = "Current"
    return {
        "status": status,
        "reason": "comparison price freshness is the weakest component freshness",
        "source_date": None,
        "components": component_statuses,
    }


def freshness_by_component(source_snapshot: dict[str, Any]) -> dict[str, dict[str, Any]]:
    data = source_snapshot.get("data") or {}
    price = data.get("price") or {}
    component_price_freshness: list[dict[str, Any]] = []
    if isinstance(price, dict) and isinstance(price.get("components"), list):
        for component in price.get("components") or []:
            if not isinstance(component, dict):
                continue
            component_ticker = component.get("ticker")
            component_price = component.get("price") if isinstance(component.get("price"), dict) else {}
            component_status = _price_freshness_from_date(component_price.get("date"))
            component_status = {"ticker": component_ticker, **component_status}
            component_price_freshness.append(component_status)
        price_freshness = _roll_up_price_status(component_price_freshness)
    else:
        price_date = price.get("date") if isinstance(price, dict) else None
        price_freshness = _price_freshness_from_date(price_date)

    filings = data.get("filings") or []
    filing_date = None
    if isinstance(filings, list) and filings and isinstance(filings[0], dict):
        filing_date = filings[0].get("filing_date")
    filing_status = "Recent" if filing_date else "Unknown"

    static_present = any(bool(data.get(key)) for key in ("asset_context", "comparison_context"))

    return {
        "price": price_freshness,
        "filings": {"status": filing_status, "reason": "filing-driven freshness" if filing_date else "filing date missing", "source_date": filing_date},
        "static_context": {"status": "Stale but Usable" if static_present else "Not Found", "reason": "structural context only; not current evidence"},
    }


def provider_quality_summary(source_snapshot: dict[str, Any]) -> dict[str, Any]:
    results = [r for r in source_snapshot.get("provider_results") or [] if isinstance(r, dict)]
    counts: dict[str, int] = {}
    quality_counts: dict[str, int] = {}
    for result in results:
        counts[str(result.get("status"))] = counts.get(str(result.get("status")), 0) + 1
        quality_counts[str(result.get("quality_level"))] = quality_counts.get(str(result.get("quality_level")), 0) + 1
    return {
        "result_status_counts": counts,
        "quality_level_counts": quality_counts,
        "providers_attempted": len([r for r in results if r.get("status") != "disabled"]),
        "disabled_api_slots": len([r for r in results if r.get("status") == "disabled"]),
    }


def assess_quick_data_quality(source_snapshot: dict[str, Any]) -> dict[str, Any]:
    missing = list(source_snapshot.get("missing") or [])
    identity = source_snapshot.get("asset_identity")
    retrieved = source_snapshot.get("retrieved") or {}
    freshness_required = quick_freshness_required(source_snapshot)
    component_freshness = freshness_by_component(source_snapshot)

    price_freshness = component_freshness.get("price", {}).get("status")
    # Mock fixtures are deterministic test inputs; live/public stale or undated prices downgrade to Limited.
    if (
        source_snapshot.get("mode") != "mock"
        and retrieved.get("price")
        and price_freshness in {"Unknown", "Stale but Usable"}
        and "price_freshness" not in missing
    ):
        missing.append("price_freshness")

    if not identity:
        status = "Blocked"
        reason = "Asset identity is missing, so even a quick filter would be unsupported."
    elif not any(bool(retrieved.get(key)) for key in ("filings", "price", "recent_events", "valuation_context", "risk_signal", "asset_context", "comparison_context")):
        status = "Blocked"
        reason = "Identity exists, but no supporting public-data component was obtained."
    elif missing or freshness_required:
        status = "Limited"
        reason = "Quick answer allowed, but missing or freshness-sensitive inputs prevent a confident preliminary view."
    else:
        status = "Preliminary"
        reason = "Asset identity and the minimum quick public-data snapshot are available."

    freshness_limitations = []
    if "price" in missing:
        freshness_limitations.append("price missing")
    if "price_freshness" in missing:
        freshness_limitations.append("price stale or missing source date")
    if "recent_events" in missing:
        freshness_limitations.append("recent events missing")
    if "valuation_context" in missing:
        freshness_limitations.append("valuation context missing")
    if is_freshness_dependent(source_snapshot.get("normalized_prompt", "")):
        freshness_limitations.append("prompt asks for current/latest context")
    if source_snapshot.get("answer_freshness_required"):
        freshness_limitations.append("user answers ask for current/latest context")

    return {
        "status": status,
        "missing_inputs": missing,
        "freshness_limitations": freshness_limitations,
        "reason_for_status": reason,
        "quick_answer_allowed": status in {"Preliminary", "Limited"},
        "access_status": source_snapshot.get("access_status"),
        "freshness_status": source_snapshot.get("freshness_status"),
        "provider_quality_summary": provider_quality_summary(source_snapshot),
        "freshness_by_component": component_freshness,
        "source_scope": source_snapshot.get("source_scope", "Public-Data Only"),
        "evidence_alignment": source_snapshot.get("evidence_alignment", "Quick snapshot only; not an Evidence Collector evidence_pack"),
    }


def format_missing_inputs(missing_inputs: list[str]) -> str:
    if not missing_inputs:
        return "None in the quick snapshot"
    return ", ".join(missing_inputs)


def format_quick_limitations(data_quality: dict[str, Any]) -> str:
    missing_inputs = list(data_quality.get("missing_inputs") or [])
    freshness_limitations = list(data_quality.get("freshness_limitations") or [])
    parts = []
    if missing_inputs:
        parts.append("missing inputs: " + ", ".join(missing_inputs))
    if freshness_limitations:
        parts.append("freshness limits: " + ", ".join(freshness_limitations))
    if not parts:
        return "missing inputs: None in the quick snapshot"
    return "; ".join(parts)
