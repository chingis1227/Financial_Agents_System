# Financial Agent System

The Financial Agent System is a Codex-native, agents-first financial analysis project. It uses concise runtime route cards, reusable skills, canonical implementation documents, and validator-backed behavior tests to make investment workflows more repeatable.

The current state is summarized in `PROJECT_STATE.md`. Historical build trackers are archived under `archive/project-history/` and do not control daily runtime behavior.

## How to use it

Start Codex from the project root. For investment requests, Codex should route through `workflows/route_cards/investment_request_router.md` before answering.

| Command | Use when | What happens | Boundary |
|---|---|---|---|
| `AGENT:` | You want the large agent workflow for an asset, comparison, or capital-allocation decision. | Codex asks exactly 5 relevant questions, then uses relevant spawned subagents when available and saves report/audit artifacts. | Do not claim an agent workflow unless subagents actually ran; if they cannot run, fallback is audit-only and the user-facing output is Limited. |
| `QUICK:` | You want a short preliminary answer. | Codex asks exactly 3 relevant questions, then gives a chat-only Preliminary / Limited view. | No saved report, no audit, no final IC Action. |
| Specialist command | You want one analyst only, such as risk, valuation, macro, news, portfolio fit, or committee-prep review. | Codex routes to one specialist agent/method and keeps the output scoped. | Boundary: Not an IC Action, including `IC:`. |

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

## Prompt examples

```text
AGENT: Microsoft for 3 years, no current position
```

```text
QUICK: Microsoft
```

```text
RISK: Microsoft
```

```text
VAL: Nvidia
```

```text
NEWS: why did Nvidia rise today?
```

```text
ETF: QQQ vs SCHG
```

## Current runtime files

| Path | Purpose |
|---|---|
| `PROJECT_STATE.md` | Short current-state entrypoint. |
| `AGENTS.md` | Compact Codex runtime instructions. |
| `workflows/route_cards/` | Daily route selection and workflow contracts. |
| `.agents/skills/investment-workflow-router/` | First skill for command shortcut, investment-action, and comparison prompts. |
| `implementation/` | Canonical reference layer and supporting operational records. |
| `references/` | Advisory playbooks and source overlays. |
| `archive/project-history/` | Historical task and backlog records. |
| `archive/legacy-prd/` | Retired PRDs and provenance-only material. |

## Validation

Run these after changing docs, route cards, agents, skills, workflow behavior, tests, or validators:

```powershell
py -3 tools\validate_project_consistency.py
py -3 tools\validate_behavior_contracts.py
py -3 tools\validate_runtime_readiness.py
```

Validation is the TDD-like gate for this documentation-driven system: behavior rules must have fixtures, fixtures must be checked by validators, and project state must stay synchronized with the registry.

## Source-of-truth model

- Canonical statuses, gates, and report rules live in `implementation/00-master-rules.md`.
- Registry and source precedence live in `implementation/01-documentation-control.md`.
- Current runtime state lives in `PROJECT_STATE.md`.
- Daily investment routing lives in `workflows/route_cards/`.
- Documentation synchronization rules live in `implementation/15-documentation-sync-contract.md`.
- Historical reports and archived PRDs do not override current state or canonical implementation documents.

## OpenAI / Codex best-practice alignment

This project follows OpenAI / Codex guidance by keeping `AGENTS.md` concise, turning repeated workflows into skills, using explicit validation, keeping custom agents narrow, and treating subagents as real only when actually spawned. A future API-backed version may use OpenAI Agents SDK orchestration with a manager agent, handoffs or agents-as-tools, guardrails, and traces.
