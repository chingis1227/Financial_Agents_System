from __future__ import annotations

from pathlib import Path
import json
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
    "sector-industry-analysis-agent", "investment-committee-agent", "equity-agent",
    "structural-winners-discovery-agent",
}

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

SMOKE_TESTS = {
    "etf-qqq-schg-2026-06-30": [
        "agent_workflow_audit.md", "evidence_pack.md", "etf_analysis.md",
        "valuation_expectations.md", "risk_red_team.md", "portfolio_fit.md",
        "market_positioning.md", "macro_sensitivity.md", "news_catalysts.md",
        "market_sense.md", "market_intelligence_briefing.md", "sector_context.md",
        "decision_prep_memo.md",
    ],
    "commodity-gold-2026-06-30": [
        "agent_workflow_audit.md", "evidence_pack.md", "commodity_analysis.md",
        "macro_sensitivity.md", "market_positioning.md", "valuation_expectations.md",
        "risk_red_team.md", "portfolio_fit.md", "news_catalysts.md", "market_sense.md",
        "market_intelligence_briefing.md", "decision_prep_memo.md",
    ],
    "crypto-btc-2026-06-30": [
        "agent_workflow_audit.md", "evidence_pack.md", "crypto_analysis.md",
        "valuation_expectations.md", "macro_sensitivity.md", "market_positioning.md",
        "risk_red_team.md", "portfolio_fit.md", "news_catalysts.md", "market_sense.md",
        "market_intelligence_briefing.md", "decision_prep_memo.md",
    ],
    "fixed-income-tlt-2026-06-30": [
        "agent_workflow_audit.md", "evidence_pack.md", "etf_analysis.md",
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

VALID_EXECUTION_MODES = {"Agent workflow with spawned subagents"}
STALE_RUNTIME_LABELS = ["Delegated Full Agent Workflow", "Single-agent Full Cycle"]

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
        for token in ["Execution modes", "decision_prep_memo.md", "evidence_gap_memo.md", "final_investment_memo.md", "Agent workflow with spawned subagents"]:
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
    for token in ["Codex-native first", "AGENT:", "QUICK:", "audit metadata", "archive/project-history/TASKS.md"]:
        add(f"project state contains {token}", token in ps_txt)
    for token in ["automatically spawn", "live-only", "language-policy", "investment-analytical-style"]:
        add(f"project state enforces production live workflow: {token}", token in ps_txt)
    for cmd, agent in COMMAND_AGENT_MAP.items():
        add(f"project state command map contains {cmd}", f"`{cmd}:`" in ps_txt and f"`{agent}`" in ps_txt)

canonical_live_docs = [
    ("master rules", ROOT / "implementation" / "00-master-rules.md"),
    ("routing workflows", ROOT / "implementation" / "05-routing-and-workflows.md"),
]
for label, path in canonical_live_docs:
    add(f"{label} live doc exists", path.exists(), str(path))
    if path.exists():
        txt = read(path)
        add(f"{label} requires automatic spawned subagents", "automatically" in txt and "subagents" in txt)
        add(f"{label} blocks production when subagents unavailable", "Blocked" in txt and "subagents" in txt)

canonical_ambiguity_docs = [
    ("runtime architecture", ROOT / "implementation" / "13-codex-runtime-architecture.md"),
    ("investment router route card", ROOT / "workflows" / "route_cards" / "investment_request_router.md"),
    ("investment router skill", ROOT / ".agents" / "skills" / "investment-workflow-router" / "SKILL.md"),
]
for label, path in canonical_ambiguity_docs:
    add(f"{label} ambiguity doc exists", path.exists(), str(path))
    if path.exists():
        txt = read(path)
        add(
            f"{label} counts identity clarification inside required questions where possible",
            "count the clarification inside the required 5-question `AGENT:` block or 3-question `QUICK:` block" in txt
            or "Count identity clarification inside the required intake block where possible" in txt
            or "count exact ticker/ISIN/CUSIP" in txt,
        )
        add(
            f"{label} has no resolve-identity-before-questions rule",
            "resolve identity first, then ask the 5 or 3 questions" not in txt,
        )

for rel in WORKFLOWS:
    p = ROOT / rel
    if p.exists():
        txt = read(p)
        for token in ["Runtime Execution Plan", "decision mode", "Materiality Gate", "Thesis Spine", "monitoring_triggers"]:
            add(f"workflow {rel} contains institutional token {token}", token in txt, token)

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
    for token in ["description:", "AGENT:", "QUICK:", "Command mapping", "exactly 5", "exactly 3", "Selected route card", "does not issue `IC Action`"]:
        add(f"investment workflow router skill contains {token}", token in rs_txt)
    add(
        "investment workflow router skill counts ambiguity inside required questions where possible",
        "count the clarification inside the required 5-question `AGENT:` block or 3-question `QUICK:` block" in rs_txt,
    )
    add(
        "investment workflow router skill reserves separate clarification for truly unroutable identity conflicts",
        "Ask a separate blocking clarification only when the request is truly unroutable" in rs_txt,
    )
    add(
        "investment workflow router skill has no broad blocking-clarification-first wording",
        "ask the minimum blocking clarification first" not in rs_txt,
    )
    for cmd, agent in COMMAND_AGENT_MAP.items():
        add(f"router skill maps {cmd}", f"`{cmd}:`" in rs_txt and f"`{agent}`" in rs_txt)

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
    for token in ["ETF large-workflow artifacts", "Commodity large-workflow artifacts", "Crypto large-workflow artifacts", "Fixed Income large-workflow artifacts", "Multi-asset comparison artifacts"]:
        add(f"handoff standard contains {token}", token in txt)
    add(
        "handoff standard blocks AGENT when subagents cannot run",
        "Blocked" in txt and "subagents" in txt,
    )
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

        # Execution mode labels in smoke-test artifacts must use the current controlled vocabulary.
        for stale in STALE_RUNTIME_LABELS:
            add(f"smoke artifact has no stale execution label: {folder}/{artifact}/{stale}", stale not in txt)
        for match in re.finditer(r"(?im)^\s*-?\s*Execution mode:\s*`?([^`\r\n]+?)`?\s*$", txt):
            mode = match.group(1).strip().rstrip(".")
            add(f"smoke artifact execution mode is current: {folder}/{artifact}", mode in VALID_EXECUTION_MODES, mode)
        if artifact == "agent_workflow_audit.md":
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
                for token in ["## Spawn record", "Agent id"]:
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
    for token in ["AGENT:", "QUICK:", "automatically", "live-only"]:
        add(f"README contains delegated execution guardrail: {token}", token in txt)
    for cmd, agent in COMMAND_AGENT_MAP.items():
        add(f"README command map contains {cmd}", f"`{cmd}:`" in txt and f"`{agent}`" in txt)
    for raw_token in ["AGENT: Microsoft", "QUICK: Microsoft", "RISK: Microsoft", "VAL: Nvidia", "NEWS: why did Nvidia", "ETF: QQQ vs SCHG"]:
        token = raw_token.encode("ascii").decode("unicode_escape") if "\\u" in raw_token else raw_token
        add(f"README contains command prompt/term: {token}", token.casefold() in txt.casefold())
else:
    add("README exists", False)

# Integrated Automation Lab
automation_lab = ROOT / "automation_lab"
add("integrated Automation Lab directory exists", automation_lab.exists(), str(automation_lab))
if automation_lab.exists():
    required_lab_files = [
        "fa_automation.py",
        "README.md",
        "ROADMAP.md",
        "MERGE_READINESS.md",
        "requirements-live.txt",
        "config/route_check_cases.json",
        "quick_data/__init__.py",
        "agent_data/__init__.py",
        "data_sources/README.md",
        "tests/test_route_check_cli.py",
        "tests/test_quick_answer_cli.py",
        "tests/test_agent_run_cli.py",
    ]
    for rel in required_lab_files:
        add(f"Automation Lab file exists: {rel}", (automation_lab / rel).exists(), rel)

    add(
        "Automation Lab has no nested Git repository",
        not (automation_lab / ".git").exists(),
        str(automation_lab / ".git"),
    )

    lab_cli = automation_lab / "fa_automation.py"
    if lab_cli.exists():
        txt = read(lab_cli)
        add("Automation Lab resolves project root from env or parent", 'FA_AUTOMATION_PROJECT_ROOT' in txt and "LAB_ROOT.parent" in txt)
        add("Automation Lab does not hard-code separate project root", 'Path(r"C:\\Users\\ShumeikoYe\\OneDrive\\Documents\\Financial Agent System")' not in txt)

    merge_doc = automation_lab / "MERGE_READINESS.md"
    if merge_doc.exists():
        txt = read(merge_doc)
        for token in ["one GitHub repository", "must not contain a nested `.git/`", "live-acceptance --require-live", "Financial Agent Reports"]:
            add(f"Automation Lab merge readiness contains {token}", token in txt)

    lab_readme = automation_lab / "README.md"
    if lab_readme.exists():
        txt = read(lab_readme)
        add("Automation Lab README documents unified repository location", "Unified repository location" in txt and "Financial Agent System\\automation_lab" in txt)
        add("Automation Lab README uses parent venv commands", "..\\.venv\\Scripts\\python.exe" in txt)

    gitignore = ROOT / ".gitignore"
    add("root .gitignore exists for Automation Lab ignores", gitignore.exists(), str(gitignore))
    if gitignore.exists():
        txt = read(gitignore)
        for token in ["automation_lab/runs/", "automation_lab/data_runs/", "automation_lab/.venv/", "automation_lab/**/__pycache__/"]:
            add(f"root .gitignore ignores {token}", token in txt)

    try:
        import subprocess

        tracked_generated = subprocess.run(
            ["git", "ls-files", "automation_lab/runs", "automation_lab/data_runs", "automation_lab/.venv", "automation_lab/**/__pycache__"],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        tracked_paths = [line.strip() for line in tracked_generated.stdout.splitlines() if line.strip() and not line.strip().endswith("/.gitkeep") and not line.strip().endswith("\\.gitkeep") and Path(line.strip()).name != ".gitkeep"]
        add(
            "Automation Lab generated/local artifacts are not tracked",
            tracked_generated.returncode == 0 and not tracked_paths,
            ", ".join(tracked_paths[:10]),
        )
    except Exception as exc:
        add("Automation Lab generated/local tracking check runs", False, str(exc))

if project_state.exists():
    add("project state documents integrated Automation Lab", "Integrated Automation Lab live acceptance" in ps_txt and "automation_lab/" in ps_txt)
if readme.exists():
    add("README documents integrated Automation Lab", "Integrated Automation Lab live acceptance" in read(readme) and "automation_lab/" in read(readme))

# Hardening report
report = ROOT / "implementation" / "non_equity_production_hardening_report.md"
add("hardening report exists", report.exists())
if report.exists():
    txt = read(report)
    for token in ["ETF", "Commodity", "Crypto", "Fixed Income", "Final readiness statement", "0 blocking issues"]:
        add(f"hardening report contains {token}", token in txt)

# Codex SDK control layer
package_json = ROOT / "package.json"
add("Codex SDK package.json exists", package_json.exists(), str(package_json))
if package_json.exists():
    try:
        package = json.loads(read(package_json))
        dependencies = package.get("dependencies", {})
        scripts = package.get("scripts", {})
        add("Codex SDK dependency declared", "@openai/codex-sdk" in dependencies)
        for script in ["build", "test", "codex:run", "codex:resume", "codex:doctor"]:
            add(f"package script exists: {script}", script in scripts)
    except Exception as exc:
        add("package.json parses as JSON", False, str(exc))

codex_config = ROOT / ".codex" / "config.toml"
add("Codex repo config exists", codex_config.exists(), str(codex_config))
if codex_config.exists():
    try:
        config = tomllib.loads(read(codex_config))
        agents_config = config.get("agents", {})
        add("Codex config has [agents]", isinstance(agents_config, dict))
        add("Codex config has agents.max_threads", agents_config.get("max_threads") == 12)
        add("Codex config has agents.max_depth", agents_config.get("max_depth") == 1)
        add("Codex config has agents.job_max_runtime_seconds", agents_config.get("job_max_runtime_seconds") == 1800)
    except Exception as exc:
        add("Codex config parses as TOML", False, str(exc))

sdk_files = [
    "src/codex-sdk/cli.ts",
    "src/codex-sdk/runner.ts",
    "src/codex-sdk/types.ts",
    "tests/codex-sdk.test.ts",
    "tsconfig.json",
]
for rel in sdk_files:
    add(f"Codex SDK source file exists: {rel}", (ROOT / rel).exists(), rel)

cli_source = ROOT / "src" / "codex-sdk" / "cli.ts"
runner_source = ROOT / "src" / "codex-sdk" / "runner.ts"
test_source = ROOT / "tests" / "codex-sdk.test.ts"
if cli_source.exists():
    txt = read(cli_source)
    add("Codex SDK CLI supports live execution", "--live" in txt)
    add("Codex SDK CLI has live flag", 'case "--live"' in txt)
    add("Codex SDK CLI rejects thread id on run", "does not accept --thread-id" in txt)
    add("Codex SDK CLI supports resume command", 'command === "resume"' in txt)
if runner_source.exists():
    txt = read(runner_source)
    add("Codex SDK runner imports @openai/codex-sdk", '@openai/codex-sdk' in txt)
    add("Codex SDK runner contains live request branch", "request.live" in txt)
    add("Codex SDK runner uses collision-safe log suffix", "randomUUID" in txt and "getMilliseconds" in txt)
    add("Codex SDK runner log root is outside repository path", "Financial Agent Reports" in txt and "_sdk_runs" in txt)
    add("Codex SDK runner separates run and resume modes", 'request.mode === "resume"' in txt)
if test_source.exists():
    txt = read(test_source)
    for token in ["live run", "resume run", "doctor", "default log root", "rejects thread id on run", "workspace and sandbox"]:
        add(f"Codex SDK tests cover {token}", token in txt)

sdk_docs = [
    ("README", ROOT / "README.md"),
    ("PROJECT_STATE", ROOT / "PROJECT_STATE.md"),
    ("AGENTS", ROOT / "AGENTS.md"),
    ("sync contract", ROOT / "implementation" / "15-documentation-sync-contract.md"),
    ("runtime architecture", ROOT / "implementation" / "13-codex-runtime-architecture.md"),
]
false_runtime_claims = [
    re.compile(r"(?i)\buses\s+OpenAI Agents SDK\b"),
    re.compile(r"(?i)\bOpenAI Agents SDK runtime\s+(?:is\s+)?(?:present|implemented|active)\b"),
]
for label, path in sdk_docs:
    add(f"{label} exists for Codex SDK docs", path.exists(), str(path))
    if path.exists():
        txt = read(path)
        add(f"{label} mentions Codex SDK", "Codex SDK" in txt)
        if label != "runtime architecture":
            add(f"{label} documents npm.cmd for SDK checks", "npm.cmd" in txt)
        for pat in false_runtime_claims:
            add(f"{label} has no false OpenAI Agents SDK runtime claim: {pat.pattern}", pat.search(txt) is None)

if readme.exists():
    txt = read(readme)
    for token in ["Run through Codex SDK", "--live", "Financial Agent Reports\\_sdk_runs"]:
        add(f"README Codex SDK section contains {token}", token in txt)

langgraph_token_expectations = {
    "langgraph_runtime/state.py": ["decision_mode", "materiality_plan", "thesis_spine", "portfolio_fit_level"],
    "langgraph_runtime/routing.py": ["decision_mode", "materiality_plan", "SENSE"],
    "langgraph_runtime/nodes.py": ["decision_mode", "materiality_plan", "thesis_spine", "portfolio_fit_level"],
    "langgraph_runtime/artifacts.py": ["decision_mode", "materiality_plan", "thesis_spine", "portfolio_fit_level"],
}
for rel, tokens in langgraph_token_expectations.items():
    p = ROOT / rel
    add(f"LangGraph institutional file exists: {rel}", p.exists(), rel)
    if p.exists():
        txt = read(p)
        for token in tokens:
            add(f"{rel} contains {token}", token in txt, token)

failed = [c for c in checks if not c[1]]
for name, ok, detail in checks:
    print(("PASS" if ok else "FAIL") + f" | {name}" + (f" | {detail}" if detail else ""))
print(f"\nSummary: {len(checks) - len(failed)} passed / {len(checks)} total")
if failed:
    print("\nFailures:")
    for name, _, detail in failed:
        print(f"- {name}" + (f" ({detail})" if detail else ""))
    sys.exit(1)
