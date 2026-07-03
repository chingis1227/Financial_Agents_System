"""Global public-equity source preflight for TASK-013 AGENT."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path
from typing import Any

from .source_fetchers import now_iso, sec_company_facts, sec_submissions, stooq_history, stooq_quote, yahoo_chart
from .document_parser import parse_document
from .equity_resolver import clean_resolved_identity, resolve_equity_request
from .source_registry import (
    SOURCE_REGISTRY,
    source_registry_snapshot,
    supported_equity_identity,
    supported_equity_metadata,
)

try:
    from data_providers import run_provider_registry_for_preflight
except ImportError:  # pragma: no cover - package import path fallback
    from automation_lab.data_providers import run_provider_registry_for_preflight

LAB_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_AGENT_FIXTURES = {
    "MSFT": LAB_ROOT / "fixtures" / "agent" / "msft_deep_equity_pack.json",
    "AAPL": LAB_ROOT / "fixtures" / "agent" / "aapl_deep_equity_pack.json",
}


def source_record(
    source_id: str,
    status: str,
    data: Any = None,
    url: str | None = None,
    error: str | None = None,
    fallback_used: str | None = None,
    source_date: str | None = None,
) -> dict[str, Any]:
    definition = next(source for source in SOURCE_REGISTRY if source.source_id == source_id)
    return {
        "source_id": source_id,
        "name": definition.name,
        "category": definition.category,
        "importance": definition.importance,
        "status": status,
        "primary": definition.primary,
        "fallbacks": list(definition.fallbacks),
        "fallback_used": fallback_used,
        "url": url,
        "source_date": source_date,
        "retrieved_at": now_iso(),
        "freshness_rule": definition.freshness_rule,
        "access_status": "Available" if status == "ok" else "Not Found" if status == "missing" else "Inaccessible" if status == "error" else "Partial",
        "source_tier": "Tier 1" if definition.category in {"filings", "fundamentals", "identity"} else "Tier 2" if definition.category == "market_data" else "Tier 3" if definition.category == "events" else "Tier 2",
        "data": data,
        "error": error,
    }


def provider_result(record: dict[str, Any], provider_id: str | None = None, order: int | None = None) -> dict[str, Any]:
    return {
        "provider_id": provider_id or str(record.get("fallback_used") or record.get("primary") or "unknown").lower().replace(" ", "_"),
        "source_id": record.get("source_id"),
        "provider": record.get("fallback_used") or record.get("primary"),
        "url": record.get("url"),
        "status": record.get("status"),
        "source_date": record.get("source_date"),
        "retrieved_at": record.get("retrieved_at"),
        "quality_tier": record.get("source_tier"),
        "extracted_fields": sorted((record.get("data") or {}).keys()) if isinstance(record.get("data"), dict) else [],
        "limitations": record.get("error"),
        "attempt_order": order,
    }


def _latest_form(records: list[dict[str, Any]], form: str) -> dict[str, Any] | None:
    for record in records:
        if record.get("form") == form:
            return record
    return None


def _stamp_mock_records(records: list[dict[str, Any]], timestamp: str) -> list[dict[str, Any]]:
    stamped = []
    for record in records:
        merged = {**record}
        merged.setdefault("retrieved_at", timestamp)
        if merged.get("status") == "ok" and merged.get("source_id") in {
            "current_price", "historical_price", "recent_8k", "ir_news", "public_news"
        }:
            stable_date = date.today().isoformat()
            merged["source_date"] = stable_date
            if isinstance(merged.get("data"), dict) and "date" in merged["data"]:
                merged["data"] = {**merged["data"], "date": stable_date}
            if isinstance(merged.get("data"), dict) and isinstance(merged["data"].get("points"), list) and merged["data"]["points"]:
                points = list(merged["data"]["points"])
                points[-1] = {**points[-1], "date": stable_date}
                merged["data"] = {**merged["data"], "points": points}
        stamped.append(merged)
    return stamped


def _generic_mock_records(identity: dict[str, Any]) -> list[dict[str, Any]]:
    today = date.today().isoformat()
    ticker = identity.get("ticker", "EQUITY")
    cik = identity.get("cik")
    issuer_url = identity.get("ir_url") or f"https://www.google.com/search?q={ticker}+investor+relations"
    sec_url = f"https://data.sec.gov/submissions/CIK{str(cik).zfill(10)}.json" if cik else issuer_url
    return [
        source_record("identity", "ok", clean_resolved_identity(identity), url=issuer_url, source_date=today),
        source_record("sec_submissions", "ok", {"test_only": True, "coverage": "SEC submissions or issuer filings candidate"}, url=sec_url, source_date=today, fallback_used="TASK-013 generic mock"),
        source_record("latest_10k", "ok", {"test_only": True, "form": "10-K/20-F/annual report proxy"}, url=sec_url, source_date=today, fallback_used="TASK-013 generic mock"),
        source_record("latest_10q", "ok", {"test_only": True, "form": "10-Q/6-K/interim report proxy"}, url=sec_url, source_date=today, fallback_used="TASK-013 generic mock"),
        source_record("recent_8k", "missing", None, url=sec_url, source_date=today, error="No recent event required in generic mock; absence of 8-K alone is not a hard gate."),
        source_record("company_facts", "ok", {"test_only": True, "facts": {}}, url=sec_url, source_date=today, fallback_used="TASK-013 generic mock"),
        source_record("current_price", "ok", {"date": today, "close": "100.00", "test_only": True}, url=f"mock://price/{ticker}", source_date=today, fallback_used="TASK-013 generic mock"),
        source_record("historical_price", "ok", {"points": [{"date": today, "close": 100.0}], "test_only": True}, url=f"mock://history/{ticker}", source_date=today, fallback_used="TASK-013 generic mock"),
        source_record("filing_text", "ok", {"document_url": sec_url, "test_only": True}, url=sec_url, source_date=today, fallback_used="TASK-013 generic mock"),
        source_record("ir_news", "ok", {"test_only": True, "source": "issuer IR candidate"}, url=issuer_url, source_date=today, fallback_used="TASK-013 generic mock"),
        source_record("public_news", "ok", {"test_only": True, "source": "public search candidate"}, url=f"https://www.google.com/search?q={ticker}+news", source_date=today, fallback_used="TASK-013 generic mock"),
        source_record("peer_context", "ok", {"peers": [], "basis": "generic public equity peer context", "test_only": True}, url=f"mock://peer/{ticker}", source_date=today),
        source_record("sector_context", "ok", {"sector": "Unknown", "test_only": True}, url=f"mock://sector/{ticker}", source_date=today),
        source_record("macro_rates", "ok", {"drivers": ["rates", "FX", "risk appetite"], "test_only": True}, url="https://home.treasury.gov/", source_date=today),
        source_record("secondary_market_pages", "missing", None, url=None, error="nice-to-have not fetched in generic mock"),
        source_record("additional_presentations", "missing", None, url=issuer_url, error="nice-to-have not fetched in generic mock"),
    ]


def attach_provider_results(preflight: dict[str, Any], extra_results: list[dict[str, Any]] | None = None) -> dict[str, Any]:
    results = extra_results or []
    offset = len(results)
    results.extend(provider_result(record, order=offset + index + 1) for index, record in enumerate(preflight.get("source_records", [])))
    preflight["provider_results"] = results
    return preflight


def attach_data_provider_registry(preflight: dict[str, Any], *, route: str = "equity_full_cycle") -> dict[str, Any]:
    """Attach production provider-layer attempts without disturbing legacy preflight fields."""

    try:
        registry_run = run_provider_registry_for_preflight(
            route=route,
            identity=preflight.get("subject_identity") or {},
            mode=str(preflight.get("mode") or "mock"),
            persist=False,
        )
    except Exception as exc:  # pragma: no cover - registry must never break legacy preflight
        registry_run = {"provider_registry": [], "provider_plan": [], "provider_results": [], "data_run_artifacts": {}, "error": str(exc)}
    preflight["data_provider_registry"] = registry_run.get("provider_registry", [])
    preflight["data_provider_plan"] = registry_run.get("provider_plan", [])
    preflight["data_provider_results"] = registry_run.get("provider_results", [])
    preflight["data_run_artifacts"] = registry_run.get("data_run_artifacts", {})
    return preflight


def _mock_preflight(prompt: str, answers: list[str], ticker: str, resolved_identity: dict[str, Any] | None = None) -> dict[str, Any]:
    normalized_ticker = ticker.upper()
    timestamp = now_iso()
    if normalized_ticker in DEFAULT_AGENT_FIXTURES:
        fixture_path = DEFAULT_AGENT_FIXTURES[normalized_ticker]
        data = json.loads(fixture_path.read_text(encoding="utf-8-sig"))
        identity = data["subject_identity"]
        resolver_identity = resolved_identity or resolve_equity_request(prompt, mode="mock")
        identity = {**resolver_identity, **identity}
        records = _stamp_mock_records(data["source_records"], timestamp)
    else:
        identity = resolved_identity or resolve_equity_request(prompt, mode="mock")
        records = _generic_mock_records(identity)
    preflight = {
        "schema_version": "agent_source_preflight.v2",
        "task_id": "TASK-013",
        "mode": "mock",
        "prompt": prompt,
        "answers_count": len(answers),
        "subject_identity": clean_resolved_identity(identity),
        "resolver_result": clean_resolved_identity(identity),
        "source_scope": "Public-Data Only",
        "source_registry": source_registry_snapshot(),
        "source_records": records,
        "retrieved_at": timestamp,
        "mock_disclaimer": "TASK-013 generic mock is test-only and not real investment analysis.",
        "freshness_policy": {
            "mock_fixture_rule": "fixture dates are deterministic for tests; generic mock is synthetic and test-only",
            "live_current_rule": "latest/current claims require latest available market close or current-session timestamp where public provider supplies it",
        },
    }
    return attach_provider_results(preflight)


def _static_context_records(ticker: str, identity: dict[str, Any] | None = None) -> list[dict[str, Any]]:
    normalized_ticker = ticker.upper()
    try:
        metadata = supported_equity_metadata(normalized_ticker)
    except KeyError:
        metadata = identity or {"ticker": normalized_ticker}
    ir_url = metadata.get("ir_url")
    return [
        source_record(
            "peer_context",
            "ok",
            metadata.get("peer_context"),
            url=f"static://agent/{normalized_ticker.lower()}/peer_context",
            fallback_used="static peer context",
            source_date=str(date.today()),
        ),
        source_record(
            "sector_context",
            "ok",
            metadata.get("sector_context"),
            url=f"static://agent/{normalized_ticker.lower()}/sector_context",
            fallback_used="static sector context",
            source_date=str(date.today()),
        ),
        source_record(
            "macro_rates",
            "ok",
            metadata.get("macro_context"),
            url="https://home.treasury.gov/",
            fallback_used="static rates context",
            source_date=str(date.today()),
        ),
        source_record("secondary_market_pages", "missing", None, url=None, error="nice-to-have not fetched in TASK-013"),
        source_record("additional_presentations", "missing", None, url=ir_url, error="nice-to-have not fetched in TASK-013"),
    ]


def _live_preflight(prompt: str, answers: list[str], ticker: str, resolved_identity: dict[str, Any] | None = None) -> dict[str, Any]:
    normalized_ticker = ticker.upper()
    identity = resolved_identity or resolve_equity_request(prompt, mode="live")
    metadata = identity
    cik = identity.get("cik")
    cik_compact = str(int("".join(ch for ch in str(cik) if ch.isdigit()))) if cik else ""
    timestamp = now_iso()
    records: list[dict[str, Any]] = [
        source_record("identity", "ok", clean_resolved_identity(identity), url=f"https://www.sec.gov/edgar/browse/?CIK={cik_compact}" if cik_compact else identity.get("ir_url"))
    ]
    filings_records: list[dict[str, Any]] = []
    try:
        if not cik:
            raise ValueError("No SEC CIK available; using issuer/regulator public filing candidates")
        submissions = sec_submissions(str(cik))
        filings_records = submissions["records"]
        records.append(source_record("sec_submissions", "ok", {"records": filings_records[:12], "raw_name": submissions.get("raw_name")}, url=submissions["url"], source_date=filings_records[0].get("filing_date") if filings_records else None))
        annual_forms = ["20-F", "40-F", "10-K"] if identity.get("instrument_classification") == "adr_or_foreign_issuer_us_listing" else ["10-K", "20-F", "40-F"]
        interim_forms = ["6-K", "10-Q"] if identity.get("instrument_classification") == "adr_or_foreign_issuer_us_listing" else ["10-Q", "6-K"]
        annual = next((_latest_form(filings_records, form) for form in annual_forms if _latest_form(filings_records, form)), None)
        interim = next((_latest_form(filings_records, form) for form in interim_forms if _latest_form(filings_records, form)), None)
        latest_8k = _latest_form(filings_records, "8-K") or _latest_form(filings_records, "6-K")
        records.append(source_record("latest_10k", "ok" if annual else "missing", annual, url=annual.get("document_url") if annual else submissions["url"], error=None if annual else f"No annual filing found in recent SEC records ({'/'.join(annual_forms)})", source_date=annual.get("filing_date") if annual else None, fallback_used="20-F/40-F annual filing" if annual and annual.get("form") in {"20-F", "40-F"} else None))
        records.append(source_record("latest_10q", "ok" if interim else "missing", interim, url=interim.get("document_url") if interim else submissions["url"], error=None if interim else f"No interim filing found in recent SEC records ({'/'.join(interim_forms)})", source_date=interim.get("filing_date") if interim else None, fallback_used="6-K interim filing" if interim and interim.get("form") == "6-K" else None))
        records.append(source_record("recent_8k", "ok" if latest_8k else "missing", latest_8k, url=latest_8k.get("document_url") if latest_8k else submissions["url"], error=None if latest_8k else "No 8-K/6-K found in recent SEC records", source_date=latest_8k.get("filing_date") if latest_8k else None, fallback_used="6-K foreign issuer event filing" if latest_8k and latest_8k.get("form") == "6-K" else None))
        latest_doc = annual or interim
        records.append(source_record("filing_text", "ok" if latest_doc and latest_doc.get("document_url") else "missing", {"document_url": latest_doc.get("document_url")} if latest_doc else None, url=latest_doc.get("document_url") if latest_doc else submissions["url"], source_date=latest_doc.get("filing_date") if latest_doc else None))
    except Exception as exc:
        if not cik and identity.get("instrument_classification") == "non_us_listed_equity":
            issuer_url = identity.get("ir_url") or f"https://www.google.com/search?q={normalized_ticker}+annual+report"
            records.append(source_record("sec_submissions", "partial", {"proxy": "issuer/regulator filing candidate for non-US listing", "verified_document": False}, url=issuer_url, source_date=str(date.today()), fallback_used="issuer investor relations / web-search fallback", error="Non-US issuer filing page candidate recorded; exact regulator filing feed not verified."))
            records.append(source_record("latest_10k", "partial", {"proxy_form": "annual report", "verified_document": False}, url=issuer_url, source_date=str(date.today()), fallback_used="issuer annual report candidate", error="Annual report candidate exists but document extraction is not fully verified in this run."))
            records.append(source_record("latest_10q", "partial", {"proxy_form": "interim report", "verified_document": False}, url=issuer_url, source_date=str(date.today()), fallback_used="issuer interim report candidate", error="Interim report candidate exists but document extraction is not fully verified in this run."))
            records.append(source_record("recent_8k", "missing", None, url=issuer_url, error="No SEC 8-K expected for direct non-US listing; issuer events are checked through IR/news."))
            records.append(source_record("filing_text", "partial", {"document_url": issuer_url, "proxy": "issuer reports page", "verified_document": False}, url=issuer_url, source_date=str(date.today()), fallback_used="issuer reports page", error="Issuer reports page candidate recorded; full document text was not extracted."))
        else:
            for source_id in ("sec_submissions", "latest_10k", "latest_10q", "recent_8k", "filing_text"):
                records.append(source_record(source_id, "error", None, error=str(exc)))

    try:
        if not cik:
            raise ValueError("No SEC companyfacts CIK available")
        facts = sec_company_facts(str(cik))
        records.append(source_record("company_facts", "ok", {"entity_name": facts.get("entity_name"), "facts": facts.get("facts")}, url=facts["url"]))
    except Exception as exc:
        if not cik and identity.get("instrument_classification") == "non_us_listed_equity":
            issuer_url = identity.get("ir_url") or f"https://www.google.com/search?q={normalized_ticker}+financial+statements"
            records.append(source_record("company_facts", "partial", {"proxy": "issuer financial statements candidate for non-US listing", "verified_xbrl": False}, url=issuer_url, source_date=str(date.today()), fallback_used="issuer public financial statements", error="Non-US financial-statement proxy recorded; SEC companyfacts/XBRL equivalent was not available."))
        else:
            records.append(source_record("company_facts", "error", None, error=str(exc)))

    price_ticker = identity.get("price_ticker") or normalized_ticker
    price_provider_results: list[dict[str, Any]] = [
        {
            "provider_id": "stooq_history",
            "source_id": "historical_price",
            "provider": "Stooq public historical CSV",
            "status": "attempted",
            "attempt_order": 1,
            "url": None,
            "retrieved_at": timestamp,
            "quality_tier": "Tier 2",
        },
        {
            "provider_id": "official_exchange_or_issuer_quote",
            "source_id": "current_price",
            "provider": "Official exchange / issuer quote where accessible",
            "status": "not_configured",
            "attempt_order": 2,
            "url": identity.get("ir_url"),
            "retrieved_at": timestamp,
            "quality_tier": "Tier 1/2",
            "limitations": "No generic no-key official exchange quote connector is configured; issuer/IR quote pages remain source candidates.",
        },
        {
            "provider_id": "yahoo_public_chart",
            "source_id": "current_price",
            "provider": "Yahoo public chart fallback",
            "status": "not_attempted",
            "attempt_order": 3,
            "url": None,
            "retrieved_at": timestamp,
            "quality_tier": "Tier 2",
        },
    ]
    try:
        history = stooq_history(price_ticker)
        price_provider_results[0].update({"status": "ok", "url": history["url"], "source_date": history["latest"].get("date"), "extracted_fields": ["date", "close", "history"]})
        records.append(source_record("current_price", "ok", history["latest"], url=history["url"], source_date=history["latest"].get("date")))
        records.append(source_record("historical_price", "ok", {"points": history["history"][-260:]}, url=history["url"], source_date=history["latest"].get("date")))
    except Exception as stooq_exc:
        price_provider_results[0].update({"status": "error", "limitations": str(stooq_exc)})
        try:
            chart = yahoo_chart(str(price_ticker), range_value="1y", interval="1d")
            price_provider_results[2].update({"status": "ok", "url": chart["url"], "source_date": chart["latest"].get("date"), "extracted_fields": ["date", "close", "history"]})
            records.append(source_record("current_price", "ok", chart["latest"], url=chart["url"], fallback_used="Yahoo public chart", source_date=chart["latest"].get("date")))
            records.append(source_record("historical_price", "ok", {"points": chart["history"][-260:]}, url=chart["url"], fallback_used="Yahoo public chart", source_date=chart["latest"].get("date")))
        except Exception as yahoo_exc:
            price_provider_results[2].update({"status": "error", "limitations": str(yahoo_exc)})
            try:
                quote = stooq_quote(price_ticker)
                records.append(source_record("current_price", "ok", quote["latest"], url=quote["url"], fallback_used="Stooq public quote", source_date=quote["latest"].get("date")))
                records.append(source_record("historical_price", "error", None, url=quote["url"], error="Stooq history and Yahoo history unavailable; quote-only fallback is insufficient for historical price", fallback_used="Stooq quote-only"))
            except Exception as quote_exc:
                records.append(source_record("current_price", "error", None, error=f"Stooq history: {stooq_exc}; Yahoo: {yahoo_exc}; Stooq quote: {quote_exc}"))
                records.append(source_record("historical_price", "error", None, error=f"Stooq history: {stooq_exc}; Yahoo: {yahoo_exc}"))

    latest_8k = (_latest_form(filings_records, "8-K") or _latest_form(filings_records, "6-K")) if filings_records else None
    records.append(source_record("ir_news", "ok" if latest_8k else "missing", {"proxy": "SEC 8-K used as issuer-event fallback", "latest_8k": latest_8k}, url=latest_8k.get("document_url") if latest_8k else metadata.get("ir_url"), fallback_used="SEC 8-K", source_date=latest_8k.get("filing_date") if latest_8k else None))
    records.append(source_record("public_news", "ok" if latest_8k else "missing", {"event_scan": "SEC 8-K and public issuer-event fallback; no paywalled scraping", "latest_8k": latest_8k}, url=latest_8k.get("document_url") if latest_8k else None, fallback_used="SEC 8-K", source_date=latest_8k.get("filing_date") if latest_8k else None))
    records.extend(_static_context_records(normalized_ticker, identity))

    preflight = {
        "schema_version": "agent_source_preflight.v2",
        "task_id": "TASK-013",
        "mode": "live",
        "prompt": prompt,
        "answers_count": len(answers),
        "subject_identity": clean_resolved_identity(identity),
        "resolver_result": clean_resolved_identity(identity),
        "source_scope": "Public-Data Only",
        "source_registry": source_registry_snapshot(),
        "source_records": records,
        "retrieved_at": timestamp,
        "freshness_policy": {
            "mock_fixture_rule": "fixture dates are deterministic for tests",
            "live_current_rule": "latest/current claims require latest available market close or current-session timestamp where public provider supplies it; weekends/holidays use latest available close with retrieved_at timestamp",
        },
    }
    return attach_provider_results(preflight, price_provider_results)


def summarize_preflight(preflight: dict[str, Any]) -> dict[str, Any]:
    records = preflight.get("source_records", [])
    required = [record for record in records if record.get("importance") == "required"]
    important = [record for record in records if record.get("importance") == "important"]
    missing_required = [record["source_id"] for record in required if record.get("status") not in {"ok", "partial"}]
    partial_required = [record["source_id"] for record in required if record.get("status") == "partial"]
    missing_important = [record["source_id"] for record in important if record.get("status") != "ok"]
    return {
        "required_attempted": sorted({record["source_id"] for record in required}),
        "important_attempted": sorted({record["source_id"] for record in important}),
        "missing_required": missing_required,
        "partial_required": partial_required,
        "missing_important": missing_important,
        "hard_gate_passed": not missing_required,
        "limitation_needed": bool(missing_important or partial_required),
    }


def attach_parsed_documents(preflight: dict[str, Any], *, max_documents: int = 2, max_attempts: int = 2) -> dict[str, Any]:
    """Parse first safe equity filing/company-document candidates into claim-level evidence.

    Parser failures are recorded as parser warnings and never fail preflight.
    Mock and synthetic URLs are intentionally skipped to keep tests deterministic.
    """

    parsed_documents: list[dict[str, Any]] = []
    parser_warnings: list[str] = []
    attempts = 0
    candidate_ids = {"filing_text", "latest_10k", "latest_10q", "recent_8k", "ir_news", "public_news"}
    for record in preflight.get("source_records", []):
        if len(parsed_documents) >= max_documents or attempts >= max_attempts:
            break
        if record.get("source_id") not in candidate_ids or record.get("status") not in {"ok", "partial"}:
            continue
        data = record.get("data") if isinstance(record.get("data"), dict) else {}
        url = record.get("url") or data.get("document_url")
        if not isinstance(url, str) or not url.startswith(("http://", "https://")):
            continue
        if "google.com/search" in url or url.startswith("mock://"):
            continue
        attempts += 1
        source_tier = record.get("source_tier") or ("Tier 1" if record.get("category") in {"filings", "fundamentals", "company_materials"} else "Tier 3")
        parsed = parse_document(
            url,
            source_tier=source_tier,
            default_claim_type="Reported Fact" if source_tier == "Tier 1" else "News Report",
            company=(preflight.get("subject_identity") or {}).get("company_name"),
            timeout=12,
        )
        parsed["preflight_source_id"] = record.get("source_id")
        if parsed.get("source", {}).get("access_status") in {"Available", "Partial", "Unsupported"}:
            parsed_documents.append(parsed)
        if parsed.get("warnings"):
            parser_warnings.extend(f"{record.get('source_id')}: {warning}" for warning in parsed["warnings"])
    preflight["parsed_documents"] = parsed_documents
    preflight["document_parser"] = {
        "schema_version": "equity_preflight_document_parser.v1",
        "status": "available" if parsed_documents else "no_parseable_document",
        "parsed_document_count": len(parsed_documents),
        "warnings": parser_warnings,
        "boundary": "Evidence supplier only; no IC Action or recommendation.",
    }
    return preflight


def build_equity_source_preflight(prompt: str, answers: list[str], mode: str, ticker: str = "MSFT") -> dict[str, Any]:
    resolved = resolve_equity_request(prompt if prompt else ticker, mode=mode)
    normalized_ticker = str(resolved.get("ticker") or ticker).upper()
    if mode == "mock":
        preflight = _mock_preflight(prompt, answers, normalized_ticker, resolved)
    elif mode == "live":
        preflight = _live_preflight(prompt, answers, normalized_ticker, resolved)
    else:
        raise ValueError(f"Unsupported AGENT preflight mode: {mode}")
    preflight["summary"] = summarize_preflight(preflight)
    attach_data_provider_registry(preflight)
    if mode == "live":
        attach_parsed_documents(preflight)
    return preflight


def build_msft_source_preflight(prompt: str, answers: list[str], mode: str) -> dict[str, Any]:
    """Compatibility wrapper for older tests/imports."""
    return build_equity_source_preflight(prompt=prompt, answers=answers, mode=mode, ticker="MSFT")
