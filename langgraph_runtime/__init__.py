"""Additive Python LangGraph runtime for the Financial Agent System."""

__all__ = ["build_graph", "run_financial_agent", "classify_request"]


def __getattr__(name: str):
    if name in {"build_graph", "run_financial_agent"}:
        from .financial_agent_graph import build_graph, run_financial_agent
        return {"build_graph": build_graph, "run_financial_agent": run_financial_agent}[name]
    if name == "classify_request":
        from .routing import classify_request
        return classify_request
    raise AttributeError(name)
