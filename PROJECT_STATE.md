# Project State

Status: Current runtime state
Last updated: 2026-06-30

## Purpose

This file is the short current-state entrypoint for Codex runtime work in the Financial Agent System. It is intentionally compact. Historical task logs and audit reports do not override this file or the canonical implementation documents.

## Current operating model

- Runtime style: Codex-native first; no OpenAI API / Agents SDK orchestrator is required for the current version.
- Daily runtime path: `PROJECT_STATE.md` -> `AGENTS.md` -> `workflows/route_cards/investment_request_router.md` -> selected route card -> validators.
- Concrete-asset investment-action requests default to Full Cycle unless the user explicitly asks for a short / fast / quick / preliminary answer.
- Quick Take is chat-only, asks exactly 3 relevant questions first, and must not create `investment_report.md` or an `audit` folder.
- Full Cycle asks exactly 5 relevant questions first, then writes `investment_report.md` plus `audit/` when the workflow runs.
- Subagents are counted as used only when they are actually spawned; in validator terms, subagents were actually spawned. If no subagents are spawned, audit metadata must use `Single-agent Full Cycle`, not `Delegated Full Agent Workflow`; do not claim delegated execution without a real spawn record.
- Final IC Actions remain owned by Investment Committee synthesis only; specialist outputs are scoped handoffs and must not use final buy/sell/hold/add/trim/exit labels.

## Current ready routes

| Route | Current status | Runtime entrypoint |
|---|---|---|
| Quick Take | Ready for preliminary chat-only use | `workflows/route_cards/quick_take.md` |
| Equity Full Cycle | Ready for regular use | `workflows/route_cards/equity_full_cycle.md` |
| ETF / fund Full Cycle | Ready after non-equity Level 2 hardening | `workflows/route_cards/etf_full_cycle.md` |
| Commodity Full Cycle | Ready after non-equity Level 2 hardening | `workflows/route_cards/commodity_full_cycle.md` |
| Crypto Full Cycle | Ready after non-equity Level 2 hardening | `workflows/route_cards/crypto_full_cycle.md` |
| Fixed Income Full Cycle | Ready after non-equity Level 2 hardening | `workflows/route_cards/fixed_income_full_cycle.md` |
| Multi-asset comparison | Ready after non-equity Level 2 hardening | `workflows/route_cards/multi_asset_comparison.md` |
| Direct specialist request | Ready with IC boundary | `workflows/route_cards/direct_specialist.md` |

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

- No fully automated OpenAI Agents SDK orchestrator is implemented in this phase.
- No persistent external market-data pipeline or real-time monitor is guaranteed unless a specific automation is configured.
- Portfolio Fit remains Limited / not personalized when the user does not provide portfolio context.
- Freshness-dependent claims require current sources with timestamps; otherwise the output must be Limited or Blocked.

## Required validation after project changes

Run these checks after changing docs, route cards, agents, skills, validators, or workflow behavior:

```powershell
py -3 tools\validate_project_consistency.py
py -3 tools\validate_behavior_contracts.py
py -3 tools\validate_runtime_readiness.py
```
