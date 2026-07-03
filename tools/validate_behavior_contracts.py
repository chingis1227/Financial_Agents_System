from __future__ import annotations

from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
BEHAVIOR = ROOT / "tests" / "behavior"
checks: list[tuple[str, bool, str]] = []

EXACT_SPECIALIST_BOUNDARY = "Boundary: Not an IC Action"
EXPECTED_COMMANDS = {
    "RISK", "VAL", "MACRO", "NEWS", "PORTFOLIO", "SECTOR", "EVIDENCE", "POSITIONING",
    "INTEL", "EQUITY", "ETF", "COMMODITY", "CRYPTO", "FI", "WINNERS", "IC",
}

valid_routes = {
    "quick_take",
    "equity_full_cycle",
    "etf_full_cycle",
    "commodity_full_cycle",
    "crypto_full_cycle",
    "fixed_income_full_cycle",
    "multi_asset_comparison",
    "direct_specialist",
}


def add(name: str, ok: bool, detail: str = "") -> None:
    checks.append((name, ok, detail))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig") if path.exists() else ""


def load(name: str):
    p = BEHAVIOR / name
    add(f"fixture exists: {name}", p.exists(), str(p))
    if not p.exists():
        return []
    try:
        data = json.loads(p.read_text(encoding="utf-8-sig"))
        add(f"fixture parses: {name}", isinstance(data, list), name)
        return data if isinstance(data, list) else []
    except Exception as exc:
        add(f"fixture parses: {name}", False, str(exc))
        return []


command_map_fixture = load("command_map.yaml")
COMMAND_AGENT_MAP = {
    str(c.get("command")): str(c.get("agent"))
    for c in command_map_fixture
    if isinstance(c, dict) and c.get("command") and c.get("agent")
}
COMMAND_SKILL_MAP = {
    str(c.get("command")): str(c.get("skill"))
    for c in command_map_fixture
    if isinstance(c, dict) and c.get("command") and c.get("skill")
}
add("command map fixture has every expected command", set(COMMAND_AGENT_MAP) == EXPECTED_COMMANDS, str(sorted(COMMAND_AGENT_MAP)))
add("command map fixture has skill for every expected command", set(COMMAND_SKILL_MAP) == EXPECTED_COMMANDS, str(sorted(COMMAND_SKILL_MAP)))
add("command map fixture has no duplicate commands", len(COMMAND_AGENT_MAP) == len(command_map_fixture), str(len(command_map_fixture)))

routing = load("routing_cases.yaml")
guardrails = load("guardrail_cases.yaml")
reports = load("report_contract_cases.yaml")
language_style = load("language_style_cases.yaml")
golden = load("golden_prompts.yaml")
all_prompt_cases = routing + golden

fixture_command_agent_map = {str(c.get("command")): str(c.get("agent")) for c in command_map_fixture if isinstance(c, dict)}
fixture_command_skill_map = {str(c.get("command")): str(c.get("skill")) for c in command_map_fixture if isinstance(c, dict)}
add("command map fixture matches command->agent map", fixture_command_agent_map == COMMAND_AGENT_MAP, str(fixture_command_agent_map))
add("command map fixture matches command->skill map", fixture_command_skill_map == COMMAND_SKILL_MAP, str(fixture_command_skill_map))

fixture_text = "\n".join(
    (BEHAVIOR / name).read_text(encoding="utf-8-sig")
    for name in [
        "routing_cases.yaml",
        "guardrail_cases.yaml",
        "report_contract_cases.yaml",
        "language_style_cases.yaml",
        "golden_prompts.yaml",
        "command_map.yaml",
    ]
    if (BEHAVIOR / name).exists()
)
fixture_text_without_controlled_label = fixture_text.replace("Non-delegated audit fallback", "CONTROLLED_FALLBACK_LABEL")
add("active behavior fixtures have no generic delegated wording", re.search(r"(?i)\bdelegated\b|delegated_", fixture_text_without_controlled_label) is None)

