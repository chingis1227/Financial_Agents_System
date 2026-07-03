"""FRED macro provider."""

from __future__ import annotations

import os
from typing import Any

from .base import BaseProvider, ProviderResult
from .freshness import daily_series_freshness, monthly_series_freshness
from .http import http_json, urlencode

DEFAULT_FRED_SERIES = ["FEDFUNDS", "DGS2", "DGS10", "DGS20", "DGS30", "T10YIE", "DFII10", "CPIAUCSL", "UNRATE", "GDP", "BAMLH0A0HYM2"]


class FREDProvider(BaseProvider):
    provider_id = "fred_provider"
    provider_name = "FRED official macro series"
    source_tier = "Tier 1"
    source_type = "fred_series"
    asset_classes = ("macro", "fixed_income", "multi_asset")
    requires_api_key = True
    env_key = "FRED_API_KEY"

    def fetch(self, query: dict[str, Any], *, storage: Any = None, allow_network: bool = True) -> ProviderResult:
        subject = str(query.get("subject") or "macro")
        asset_class = str(query.get("asset_class") or "macro")
        api_key = os.environ.get(self.env_key or "")
        if not api_key and "observations_data" not in query:
            return self.disabled_result(query, "FRED_API_KEY is not configured; provider disabled gracefully.")
        series_ids = query.get("series_ids") or query.get("series") or DEFAULT_FRED_SERIES
        if isinstance(series_ids, str):
            series_ids = [series_ids]
        if not allow_network and "observations_data" not in query:
            return self.disabled_result(query, "Network disabled for this provider run; FRED attempt recorded but not fetched.")
        rows: list[dict[str, Any]] = []
        raw: dict[str, Any] = {}
        try:
            observations_fixture = query.get("observations_data") or {}
            for series_id in series_ids:
                if series_id in observations_fixture:
                    data = observations_fixture[series_id]
                    url = "fixture://fred"
                else:
                    params = urlencode({"series_id": series_id, "api_key": api_key, "file_type": "json", "sort_order": "desc", "limit": 24})
                    url = f"https://api.stlouisfed.org/fred/series/observations?{params}"
                    data = http_json(url)
                raw[series_id] = data
                for item in data.get("observations", []):
                    value = item.get("value")
                    if value in (None, ".", ""):
                        continue
                    rows.append({"series_id": series_id, "date": item.get("date"), "value": float(value)})
            raw_path = storage.save_raw_json(self.provider_id, query, raw, url="https://fred.stlouisfed.org/") if storage else None
            normalized = {"series": rows, "series_ids": list(series_ids)}
            normalized_path = storage.save_normalized(self.provider_id, query, normalized, url="https://fred.stlouisfed.org/") if storage else None
            latest_date = max((row["date"] for row in rows if row.get("date")), default=None)
            freshness = daily_series_freshness(latest_date) if any(str(s).startswith("D") for s in series_ids) else monthly_series_freshness(latest_date)
            claims = [
                {
                    "claim": f"FRED series {row['series_id']} reported {row['value']} on {row['date']}.",
                    "claim_type": "Market Data",
                    "materiality": "Important",
                    "source": "https://fred.stlouisfed.org/",
                    "source_tier": "Tier 1",
                    "source_date": row.get("date"),
                    "freshness": freshness,
                    "support_status": "Supported",
                    "access": "Available",
                    "limitation": "",
                }
                for row in rows[:20]
            ]
            return ProviderResult(
                provider_id=self.provider_id,
                provider_name=self.provider_name,
                source_tier=self.source_tier,
                source_type=self.source_type,
                asset_class=asset_class,
                subject=subject,
                query=query,
                url="https://fred.stlouisfed.org/",
                status="ok" if rows else "missing",
                access_status="Available" if rows else "Not Found",
                freshness_status=freshness,
                source_date=latest_date,
                raw_path=raw_path,
                normalized_path=normalized_path,
                normalized_data=normalized,
                claims=claims,
                limitations=[] if rows else ["No FRED observations normalized."],
                metadata={"series_ids": list(series_ids)},
            )
        except Exception as exc:
            return self.error_result(query, exc, url="https://fred.stlouisfed.org/")
