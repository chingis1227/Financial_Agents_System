"""Snapshot builders for QUICK data runs."""

from __future__ import annotations

import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .identity import QUICK_ASSET_IDENTITIES, detect_quick_asset_identity, quick_fixture_slug, quick_identity_slug
from .providers import ProviderResult, provider_result_from_disabled, run_price_provider, run_sec_filings_provider, safe_now_iso, source_record
from .quality import answers_require_freshness
from .registry import all_providers, disabled_api_slots, provider_snapshot, providers_for, static_context_for_ticker

try:
    from data_providers import provider_plan_for_route, provider_registry_snapshot
except ImportError:  # pragma: no cover - package import path fallback
    from automation_lab.data_providers import provider_plan_for_route, provider_registry_snapshot

LAB_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_QUICK_DATA_RUNS_DIR = LAB_ROOT / "data_runs" / "quick"
DEFAULT_QUICK_FIXTURES_DIR = LAB_ROOT / "fixtures" / "quick"
QUICK_DATA_RUNS_DIR_ENV = "FA_AUTOMATION_QUICK_DATA_RUNS_DIR"
QUICK_FIXTURES_DIR_ENV = "FA_AUTOMATION_QUICK_FIXTURES_DIR"
SNAPSHOT_SCHEMA_VERSION = "quick_source_snapshot.v1.1"
SOURCE_SCOPE = "Public-Data Only"
EVIDENCE_ALIGNMENT = "Quick snapshot only; not an Evidence Collector evidence_pack"


def normalize_quick_prompt(prompt: str) -> str:
    stripped = prompt.strip()
    if stripped.lower().startswith("quick:"):
        return stripped
    return f"QUICK: {stripped}"


def safe_now_iso_microseconds() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="microseconds")


def safe_timestamp_for_path(timestamp: str) -> str:
    return timestamp.replace(":", "").replace("+", "p").replace("-", "")


def get_quick_data_runs_dir() -> Path:
    override = os.environ.get(QUICK_DATA_RUNS_DIR_ENV)
    return Path(override) if override else DEFAULT_QUICK_DATA_RUNS_DIR


def get_quick_fixtures_dir() -> Path:
    override = os.environ.get(QUICK_FIXTURES_DIR_ENV)
    return Path(override) if override else DEFAULT_QUICK_FIXTURES_DIR


def create_quick_run_dir(identity: dict[str, Any] | None, data_runs_dir: Path | None = None) -> Path:
    timestamp = safe_timestamp_for_path(safe_now_iso_microseconds())
    asset = quick_identity_slug(identity)
    run_dir = (data_runs_dir or get_quick_data_runs_dir()) / f"{timestamp}-{asset}"
    run_dir.mkdir(parents=True, exist_ok=False)
    return run_dir


def load_mock_quick_fixture(identity_or_ticker: dict[str, Any] | str) -> dict[str, Any]:
    fixture_path = get_quick_fixtures_dir() / f"{quick_fixture_slug(identity_or_ticker)}_public_snapshot.json"
    with fixture_path.open("r", encoding="utf-8-sig") as file:
        fixture = json.load(file)
    if not isinstance(fixture, dict):
        raise ValueError("quick-answer mock fixture must be a JSON object")
    return fixture


def _base_snapshot_fields() -> dict[str, Any]:
    return {
        "schema_version": SNAPSHOT_SCHEMA_VERSION,
        "providers": provider_snapshot(),
        "data_provider_registry": provider_registry_snapshot(),
        "data_provider_plan": [],
        "provider_results": [],
        "provider_errors": [],
        "source_scope": SOURCE_SCOPE,
        "evidence_alignment": EVIDENCE_ALIGNMENT,
    }


def _route_for_quick_identity(identity: dict[str, Any] | None) -> str | None:
    security_type = (identity or {}).get("security_type")
    return {
        "equity": "equity_full_cycle",
        "etf": "etf_full_cycle",
        "bond_etf": "fixed_income_full_cycle",
        "commodity_etf": "commodity_full_cycle",
        "crypto": "crypto_full_cycle",
        "multi_asset_comparison": "multi_asset_comparison",
    }.get(str(security_type))


def _data_provider_plan_for_identity(identity: dict[str, Any] | None) -> list[dict[str, Any]]:
    route = _route_for_quick_identity(identity)
    return provider_plan_for_route(route) if route else []