for case in all_prompt_cases:
    cid = case.get("id", "<missing>")
    route = case.get("expected_route")
    command = case.get("command")
    rq = case.get("required_questions")
    prompt_raw = str(case.get("prompt", ""))
    prompt = prompt_raw.lower()
    add(f"{cid} has expected route", route in valid_routes, str(route))
    add(f"{cid} has valid required question count", rq in {0, 3, 5}, str(rq))
    add(f"{cid} prompt is not placeholder-corrupted", prompt_raw.count("?") / max(1, len(prompt_raw)) < 0.20, prompt_raw)
    add(
        f"{cid} prompt has semantic text",
        re.search(r"[\u0400-\u04FF]", prompt_raw) is not None or re.search(r"[A-Za-z]{4,}", prompt_raw) is not None,
        prompt_raw,
    )
    if command == "AGENT":
        add(f"{cid} AGENT command asks 5 questions", rq == 5, str(rq))
        add(f"{cid} AGENT command requires spawned subagents or Limited fallback", case.get("requires_spawned_subagents") is True, str(case))
        add(f"{cid} AGENT prompt starts with prefix", prompt_raw.upper().startswith("AGENT:"), prompt_raw)
    if command == "QUICK" or route == "quick_take":
        add(f"{cid} QUICK command asks 3 questions", rq == 3, str(rq))
        add(f"{cid} QUICK command uses canonical quick_take route", route == "quick_take", str(route))
        add(
            f"{cid} QUICK prompt has prefix or explicit quick trigger",
            prompt_raw.upper().startswith("QUICK:")
            or any(
                t in prompt
                for t in [
                    "quick",
                    "short",
                    "fast",
                    "preliminary",
                    "brief",
                    "быстро",
                    "кратко",
                    "глянь",
                    "коротко",
                ]
            ),
            prompt_raw,
        )
    if command in COMMAND_AGENT_MAP:
        add(f"{cid} specialist command routes direct", route == "direct_specialist", str(route))
        add(f"{cid} specialist command target agent", case.get("expected_agent") == COMMAND_AGENT_MAP[command], str(case.get("expected_agent")))
        add(f"{cid} specialist command prompt starts with prefix", prompt_raw.upper().startswith(f"{command}:"), prompt_raw)
        add(f"{cid} specialist command does not ask AGENT questions", rq == 0, str(rq))
    if command == "ORDINARY_ROUTER":
        add(f"{cid} ordinary router is not quick", route != "quick_take", str(route))
    if case.get("freshness_required"):
        add(f"{cid} freshness case has freshness flag", True)

# Required golden coverage.
required_ids = {
    "golden_agent_microsoft",
    "golden_quick_microsoft",
    "golden_ordinary_microsoft_router",
    "golden_agent_btc_three_year",
    "golden_agent_qqq_schg",
    "golden_agent_gold_latest",
    "golden_agent_tlt",
    "golden_nvda_today_quick_reaction",
    "golden_premature_final_memo",
    *{f"golden_command_{cmd.lower()}" for cmd in COMMAND_AGENT_MAP},
}
seen = {c.get("id") for c in golden}
for rid in sorted(required_ids):
    add(f"golden prompt covered: {rid}", rid in seen, rid)

for case in golden:
    command = str(case.get("command", "")).upper()
    if command in COMMAND_AGENT_MAP:
        add(
            f"{case.get('id')} specialist golden requires exact visible boundary",
            case.get("required_boundary") == EXACT_SPECIALIST_BOUNDARY,
            str(case),
        )

# Every command must appear in routing and golden fixtures.
routing_commands = {c.get("command") for c in routing}
golden_commands = {c.get("command") for c in golden}
for cmd in ["AGENT", "QUICK", *COMMAND_AGENT_MAP.keys()]:
    add(f"routing fixture covers command {cmd}", cmd in routing_commands, cmd)
    add(f"golden fixture covers command {cmd}", cmd in golden_commands, cmd)

# Guardrail fixture coverage.
required_guardrails = {
    "non_ic_no_final_action",
    "agent_requires_spawn_or_limited_fallback",
    "spawned_subagent_workflow_requires_actual_spawn",
    "freshness_requires_timestamp_or_limited",
    "missing_context_not_hard_avoid",
    "quick_take_no_final_action_escape_hatch",
    "russian_report_language_style_gate",
}
seen_guardrails = {c.get("id") for c in guardrails}
for rid in sorted(required_guardrails):
    add(f"guardrail covered: {rid}", rid in seen_guardrails, rid)

# Report contract fixture coverage.
required_contracts = {"quick_contract", "agent_workflow_contract", "reader_facing_report_contract", "specialist_contract", "russian_language_style_contract"}
seen_contracts = {c.get("id") for c in reports}
for rid in sorted(required_contracts):
    add(f"report contract covered: {rid}", rid in seen_contracts, rid)
quick_contract = next((c for c in reports if c.get("id") == "quick_contract"), {})
quick_forbidden = set(quick_contract.get("forbidden", []))
for token in ["Action Box", "IC Action: Buy", "IC Action: Sell", "IC Action: Hold", "final_investment_memo.md"]:
    add(f"QUICK contract forbids final action artifact/wording: {token}", token in quick_forbidden, token)
agent_contract = next((c for c in reports if c.get("id") == "agent_workflow_contract"), {})
add("AGENT contract requires spawned subagents or Limited fallback", agent_contract.get("requires_spawned_subagents_or_limited_fallback") is True)
reader_report_contract = next((c for c in reports if c.get("id") == "reader_facing_report_contract"), {})
reader_forbidden = set(reader_report_contract.get("investment_report_forbidden", []))
for token in ["Artifact Type", "Analysis Status", "IC Action Status", "Gate status", "Mode:", "Route:", "Boundary: Not an IC Action", "Portfolio Fit is Limited", "Missing gates", "Limited", "Blocked", "module status", "handoff", "gate failed", "not personalized gate"]:
    add(f"reader-facing report forbids technical token: {token}", token in reader_forbidden, token)
