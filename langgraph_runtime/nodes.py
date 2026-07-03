from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from langgraph.types import interrupt

from .artifacts import write_full_workflow_artifacts
from .config import get_settings
from .openai_adapter import OpenAIAdapter
from .routing import classify_request
from .state import FinancialAgentState


def _completed(state: FinancialAgentState, node: str) -> list[str]:
    return [*(state.get("completed_nodes") or []), node]


def _with_node(state: FinancialAgentState, node: str, update: dict[str, Any]) -> dict[str, Any]:
    update["completed_nodes"] = _completed(state, node)
    return update


def intake_router_node(state: FinancialAgentState) -> dict[str, Any]:
    decision = classify_request(state["original_user_request"])
    user_context = dict(state.get("user_context") or {})
    if decision.target_agent:
        user_context["target_agent"] = decision.target_agent
    user_context["required_questions"] = decision.required_questions
    user_context["freshness_required"] = decision.freshness_required
    user_context["route_card"] = decision.route_card
    update = decision.as_state_update()
    update["user_context"] = user_context
    limitations = list(state.get("limitations") or [])
    if decision.freshness_required:
        limitations.append("Freshness-sensitive request; current timestamped evidence is required for live current-market conclusions.")
    update["limitations"] = limitations
    return _with_node(state, "intake_router_node", update)


def clarification_node(state: FinancialAgentState) -> dict[str, Any]:
    missing = state.get("missing_context") or ["asset_identity"]
    payload = {
        "kind": "missing_context",
        "message": "Decision-critical context is missing before this workflow can support a decision-grade output.",
        "missing_context": missing,
        "route": state.get("route"),
        "required_questions": state.get("user_context", {}).get("required_questions", 5),
    }
    if state.get("allow_interrupts", True):
        answer = interrupt(payload)
        user_context = dict(state.get("user_context") or {})
        user_context["clarification_response"] = answer
        return _with_node(state, "clarification_node", {"user_context": user_context, "missing_context": []})
    return _with_node(state, "clarification_node", {"final_status": "Limited", "limitations": [*state.get("limitations", []), f"Missing context: {', '.join(missing)}"]})


def evidence_planner_node(state: FinancialAgentState) -> dict[str, Any]:
    plan = {
        "claim_universe": [
            "asset identity and instrument scope",
            "business/asset-class fundamentals",
            "valuation or expectations",
            "risk/red-team constraints",
            "portfolio fit and missing personalization context",
        ],
        "freshness_required": bool(state.get("user_context", {}).get("freshness_required")),
        "source_hierarchy": ["company filings or issuer material", "official market/economic data", "reputable financial news", "specialist reference layer"],
        "mode": state.get("mode", "dry_run"),
    }
    return _with_node(state, "evidence_planner_node", {"evidence_plan": plan})


def evidence_collector_node(state: FinancialAgentState) -> dict[str, Any]:
    prompt = state["original_user_request"].casefold()
    wants_no_evidence = "without evidence" in prompt or "без доказ" in prompt or "no evidence" in prompt
    freshness_required = bool(state.get("user_context", {}).get("freshness_required"))
    mode = state.get("mode", "dry_run")
    pack: dict[str, Any] = {
        "status": "Blocked" if wants_no_evidence else ("Limited" if mode == "dry_run" else "Collected"),
        "as_of": datetime.now(timezone.utc).isoformat(),
        "sources": [],
        "claims_supported": [] if wants_no_evidence else ["identity", "workflow scope", "dry-run module contract coverage"],
        "freshness_required": freshness_required,
    }
    limitations = list(state.get("limitations") or [])
    if wants_no_evidence:
        limitations.append("User requested output without evidence; evidence readiness gate must fail.")
    elif mode == "dry_run":
        pack["sources"] = ["Dry-run synthetic source placeholder; no live market facts collected."]
        limitations.append("Dry-run mode does not collect live market evidence; conclusions are Limited and not a final IC Action.")
    else:
        settings = get_settings(require_api_key=True)
        adapter = OpenAIAdapter(settings)
        summary = adapter.responses_text(
            system="You are an evidence planning assistant. Do not invent source facts. Return a concise evidence-scope note only.",
            user=f"Prepare evidence collection scope for: {state['original_user_request']}",
        )
        pack["sources"] = ["OpenAI API live evidence-scope note; external source retrieval still requires configured tools."]
        pack["live_scope_note"] = summary
        limitations.append("Live OpenAI adapter ran; current market source retrieval remains constrained unless external data tools are added.")
    return _with_node(state, "evidence_collector_node", {"evidence_pack": pack, "limitations": limitations})


