"""Canonical source-tier helpers for provider outputs."""

from __future__ import annotations

from .base import VALID_SOURCE_TIERS

TIER_1_SOURCE_TYPES = {
    "sec_filings",
    "sec_companyfacts",
    "fred_series",
    "treasury_rates",
    "cftc_cot",
    "usda_nass",
    "usda_wasde",
    "usda_psd",
    "issuer_etf",
    "official_exchange",
}
TIER_2_SOURCE_TYPES = {"public_market_data", "eodhd", "stooq", "yahoo_chart", "nasdaq_data_link"}
TIER_3_SOURCE_TYPES = {"financial_media", "public_news"}
POINTER_ONLY_SOURCE_TYPES = {"search_discovery", "perplexity", "search_snippet", "ai_summary"}


def source_tier_for_type(source_type: str) -> str:
    if source_type in TIER_1_SOURCE_TYPES:
        return "Tier 1"
    if source_type in TIER_2_SOURCE_TYPES:
        return "Tier 2"
    if source_type in TIER_3_SOURCE_TYPES:
        return "Tier 3"
    if source_type in POINTER_ONLY_SOURCE_TYPES:
        return "Pointer-Only"
    return "Tier 4"


def assert_valid_tier(source_tier: str) -> str:
    if source_tier not in VALID_SOURCE_TIERS:
        raise ValueError(f"invalid source tier: {source_tier}")
    return source_tier


def can_support_material_claim(source_tier: str) -> bool:
    return source_tier in {"Tier 1", "Tier 2", "Tier 3"}


def pointer_only_limitation(source_type: str) -> str:
    return (
        f"{source_type} is Pointer-Only and cannot support decision-critical claims until the underlying source "
        "is fetched and parsed."
    )
