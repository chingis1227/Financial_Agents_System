"""Deterministic financial claim extraction for parser MVP."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any


METRIC_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("Revenue", re.compile(r"\b(revenue|sales)\b", re.IGNORECASE)),
    ("Gross profit", re.compile(r"\bgross profit\b", re.IGNORECASE)),
    ("Gross margin", re.compile(r"\bgross margin\b", re.IGNORECASE)),
    ("Operating income", re.compile(r"\boperating income\b", re.IGNORECASE)),
    ("Operating margin", re.compile(r"\boperating margin\b", re.IGNORECASE)),
    ("Adjusted EBITDA", re.compile(r"\badjusted ebitda\b", re.IGNORECASE)),
    ("EBITDA", re.compile(r"\bebitda\b", re.IGNORECASE)),
    ("Net income", re.compile(r"\bnet income\b", re.IGNORECASE)),
    ("Adjusted EPS", re.compile(r"\badjusted eps\b", re.IGNORECASE)),
    ("EPS", re.compile(r"\b(eps|earnings per share)\b", re.IGNORECASE)),
    ("Free cash flow", re.compile(r"\b(free cash flow|fcf)\b", re.IGNORECASE)),
    ("Operating cash flow", re.compile(r"\boperating cash flow\b", re.IGNORECASE)),
    ("Capex", re.compile(r"\b(capex|capital expenditures?)\b", re.IGNORECASE)),
    ("Cash", re.compile(r"\bcash\b", re.IGNORECASE)),
    ("Debt", re.compile(r"\bdebt\b", re.IGNORECASE)),
    ("Guidance", re.compile(r"\b(guidance|outlook|expects?|forecast|projects?)\b", re.IGNORECASE)),
    ("Growth", re.compile(r"\b(yoy|year-over-year|qoq|quarter-over-quarter|growth|grew|increased|declined)\b", re.IGNORECASE)),
    ("Users", re.compile(r"\b(users|subscribers|customers|units)\b", re.IGNORECASE)),
    ("AUM", re.compile(r"\b(aum|assets under management)\b", re.IGNORECASE)),
    ("NAV", re.compile(r"\bnav\b", re.IGNORECASE)),
    ("Expense ratio", re.compile(r"\bexpense ratio\b", re.IGNORECASE)),
    ("Yield", re.compile(r"\byield\b", re.IGNORECASE)),
    ("Duration", re.compile(r"\bduration\b", re.IGNORECASE)),
    ("Spread", re.compile(r"\bspread\b", re.IGNORECASE)),
    ("TVL", re.compile(r"\b(tvl|total value locked)\b", re.IGNORECASE)),
    ("Hashrate", re.compile(r"\bhash\s?rate\b", re.IGNORECASE)),
    ("Fees", re.compile(r"\bfees\b", re.IGNORECASE)),
    ("Production", re.compile(r"\bproduction\b", re.IGNORECASE)),
    ("Inventory", re.compile(r"\binventory|inventories\b", re.IGNORECASE)),
)

MONEY_RE = re.compile(
    r"(?P<currency>[$€£])\s*(?P<number>[+-]?\d[\d,]*(?:\.\d+)?)\s*(?P<scale>billion|bn|million|mm|thousand|k)?",
    re.IGNORECASE,
)
PERCENT_RE = re.compile(r"(?P<number>[+-]?\d[\d,]*(?:\.\d+)?)\s*(?:%|percent)", re.IGNORECASE)
PLAIN_SCALED_RE = re.compile(
    r"(?P<number>[+-]?\d[\d,]*(?:\.\d+)?)\s*(?P<scale>billion|bn|million|mm|thousand|k)\b",
    re.IGNORECASE,
)
PERIOD_RE = re.compile(
    r"\b("
    r"Q[1-4]\s*(?:FY)?\s*20\d{2}|"
    r"FY\s*20\d{2}|"
    r"fiscal\s+(?:year\s+)?20\d{2}|"
    r"(?:first|second|third|fourth)\s+quarter\s+20\d{2}|"
    r"full[-\s]?year\s+20\d{2}|"
    r"20\d{2}"
    r")\b",
    re.IGNORECASE,
)
COMPARISON_RE = re.compile(r"\b(YoY|year-over-year|QoQ|quarter-over-quarter)\b", re.IGNORECASE)

CURRENCY_MAP = {"$": "USD", "€": "EUR", "£": "GBP"}
SCALE_MAP = {
    "billion": 1.0,
    "bn": 1.0,
    "million": 0.001,
    "mm": 0.001,
    "thousand": 0.000001,
    "k": 0.000001,
}


@dataclass(frozen=True)
class NormalizedNumber:
    value: float
    unit: str
    original_text: str
    ambiguous: bool = False


@dataclass(frozen=True)
class NumberCandidate:
    start: int
    end: int
    kind: str
    raw_number: float
    original_text: str
    currency: str | None = None
    scale: str | None = None


@dataclass(frozen=True)
class MetricMatch:
    metric: str
    start: int
    end: int


def _split_sentences(text: str) -> list[str]:
    chunks = re.split(r"(?<=[.!?])\s+|\n+", text)
    return [chunk.strip(" -\t") for chunk in chunks if chunk.strip(" -\t")]


def _number_candidates(sentence: str) -> list[NumberCandidate]:
    candidates: list[NumberCandidate] = []
    for match in MONEY_RE.finditer(sentence):
        candidates.append(
            NumberCandidate(
                start=match.start(),
                end=match.end(),
                kind="money",
                raw_number=float(match.group("number").replace(",", "")),
                original_text=match.group(0),
                currency=CURRENCY_MAP.get(match.group("currency"), match.group("currency")),
                scale=(match.group("scale") or "").lower() or None,
            )
        )
    money_spans = [(candidate.start, candidate.end) for candidate in candidates]
    for match in PERCENT_RE.finditer(sentence):
        if any(start <= match.start() < end for start, end in money_spans):
            continue
        candidates.append(
            NumberCandidate(
                start=match.start(),
                end=match.end(),
                kind="percent",
                raw_number=float(match.group("number").replace(",", "")),
                original_text=match.group(0),
            )
        )
    occupied = [(candidate.start, candidate.end) for candidate in candidates]
    for match in PLAIN_SCALED_RE.finditer(sentence):
        if any(not (match.end() <= start or match.start() >= end) for start, end in occupied):
            continue
        candidates.append(
            NumberCandidate(
                start=match.start(),
                end=match.end(),
                kind="scaled",
                raw_number=float(match.group("number").replace(",", "")),
                original_text=match.group(0),
                scale=match.group("scale").lower(),
            )
        )
    return sorted(candidates, key=lambda candidate: candidate.start)


def _candidate_allowed(candidate: NumberCandidate, metric: str) -> bool:
    metric_lower = metric.lower()
    if candidate.kind == "percent":
        return "margin" in metric_lower or metric in {"Growth", "Yield", "Expense ratio", "Spread", "Guidance"}
    if candidate.kind == "money":
        return metric not in {"Growth", "Gross margin", "Operating margin", "Yield", "Expense ratio", "Spread"}
    if candidate.kind == "scaled":
        return metric not in {"EPS", "Adjusted EPS", "Growth", "Gross margin", "Operating margin", "Yield", "Expense ratio", "Spread"}
    return False


def _normalize_candidate(candidate: NumberCandidate, metric: str) -> NormalizedNumber:
    if candidate.kind == "percent":
        return NormalizedNumber(candidate.raw_number, "percent", candidate.original_text)
    if candidate.kind == "money":
        currency = candidate.currency or "currency"
        if metric in {"EPS", "Adjusted EPS"}:
            return NormalizedNumber(candidate.raw_number, f"{currency} per share", candidate.original_text)
        if candidate.scale:
            return NormalizedNumber(round(candidate.raw_number * SCALE_MAP.get(candidate.scale, 1.0), 6), f"{currency} billions", candidate.original_text)
        return NormalizedNumber(candidate.raw_number, currency, candidate.original_text, ambiguous=True)
    if candidate.kind == "scaled":
        scale = candidate.scale or ""
        if metric == "Users":
            return NormalizedNumber(candidate.raw_number, f"count {scale}", candidate.original_text)
        return NormalizedNumber(round(candidate.raw_number * SCALE_MAP.get(scale, 1.0), 6), "billions", candidate.original_text, ambiguous=True)
    raise ValueError(f"Unsupported number candidate kind: {candidate.kind}")


def _normalize_number(sentence: str, metric: str, metric_start: int, metric_end: int) -> NormalizedNumber | None:
    allowed = [candidate for candidate in _number_candidates(sentence) if _candidate_allowed(candidate, metric)]
    if not allowed:
        return None
    after_metric = [candidate for candidate in allowed if candidate.start >= metric_end]
    if after_metric:
        chosen = min(after_metric, key=lambda candidate: candidate.start - metric_end)
    else:
        chosen = min(allowed, key=lambda candidate: min(abs(candidate.start - metric_end), abs(metric_start - candidate.end)))
    return _normalize_candidate(chosen, metric)


def _detect_period(sentence: str, fallback_text: str = "") -> str:
    match = PERIOD_RE.search(sentence) or PERIOD_RE.search(fallback_text)
    return " ".join(match.group(1).split()) if match else "Unknown"


def _detect_metrics(sentence: str) -> list[str]:
    matched: list[str] = [match.metric for match in _detect_metric_matches(sentence)]
    if "Adjusted EPS" in matched and "EPS" in matched:
        matched.remove("EPS")
    if "Adjusted EBITDA" in matched and "EBITDA" in matched:
        matched.remove("EBITDA")
    priority = {name: index for index, (name, _pattern) in enumerate(METRIC_PATTERNS)}
    return sorted(dict.fromkeys(matched), key=lambda name: priority[name])


def _detect_metric_matches(sentence: str) -> list[MetricMatch]:
    matches: list[MetricMatch] = []
    for name, pattern in METRIC_PATTERNS:
        match = pattern.search(sentence)
        if match:
            matches.append(MetricMatch(name, match.start(), match.end()))
    names = [match.metric for match in matches]
    if "Adjusted EPS" in names:
        matches = [match for match in matches if match.metric != "EPS"]
    if "Adjusted EBITDA" in names:
        matches = [match for match in matches if match.metric != "EBITDA"]
    priority = {name: index for index, (name, _pattern) in enumerate(METRIC_PATTERNS)}
    deduped: dict[str, MetricMatch] = {}
    for match in sorted(matches, key=lambda item: priority[item.metric]):
        deduped.setdefault(match.metric, match)
    return list(deduped.values())


def _claim_type(sentence: str, default: str) -> str:
    if re.search(r"\b(guidance|outlook|expects?|forecast|projects?)\b", sentence, re.IGNORECASE):
        return "Official Guidance"
    return default


def _location(block: dict[str, Any]) -> dict[str, Any]:
    return {
        "page": block.get("page"),
        "section": block.get("section") or block.get("location_hint"),
        "table": block.get("table"),
    }


def extract_financial_claims(
    text_blocks: list[dict[str, Any]],
    *,
    source_tier: str = "Tier 3",
    default_claim_type: str = "Reported Fact",
    company: str | None = None,
) -> tuple[list[dict[str, Any]], list[str]]:
    """Extract normalized financial claims from parser text blocks."""

    claims: list[dict[str, Any]] = []
    seen: set[tuple[str, float, str, str]] = set()
    warnings: list[str] = []

    for block in text_blocks:
        block_text = str(block.get("text") or "")
        for sentence in _split_sentences(block_text):
            metric_matches = _detect_metric_matches(sentence)
            if not metric_matches:
                continue
            for metric_match in metric_matches:
                metric = metric_match.metric
                normalized = _normalize_number(sentence, metric, metric_match.start, metric_match.end)
                if not normalized:
                    continue
                period = _detect_period(sentence, block_text)
                comparison_match = COMPARISON_RE.search(sentence)
                limitations: list[str] = []
                confidence = "High"
                if period == "Unknown":
                    limitations.append("Period not explicit near claim")
                    confidence = "Medium"
                if normalized.ambiguous:
                    limitations.append("Unit or currency scale is ambiguous")
                    confidence = "Low" if period == "Unknown" else "Medium"
                if re.search(r"\badjusted|non-gaap\b", sentence, re.IGNORECASE) and "Adjusted" not in metric:
                    limitations.append("Adjusted/non-GAAP basis detected in source text")
                key = (metric, normalized.value, normalized.unit, period)
                if key in seen:
                    continue
                seen.add(key)
                claims.append(
                    {
                        "claim": sentence,
                        "metric": metric,
                        "value": normalized.value,
                        "unit": normalized.unit,
                        "period": period,
                        "company": company,
                        "claim_type": _claim_type(sentence, default_claim_type),
                        "source_tier": source_tier,
                        "source_location": _location(block),
                        "support_status": "Supported",
                        "confidence": confidence,
                        "limitations": limitations,
                        "original_text_span": normalized.original_text,
                        "comparison": comparison_match.group(1) if comparison_match else None,
                    }
                )

    if not claims:
        warnings.append("No financial claims found")
    return claims, warnings