def provider_results_to_sources(results: list[ProviderResult]) -> list[dict[str, Any]]:
    sources = []
    for result in results:
        if result.source_record:
            sources.append(result.source_record)
    return sources


def provider_results_snapshot(results: list[ProviderResult]) -> list[dict[str, Any]]:
    return [result.to_snapshot() for result in results]


def provider_errors_snapshot(results: list[ProviderResult]) -> list[dict[str, Any]]:
    errors = []
    for result in results:
        if result.status == "error" or (result.status == "missing" and result.error):
            errors.append({"provider_id": result.provider_id, "component": result.component, "status": result.status, "error": result.error})
    return errors


def disabled_api_results() -> list[ProviderResult]:
    return [provider_result_from_disabled(provider, (provider.components[0] if provider.components else "unknown")) for provider in disabled_api_slots()]


def quick_component_missing(components: dict[str, Any], identity: dict[str, Any] | None) -> list[str]:
    security_type = (identity or {}).get("security_type")
    required = ["identity", "price", "recent_events", "valuation_context", "risk_signal"]
    if security_type == "equity":
        required.insert(1, "filings")
    if security_type in {"etf", "bond_etf", "commodity_etf", "crypto"}:
        required.append("asset_context")
    if security_type == "multi_asset_comparison":
        required = ["identity", "components", "price", "recent_events", "valuation_context", "risk_signal", "comparison_context"]
    return [key for key in required if components.get(key) in (None, [], {}, "")]


def quick_retrieved_map(components: dict[str, Any]) -> dict[str, bool]:
    return {key: value not in (None, [], {}, "") for key, value in components.items()}


def static_context_for_identity(identity: dict[str, Any]) -> dict[str, Any]:
    return static_context_for_ticker(identity.get("ticker"))


def comparison_fixture_components(identity: dict[str, Any], fixture: dict[str, Any]) -> dict[str, Any]:
    components = fixture.get("components") or identity.get("components")
    return {
        "identity": identity,
        "components": components,
        "filings": fixture.get("filings"),
        "price": fixture.get("price"),
        "recent_events": fixture.get("recent_events"),
        "valuation_context": fixture.get("valuation_context"),
        "risk_signal": fixture.get("risk_signal"),
        "comparison_context": fixture.get("comparison_context"),
    }


def quick_components_from_fixture(identity: dict[str, Any], fixture: dict[str, Any]) -> dict[str, Any]:
    if identity.get("security_type") == "multi_asset_comparison":
        return comparison_fixture_components(identity, fixture)
    context = static_context_for_identity(identity)
    return {
        "identity": identity,
        "filings": fixture.get("filings"),
        "price": fixture.get("price"),
        "recent_events": fixture.get("recent_events", context.get("recent_events")),
        "valuation_context": fixture.get("valuation_context", context.get("valuation_context")),
        "risk_signal": fixture.get("risk_signal", context.get("risk_signal")),
        "asset_context": fixture.get("asset_context", context.get("asset_context")),
    }


def empty_quick_snapshot(
    *,
    prompt: str,
    normalized_prompt: str,
    answers: list[str],
    timestamp: str,
    mode: str,
    missing: list[str],
    access_status: str,
    freshness_status: str,
    reason: str,
    identity: dict[str, Any] | None = None,
) -> dict[str, Any]:
    result = ProviderResult(
        provider_id="prompt_identity",
        component="identity",
        status="missing" if identity is None else "ok",
        data=identity,
        source_record=source_record("identity", "prompt parser", access_status, detail=reason),
        error=reason if identity is None else None,
        retrieved_at=safe_now_iso(),
        source_date=None,
        freshness_status=freshness_status,
        quality_level="failed" if identity is None else "static_context",
    )
    provider_results = [result, *disabled_api_results()]
    return {
        **_base_snapshot_fields(),
        "data_provider_plan": _data_provider_plan_for_identity(identity),
        "prompt": prompt,
        "normalized_prompt": normalized_prompt,
        "user_answers": answers,
        "mode": mode,
        "timestamp": timestamp,
        "asset_identity": identity,
        "answer_freshness_required": answers_require_freshness(answers),
        "data": {
            "identity": identity,
            "filings": None,
            "price": None,
            "recent_events": None,
            "valuation_context": None,
            "risk_signal": None,
            "asset_context": None,
            "comparison_context": None,
            "components": identity.get("components") if identity else None,
        },
        "sources": provider_results_to_sources(provider_results),
        "retrieved": {
            "identity": identity is not None,
            "filings": False,
            "price": False,
            "recent_events": False,
            "valuation_context": False,
            "risk_signal": False,
            "asset_context": False,
            "comparison_context": False,
            "components": bool(identity and identity.get("components")),
        },
        "missing": missing,
        "not_obtained": missing,
        "access_status": access_status,
        "freshness_status": freshness_status,
        "reason": reason,
        "provider_results": provider_results_snapshot(provider_results),
        "provider_errors": provider_errors_snapshot(provider_results),
    }


