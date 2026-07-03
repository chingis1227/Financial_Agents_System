"""QUICK data-layer package for Financial Agent Automation Lab."""

from .identity import (
    COMPARISON_IDENTITY,
    MSFT_IDENTITY,
    QUICK_ASSET_IDENTITIES,
    detect_quick_asset_identity,
    quick_fixture_slug,
    quick_identity_slug,
)
from .quality import (
    answers_require_freshness,
    assess_quick_data_quality,
    format_missing_inputs,
    format_quick_limitations,
    quick_freshness_required,
)
from .output_quality import (
    OUTPUT_QUALITY_REQUIRED_CHECKS,
    OUTPUT_QUALITY_SCHEMA_VERSION,
    assess_quick_output_quality,
    is_output_quality_pass,
    quality_failure_summary,
)
from .snapshot import (
    build_live_comparison_snapshot,
    build_live_source_snapshot,
    build_mock_source_snapshot,
    build_quick_source_snapshot,
    create_quick_run_dir,
    empty_quick_snapshot,
    quick_component_missing,
    quick_components_from_fixture,
    quick_retrieved_map,
    safe_timestamp_for_path,
    static_context_for_identity,
)

__all__ = [
    "COMPARISON_IDENTITY",
    "MSFT_IDENTITY",
    "QUICK_ASSET_IDENTITIES",
    "answers_require_freshness",
    "assess_quick_data_quality",
    "assess_quick_output_quality",
    "build_live_comparison_snapshot",
    "build_live_source_snapshot",
    "build_mock_source_snapshot",
    "build_quick_source_snapshot",
    "create_quick_run_dir",
    "detect_quick_asset_identity",
    "empty_quick_snapshot",
    "format_missing_inputs",
    "format_quick_limitations",
    "quick_component_missing",
    "quick_components_from_fixture",
    "quick_fixture_slug",
    "quick_freshness_required",
    "quick_identity_slug",
    "quick_retrieved_map",
    "OUTPUT_QUALITY_REQUIRED_CHECKS",
    "OUTPUT_QUALITY_SCHEMA_VERSION",
    "is_output_quality_pass",
    "quality_failure_summary",
    "safe_timestamp_for_path",
    "static_context_for_identity",
]
