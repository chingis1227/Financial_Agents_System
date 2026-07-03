# Project State

Status: Current runtime state
Last updated: 2026-07-03

## Purpose

This file is the short current-state entrypoint for Codex runtime work in the Financial Agent System. Historical task logs and audit reports do not override this file or the canonical implementation documents.

## Current operating model

- Runtime style: Codex-native first, with an additive Python `langgraph_runtime/` layer for LangGraph live/live execution. The new layer uses the OpenAI API in explicit live mode only; it is not an OpenAI Agents SDK runtime.
- Codex SDK v1 control layer present: TypeScript CLI wrapper for live/live Codex thread execution, with live SDK logs outside the repository.
- Python LangGraph runtime present: `langgraph_runtime/financial_agent_graph.py` exposes `run` and `chat`; live mode is the production path and requires `OPENAI_API_KEY`; live/historical fixture behavior is retained only for historical test fixtures and is not an operator workflow.
- Daily runtime path: `PROJECT_STATE.md` -> `AGENTS.md` -> `workflows/route_cards/investment_request_router.md` -> selected route card -> validators.
- User-facing command model: `AGENT:` for the large agent workflow, `QUICK:` for a short preliminary answer, and specialist prefixes for one analyst.
- Ordinary investment-action prompts without a prefix are mandatory auto-dispatch inputs: buy/sell/hold/add/trim/exit, asset comparisons, and asset analysis for a stated horizon first route through the router. `AGENT:` remains a shortcut/override, not a prerequisite for the large workflow; explicit short/quick/preliminary wording still routes to `QUICK:`.
- Automation Lab also exposes a thin auto-dispatch entrypoint, `automation_lab/fa_automation.py dispatch --prompt "<user request>"`, which classifies prefixed and ordinary requests and then calls the existing QUICK, AGENT, or direct-specialist flow. It does not redefine canonical investment rules.
- Fabrinet identity is recognized as public equity `FN` for `Fabrinet`, `Fabrynet`, `Fabryns`, and `FN`; numeric horizons such as `3-5` are horizon ranges and must not be resolved as ticker symbols.
- Evidence Document Parser Layer is available as MVP local parser infrastructure under `automation_lab/agent_data/`: it converts accessible HTML/PDF/raw-text documents into claim-level evidence records for Evidence Pack support. It is not MCP, not an OpenAI Agents SDK runtime, and not a specialist agent.
- Production Data Provider & Parsing Layer is available under `automation_lab/data_providers/` and `automation_lab/data_parsers/`: it provides a unified ProviderResult contract, route-aware provider registry, raw/normalized cache, freshness/source-tier helpers, official/market provider adapters, and provider-derived Evidence Pack claim inputs. It is data/evidence infrastructure only and does not redefine investment rules.
- `AGENT:` asks exactly 5 relevant questions first, then automatically spawns all route-relevant subagents without requiring the user to ask for agents, delegation, or parallel work. Do not claim an agent workflow unless subagents were actually spawned.
- If subagent spawning is technically unavailable, the run is Blocked for production live workflow; do not replace it with historical fixture or non-delegated analysis.
- `QUICK:` is chat-only, asks exactly 3 relevant questions first, and must not create `investment_report.md` or an `audit` folder.
- Final IC Actions remain owned by Investment Committee synthesis only; specialist outputs are scoped handoffs and must not use final buy/sell/hold/add/trim/exit labels.
- Parsed document evidence is supporting audit/evidence material only; it never produces an `IC Action` or investment recommendation by itself.

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
| `SENSE:` | One specialist only | `market-sense-agent` |
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
| Automation Lab auto-dispatch | Ready as a thin CLI router over existing QUICK / AGENT / specialist flows | `automation_lab/fa_automation.py dispatch --prompt "<user request>"` |

| Python LangGraph runtime | Available for live routing, equity full-cycle artifacts, direct specialist/Quick Take boundaries, missing-context interrupts, evidence-gate blocking, and live OpenAI API adapter gated on `OPENAI_API_KEY` | `langgraph_runtime/financial_agent_graph.py` |
| Evidence Document Parser Layer | MVP available; parses accessible HTML/PDF/raw text into normalized claim evidence and merges parsed claims into Evidence Pack rows for equity preflight first | `automation_lab/agent_data/document_parser.py` |
| Data Provider & Parsing Layer | Available; ProviderResult registry/cache/parsers feed preflight snapshots and Evidence Pack inputs across equity, ETF, fixed income, macro, commodity/grain, crypto, and multi-asset workflows with graceful degradation for missing keys | `automation_lab/data_providers/` |

