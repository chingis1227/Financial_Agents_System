"""AGENT data layer for TASK-012 supported-equity preflight."""

from .equity_preflight import build_equity_source_preflight
from .equity_msft_preflight import build_msft_source_preflight
from .evidence_pack import build_evidence_pack, render_evidence_pack_markdown
from .document_parser import parse_document
from .evidence_pack_merge import merge_parsed_document_into_evidence_pack, merge_parsed_documents_into_evidence_pack
from .source_registry import (
    EQUITY_AGENT_IDENTITIES,
    MSFT_AGENT_IDENTITY,
    SOURCE_IMPORTANCE_LEVELS,
    SOURCE_REGISTRY,
    REQUIRED_SOURCE_IDS,
    IMPORTANT_SOURCE_IDS,
    NICE_TO_HAVE_SOURCE_IDS,
    SUPPORTED_EQUITY_TICKERS,
    supported_equity_identity,
    supported_equity_metadata,
)
from .equity_resolver import (
    clean_resolved_identity,
    detect_equity_mentions,
    resolve_equity_request,
)

__all__ = [
    "build_equity_source_preflight",
    "build_msft_source_preflight",
    "build_evidence_pack",
    "render_evidence_pack_markdown",
    "parse_document",
    "merge_parsed_document_into_evidence_pack",
    "merge_parsed_documents_into_evidence_pack",
    "EQUITY_AGENT_IDENTITIES",
    "MSFT_AGENT_IDENTITY",
    "SOURCE_IMPORTANCE_LEVELS",
    "SOURCE_REGISTRY",
    "REQUIRED_SOURCE_IDS",
    "IMPORTANT_SOURCE_IDS",
    "NICE_TO_HAVE_SOURCE_IDS",
    "SUPPORTED_EQUITY_TICKERS",
    "supported_equity_identity",
    "supported_equity_metadata",
    "clean_resolved_identity",
    "detect_equity_mentions",
    "resolve_equity_request",
]