reader_required = set(reader_report_contract.get("investment_report_required", []))
for token in ["Portfolio role", "general terms", "not provided"]:
    add(f"reader-facing report requires Portfolio role wording: {token}", token in reader_required, token)
reader_required_ru = set(reader_report_contract.get("investment_report_required_ru", []))
for token in ["Портфельная роль", "в общем виде", "контекст не указан"]:
    add(f"reader-facing report requires Russian Portfolio role wording: {token}", token in reader_required_ru, token)
audit_required = set(reader_report_contract.get("audit_required", []))
for token in ["Portfolio Fit: Limited / not personalized", "General Portfolio Role Mode"]:
    add(f"audit contract retains Portfolio Fit technical status: {token}", token in audit_required, token)
specialist_contract = next((c for c in reports if c.get("id") == "specialist_contract"), {})
add("specialist contract requires exact boundary label", specialist_contract.get("required_boundary") == EXACT_SPECIALIST_BOUNDARY)
add("specialist contract requires visible boundary line", specialist_contract.get("required_visible_boundary_line") is True)
add("specialist contract boundary line prefix exact", specialist_contract.get("required_boundary_line_prefix") == EXACT_SPECIALIST_BOUNDARY)
ic_shortcut_forbidden = set(specialist_contract.get("ic_shortcut_forbidden", []))
for token in ["Action Box", "IC Action: Buy", "IC Action: Sell", "IC Action: Hold", "Buy recommendation", "Sell recommendation", "Hold recommendation"]:
    add(f"IC shortcut specialist contract forbids {token}", token in ic_shortcut_forbidden, token)
russian_language_contract = next((c for c in reports if c.get("id") == "russian_language_style_contract"), {})
add("Russian language contract requires language-policy skill", ".agents/skills/language-policy/SKILL.md" in russian_language_contract.get("required_skills", []))
add("Russian language contract requires investment-analytical-style skill", ".agents/skills/investment-analytical-style/SKILL.md" in russian_language_contract.get("required_skills", []))
for token in ["growth exposure", "headline earnings", "profit pools", "customer wins", "downside-модель"]:
    add(
        f"Russian language contract forbids Run-glish phrase: {token}",
        token in set(russian_language_contract.get("forbidden_phrases", [])),
        token,
    )

seen_language_cases = {c.get("id") for c in language_style}
for rid in [
    "russian_report_rejects_growth_exposure",
    "russian_report_rejects_headline_earnings",
    "russian_report_rejects_hybrid",
    "russian_report_allows_controlled_labels",
    "russian_report_clean_investment_style",
    "russian_report_rejects_encoding_corruption",
]:
    add(f"language style fixture covered: {rid}", rid in seen_language_cases, rid)

# Strict QUICK source checks.
strict_quick_sources = [
    ("master rules", ROOT / "implementation" / "00-master-rules.md"),
    ("quick take route card", ROOT / "workflows" / "route_cards" / "quick_take.md"),
    ("ic schemas", ROOT / "implementation" / "07-investment-committee-and-report-schemas.md"),
    ("acceptance qa", ROOT / "implementation" / "09-system-acceptance-qa.md"),
]
quick_escape_hatch_patterns = [
    re.compile(r"No\s+final\s+IC\s+Action\s+unless", re.I),
    re.compile(r"IC\s+Action\s+Status\s*:\s*.*\bunless\b", re.I),
    re.compile(r"Quick\s+Take[^\n|.]*\bunless\b[^\n|.]*(?:gate|gates)[^\n|.]*(?:pass|complete|completed)", re.I),
    re.compile(r"\bunless\b[^\n|.]*(?:required\s+)?(?:IC\s+)?gates?[^\n|.]*(?:pass|complete|completed)", re.I),
]
for label, path in strict_quick_sources:
    txt = path.read_text(encoding="utf-8-sig") if path.exists() else ""
    add(f"{label} says Quick Take never issues final IC Action", "Quick Take never issues final IC Action" in txt, str(path))
    for pattern in quick_escape_hatch_patterns:
        add(f"{label} has no Quick Take final-gates escape hatch: {pattern.pattern}", pattern.search(txt) is None, str(path))


