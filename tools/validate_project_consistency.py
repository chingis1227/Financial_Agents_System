from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
checks: list[tuple[str, bool, str]] = []


CANONICAL_UX_DOCS = [
    p for p in sorted((ROOT / "implementation").glob("*.md"))
    if p.name not in {
        "final-system-audit-report.md",
        "non_equity_production_hardening_report.md",
        "p10-qa-execution-report.md",
        "runtime-baseline-report.md",
    }
]
ACTIVE_RUNTIME_UX_DOCS = (
    CANONICAL_UX_DOCS
    + sorted((ROOT / ".codex" / "agents").glob("*.toml"))
    + sorted((ROOT / ".agents" / "skills").glob("*/SKILL.md"))
    + sorted((ROOT / "workflows").glob("*.md"))
    + sorted((ROOT / "workflows" / "route_cards").glob("*.md"))
    + sorted((ROOT / "workflows" / "smoke-tests").glob("*/*.md"))
)

RUNTIME_COMMAND_MODEL_DOCS = {
    "00-master-rules.md",
    "02-canonical-architecture.md",
    "04-evidence-layer.md",
    "05-routing-and-workflows.md",
    "06-agent-contracts.md",
    "07-investment-committee-and-report-schemas.md",
    "09-system-acceptance-qa.md",
    "11-skill-contracts.md",
    "13-codex-runtime-architecture.md",
}

OLD_USER_MODE_PATTERNS = [
    r"default(?:s)?\s+to\s+Full Cycle",
    r"Concrete-asset[^\n]{0,120}default(?:s)?\s+to\s+Full Cycle",
    r"Full Cycle\s+default\s+triggers",
    r"Single-agent Full Cycle",
    r"Delegated Full Agent Workflow",
    r"user-facing Full Cycle",
    r"no full cycle",
    r"\bSingle-agent\b",
    r"\bDelegated mode\b",
    r"\bdelegated mode\b",
    r"\bDelegated workflow\b",
    r"\bdelegated workflow\b",
    r"Full [A-Za-z ]+ Cycle",
]

COMMAND_AGENT_MAP = {
    "RISK": "risk-red-team-agent",
    "VAL": "valuation-expectations-agent",
    "MACRO": "macro-agent",
    "NEWS": "news-catalysts-agent",
    "PORTFOLIO": "portfolio-fit-agent",
    "SECTOR": "sector-industry-analysis-agent",
    "EVIDENCE": "evidence-collector",
    "POSITIONING": "market-positioning-agent",
    "SENSE": "market-sense-agent",
    "INTEL": "market-intelligence-agent",
    "EQUITY": "equity-agent",
    "ETF": "etf-agent",
    "COMMODITY": "commodity-agent",
    "CRYPTO": "crypto-agent",
    "FI": "fixed-income-agent",
    "WINNERS": "structural-winners-discovery-agent",
    "IC": "investment-committee-agent",
}

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
    ".agents/skills/language-policy/SKILL.md",
    ".agents/skills/investment-analytical-style/SKILL.md",
    "tools/validate_language_style.py",
    "tests/behavior/language_style_cases.yaml",
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
    "AGENT:",
    "QUICK:",
    "audit metadata",
    "archive/project-history/TASKS.md",
    "implementation/non_equity_production_hardening_report.md",
    "tools\\validate_project_consistency.py",
    "tools\\validate_language_style.py",
]:
    add(f"PROJECT_STATE contains {token}", token in state, token)
for cmd, agent in COMMAND_AGENT_MAP.items():
    add(f"PROJECT_STATE command map contains {cmd}", f"`{cmd}:`" in state and f"`{agent}`" in state, f"{cmd}->{agent}")

# AGENTS.md should not use archived build docs as active runtime sources.
agents = read("AGENTS.md") if exists("AGENTS.md") else ""
add("AGENTS reads PROJECT_STATE first", "Read `PROJECT_STATE.md`" in agents)
add("AGENTS points to route router", "workflows/route_cards/investment_request_router.md" in agents)
for forbidden in ["Read `TASKS.md`", "Read `IMPLEMENTATION_BACKLOG.md`", "TASKS.md` for active work", "IMPLEMENTATION_BACKLOG.md` for phase"]:
    add(f"AGENTS has no archived active runtime instruction: {forbidden}", forbidden not in agents)
for token in ["validate_project_consistency.py", "validate_language_style.py", "validate_behavior_contracts.py", "validate_runtime_readiness.py"]:
    add(f"AGENTS requires validator {token}", token in agents)
for token in ["AGENT:", "QUICK:", "live-only", "language-policy", "investment-analytical-style"]:
    add(f"AGENTS contains production workflow rule {token}", token in agents, token)
for cmd, agent in COMMAND_AGENT_MAP.items():
    add(f"AGENTS command map contains {cmd}", f"`{cmd}:`" in agents and f"`{agent}`" in agents, f"{cmd}->{agent}")

# User-facing UX docs should not present old selectable modes.
ux_docs = [
    ROOT / "PROJECT_STATE.md",
    ROOT / "AGENTS.md",
    ROOT / "README.md",
    ROOT / ".agents" / "skills" / "investment-workflow-router" / "SKILL.md",
]
old_user_mode_patterns = [
    re.compile(r"\|\s*`?Full Cycle`?\s*\|", re.I),
    re.compile(r"\|\s*`?Single-agent Full Cycle`?\s*\|", re.I),
    re.compile(r"##\s*Full Cycle\b", re.I),
    re.compile(r"##\s*Single-agent Full Cycle\b", re.I),
    re.compile(r"Use when.*Full Cycle", re.I),
    re.compile(r"Use when.*Single-agent", re.I),
]
for path in ux_docs:
    if not path.exists():
        continue
    txt = path.read_text(encoding="utf-8-sig")
    rel = path.relative_to(ROOT).as_posix()
    for pattern in old_user_mode_patterns:
        add(f"{rel} has no old selectable user mode: {pattern.pattern}", pattern.search(txt) is None)
    add(f"{rel} documents AGENT command", "AGENT:" in txt)
    add(f"{rel} documents QUICK command", "QUICK:" in txt)

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


# Canonical docs must not reintroduce old selectable UX modes. Internal file
# names like *_full_cycle.md are allowed elsewhere; these active-behavior
# phrases are not allowed in canonical runtime behavior docs.
for doc in ACTIVE_RUNTIME_UX_DOCS:
    if doc.exists() and doc.is_file():
        txt = read(doc)
        for pattern in OLD_USER_MODE_PATTERNS:
            add(f"{doc.relative_to(ROOT)} has no old active UX phrase: {pattern}", re.search(pattern, txt, re.IGNORECASE) is None)
        if doc.name in RUNTIME_COMMAND_MODEL_DOCS:
            add(
                f"{doc.relative_to(ROOT)} mentions AGENT/large-workflow command model",
                "AGENT:" in txt or "large workflow" in txt or "large-workflow" in txt,
            )
    else:
        add(f"active runtime UX doc exists: {doc.relative_to(ROOT)}", False)

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
