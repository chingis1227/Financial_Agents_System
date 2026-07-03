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

## Run through Python LangGraph runtime

The additive Python LangGraph runtime lives in `langgraph_runtime/`. It preserves the existing route cards, skills, evidence gates, validation rules, and report boundaries while providing a live/dry-run graph entrypoint. It does not delete or replace the Codex-native layer, and it is not an OpenAI Agents SDK runtime.

Dry-run mode never calls the OpenAI API and can be used for routing, gate, report, and audit validation:

```powershell
py -3 -m langgraph_runtime.financial_agent_graph run --prompt "????????????? Microsoft ?? 3 ????, ??????? ???" --dry-run
```

Live mode requires `OPENAI_API_KEY` from the environment or `.env` and uses configurable model settings from `.env.example`:

```powershell
py -3 -m langgraph_runtime.financial_agent_graph run --prompt "AGENT: Microsoft for 3 years, no current position" --live
py -3 -m langgraph_runtime.financial_agent_graph chat
```

Configurable settings:

- `OPENAI_API_KEY`
- `OPENAI_MODEL` (default: `gpt-5.3-codex`)
- `OPENAI_REASONING_EFFORT` (default: `low`)

Current LangGraph MVP routes natural-language and prefix prompts through `intake_router_node`, supports equity full-cycle dry-run artifacts, direct specialist and Quick Take boundaries, missing-context interrupts, evidence-readiness gate failure handling, and idempotent `investment_report.md` plus `audit/` artifact writing.

## Run through Codex SDK

The optional Codex SDK v1 control layer starts Codex from a small TypeScript CLI while preserving the existing Codex-native runtime rules. It is a control-plane wrapper only: `AGENT:`, `QUICK:`, route cards, skills, custom agents, report packaging, and audit behavior remain owned by the existing project instructions.

Use `npm.cmd` on Windows because PowerShell may block `npm.ps1`; do not change the system execution policy for this project.

```powershell
npm.cmd install
npm.cmd run build
npm.cmd test
npm.cmd run codex:doctor
npm.cmd run codex:run -- --prompt "AGENT: Microsoft for 3 years, no current position" --dry-run
npm.cmd run codex:run -- --prompt-file ".\prompt.txt" --live
npm.cmd run codex:run -- --prompt "QUICK: Microsoft" --live
npm.cmd run codex:resume -- --thread-id "<id>" --prompt "continue" --live
```

Default SDK mode is `--dry-run`; live Codex execution requires explicit `--live`. Dry-runs print to stdout only and do not create run-log files. Live SDK service logs are written outside the repository under `C:\Users\ShumeikoYe\OneDrive\Documents\Financial Agent Reports\_sdk_runs\`.
Use `--prompt-file` for Automation Lab or other long prompts so Windows command-line limits and prompt leakage in process arguments are avoided.

## Integrated Automation Lab live acceptance

`automation_lab/` is the integrated execution/orchestration layer inside this repository. It does not replace this repository's route cards, skills, evidence policy, or IC gates; those remain owned by the Financial Agent System canonical docs and route cards.

As of 2026-07-03, Automation Lab has passed `live-acceptance --require-live` for the supported runtime matrix:

- QUICK live/public validation;
- full AGENT live packages for equity, ETF/fund, fixed income, crypto, commodity, and multi-asset comparison;
- direct specialist prefixes: RISK, VAL, MACRO, NEWS, PORTFOLIO, SECTOR, EVIDENCE, POSITIONING, INTEL, EQUITY, ETF, COMMODITY, CRYPTO, FI, WINNERS, and IC.

Run it from the unified repository:

```powershell
cd "C:\Users\ShumeikoYe\OneDrive\Documents\Financial Agent System\automation_lab"
..\.venv\Scripts\python.exe -m unittest discover -s tests -p "test_*.py"
..\.venv\Scripts\python.exe fa_automation.py live-doctor
..\.venv\Scripts\python.exe fa_automation.py live-acceptance --require-live
```

Reports and audit packages are saved outside the repository under `C:\Users\ShumeikoYe\OneDrive\Documents\Financial Agent Reports\`. Local Lab run caches under `automation_lab/runs/` and `automation_lab/data_runs/` are ignored by Git.

## Current runtime files

| Path | Purpose |
|---|---|
| `PROJECT_STATE.md` | Short current-state entrypoint. |
| `AGENTS.md` | Compact Codex runtime instructions. |
| `workflows/route_cards/` | Daily route selection and workflow contracts. |
| `.agents/skills/investment-workflow-router/` | First skill for command shortcut, investment-action, and comparison prompts. |
| `automation_lab/` | Integrated execution/orchestration Lab for QUICK, AGENT, specialist, live-doctor, and live-acceptance runs; generated artifacts are ignored or saved outside the repo. |
| `implementation/` | Canonical reference layer and supporting operational records. |
| `references/` | Advisory playbooks and source overlays. |
| `archive/project-history/` | Historical task and backlog records. |
| `archive/legacy-prd/` | Retired PRDs and provenance-only material. |

## Validation

Run these after changing docs, route cards, agents, skills, workflow behavior, tests, or validators:

```powershell
py -3 tools\validate_project_consistency.py
py -3 tools\validate_language_style.py
py -3 tools\validate_behavior_contracts.py
py -3 tools\validate_runtime_readiness.py
cd automation_lab
..\.venv\Scripts\python.exe -m unittest discover -s tests -p "test_*.py"
cd ..
```

After changing the Codex SDK control layer, also run:

```powershell
npm.cmd run build
npm.cmd test
npm.cmd run codex:doctor
npm.cmd run codex:run -- --prompt "QUICK: Microsoft" --dry-run
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

This project follows OpenAI / Codex guidance by keeping `AGENTS.md` concise, turning repeated workflows into skills, using explicit validation, keeping custom agents narrow, treating subagents as real only when actually spawned, and using Codex SDK only as a control plane. It does not implement an OpenAI Agents SDK runtime.
