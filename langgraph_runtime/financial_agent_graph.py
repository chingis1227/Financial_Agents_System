from __future__ import annotations

import argparse
import sys
import uuid
from typing import Any

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph

from .config import get_settings
from .nodes import (
    intake_router_node,
    audit_writer_node,
    clarification_node,
    comparison_node,
    direct_specialist_node,
    equity_analysis_node,
    evidence_collector_node,
    evidence_planner_node,
    evidence_readiness_gate_node,
    financial_statement_node,
    generic_asset_workflow_node,
    investment_committee_node,
    macro_node,
    materiality_planner_node,
    market_intelligence_node,
    market_news_node,
    market_positioning_node,
    market_sense_node,
    news_catalysts_node,
    portfolio_fit_node,
    quick_take_node,
    report_writer_node,
    risk_red_team_node,
    sector_node,
    theme_discovery_node,
    valuation_node,
)
from .state import FinancialAgentState, initial_state


def build_equity_subgraph() -> Any:
    """Build the reusable equity specialist subgraph.

    The parent graph owns routing, evidence, gates, report and audit. The subgraph
    owns the ordered equity specialist modules for the MVP full-cycle path.
    """
    builder = StateGraph(FinancialAgentState)
    builder.add_node("equity_analysis_node", equity_analysis_node)
    builder.add_node("macro_node", macro_node)
    builder.add_node("sector_node", sector_node)
    builder.add_node("financial_statement_node", financial_statement_node)
    builder.add_node("valuation_node", valuation_node)
    builder.add_node("risk_red_team_node", risk_red_team_node)
    builder.add_node("news_catalysts_node", news_catalysts_node)
    builder.add_node("market_positioning_node", market_positioning_node)
    builder.add_node("market_sense_node", market_sense_node)
    builder.add_node("market_intelligence_node", market_intelligence_node)
    builder.add_node("portfolio_fit_node", portfolio_fit_node)
    builder.add_edge(START, "equity_analysis_node")
    builder.add_edge("equity_analysis_node", "macro_node")
    builder.add_edge("macro_node", "sector_node")
    builder.add_edge("sector_node", "financial_statement_node")
    builder.add_edge("financial_statement_node", "valuation_node")
    builder.add_edge("valuation_node", "risk_red_team_node")
    builder.add_edge("risk_red_team_node", "news_catalysts_node")
    builder.add_edge("news_catalysts_node", "market_positioning_node")
    builder.add_edge("market_positioning_node", "market_sense_node")
    builder.add_edge("market_sense_node", "market_intelligence_node")
    builder.add_edge("market_intelligence_node", "portfolio_fit_node")
    builder.add_edge("portfolio_fit_node", END)
    return builder.compile()


def build_graph(*, checkpointer: InMemorySaver | None = None) -> Any:
    builder = StateGraph(FinancialAgentState)
    builder.add_node("intake_router_node", intake_router_node)
    builder.add_node("clarification_node", clarification_node)
    builder.add_node("evidence_planner_node", evidence_planner_node)
    builder.add_node("evidence_collector_node", evidence_collector_node)
    builder.add_node("evidence_readiness_gate_node", evidence_readiness_gate_node)
    builder.add_node("materiality_planner_node", materiality_planner_node)
    builder.add_node("equity_workflow_subgraph", build_equity_subgraph())
    builder.add_node("generic_asset_workflow_node", generic_asset_workflow_node)
    builder.add_node("direct_specialist_node", direct_specialist_node)
    builder.add_node("quick_take_node", quick_take_node)
    builder.add_node("market_news_node", market_news_node)
    builder.add_node("comparison_node", comparison_node)
    builder.add_node("theme_discovery_node", theme_discovery_node)
    builder.add_node("investment_committee_node", investment_committee_node)
    builder.add_node("report_writer_node", report_writer_node)
    builder.add_node("audit_writer_node", audit_writer_node)

    builder.add_edge(START, "intake_router_node")
    builder.add_conditional_edges(
        "intake_router_node",
        _route_after_intake,
        {
            "clarification_node": "clarification_node",
            "evidence_planner_node": "evidence_planner_node",
            "direct_specialist_node": "direct_specialist_node",
            "quick_take_node": "quick_take_node",
            "market_news_node": "market_news_node",
            "comparison_node": "comparison_node",
            "theme_discovery_node": "theme_discovery_node",
        },
    )
    builder.add_edge("clarification_node", "evidence_planner_node")
    builder.add_edge("evidence_planner_node", "evidence_collector_node")
    builder.add_edge("evidence_collector_node", "materiality_planner_node")
    builder.add_edge("materiality_planner_node", "evidence_readiness_gate_node")
    builder.add_conditional_edges(
        "evidence_readiness_gate_node",
        _route_after_evidence_gate,
        {
            "equity_workflow_subgraph": "equity_workflow_subgraph",
            "comparison_node": "comparison_node",
            "report_writer_node": "report_writer_node",
            "generic_asset_workflow_node": "generic_asset_workflow_node",
        },
    )
    builder.add_edge("equity_workflow_subgraph", "investment_committee_node")
    builder.add_edge("generic_asset_workflow_node", "investment_committee_node")
    builder.add_edge("comparison_node", "investment_committee_node")
    builder.add_edge("investment_committee_node", "report_writer_node")
    builder.add_edge("direct_specialist_node", "report_writer_node")
    builder.add_edge("quick_take_node", "report_writer_node")
    builder.add_edge("market_news_node", "report_writer_node")
    builder.add_edge("theme_discovery_node", "report_writer_node")
    builder.add_edge("report_writer_node", "audit_writer_node")
    builder.add_edge("audit_writer_node", END)
    return builder.compile(checkpointer=checkpointer or InMemorySaver())


