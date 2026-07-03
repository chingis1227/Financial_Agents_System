"""USDA WASDE provider/parser wrapper."""

from __future__ import annotations

from typing import Any

from .base import BaseProvider, ProviderResult
from .freshness import monthly_series_freshness
from .http import http_text

try:
    from data_parsers.usda_wasde_parser import parse_wasde_text
except ImportError:  # pragma: no cover
    from automation_lab.data_parsers.usda_wasde_parser import parse_wasde_text


class USDAWASDEProvider(BaseProvider):
    provider_id = "usda_wasde_provider"
    provider_name = "USDA WASDE"
    source_tier = "Tier 1"
    source_type = "usda_wasde"
    asset_classes = ("commodity", "grains")

    def fetch(self, query: dict[str, Any], *, storage: Any = None, allow_network: bool = True) -> ProviderResult:
        subject = str(query.get("subject") or query.get("commodity") or "grain")
        asset_class = str(query.get("asset_class") or "grains")
        url = str(query.get("url") or "https://www.usda.gov/oce/commodity/wasde")
        if not allow_network and "text" not in query:
            return self.disabled_result(query, "Network disabled for this provider run; WASDE attempt recorded but not fetched.")
        try:
            text = query.get("text") or http_text(url)
            raw_path = storage.save_raw_text(self.provider_id, query, text, url=url) if storage else None
            rows = parse_wasde_text(text)
            normalized = {"rows": rows}
            normalized_path = storage.save_normalized(self.provider_id, query, normalized, url=url) if storage else None
            latest_date = query.get("source_date")
            freshness = monthly_series_freshness(latest_date)
            claim_limitation = "" if latest_date and freshness != "Unknown" else "WASDE source/report date was not supplied; freshness is Unknown and this claim must remain date-limited."
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
                        "claim": f"WASDE {row.get('commodity')} {row.get('metric')} normalized as {row.get('value')} {row.get('unit')}.",
                        "claim_type": "Reported Fact",
                        "materiality": "Important",
                        "source": url,
                        "source_tier": "Tier 1",
                        "source_date": latest_date,
                        "freshness": freshness,
                        "support_status": "Supported",
                        "access": "Available",
                        "limitation": claim_limitation,
                    }
                    for row in rows[:20]
                ],
                limitations=(
                    [claim_limitation]
                    if rows and claim_limitation
                    else [] if rows else ["WASDE source was accessible but key grain table values were not parsed; do not treat as silent success."]
                ),
            )
        except Exception as exc:
            return self.error_result(query, exc, url=url)
