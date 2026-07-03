# Codex Runtime Architecture

Status: Canonical Codex runtime architecture

## 1. Purpose

This document defines how the Financial Agent System should be packaged for OpenAI Codex using project instructions, repo-scoped skills, project-scoped custom agents, and workflow runbooks.

It does not replace the financial-agent architecture. It maps the canonical implementation layer into Codex-native operating surfaces so Codex can work reliably without reading the whole legacy PRD corpus on every task.

The Codex SDK v1 layer is a control-plane wrapper for starting, resuming, and logging local Codex threads. It must not duplicate financial workflow rules, replace route cards, or be described as an OpenAI Agents SDK runtime. Codex SDK owns launch/control/logging; `AGENTS.md`, route cards, skills, custom agents, handoff artifacts, and validators own financial behavior.

Official OpenAI references:

- Codex `AGENTS.md`: <https://developers.openai.com/codex/guides/agents-md>
- Codex skills: <https://developers.openai.com/codex/skills>
- Codex subagents and custom agents: <https://developers.openai.com/codex/subagents>
- Codex SDK: <https://developers.openai.com/codex/sdk>

## 2. Runtime design principle

Use this pattern:

```text
AGENTS.md
  -> canonical implementation documents
  -> thin custom agents
  -> focused repo skills
  -> supporting legacy PRDs / frameworks only when routed through the registry
```

Runtime rule:

- `AGENTS.md` is the concise project guidance and source-of-truth navigator.
- `README.md` is the human-readable project map.
- `.codex/agents/*.toml` defines project-scoped custom Codex agents.
- `.agents/skills/*/SKILL.md` defines repo-scoped reusable Codex skills.
- `implementation/*.md` remains the canonical implementation layer.
- Legacy PRDs and frameworks remain source material or supporting references according to `implementation/01-documentation-control.md` and `implementation/10-traceability-matrix.md`.

Do not copy full PRDs into custom-agent TOML files or `SKILL.md` files. Custom agents and skills should point to canonical contracts and load supporting legacy material only when needed.

## 2A. Project-root discovery rule

Codex project instructions and repo skills depend on where Codex is launched and what it treats as the project root. For this project:

- Start Codex from the project root: `Financial Agent System/`.
- If the project is later converted into a Git repository, keep root `AGENTS.md`, `.codex/agents/`, and `.agents/skills/` at the Git root unless a deliberate nested override is documented.
- Do not assume root `AGENTS.md` or root repo skills will be discovered when Codex is launched directly from a nested folder such as `implementation/`.
- If nested operation becomes necessary, add a small nested `AGENTS.md` or runbook note that routes back to the root source-of-truth files.

## 3. Required project files

### Root `AGENTS.md`

Purpose: durable project guidance loaded by Codex before work starts.

Required content:

- project authority order;
- runtime reading order;
- rule that canonical implementation documents govern over legacy PRDs;
- instruction to use `PROJECT_STATE.md` for current runtime state;
- instruction to treat `archive/project-history/TASKS.md` and `archive/project-history/IMPLEMENTATION_BACKLOG.md` as historical records;
- instruction to use `implementation/01-documentation-control.md` and `implementation/10-traceability-matrix.md` before treating any legacy PRD as relevant;
- no-MVP rule;
- evidence-before-synthesis rule;
- Investment Committee final synthesis boundary;
- skill and subagent usage rules;
- language policy: internal project Markdown in English unless explicitly requested otherwise; user-facing answers and report content follow the user's requested language under `implementation/14-language-and-style.md`.

Project authority order:

```text
1. implementation/00-master-rules.md for statuses, gates, output standards, confidence, source display, style, and artifact naming
2. implementation/01-documentation-control.md for registry, source precedence, archive behavior, and source issues
3. implementation/14-language-and-style.md for user-facing language selection, Russian language policy, and investment-analytical presentation style
4. PROJECT_STATE.md for current runtime state
5. workflows/route_cards/ for daily runtime route selection
6. Other canonical implementation documents for their specific domains
7. Supporting References under `references/` only when they do not conflict with canonical documents
8. `implementation/remaining-requirements.md` only as a residual candidate-requirement register, not as executable runtime authority
9. Archive documents under `archive/legacy-prd/` never as active source of truth
```

