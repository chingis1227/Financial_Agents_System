from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any

DEFAULT_REPORT_ROOT = Path.home() / "OneDrive" / "Documents" / "Financial Agent Reports"


def default_run_dir(asset_identity: str, now: datetime | None = None) -> Path:
    safe_asset = "".join(ch for ch in asset_identity if ch.isalnum() or ch in (" ", "-", "_", ".")).strip() or "Unknown Asset"
    safe_asset = safe_asset.replace(" ", "_")
    stamp = (now or datetime.now()).strftime("%Y-%m-%d_%H%M%S")
    return DEFAULT_REPORT_ROOT / f"{safe_asset}_{stamp}"


def write_full_workflow_artifacts(state: dict[str, Any]) -> tuple[str, str]:
    output_dir = state.get("output_dir") or ""
    base = Path(output_dir) if output_dir else default_run_dir(str(state.get("asset_identity", "Unknown")))
    audit = base / "audit"
    specialists_dir = audit / "specialists"
    specialists_dir.mkdir(parents=True, exist_ok=True)

    report_path = base / "investment_report.md"
    audit_files = {
        audit / "run_metadata.md": _run_metadata(state),
        audit / "intake.md": _intake(state),
        audit / "sources.md": _sources(state),
        audit / "evidence_plan.md": _dict_doc("Evidence Plan", state.get("evidence_plan", {})),
        audit / "evidence_pack.md": _dict_doc("Evidence Pack", state.get("evidence_pack", {})),
        audit / "gates.md": _dict_doc("Gate Statuses", state.get("gate_statuses", {})),
        audit / "ic_synthesis.md": _dict_doc("IC Synthesis", state.get("ic_synthesis", {})),
    }
    _write_idempotent(report_path, _investment_report(state))
    for path, content in audit_files.items():
        _write_idempotent(path, content)
    for name, content in sorted((state.get("specialist_outputs") or {}).items()):
        _write_idempotent(specialists_dir / f"{name}.md", content.rstrip() + "\n")
    return str(report_path), str(audit)


def _write_idempotent(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    normalized = content if content.endswith("\n") else content + "\n"
    if path.exists() and path.read_text(encoding="utf-8-sig") == normalized:
        return
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(normalized, encoding="utf-8")
    tmp.replace(path)


def _investment_report(state: dict[str, Any]) -> str:
    ic = state.get("ic_synthesis") or {}
    status = state.get("final_status", "Limited")
    lines = [
        f"# Investment report — {state.get('asset_identity', 'Unknown')}",
        "",
        "Artifact Type: investment_report.md",
        "Language: English",
        f"Analysis Status: {status}",
        f"IC Action Status: {ic.get('ic_action_status', 'Not an IC Action')}",
        f"Route: {state.get('route', 'unknown')}",
        f"Mode: {state.get('mode', 'dry_run')}",
        "",
        "## Executive summary",
        str(ic.get("summary", "Dry-run report generated from existing route-card and skill contracts. This is not a final IC Action.")),
        "",
        "## Evidence limits",
    ]
    limitations = state.get("limitations") or []
    if limitations:
        lines.extend(f"- {item}" for item in limitations)
    else:
        lines.append("- No additional limitations recorded.")
    lines.extend([
        "",
        "## Gate status",
        _markdown_kv(state.get("gate_statuses") or {}),
        "",
        "## Specialist summaries",
    ])
    for name, output in sorted((state.get("specialist_outputs") or {}).items()):
        first = output.strip().splitlines()[0] if output.strip() else "No output"
        lines.append(f"- **{name}**: {first.lstrip('# ').strip()}")
    lines.extend([
        "",
        "## Boundary",
        "No positive final IC Action is issued unless evidence, valuation, risk, portfolio fit, and IC gates pass.",
    ])
    return "\n".join(lines)


def _run_metadata(state: dict[str, Any]) -> str:
    return "\n".join([
        "# Run metadata",
        "",
        f"Run ID: {state.get('run_id', '')}",
        f"Thread ID: {state.get('thread_id', '')}",
        f"Mode: {state.get('mode', 'dry_run')}",
        f"Route: {state.get('route', '')}",
        f"Completed LangGraph nodes: {', '.join(state.get('completed_nodes') or [])}",
        "Subagent claim: No Codex subagents are claimed by this LangGraph runtime; these are LangGraph nodes.",
    ])


def _intake(state: dict[str, Any]) -> str:
    return "\n".join([
        "# Intake",
        "",
        f"Original request: {state.get('original_user_request', '')}",
        f"Normalized request: {state.get('normalized_request', '')}",
        f"Detected intent: {state.get('detected_intent', '')}",
        f"Asset identity: {state.get('asset_identity', '')}",
        f"Asset class: {state.get('asset_class', '')}",
        f"Horizon: {state.get('horizon', '')}",
        f"Position context: {state.get('position_context', '')}",
        f"Missing context: {', '.join(state.get('missing_context') or []) or 'None'}",
    ])


def _sources(state: dict[str, Any]) -> str:
    pack = state.get("evidence_pack") or {}
    sources = pack.get("sources") or []
    lines = ["# Sources", "", "Source freshness must be visible when material.", ""]
    if not sources:
        lines.append("- No live sources collected. Dry-run outputs are synthetic and Limited.")
    else:
        for source in sources:
            lines.append(f"- {source}")
    return "\n".join(lines)


def _dict_doc(title: str, data: Any) -> str:
    return f"# {title}\n\n{_markdown_kv(data)}"


def _markdown_kv(data: Any, indent: int = 0) -> str:
    pad = "  " * indent
    if isinstance(data, dict):
        if not data:
            return f"{pad}- Empty"
        lines: list[str] = []
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                lines.append(f"{pad}- {key}:")
                lines.append(_markdown_kv(value, indent + 1))
            else:
                lines.append(f"{pad}- {key}: {value}")
        return "\n".join(lines)
    if isinstance(data, list):
        if not data:
            return f"{pad}- Empty"
        return "\n".join(f"{pad}- {item}" for item in data)
    return f"{pad}{data}"