def evidence_readiness_gate_node(state: FinancialAgentState) -> dict[str, Any]:
    pack = state.get("evidence_pack") or {}
    gates = dict(state.get("gate_statuses") or {})
    status = pack.get("status", "Blocked")
    if status == "Blocked":
        gates["evidence_readiness"] = {"status": "Blocked", "reason": "Evidence pack is blocked or intentionally absent."}
        payload = {"kind": "evidence_readiness_failed", "route": state.get("route"), "reason": gates["evidence_readiness"]["reason"]}
        if state.get("allow_interrupts", True):
            resume_value = interrupt(payload)
            gates["evidence_readiness"]["human_resume"] = resume_value
            return _with_node(state, "evidence_readiness_gate_node", {"gate_statuses": gates})
        return _with_node(state, "evidence_readiness_gate_node", {"gate_statuses": gates, "final_status": "Blocked"})
    if status == "Limited":
        gates["evidence_readiness"] = {"status": "Limited", "reason": "Dry-run evidence is synthetic; do not issue final IC Action."}
    else:
        gates["evidence_readiness"] = {"status": "Pass", "reason": "Evidence collection stage completed for configured source scope."}
    return _with_node(state, "evidence_readiness_gate_node", {"gate_statuses": gates})


def equity_analysis_node(state: FinancialAgentState) -> dict[str, Any]:
    return _specialist(state, "equity_analysis_node", "equity_company_analysis", [
        f"Asset: {state.get('asset_identity')}",
        "Business-quality view is dry-run scaffolded from the equity-company-analysis skill contract.",
        "No live company facts are invented.",
    ])


def macro_node(state: FinancialAgentState) -> dict[str, Any]:
    return _specialist(state, "macro_node", "macro_analysis", ["Macro context is included as a required full-cycle module.", "Dry-run mode records method coverage, not a current macro call."])


def sector_node(state: FinancialAgentState) -> dict[str, Any]:
    return _specialist(state, "sector_node", "sector_industry_analysis", ["Sector/industry context module executed in scaffold mode.", "No unsupported peer or market-share claims are made."])


def financial_statement_node(state: FinancialAgentState) -> dict[str, Any]:
    return _specialist(state, "financial_statement_node", "financial_statement_analysis", ["Financial statement module is present for material company analysis.", "Dry-run output does not invent revenue, margin, cash-flow, or balance-sheet facts."])


def valuation_node(state: FinancialAgentState) -> dict[str, Any]:
    gates = dict(state.get("gate_statuses") or {})
    gates["valuation"] = {"status": "Limited", "reason": "No live valuation dataset in dry-run mode."}
    update = _specialist(state, "valuation_node", "valuation_expectations", ["Valuation/expectations module ran in Limited dry-run mode.", "No positive action can pass without live valuation evidence."])
    update["gate_statuses"] = gates
    return update


def risk_red_team_node(state: FinancialAgentState) -> dict[str, Any]:
    gates = dict(state.get("gate_statuses") or {})
    gates["risk"] = {"status": "Limited", "reason": "Risk review scaffold completed; source-backed risk evidence still required."}
    if state.get("allow_interrupts", True):
        resume_value = interrupt({
            "kind": "risk_gate_failed",
            "route": state.get("route"),
            "reason": gates["risk"]["reason"],
            "required_follow_up": "Provide or collect source-backed risk evidence before any final IC action.",
        })
        gates["risk"]["human_resume"] = resume_value
    update = _specialist(state, "risk_red_team_node", "risk_red_team", ["Risk red-team module ran and constrains any final action.", "Boundary: Not an IC Action."])
    update["gate_statuses"] = gates
    return update


def news_catalysts_node(state: FinancialAgentState) -> dict[str, Any]:
    return _specialist(state, "news_catalysts_node", "news_catalysts", ["News/catalyst module is present.", "Freshness-sensitive conclusions require current timestamped sources."])


def market_positioning_node(state: FinancialAgentState) -> dict[str, Any]:
    return _specialist(state, "market_positioning_node", "market_positioning", ["Market positioning module is present.", "Dry-run output does not claim current positioning data."])


