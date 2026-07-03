"""Canonical ProviderResult contract for Automation Lab data providers.

The provider layer is source/evidence infrastructure. It fetches, parses,
normalizes, and records limitations; it never issues investment conclusions.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any

VALID_SOURCE_TIERS = {"Tier 1", "Tier 2", "Tier 3", "Tier 4", "Pointer-Only"}
VALID_STATUSES = {"ok", "partial", "missing", "error", "disabled"}
VALID_ACCESS_STATUSES = {"Available", "Partial", "Inaccessible", "Not Found", "Restricted"}
VALID_FRESHNESS_STATUSES = {"Current", "Recent", "Stale but Usable", "Refresh Required", "Unknown"}


def now_iso() -> str:
    """Return a timezone-aware local ISO timestamp."""
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def _as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


@dataclass
class ProviderResult:
    provider_id: str
    provider_name: str
    source_tier: str
    source_type: str
    asset_class: str
    subject: str
    query: dict[str, Any]
    url: str | None
    status: str
    access_status: str
    freshness_status: str
    source_date: str | None = None
    retrieved_at: str = field(default_factory=now_iso)
    raw_path: str | None = None
    normalized_path: str | None = None
    normalized_data: Any = None
    claims: list[dict[str, Any]] = field(default_factory=list)
    limitations: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        result = asdict(self)
        result["claims"] = _as_list(result.get("claims"))
        result["limitations"] = [str(item) for item in _as_list(result.get("limitations")) if item not in (None, "")]
        result["errors"] = [str(item) for item in _as_list(result.get("errors")) if item not in (None, "")]
        result["metadata"] = result.get("metadata") or {}
        validate_provider_result(result)
        return result

    @classmethod
    def disabled(
        cls,
        *,
        provider_id: str,
        provider_name: str,
        source_tier: str,
        source_type: str,
        asset_class: str,
        subject: str,
        query: dict[str, Any] | None = None,
        reason: str = "Provider disabled or not configured.",
        url: str | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> "ProviderResult":
        return cls(
            provider_id=provider_id,
            provider_name=provider_name,
            source_tier=source_tier,
            source_type=source_type,
            asset_class=asset_class,
            subject=subject,
            query=query or {},
            url=url,
            status="disabled",
            access_status="Restricted",
            freshness_status="Unknown",
            limitations=[reason],
            metadata=metadata or {},
        )

    @classmethod
    def error(
        cls,
        *,
        provider_id: str,
        provider_name: str,
        source_tier: str,
        source_type: str,
        asset_class: str,
        subject: str,
        query: dict[str, Any] | None = None,
        error: str,
        url: str | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> "ProviderResult":
        return cls(
            provider_id=provider_id,
            provider_name=provider_name,
            source_tier=source_tier,
            source_type=source_type,
            asset_class=asset_class,
            subject=subject,
            query=query or {},
            url=url,
            status="error",
            access_status="Inaccessible",
            freshness_status="Unknown",
            errors=[error],
            metadata=metadata or {},
        )


def validate_provider_result(result: dict[str, Any]) -> None:
    required = {
        "provider_id",
        "provider_name",
        "source_tier",
        "source_type",
        "asset_class",
        "subject",
        "query",
        "url",
        "status",
        "access_status",
        "freshness_status",
        "source_date",
        "retrieved_at",
        "raw_path",
        "normalized_path",
        "normalized_data",
        "claims",
        "limitations",
        "errors",
        "metadata",
    }
    missing = required - set(result)
    if missing:
        raise ValueError(f"ProviderResult missing fields: {sorted(missing)}")
    if result["source_tier"] not in VALID_SOURCE_TIERS:
        raise ValueError(f"invalid source_tier: {result['source_tier']}")
    if result["status"] not in VALID_STATUSES:
        raise ValueError(f"invalid status: {result['status']}")
    if result["access_status"] not in VALID_ACCESS_STATUSES:
        raise ValueError(f"invalid access_status: {result['access_status']}")
    if result["freshness_status"] not in VALID_FRESHNESS_STATUSES:
        raise ValueError(f"invalid freshness_status: {result['freshness_status']}")
    if not isinstance(result.get("query"), dict):
        raise ValueError("query must be an object")
    if not isinstance(result.get("claims"), list):
        raise ValueError("claims must be an array")
    if not isinstance(result.get("limitations"), list):
        raise ValueError("limitations must be an array")
    if not isinstance(result.get("errors"), list):
        raise ValueError("errors must be an array")
    if not isinstance(result.get("metadata"), dict):
        raise ValueError("metadata must be an object")
    retrieved_at = result.get("retrieved_at")
    if not isinstance(retrieved_at, str) or not (
        retrieved_at.endswith("Z") or "+" in retrieved_at[-6:] or "-" in retrieved_at[-6:]
    ):
        raise ValueError("retrieved_at must include timezone")
    for index, claim in enumerate(result.get("claims") or []):
        validate_provider_claim(claim, index=index, provider_id=str(result.get("provider_id")))


def validate_provider_claim(claim: dict[str, Any], *, index: int = 0, provider_id: str = "provider") -> None:
    if not isinstance(claim, dict):
        raise ValueError(f"{provider_id} claim {index} must be an object")
    required = {
        "claim",
        "claim_type",
        "materiality",
        "source",
        "source_tier",
        "source_date",
        "freshness",
        "support_status",
        "access",
        "limitation",
    }
    missing = required - set(claim)
    if missing:
        raise ValueError(f"{provider_id} claim {index} missing fields: {sorted(missing)}")
    if claim.get("source_tier") not in VALID_SOURCE_TIERS:
        raise ValueError(f"{provider_id} claim {index} has invalid source_tier: {claim.get('source_tier')}")
    if claim.get("access") not in VALID_ACCESS_STATUSES:
        raise ValueError(f"{provider_id} claim {index} has invalid access: {claim.get('access')}")
    material = claim.get("materiality") in {"Decision-Critical", "Important"}
    supported = claim.get("support_status") == "Supported"
    if material and supported:
        if not claim.get("claim") or not claim.get("source"):
            raise ValueError(f"{provider_id} claim {index} lacks claim text or source")
        if (not claim.get("source_date") or claim.get("freshness") == "Unknown") and not claim.get("limitation"):
            raise ValueError(
                f"{provider_id} claim {index} has material supported evidence without source_date/freshness limitation"
            )


class BaseProvider:
    provider_id = "base"
    provider_name = "Base provider"
    source_tier = "Tier 4"
    source_type = "generic"
    asset_classes: tuple[str, ...] = ("unknown",)
    requires_api_key = False
    env_key: str | None = None

    def fetch(self, query: dict[str, Any], *, storage: Any = None, allow_network: bool = True) -> ProviderResult:
        raise NotImplementedError

    def disabled_result(self, query: dict[str, Any], reason: str) -> ProviderResult:
        return ProviderResult.disabled(
            provider_id=self.provider_id,
            provider_name=self.provider_name,
            source_tier=self.source_tier,
            source_type=self.source_type,
            asset_class=str(query.get("asset_class") or "unknown"),
            subject=str(query.get("subject") or query.get("ticker") or query.get("cik") or "unknown"),
            query=query,
            reason=reason,
        )

    def error_result(self, query: dict[str, Any], error: Exception | str, url: str | None = None) -> ProviderResult:
        return ProviderResult.error(
            provider_id=self.provider_id,
            provider_name=self.provider_name,
            source_tier=self.source_tier,
            source_type=self.source_type,
            asset_class=str(query.get("asset_class") or "unknown"),
            subject=str(query.get("subject") or query.get("ticker") or query.get("cik") or "unknown"),
            query=query,
            error=str(error),
            url=url,
        )
