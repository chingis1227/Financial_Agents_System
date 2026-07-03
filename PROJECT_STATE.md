# Project State

Status: Current runtime state
Last updated: 2026-07-02

## Purpose

This file is the short current-state entrypoint for Codex runtime work in the Financial Agent System. Historical task logs and audit reports do not override this file or the canonical implementation documents.

## Current operating model

- Runtime style: Codex-native first, with an additive Python `langgraph_runtime/` layer for LangGraph dry-run/live execution. The new layer uses the OpenAI API in explicit live mode only; it is not an OpenAI Agents SDK runtime.
- Codex SDK v1 control layer present: TypeScript CLI wrapper for dry-run/live Codex thread execution, with live SDK logs outside the repository.
- Python LangGraph runtime present: `langgraph_runtime/financial_agent_graph.py` exposes `run` and `chat`; dry-run mode is deterministic, and live mode requires `OPENAI_API_KEY`.
- Daily runtime path: `PROJECT_STATE.md` -> `AGENTS.md` -> `workflows/route_cards/investment_request_router.md` -> selected route card -> validators.
- User-facing command model: `AGENT:` for the large agent workflow, `QUICK:` for a short preliminary answer, and specialist prefixes for one analyst.
- Ordinary investment-action prompts without a prefix still route through the router, but recommended UX is `AGENT:` or `QUICK:`.
- `AGENT:` asks exactly 5 relevant questions first, then uses relevant spawned subagents when available. Do not claim an agent workflow unless subagents were actually spawned.
- If subagents cannot be spawned after `AGENT:`, record the fallback only in audit metadata and mark the user-facing output Limited; do not advertise the fallback as a selectable user mode.
- `QUICK:` is chat-only, asks exactly 3 relevant questions first, and must not create `investment_report.md` or an `audit` folder.
- Final IC Actions remain owned by Investment Committee synthesis only; specialist outputs are scoped handoffs and must not use final buy/sell/hold/add/trim/exit labels.

## Command shortcuts

| Command | Runtime meaning | Target |
|---|---|---|
| `AGENT:` | Large agent workflow with relevant spawned subagents | Router-selected asset workflow + IC synthesis |
| `QUICK:` | Short preliminary answer | Quick Take route |
| `RISK:` | One specialist only | `risk-red-team-agent` |
| `VAL:` | One specialist only | `valuation-expectations-agent` |
| `MACRO:` | One specialist only | `macro-agent` |
| `NEWS:` | One specialist only | `news-catalysts-agent` |
| `PORTFOLIO:` | One specialist only | `portfolio-fit-agent` |
| `SECTOR:` | One specialist only | `sector-industry-analysis-agent` |
| `EVIDENCE:` | One specialist only | `evidence-collector` |
| `POSITIONING:` | One specialist only | `market-positioning-agent` |
| `INTEL:` | One specialist only | `market-intelligence-agent` |
| `EQUITY:` | One specialist only | `equity-agent` |
| `ETF:` | One specialist only | `etf-agent` |
| `COMMODITY:` | One specialist only | `commodity-agent` |
| `CRYPTO:` | One specialist only | `crypto-agent` |
| `FI:` | One specialist only | `fixed-income-agent` |
| `WINNERS:` | One specialist only | `structural-winners-discovery-agent` |
| `IC:` | One specialist only; committee-prep handoff, not final action | `investment-committee-agent` |

## Current ready routes

| Route | Current status | Runtime entrypoint |
|---|---|---|
| `QUICK:` | Ready for preliminary chat-only use | `workflows/route_cards/quick_take.md` |
| `AGENT:` equity workflow | Ready for regular use | `workflows/route_cards/equity_full_cycle.md` |
| `AGENT:` ETF / fund workflow | Ready; Level 2 hardening complete | `workflows/route_cards/etf_full_cycle.md` |
| `AGENT:` commodity workflow | Ready; Level 2 hardening complete | `workflows/route_cards/commodity_full_cycle.md` |
| `AGENT:` crypto workflow | Ready; Level 2 hardening complete | `workflows/route_cards/crypto_full_cycle.md` |
| `AGENT:` fixed-income workflow | Ready; Level 2 hardening complete | `workflows/route_cards/fixed_income_full_cycle.md` |
| `AGENT:` multi-asset comparison | Ready; Level 2 hardening complete | `workflows/route_cards/multi_asset_comparison.md` |
| Specialist command | Ready with analyst boundary | `workflows/route_cards/direct_specialist.md` |