def build_mock_source_snapshot(prompt: str, normalized_prompt: str, answers: list[str]) -> dict[str, Any]:
    identity = detect_quick_asset_identity(normalized_prompt)
    timestamp = safe_now_iso()
    if identity is None:
        return empty_quick_snapshot(
            prompt=prompt,
            normalized_prompt=normalized_prompt,
            answers=answers,
            timestamp=timestamp,
            mode="mock",
            missing=["identity", "price", "recent_events", "valuation_context", "risk_signal"],
            access_status="blocked",
            freshness_status="blocked",
            reason="Asset identity could not be determined from the prompt.",
        )

    try:
        fixture = load_mock_quick_fixture(identity)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        return empty_quick_snapshot(
            prompt=prompt,
            normalized_prompt=normalized_prompt,
            answers=answers,
            timestamp=timestamp,
            mode="mock",
            missing=["fixture", "price", "recent_events", "valuation_context", "risk_signal"],
            access_status="blocked",
            freshness_status="blocked",
            reason=f"Mock fixture unavailable or invalid: {exc}",
            identity=identity,
        )

    components = quick_components_from_fixture(identity, fixture)
    missing = quick_component_missing(components, identity)
    fixture_sources = fixture.get("sources") if isinstance(fixture.get("sources"), list) else []
    provider_results = [
        ProviderResult(
            provider_id="mock_fixture",
            component="snapshot",
            status="ok" if not missing else "missing",
            data={"fixture": quick_fixture_slug(identity)},
            source_record=source_record("snapshot", "Mock QUICK fixture", "ok" if not missing else "missing", detail=f"missing: {', '.join(missing)}" if missing else "fixture complete"),
            error=None if not missing else f"missing fixture fields: {', '.join(missing)}",
            retrieved_at=safe_now_iso(),
            source_date=timestamp[:10],
            freshness_status="fixture_dated",
            quality_level="mock" if not missing else "failed",
        ),
        *disabled_api_results(),
    ]
    sources = fixture_sources or provider_results_to_sources(provider_results)
    return {
        **_base_snapshot_fields(),
        "data_provider_plan": _data_provider_plan_for_identity(identity),
        "prompt": prompt,
        "normalized_prompt": normalized_prompt,
        "user_answers": answers,
        "mode": "mock",
        "timestamp": timestamp,
        "asset_identity": identity,
        "answer_freshness_required": answers_require_freshness(answers),
        "data": components,
        "sources": sources,
        "retrieved": quick_retrieved_map(components),
        "missing": missing,
        "not_obtained": missing,
        "access_status": "ok" if not missing else "partial",
        "freshness_status": "mock_current" if not missing else "limited",
        "provider_results": provider_results_snapshot(provider_results),
        "provider_errors": provider_errors_snapshot(provider_results),
    }


def _first_ok_result(results: list[ProviderResult], component: str) -> ProviderResult | None:
    for result in results:
        if result.component == component and result.status == "ok" and result.data not in (None, [], {}, ""):
            return result
    return None


def collect_price_by_registry(ticker: str, asset_type: str | None) -> tuple[dict[str, Any] | None, list[ProviderResult]]:
    results: list[ProviderResult] = []
    for provider in providers_for("price", asset_type=asset_type, include_disabled=False):
        if provider.provider_type != "public":
            continue
        result = run_price_provider(provider, ticker)
        results.append(result)
        if result.status == "ok" and result.data:
            break
    return (_first_ok_result(results, "price").data if _first_ok_result(results, "price") else None), results


