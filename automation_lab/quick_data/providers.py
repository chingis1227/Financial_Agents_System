"""Provider contracts and public fetch helpers for QUICK data snapshots."""

from __future__ import annotations

import json
import urllib.request
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from typing import Any, Callable

ALLOWED_PROVIDER_TYPES = {"mock", "public", "static", "api"}
ALLOWED_PROVIDER_STATUSES = {"ok", "missing", "error", "disabled"}
ALLOWED_QUALITY_LEVELS = {"official", "public_market", "static_context", "mock", "disabled_api", "failed"}


def safe_now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


@dataclass(frozen=True)
class ProviderMetadata:
    provider_id: str
    name: str
    provider_type: str
    components: tuple[str, ...]
    asset_types: tuple[str, ...]
    quality_level: str
    access_mode: str
    priority: int
    enabled: bool
    freshness_policy: str

    def to_snapshot(self) -> dict[str, Any]:
        data = asdict(self)
        data["components"] = list(self.components)
        data["asset_types"] = list(self.asset_types)
        return data


@dataclass(frozen=True)
class ProviderResult:
    provider_id: str
    component: str
    status: str
    data: Any = None
    source_record: dict[str, Any] | None = None
    error: str | None = None
    retrieved_at: str | None = None
    source_date: str | None = None
    freshness_status: str = "unknown"
    quality_level: str = "failed"

    def to_snapshot(self) -> dict[str, Any]:
        return {
            "provider_id": self.provider_id,
            "component": self.component,
            "status": self.status,
            "data": self.data,
            "source_record": self.source_record,
            "error": self.error,
            "retrieved_at": self.retrieved_at or safe_now_iso(),
            "source_date": self.source_date,
            "freshness_status": self.freshness_status,
            "quality_level": self.quality_level,
        }


def source_record(component: str, name: str, status: str, url: str | None = None, detail: str = "") -> dict[str, Any]:
    record: dict[str, Any] = {
        "component": component,
        "name": name,
        "status": status,
        "retrieved_at": safe_now_iso(),
    }
    if url:
        record["url"] = url
    if detail:
        record["detail"] = detail
    return record


def provider_result_from_disabled(metadata: ProviderMetadata, component: str) -> ProviderResult:
    return ProviderResult(
        provider_id=metadata.provider_id,
        component=component,
        status="disabled",
        data=None,
        source_record=source_record(component, metadata.name, "disabled", detail="Future optional API slot; no key required or used in TASK-009."),
        error=None,
        retrieved_at=safe_now_iso(),
        source_date=None,
        freshness_status="disabled",
        quality_level="disabled_api",
    )


def http_json(url: str, timeout: int = 10) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Financial Agent Automation Lab contact: local@example.com",
            "Accept": "application/json,text/plain,*/*",
        },
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        data = response.read().decode("utf-8")
    parsed = json.loads(data)
    if not isinstance(parsed, dict):
        raise ValueError("expected JSON object")
    return parsed


def http_text(url: str, timeout: int = 10) -> str:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Financial Agent Automation Lab contact: local@example.com"},
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read().decode("utf-8", errors="replace")


def sec_recent_filings(cik: str) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    cik_digits = "".join(ch for ch in str(cik) if ch.isdigit()).zfill(10)
    url = f"https://data.sec.gov/submissions/CIK{cik_digits}.json"
    data = http_json(url)
    recent = data.get("filings", {}).get("recent", {})
    forms = recent.get("form", [])
    filing_dates = recent.get("filingDate", [])
    accession_numbers = recent.get("accessionNumber", [])
    primary_documents = recent.get("primaryDocument", [])
    filings: list[dict[str, Any]] = []
    for index, form in enumerate(forms[:200]):
        if form not in {"10-K", "10-Q", "8-K"}:
            continue
        filings.append(
            {
                "form": form,
                "filing_date": filing_dates[index] if index < len(filing_dates) else None,
                "accession_number": accession_numbers[index] if index < len(accession_numbers) else None,
                "primary_document": primary_documents[index] if index < len(primary_documents) else None,
                "source_identifier": f"SEC CIK{cik_digits}",
            }
        )
        if len(filings) >= 6:
            break
    source = source_record("filings", "SEC submissions", "ok", url=url)
    return filings, source


def fetch_stooq_price(ticker: str) -> tuple[dict[str, Any] | None, dict[str, Any]]:
    symbol = ticker.lower()
    url = f"https://stooq.com/q/l/?s={symbol}.us&f=sd2t2ohlcv&h&e=csv"
    text = http_text(url)
    rows = [row for row in text.splitlines() if row.strip()]
    if len(rows) < 2:
        return None, source_record("price", "Stooq public CSV", "missing", url=url, detail="no rows")
    headers = [item.strip() for item in rows[0].split(",")]
    values = [item.strip() for item in rows[1].split(",")]
    data = dict(zip(headers, values, strict=False))
    close = data.get("Close")
    if not close or close.upper() == "N/D":
        return None, source_record("price", "Stooq public CSV", "missing", url=url, detail="no close price")
    price = {
        "ticker": ticker.upper(),
        "date": data.get("Date"),
        "time": data.get("Time"),
        "close": close,
        "currency": "USD",
        "source": "Stooq public CSV",
        "source_identifier": url,
    }
    return price, source_record("price", "Stooq public CSV", "ok", url=url)


