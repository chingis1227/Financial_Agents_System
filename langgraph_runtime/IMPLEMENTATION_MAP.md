# LangGraph Runtime Implementation Map

Status: Active implementation plan for the additive LangGraph runtime layer.

## Purpose

Add `langgraph_runtime/` as a Python LangGraph runtime that can execute the existing Financial Agent System workflow contracts without deleting or replacing the Codex-native route cards, skills, custom agents, validators, or Codex SDK control layer.

## Source mapping

| Existing source | LangGraph runtime role |
|---|---|
| `workflows/route_cards/investment_request_router.md` | `intake_router_node` routing policy and prefix mapping |
| `workflows/route_cards/equity_full_cycle.md` | full-cycle equity workflow path |
| `workflows/route_cards/quick_take.md` | quick/preliminary output constraints |
| `workflows/route_cards/direct_specialist.md` | direct specialist route and boundary |
| `.agents/skills/evidence-collection/SKILL.md` | evidence plan and evidence pack prompt/reference layer |
| `.agents/skills/equity-company-analysis/SKILL.md` | equity specialist method prompt/reference layer |
| `.agents/skills/financial-statement-analysis/SKILL.md` | financial statement specialist method prompt/reference layer |
| `.agents/skills/macro-analysis/SKILL.md` | macro specialist method prompt/reference layer |
| `.agents/skills/sector-industry-analysis/SKILL.md` | sector specialist method prompt/reference layer |
| `.agents/skills/valuation-expectations/SKILL.md` | valuation specialist method prompt/reference layer |
| `.agents/skills/risk-red-team/SKILL.md` | risk gate and red-team specialist prompt/reference layer |
| `.agents/skills/news-catalysts/SKILL.md` | news/catalyst specialist prompt/reference layer |
| `.agents/skills/market-positioning/SKILL.md` | positioning specialist prompt/reference layer |
| `.agents/skills/portfolio-fit/SKILL.md` | portfolio fit specialist prompt/reference layer, audit-only Limited / not personalized status when portfolio context is missing, and reader-facing General Portfolio Role Mode |
| `.agents/skills/investment-committee-synthesis/SKILL.md` | IC synthesis prompt/reference layer and positive-action gate |
| `implementation/00-master-rules.md` | status, gates, source and final-action governance |
| `implementation/04-evidence-layer.md` | evidence readiness gate policy |
| `implementation/07-investment-committee-and-report-schemas.md` | report/audit artifact shape |
| `implementation/14-language-and-style.md` | user-facing report language convention |

## Files to create/change

- Create `langgraph_runtime/__init__.py`.
- Create `langgraph_runtime/state.py` for typed graph state.
- Create `langgraph_runtime/config.py` for `.env` and model/runtime settings.
- Create `langgraph_runtime/openai_adapter.py` for live OpenAI API calls with no hardcoded key.
- Create `langgraph_runtime/routing.py` for deterministic dry-run routing and live structured-router fallback.
- Create `langgraph_runtime/artifacts.py` for idempotent reader-facing report and technical audit writing.
- Create `langgraph_runtime/nodes.py` for required graph nodes and dry-run MVP behavior.
- Create `langgraph_runtime/financial_agent_graph.py` for StateGraph construction, conditional edges, subgraph wiring, checkpointer, interrupts, streaming helper, and CLI.
- Create `.env.example` with `OPENAI_API_KEY`, `OPENAI_MODEL`, and `OPENAI_REASONING_EFFORT`.
- Add `tests/langgraph_runtime/test_financial_agent_graph.py` for routing, dry-run, interrupts, gates, and artifact creation.
- Update `README.md`, `PROJECT_STATE.md`, `AGENTS.md`, `implementation/13-codex-runtime-architecture.md`, and `implementation/15-documentation-sync-contract.md` to document the additive LangGraph runtime while keeping Codex-native behavior intact.

## Runtime shape

The graph uses `StateGraph(FinancialAgentState)`, conditional routing after intake and evidence readiness, an equity specialist subgraph, an in-memory checkpointer for resumable local runs, and dynamic interrupts for missing decision-critical context and failed gates. Dry-run mode is deterministic and does not call OpenAI. Live mode calls the OpenAI API only when `--live` is selected and `OPENAI_API_KEY` is present.
