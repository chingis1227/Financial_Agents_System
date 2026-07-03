"""Provider registry and route-aware orchestration."""

from __future__ import annotations

from typing import Any

from .base import BaseProvider, ProviderResult, validate_provider_result
from .cache import DataRunStorage
from .cftc_cot_provider import CFTCCOTProvider
from .eodhd_provider import EODHDProvider
from .etf_issuer_provider import ETFIssuerProvider
from .fred_provider import FREDProvider
from .public_price_provider import PublicPriceProvider
from .search_discovery_provider import SearchDiscoveryProvider
from .sec_provider import SECProvider
from .treasury_provider import TreasuryProvider
from .usda_nass_provider import USDANASSProvider
from .usda_psd_provider import USDAPSDProvider
from .usda_wasde_provider import USDAWASDEProvider


PROVIDER_CLASSES: tuple[type[BaseProvider], ...] = (
    SECProvider,
    FREDProvider,
    TreasuryProvider,
    CFTCCOTProvider,
    USDANASSProvider,
    USDAWASDEProvider,
    USDAPSDProvider,
    ETFIssuerProvider,
    PublicPriceProvider,
    SearchDiscoveryProvider,
    EODHDProvider,
)

ROUTE_PROVIDER_IDS: dict[str, tuple[str, ...]] = {
    "equity_full_cycle": ("sec_provider", "public_price_provider", "search_discovery_provider", "eodhd_provider"),
    "etf_full_cycle": ("etf_issuer_provider", "public_price_provider", "search_discovery_provider", "eodhd_provider"),
    "fixed_income_full_cycle": ("etf_issuer_provider", "treasury_provider", "fred_provider", "public_price_provider", "search_discovery_provider"),
    "commodity_full_cycle": (
        "cftc_cot_provider",
        "usda_nass_provider",
        "usda_wasde_provider",
        "usda_psd_provider",
        "public_price_provider",
        "etf_issuer_provider",
        "search_discovery_provider",
    ),
    "crypto_full_cycle": ("public_price_provider", "eodhd_provider", "search_discovery_provider"),
    "multi_asset_comparison": ("sec_provider", "etf_issuer_provider", "treasury_provider", "fred_provider", "public_price_provider", "eodhd_provider"),
}

ASSET_CLASS_ROUTES = {
    "equity": "equity_full_cycle",
    "etf": "etf_full_cycle",
    "bond_etf": "fixed_income_full_cycle",
    "fixed_income": "fixed_income_full_cycle",
    "commodity": "commodity_full_cycle",
    "commodity_etf": "commodity_full_cycle",
    "grains": "commodity_full_cycle",
    "crypto": "crypto_full_cycle",
    "multi_asset": "multi_asset_comparison",
    "multi_asset_comparison": "multi_asset_comparison",
}


class ProviderRegistry:
    def __init__(self, providers: list[BaseProvider] | None = None) -> None:
        self.providers: dict[str, BaseProvider] = {provider.provider_id: provider for provider in (providers or [cls() for cls in PROVIDER_CLASSES])}

    def snapshot(self) -> list[dict[str, Any]]:
        return [
            {
                "provider_id": provider.provider_id,
                "provider_name": provider.provider_name,
                "source_tier": provider.source_tier,
                "source_type": provider.source_type,
                "asset_classes": list(provider.asset_classes),
                "requires_api_key": provider.requires_api_key,
                "env_key": provider.env_key,
            }
            for provider in self.providers.values()
        ]

    def providers_for_route(self, route: str) -> list[BaseProvider]:
        return [self.providers[pid] for pid in ROUTE_PROVIDER_IDS.get(route, ()) if pid in self.providers]

    def providers_for_query(self, route: str | None, query: dict[str, Any], asset_class: str | None = None) -> list[BaseProvider]:
        providers = self.providers_for_route(route) if route else self.providers_for_asset_class(asset_class or str(query.get("asset_class") or "unknown"))
        if route == "commodity_full_cycle":
            ticker = str(query.get("ticker") or "").upper()
            commodity = str(query.get("commodity") or "").lower()
            is_grain = commodity in {"corn", "wheat", "soybeans", "soybean"} or ticker in {"CORN", "WEAT", "SOYB", "DBA"}
            if not is_grain:
                providers = [
                    provider
                    for provider in providers
                    if provider.provider_id not in {"cftc_cot_provider", "usda_nass_provider", "usda_wasde_provider", "usda_psd_provider"}
                ]
        return providers

    def providers_for_asset_class(self, asset_class: str) -> list[BaseProvider]:
        return self.providers_for_route(ASSET_CLASS_ROUTES.get(asset_class, asset_class))

    def provider_plan(self, *, route: str | None = None, asset_class: str | None = None) -> list[dict[str, Any]]:
        providers = self.providers_for_route(route) if route else self.providers_for_asset_class(asset_class or "unknown")
        return [
            {
                "provider_id": provider.provider_id,
                "provider_name": provider.provider_name,
                "source_tier": provider.source_tier,
                "source_type": provider.source_type,
                "asset_classes": list(provider.asset_classes),
            }
            for provider in providers
        ]

    def run(
        self,
        *,
        query: dict[str, Any],
        route: str | None = None,
        asset_class: str | None = None,
        allow_network: bool = True,
        persist: bool = False,
        storage_root: str | None = None,
    ) -> dict[str, Any]:
        providers = self.providers_for_query(route, query, asset_class)
        subject = str(query.get("subject") or query.get("ticker") or query.get("asset") or "subject")
        storage = DataRunStorage(storage_root, subject=subject, persist=persist)
        result_dicts: list[dict[str, Any]] = []
        for provider in providers:
            provider_query = {**query, "asset_class": query.get("asset_class") or asset_class or "unknown"}
            try:
                result = provider.fetch(provider_query, storage=storage, allow_network=allow_network)
            except Exception as exc:  # providers must degrade; registry is the last safety net.
                result = provider.error_result(provider_query, exc)
            try:
                result_dict = result.to_dict() if isinstance(result, ProviderResult) else result
                validate_provider_result(result_dict)
            except Exception as validation_exc:
                result_dict = provider.error_result(provider_query, f"ProviderResult validation failed: {validation_exc}").to_dict()
            result_dicts.append(result_dict)
        artifacts = storage.write_run_artifacts(result_dicts)
        actual_plan = [
            {
                "provider_id": provider.provider_id,
                "provider_name": provider.provider_name,
                "source_tier": provider.source_tier,
                "source_type": provider.source_type,
                "asset_classes": list(provider.asset_classes),
            }
            for provider in providers
        ]
        return {"provider_registry": self.snapshot(), "provider_plan": actual_plan, "provider_results": result_dicts, "data_run_artifacts": artifacts}