def build_live_source_snapshot(prompt: str, normalized_prompt: str, answers: list[str]) -> dict[str, Any]:
    identity = detect_quick_asset_identity(normalized_prompt)
    timestamp = safe_now_iso()
    if identity is None:
        return empty_quick_snapshot(
            prompt=prompt,
            normalized_prompt=normalized_prompt,
            answers=answers,
            timestamp=timestamp,
            mode="live",
            missing=["identity", "price", "recent_events", "valuation_context", "risk_signal"],
            access_status="blocked",
            freshness_status="blocked",
            reason="Asset identity could not be determined from the prompt.",
        )

    if identity.get("security_type") == "multi_asset_comparison":
        return build_live_comparison_snapshot(prompt, normalized_prompt, answers, identity, timestamp)

    ticker = str(identity.get("ticker"))
    asset_type = str(identity.get("security_type"))
    context = static_context_for_identity(identity)
    provider_results: list[ProviderResult] = [
        ProviderResult(
            provider_id="identity_seed",
            component="identity",
            status="ok",
            data=identity,
            source_record=source_record("identity", identity.get("source", "Automation Lab identity seed"), "ok", detail=f"{ticker} quick identity recognized"),
            retrieved_at=safe_now_iso(),
            source_date=None,
            freshness_status="structural",
            quality_level="static_context",
        )
    ]

    filings: list[dict[str, Any]] | None = None
    recent_events: list[dict[str, Any]] | None = context.get("recent_events")
    valuation_context: dict[str, Any] | None = context.get("valuation_context")
    risk_signal: dict[str, Any] | None = context.get("risk_signal")
    asset_context: dict[str, Any] | None = context.get("asset_context")

    if asset_context or valuation_context or risk_signal or recent_events:
        provider_results.append(
            ProviderResult(
                provider_id="static_quick_context",
                component="asset_context",
                status="ok",
                data=context,
                source_record=source_record("asset_context", "Automation Lab static quick context", "ok", detail="structural context only"),
                retrieved_at=safe_now_iso(),
                source_date=None,
                freshness_status="structural_only",
                quality_level="static_context",
            )
        )

    if identity.get("cik"):
        sec_providers = providers_for("filings", asset_type=asset_type, include_disabled=False)
        sec_provider = next((provider for provider in sec_providers if provider.provider_id == "sec_submissions"), None)
        if sec_provider:
            sec_result = run_sec_filings_provider(sec_provider, identity["cik"])
            provider_results.append(sec_result)
            if sec_result.status == "ok" and sec_result.data:
                filings = sec_result.data
                recent_events = filings[:3]

    price_ticker = str(identity.get("price_ticker") or ticker)
    price, price_results = collect_price_by_registry(price_ticker, asset_type)
    for price_result in price_results:
        if price_result.data and price_ticker != ticker:
            price_result.data["ticker"] = ticker
    provider_results.extend(price_results)

    if price and valuation_context:
        valuation_context = {**valuation_context, "price_reference": price}
    elif price:
        valuation_context = {
            "summary": "Fast context only: public price reference is available; no full valuation model was run.",
            "price_reference": price,
            "source": "Automation Lab quick context from public price source",
        }
    if not risk_signal and (filings or price or asset_context):
        risk_signal = {
            "summary": "Main limitation: QUICK only sees a narrow public snapshot and does not complete valuation, risk, portfolio, or IC gates.",
            "source": "Automation Lab quick rule layer",
        }

    provider_results.extend(disabled_api_results())
    components = {
        "identity": identity,
        "filings": filings,
        "price": price,
        "recent_events": recent_events,
        "valuation_context": valuation_context,
        "risk_signal": risk_signal,
        "asset_context": asset_context,
    }
    missing = quick_component_missing(components, identity)
    return {
        **_base_snapshot_fields(),
        "data_provider_plan": _data_provider_plan_for_identity(identity),
        "prompt": prompt,
        "normalized_prompt": normalized_prompt,
        "user_answers": answers,
        "mode": "live",
        "timestamp": timestamp,
        "asset_identity": identity,
        "answer_freshness_required": answers_require_freshness(answers),
        "data": components,
        "sources": provider_results_to_sources(provider_results),
        "retrieved": quick_retrieved_map(components),
        "missing": missing,
        "not_obtained": missing,
        "access_status": "ok" if not missing else "partial",
        "freshness_status": "public_best_effort" if not missing else "limited",
        "provider_results": provider_results_snapshot(provider_results),
        "provider_errors": provider_errors_snapshot(provider_results),
    }