Runtime audit plan template:

```text
Execution mode: Agent workflow with spawned subagents
Subject: [asset]
Route: Master Intake -> Asset Intake -> [asset workflow]
Included modules:
- request intake and 5-question workflow intake
- asset identity and route check
- evidence collection and freshness check
- macro context (default for every asset class)
- sector / industry context (default for equity; otherwise include only when relevant)
- lead asset-class analysis
- financial statement analysis, when applicable
- news / catalysts, when freshness or event risk is material
- valuation / expectations or asset-class equivalent
- risk / red-team review
- portfolio fit / limited portfolio fit
- IC synthesis
Actually spawned subagents when spawned-subagent mode is used:
- [agent name -> handoff artifact]
Fallback reason when no subagents were spawned:
- [only if production blocked state when subagents are unavailable is used]
Excluded modules:
- [module -> reason]
Module status table:
| Module | Status | Reason / limitation |
|---|---|---|
| request intake and workflow intake | Complete / Limited / Blocked | [reason] |
| evidence collection | Complete / Limited / Blocked | [reason] |
| macro context | Complete / Limited / Blocked / Not material | default module for all full asset workflows; at least a short macro handoff is expected unless explicit source scope or route rationale justifies Not material / Skipped with reason in audit |
| sector / industry context | Complete / Limited / Blocked / Not material | default for equity; otherwise explain relevance |
| lead asset-class analysis | Complete / Limited / Blocked | [reason] |
| financial statement analysis | Complete / Limited / Blocked / Not material | [reason] |
| valuation / expectations | Complete / Limited / Blocked | [reason] |
| risk / red-team review | Complete / Limited / Blocked | [reason] |
| portfolio fit | Complete / Limited / Blocked | [reason] |
| IC synthesis | Complete / Limited / Blocked | [reason] |
```

Minimum equity handoff artifact set:

```text
evidence_pack.md
macro_sensitivity.md or macro_context.md
sector_context.md or sector_industry_analysis.md
equity_company_analysis.md
financial_statement_analysis.md
valuation_expectations.md
risk_red_team.md
portfolio_fit.md
IC-stage gate-aware artifact: decision_prep_memo.md by default when portfolio context is the remaining final-action gate; otherwise limited_ic_draft.md, evidence_gap_memo.md, or final_investment_memo.md only as allowed by IC schemas.
```

Investment Committee synthesis may consume only the audit Runtime Execution Plan, validated handoff artifacts or artifact-equivalent summaries, the pre-IC evidence lock, material conditional-module handoffs, and sanity-checked user context. If a required handoff is missing or lacks owner/status/evidence limits/missing gates/downstream handoff, IC must request the corrected handoff or select a gate-aware Limited/Blocked artifact such as `decision_prep_memo.md`, `limited_ic_draft.md`, or `evidence_gap_memo.md`.

### Canonical sequence

The runtime should preserve the canonical system sequence:

1. Intake router classifies the request.
2. Concrete-asset investment action requests route through `AGENT:` / the internal full workflow unless the user explicitly asks for `QUICK:` / short / fast / quick take / preliminary answer.
3. Large workflow runs record `Execution mode` and a Runtime Execution Plan in audit before analysis, including included modules, excluded modules, and rationale.
4. Evidence Collector establishes source readiness.
5. Relevant asset, specialist, discovery, or market modules run according to the workflow contract. When subagents are actually spawned, they perform spawned-subagent modules and return structured handoffs; otherwise the main session records a production blocked state when subagents are unavailable without advertising it as a user mode.
6. Reusable analytical methods are executed through repo skills.
7. Specialist outputs produce handoff artifacts or handoff summaries.
8. Investment Committee synthesizes only after evidence and required specialist gates are satisfied, or produces a gate-aware non-final artifact when gates are incomplete.
9. Final output follows master rules and report schemas and must not imply spawned subagents ran unless they actually did.


