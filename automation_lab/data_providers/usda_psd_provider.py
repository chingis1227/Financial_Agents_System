"""USDA PSD provider stub with graceful degradation."""

from __future__ import annotations

from typing import Any

from .base import BaseProvider


class USDAPSDProvider(BaseProvider):
    provider_id = "usda_psd_provider"
    provider_name = "USDA PSD"
    source_tier = "Tier 1"
    source_type = "usda_psd"
    asset_classes = ("commodity", "grains")

    def fetch(self, query: dict[str, Any], *, storage: Any = None, allow_network: bool = True):
        return self.disabled_result(
            query,
            "USDA PSD full API/download integration is documented as a future extension; provider degrades explicitly instead of faking data.",
        )