def portfolio_fit_node(state: FinancialAgentState) -> dict[str, Any]:
    gates = dict(state.get("gate_statuses") or {})
    missing = state.get("position_context") == "Unknown" or not state.get("user_context", {}).get("portfolio_context")
    gates["portfolio_fit"] = {"status": "Limited" if missing else "Pass", "reason": "User portfolio context is missing; portfolio fit is not personalized." if missing else "Portfolio context present."}
    limitations = list(state.get("limitations") or [])
    if missing:
        limitations.append("Portfolio Fit is Limited because user portfolio context is missing.")
    update = _specialist(state, "portfolio_fit_node", "portfolio_fit", ["Portfolio fit module ran.", gates["portfolio_fit"]["reason"], "No exact allocation instruction is issued."])
    update["gate_statuses"] = gates
    update["limitations"] = limitations
    return update


def _specialist(state: FinancialAgentState, node: str, key: str, bullets: list[str]) -> dict[str, Any]:
    outputs = dict(state.get("specialist_outputs") or {})
    outputs[key] = "\n".join([f"# {key.replace('_', ' ').title()}", "", "Analysis Status: Limited", "IC Action Status: Not an IC Action", "Boundary: Not an IC Action. Method output only.", "", *[f"- {b}" for b in bullets]])
    return _with_node(state, node, {"specialist_outputs": outputs})


def direct_specialist_node(state: FinancialAgentState) -> dict[str, Any]:
    agent = state.get("user_context", {}).get("target_agent", "specialist-agent")
    outputs = dict(state.get("specialist_outputs") or {})
    outputs[agent] = "\n".join([
        f"# Direct specialist output — {agent}",
        "",
        "Analysis Status: Preliminary",
        "IC Action Status: Not an IC Action",
        "Boundary: Not an IC Action",
        "",
        f"Subject: {state.get('asset_identity', 'Unknown')}",
        "This direct specialist route is scoped and cannot issue a final buy/sell/hold/add/trim/exit action.",
    ])
    return _with_node(state, "direct_specialist_node", {"specialist_outputs": outputs, "final_status": "Preliminary"})


def market_news_node(state: FinancialAgentState) -> dict[str, Any]:
    outputs = dict(state.get("specialist_outputs") or {})
    outputs["market_news_update"] = "\n".join([
        "# Market/news update",
        "",
        "Analysis Status: Limited",
        "IC Action Status: Not an IC Action",
        "Boundary: Not an IC Action",
        "",
        "Freshness-sensitive market/news questions require current timestamped sources. Dry-run mode does not explain actual current price moves.",
    ])
    return _with_node(state, "market_news_node", {"specialist_outputs": outputs, "final_status": "Limited"})


def comparison_node(state: FinancialAgentState) -> dict[str, Any]:
    outputs = dict(state.get("specialist_outputs") or {})
    outputs["comparison"] = "\n".join([
        "# Comparison scaffold",
        "",
        "Analysis Status: Limited",
        "IC Action Status: Not an IC Action",
        "Boundary: Not an IC Action",
        "",
        f"Comparison subject: {state.get('asset_identity')}",
        "A role-based comparison can be prepared, but no universal winner or final allocation is issued without gates.",
    ])
    return _with_node(state, "comparison_node", {"specialist_outputs": outputs})


def investment_committee_node(state: FinancialAgentState) -> dict[str, Any]:
    gates = dict(state.get("gate_statuses") or {})
    evidence_status = (gates.get("evidence_readiness") or {}).get("status", "Blocked")
    valuation_status = (gates.get("valuation") or {}).get("status", "Blocked")
    risk_status = (gates.get("risk") or {}).get("status", "Blocked")
    portfolio_status = (gates.get("portfolio_fit") or {}).get("status", "Blocked")
    all_pass = all(s == "Pass" for s in [evidence_status, valuation_status, risk_status, portfolio_status])
    if all_pass:
        action_status = "Eligible for IC Action"
        final_status = "Complete"
        summary = "All required gates passed. IC may issue a final action if the report body supports it."
        if state.get("allow_interrupts", True):
            interrupt({
                "kind": "final_ic_confirmation_required",
                "route": state.get("route"),
                "asset_identity": state.get("asset_identity"),
                "message": "Confirm before issuing any final IC action.",
            })
    else:
        action_status = "Not an IC Action"
        final_status = "Blocked" if evidence_status == "Blocked" else "Limited"
        summary = "One or more required gates are incomplete, Limited, or Blocked; no positive final IC Action is issued."
    synthesis = {
        "ic_action_status": action_status,
        "summary": summary,
        "consumed_modules": sorted((state.get("specialist_outputs") or {}).keys()),
        "gate_summary": {"evidence": evidence_status, "valuation": valuation_status, "risk": risk_status, "portfolio_fit": portfolio_status},
    }
    return _with_node(state, "investment_committee_node", {"ic_synthesis": synthesis, "final_status": final_status})