def _route_after_intake(state: FinancialAgentState) -> str:
    if state.get("detected_intent") == "needs_clarification" or state.get("route") == "needs_clarification":
        return "clarification_node"
    if state.get("detected_intent") == "full_agent_workflow" and state.get("missing_context"):
        return "clarification_node"
    if state.get("detected_intent") == "direct_specialist":
        return "direct_specialist_node"
    if state.get("detected_intent") == "quick_take":
        return "quick_take_node"
    if state.get("detected_intent") == "market_news_update":
        return "market_news_node"
    if state.get("detected_intent") == "comparison":
        return "evidence_planner_node"
    if state.get("detected_intent") == "theme_discovery":
        return "theme_discovery_node"
    return "evidence_planner_node"


def _route_after_evidence_gate(state: FinancialAgentState) -> str:
    gate = (state.get("gate_statuses") or {}).get("evidence_readiness", {})
    if gate.get("status") == "Blocked":
        return "report_writer_node"
    if state.get("route") == "multi_asset_comparison":
        return "comparison_node"
    if state.get("route") == "equity_full_cycle":
        return "equity_workflow_subgraph"
    return "generic_asset_workflow_node"


def run_financial_agent(
    prompt: str,
    *,
    dry_run: bool = True,
    live: bool = False,
    output_dir: str = "",
    thread_id: str | None = None,
    allow_interrupts: bool = True,
) -> dict[str, Any]:
    if live and dry_run:
        dry_run = False
    mode = "live" if live else "dry_run"
    if live:
        get_settings(require_api_key=True)
    tid = thread_id or f"financial-agent-{uuid.uuid4()}"
    state = initial_state(prompt, mode=mode, output_dir=output_dir, thread_id=tid, allow_interrupts=allow_interrupts)
    state["run_id"] = str(uuid.uuid4())
    graph = build_graph()
    config = {"configurable": {"thread_id": tid}}
    result = graph.invoke(state, config=config)
    return result


def stream_financial_agent(prompt: str, *, dry_run: bool = True, live: bool = False, thread_id: str | None = None) -> list[Any]:
    tid = thread_id or f"financial-agent-{uuid.uuid4()}"
    state = initial_state(prompt, mode="live" if live else "dry_run", thread_id=tid)
    graph = build_graph()
    events = []
    for event in graph.stream(state, config={"configurable": {"thread_id": tid}}, stream_mode="updates"):
        events.append(event)
    return events


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python -m langgraph_runtime.financial_agent_graph")
    sub = parser.add_subparsers(dest="command", required=True)

    run = sub.add_parser("run", help="Run one financial-agent graph request")
    run.add_argument("--prompt", required=True)
    run.add_argument("--dry-run", action="store_true", help="Run without OpenAI API calls")
    run.add_argument("--live", action="store_true", help="Use OpenAI API-backed live mode")
    run.add_argument("--output-dir", default="")
    run.add_argument("--thread-id", default="")
    run.add_argument("--no-interrupts", action="store_true", help="Record Limited/Blocked statuses instead of pausing")

    sub.add_parser("chat", help="Start a minimal interactive chat loop")
    args = parser.parse_args(argv)

    if args.command == "chat":
        print("Financial Agent LangGraph chat. Type 'exit' to quit.")
        while True:
            prompt = input("> ").strip()
            if prompt.casefold() in {"exit", "quit"}:
                return 0
            result = run_financial_agent(prompt, dry_run=True, live=False, allow_interrupts=False)
            _print_result(result)
        return 0

    if args.live and args.dry_run:
        print("Choose either --dry-run or --live, not both.", file=sys.stderr)
        return 2
    try:
        result = run_financial_agent(
            args.prompt,
            dry_run=not args.live,
            live=args.live,
            output_dir=args.output_dir,
            thread_id=args.thread_id or None,
            allow_interrupts=not args.no_interrupts,
        )
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    _print_result(result)
    return 0


def _print_result(result: dict[str, Any]) -> None:
    if "__interrupt__" in result:
        print("Interrupted for human input:")
        print(result["__interrupt__"])
        return
    print(f"Status: {result.get('final_status')}")
    print(f"Intent: {result.get('detected_intent')}")
    print(f"Route: {result.get('route')}")
    print(f"Asset: {result.get('asset_identity')} ({result.get('asset_class')})")
    if result.get("report_path"):
        print(f"Report: {result.get('report_path')}")
        print(f"Audit: {result.get('audit_path')}")
    else:
        outputs = result.get("specialist_outputs") or {}
        for name, content in outputs.items():
            print(f"\n[{name}]\n{content}")


if __name__ == "__main__":
    raise SystemExit(main())





