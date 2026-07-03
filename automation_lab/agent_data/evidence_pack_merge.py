"""Merge parsed document claims into Automation Lab Evidence Packs."""

from __future__ import annotations

from typing import Any


def _format_location(location: dict[str, Any] | None) -> str:
    if not location:
        return ""
    parts = []
    if location.get("page"):
        parts.append(f"page {location.get('page')}")
    if location.get("section"):
        parts.append(str(location.get("section")))
    if location.get("table"):
        parts.append(f"table: {location.get('table')}")
    return " / ".join(parts)


def _same_metric_period(a: dict[str, Any], b: dict[str, Any]) -> bool:
    return bool(a.get("metric")) and a.get("metric") == b.get("metric") and (a.get("period") or "Unknown") == (b.get("period") or "Unknown")


def merge_parsed_document_into_evidence_pack(
    pack: dict[str, Any],
    parsed_document: dict[str, Any],
    *,
    materiality: str = "Important",
) -> dict[str, Any]:
    """Add parsed source metadata, claims, missing evidence, and conflicts to an Evidence Pack."""

    source = parsed_document.get("source", {})
    source_ref = source.get("url") or source.get("local_path") or source.get("title") or source.get("source_id")
    pack.setdefault("source_inventory", [])
    pack["source_inventory"].append(
        {
            "source_id": source.get("source_id"),
            "title": source.get("title"),
            "url": source.get("url"),
            "local_path": source.get("local_path"),
            "publisher": source.get("publisher"),
            "published_at": source.get("published_at"),
            "retrieved_at": source.get("retrieved_at"),
            "document_type": source.get("document_type"),
            "access_status": source.get("access_status"),
            "source_tier": source.get("source_tier"),
            "parser_schema_version": parsed_document.get("schema_version"),
        }
    )

    existing_claims = list(pack.get("parsed_claims", []))
    new_claims = parsed_document.get("extracted_claims", []) or []
    pack.setdefault("parsed_claims", [])
    pack["parsed_claims"].extend(new_claims)
    pack.setdefault("claim_support_matrix", [])
    pack.setdefault("missing_weak_evidence_register", [])
    pack.setdefault("conflict_register", [])

    if not new_claims:
        pack["missing_weak_evidence_register"].append(
            {
                "needed_evidence": f"Financial claims in {source_ref}",
                "why_it_matters": "Document was parsed but no supported financial claim was detected",
                "materiality": materiality,
                "needed_freshness": source.get("published_at") or source.get("retrieved_at"),
                "suggested_source_type": "Issuer document, filing, or article with extractable text",
                "consequence_if_unavailable": "Keep the document as source inventory only; do not use it as claim support",
                "observed_status": "Not Found",
                "limitation": "; ".join(parsed_document.get("warnings") or []),
            }
        )

    for claim in new_claims:
        location = _format_location(claim.get("source_location"))
        pack["claim_support_matrix"].append(
            {
                "claim": claim.get("claim"),
                "claim_type": claim.get("claim_type"),
                "materiality": materiality,
                "source": source_ref,
                "source_tier": claim.get("source_tier") or source.get("source_tier"),
                "source_date": source.get("published_at"),
                "freshness": "Unknown" if not source.get("published_at") else "Recent",
                "support_status": claim.get("support_status"),
                "access": source.get("access_status"),
                "location": location,
                "limitation": "; ".join(claim.get("limitations") or []),
                "metric": claim.get("metric"),
                "value": claim.get("value"),
                "unit": claim.get("unit"),
                "period": claim.get("period"),
                "confidence": claim.get("confidence"),
            }
        )
        for prior in existing_claims:
            if not _same_metric_period(prior, claim):
                continue
            if prior.get("value") != claim.get("value") or prior.get("unit") != claim.get("unit"):
                pack["conflict_register"].append(
                    {
                        "claim": f"{claim.get('metric')} for {claim.get('period') or 'Unknown'}",
                        "what_conflicts": f"{prior.get('value')} {prior.get('unit')} vs {claim.get('value')} {claim.get('unit')}",
                        "why_it_matters": "Different parsed values exist for the same metric and period",
                        "source_hierarchy_treatment": "Resolve using source hierarchy and direct source access before downstream IC synthesis",
                        "materiality": materiality,
                        "current_treatment": "Contradicted",
                        "impact_on_analysis_status": "Limited until resolved if material",
                        "impact_on_ic_action_status": "Final IC Action unavailable for the conflicted claim until resolved",
                        "resolution_needed": "Review source documents and confirm the correct normalized value",
                    }
                )
    return pack


def merge_parsed_documents_into_evidence_pack(
    pack: dict[str, Any],
    parsed_documents: list[dict[str, Any]],
    *,
    materiality: str = "Important",
) -> dict[str, Any]:
    for parsed_document in parsed_documents:
        merge_parsed_document_into_evidence_pack(pack, parsed_document, materiality=materiality)
    return pack
