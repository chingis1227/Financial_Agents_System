# Financial Agent System

The Financial Agent System is a Codex-native, agents-first financial analysis project. It uses concise runtime route cards, reusable skills, canonical implementation documents, and validator-backed behavior tests to make investment workflows more repeatable.

The current state is summarized in `PROJECT_STATE.md`. Historical build trackers are archived under `archive/project-history/` and do not control daily runtime behavior.

## How to use it

Start Codex from the project root. For investment requests, Codex should route through `workflows/route_cards/investment_request_router.md` before answering.

| Mode | Use when | What happens | Boundary |
|---|---|---|---|
| `Quick Take` | You explicitly ask for short, quick, fast, or preliminary output. | Codex asks exactly 3 relevant questions, then gives a chat-only Preliminary / Limited view. | No saved report, no audit, no final IC Action. |
| `Full Cycle` | You ask whether to buy, invest, hold, sell, add, or evaluate a concrete asset for a capital decision. | Codex asks exactly 5 relevant questions, then runs the selected Full Cycle route card. | Gate-aware report. Missing portfolio context keeps Portfolio Fit / IC Action limited. |
| `Delegated Full Agent Workflow` | A Full Cycle route uses relevant subagents and they actually ran, either through Codex spawning or a real orchestrator. | Codex records the agents actually spawned and consumes structured handoffs. If no subagents actually ran, use `Single-agent Full Cycle`. | Do not claim delegation unless subagents actually ran. |

## Prompt examples

```text
Quick Take: дай быстрый предварительный взгляд на Microsoft.
```

```text
Full Cycle: стоит ли инвестировать в Microsoft на горизонт 3+ лет?
```

```text
Полный многоагентный запуск: QQQ vs SCHG. Без финального buy/sell/hold, если IC gates не закрыты.
```

```text
Почему Nvidia выросла сегодня? Используй свежие источники с timestamp или пометь вывод Limited / Blocked.
```

Additional routing examples to keep behavior explicit:

```text
Дай быстрый предварительный вывод по BTC.
```

```text
Нужен полный анализ в одной сессии по TLT.
```

```text
Сделай мемо для подготовки решения по золоту; если свежих источников нет, пометь результат Limited.
```

```text
Проверь маршрутизацию для BTC, золото, QQQ и TLT.
```

## Current runtime files

| Path | Purpose |
|---|---|
| `PROJECT_STATE.md` | Short current-state entrypoint. |
| `AGENTS.md` | Compact Codex runtime instructions. |
| `workflows/route_cards/` | Daily route selection and workflow contracts. |
| `.agents/skills/investment-workflow-router/` | First skill for investment-action and comparison prompts. |
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
