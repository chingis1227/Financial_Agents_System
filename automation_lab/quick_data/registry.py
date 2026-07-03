"""Provider registry for QUICK snapshots."""

from __future__ import annotations

import json
from typing import Any

from .providers import ProviderMetadata

STATIC_QUICK_CONTEXT: dict[str, dict[str, Any]] = {
    "SPY": {
        "asset_context": {
            "summary": "SPY is a broad U.S. large-cap equity ETF tracking S&P 500 exposure; expense and index context are quick wrapper checks, not a full fund review.",
            "source": "Automation Lab static ETF context",
        },
        "recent_events": [{"type": "public market context", "description": "Broad U.S. equity beta proxy; current weights require full source review.", "source_identifier": "Automation Lab static ETF context"}],
        "valuation_context": {"summary": "Fast context only: broad equity market beta and public price reference; no valuation model was run.", "source": "Automation Lab static ETF context"},
        "risk_signal": {"summary": "Main limit: broad equity drawdown and mega-cap concentration can dominate SPY outcomes; QUICK does not complete fund due diligence.", "source": "Automation Lab static ETF context"},
    },
    "BTC": {
        "asset_context": {"summary": "BTC is a crypto asset with high volatility; QUICK treats price and market context as a narrow public snapshot.", "source": "Automation Lab static crypto context"},
        "recent_events": [{"type": "public market context", "description": "Crypto market context is volatile and freshness-sensitive; protocol, custody, and regulatory checks are not complete.", "source_identifier": "Automation Lab static crypto context"}],
        "valuation_context": {"summary": "Fast context only: crypto price reference and volatility context; no token economics or valuation model was run.", "source": "Automation Lab static crypto context"},
        "risk_signal": {"summary": "Main limit: BTC carries high volatility, regulatory, custody, and liquidity assumptions that QUICK does not fully test.", "source": "Automation Lab static crypto context"},
    },
    "TLT": {
        "asset_context": {"summary": "TLT is a long-duration U.S. Treasury bond ETF where rate sensitivity and duration are central quick checks.", "source": "Automation Lab static bond ETF context"},
        "recent_events": [{"type": "public market context", "description": "Long-duration Treasury exposure is sensitive to rate moves; yield curve and distribution details need full review.", "source_identifier": "Automation Lab static bond ETF context"}],
        "valuation_context": {"summary": "Fast context only: duration and rate sensitivity frame the instrument; no fixed-income model was run.", "source": "Automation Lab static bond ETF context"},
        "risk_signal": {"summary": "Main limit: TLT can move sharply when long rates change; QUICK does not complete duration, curve, or income analysis.", "source": "Automation Lab static bond ETF context"},
    },
    "GLD": {
        "asset_context": {"summary": "GLD is a gold exposure vehicle and commodity proxy, not an operating business with cash-flow fundamentals.", "source": "Automation Lab static commodity ETF context"},
        "recent_events": [{"type": "public market context", "description": "Gold exposure is sensitive to real rates, USD, risk appetite, and commodity flows; QUICK does not complete commodity work.", "source_identifier": "Automation Lab static commodity ETF context"}],
        "valuation_context": {"summary": "Fast context only: gold exposure and public price reference; no commodity balance or macro model was run.", "source": "Automation Lab static commodity ETF context"},
        "risk_signal": {"summary": "Main limit: GLD has gold price volatility and no operating-business cash-flow anchor; real-rate sensitivity needs full analysis.", "source": "Automation Lab static commodity ETF context"},
    },
}

PROVIDER_REGISTRY: tuple[ProviderMetadata, ...] = (
    ProviderMetadata("prompt_identity", "Prompt identity parser", "static", ("identity",), ("equity", "etf", "crypto", "bond_etf", "commodity_etf", "multi_asset_comparison", "unknown"), "static_context", "local_static", 1, True, "structural_only"),
    ProviderMetadata("identity_seed", "Automation Lab identity seed", "static", ("identity",), ("equity", "etf", "crypto", "bond_etf", "commodity_etf", "multi_asset_comparison"), "static_context", "local_static", 2, True, "structural_only"),
    ProviderMetadata("mock_fixture", "Mock QUICK fixture", "mock", ("identity", "filings", "price", "recent_events", "valuation_context", "risk_signal", "asset_context", "comparison_context"), ("equity", "etf", "crypto", "bond_etf", "commodity_etf", "multi_asset_comparison"), "mock", "local_fixture", 10, True, "fixture_dated"),
    ProviderMetadata("static_quick_context", "Automation Lab static quick context", "static", ("recent_events", "valuation_context", "risk_signal", "asset_context", "comparison_context"), ("etf", "crypto", "bond_etf", "commodity_etf", "multi_asset_comparison"), "static_context", "local_static", 20, True, "structural_only"),
    ProviderMetadata("sec_submissions", "SEC submissions", "public", ("filings", "recent_events"), ("equity",), "official", "public_no_key", 30, True, "filing_driven"),
    ProviderMetadata("yahoo_chart_price", "Yahoo public chart", "public", ("price",), ("equity", "etf", "bond_etf", "commodity_etf", "crypto", "multi_asset_comparison"), "public_market", "public_no_key", 40, True, "dated_quote"),
    ProviderMetadata("stooq_price", "Stooq public CSV", "public", ("price",), ("equity", "etf", "bond_etf", "commodity_etf", "multi_asset_comparison"), "public_market", "public_no_key", 50, True, "dated_quote"),
    ProviderMetadata("alpha_vantage_api", "Alpha Vantage API", "api", ("price", "fundamentals"), ("equity", "etf", "crypto", "commodity_etf"), "disabled_api", "api_key_optional_future", 100, False, "future_api_slot"),
    ProviderMetadata("financial_modeling_prep_api", "Financial Modeling Prep API", "api", ("price", "fundamentals", "profile"), ("equity", "etf"), "disabled_api", "api_key_optional_future", 110, False, "future_api_slot"),
    ProviderMetadata("nasdaq_data_link_api", "Nasdaq Data Link API", "api", ("price", "macro", "reference"), ("equity", "etf", "bond_etf", "commodity_etf"), "disabled_api", "api_key_optional_future", 120, False, "future_api_slot"),
)


def all_providers() -> list[ProviderMetadata]:
    return sorted(PROVIDER_REGISTRY, key=lambda provider: provider.priority)


def provider_snapshot() -> list[dict[str, Any]]:
    return [provider.to_snapshot() for provider in all_providers()]


def providers_for(component: str, asset_type: str | None = None, include_disabled: bool = False) -> list[ProviderMetadata]:
    providers = []
    for provider in all_providers():
        if component not in provider.components:
            continue
        if asset_type and asset_type not in provider.asset_types:
            continue
        if not include_disabled and not provider.enabled:
            continue
        providers.append(provider)
    return providers


def disabled_api_slots() -> list[ProviderMetadata]:
    return [provider for provider in all_providers() if provider.provider_type == "api" and not provider.enabled]


def static_context_for_ticker(ticker: str | None) -> dict[str, Any]:
    if ticker in STATIC_QUICK_CONTEXT:
        return json.loads(json.dumps(STATIC_QUICK_CONTEXT[ticker]))
    return {}
