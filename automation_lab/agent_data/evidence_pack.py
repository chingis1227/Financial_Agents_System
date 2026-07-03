"""Evidence pack builder for TASK-012 supported-equity AGENT."""

from __future__ import annotations

from typing import Any

from .evidence_pack_merge import merge_parsed_documents_into_evidence_pack


def _support_status(record: dict[str, Any]) -> str:
    if record.get("status") == "ok":
        return "Supported"
    if record.get("importance") == "required":
        return "Unsupported"
    return "Partially Supported" if record.get("importance") == "important" else "Not Found"


def build_evidence_pack(preflight: dict[str, Any], freshness_required: bool) -> dict[str, Any]:
    records = preflight.get("source_records", [])
    claims = []
    for record in records:
        claims.append({
            "claim": f"{record.get('name')} was checked for {preflight.get('subject_identity', {}).get('ticker', 'the selected equity')} AGENT workflow.",
            "claim_type": "Reported Fact" if record.get("category") in {"filings", "fundamentals", "identity"} else "Market Data" if record.get("category") == "market_data" else "Analyst Interpretation",
            "materiality": "Decision-Critical" if record.get("importance") == "required" else "Important" if record.get("importance") == "important" else "Contextual",
            "source": record.get("url") or record.get("primary"),
            "source_tier": record.get("source_tier"),
            "source_date": record.get("source_date"),
            "freshness": "Stale" if record.get("freshness_status") == "stale" else "Current" if record.get("status") == "ok" and record.get("category") == "market_data" and freshness_required else "Recent" if record.get("status") == "ok" else "Unknown",
            "support_status": _support_status(record),
            "access": record.get("access_status"),
            "limitation": record.get("error") or "",
        })
    missing = [record for record in records if record.get("status") != "ok"]
    conflicts: list[dict[str, Any]] = []
    summary = preflight.get("summary", {})
    readiness = "Complete" if summary.get("hard_gate_passed") and not summary.get("limitation_needed") else "Limited" if summary.get("hard_gate_passed") else "Blocked"
    pack = {
        "schema_version": "agent_evidence_pack.v1",
        "artifact_type": "Supporting Evidence Pack",
        "owner": "Evidence Collector",
        "subject_identity": preflight.get("subject_identity"),
        "source_scope": preflight.get("source_scope"),
        "evidence_snapshot_time": preflight.get("retrieved_at"),
        "freshness_required": freshness_required,
        "evidence_readiness": readiness,
        "claim_support_matrix": claims,
        "conflict_register": conflicts,
        "missing_weak_evidence_register": [
            {
                "needed_evidence": record.get("name"),
                "why_it_matters": "Required source" if record.get("importance") == "required" else "Important context source",
                "materiality": "Decision-Critical" if record.get("importance") == "required" else "Important",
                "needed_freshness": record.get("freshness_rule"),
                "suggested_source_type": record.get("primary"),
                "consequence_if_unavailable": "Limit or stop full AGENT execution" if record.get("importance") == "required" else "Explain limitation in reader report and audit",
                "observed_status": record.get("status"),
                "limitation": record.get("error"),
            }
            for record in missing
        ],
        "readiness_by_downstream_agent": {
            "evidence-collector": readiness,
            "financial-statement-analysis": "Complete" if any(r.get("source_id") == "company_facts" and r.get("status") == "ok" for r in records) else "Limited",
            "valuation-expectations-agent": "Complete" if any(r.get("source_id") == "current_price" and r.get("status") == "ok" for r in records) else "Limited",
            "investment-committee-agent": "Decision-prep only unless portfolio context and all final gates pass",
        },
        "pre_ic_evidence_lock": {
            "lock_time": preflight.get("retrieved_at"),
            "evidence_pack_status": readiness,
            "allowed_ic_output": "decision_prep_memo" if readiness != "Blocked" else "evidence_gap_memo",
            "missing_decision_critical_inputs": list(summary.get("missing_required", [])) + list(summary.get("partial_required", [])),
            "missing_important_inputs": summary.get("missing_important", []),
        },
    }
    parsed_documents = preflight.get("parsed_documents") or []
    if parsed_documents:
        merge_parsed_documents_into_evidence_pack(pack, parsed_documents, materiality="Important")
    return pack


def render_evidence_pack_markdown(pack: dict[str, Any]) -> str:
    identity = pack.get("subject_identity", {})
    lines = [
        f"# Evidence Pack - {identity.get('ticker', 'EQUITY')}",
        "",
        "- Artifact Type: Supporting Evidence Pack",
        "- Owner: Evidence Collector",
        f"- Subject identity: {identity.get('ticker')} / {identity.get('company_name')}",
        f"- Request / source scope: {pack.get('source_scope')}",
        f"- Evidence snapshot time: {pack.get('evidence_snapshot_time')}",
        f"- Evidence readiness: {pack.get('evidence_readiness')}",
        "",
        "## Evidence summary",
        f"The pack maps public {identity.get('ticker', 'equity')} sources to material downstream AGENT claims and records missing or weak evidence before IC synthesis.",
        "",
        "## Source inventory",
        "See `source_inventory.json` for the full source register.",
        "",
        "## Claim support matrix",
        "| Claim | Claim type | Materiality | Source / tier | Source date | Freshness | Support status | Access | Location | Limitation |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    for claim in pack.get("claim_support_matrix", []):
        lines.append(
            f"| {claim.get('claim')} | {claim.get('claim_type')} | {claim.get('materiality')} | {claim.get('source_tier')} | {claim.get('source_date') or ''} | {claim.get('freshness')} | {claim.get('support_status')} | {claim.get('access')} | {claim.get('location') or ''} | {claim.get('limitation') or ''} |"
        )
    lines.extend(["", "## Conflict register", "No material source conflicts identified in preflight." if not pack.get("conflict_register") else "Material conflicts recorded in JSON evidence pack.", "", "## Missing / weak evidence register"])
    missing = pack.get("missing_weak_evidence_register", [])
    if not missing:
        lines.append("No missing required or important source categories in this preflight.")
    else:
        for item in missing:
            lines.append(f"- {item.get('needed_evidence')}: {item.get('consequence_if_unavailable')}")
    lock = pack.get("pre_ic_evidence_lock", {})
    lines.extend(["", "## Pre-IC evidence lock", f"- Evidence pack status: {lock.get('evidence_pack_status')}", f"- Allowed IC output: {lock.get('allowed_ic_output')}", f"- Missing decision-critical inputs: {', '.join(lock.get('missing_decision_critical_inputs') or []) or 'None'}"])
    return "\n".join(lines) + "\n"
