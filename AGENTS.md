# Financial Agent System - Codex Instructions

## Purpose

This repo defines a Codex-native financial analysis runtime. The integrated `automation_lab/` directory is the execution/orchestration layer and must not redefine canonical investment rules. Codex should use the short current-state and route-card layer first, then consult canonical implementation documents only when the selected task needs deeper rules.

This project follows official OpenAI / Codex best practices: keep `AGENTS.md` practical and concise, make repeated workflows into skills, use explicit validation, and never claim subagents ran unless they were actually spawned.

## Start here

1. Confirm the project root contains `AGENTS.md`, `PROJECT_STATE.md`, `implementation/`, and `workflows/`.
2. Read `PROJECT_STATE.md` for current operating state.
3. For investment requests, read `workflows/route_cards/investment_request_router.md` before answering.
4. For source authority or conflicts, use `implementation/01-documentation-control.md` and `implementation/00-master-rules.md`.
5. For documentation/runtime changes, use `implementation/15-documentation-sync-contract.md` and run validators.
6. For Codex SDK control-layer changes, also run the Node checks listed under Required validation after changes.
7. For Python LangGraph runtime changes, keep `langgraph_runtime/` additive, preserve route-card boundaries, and run the LangGraph runtime unittest suite.

## Active authority order

1. `implementation/00-master-rules.md` for statuses, gates, output standards, confidence, source display, style, and artifact naming.
2. `implementation/01-documentation-control.md` for registry, source precedence, archive behavior, and source issues.
3. `PROJECT_STATE.md` for current runtime state and historical/superseded document handling.
4. `workflows/route_cards/` for daily runtime route selection.
5. Specific canonical implementation documents for their domains.
6. Supporting references under `references/` only when routed by registry/traceability and non-conflicting.
7. Archive material only as provenance; never as active source of truth.

## User command model

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
| `SENSE:` | One specialist only | `market-sense-agent` |
| `INTEL:` | One specialist only | `market-intelligence-agent` |
| `EQUITY:` | One specialist only | `equity-agent` |
| `ETF:` | One specialist only | `etf-agent` |
| `COMMODITY:` | One specialist only | `commodity-agent` |
| `CRYPTO:` | One specialist only | `crypto-agent` |
| `FI:` | One specialist only | `fixed-income-agent` |
| `WINNERS:` | One specialist only | `structural-winners-discovery-agent` |
| `IC:` | One specialist only; committee-prep handoff, not final action | `investment-committee-agent` |

## Non-negotiable runtime rules

- Do not use archive files as active source of truth.
- Any ordinary user request about an investment decision, buy/sell/hold/add/trim/exit, asset comparison, or asset analysis for a stated horizon must enter auto-dispatch first; do not answer with chat-only analysis in bypass of the router.
- `AGENT:` is the user-facing command for the large agent workflow. It asks exactly 5 relevant questions first, then uses relevant spawned subagents when available.
- Do not claim an agent workflow unless subagents were actually spawned. If subagents cannot be spawned, record fallback only in audit metadata and mark the user-facing output Limited.
- `QUICK:` is only Preliminary or Limited, asks exactly 3 relevant questions first, stays chat-only, and never creates report/audit files.
- Specialist commands, including `IC:`, route to one analyst only, must show `Boundary: Not an IC Action`, and must not issue final `IC Action`.
- Do not issue final `IC Action` outside Investment Committee synthesis.
- Freshness-dependent requests such as today, now, latest, earnings, price action, or news require current timestamped sources or must be Limited / Blocked.
- Large workflow reports are saved outside the repo under `C:\Users\ShumeikoYe\OneDrive\Documents\Financial Agent Reports\[ASSET] yyyy-mm-dd hhmm\` as `investment_report.md` plus `audit/`.
- The Codex SDK TypeScript layer is a control-plane wrapper only. It must not duplicate financial workflow rules, replace route cards, or claim OpenAI Agents SDK runtime behavior.
- Ordinary chat after a saved workflow should show the reader-facing report and saved-report path, not runtime/debug tables, unless explicitly requested.

## Runtime route map

| User intent | Required route |
|---|---|
| `QUICK:` or explicit short / quick / fast / preliminary | `workflows/route_cards/quick_take.md` |
| `AGENT:` with a concrete asset or comparison | `workflows/route_cards/investment_request_router.md` -> selected asset/comparison route card |
| buy / invest / hold / sell / add / analyze concrete asset without prefix | auto-dispatch through router; `AGENT:` is a shortcut, not a prerequisite |
| Fabrinet / Fabrynet / Fabryns / FN with investment horizon | equity full-cycle workflow (`FN`); do not treat `3-5` as a ticker |
| specialist command | `workflows/route_cards/direct_specialist.md`; one analyst only; no final IC Action |
| docs/runtime maintenance | `implementation/15-documentation-sync-contract.md` |

## Skills and agents

- Use `.agents/skills/investment-workflow-router/` first for investment-action, comparison, command shortcut, or portfolio-decision prompts.
- Custom agents in `.codex/agents/` are thin profiles for spawned sessions, not always-on workers.
- Skills own reusable method steps; agents own role, boundary, status, and handoff.
- Direct specialist skills and agents must not use `Action Box` or final buy/sell/hold/add/trim/exit language. Final IC action is available only through the gated large workflow, not the `IC:` shortcut.

## Required validation after changes

After changing project docs, route cards, agents, skills, workflow behavior, tests, or validators, run:

```powershell
py -3 tools\validate_project_consistency.py
py -3 tools\validate_language_style.py
py -3 tools\validate_behavior_contracts.py
py -3 tools\validate_runtime_readiness.py
py -3 -m unittest discover -s tests\langgraph_runtime -v
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

Do not mark work complete if validation fails. Fix the inconsistency or report it as a source issue.

## Language

Internal project Markdown is English unless explicitly requested otherwise. User-facing chat answers and generated report content follow the user's language. Russian user-facing output must be natural Russian and preserve tickers, file paths, URLs, and controlled technical labels where needed.

## Institutional workflow logic

- `SENSE:` maps to `market-sense-agent` as a direct specialist.
- Materiality Gate controls optional market modules: include only if material or explicitly requested, otherwise record skip reason.
- "Run all agents" means all relevant agents for the decision mode, not literally every profile.
- Structural Winners is discovery-only.
- Large saved reports include Quality vs Entry, Key Internal Conflicts, What Would Change Our Mind, and Monitoring Triggers.