# Specialist command shortcuts are scoped handoffs, including IC:. They must not
# create a direct final-action escape hatch.
direct_specialist_text = read(ROOT / "workflows" / "route_cards" / "direct_specialist.md")
router_skill_text = read(ROOT / ".agents" / "skills" / "investment-workflow-router" / "SKILL.md")
for label, txt in [("direct specialist route card", direct_specialist_text), ("router skill", router_skill_text)]:
    add(
        f"{label} has no IC shortcut final-action carveout",
        "unless `IC:`" not in txt
        and "IC:` may produce" not in txt
        and "non-IC specialist commands" not in txt
        and "except gated `IC:`" not in txt,
    )
    add(
        f"{label} forbids final IC Action for IC shortcut",
        "including `IC:`" in txt and ("No final `IC Action`" in txt or "must not use `IC Action`" in txt),
    )

for case in routing + golden:
    command = str(case.get("command", "")).upper()
    if command in COMMAND_AGENT_MAP:
        add(
            f"{case.get('id')} specialist fixture stays direct/non-final",
            case.get("expected_route") == "direct_specialist" and case.get("required_questions") == 0,
            str(case),
        )

# Router skill and route card command coverage.
router = (ROOT / ".agents" / "skills" / "investment-workflow-router" / "SKILL.md").read_text(encoding="utf-8-sig") if (ROOT / ".agents" / "skills" / "investment-workflow-router" / "SKILL.md").exists() else ""
route_router = (ROOT / "workflows" / "route_cards" / "investment_request_router.md").read_text(encoding="utf-8-sig") if (ROOT / "workflows" / "route_cards" / "investment_request_router.md").exists() else ""
direct_card = (ROOT / "workflows" / "route_cards" / "direct_specialist.md").read_text(encoding="utf-8-sig") if (ROOT / "workflows" / "route_cards" / "direct_specialist.md").exists() else ""
for token in ["AGENT:", "QUICK:", "Command mapping", "Selected route card", "does not issue `IC Action`"]:
    add(f"router skill contains {token}", token in router, token)
for cmd, agent in COMMAND_AGENT_MAP.items():
    for label, txt in [("router skill", router), ("investment route card", route_router), ("direct specialist route card", direct_card)]:
        add(f"{label} maps {cmd} to {agent}", f"`{cmd}:`" in txt and f"`{agent}`" in txt, f"{cmd}->{agent}")
    profile_path = ROOT / ".codex" / "agents" / f"{agent}.toml"
    profile_text = read(profile_path)
    add(f"{cmd} target profile exists: {agent}", profile_path.exists(), str(profile_path))
    add(
        f"{cmd} target profile requires exact specialist boundary label",
        EXACT_SPECIALIST_BOUNDARY in profile_text,
        str(profile_path),
    )
    skill_dir = COMMAND_SKILL_MAP[cmd]
    skill_path = ROOT / ".agents" / "skills" / skill_dir / "SKILL.md"
    skill_text = read(skill_path)
    add(f"{cmd} matching skill exists: {skill_dir}", skill_path.exists(), str(skill_path))
    add(
        f"{cmd} matching skill requires exact specialist boundary label",
        EXACT_SPECIALIST_BOUNDARY in skill_text,
        str(skill_path),
    )
    add(
        f"{cmd} golden fixture requires exact visible specialist boundary",
        any(c.get("command") == cmd and c.get("required_boundary") == EXACT_SPECIALIST_BOUNDARY for c in golden),
        cmd,
    )
add(
    "direct specialist route card requires visible boundary line",
    "visible boundary line that begins exactly" in direct_card and EXACT_SPECIALIST_BOUNDARY in direct_card,
)
for token in ["AGENT:", "QUICK:", "Do not claim agent workflow", "subagents were actually spawned"]:
    add(f"investment route card contains {token}", token in route_router, token)
add(
    "investment router counts ambiguity inside required 5/3 question block where possible",
    "count the clarification inside the required 5-question `AGENT:` block or 3-question `QUICK:` block" in route_router,
)
add(
    "investment router no longer resolves ambiguity before required questions by default",
    "resolve that blocking ambiguity before the 5 or 3 questions" not in route_router,
)
add(
    "router skill counts ambiguity inside required 5/3 question block where possible",
    "count the clarification inside the required 5-question `AGENT:` block or 3-question `QUICK:` block" in router,
)
add(
    "router skill reserves blocking clarification for truly unroutable identity conflicts",
    "Ask a separate blocking clarification only when the request is truly unroutable" in router,
)
add(
    "router skill no longer asks broad blocking ambiguity clarification first",
    "ask the minimum blocking clarification first" not in router,
)

failed = [c for c in checks if not c[1]]
for name, ok, detail in checks:
    print(("PASS" if ok else "FAIL") + f" | {name}" + (f" | {detail}" if detail else ""))
print(f"\nSummary: {len(checks) - len(failed)} passed / {len(checks)} total")
if failed:
    print("\nFailures:")
    for name, _, detail in failed:
        print(f"- {name}" + (f" ({detail})" if detail else ""))
    sys.exit(1)
