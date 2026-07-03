"""ETF issuer provider focused on official issuer pages/holdings."""

from __future__ import annotations

from typing import Any

from .base import BaseProvider, ProviderResult
from .freshness import etf_holdings_freshness
from .http import http_text

try:
    from data_parsers.issuer_etf_parser import parse_ishares_holdings_csv
except ImportError:  # pragma: no cover
    from automation_lab.data_parsers.issuer_etf_parser import parse_ishares_holdings_csv

ISHARES_PAGES = {
    "TLT": "https://www.ishares.com/us/products/239454/ishares-20-year-treasury-bond-etf",
    "CORN": "https://www.teucrium.com/etfs/corn",
    "WEAT": "https://www.teucrium.com/etfs/weat",
    "SOYB": "https://www.teucrium.com/etfs/soyb",
}


class ETFIssuerProvider(BaseProvider):
    provider_id = "etf_issuer_provider"
    provider_name = "ETF issuer official pages and holdings"
    source_tier = "Tier 1"
    source_type = "issuer_etf"
    asset_classes = ("etf", "bond_etf", "commodity_etf", "fixed_income", "commodity")

    def fetch(self, query: dict[str, Any], *, storage: Any = None, allow_network: bool = True) -> ProviderResult:
        ticker = str(query.get("ticker") or query.get("subject") or "").upper()
        subject = str(query.get("subject") or ticker or "ETF")
        asset_class = str(query.get("asset_class") or "etf")
        issuer_url = query.get("issuer_url") or ISHARES_PAGES.get(ticker)
        holdings_url = query.get("holdings_url")
        if not issuer_url:
            return ProviderResult(
                provider_id=self.provider_id,
                provider_name=self.provider_name,
                source_tier=self.source_tier,
                source_type=self.source_type,
                asset_class=asset_class,
                subject=subject,
                query=query,
                url=None,
                status="missing",
                access_status="Not Found",
                freshness_status="Unknown",
                limitations=["No official issuer URL is configured for this ticker."],
            )
        if not allow_network and "holdings_csv" not in query:
            return ProviderResult(
                provider_id=self.provider_id,
                provider_name=self.provider_name,
                source_tier=self.source_tier,
                source_type=self.source_type,
                asset_class=asset_class,
                subject=subject,
                query=query,
                url=issuer_url,
                status="partial",
                access_status="Partial",
                freshness_status="Unknown",
                normalized_data={"ticker": ticker, "issuer_url": issuer_url, "holdings": []},
                limitations=["Issuer page candidate recorded; network disabled so holdings were not fetched or parsed."],
            )
        try:
            page_text = query.get("issuer_page_text") or (http_text(str(issuer_url)) if allow_network else "")
            raw_path = storage.save_raw_text(self.provider_id, query, page_text, url=str(issuer_url), suffix=".html") if storage and page_text else None
            holdings = {"ticker": ticker, "issuer_url": issuer_url, "holdings": [], "holding_count": 0, "as_of_date": query.get("as_of_date")}
            holdings_raw_path = None
            if query.get("holdings_csv") or holdings_url:
                csv_text = query.get("holdings_csv") or http_text(str(holdings_url))
                holdings_raw_path = storage.save_raw_text(f"{self.provider_id}_holdings", query, csv_text, url=str(holdings_url), suffix=".csv") if storage else None
                holdings = {**holdings, **parse_ishares_holdings_csv(csv_text, ticker=ticker)}
            normalized = {
                "ticker": ticker,
                "fund_name": query.get("fund_name"),
                "issuer_url": issuer_url,
                "holdings_file_url": holdings_url,
                "expense_ratio": query.get("expense_ratio"),
                "aum": query.get("aum"),
                "duration": query.get("duration"),
                "yield_metrics": query.get("yield_metrics"),
                **holdings,
            }
            normalized_path = storage.save_normalized(self.provider_id, query, normalized, url=str(issuer_url)) if storage else None
            status = "ok" if normalized.get("holdings") else "partial"
            limitations = [] if status == "ok" else ["Issuer page found, but holdings were not parsed; do not pretend holdings support exists."]
            source_date = normalized.get("as_of_date") or query.get("source_date")
            freshness = etf_holdings_freshness(source_date)
            return ProviderResult(
                provider_id=self.provider_id,
                provider_name=self.provider_name,
                source_tier=self.source_tier,
                source_type=self.source_type,
                asset_class=asset_class,
                subject=subject,
                query=query,
                url=str(issuer_url),
                status=status,
                access_status="Available" if status == "ok" else "Partial",
                freshness_status=freshness,
                source_date=source_date,
                raw_path=holdings_raw_path or raw_path,
                normalized_path=normalized_path,
                normalized_data=normalized,
                claims=[
                    {
                        "claim": f"{ticker} issuer holdings parsed with {normalized.get('holding_count')} rows as of {source_date}.",
                        "claim_type": "Reported Fact",
                        "materiality": "Decision-Critical",
                        "source": holdings_url or issuer_url,
                        "source_tier": "Tier 1",
                        "source_date": source_date,
                        "freshness": freshness,
                        "support_status": "Supported",
                        "access": "Available",
                        "limitation": "",
                    }
                ]
                if status == "ok"
                else [],
                limitations=limitations,
                metadata={"raw_page_path": raw_path},
            )
        except Exception as exc:
            return self.error_result(query, exc, url=str(issuer_url))