### AGENT workflow runtime plan and completion check

For concrete-asset investment action requests, such as asking whether to invest, buy, add, hold, sell, start exposure, or evaluate an asset for a multi-year horizon, the runtime routes through `AGENT:` / the internal full workflow unless the user explicitly requests `QUICK:` / short / fast / quick take / preliminary output. `AGENT:` automatically spawns all route-relevant subagents without requiring explicit user delegation wording, and must not claim agent workflow execution unless subagents were actually spawned.

The audit pack must record `Execution mode` and a compact Runtime Execution Plan before analysis. The plan lists analytical modules executed by the main session and, only when spawned-subagent work actually occurred, the subagents spawned and the handoffs they must return. Non-spawned-subagent blocked production issue is audit-only and not a selectable user mode. Ordinary chat does not show this block unless explicitly requested:

Runtime Execution Plan required fields are audit metadata: execution mode, subject / asset, included modules, excluded modules, reason for route, actually spawned subagents when spawned-subagent mode is used, fallback reason when no subagents were spawned, and module status for every included module using `Complete`, `Limited`, `Blocked`, `Not material`, or `Skipped with reason`.

```text
# audit\run_metadata.md snippet; not ordinary chat
Execution mode: Agent workflow with spawned subagents
Subject: [asset]
Route: Master Intake -> Asset Intake -> Equity internal full workflow
Included modules:
- request intake and 5-question workflow intake
- asset identity and route check
- evidence collection and freshness check
- macro context (default for every full asset workflow)
- sector / industry context (default for equity)
- equity company analysis
- financial statement analysis, when applicable
- news / catalysts, when freshness or event risk is material
- valuation / expectations
- risk / red-team review
- portfolio fit / limited portfolio fit
- IC synthesis
Actually spawned subagents when spawned-subagent mode is used:
- [agent name -> handoff artifact]
Fallback reason when no subagents were spawned:
- [only if production blocked state when subagents are unavailable is used]
Excluded modules:
- [module -> reason]
Module status table:
| Module | Status | Reason / limitation |
|---|---|---|
| request intake and workflow intake | Complete / Limited / Blocked | [reason] |
| evidence collection | Complete / Limited / Blocked | [reason] |
| macro context | Complete / Limited / Blocked / Not material | default module for every full asset workflow; at least a short macro handoff is expected unless explicit source scope or route rationale justifies Not material / Skipped with reason in audit |
| sector / industry context | Complete / Limited / Blocked / Not material | default equity module; status must be audit-recorded |
| equity company analysis | Complete / Limited / Blocked | [reason] |
| financial statement analysis | Complete / Limited / Blocked / Not material | [reason] |
| valuation / expectations | Complete / Limited / Blocked | [reason] |
| risk / red-team review | Complete / Limited / Blocked | [reason] |
| portfolio fit | Complete / Limited / Blocked | [reason] |
| IC synthesis | Complete / Limited / Blocked | [reason] |
Reason:
- [short route rationale]
```

Every listed module must have an audit-recorded status as `Complete`, `Limited`, `Blocked`, `Not material`, or `Skipped with reason`.

Status tokens `Complete`, `Limited`, `Blocked`, `Not material`, and `Skipped with reason` are controlled metadata and may remain in English inside audit; reader-facing report prose must follow the user-facing language policy.

Before calling the result a complete large workflow, the runtime must verify that every item listed under Included Modules appears in a Module Status table with one valid status. Conditional modules such as financial statements, news/catalysts, valuation, risk, and Portfolio Fit must be included with status or excluded with reason. Macro is a default module for every asset class; sector / industry is a default module for equity. If any listed module has no valid status, complete the missing work, record a valid module status, or downgrade to `Preliminary`, `Limited`, `Evidence Gap Memo`, or another gate-aware non-final artifact. A Limited large workflow remains valid only when every included module has an audit-recorded valid status and the artifact is gate-aware.

