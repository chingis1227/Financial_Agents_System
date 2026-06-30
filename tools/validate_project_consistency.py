from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
checks: list[tuple[str, bool, str]] = []

def add(name: str, ok: bool, detail: str = "") -> None:
    checks.append((name, ok, detail))

def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8-sig")

def exists(rel: str) -> bool:
    return (ROOT / rel).exists()

# Required active files
for rel in [
    "PROJECT_STATE.md",
    "AGENTS.md",
    "README.md",
    "implementation/01-documentation-control.md",
    "implementation/15-documentation-sync-contract.md",
    "workflows/route_cards/investment_request_router.md",
    ".agents/skills/investment-workflow-router/SKILL.md",
]:
    add(f"required active file exists: {rel}", exists(rel), rel)

# Historical build docs moved out of root
for rel in ["TASKS.md", "IMPLEMENTATION_BACKLOG.md"]:
    add(f"historical build doc absent from root: {rel}", not exists(rel), rel)
for rel in ["archive/project-history/TASKS.md", "archive/project-history/IMPLEMENTATION_BACKLOG.md"]:
    add(f"historical build doc archived: {rel}", exists(rel), rel)

# Documentation control registration / status expectations
doc = read("implementation/01-documentation-control.md") if exists("implementation/01-documentation-control.md") else ""
for token in [
    "PROJECT_STATE.md",
    "implementation/15-documentation-sync-contract.md",
    "implementation/non_equity_production_hardening_report.md",
    "archive/project-history/TASKS.md",
    "archive/project-history/IMPLEMENTATION_BACKLOG.md",
]:
    add(f"documentation control mentions {token}", token in doc, token)
for pattern in [
    r"\|\s*`IMPLEMENTATION_BACKLOG\.md`\s*\|\s*Canonical\s*\|",
    r"\|\s*`TASKS\.md`\s*\|\s*Canonical\s*\|",
    r"\|\s*`IMPLEMENTATION_BACKLOG\.md`\s*\|[^|\n]*(active|current|operational|runtime)",
    r"\|\s*`TASKS\.md`\s*\|[^|\n]*(active|current|operational|runtime)",
]:
    add(
        f"documentation control has no stale root task/backlog authority pattern: {pattern}",
        re.search(pattern, doc, re.I) is None,
    )
for rel in [
    "workflows/route_cards/investment_request_router.md",
    "workflows/route_cards/quick_take.md",
    "workflows/route_cards/equity_full_cycle.md",
    "workflows/route_cards/etf_full_cycle.md",
    "workflows/route_cards/commodity_full_cycle.md",
    "workflows/route_cards/crypto_full_cycle.md",
    "workflows/route_cards/fixed_income_full_cycle.md",
    "workflows/route_cards/multi_asset_comparison.md",
    "workflows/route_cards/direct_specialist.md",
]:
    add(f"route card registered: {rel}", f"`{rel}`" in doc, rel)

# Active implementation docs should be registered unless explicitly operational/superseded and registered.
if (ROOT / "implementation").exists():
    for p in sorted((ROOT / "implementation").glob("*.md")):
        rel = p.relative_to(ROOT).as_posix()
        add(f"implementation doc registered: {rel}", f"`{rel}`" in doc, rel)

# PROJECT_STATE consistency
state = read("PROJECT_STATE.md") if exists("PROJECT_STATE.md") else ""
for token in [
    "Codex-native first",
    "Full Cycle",
    "Quick Take",
    "Single-agent Full Cycle",
    "archive/project-history/TASKS.md",
    "implementation/non_equity_production_hardening_report.md",
    "tools\\validate_project_consistency.py",
]:
    add(f"PROJECT_STATE contains {token}", token in state, token)

# AGENTS.md should not use archived build docs as active runtime sources.
agents = read("AGENTS.md") if exists("AGENTS.md") else ""
add("AGENTS reads PROJECT_STATE first", "Read `PROJECT_STATE.md`" in agents)
add("AGENTS points to route router", "workflows/route_cards/investment_request_router.md" in agents)
for forbidden in ["Read `TASKS.md`", "Read `IMPLEMENTATION_BACKLOG.md`", "TASKS.md` for active work", "IMPLEMENTATION_BACKLOG.md` for phase"]:
    add(f"AGENTS has no archived active runtime instruction: {forbidden}", forbidden not in agents)
for token in ["validate_project_consistency.py", "validate_behavior_contracts.py", "validate_runtime_readiness.py"]:
    add(f"AGENTS requires validator {token}", token in agents)

