"""Unified public price provider: Stooq first, Yahoo chart fallback."""

from __future__ import annotations

import csv
from datetime import datetime, timezone
from io import StringIO
from typing import Any

from .base import BaseProvider, ProviderResult
from .freshness import market_price_freshness
from .http import http_json, http_text, urlencode


def _stooq_candidates(ticker: str) -> list[str]:
    normalized = ticker.strip().lower().replace("/", ".")
    if "." in normalized:
        return [normalized]
    return [f"{normalized}.us", normalized]


class PublicPriceProvider(BaseProvider):
    provider_id = "public_price_provider"
    provider_name = "Public price provider (Stooq/Yahoo)"
    source_tier = "Tier 2"
    source_type = "public_market_data"
    asset_classes = ("equity", "etf", "bond_etf", "commodity_etf", "crypto", "fixed_income", "commodity", "multi_asset")

    def fetch(self, query: dict[str, Any], *, storage: Any = None, allow_network: bool = True) -> ProviderResult:
        ticker = str(query.get("price_ticker") or query.get("ticker") or query.get("subject") or "").upper()
        subject = str(query.get("subject") or ticker or "asset")
        asset_class = str(query.get("asset_class") or "unknown")
        if not ticker:
            return self.disabled_result(query, "No ticker supplied for public price provider.")
        if not allow_network and "price_data" not in query:
            return self.disabled_result(query, "Network disabled for this provider run; public price attempt recorded but not fetched.")
        try:
            if "price_data" in query:
                normalized = query["price_data"]
                url = normalized.get("source_identifier") or "fixture://public-price"
                raw_path = None
            else:
                normalized = None
                errors = []
                url = None
                raw_path = None
                if asset_class != "crypto":
                    for symbol in _stooq_candidates(ticker):
                        stooq_url = f"https://stooq.com/q/d/l/?s={symbol}&i=d"
                        try:
                            text = http_text(stooq_url)
                            raw_path = storage.save_raw_text(f"{self.provider_id}_stooq", query, text, url=stooq_url, suffix=".csv") if storage else None
                            points = []
                            for row in csv.DictReader(StringIO(text)):
                                if row.get("Close") and row.get("Close") != "N/D" and row.get("Date"):
                                    points.append({"date": row["Date"], "close": float(row["Close"])})
                            if points:
                                latest = points[-1]
                                normalized = {"ticker": ticker, "latest": latest, "history": points[-260:], "currency": "USD", "provider": "Stooq public CSV"}
                                url = stooq_url
                                break
                        except Exception as exc:
                            errors.append(f"Stooq {symbol}: {exc}")
                if normalized is None:
                    params = urlencode({"range": query.get("range", "1y"), "interval": query.get("interval", "1d")})
                    yahoo_url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?{params}"
                    data = http_json(yahoo_url)
                    raw_path = storage.save_raw_json(f"{self.provider_id}_yahoo", query, data, url=yahoo_url) if storage else raw_path
                    result = (data.get("chart", {}).get("result") or [None])[0]
                    if not isinstance(result, dict):
                        raise ValueError("; ".join(errors + ["Yahoo chart result missing"]))
                    timestamps = result.get("timestamp") or []
                    closes = (result.get("indicators", {}).get("quote") or [{}])[0].get("close") or []
                    points = []
                    for index, close in enumerate(closes):
                        if close is None or index >= len(timestamps):
                            continue
                        points.append({"date": datetime.fromtimestamp(timestamps[index], tz=timezone.utc).date().isoformat(), "close": round(float(close), 4)})
                    if not points:
                        raise ValueError("; ".join(errors + ["Yahoo chart close missing"]))
                    latest = points[-1]
                    normalized = {"ticker": ticker, "latest": latest, "history": points[-260:], "currency": (result.get("meta") or {}).get("currency", "USD"), "provider": "Yahoo public chart"}
                    url = yahoo_url
            normalized_path = storage.save_normalized(self.provider_id, query, normalized, url=url) if storage else None
            latest = normalized.get("latest") if isinstance(normalized, dict) else {}
            source_date = latest.get("date") if isinstance(latest, dict) else normalized.get("date")
            freshness = market_price_freshness(source_date)
            return ProviderResult(
                provider_id=self.provider_id,
                provider_name=self.provider_name,
                source_tier=self.source_tier,
                source_type=self.source_type,
                asset_class=asset_class,
                subject=subject,
                query=query,
                url=url,
                status="ok",
                access_status="Available",
                freshness_status=freshness,
                source_date=source_date,
                raw_path=raw_path,
                normalized_path=normalized_path,
                normalized_data=normalized,
                claims=[
                    {
                        "claim": f"Public latest price for {ticker} was {latest.get('close')} on {source_date}.",
                        "claim_type": "Market Data",
                        "materiality": "Decision-Critical",
                        "source": url,
                        "source_tier": "Tier 2",
                        "source_date": source_date,
                        "freshness": freshness,
                        "support_status": "Supported",
                        "access": "Available",
                        "limitation": "Public market-data fallback; official exchange provider should supersede where configured.",
                    }
                ],
            )
        except Exception as exc:
            return self.error_result(query, exc)