Subagents should be used for `AGENT:` concrete-asset investment workflows when relevant and available. Custom agents are configuration layers for spawned Codex sessions, not permanently running independent agents. They should not create uncontrolled agent-to-agent chat. Handoffs must use structured artifacts and workflow rules. If no subagents were spawned, record a production blocked state when subagents are unavailable only in audit metadata; do not present the output as an agent workflow with spawned subagents.

### Intake questions and report packaging

Before an `AGENT:` / full investment workflow starts, ask exactly 5 asset-specific questions in one block and wait for the user's next message. Before an explicit short / fast / Quick Take answer, ask exactly 3 relevant questions in one block and keep the answer chat-only. If asset identity, ticker, instrument, currency, maturity, or structure is ambiguous, count the clarification inside the required 5-question `AGENT:` block or 3-question `QUICK:` block wherever possible. Ask a separate blocking clarification only when the request is truly unroutable, such as an unresolved ticker/share-class/instrument conflict that prevents route selection.

Full workflow packaging writes reader-facing `investment_report.md` plus an `audit\` folder under `C:\Users\ShumeikoYe\OneDrive\Documents\Financial Agent Reports\[ASSET] yyyy-mm-dd hhmm\`. The chat response must reproduce `investment_report.md` exactly and end with only the saved report path. The audit path, agent list, execution mode, runtime plan, module statuses, canonical artifact type, full source list, Portfolio Fit technical status, and handoff metadata are shown only when explicitly requested. When portfolio context is missing, the report shows general Portfolio role wording while audit records `Portfolio Fit: Limited / not personalized` and General Portfolio Role Mode.

## 9. Generation sequence

Do not generate all runtime files before their canonical sources are stable.

Recommended sequence:

1. Finalize canonical architecture and master rules.
2. Finalize contract templates.
3. Finalize canonical agent contracts.
4. Finalize canonical skill contracts.
5. Create root `AGENTS.md`.
6. Create root `README.md`.
7. Create `.codex/agents/*.toml` from the 20 planned contracts.
8. Create method `.agents/skills/*/SKILL.md` from canonical skill contracts and presentation skills from `implementation/14-language-and-style.md`.
9. Create or split workflow runbooks if `implementation/05-routing-and-workflows.md` becomes too large.
10. Run acceptance checks from `implementation/09-system-acceptance-qa.md`.

## 10. P1A-CODEX-01 runtime edge-case rules

These rules canonicalize the approved Codex runtime edge-case decisions for P1A-CODEX-01. They govern architecture and packaging behavior only. They do not authorize creation of root `AGENTS.md`, root `README.md`, custom-agent TOML files, repo skills, or workflow runbooks before P1A-CODEX-02 and its dependencies are ready.

Rule IDs preserve the original review sequence. The tables below group them by runtime concern so implementers can apply related safeguards together; QA coverage is audited by stable ID rather than table order.

### Project discovery and source-of-truth behavior

| Rule ID | Runtime edge case | Required safe behavior |
|---|---|---|
| P1A-CODEX-01-01 | Codex is launched from a nested folder rather than the project root. | Use a hybrid root-discovery rule: prefer launch from `Financial Agent System/`, attempt to identify the root from canonical project files, and ask the user to reopen the root only when the project cannot be safely identified. |
| P1A-CODEX-01-02 | Runtime files are requested before canonical contracts are stable. | Permit only safe navigation/structure artifacts until contracts are ready; do not create runtime-ready agents or skills before their canonical gates. |
| P1A-CODEX-01-03 | Root `AGENTS.md` conflicts with canonical implementation documents. | Treat `AGENTS.md` as entrypoint and navigator only; canonical implementation documents govern, and conflicts must be surfaced as source issues. |
| P1A-CODEX-01-16 | Legacy PRD material contains useful detail not yet canonicalized. | Use legacy detail only through registry and traceability routing; if important missing detail is found, record a source issue rather than silently promoting it to runtime rule. |

### Runtime generation gates

| Rule ID | Runtime edge case | Required safe behavior |
|---|---|---|
| P1A-CODEX-01-04 | Custom-agent TOML files could become large copied PRDs. | Keep custom agents thin, but require output contracts: role, non-responsibilities, canonical documents, statuses, handoff blocks, and Limited/Blocked behavior. |
| P1A-CODEX-01-21 | User asks to create a custom agent before its canonical agent contract is ready. | Use contract-gated generation: create runtime-ready `.toml` only from a canonical contract or stable canonical section; otherwise create only a planned manifest entry or an explicitly `Draft / Not Runtime-Ready` artifact. |
| P1A-CODEX-01-22 | User asks to create a skill before its canonical skill contract is ready. | Use a skill readiness gate: runtime-ready `SKILL.md` requires triggers, inputs, steps, output contract, guardrails, Limited/Blocked behavior, and quality checks; otherwise keep only a planned skill entry or `Not Runtime-Ready` draft. |

### Agent, skill, workflow, and IC boundaries

| Rule ID | Runtime edge case | Required safe behavior |
|---|---|---|
| P1A-CODEX-01-05 | User asks a specialist agent for a final buy/sell decision. | Specialist agents provide scoped `Specialist Verdict` only, state `Boundary: Not an IC Action`, list missing IC gates, and may offer to route to IC workflow. |
| P1A-CODEX-01-17 | User asks to "run all agents" for one idea. | Interpret full analysis as a relevant-complete spawned-subagent workflow, not literally all agents; use relevant agents only, record included/excluded agents and structured handoffs in audit, and show them in chat only if requested. |
| P1A-CODEX-01-18 | Agents produce conflicting findings. | IC performs conflict synthesis rather than averaging: identify agreement, decision-critical conflicts, facts needed to resolve them, and whether Complete IC Action is allowed. |
| P1A-CODEX-01-20 | A task matches both a custom agent and a repo skill. | Agent owns role, boundary, status, and handoff; skill owns reusable method. Workflow/router decides sequencing. Skills do not issue final IC Actions. |
| P1A-CODEX-01-23 | User requests a final report before required gates are complete. | Use gate-aware artifact naming such as `Preliminary Investment Brief`, `Limited IC Draft`, `Evidence Gap Memo`, `Specialist Summary`, or `Decision-Prep Memo`; do not label it `Final Investment Memo`. |
| P1A-CODEX-01-27 | User asks for watchlist or monitoring behavior. | Require an explicit monitoring contract covering sources, frequency, triggers, thresholds, thesis-changing events, output, and any automation limits; do not promise real-time monitoring unless automation is configured. |

### Evidence, freshness, and source-scope controls

| Rule ID | Runtime edge case | Required safe behavior |
|---|---|---|
| P1A-CODEX-01-06 | Evidence Collector cannot obtain reliable sources. | Apply claim-level support and constrain status to Complete, Limited, or Blocked based on confirmed, partial, conflicting, stale, unsupported, or unavailable claims. |
| P1A-CODEX-01-12 | User asks about today, yesterday, now, latest, earnings, price action, or news. | Apply a freshness gate: use current sources with timestamps, separate facts from market reaction and interpretation, and mark Limited/Blocked if fresh data is unavailable. |
| P1A-CODEX-01-13 | Sources conflict on a material claim. | Apply conflict protocol: show the conflict, rank source authority, check date/period/methodology/unit/currency, and do not treat disputed facts as fully supported until resolved. |
| P1A-CODEX-01-24 | User-provided file is incomplete, unclear, or mixed with assumptions. | Classify file provenance, check units/currency/periods/tickers/formulas/missing fields, separate facts from assumptions, and treat user files as evidence inputs rather than unconditional truth. |
| P1A-CODEX-01-25 | User says to use only their sources. | Respect the source scope, mark the output `Limited by source scope`, avoid claims beyond provided materials, and offer external verification as an optional next step only. |
| P1A-CODEX-01-26 | User forbids internet/data refresh for a freshness-dependent request. | Use no-refresh constrained mode: status Limited, no current-market claims, scenario/framework analysis only, and no Complete current-market conclusion. |

### User-context and UX behavior

| Rule ID | Runtime edge case | Required safe behavior |
|---|---|---|
| P1A-CODEX-01-07 | User asks for a quick answer while evidence gates are normally required. | Allow Quick Take only when the user explicitly asks for `QUICK:` / short / fast / quick take / preliminary output. Concrete-asset investment action requests otherwise route to `AGENT:` / the internal full workflow, with no final buy/sell unless IC gates pass. Count identity clarification inside the required intake block where possible; ask separately only for truly unroutable identity conflicts. Non-blocking portfolio context limits Portfolio Fit / IC status. |
| P1A-CODEX-01-08 | User asks to compare ideas across different asset classes. | Use cross-asset comparison framing: common role-based criteria plus asset-specific criteria; do not declare a universal winner without the user's objective. |
| P1A-CODEX-01-09 | User omits investment horizon. | For quick takes, separate tactical 0-3 months, medium-term 6-18 months, and long-term 3-5 years; final IC Action requires explicit time horizon. |
| P1A-CODEX-01-10 | User omits risk profile or portfolio context. | For clear concrete-asset internal full workflow requests, proceed with general analysis and mark Portfolio Fit Limited / not personalized; ask minimum context before personalized final action. If the missing context blocks route or safe identity, ask first. |
| P1A-CODEX-01-11 | User requests exact position size or allocation. | Discuss only scenario-based ranges with assumptions and stress tests; do not issue exact allocation as an instruction. |
| P1A-CODEX-01-14 | User asks for a simple explanation of a complex investment question. | Use plain language while keeping visible statuses, assumptions, risks, unknowns, and IC boundaries. |
| P1A-CODEX-01-15 | User asks for "no disclaimers" or just the action. | Compress wording but preserve critical guardrails: status, assumptions, missing data, evidence limits, and specialist-vs-IC boundary. |
| P1A-CODEX-01-19 | User requests a format that could hide limitations. | Respect the requested format only if mandatory fields remain visible: status, confidence/uncertainty, evidence limitations, assumptions, missing data, source basis, and output boundary. |
| P1A-CODEX-01-32 | User asks whether an asset is "good" without stating the job it should do. | Use role-first assessment across growth, income, preservation, inflation hedge, crisis hedge, diversifier, speculation, and liquidity parking; IC Action requires an objective. |

### Asset, thesis, and instrument complexity

| Rule ID | Runtime edge case | Required safe behavior |
|---|---|---|
| P1A-CODEX-01-28 | User equates good business quality with good investment quality. | Separate Business Quality Verdict from Financial Quality, Competitive Position, Valuation/Expectations, Risk/Downside, Investment View, and IC Action. |
| P1A-CODEX-01-29 | Asset looks cheap but may be a value trap. | Require a value-trap checklist before positive valuation verdict: earnings quality, leverage/liquidity, cyclicality, secular decline, governance, accounting red flags, regulatory/litigation, dividend sustainability, catalyst, and why the market is wrong. |
| P1A-CODEX-01-30 | Asset looks expensive but growth may justify valuation. | Use a growth-expectations bridge: embedded growth, realism, runway, margins, reinvestment, competitive durability, unit economics, slowdown downside, compression triggers, and what must go right. |
| P1A-CODEX-01-31 | User asks for a thesis but no catalyst/path is visible. | Classify thesis path as hard catalyst, soft catalyst, structural compounding, monitoring thesis, or no credible path; constrain IC Action when no credible path exists. |
| P1A-CODEX-01-33 | Product is complex, such as leveraged/inverse ETF, options strategy, structured note, high-yield bond, or crypto yield. | Apply complex product gate before attractive yield/upside conclusions: payoff, leverage/inverse mechanics, path dependency, embedded options, costs, liquidity, counterparty/issuer risk, failure modes, suitability, and holding-period mismatch. |
| P1A-CODEX-01-34 | Asset is private, illiquid, microcap, sparse-data, or poorly covered. | Use sparse-data mode by default: provenance, liquidity/price discovery warnings, higher positive-conclusion threshold, scenario ranges instead of point valuation, fraud/governance/accounting checks, exit risk, and Limited status absent strong primary documents. |
| P1A-CODEX-01-35 | Ticker, listing, instrument, or asset identity is ambiguous. | Use ambiguity gate: proceed with explicit assumption only when obvious; count exact ticker/ISIN/CUSIP, exchange, currency, asset type, maturity, structure, share class, or jurisdiction clarification inside the required intake block where possible, and ask separately only when the request is truly unroutable. |

### P10 runtime QA operating note

When P10-QA executes runtime acceptance checks, Codex runtime behavior follows the QA model in `implementation/09-system-acceptance-qa.md`:

- use synthetic fixtures for stable pass/fail behavior and live-smoke checks only for freshness behavior;
- score safety/gate correctness separately from UX/usefulness, and do not let UX usefulness override a safety failure;
- classify prompts as personal/final action, concrete-asset investment action, market setup / attractiveness, or analysis-only before choosing internal full workflow, ask-first, or explicit Preliminary/Limited output;
- treat final action language from non-IC agents or skills as a safety failure;
- require Limited/Blocked outputs to include a concise next-step block;
- compress caveats when requested, but never remove status, evidence limits, missing gates, or boundaries;
- treat missing data as Defer / Not Actionable rather than Hard Avoid; Hard Avoid requires strong disqualifying evidence and IC ownership;
- verify runtime agents remain thin and skills remain concise adapters to canonical contracts.
- verify user-facing language and presentation style follow `implementation/14-language-and-style.md`, including strict Russian mode for Russian output and investment-analytical style for financial user-facing text.

## 11. Acceptance criteria

### P1A-CODEX-01 readiness

The Codex runtime architecture layer is ready when:

- `implementation/13-codex-runtime-architecture.md` defines the intended root `AGENTS.md`, root `README.md`, `.codex/agents/`, `.agents/skills/`, and workflow runbook conventions;
- project authority order and runtime reading order are separated clearly around `PROJECT_STATE.md` and route cards;
- the project-root discovery rule is documented;
- the 20 planned custom-agent files are mapped to canonical agent/router contracts;
- planned repo skills are mapped to canonical method-skill contracts;
- `AGENT:` / full concrete-asset investment workflows use relevant spawned subagents by default; if no subagents are actually spawned, audit records a production blocked state when subagents are unavailable and output must not imply subagent spawning;
- validation checks for future custom-agent TOML files are documented;
- legacy PRDs remain routed through the registry and traceability matrix.
- this document contains stable runtime edge-case rules `P1A-CODEX-01-01` through `P1A-CODEX-01-35`;
- P1A-CODEX-01 architecture rules are clearly separated from P1A-CODEX-02 runtime file generation;
- runtime-ready custom agents and repo skills remain gated by canonical agent/skill contract readiness.



### P1A structural runtime readiness gate

P1A-CODEX-02 may be marked Done when the generated Codex runtime package is created from the current canonical agent and skill contracts and those contracts pass the structural readiness checks below. This is a packaging gate for Codex runtime files. It did not originally complete broader P5-AGT-01 or P5-SKL-01 normalization; after P5-AGT-01 and P5-SKL-01 completion, agent and method-skill contracts are normalized and runtime adapters should remain synchronized to those canonical contracts.

- Agent structural readiness requires: Purpose, Scope, Responsibilities, Non-responsibilities, Required inputs, Evidence requirements, Workflow role, Handoffs, failure-state rules, and Success criteria.
- Skill structural readiness requires: Purpose, When to use, What you get, What it will not do, Required inputs, Step sequence, Output contract, Guardrails, Failure states, and Quality checks.
- If a future P5 normalization change materially changes a canonical contract, the affected runtime agent or skill must be regenerated or marked Not Runtime-Ready until reconciled.
- The generated runtime package must record the gate result in `.codex/runtime-readiness-report.md`.

### P1A-CODEX-02 readiness

The generated Codex runtime package is ready when:

- root `AGENTS.md` exists and provides concise project guidance;
- root `README.md` exists and orients users and maintainers;
- `.codex/agents/` contains the 20 planned custom-agent TOML files;
- `.agents/skills/` contains method skills mapped to canonical skill contracts and presentation skills mapped to `implementation/14-language-and-style.md`;
- custom agents are narrow adapters and do not copy full PRDs;
- skills are focused reusable workflows and do not silently override canonical contracts;
- legacy PRDs are accessed only through the registry and traceability matrix;
- route cards and workflow runbooks explain how routers, evidence, agents, skills, handoffs, and IC synthesis connect;
- QA scenarios can verify routing, evidence, specialist output, skill activation, and IC gates.


## Additive Python LangGraph runtime

Status: MVP runtime layer present.

`langgraph_runtime/` is an additive Python runtime that maps the existing route-card and skill contracts into a LangGraph `StateGraph`. It does not replace root `AGENTS.md`, route cards, repo skills, custom agents, validators, or the Codex SDK control layer. It also must not claim OpenAI Agents SDK runtime behavior.

## Automation Lab data provider layer

Status: Available data/evidence infrastructure.

`automation_lab/data_providers/` and `automation_lab/data_parsers/` provide the on-demand provider/parsing layer used by Automation Lab preflight and snapshot flows. The layer owns source fetching, parsing, normalization, raw/normalized cache files, source-tier/freshness metadata, ProviderResult schema validation, and conversion of provider claims into Evidence Pack inputs.

This layer is not an agent runtime and must not redefine route cards, evidence gates, IC actions, report language, or canonical investment rules. Search/discovery outputs remain Pointer-Only until the underlying official/accessible source is fetched and parsed.

Runtime files:

- `langgraph_runtime/IMPLEMENTATION_MAP.md` records the inventory-to-runtime mapping and exact created files.
- `langgraph_runtime/state.py` defines the typed graph state fields required by the runtime objective.
- `langgraph_runtime/routing.py` implements natural-language and explicit-prefix routing.
- `langgraph_runtime/nodes.py` implements required graph node functions, live module outputs, gates, interrupts, and artifact handoff boundaries.
- `langgraph_runtime/financial_agent_graph.py` builds the `StateGraph`, conditional edges, equity subgraph, checkpointer, streaming helper, and CLI.
- `.env.example` documents `OPENAI_API_KEY`, `OPENAI_MODEL`, and `OPENAI_REASONING_EFFORT`.

Runtime rules:

- Dry-run mode must not call the OpenAI API.
- Live mode must require `OPENAI_API_KEY` and must not hardcode secrets.
- Ordinary natural-language investment requests route through `intake_router_node`; explicit prefixes remain shortcuts.
- Missing decision-critical context, evidence readiness failure, risk gate failure, and final IC confirmation points use LangGraph interrupt-capable nodes where applicable.
- Reports are idempotently written as reader-facing `investment_report.md` plus technical `audit/` only for full workflows. Quick Take and direct specialist routes remain Preliminary / Not an IC Action and do not create full report/audit artifacts. Portfolio Fit technical status stays in audit; missing portfolio context appears in the report as general Portfolio role.


## Production live AGENT execution rule

For user-requested investment analysis, the Codex-native runtime is live-first and agent-first. A prompt such as "analyze this company" is sufficient to trigger the route-relevant AGENT workflow; the user does not need to write "use agents", "delegate", or "run in parallel". The parent workflow must spawn all route-relevant custom agents, collect their structured handoffs, and only then perform IC synthesis. Historical fixture/non-production fixture/live paths are not production analysis paths. No fixed wall-clock timeout may stop a production live workflow; subprocess and full-run timeout environment variables are deprecated for production and must not cap specialist execution.
