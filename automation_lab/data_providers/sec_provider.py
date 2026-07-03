"""SEC EDGAR provider."""

from __future__ import annotations

from typing import Any

from .base import BaseProvider, ProviderResult
from .freshness import filing_freshness
from .http import http_json

try:
    from data_parsers.sec_filing_parser import latest_by_form, normalize_companyfacts, normalize_submissions
except ImportError:  # pragma: no cover - package import path fallback
    from automation_lab.data_parsers.sec_filing_parser import latest_by_form, normalize_companyfacts, normalize_submissions


class SECProvider(BaseProvider):
    provider_id = "sec_provider"
    provider_name = "SEC EDGAR submissions and companyfacts"
    source_tier = "Tier 1"
    source_type = "sec_filings"
    asset_classes = ("equity",)

    def fetch(self, query: dict[str, Any], *, storage: Any = None, allow_network: bool = True) -> ProviderResult:
        cik = query.get("cik")
        subject = str(query.get("subject") or query.get("ticker") or cik or "unknown")
        asset_class = str(query.get("asset_class") or "equity")
        if not cik:
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
                limitations=["No CIK supplied; SEC provider cannot fetch submissions/companyfacts."],
            )
        if not allow_network and "submissions_data" not in query and "companyfacts_data" not in query:
            return self.disabled_result(query, "Network disabled for this provider run; SEC attempt recorded but not fetched.")
        cik10 = "".join(ch for ch in str(cik) if ch.isdigit()).zfill(10)
        submissions_url = f"https://data.sec.gov/submissions/CIK{cik10}.json"
        facts_url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik10}.json"
        try:
            submissions_raw = query.get("submissions_data") or http_json(submissions_url)
            facts_raw = query.get("companyfacts_data")
            raw_path = storage.save_raw_json(self.provider_id, query, submissions_raw, url=submissions_url) if storage else None
            records = normalize_submissions(submissions_raw, cik10)
            annual = latest_by_form(records, ["10-K", "20-F", "40-F"])
            interim = latest_by_form(records, ["10-Q", "6-K"])
            latest_event = latest_by_form(records, ["8-K", "6-K"])
            normalized: dict[str, Any] = {
                "cik": cik10,
                "entity_name": submissions_raw.get("name"),
                "filings": records,
                "latest_annual": annual,
                "latest_interim": interim,
                "latest_event": latest_event,
            }
            if facts_raw is not None or query.get("include_companyfacts", True):
                try:
                    facts_raw = facts_raw if facts_raw is not None else http_json(facts_url)
                    normalized["companyfacts"] = normalize_companyfacts(facts_raw, query.get("metrics"))
                    if storage:
                        storage.save_raw_json(f"{self.provider_id}_companyfacts", query, facts_raw, url=facts_url)
                except Exception as exc:
                    normalized["companyfacts_error"] = str(exc)
            normalized_path = storage.save_normalized(self.provider_id, query, normalized, url=submissions_url) if storage else None
            source_date = (records[0].get("filing_date") if records else None) or None
            claims = []
            for item, label in [(annual, "latest annual filing"), (interim, "latest interim filing"), (latest_event, "latest event filing")]:
                if item:
                    claims.append(
                        {
                            "claim": f"SEC {label} for {subject}: {item.get('form')} filed {item.get('filing_date')}.",
                            "claim_type": "Reported Fact",
                            "materiality": "Decision-Critical" if label != "latest event filing" else "Important",
                            "source": item.get("document_url") or submissions_url,
                            "source_tier": "Tier 1",
                            "source_date": item.get("filing_date"),
                            "freshness": filing_freshness(item.get("filing_date"), historical_fact=True),
                            "support_status": "Supported",
                            "access": "Available",
                            "limitation": "",
                        }
                    )
            return ProviderResult(
                provider_id=self.provider_id,
                provider_name=self.provider_name,
                source_tier=self.source_tier,
                source_type=self.source_type,
                asset_class=asset_class,
                subject=subject,
                query=query,
                url=submissions_url,
                status="ok" if records else "missing",
                access_status="Available" if records else "Not Found",
                freshness_status=filing_freshness(source_date, historical_fact=True),
                source_date=source_date,
                raw_path=raw_path,
                normalized_path=normalized_path,
                normalized_data=normalized,
                claims=claims,
                limitations=[] if records else ["SEC submissions contained no supported recent filing forms."],
                metadata={"facts_url": facts_url},
            )
        except Exception as exc:
            return self.error_result(query, exc, url=submissions_url)
