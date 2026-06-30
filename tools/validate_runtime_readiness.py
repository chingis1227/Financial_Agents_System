from __future__ import annotations

from pathlib import Path
import re
import sys
import tomllib

ROOT = Path(__file__).resolve().parents[1]

WORKFLOWS = [
    "workflows/equity_full_cycle.md",
    "workflows/etf_full_cycle.md",
    "workflows/commodity_full_cycle.md",
    "workflows/crypto_full_cycle.md",
    "workflows/fixed_income_full_cycle.md",
    "workflows/multi_asset_full_agent_workflow.md",
]

ROUTE_CARDS = [
    "workflows/route_cards/investment_request_router.md",
    "workflows/route_cards/quick_take.md",
    "workflows/route_cards/equity_full_cycle.md",
    "workflows/route_cards/etf_full_cycle.md",
    "workflows/route_cards/commodity_full_cycle.md",
    "workflows/route_cards/crypto_full_cycle.md",
    "workflows/route_cards/fixed_income_full_cycle.md",
    "workflows/route_cards/multi_asset_comparison.md",
    "workflows/route_cards/direct_specialist.md",
]

STALE_DELEGATED_DEFAULT_PATTERNS = [
    re.compile(r"subagents are explicitly requested", re.I),
    re.compile(r"explicitly want a real multi-agent run", re.I),
    re.compile(r"explicit request is required", re.I),
    re.compile(r"only when explicitly requested", re.I),
]

REQUIRED_AGENTS = {
    "master-intake-router", "asset-intake-router", "evidence-collector", "etf-agent",
    "commodity-agent", "crypto-agent", "fixed-income-agent", "valuation-expectations-agent",
    "risk-red-team-agent", "portfolio-fit-agent", "macro-agent", "market-positioning-agent",
    "news-catalysts-agent", "market-sense-agent", "market-intelligence-agent",
    "sector-industry-analysis-agent", "investment-committee-agent",
}

SMOKE_TESTS = {
    "etf-qqq-schg-2026-06-30": [
        "delegated_workflow_audit.md", "evidence_pack.md", "etf_analysis.md",
        "valuation_expectations.md", "risk_red_team.md", "portfolio_fit.md",
        "market_positioning.md", "macro_sensitivity.md", "news_catalysts.md",
        "market_sense.md", "market_intelligence_briefing.md", "sector_context.md",
        "decision_prep_memo.md",
    ],
    "commodity-gold-2026-06-30": [
        "delegated_workflow_audit.md", "evidence_pack.md", "commodity_analysis.md",
        "macro_sensitivity.md", "market_positioning.md", "valuation_expectations.md",
        "risk_red_team.md", "portfolio_fit.md", "news_catalysts.md", "market_sense.md",
        "market_intelligence_briefing.md", "decision_prep_memo.md",
    ],
    "crypto-btc-2026-06-30": [
        "delegated_workflow_audit.md", "evidence_pack.md", "crypto_analysis.md",
        "valuation_expectations.md", "macro_sensitivity.md", "market_positioning.md",
        "risk_red_team.md", "portfolio_fit.md", "news_catalysts.md", "market_sense.md",
        "market_intelligence_briefing.md", "decision_prep_memo.md",
    ],
    "fixed-income-tlt-2026-06-30": [
        "delegated_workflow_audit.md", "evidence_pack.md", "etf_analysis.md",
        "fixed_income_analysis.md", "macro_sensitivity.md", "valuation_expectations.md",
        "risk_red_team.md", "portfolio_fit.md", "market_positioning.md", "news_catalysts.md",
        "market_sense.md", "market_intelligence_briefing.md", "decision_prep_memo.md",
    ],
}

HANDOFF_META_FIELDS = [
    "Artifact", "Subject", "Owner", "Producing agent/skill/workflow", "Workflow",
    "Execution mode", "As-of date/time", "Output status", "Evidence status",
    "Freshness status", "Source scope", "Evidence limits", "Key limitations",
    "Missing gates", "Decision boundary", "Downstream handoff", "Required follow-up",
]

STRUCTURED_HANDOFF_FIELDS = [
    "Artifact", "Subject", "Scope", "Owner", "Producing agent/skill/workflow", "Workflow",
    "Execution mode", "As-of date/time", "Output status", "Evidence status",
    "Freshness status", "Source scope", "Evidence limits", "Key limitations", "Key findings",
    "Missing gates", "Decision boundary", "Decision constraints", "Downstream handoff",
    "Required follow-up",
]

