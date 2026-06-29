# Codex Runtime Architecture

Status: Canonical Codex runtime architecture

## 1. Purpose

This document defines how the Financial Agent System should be packaged for OpenAI Codex using project instructions, repo-scoped skills, project-scoped custom agents, and workflow runbooks.

It does not replace the financial-agent architecture. It maps the canonical implementation layer into Codex-native operating surfaces so Codex can work reliably without reading the whole legacy PRD corpus on every task.

Official OpenAI references:

- Codex `AGENTS.md`: <https://developers.openai.com/codex/guides/agents-md>
- Codex skills: <https://developers.openai.com/codex/skills>
- Codex subagents and custom agents: <https://developers.openai.com/codex/subagents>

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
- instruction to use `TASKS.md` for active work status;
- instruction to use `IMPLEMENTATION_BACKLOG.md` for phase meaning and scope;
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
4. IMPLEMENTATION_BACKLOG.md for phase meaning and implementation scope
5. TASKS.md for active work status
6. Other canonical implementation documents for their specific domains
7. Supporting References only when they do not conflict with canonical documents
8. Needs Merge / Draft Source documents only as source material
9. Archive documents never as active source of truth
```

Runtime reading order:

```text
1. AGENTS.md as the concise navigator Codex loads first
2. implementation/01-documentation-control.md when source status matters
3. implementation/00-master-rules.md when global statuses, gates, style, or artifact naming matter
4. IMPLEMENTATION_BACKLOG.md when phase meaning or scope matters
5. TASKS.md when active work status matters
6. The specific canonical implementation document for the task domain
7. implementation/13-codex-runtime-architecture.md when Codex runtime packaging, custom agents, repo skills, or edge-case runtime rules matter
8. implementation/14-language-and-style.md when user-facing language, Russian output, translation cleanup, or investment-analytical presentation style matters
9. implementation/10-traceability-matrix.md before using legacy detail
10. Supporting legacy files only after registry / traceability routing
```

`AGENTS.md` is first in runtime reading order because Codex loads it first. It is not higher than canonical implementation documents in project authority.

### Root `README.md`

Purpose: human-readable orientation for maintainers and operators.

Required content:

- what the Financial Agent System is;
- current implementation status;
- directory map;
- canonical document map;
- planned Codex runtime surfaces;
- how to add or change agents, skills, workflows, and references;
- how to validate changes.

`README.md` is informational. It must not override canonical implementation documents.

### `.codex/agents/`

Purpose: project-scoped custom Codex agents.

Each custom agent must be a standalone TOML file with:

- `name`;
- `description`;
- `developer_instructions`.

Optional fields such as model, reasoning effort, sandbox, and skills should be omitted unless there is a documented project reason. Inheriting the parent session default is preferred unless a task explicitly requires a different model or execution profile.

Validation checks for future custom-agent TOML files:

- required fields exist: `name`, `description`, `developer_instructions`;
- `description` is narrow and trigger-oriented;
- `developer_instructions` points to canonical documents instead of copying full PRD content;
- no model, reasoning, sandbox, or tool override is included unless justified by the relevant runtime task;
- agent boundaries match `implementation/06-agent-contracts.md`;
- the file does not promote a legacy PRD, framework, or example above canonical documents.

### `.agents/skills/`

Purpose: repo-scoped reusable task workflows.

Each skill must be a directory containing `SKILL.md` with YAML front matter:

```md
---
name: skill-name
description: Clear when-to-use trigger and boundaries.
---
```

Each skill should include:

- purpose;
- when to use / when not to use;
- required canonical documents;
- required inputs;
- step sequence;
- output contract;
- guardrails;
- failure / Limited / Blocked behavior;
- quality checks.

Prefer instruction-only skills unless deterministic scripts are needed.

### Workflow runbooks

Workflow runbooks may live under a future `workflows/` folder or inside `implementation/05-routing-and-workflows.md` until split.

Each runbook should specify:

- entry condition;
- lead router / agent;
- required skills;
- optional custom agents;
- evidence requirements;
- sequence and parallelizable branches;
- handoff artifacts;
- completion rules;
- acceptance checks.

## 4. Custom-agent mapping

Create these 20 project-scoped custom-agent files when `P1A-CODEX-02` is executed.

| Planned contract | Custom-agent file | Runtime role |
|---|---|---|
| Master Intake Router | `.codex/agents/master-intake-router.toml` | Classifies user request and selects workflow; does not make investment decisions. |
| Asset Intake Router | `.codex/agents/asset-intake-router.toml` | Routes asset-first requests to the correct asset workflow. |
| Theme / Opportunity Intake Router | `.codex/agents/theme-opportunity-intake-router.toml` | Routes theme-first and opportunity-discovery requests. |
| Evidence Collector Agent | `.codex/agents/evidence-collector.toml` | Controls evidence collection, source status, and readiness. |
| Equity Agent | `.codex/agents/equity-agent.toml` | Produces equity specialist analysis. |
| ETF Agent | `.codex/agents/etf-agent.toml` | Produces ETF wrapper / exposure analysis. |
| Fixed Income Agent | `.codex/agents/fixed-income-agent.toml` | Produces bond / fixed-income specialist analysis. |
| Commodity Agent | `.codex/agents/commodity-agent.toml` | Produces commodity and commodity-linked exposure analysis. |
| Crypto Agent | `.codex/agents/crypto-agent.toml` | Produces crypto asset and crypto-linked exposure analysis. |
| Valuation & Expectations Agent | `.codex/agents/valuation-expectations-agent.toml` | Produces valuation and expectations analysis. |
| Risk / Red Team Agent | `.codex/agents/risk-red-team-agent.toml` | Challenges thesis quality and downside risks. |
| News & Catalysts Agent | `.codex/agents/news-catalysts-agent.toml` | Identifies recent and upcoming market-moving events. |
| Market Positioning Agent | `.codex/agents/market-positioning-agent.toml` | Assesses consensus, positioning, flows, and expectations where available. |
| Macro Agent | `.codex/agents/macro-agent.toml` | Assesses macro regime, sensitivity, and surprise context. |
| Portfolio Fit Agent | `.codex/agents/portfolio-fit-agent.toml` | Assesses portfolio role and fit without exact sizing. |
| Market Sense Agent | `.codex/agents/market-sense-agent.toml` | Produces market-behavior hypotheses without replacing evidence. |
| Market Intelligence Agent | `.codex/agents/market-intelligence-agent.toml` | Produces broad market intelligence briefings. |
| Sector & Industry Analysis Agent | `.codex/agents/sector-industry-analysis-agent.toml` | Produces sector / industry context. |
| Structural Winners Discovery Agent | `.codex/agents/structural-winners-discovery-agent.toml` | Produces candidate discovery, maps, and watchlists. |
| Investment Committee Agent | `.codex/agents/investment-committee-agent.toml` | Produces final decision-support synthesis subject to evidence and specialist gates. |

## 5. Custom-agent authoring standard

Each custom-agent TOML should be thin and should use this shape:

```toml
name = "agent-name"
description = "One-sentence trigger and scope."
developer_instructions = """
You are [Agent Name] for the Financial Agent System.

Before working, follow AGENTS.md and read only the canonical documents needed for the task:
- implementation/00-master-rules.md
- implementation/01-documentation-control.md
- implementation/02-canonical-architecture.md when architecture or boundaries matter
- implementation/05-routing-and-workflows.md when workflow routing matters
- implementation/06-agent-contracts.md for agent scope
- implementation/11-skill-contracts.md for method-skill behavior
- implementation/10-traceability-matrix.md when legacy detail is needed

Use the relevant repo skill when the task matches it.
Do not treat legacy PRDs as source of truth unless routed through the registry.
Do not override Evidence Collector readiness or Investment Committee boundaries.
Return status, key findings, evidence limitations, handoffs, and next required step.
"""
```

Do not include full legacy PRD content, large frameworks, or long methodology libraries inside `developer_instructions`.

## 6. Repo-skill mapping

Create repo skills from canonical skill contracts in `implementation/11-skill-contracts.md`.

Initial planned method skills:

| Canonical skill contract | Skill folder |
|---|---|
| Evidence Collection Method Skill | `.agents/skills/evidence-collection/` |
| Equity Company Analysis Method Skill | `.agents/skills/equity-company-analysis/` |
| Financial Statement Analysis Skill | `.agents/skills/financial-statement-analysis/` |
| Valuation & Expectations Method Skill | `.agents/skills/valuation-expectations/` |
| Risk / Red Team Method Skill | `.agents/skills/risk-red-team/` |
| Investment Committee Synthesis Method Skill | `.agents/skills/investment-committee-synthesis/` |
| ETF Analysis Method Skill | `.agents/skills/etf-analysis/` |
| Fixed Income Analysis Method Skill | `.agents/skills/fixed-income-analysis/` |
| Commodity Analysis Method Skill | `.agents/skills/commodity-analysis/` |
| Crypto Analysis Method Skill | `.agents/skills/crypto-analysis/` |
| Macro Analysis Method Skill | `.agents/skills/macro-analysis/` |
| News & Catalysts Method Skill | `.agents/skills/news-catalysts/` |
| Market Positioning Method Skill | `.agents/skills/market-positioning/` |
| Portfolio Fit Method Skill | `.agents/skills/portfolio-fit/` |
| Sector & Industry Analysis Method Skill | `.agents/skills/sector-industry-analysis/` |
| Structural Winner Discovery Method Skill | `.agents/skills/structural-winner-discovery/` |
| Driver Dominance Analysis Skill | `.agents/skills/driver-dominance-analysis/` |
| Market Sense Hypothesis Engine Skill | `.agents/skills/market-sense-hypothesis-engine/` |
| Market Intelligence Briefing Skill | `.agents/skills/market-intelligence-briefing/` |

Presentation-layer repo skills are governed by `implementation/14-language-and-style.md`, not by the method-skill contracts in `implementation/11-skill-contracts.md`:

| Presentation behavior | Skill folder |
|---|---|
| Russian language policy, translation cleanup, and Russian-target normalization | `.agents/skills/language-policy/` |
| Concise investment-analytical user-facing writing style | `.agents/skills/investment-analytical-style/` |

Presentation skills are runtime adapters for final user-facing text. They must not collect evidence, decide routing, issue `IC Action`, use `Action Box`, add facts, add sources, add caveats, add conclusions, add recommendations, add investment calls, add risk warnings, or replace analytical method skills.

## 7. Skill authoring standard

Each `SKILL.md` should:

- keep the `description` concise and trigger-oriented;
- front-load when to use and when not to use the skill;
- use imperative steps;
- point to canonical contracts rather than copying them;
- identify supporting references from the traceability matrix only when needed;
- require explicit output artifacts and handoff blocks;
- include Limited / Blocked behavior;
- include quality checks that map back to `implementation/09-system-acceptance-qa.md`.

## 8. Workflow execution model

The runtime should preserve the canonical system sequence:

1. Intake router classifies the request.
2. Evidence Collector establishes source readiness.
3. Relevant asset, specialist, discovery, or market agents run according to the workflow contract.
4. Reusable analytical methods are executed through repo skills.
5. Specialist outputs produce handoff artifacts.
6. Investment Committee synthesizes only after evidence and required specialist gates are satisfied.
7. Final output follows master rules and report schemas.

Subagents must be used only when the user, workflow runbook, or operator explicitly requests parallel delegated work. Custom agents are configuration layers for spawned Codex sessions, not permanently running independent agents. They should not create uncontrolled agent-to-agent chat. Handoffs must use structured artifacts and workflow rules.

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
| P1A-CODEX-01-17 | User asks to "run all agents" for one idea. | Interpret full analysis as a relevant-complete workflow, not literally all agents; router selects required and trigger-based agents and explains the scope. |
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
| P1A-CODEX-01-07 | User asks for a quick answer while evidence gates are normally required. | Allow Quick Take only as Preliminary/Limited for market-action or analysis-only requests, with no final buy/sell, key unknowns, and a suggested evidence-first or IC-ready next step. If the user asks for personal/final action and key context is missing, ask first. |
| P1A-CODEX-01-08 | User asks to compare ideas across different asset classes. | Use cross-asset comparison framing: common role-based criteria plus asset-specific criteria; do not declare a universal winner without the user's objective. |
| P1A-CODEX-01-09 | User omits investment horizon. | For quick takes, separate tactical 0-3 months, medium-term 6-18 months, and long-term 3-5 years; final IC Action requires explicit time horizon. |
| P1A-CODEX-01-10 | User omits risk profile or portfolio context. | For personal/final action or Portfolio Fit, ask for minimum context before user-specific guidance. General analysis and typical asset roles may proceed only as Limited / not personalized. |
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
| P1A-CODEX-01-35 | Ticker, listing, instrument, or asset identity is ambiguous. | Use ambiguity gate: proceed with explicit assumption only when obvious; ask for exact ticker/ISIN/CUSIP, exchange, currency, asset type, maturity, structure, share class, or jurisdiction when ambiguity is material. |

### P10 runtime QA operating note

When P10-QA executes runtime acceptance checks, Codex runtime behavior follows the QA model in `implementation/09-system-acceptance-qa.md`:

- use synthetic fixtures for stable pass/fail behavior and live-smoke checks only for freshness behavior;
- score safety/gate correctness separately from UX/usefulness, and do not let UX usefulness override a safety failure;
- classify prompts as personal/final action, market action / investment attractiveness, or analysis-only before choosing ask-first versus Preliminary/Limited output;
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
- project authority order and runtime reading order are separated clearly;
- the project-root discovery rule is documented;
- the 20 planned custom-agent files are mapped to canonical agent/router contracts;
- planned repo skills are mapped to canonical method-skill contracts;
- subagent usage is limited to explicitly requested or runbook-defined delegated work;
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
- root `README.md` exists and orients human maintainers;
- `.codex/agents/` contains the 20 planned custom-agent TOML files;
- `.agents/skills/` contains method skills mapped to canonical skill contracts and presentation skills mapped to `implementation/14-language-and-style.md`;
- custom agents are narrow adapters and do not copy full PRDs;
- skills are focused reusable workflows and do not silently override canonical contracts;
- legacy PRDs are accessed only through the registry and traceability matrix;
- workflow runbooks explain how routers, evidence, agents, skills, handoffs, and IC synthesis connect;
- QA scenarios can verify routing, evidence, specialist output, skill activation, and IC gates.