def fetch_yahoo_chart_price(ticker: str) -> tuple[dict[str, Any] | None, dict[str, Any]]:
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker.upper()}?range=5d&interval=1d"
    data = http_json(url)
    result = (data.get("chart", {}).get("result") or [None])[0]
    if not isinstance(result, dict):
        return None, source_record("price", "Yahoo public chart", "missing", url=url, detail="no chart result")
    meta = result.get("meta") or {}
    indicators = result.get("indicators", {}).get("quote") or []
    quote = indicators[0] if indicators else {}
    timestamps = result.get("timestamp") or []
    closes = quote.get("close") or []
    price = None
    price_timestamp = None
    for index in range(len(closes) - 1, -1, -1):
        if closes[index] is not None:
            price = closes[index]
            price_timestamp = timestamps[index] if index < len(timestamps) else None
            break
    if price is None:
        regular = meta.get("regularMarketPrice")
        if regular is None:
            return None, source_record("price", "Yahoo public chart", "missing", url=url, detail="no price")
        price = regular
        price_timestamp = meta.get("regularMarketTime")
    date_text = None
    if isinstance(price_timestamp, int):
        date_text = datetime.fromtimestamp(price_timestamp, tz=timezone.utc).date().isoformat()
    return (
        {
            "ticker": ticker.upper(),
            "date": date_text,
            "close": round(float(price), 4),
            "currency": meta.get("currency", "USD"),
            "source": "Yahoo public chart",
            "source_identifier": url,
        },
        source_record("price", "Yahoo public chart", "ok", url=url),
    )


PRICE_FETCHERS: dict[str, Callable[[str], tuple[dict[str, Any] | None, dict[str, Any]]]] = {
    "stooq_price": fetch_stooq_price,
    "yahoo_chart_price": fetch_yahoo_chart_price,
}


def run_price_provider(metadata: ProviderMetadata, ticker: str) -> ProviderResult:
    if not metadata.enabled:
        return provider_result_from_disabled(metadata, "price")
    fetcher = PRICE_FETCHERS.get(metadata.provider_id)
    if fetcher is None:
        return ProviderResult(
            provider_id=metadata.provider_id,
            component="price",
            status="error",
            error="No fetcher is registered for provider.",
            source_record=source_record("price", metadata.name, "error", detail="missing fetcher"),
            retrieved_at=safe_now_iso(),
            quality_level="failed",
        )
    try:
        price, source = fetcher(ticker)
        if price:
            return ProviderResult(
                provider_id=metadata.provider_id,
                component="price",
                status="ok",
                data=price,
                source_record=source,
                retrieved_at=safe_now_iso(),
                source_date=price.get("date"),
                freshness_status="provider_dated" if price.get("date") else "unknown",
                quality_level=metadata.quality_level,
            )
        return ProviderResult(
            provider_id=metadata.provider_id,
            component="price",
            status="missing",
            data=None,
            source_record=source,
            error=source.get("detail"),
            retrieved_at=safe_now_iso(),
            source_date=None,
            freshness_status="unknown",
            quality_level="failed",
        )
    except Exception as exc:  # public provider failures are captured and downgraded by snapshot quality.
        return ProviderResult(
            provider_id=metadata.provider_id,
            component="price",
            status="error",
            data=None,
            source_record=source_record("price", metadata.name, "error", detail=str(exc)),
            error=str(exc),
            retrieved_at=safe_now_iso(),
            source_date=None,
            freshness_status="unknown",
            quality_level="failed",
        )


def run_sec_filings_provider(metadata: ProviderMetadata, cik: str) -> ProviderResult:
    if not metadata.enabled:
        return provider_result_from_disabled(metadata, "filings")
    try:
        filings, source = sec_recent_filings(cik)
        latest_date = None
        if filings:
            latest_date = filings[0].get("filing_date")
        return ProviderResult(
            provider_id=metadata.provider_id,
            component="filings",
            status="ok" if filings else "missing",
            data=filings,
            source_record=source if filings else {**source, "status": "missing", "detail": "no supported recent filing forms"},
            error=None if filings else "no supported recent filing forms",
            retrieved_at=safe_now_iso(),
            source_date=latest_date,
            freshness_status="filing_driven" if latest_date else "unknown",
            quality_level=metadata.quality_level if filings else "failed",
        )
    except Exception as exc:
        return ProviderResult(
            provider_id=metadata.provider_id,
            component="filings",
            status="error",
            data=None,
            source_record=source_record("filings", metadata.name, "error", detail=str(exc)),
            error=str(exc),
            retrieved_at=safe_now_iso(),
            source_date=None,
            freshness_status="unknown",
            quality_level="failed",
        )


def fetch_public_price(ticker: str, asset_type: str | None = None) -> tuple[dict[str, Any] | None, list[dict[str, Any]]]:
    """Compatibility helper that executes enabled public price providers by registry priority."""
    from .registry import providers_for

    sources: list[dict[str, Any]] = []
    for metadata in providers_for("price", asset_type=asset_type, include_disabled=False):
        if metadata.provider_type != "public":
            continue
        result = run_price_provider(metadata, ticker)
        if result.source_record:
            sources.append(result.source_record)
        if result.status == "ok" and result.data:
            return result.data, sources
    return None, sources