| Python LangGraph runtime | Available for dry-run routing, equity full-cycle artifacts, direct specialist/Quick Take boundaries, missing-context interrupts, evidence-gate blocking, and live OpenAI API adapter gated on `OPENAI_API_KEY` | `langgraph_runtime/financial_agent_graph.py` |

## External Automation Lab live acceptance

Financial Agent Automation Lab is the execution/orchestration layer, not the canonical investment-rule source. As of 2026-07-03, its supported live acceptance matrix has passed with real Codex SDK `sdk_thread_id` evidence for:

- QUICK live/public validation;
- full AGENT live packages for equity, ETF/fund, fixed income, crypto, commodity, and multi-asset comparison;
- all direct specialist prefixes: RISK, VAL, MACRO, NEWS, PORTFOLIO, SECTOR, EVIDENCE, POSITIONING, INTEL, EQUITY, ETF, COMMODITY, CRYPTO, FI, WINNERS, and IC.

Latest Automation Lab acceptance status: `live-acceptance --require-live` passes with no smoke gaps, no live gaps, and no usage-limit gaps. Detailed execution artifacts remain outside this repository under `C:\Users\ShumeikoYe\OneDrive\Documents\Financial Agent Reports\`.

## Active documents

- Runtime navigator: `AGENTS.md`.
- User guide: `README.md`.
- Current-state summary: `PROJECT_STATE.md`.
- Documentation registry: `implementation/01-documentation-control.md`.
- Master gates/statuses: `implementation/00-master-rules.md`.
- Evidence rules: `implementation/04-evidence-layer.md`.
- Routing and workflows: `implementation/05-routing-and-workflows.md`.
- IC and report schemas: `implementation/07-investment-committee-and-report-schemas.md`.
- Runtime architecture: `implementation/13-codex-runtime-architecture.md`.
- Language/style: `implementation/14-language-and-style.md`.
- Documentation sync: `implementation/15-documentation-sync-contract.md`.
- Runtime route cards: `workflows/route_cards/`.

## Historical or superseded records

- `archive/project-history/TASKS.md` is a historical implementation task log.
- `archive/project-history/IMPLEMENTATION_BACKLOG.md` is a historical implementation roadmap.
- `implementation/final-system-audit-report.md`, `implementation/p10-qa-execution-report.md`, `.codex/runtime-readiness-report.md`, and `implementation/runtime-baseline-report.md` are supporting validation records. They do not override this current state or canonical implementation documents.
- `implementation/non_equity_production_hardening_report.md` is the current non-equity hardening evidence record for ETF, commodity, crypto, fixed income, and multi-asset routes.

## Current limitations

- No OpenAI Agents SDK orchestrator is implemented; Codex SDK is only a control-plane wrapper around Codex, while `langgraph_runtime/` is an additive LangGraph/OpenAI API runtime.
- No persistent external market-data pipeline or real-time monitor is guaranteed unless a specific automation is configured.
- Portfolio Fit remains Limited / not personalized when the user does not provide portfolio context.
- Freshness-dependent claims require current sources with timestamps; otherwise the output must be Limited or Blocked.

## Required validation after project changes

Run these checks after changing docs, route cards, agents, skills, validators, or workflow behavior:

```powershell
py -3 tools\validate_project_consistency.py
py -3 tools\validate_behavior_contracts.py
py -3 tools\validate_runtime_readiness.py
py -3 -m unittest discover -s tests\langgraph_runtime -v
```

After changing the Codex SDK control layer, also run:

```powershell
npm.cmd run build
npm.cmd test
npm.cmd run codex:doctor
npm.cmd run codex:run -- --prompt "QUICK: Microsoft" --dry-run
```