# Repository-wide stale authority scan for retired root build-control files.
allowed_history_terms = re.compile(
    r"archive/project-history|historical|provenance|archived|retired|former|superseded|as-of|at the time|not current runtime authority|not active",
    re.I,
)
stale_line_patterns = [
    re.compile(r"`(?:TASKS|IMPLEMENTATION_BACKLOG)\.md`"),
    re.compile(r"(?<!project-history/)\bTASKS\.md\b"),
    re.compile(r"(?<!project-history/)\bIMPLEMENTATION_BACKLOG\.md\b"),
]
active_authority_patterns = [
    re.compile(r"Authority:\s*Subordinate to\s*`?IMPLEMENTATION_BACKLOG\.md`?", re.I),
    re.compile(r"Root contains\s*`?TASKS\.md`?", re.I),
    re.compile(r"Root contains[^.\n]*`?IMPLEMENTATION_BACKLOG\.md`?", re.I),
    re.compile(r"`?TASKS\.md`?[^.\n]*(operational register|work queue|active|current|runtime authority)", re.I),
    re.compile(r"`?IMPLEMENTATION_BACKLOG\.md`?[^.\n]*(governs|canonical|active|current|runtime authority)", re.I),
]
scan_paths = [
    ROOT / "PROJECT_STATE.md",
    ROOT / "AGENTS.md",
    ROOT / "README.md",
]
scan_dirs = ["implementation", "workflows", ".agents", ".codex/agents", "tests"]
ignored_parts = {".git", ".venv", "archive", "__pycache__", ".mypy_cache", ".pytest_cache", "node_modules"}
for scan_dir in scan_dirs:
    base = ROOT / scan_dir
    if not base.exists():
        continue
    for p in sorted(base.rglob("*")):
        if not p.is_file() or p.suffix.lower() not in {".md", ".yaml", ".yml", ".json", ".toml", ".txt"}:
            continue
        rel_parts = set(p.relative_to(ROOT).parts)
        if rel_parts & ignored_parts:
            continue
        scan_paths.append(p)
scan_paths = sorted(set(scan_paths))
for path in scan_paths:
    if not path.exists():
        continue
    rel = path.relative_to(ROOT).as_posix()
    for lineno, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
        if not any(p.search(line) for p in stale_line_patterns):
            continue
        archive_path_context = "archive/project-history" in line or ("archive" in line and "project-history" in line)
        allowed = allowed_history_terms.search(line) is not None or archive_path_context
        forbidden_active = any(p.search(line) for p in active_authority_patterns) and not archive_path_context
        add(
            f"no stale root task/backlog authority in {rel}:{lineno}",
            allowed and not forbidden_active,
            line.strip(),
        )

# Traceability must not keep retired root build-control files as active/current authority.
trace = read("implementation/10-traceability-matrix.md") if exists("implementation/10-traceability-matrix.md") else ""
for pattern in [
    r"\|\s*`IMPLEMENTATION_BACKLOG\.md`\s*\|",
    r"\|\s*`TASKS\.md`\s*\|",
    r"`IMPLEMENTATION_BACKLOG\.md`[^`\n]*(Canonical|active|current|operational|runtime)",
    r"`TASKS\.md`[^`\n]*(Canonical|active|current|operational|runtime)",
]:
    add(
        f"traceability has no stale root task/backlog authority pattern: {pattern}",
        re.search(pattern, trace, re.I) is None,
    )
for token in ["archive/project-history/IMPLEMENTATION_BACKLOG.md", "archive/project-history/TASKS.md", "Archived provenance only"]:
    add(f"traceability uses archived historical reference: {token}", token in trace, token)

# Status header mismatch checks for known drift fixes
remaining = read("implementation/remaining-requirements.md") if exists("implementation/remaining-requirements.md") else ""
add("remaining-requirements status is supporting", "Status: Supporting residual-requirement register" in remaining)
p10 = read("implementation/p10-qa-execution-report.md") if exists("implementation/p10-qa-execution-report.md") else ""
add("p10 report has Status header", re.search(r"^Status:\s*Supporting operational validation record", p10, re.M) is not None)

# Route cards contain required contract sections
for p in sorted((ROOT / "workflows" / "route_cards").glob("*.md")):
    txt = p.read_text(encoding="utf-8-sig")
    for section in ["## Trigger", "## Required first action", "## Forbidden output", "## Downgrade rules", "## Validation expectations"]:
        add(f"{p.name} contains {section}", section in txt)

failed = [c for c in checks if not c[1]]
for name, ok, detail in checks:
    print(("PASS" if ok else "FAIL") + f" | {name}" + (f" | {detail}" if detail else ""))
print(f"\nSummary: {len(checks) - len(failed)} passed / {len(checks)} total")
if failed:
    print("\nFailures:")
    for name, _, detail in failed:
        print(f"- {name}" + (f" ({detail})" if detail else ""))
    sys.exit(1)