DEFAULT_PROVIDER_REGISTRY = ProviderRegistry()


def provider_registry_snapshot() -> list[dict[str, Any]]:
    return DEFAULT_PROVIDER_REGISTRY.snapshot()


def provider_plan_for_route(route: str) -> list[dict[str, Any]]:
    return DEFAULT_PROVIDER_REGISTRY.provider_plan(route=route)


def run_provider_registry_for_preflight(
    *,
    route: str,
    identity: dict[str, Any],
    mode: str,
    persist: bool = False,
) -> dict[str, Any]:
    if route == "multi_asset_comparison" and isinstance(identity.get("components"), list):
        aggregate_results: list[dict[str, Any]] = []
        aggregate_plan: list[dict[str, Any]] = []
        component_statuses: list[dict[str, Any]] = []
        for component in identity.get("components") or []:
            if not isinstance(component, dict):
                continue
            component_route = component.get("selected_route") or ASSET_CLASS_ROUTES.get(str(component.get("security_type") or ""), "equity_full_cycle")
            component_output = run_provider_registry_for_preflight(
                route=str(component_route),
                identity=component,
                mode=mode,
                persist=False,
            )
            component_results = component_output.get("provider_results") or []
            for result in component_results:
                metadata = result.setdefault("metadata", {})
                metadata["comparison_component"] = {
                    "ticker": component.get("ticker"),
                    "security_type": component.get("security_type"),
                    "selected_route": component_route,
                }
            aggregate_results.extend(component_results)
            for plan_item in component_output.get("provider_plan") or []:
                aggregate_plan.append({**plan_item, "component_ticker": component.get("ticker"), "component_route": component_route})
            component_statuses.append(
                {
                    "ticker": component.get("ticker"),
                    "selected_route": component_route,
                    "provider_count": len(component_results),
                    "has_supported_claim": any(result.get("claims") for result in component_results),
                    "has_available_source": any(result.get("status") in {"ok", "partial", "disabled"} for result in component_results),
                }
            )
        parity_status = "Complete" if component_statuses and all(item["provider_count"] > 0 for item in component_statuses) else "Limited"
        return {
            "provider_registry": DEFAULT_PROVIDER_REGISTRY.snapshot(),
            "provider_plan": aggregate_plan,
            "provider_results": aggregate_results,
            "data_run_artifacts": {"run_dir": None, "provider_results": None, "source_inventory": None, "evidence_inputs": None},
            "evidence_parity": {"status": parity_status, "components": component_statuses},
        }
    ticker = identity.get("ticker")
    security_type = identity.get("security_type") or identity.get("asset_class")
    asset_class = "fixed_income" if route == "fixed_income_full_cycle" else "commodity" if route == "commodity_full_cycle" else str(security_type or "unknown")
    query = {
        "subject": identity.get("company_name") or ticker or route,
        "ticker": ticker,
        "price_ticker": identity.get("price_ticker") or ticker,
        "cik": identity.get("cik"),
        "asset_class": asset_class,
        "commodity": "corn" if str(ticker).upper() == "CORN" else None,
        "issuer_url": identity.get("issuer_url") or identity.get("ir_url"),
    }
    return DEFAULT_PROVIDER_REGISTRY.run(query=query, route=route, asset_class=asset_class, allow_network=(mode == "live"), persist=persist)
