"""Freshness policy helpers for provider results."""

from __future__ import annotations

from datetime import datetime, timezone


def parse_date(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        if "T" in value:
            parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
            return parsed if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)
        return datetime.fromisoformat(value).replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def age_days(source_date: str | None, *, now: datetime | None = None) -> float | None:
    parsed = parse_date(source_date)
    if parsed is None:
        return None
    current = now or datetime.now(timezone.utc)
    return (current - parsed.astimezone(timezone.utc)).total_seconds() / 86400


def classify_by_age(
    source_date: str | None,
    *,
    current_days: int,
    recent_days: int,
    stale_usable_days: int | None = None,
    now: datetime | None = None,
) -> str:
    age = age_days(source_date, now=now)
    if age is None or age < 0:
        return "Unknown"
    if age <= current_days:
        return "Current"
    if age <= recent_days:
        return "Recent"
    if stale_usable_days is not None and age <= stale_usable_days:
        return "Stale but Usable"
    return "Refresh Required"


def filing_freshness(source_date: str | None, *, historical_fact: bool = False) -> str:
    if historical_fact and source_date:
        return "Current"
    return classify_by_age(source_date, current_days=95, recent_days=460, stale_usable_days=3700)


def market_price_freshness(source_date: str | None) -> str:
    return classify_by_age(source_date, current_days=4, recent_days=10, stale_usable_days=30)


def daily_series_freshness(source_date: str | None) -> str:
    return classify_by_age(source_date, current_days=5, recent_days=14, stale_usable_days=45)


def monthly_series_freshness(source_date: str | None) -> str:
    return classify_by_age(source_date, current_days=45, recent_days=75, stale_usable_days=120)


def cot_freshness(source_date: str | None) -> str:
    return classify_by_age(source_date, current_days=10, recent_days=17, stale_usable_days=31)


def etf_holdings_freshness(source_date: str | None) -> str:
    return classify_by_age(source_date, current_days=14, recent_days=45, stale_usable_days=90)
