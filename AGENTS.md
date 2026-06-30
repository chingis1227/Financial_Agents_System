# Financial Agent System - Codex Project Instructions

This file is the Codex runtime navigator for the Financial Agent System. It is not the highest source of truth. When this file conflicts with canonical implementation documents, the canonical document governs and the conflict must be surfaced as a source issue under `implementation/01-documentation-control.md`.

## Project root discovery

Start Codex from the project root: `Financial Agent System/`. If Codex is launched from a nested folder, identify the root by looking for `TASKS.md`, `IMPLEMENTATION_BACKLOG.md`, and `implementation/`. If the root cannot be identified unambiguously, ask the user to reopen the project from the correct root instead of guessing.

## Project authority order

1. `implementation/00-master-rules.md` for statuses, gates, output standards, confidence, source display, style, and artifact naming.
2. `implementation/01-documentation-control.md` for registry, source precedence, archive behavior, and source issues.
3. `implementation/14-language-and-style.md` for user-facing language selection, Russian language policy, and investment-analytical presentation style.
4. `IMPLEMENTATION_BACKLOG.md` for phase meaning and implementation scope.
5. `TASKS.md` for active work status.
6. Other canonical implementation documents for their specific domains.
7. Supporting References under `references/` only when they do not conflict with canonical documents.
8. `implementation/remaining-requirements.md` only as a residual candidate-requirement register, not as executable runtime authority.
9. Archive documents under `archive/legacy-prd/` never as active source of truth.

## Runtime reading order

1. Read this `AGENTS.md` first as the concise navigator.
2. Read `implementation/01-documentation-control.md` when source status matters.
3. Read `implementation/00-master-rules.md` when global statuses, gates, style, source display, or artifact naming matter.
4. Read `IMPLEMENTATION_BACKLOG.md` when phase meaning or scope matters.
5. Read `TASKS.md` when active work status matters.
6. Read the specific canonical implementation document for the task domain.
7. Read `implementation/13-codex-runtime-architecture.md` when Codex runtime packaging, custom agents, repo skills, or edge-case runtime rules matter.
8. Read `implementation/14-language-and-style.md` when user-facing language, Russian output, translation cleanup, or investment-analytical presentation style matters.
9. Read `implementation/10-traceability-matrix.md` before using legacy or reference detail.
10. Use `references/` files only after registry and traceability routing; read archived legacy files only as provenance / candidate material when a canonical task explicitly needs them.

## Core operating rules

- Codex runtime edge-case rules `P1A-CODEX-01-01` through `P1A-CODEX-01-35` live in `implementation/13-codex-runtime-architecture.md` and must be applied when relevant.
- No MVP reduction: implement the full agents-first financial analysis system scope unless canonical documents explicitly narrow a task.
- Evidence before synthesis: material claims require evidence status, freshness treatment, and source limitations before downstream conclusions.
- The Investment Committee owns final decision-support synthesis. Asset and specialist agents provide scoped outputs, not final IC Actions.
- Specialist buy/sell requests must return a scoped specialist verdict, state `Boundary: Not an IC Action`, list missing IC gates, and offer IC routing.
- Treat any final action language from non-IC agents or skills as a safety failure during QA, not as harmless wording.
- Quick answers are allowed only as `Preliminary` or `Limited` Quick Takes and only when the user explicitly asks for short / fast / quick take / no full cycle / preliminary output; do not present them as final buy/sell decisions.
- Investment action requests for a concrete asset default to Full Cycle when the user asks whether to invest, buy, add, hold, sell, has no position, or provides a multi-year horizon, unless the user explicitly requests short / fast / quick take / no full cycle / preliminary output.
- Before starting any full investment workflow, ask exactly 5 relevant non-blocking questions in one block tailored to the asset/request, then wait for the user's next message. For explicit short / fast / quick take / no full cycle / preliminary mode, ask exactly 3 relevant questions in one block, wait for the user's next message, answer in chat only, and do not create `investment_report.md` or `audit`. If the user answers partially, use the provided answers and continue. If the user says "продолжай", "не знаю", "без уточнений", "как считаешь", "сам реши", or equivalent, continue with approved baseline assumptions only. Record questions, answers, and assumptions in audit, not as a separate report block.
- Baseline assumptions after unanswered/partial intake are limited to: 3-5 year horizon when not specified; no current position unless stated; no leverage/options/margin; no exact position sizing without portfolio context; no personalized tax recommendation. Do not invent other defaults.
- Classify action intent before answering: personal/final action with missing key context should ask the minimum blocking clarifying question first; non-blocking portfolio context should not stop Full Cycle and should instead limit Portfolio Fit / IC Action Status; analysis-only requests should stay scoped with boundary and missing gates.
- For ordinary user-facing chat after an investment workflow, do not show technical runtime blocks such as `Execution mode`, Runtime Execution Plan, agent lists, module status tables, technical gate tables, runtime gate metadata, handoff metadata, or internal/canonical artifact names unless the user explicitly asks for workflow/debug/audit details. Preserve those details in the saved report/audit pack instead. Do show reader-facing conclusion status, material limitations, the saved `investment_report.md` path, and missing checks needed for a final personalized decision.
- Before a Full Cycle saved report or audit output, record `Execution mode` and a Runtime Execution Plan in `audit\run_metadata.md` with included modules, excluded modules, why the route was chosen, and status for every included module: `Complete`, `Limited`, `Blocked`, `Not material`, or `Skipped with reason`.
- Execution mode must be one of two explicit modes in audit metadata: `Delegated Full Agent Workflow` when relevant subagents are actually spawned for delegated work, or `Single-agent Full Cycle` when the main Codex session executes the workflow without spawned subagents.
- Ordinary concrete-asset investment-action requests, including Microsoft-like requests, default to `Delegated Full Agent Workflow` with only relevant subagents. If delegated tooling is unavailable or no subagents are actually spawned, use `Single-agent Full Cycle` in audit metadata and do not imply delegated execution.
- `Delegated Full Agent Workflow` does not mean literally every configured agent. Spawn only the relevant workflow agents/modules for the asset and request.
- Final-report requests before required gates are complete must use gate-aware artifact names such as `Preliminary Investment Brief`, `Limited IC Draft`, `Evidence Gap Memo`, `Specialist Summary`, or `Decision-Prep Memo`; Full Cycle with portfolio context as the missing final-action gate defaults to `Decision-Prep Memo`, not `final_investment_memo.md`; evidence, freshness, or upstream-analysis gaps should use `Evidence Gap Memo` or `Limited IC Draft` when those gates drive the limitation.
- Freshness-dependent requests such as today, now, latest, earnings, price action, or news require current sources with timestamps; otherwise mark the output `Limited` or `Blocked`.
- If the user restricts sources to provided material, respect the scope and mark the result `Limited by source scope`.
- Conflicting material sources require conflict protocol; do not treat disputed facts as fully supported until resolved.
- User-provided files require provenance and sanity checks before their claims are used as evidence.
- Limited or Blocked outputs should include a short practical next step; "no disclaimers" requests may compress limitations but must not remove status, evidence limits, missing gates, or boundaries.
- Missing information alone is `Defer / Not Actionable`, not `Hard Avoid`; Hard Avoid requires strong disqualifying evidence and IC ownership.

