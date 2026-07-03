"""CFTC Commitments of Traders provider."""

from __future__ import annotations

from typing import Any

from .base import BaseProvider, ProviderResult
from .freshness import cot_freshness
from .http import http_text

try:
    from data_parsers.cftc_cot_parser import parse_cot_csv
except ImportError:  # pragma: no cover
    from automation_lab.data_parsers.cftc_cot_parser import parse_cot_csv


class CFTCCOTProvider(BaseProvider):
    provider_id = "cftc_cot_provider"
    provider_name = "CFTC Commitments of Traders"
    source_tier = "Tier 1"
    source_type = "cftc_cot"
    asset_classes = ("commodity", "grains", "multi_asset")

    def fetch(self, query: dict[str, Any], *, storage: Any = None, allow_network: bool = True) -> ProviderResult:
        subject = str(query.get("subject") or query.get("market") or "commodity")
        asset_class = str(query.get("asset_class") or "commodity")
        url = str(query.get("url") or "https://www.cftc.gov/dea/newcot/f_disagg.txt")
        if not allow_network and "csv_text" not in query:
            return self.disabled_result(query, "Network disabled for this provider run; CFTC COT attempt recorded but not fetched.")
        try:
            text = query.get("csv_text") or http_text(url)
            raw_path = storage.save_raw_text(self.provider_id, query, text, url=url, suffix=".csv") if storage else None
            rows = parse_cot_csv(text, market_filter=query.get("market") or query.get("commodity"))
            normalized = {"rows": rows, "reporting_lag_limitation": "COT is published with a reporting lag."}
            normalized_path = storage.save_normalized(self.provider_id, query, normalized, url=url) if storage else None
            latest_date = max((row.get("report_date") for row in rows if row.get("report_date")), default=None)
            freshness = cot_freshness(latest_date)
            return ProviderResult(
                provider_id=self.provider_id,
                provider_name=self.provider_name,
                source_tier=self.source_tier,
                source_type=self.source_type,
                asset_class=asset_class,
                subject=subject,
                query=query,
                url=url,
                status="ok" if rows else "partial",
                access_status="Available" if rows else "Partial",
                freshness_status=freshness,
                source_date=latest_date,
                raw_path=raw_path,
                normalized_path=normalized_path,
                normalized_data=normalized,
                claims=[
                    {
                        "claim": f"CFTC COT managed money net positioning for {row.get('market_name')} was {row.get('net_managed_money')} on {row.get('report_date')}.",
                        "claim_type": "Market Data",
                        "materiality": "Important",
                        "source": url,
                        "source_tier": "Tier 1",
                        "source_date": row.get("report_date"),
                        "freshness": freshness,
                        "support_status": "Supported",
                        "access": "Available",
                        "limitation": "COT data has reporting lag.",
                    }
                    for row in rows[:20]
                ],
                limitations=["COT data has reporting lag."] if rows else ["COT file fetched but no matching rows parsed."],
            )
        except Exception as exc:
            return self.error_result(query, exc, url=url)
