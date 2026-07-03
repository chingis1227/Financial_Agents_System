"""Pointer-only search/discovery provider."""

from __future__ import annotations

import os
from typing import Any

from .base import BaseProvider, ProviderResult
from .source_quality import pointer_only_limitation


class SearchDiscoveryProvider(BaseProvider):
    provider_id = "search_discovery_provider"
    provider_name = "Search discovery provider"
    source_tier = "Pointer-Only"
    source_type = "search_discovery"
    asset_classes = ("equity", "etf", "fixed_income", "commodity", "grains", "crypto", "multi_asset")

    def fetch(self, query: dict[str, Any], *, storage: Any = None, allow_network: bool = True) -> ProviderResult:
        subject = str(query.get("subject") or query.get("ticker") or "asset")
        asset_class = str(query.get("asset_class") or "unknown")
        results = query.get("results") or []
        api_key = os.environ.get("PERPLEXITY_API_KEY")
        if not results and not api_key:
            return ProviderResult(
                provider_id=self.provider_id,
                provider_name=self.provider_name,
                source_tier=self.source_tier,
                source_type=self.source_type,
                asset_class=asset_class,
                subject=subject,
                query=query,
                url=None,
                status="disabled",
                access_status="Restricted",
                freshness_status="Unknown",
                limitations=["No local public search connector or PERPLEXITY_API_KEY configured; provider remains Pointer-Only."],
                metadata={"claim_support_allowed": False},
            )
        normalized = {"results": results, "claim_support_allowed": False}
        normalized_path = storage.save_normalized(self.provider_id, query, normalized, url=None) if storage else None
        return ProviderResult(
            provider_id=self.provider_id,
            provider_name=self.provider_name,
            source_tier=self.source_tier,
            source_type=self.source_type,
            asset_class=asset_class,
            subject=subject,
            query=query,
            url=None,
            status="partial",
            access_status="Partial",
            freshness_status="Unknown",
            normalized_path=normalized_path,
            normalized_data=normalized,
            claims=[],
            limitations=[pointer_only_limitation("Search discovery")],
            metadata={"claim_support_allowed": False},
        )
