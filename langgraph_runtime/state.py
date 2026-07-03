from __future__ import annotations

from typing import Any, Literal, NotRequired, TypedDict

Intent = Literal[
    "full_agent_workflow",
    "quick_take",
    "direct_specialist",
    "market_news_update",
    "comparison",
    "theme_discovery",
    "needs_clarification",
    "blocked",
]

Route = Literal[
    "equity_full_cycle",
    "quick_take",
    "direct_specialist",
    "market_news_update",
    "multi_asset_comparison",
    "theme_discovery",
    "needs_clarification",
    "blocked",
    "crypto_full_cycle",
    "etf_full_cycle",
    "commodity_full_cycle",
    "fixed_income_full_cycle",
]

AssetClass = Literal["equity", "etf", "crypto", "commodity", "fixed_income", "multi_asset", "theme", "unknown"]

class FinancialAgentState(TypedDict):
    original_user_request: str
    normalized_request: str
    detected_intent: Intent
    route: Route
    asset_identity: str
    asset_class: AssetClass
    horizon: str
    position_context: str
    decision_mode: str
    materiality_plan: dict[str, Any]
    thesis_spine: dict[str, Any]
    portfolio_fit_level: int
    risk_premortem: dict[str, Any]
    ic_conflicts: dict[str, Any]
    monitoring_triggers: dict[str, Any]
    quality_view: dict[str, Any]
    entry_view: dict[str, Any]
    user_context: dict[str, Any]
    missing_context: list[str]
    evidence_plan: dict[str, Any]
    evidence_pack: dict[str, Any]
    specialist_outputs: dict[str, str]
    gate_statuses: dict[str, Any]
    limitations: list[str]
    ic_synthesis: dict[str, Any]
    final_status: Literal["NotStarted", "Preliminary", "Limited", "Blocked", "Complete"]
    report_path: str
    audit_path: str
    errors: list[str]

    # Runtime-control fields. They are not part of the canonical minimum state, but make CLI/test execution explicit.
    mode: NotRequired[Literal["live"]]
    output_dir: NotRequired[str]
    run_id: NotRequired[str]
    thread_id: NotRequired[str]
    allow_interrupts: NotRequired[bool]
    live_router_used: NotRequired[bool]
    completed_nodes: NotRequired[list[str]]


def initial_state(prompt: str, *, mode: str = "live", output_dir: str = "", thread_id: str = "default", allow_interrupts: bool = True) -> FinancialAgentState:
    return {
        "original_user_request": prompt,
        "normalized_request": " ".join(prompt.strip().split()),
        "detected_intent": "needs_clarification",
        "route": "needs_clarification",
        "asset_identity": "Unknown",
        "asset_class": "unknown",
        "horizon": "Unknown",
        "position_context": "Unknown",
        "decision_mode": "Unknown",
        "materiality_plan": {},
        "thesis_spine": {},
        "portfolio_fit_level": 0,
        "risk_premortem": {},
        "ic_conflicts": {},
        "monitoring_triggers": {},
        "quality_view": {},
        "entry_view": {},
        "user_context": {},
        "missing_context": [],
        "evidence_plan": {},
        "evidence_pack": {},
        "specialist_outputs": {},
        "gate_statuses": {},
        "limitations": [],
        "ic_synthesis": {},
        "final_status": "NotStarted",
        "report_path": "",
        "audit_path": "",
        "errors": [],
        "mode": mode,  # type: ignore[typeddict-item]
        "output_dir": output_dir,
        "run_id": "",
        "thread_id": thread_id,
        "allow_interrupts": allow_interrupts,
        "completed_nodes": [],
    }