FORBIDDEN_FINAL_ACTION_PATTERNS = [
    re.compile(r"(?im)^\s*(IC Action|Final IC Action|Final action|Action)\s*:\s*(Buy|Sell|Hold|Add|Trim|Exit)\b"),
    re.compile(r"(?im)^\s*Action Box\b"),
    re.compile(r"(?im)^\s*(Buy|Sell|Hold|Add|Trim|Exit)\s+recommendation\b"),
]

checks: list[tuple[str, bool, str]] = []

def add(name: str, ok: bool, detail: str = "") -> None:
    checks.append((name, ok, detail))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")

# Workflows
for rel in WORKFLOWS:
    p = ROOT / rel
    add(f"workflow exists: {rel}", p.exists(), str(p))
    if p.exists():
        txt = read(p)
        for token in ["Execution modes", "decision_prep_memo.md", "evidence_gap_memo.md", "final_investment_memo.md", "Delegated Full Agent Workflow", "Single-agent Full Cycle"]:
            add(f"workflow {rel} contains {token}", token in txt)
        for pat in STALE_DELEGATED_DEFAULT_PATTERNS:
            add(f"workflow {rel} has no stale delegated-default wording: {pat.pattern}", pat.search(txt) is None)

# Documentation-control registration for runtime runbooks
doc_control = ROOT / "implementation" / "01-documentation-control.md"
add("documentation control exists", doc_control.exists(), str(doc_control))
if doc_control.exists():
    doc_txt = read(doc_control)
    for rel in WORKFLOWS:
        add(f"documentation control registers {rel}", f"`{rel}`" in doc_txt)

# Current-state and route-card runtime layer
project_state = ROOT / "PROJECT_STATE.md"
add("project state exists", project_state.exists(), str(project_state))
if project_state.exists():
    ps_txt = read(project_state)
    for token in ["Codex-native first", "Full Cycle", "Quick Take", "Single-agent Full Cycle", "archive/project-history/TASKS.md"]:
        add(f"project state contains {token}", token in ps_txt)
    for token in ["subagents were actually spawned", "do not claim delegated execution", "Single-agent Full Cycle"]:
        add(f"project state enforces delegation fallback: {token}", token in ps_txt)

for rel in ROUTE_CARDS:
    p = ROOT / rel
    add(f"route card exists: {rel}", p.exists(), str(p))
    if p.exists():
        txt = read(p)
        for section in ["## Trigger", "## Required first action", "## Forbidden output", "## Downgrade rules", "## Validation expectations"]:
            add(f"route card {rel} contains {section}", section in txt)
        if doc_control.exists():
            add(f"documentation control registers route card {rel}", f"`{rel}`" in doc_txt)

router_skill = ROOT / ".agents" / "skills" / "investment-workflow-router" / "SKILL.md"
add("investment workflow router skill exists", router_skill.exists(), str(router_skill))
if router_skill.exists():
    rs_txt = read(router_skill)
    for token in ["description:", "exactly 5", "exactly 3", "Selected route card", "does not issue `IC Action`"]:
        add(f"investment workflow router skill contains {token}", token in rs_txt)

add("TASKS archived away from root", not (ROOT / "TASKS.md").exists())
add("IMPLEMENTATION_BACKLOG archived away from root", not (ROOT / "IMPLEMENTATION_BACKLOG.md").exists())
add("archived TASKS exists", (ROOT / "archive" / "project-history" / "TASKS.md").exists())
add("archived IMPLEMENTATION_BACKLOG exists", (ROOT / "archive" / "project-history" / "IMPLEMENTATION_BACKLOG.md").exists())

# Agents
agent_dir = ROOT / ".codex" / "agents"
agent_names = set()
for p in sorted(agent_dir.glob("*.toml")):
    try:
        data = tomllib.loads(read(p))
        name = data.get("name")
        ok_fields = {"name", "description", "developer_instructions"}.issubset(set(data))
        agent_names.add(name)
        add(f"agent TOML valid: {p.name}", bool(name and ok_fields), f"name={name}")
    except Exception as exc:
        add(f"agent TOML valid: {p.name}", False, str(exc))
for agent in sorted(REQUIRED_AGENTS):
    add(f"required agent exists: {agent}", agent in agent_names)