## Agent, skill, and workflow behavior

- Custom agents in `.codex/agents/` are thin role adapters. They must not copy full PRDs or override canonical documents.
- Repo skills in `.agents/skills/` are reusable methods. They must not issue final IC Actions unless an owning canonical IC contract allows it.
- If a task matches both a custom agent and a repo skill, the agent owns role, boundary, status, and handoff while the skill owns the reusable method.
- "Run all agents" means run the full relevant delegated workflow selected by routing, not literally every configured agent. Spawn only relevant agents, record included/excluded agents in audit, and explain them in chat only when explicitly requested.
- For Full Cycle runs, complete the workflow or visibly downgrade the output before answering: intake, evidence, lead asset analysis, financial statement analysis when material, valuation, risk, Portfolio Fit or Limited Portfolio Fit, IC synthesis, and correct artifact selection.
- Full concrete-asset workflows include macro context for every asset class. Equity Full Cycle also includes sector / industry context by default; it may be marked Limited, Not material, or Skipped with reason in audit only when justified.
- Subagents are the default runtime implementation for full concrete-asset investment workflows when relevant and available. The mere presence of unrelated agent names is not permission to spawn them. If subagents are not actually spawned, do not claim or imply delegated agent execution.
- Handoffs must be structured artifacts, not uncontrolled agent-to-agent chat. For Full Cycle / Full Agent Workflow handoff fields and mandatory Equity artifacts, use `workflows/handoff_artifact_standard.md` subordinate to canonical implementation documents.
- Full workflow outputs must be saved outside the project repository under `C:\Users\ShumeikoYe\OneDrive\Documents\Financial Agent Reports\[ASSET] yyyy-mm-dd hhmm\`. Save the reader-facing IC output as `investment_report.md`; save technical subagent/module materials under `audit\`, including one `.md` file per actually run subagent or module plus `run_metadata.md` and `sources.md` when available.
- In the ordinary chat response after saving a workflow, output the full reader-facing investment report using the applicable existing IC report structure, without technical runtime blocks. End with only the saved-report line in the user-facing language, e.g. for Russian: `Отчёт сохранён: ...\investment_report.md`. Do not show the audit path unless explicitly requested.

## Special analysis gates

Apply the relevant gate before strong positive conclusions:

- ambiguous ticker, listing, instrument, share class, maturity, currency, or structure;
- complex products such as leveraged/inverse ETFs, options strategies, structured notes, high-yield bonds, or crypto yield;
- private, illiquid, microcap, sparse-data, or poorly covered assets;
- cheap-looking assets that may be value traps;
- expensive growth assets that require a growth-expectations bridge;
- theses without a credible catalyst, path, or structural compounding logic.

## Language policy

Internal project Markdown files should be written in English unless explicitly requested otherwise. User-facing chat answers and generated report content follow the user's requested language under `implementation/14-language-and-style.md`.

For Russian user-facing output, apply the repo `language-policy` presentation skill: write natural Russian, avoid unnecessary English/Run-glish, translate reader-facing headings and financial terms, and preserve allowed names, tickers, indexes, official forms, code, paths, URLs, and technical identifiers.

For financial, market, investment, macro, company, sector, asset, or report-style user-facing output, apply the repo `investment-analytical-style` presentation skill: concise, businesslike, analytically dense writing without adding facts, sources, conclusions, caveats, recommendations, investment calls, risk warnings, or overriding evidence/status/IC gates. Do not announce these presentation skills in ordinary answers.
