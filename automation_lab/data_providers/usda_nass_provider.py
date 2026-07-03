"""USDA NASS provider."""

from __future__ import annotations

import os
from typing import Any

from .base import BaseProvider, ProviderResult
from .freshness import monthly_series_freshness
from .http import http_json, urlencode


class USDANASSProvider(BaseProvider):
    provider_id = "usda_nass_provider"
    provider_name = "USDA NASS QuickStats"
    source_tier = "Tier 1"
    source_type = "usda_nass"
    asset_classes = ("commodity", "grains")
    requires_api_key = True
    env_key = "USDA_NASS_API_KEY"

    def fetch(self, query: dict[str, Any], *, storage: Any = None, allow_network: bool = True) -> ProviderResult:
        subject = str(query.get("subject") or query.get("commodity") or "grain")
        asset_class = str(query.get("asset_class") or "grains")
        api_key = os.environ.get(self.env_key or "")
        if not api_key and "rows_data" not in query:
            return self.disabled_result(query, "USDA_NASS_API_KEY is not configured; provider disabled gracefully.")
        if not allow_network and "rows_data" not in query:
            return self.disabled_result(query, "Network disabled for this provider run; USDA NASS attempt recorded but not fetched.")
        try:
            if "rows_data" in query:
                data = {"data": query["rows_data"]}
                url = "fixture://usda-nass"
            else:
                params = urlencode(
                    {
                        "key": api_key,
                        "format": "JSON",
                        "commodity_desc": query.get("commodity", "CORN"),
                        "agg_level_desc": query.get("geography", "NATIONAL"),
                        "statisticcat_desc": query.get("statistic", query.get("metric", "")),
                        "year__GE": query.get("year_ge"),
                    }
                )
                url = f"https://quickstats.nass.usda.gov/api/api_GET/?{params}"
                data = http_json(url)
            raw_path = storage.save_raw_json(self.provider_id, query, data, url=url) if storage else None
            rows = []
            for row in data.get("data", []):
                rows.append(
                    {
                        "commodity": row.get("commodity_desc"),
                        "metric": row.get("statisticcat_desc") or row.get("short_desc"),
                        "period": row.get("year") or row.get("reference_period_desc"),
                        "geography": row.get("state_name") or row.get("agg_level_desc"),
                        "unit": row.get("unit_desc"),
                        "value": row.get("Value"),
                        "source_date": row.get("load_time") or row.get("year"),
                    }
                )
            normalized = {"rows": rows}
            normalized_path = storage.save_normalized(self.provider_id, query, normalized, url=url) if storage else None
            latest_date = max((str(row.get("source_date")) for row in rows if row.get("source_date")), default=None)
            freshness = monthly_series_freshness(latest_date)
            return ProviderResult(
                provider_id=self.provider_id,
                provider_name=self.provider_name,
                source_tier=self.source_tier,
                source_type=self.source_type,
                asset_class=asset_class,
                subject=subject,
                query=query,
                url=url,
                status="ok" if rows else "missing",
                access_status="Available" if rows else "Not Found",
                freshness_status=freshness,
                source_date=latest_date,
                raw_path=raw_path,
                normalized_path=normalized_path,
                normalized_data=normalized,
                claims=[
                    {
                        "claim": f"USDA NASS {row.get('commodity')} {row.get('metric')} was {row.get('value')} {row.get('unit')} for {row.get('period')}.",
                        "claim_type": "Reported Fact",
                        "materiality": "Important",
                        "source": url,
                        "source_tier": "Tier 1",
                        "source_date": str(row.get("source_date") or ""),
                        "freshness": freshness,
                        "support_status": "Supported",
                        "access": "Available",
                        "limitation": "",
                    }
                    for row in rows[:20]
                ],
                limitations=[] if rows else ["No NASS rows normalized for the query."],
            )
        except Exception as exc:
            return self.error_result(query, exc)