# Skills: method skills should have front matter and required sections. Presentation skills are exempt from method-only sections.
skill_dir = ROOT / ".agents" / "skills"
presentation = {"language-policy", "investment-analytical-style"}
for p in sorted(skill_dir.glob("*/SKILL.md")):
    txt = read(p)
    fm_ok = txt.startswith("---") and "name:" in txt.split("---", 2)[1] and "description:" in txt.split("---", 2)[1]
    add(f"skill front matter: {p.parent.name}", fm_ok)
    if p.parent.name not in presentation:
        section_aliases = {
            "## Purpose": ["## Purpose"],
            "## When to use": ["## When to use"],
            "## What you get": ["## What you get"],
            "## What it will not do": ["## What it will not do"],
            "## Output contract": ["## Output contract", "## Required output core"],
            "## Guardrails": ["## Guardrails", "## Cross-skill guardrails", "## Skill-specific guardrails"],
            "## Failure states": ["## Failure states"],
            "## Quality checks": ["## Quality checks"],
        }
        for section, aliases in section_aliases.items():
            add(f"skill {p.parent.name} section {section}", any(alias in txt for alias in aliases))

# Handoff standard coverage
handoff = ROOT / "workflows" / "handoff_artifact_standard.md"
if handoff.exists():
    txt = read(handoff)
    for token in ["ETF Full Cycle artifacts", "Commodity Full Cycle artifacts", "Crypto Full Cycle artifacts", "Fixed Income Full Cycle artifacts", "Multi-asset comparison artifacts"]:
        add(f"handoff standard contains {token}", token in txt)
else:
    add("handoff standard exists", False)

# Smoke tests and artifacts
for folder, artifacts in SMOKE_TESTS.items():
    base = ROOT / "workflows" / "smoke-tests" / folder
    add(f"smoke folder exists: {folder}", base.exists(), str(base))
    for artifact in artifacts:
        p = base / artifact
        add(f"smoke artifact exists: {folder}/{artifact}", p.exists(), str(p))
        if not p.exists():
            continue
        txt = read(p)
        for pat in FORBIDDEN_FINAL_ACTION_PATTERNS:
            add(f"no final action wording: {folder}/{artifact}/{pat.pattern[:30]}", not pat.search(txt))
        if artifact == "delegated_workflow_audit.md":
            for token in ["## Spawned agents", "## Skipped agents", "## Required artifact checklist", "Final smoke-test result: Pass"]:
                add(f"audit {folder} contains {token}", token in txt)
            unresolved = re.search(r"(?im)^\|\s*`[^`]+`\s*\|\s*`[^`]+`\s*\|\s*(Pending|Blocked|Unavailable|Missing)\s*\|", txt)
            add(f"audit {folder} has no unresolved required agent status", unresolved is None, unresolved.group(0) if unresolved else "")
            if "Final smoke-test result: Pass" in txt:
                add(f"audit {folder} pass has no unresolved status text", not re.search(r"(?i)\b(Pending|Blocked|Unavailable|Missing)\b", txt))
            run_log = base / "run_log.md"
            add(f"run log exists: {folder}", run_log.exists(), str(run_log))
            if run_log.exists():
                rt = read(run_log)
                for token in ["## Spawn record", "Agent id", "Delegated Full Agent Workflow"]:
                    add(f"run log {folder} contains {token}", token in rt)
        else:
            meta = txt.split("## Handoff metadata", 1)[1].split("\n## ", 1)[0] if "## Handoff metadata" in txt else ""
            structured = txt.split("## Structured handoff", 1)[1].split("\n## ", 1)[0] if "## Structured handoff" in txt else ""
            add(f"handoff metadata section: {folder}/{artifact}", bool(meta))
            add(f"structured handoff section: {folder}/{artifact}", bool(structured))
            for field in HANDOFF_META_FIELDS:
                add(f"metadata field {field}: {folder}/{artifact}", re.search(rf"^-\s*{re.escape(field)}\s*:", meta, re.M) is not None)
            for field in STRUCTURED_HANDOFF_FIELDS:
                add(f"structured field {field}: {folder}/{artifact}", re.search(rf"^-\s*{re.escape(field)}\s*:", structured, re.M) is not None)
            if artifact != "decision_prep_memo.md":
                add(f"non-IC boundary: {folder}/{artifact}", "Boundary: Not an IC Action" in txt)
            if artifact == "evidence_pack.md":
                add(f"evidence provenance table: {folder}/{artifact}", "## Source and provenance table" in txt)
                add(
                    f"evidence provenance dated: {folder}/{artifact}",
                    re.search(r"\b20\d{2}-\d{2}-\d{2}\b", txt) is not None,
                )
                add(
                    f"evidence provenance has source locator: {folder}/{artifact}",
                    re.search(r"(?i)(official|source locator|representative source|provenance|FRED|Treasury|CFTC|World Gold Council|Schwab|Invesco|Binance|Coin Metrics|Glassnode|ETF\.com|iShares)", txt) is not None,
                )
            if artifact == "decision_prep_memo.md":
                add(f"decision scenario logic: {folder}/{artifact}", "## Decision-prep scenario logic" in txt or "## Decision-prep synthesis" in txt or "## IC synthesis" in txt)
                add(f"decision consumed module synthesis: {folder}/{artifact}", "Consumed module" in txt or "module" in txt.lower())
    decision = base / "decision_prep_memo.md"
    add(f"decision_prep_memo default exists: {folder}", decision.exists())
    add(f"no final memo forced: {folder}", not (base / "final_investment_memo.md").exists())

