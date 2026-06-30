from __future__ import annotations

from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
BEHAVIOR = ROOT / "tests" / "behavior"
checks: list[tuple[str, bool, str]] = []

def add(name: str, ok: bool, detail: str = "") -> None:
    checks.append((name, ok, detail))

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

routing = load("routing_cases.yaml")
guardrails = load("guardrail_cases.yaml")
reports = load("report_contract_cases.yaml")
golden = load("golden_prompts.yaml")

valid_routes = {
    "quick_take",
    "equity_full_cycle",
    "etf_full_cycle",
    "commodity_full_cycle",
    "crypto_full_cycle",
    "fixed_income_full_cycle",
    "multi_asset_comparison",
    "direct_specialist",
    "quick_take_or_market_reaction",
}

for case in routing + golden:
    cid = case.get("id", "<missing>")
    route = case.get("expected_route")
    add(f"{cid} has expected route", route in valid_routes, str(route))
    rq = case.get("required_questions")
    add(f"{cid} has valid required question count", rq in {0, 3, 5}, str(rq))
    prompt_raw = str(case.get("prompt", ""))
    question_mark_ratio = prompt_raw.count("?") / max(1, len(prompt_raw))
    add(f"{cid} prompt is not placeholder-corrupted", question_mark_ratio < 0.20, prompt_raw)
    add(
        f"{cid} prompt has semantic text",
        re.search(r"[\u0400-\u04FF]", prompt_raw) is not None or re.search(r"[A-Za-z]{4,}", prompt_raw) is not None,
        prompt_raw,
    )

# Required golden coverage
required_ids = {
    "golden_microsoft_full_cycle",
    "golden_microsoft_quick",
    "golden_btc_three_year",
    "golden_qqq_schg",
    "golden_gold_latest",
    "golden_tlt",
    "golden_nvda_today",
    "golden_risk_only",
    "golden_premature_final_memo",
}
seen = {c.get("id") for c in golden}
for rid in sorted(required_ids):
    add(f"golden prompt covered: {rid}", rid in seen, rid)

# Policy checks over fixtures
for case in routing + golden:
    cid = case.get("id", "<missing>")
    prompt_raw = str(case.get("prompt", ""))
    prompt = prompt_raw.lower()
    route = case.get("expected_route")
    quick_terms = ["quick", "short", "fast", "\u0431\u044b\u0441\u0442\u0440", "\u043f\u0440\u0435\u0434\u0432\u0430\u0440", "\u043a\u0440\u0430\u0442\u043a"]
    explicit_quick = any(term in prompt for term in quick_terms)
    if case.get("explicit_quick") is True or route == "quick_take":
        add(f"{cid} explicit quick prompt contains quick trigger", explicit_quick, prompt_raw)
    if "microsoft" in prompt and route == "equity_full_cycle":
        add(f"{cid} Microsoft Full Cycle prompt has no quick trigger", not explicit_quick, prompt_raw)
    if any(term in prompt for term in ["инвест", "buy", "покуп", "hold", "sell", "add", "стоит ли"]):
        if not explicit_quick and route not in {"direct_specialist", "quick_take_or_market_reaction"}:
            add(f"{cid} investment action is not quick take", route != "quick_take", str(route))
            add(f"{cid} investment action asks 5 questions", case.get("required_questions") == 5, str(case.get("required_questions")))
    if route == "quick_take":
        add(f"{cid} quick take asks 3 questions", case.get("required_questions") == 3, str(case.get("required_questions")))
    if case.get("freshness_required"):
        add(f"{cid} freshness case has freshness flag", True)

# Guardrail fixture coverage
required_guardrails = {
    "non_ic_no_final_action",
    "delegated_requires_spawn",
    "freshness_requires_timestamp_or_limited",
    "missing_context_not_hard_avoid",
    "quick_take_no_final_action_escape_hatch",
}
seen_guardrails = {c.get("id") for c in guardrails}
for rid in sorted(required_guardrails):
    add(f"guardrail covered: {rid}", rid in seen_guardrails, rid)

# Report contract fixture coverage
required_contracts = {"quick_take_contract", "full_cycle_contract", "direct_specialist_contract"}
seen_contracts = {c.get("id") for c in reports}
for rid in sorted(required_contracts):
    add(f"report contract covered: {rid}", rid in seen_contracts, rid)
quick_contract = next((c for c in reports if c.get("id") == "quick_take_contract"), {})
quick_forbidden = set(quick_contract.get("forbidden", []))
for token in ["Action Box", "IC Action: Buy", "IC Action: Sell", "IC Action: Hold", "final_investment_memo.md"]:
    add(f"quick take contract forbids final action artifact/wording: {token}", token in quick_forbidden, token)

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
        add(
            f"{label} has no Quick Take final-gates escape hatch: {pattern.pattern}",
            pattern.search(txt) is None,
            str(path),
        )

# Check route cards and router skill contain fixture-related rules.
router = (ROOT / ".agents" / "skills" / "investment-workflow-router" / "SKILL.md").read_text(encoding="utf-8-sig") if (ROOT / ".agents" / "skills" / "investment-workflow-router" / "SKILL.md").exists() else ""
for token in ["exactly 5", "exactly 3", "Concrete-asset investment-action", "Delegated Full Agent Workflow", "timestamped sources"]:
    add(f"router skill contains {token}", token in router, token)

route_router = (ROOT / "workflows" / "route_cards" / "investment_request_router.md").read_text(encoding="utf-8-sig") if (ROOT / "workflows" / "route_cards" / "investment_request_router.md").exists() else ""
for token in ["Full Cycle route", "Quick Take route", "Do not answer a concrete-asset", "subagents were actually spawned"]:
    add(f"investment route card contains {token}", token in route_router, token)

failed = [c for c in checks if not c[1]]
for name, ok, detail in checks:
    print(("PASS" if ok else "FAIL") + f" | {name}" + (f" | {detail}" if detail else ""))
print(f"\nSummary: {len(checks) - len(failed)} passed / {len(checks)} total")
if failed:
    print("\nFailures:")
    for name, _, detail in failed:
        print(f"- {name}" + (f" ({detail})" if detail else ""))
    sys.exit(1)