def report_writer_node(state: FinancialAgentState) -> dict[str, Any]:
    if state.get("route") in {"quick_take", "direct_specialist", "market_news_update"}:
        return _with_node(state, "report_writer_node", {"report_path": "", "audit_path": ""})
    report_path, audit_path = write_full_workflow_artifacts(state)
    return _with_node(state, "report_writer_node", {"report_path": report_path, "audit_path": audit_path})


def audit_writer_node(state: FinancialAgentState) -> dict[str, Any]:
    # Full artifact writing is idempotent and happens in report_writer_node; this node exists as a graph-visible audit boundary.
    return _with_node(state, "audit_writer_node", {})


def quick_take_node(state: FinancialAgentState) -> dict[str, Any]:
    outputs = dict(state.get("specialist_outputs") or {})
    outputs["quick_take"] = "\n".join([
        "# Quick Take",
        "",
        "Analysis Status: Preliminary",
        "IC Action Status: Not an IC Action",
        "Boundary: Not an IC Action",
        "",
        f"Subject: {state.get('asset_identity', 'Unknown')}",
        "Quick Take is chat-only: no investment_report.md, no audit folder, and no final IC Action.",
    ])
    return _with_node(state, "quick_take_node", {"specialist_outputs": outputs, "final_status": "Preliminary"})


def theme_discovery_node(state: FinancialAgentState) -> dict[str, Any]:
    outputs = dict(state.get("specialist_outputs") or {})
    outputs["theme_discovery"] = "\n".join([
        "# Theme discovery",
        "",
        "Analysis Status: Preliminary",
        "IC Action Status: Not an IC Action",
        "Boundary: Not an IC Action",
        "",
        "Theme discovery requires evidence and downstream specialist gates before any capital-allocation conclusion.",
    ])
    return _with_node(state, "theme_discovery_node", {"specialist_outputs": outputs, "final_status": "Preliminary"})


def generic_asset_workflow_node(state: FinancialAgentState) -> dict[str, Any]:
    route = state.get("route", "asset_workflow")
    key_by_route = {
        "crypto_full_cycle": "crypto_asset_analysis",
        "etf_full_cycle": "etf_wrapper_analysis",
        "commodity_full_cycle": "commodity_analysis",
        "fixed_income_full_cycle": "fixed_income_analysis",
    }
    key = key_by_route.get(route, "asset_class_analysis")
    outputs = dict(state.get("specialist_outputs") or {})
    outputs[key] = "\n".join([
        f"# {key.replace('_', ' ').title()}",
        "",
        "Analysis Status: Limited",
        "IC Action Status: Not an IC Action",
        "Boundary: Not an IC Action. Method output only.",
        "",
        f"Route: {route}",
        f"Subject: {state.get('asset_identity', 'Unknown')}",
        "This asset-class full-workflow scaffold preserves the selected route and does not run the equity-only subgraph.",
        "No live asset-class evidence is invented in dry-run mode.",
    ])
    gates = dict(state.get("gate_statuses") or {})
    gates.setdefault("valuation", {"status": "Limited", "reason": "Asset-class valuation/expectations equivalent requires live evidence."})
    gates.setdefault("risk", {"status": "Limited", "reason": "Asset-class risk gate requires source-backed specialist evidence."})
    gates.setdefault("portfolio_fit", {"status": "Limited", "reason": "User portfolio context is missing or incomplete."})
    limitations = list(state.get("limitations") or [])
    limitations.append(f"{route} currently uses a dry-run asset-class scaffold; no final IC Action is issued.")
    return _with_node(state, "generic_asset_workflow_node", {"specialist_outputs": outputs, "gate_statuses": gates, "limitations": limitations})