def build_live_comparison_snapshot(
    prompt: str,
    normalized_prompt: str,
    answers: list[str],
    identity: dict[str, Any],
    timestamp: str,
) -> dict[str, Any]:
    provider_results: list[ProviderResult] = [
        ProviderResult(
            provider_id="identity_seed",
            component="identity",
            status="ok",
            data=identity,
            source_record=source_record("identity", identity.get("source", "Automation Lab comparison seed"), "ok", detail="MSFT vs SPY vs BTC comparison recognized"),
            retrieved_at=safe_now_iso(),
            freshness_status="structural",
            quality_level="static_context",
        ),
        ProviderResult(
            provider_id="static_quick_context",
            component="comparison_context",
            status="ok",
            data={"summary": "MSFT is company-specific equity risk; SPY is broad U.S. equity beta; BTC is high-volatility crypto exposure."},
            source_record=source_record("comparison_context", "Automation Lab static comparison context", "ok", detail="structural comparison context only"),
            retrieved_at=safe_now_iso(),
            freshness_status="structural_only",
            quality_level="static_context",
        ),
    ]
    component_rows: list[dict[str, Any]] = []
    price_rows: list[dict[str, Any]] = []
    explicit_missing: list[str] = []
    for component in identity.get("components", []):
        ticker = component.get("ticker")
        component_rows.append(component)
        asset_identity = QUICK_ASSET_IDENTITIES.get(str(ticker), {})
        price_ticker = asset_identity.get("price_ticker", ticker)
        price, price_results = collect_price_by_registry(str(price_ticker), str(component.get("security_type")))
        for price_result in price_results:
            provider_results.append(price_result)
        if price:
            price_rows.append({"ticker": ticker, "price": price})
        else:
            explicit_missing.append(f"price:{ticker}")
    components = {
        "identity": identity,
        "components": component_rows,
        "filings": None,
        "price": {"components": price_rows, "source": "public price providers best effort"} if price_rows else None,
        "recent_events": [{"type": "comparison context", "description": "Compares single-name equity risk, broad equity beta, and crypto volatility.", "source_identifier": "Automation Lab static comparison context"}],
        "valuation_context": {"summary": "Fast comparison only: no full valuation, fund, crypto, or portfolio model was run.", "source": "Automation Lab static comparison context"},
        "risk_signal": {"summary": "Main limit: this comparison is preliminary and not portfolio-personalized; cross-asset risk needs full workflow review.", "source": "Automation Lab static comparison context"},
        "comparison_context": {"summary": "MSFT is company-specific equity risk; SPY is broad U.S. equity beta; BTC is high-volatility crypto exposure.", "source": "Automation Lab static comparison context"},
    }
    provider_results.extend(disabled_api_results())
    component_missing = quick_component_missing(components, identity)
    missing = list(dict.fromkeys([*component_missing, *explicit_missing]))
    return {
        **_base_snapshot_fields(),
        "data_provider_plan": _data_provider_plan_for_identity(identity),
        "prompt": prompt,
        "normalized_prompt": normalized_prompt,
        "user_answers": answers,
        "mode": "live",
        "timestamp": timestamp,
        "asset_identity": identity,
        "answer_freshness_required": answers_require_freshness(answers),
        "data": components,
        "sources": provider_results_to_sources(provider_results),
        "retrieved": quick_retrieved_map(components),
        "missing": missing,
        "not_obtained": missing,
        "access_status": "ok" if not missing else "partial",
        "freshness_status": "public_best_effort" if not missing else "limited",
        "provider_results": provider_results_snapshot(provider_results),
        "provider_errors": provider_errors_snapshot(provider_results),
    }


def build_quick_source_snapshot(prompt: str, answers: list[str], mode: str) -> dict[str, Any]:
    normalized_prompt = normalize_quick_prompt(prompt)
    if mode == "mock":
        return build_mock_source_snapshot(prompt, normalized_prompt, answers)
    if mode == "live":
        return build_live_source_snapshot(prompt, normalized_prompt, answers)
    raise ValueError(f"Unsupported quick-answer mode: {mode}")
