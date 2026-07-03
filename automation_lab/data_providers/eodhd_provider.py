"""Optional EODHD Tier 2 provider."""

from __future__ import annotations

import os
from typing import Any

from .base import BaseProvider


class EODHDProvider(BaseProvider):
    provider_id = "eodhd_provider"
    provider_name = "EODHD optional market data"
    source_tier = "Tier 2"
    source_type = "eodhd"
    asset_classes = ("equity", "etf", "crypto", "commodity", "multi_asset")
    requires_api_key = True
    env_key = "EODHD_API_KEY"

    def fetch(self, query: dict[str, Any], *, storage: Any = None, allow_network: bool = True):
        if not os.environ.get(self.env_key):
            return self.disabled_result(query, "EODHD_API_KEY is not configured; optional Tier 2 provider disabled gracefully.")
        return self.disabled_result(query, "EODHD integration is quota-aware future work in this layer; official Tier 1 sources remain primary.")
