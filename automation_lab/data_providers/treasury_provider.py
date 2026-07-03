"""U.S. Treasury official data provider."""

from __future__ import annotations

from typing import Any

from .base import BaseProvider, ProviderResult
from .freshness import daily_series_freshness
from .http import http_json, urlencode


class TreasuryProvider(BaseProvider):
    provider_id = "treasury_provider"
    provider_name = "U.S. Treasury Fiscal Data"
    source_tier = "Tier 1"
    source_type = "treasury_rates"
    asset_classes = ("fixed_income", "macro", "multi_asset")

    def fetch(self, query: dict[str, Any], *, storage: Any = None, allow_network: bool = True) -> ProviderResult:
        subject = str(query.get("subject") or "treasury_curve")
        asset_class = str(query.get("asset_class") or "fixed_income")
        url = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v2/accounting/od/avg_interest_rates"
        if not allow_network and "rows_data" not in query:
            return self.disabled_result(query, "Network disabled for this provider run; Treasury attempt recorded but not fetched.")
        try:
            if "rows_data" in query:
                data = {"data": query["rows_data"]}
                full_url = "fixture://treasury"
            else:
                params = urlencode({"sort": "-record_date", "page[size]": 100})
                full_url = f"{url}?{params}"
                data = http_json(full_url)
            raw_path = storage.save_raw_json(self.provider_id, query, data, url=full_url) if storage else None
            rows = []
            for item in data.get("data", []):
                rows.append(
                    {
                        "date": item.get("record_date"),
                        "maturity": item.get("security_desc") or item.get("security_type_desc"),
                        "rate": float(item.get("avg_interest_rate_amt")) if item.get("avg_interest_rate_amt") not in (None, "") else None,
                    }
                )
            normalized = {"curve_points": rows}
            normalized_path = storage.save_normalized(self.provider_id, query, normalized, url=full_url) if storage else None
            latest_date = max((row["date"] for row in rows if row.get("date")), default=None)
            freshness = daily_series_freshness(latest_date)
            return ProviderResult(
                provider_id=self.provider_id,
                provider_name=self.provider_name,
                source_tier=self.source_tier,
                source_type=self.source_type,
                asset_class=asset_class,
                subject=subject,
                query=query,
                url=full_url,
                status="ok" if rows else "missing",
                access_status="Available" if rows else "Not Found",
                freshness_status=freshness,
                source_date=latest_date,
                raw_path=raw_path,
                normalized_path=normalized_path,
                normalized_data=normalized,
                claims=[
                    {
                        "claim": f"Treasury rate point {row.get('maturity')} was {row.get('rate')} on {row.get('date')}.",
                        "claim_type": "Market Data",
                        "materiality": "Important",
                        "source": full_url,
                        "source_tier": "Tier 1",
                        "source_date": row.get("date"),
                        "freshness": freshness,
                        "support_status": "Supported",
                        "access": "Available",
                        "limitation": "",
                    }
                    for row in rows[:20]
                ],
                limitations=[] if rows else ["No Treasury rows normalized."],
            )
        except Exception as exc:
            return self.error_result(query, exc, url=url)