# Smoke-test scope hygiene: any smoke folder outside this validator set must be explicitly marked out of scope.
smoke_root = ROOT / "workflows" / "smoke-tests"
if smoke_root.exists():
    known = set(SMOKE_TESTS)
    for d in sorted(p for p in smoke_root.iterdir() if p.is_dir()):
        if d.name not in known:
            marker = d / "OUT_OF_SCOPE_FOR_NON_EQUITY_LEVEL2_VALIDATION.md"
            add(f"out-of-scope smoke folder marked: {d.name}", marker.exists(), str(marker))

# README Russian prompt coverage
readme = ROOT / "README.md"
if readme.exists():
    txt = read(readme)
    for pat in STALE_DELEGATED_DEFAULT_PATTERNS:
        add(f"README has no stale delegated-default wording: {pat.pattern}", pat.search(txt) is None)
    for token in ["subagents actually ran", "Single-agent Full Cycle", "Do not claim delegation"]:
        add(f"README contains delegated execution guardrail: {token}", token in txt)
    for raw_token in ["\u0431\u044b\u0441\u0442\u0440\u044b\u0439 \u043f\u0440\u0435\u0434\u0432\u0430\u0440\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0432\u044b\u0432\u043e\u0434", "\u043f\u043e\u043b\u043d\u044b\u0439 \u0430\u043d\u0430\u043b\u0438\u0437 \u0432 \u043e\u0434\u043d\u043e\u0439 \u0441\u0435\u0441\u0441\u0438\u0438", "\u043f\u043e\u043b\u043d\u044b\u0439 \u043c\u043d\u043e\u0433\u043e\u0430\u0433\u0435\u043d\u0442\u043d\u044b\u0439 \u0437\u0430\u043f\u0443\u0441\u043a", "\u043c\u0435\u043c\u043e \u0434\u043b\u044f \u043f\u043e\u0434\u0433\u043e\u0442\u043e\u0432\u043a\u0438 \u0440\u0435\u0448\u0435\u043d\u0438\u044f", "QQQ", "SCHG", "\u0437\u043e\u043b\u043e\u0442\u0443", "BTC", "TLT", "BTC, \u0437\u043e\u043b\u043e\u0442\u043e, QQQ \u0438 TLT"]:
        token = raw_token.encode("ascii").decode("unicode_escape") if "\\u" in raw_token else raw_token
        add(f"README contains Russian prompt/term: {token}", token.casefold() in txt.casefold())
else:
    add("README exists", False)

# Hardening report
report = ROOT / "implementation" / "non_equity_production_hardening_report.md"
add("hardening report exists", report.exists())
if report.exists():
    txt = read(report)
    for token in ["ETF", "Commodity", "Crypto", "Fixed Income", "Final readiness statement", "0 blocking issues"]:
        add(f"hardening report contains {token}", token in txt)

failed = [c for c in checks if not c[1]]
for name, ok, detail in checks:
    print(("PASS" if ok else "FAIL") + f" | {name}" + (f" | {detail}" if detail else ""))
print(f"\nSummary: {len(checks) - len(failed)} passed / {len(checks)} total")
if failed:
    print("\nFailures:")
    for name, _, detail in failed:
        print(f"- {name}" + (f" ({detail})" if detail else ""))
    sys.exit(1)