## Integrated Automation Lab live acceptance

The integrated `automation_lab/` directory is the execution/orchestration layer inside this repository, not the canonical investment-rule source. The former separate local folder was merged into the main repository layout so there is one GitHub source of truth. As of 2026-07-03, its supported live acceptance matrix has passed with real Codex SDK `sdk_thread_id` evidence for:

- QUICK live/public validation;
- full AGENT live packages for equity, ETF/fund, fixed income, crypto, commodity, and multi-asset comparison;
- all direct specialist prefixes: RISK, VAL, MACRO, NEWS, PORTFOLIO, SECTOR, EVIDENCE, POSITIONING, INTEL, EQUITY, ETF, COMMODITY, CRYPTO, FI, WINNERS, and IC.

Latest Automation Lab acceptance status: `live-acceptance --require-live` passes with no smoke gaps, no live gaps, and no usage-limit gaps. The Lab code now lives under `automation_lab/`; generated execution artifacts remain outside the repository under `C:\Users\ShumeikoYe\OneDrive\Documents\Financial Agent Reports\` or in ignored local `automation_lab/runs/` and `automation_lab/data_runs/` folders.

## Active documents

- Runtime navigator: `AGENTS.md`.
- User guide: `README.md`.
- Current-state summary: `PROJECT_STATE.md`.
- Documentation registry: `implementation/01-documentation-control.md`.
- Master gates/statuses: `implementation/00-master-rules.md`.
- Evidence rules: `implementation/04-evidence-layer.md`.
- Document evidence parsing skill: `.agents/skills/evidence-document-parser/SKILL.md`.
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
- No persistent real-time monitor is guaranteed unless a specific automation is configured; the provider layer is on-demand and cache-backed.
- Evidence Document Parser Layer is MVP-grade deterministic local infrastructure. HTML uses Python standard library parsing; PDF extraction requires `automation_lab/requirements-parser.txt` (`pypdf`) and image-only/scanned PDFs remain `Unsupported` or `Partial`.
- Optional providers requiring `FRED_API_KEY`, `USDA_NASS_API_KEY`, `PERPLEXITY_API_KEY`, or `EODHD_API_KEY` degrade to disabled/partial when keys are missing; official/no-key providers and public price fallbacks are still attempted where routed.
- When the user does not provide portfolio context, audit records Portfolio Fit as Limited / not personalized and General Portfolio Role Mode; reader-facing `investment_report.md` presents this as a general Portfolio role section rather than failure wording.
- Freshness-dependent claims require current sources with timestamps; otherwise the output must be Limited or Blocked.

## Required validation after project changes

Run these checks after changing docs, route cards, agents, skills, validators, or workflow behavior:

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
npm.cmd run codex:run -- --prompt "QUICK: Microsoft" --live
```

## Reader-facing memo policy

As of 2026-07-03, large-workflow `investment_report.md` output is a clean professional investment memo. Internal statuses, gates, source tiers, provider/access failures, handoff metadata, and module-status language remain in `audit/` and validators, while the reader-facing memo describes constraints as investment uncertainty, scenario sensitivity, current-data dependence, or a conclusion that is not justified now.

## Institutional workflow logic

- `SENSE:` is a direct specialist shortcut to `market-sense-agent`.
- Materiality Gate means optional market modules run only when decision-relevant or explicitly requested; ?run all agents? means all relevant agents.
- Large workflows maintain a Thesis Spine and separate Asset / Business Quality from Entry Setup.
- Structural Winners is discovery-only and returns candidate watchlists / review priority, not buy lists.
- Saved reports now include Quality vs Entry, Key Internal Conflicts, What Would Change Our Mind, and Monitoring Triggers; audit records decision mode, materiality plan, skipped optional agents, thesis spine evolution, and portfolio fit level.


## Current live-only operating override

As of 2026-07-03, user-requested investment workflows are live-only. Historical fixture paths may remain only as archived provenance or test names; they are not valid production analysis paths. Concrete-asset investment prompts automatically spawn all route-relevant subagents after intake without requiring explicit user delegation wording. Russian investment reports must pass the language-policy layer; all investment memos/reports must pass investment-analytical-style before being saved or shown. Live workflow execution must not use fixed 300/600/900/1200/7200-second timeouts; it runs until the required agents finish or a true external failure blocks execution.

Production audit metadata records spawned agents, handoffs, source state, presentation-skill validation, and any Blocked production issue.
