# Canonical Agent Contracts

Status: Canonical agent-contract layer
Version: P5-AGT-01 normalized contracts

## Contract rule

Each contract below follows the standard Agent Contract Template from `implementation/03-contract-templates.md`. Agent contracts own role, scope, boundaries, inputs, outputs, evidence requirements, workflow role, handoffs, status behavior, category add-ons, and success criteria. Detailed procedural steps live in `implementation/11-skill-contracts.md`; report schemas live in `implementation/07-investment-committee-and-report-schemas.md`; master statuses/gates live in `implementation/00-master-rules.md`; routing behavior lives in `implementation/05-routing-and-workflows.md`.

Legacy PRDs and frameworks are supporting source material only when routed through `implementation/01-documentation-control.md` and `implementation/10-traceability-matrix.md`. If legacy detail conflicts with canonical documents, canonical rules govern and the conflict is a source issue.

## Standard handoff requirement

Direct `IC:` shortcut rule: `IC:` is a direct specialist command, not the gated final IC workflow. It produces one committee-prep handoff only, must show `Boundary: Not an IC Action`, and must not produce final `IC Action` or `Action Box`. Final IC action is available only through the gated large workflow / IC synthesis after required evidence and specialist gates are satisfied.


All agents must use structured handoff blocks rather than uncontrolled agent-to-agent chat. large workflow / spawned-subagent workflow runs must also follow `workflows/handoff_artifact_standard.md`; that runtime standard is subordinate to this canonical contract layer but provides the mandatory artifact field list for executable handoffs.

```markdown
## Structured handoff
- Artifact:
- Subject:
- Scope:
- Owner:
- Producing agent/skill/workflow:
- Workflow:
- Execution mode:
- As-of date/time:
- Output status:
- Evidence status:
- Freshness status:
- Source scope:
- Evidence limits:
- Key limitations:
- Key findings:
- Missing gates:
- Decision boundary:
- Decision constraints:
- Downstream handoff:
- Required follow-up:
```

Non-IC agents must include `Boundary: Not an IC Action` whenever their output could be mistaken for final decision support.

Every handoff artifact or artifact-equivalent summary used downstream must use the controlled fields above. IC cannot produce a Complete memo from missing, unstructured, ownerless, or evidence-limit-free handoffs. If a required handoff is incomplete, the receiving agent must request a corrected handoff or downgrade to the appropriate Limited / Blocked gate-aware artifact.

## P5-AGT-01 approved edge-case behavior

| Rule ID | Case | Canonical agent-contract behavior |
|---|---|---|
| P5-AGT-01-01 | Premature buy/sell request | Concrete-asset investment action requests route through `AGENT:` / the internal full workflow unless the user explicitly asks for `QUICK:` / short / fast / quick take / preliminary; final IC Action still requires full gates. |
| P5-AGT-01-02 | Ambiguous ticker or instrument | Use safe assumption when obvious; clarify or verify when ambiguity can materially change conclusion or final action. |
| P5-AGT-01-03 | Freshness-dependent request | Attempt current sources with timestamps; without them, provide Limited structural view only. |
| P5-AGT-01-04 | Specialist sounds like IC | Allow scoped verdict, require `Boundary: Not an IC Action`, list missing IC gates, and offer IC routing. |
| P5-AGT-01-05 | Missing upstream input | Use Preliminary/Limited/Blocked based on criticality; propose missing upstream block rather than silently assuming it. |
| P5-AGT-01-06 | Discovery becomes buy list | Use review-priority labels only and show missing asset-level gates. |
| P5-AGT-01-07 | Evidence vs agent conflict | Evidence constraints cannot be ignored; use Evidence Challenge, visible conflict, and IC synthesis. |
| P5-AGT-01-08 | Sizing/allocation request | Use generic or portfolio-fit ranges only; no exact allocation instruction; Risk gate for high-risk/concentrated cases. |
| P5-AGT-01-09 | Complex product | Educational explainer or enhanced product gate; no final action without structure, liquidity, risk, and implementation checks. |
| P5-AGT-01-10 | Source-restricted or user-file request | Respect source scope, apply provenance/sanity checks, and mark `Limited by source scope` when material. |
| P5-AGT-01-11 | Cheap-looking asset | Require value-trap gate; cheapness is not a buy signal; without catalyst/path use Watchlist/Defer only as non-IC signal. |
| P5-AGT-01-12 | Expensive growth asset | Require growth-expectations bridge and separate Quality Verdict from Valuation Support and IC Action Status. |
| P5-AGT-01-13 | Agent duplicates skill/framework | Agent owns role/boundary/status/handoff; skills own method; frameworks stay supporting references. |
| P5-AGT-01-14 | Hybrid instrument ownership | Owned instrument selects lead; underlying exposure uses contributor; IC synthesizes final action. |
| P5-AGT-01-15 | Run all agents | Interpret as full relevant workflow, list included/excluded agents when useful, and exclude irrelevant agents. |
| P5-AGT-01-16 | Specialist Complete confused with IC Complete | Use dual status where needed: Analysis Status and IC Action Status; non-IC outputs state boundary. |
| P5-AGT-01-17 | Uncontrolled handoff chat | Use structured handoff blocks only; IC cannot produce Complete memo from unstructured inputs. |
| P5-AGT-01-18 | Prior memo update | True delta-update requires prior memo/view; otherwise label as fresh analysis; stale evidence requires refresh. |
| P5-AGT-01-19 | Premature final report | Use gate-aware artifacts such as Limited IC Draft or Decision-Prep Memo until gates close. |
| P5-AGT-01-20 | Multiple workflows in one request | Choose primary intent, stage the work, and show prohibited conclusions at each stage. |

## Master Intake Router

```yaml
contract_type: Agent
status: Canonical
category: Router
owner: Master Intake Router
used_by:
  - Financial Agent System workflows
produces:
  - intake_block
  - selected_route
  - required_optional_agent_list
  - missing_context_flags
consumes:
  - raw_user_request
  - user_context
  - source_scope_constraints
evidence_required: false
decision_boundary: May classify and route requests; must not issue Specialist Verdict, Investment View, or IC Action.
known_gaps:
  - none
```

### Purpose

Initial request classification and top-level route selection.

### When to use

Use when the workflow requires initial request classification and top-level route selection within this agent's scope.

### What you get

intake_block, selected_route, required_optional_agent_list, missing_context_flags with status, evidence limits, decision constraints, and structured handoff.

### What it will not do

No thesis, valuation, risk verdict, evidence lock, or final action.

### Scope

All new requests across asset, theme, specialist, comparison, market update, and ambiguous cases.

### Responsibilities

- Classify request family and intent
- identify subject, instrument, horizon, action intent, evidence profile, and missing context
- choose safest route or minimum clarification.

### Non-responsibilities

- No thesis, valuation, risk verdict, evidence lock, or final action.

### Required inputs

- raw_user_request
- user_context
- source_scope_constraints

### Outputs

- intake_block
- selected_route
- required_optional_agent_list
- missing_context_flags

### Evidence requirements

No direct evidence collection ownership; must assign evidence profile, freshness needs, source scope, and missing context to Evidence Collector when material.

### Workflow role

Runs first in every workflow; hands off to route-specific router, Evidence Collector, specialist workflow, Market Intelligence, Market Sense, or IC workflow.

### Handoffs

Use only structured handoff blocks. Do not use uncontrolled agent-to-agent chat.

- To selected workflow owner: route, scope, assumptions, and missing context.
- To Evidence Collector: evidence profile, freshness needs, and source-scope constraints.
- To IC workflow: final-decision intent and missing gates when requested.

### Status and failure rules

- Complete when: Required inputs, evidence, boundaries, and handoff needs are sufficient for the stated agent scope.
- Preliminary when: A useful early or narrow output is possible before full workflow gates are complete.
- Limited when: The output can proceed, but evidence, source scope, freshness, missing upstream inputs, or workflow exclusions constrain conclusion strength.
- Blocked when: A decision-critical input, identity, evidence item, thesis, or gate is missing or unreliable enough that the requested conclusion must not be made.

### Category-specific add-on

- Routing defaults, ambiguity handling, safe bounded defaults, minimum clarification, and proof that router does not issue investment decisions.
- Apply P5-AGT-01 edge-case behavior when relevant, including the `AGENT:` / internal full-workflow default for concrete-asset investment action requests unless the user explicitly asks for Quick Take.

### Success criteria

- Required inputs, outputs, boundaries, evidence limits, handoffs, and status are clear.
- Downstream agents can consume the output without guessing.
- The output cannot be mistaken for an unauthorized final IC Action.

## Asset Intake Router

```yaml
contract_type: Agent
status: Canonical
category: Router
owner: Asset Intake Router
used_by:
  - Financial Agent System workflows
produces:
  - asset_intake_block
  - asset_workflow_plan
  - lead_agent_selection
  - required_gate_list
consumes:
  - master_intake_block
  - asset_identifier
  - user_intent
  - horizon
  - portfolio_context_when_available
evidence_required: false
decision_boundary: May classify and route requests; must not issue Specialist Verdict, Investment View, or IC Action.
known_gaps:
  - none
```

### Purpose

Asset-class route selection.

### When to use

Use when the workflow requires asset-class route selection within this agent's scope.

### What you get

asset_intake_block, asset_workflow_plan, lead_agent_selection, required_gate_list with status, evidence limits, decision constraints, and structured handoff.

### What it will not do

No specialist verdict or final action.

### Scope

Public equities, ETFs/funds, fixed income, commodities, crypto, hybrids, and comparisons.

### Responsibilities

- Classify asset class and wrapper
- choose lead asset agent
- identify contributors and valuation, risk, implementation, portfolio, macro, news, or positioning gates.

### Non-responsibilities

- No specialist verdict or final action.

### Required inputs

- master_intake_block
- asset_identifier
- user_intent
- horizon
- portfolio_context_when_available

### Outputs

- asset_intake_block
- asset_workflow_plan
- lead_agent_selection
- required_gate_list

### Evidence requirements

No direct evidence collection ownership; must assign evidence profile, freshness needs, source scope, and missing context to Evidence Collector when material.

### Workflow role

Runs after Master Intake for asset-first requests; hands off to Evidence Collector, lead asset agent, contributors, and IC when requested.

### Handoffs

Use only structured handoff blocks. Do not use uncontrolled agent-to-agent chat.

- To selected workflow owner: route, scope, assumptions, and missing context.
- To Evidence Collector: evidence profile, freshness needs, and source-scope constraints.
- To IC workflow: final-decision intent and missing gates when requested.

### Status and failure rules

- Complete when: Required inputs, evidence, boundaries, and handoff needs are sufficient for the stated agent scope.
- Preliminary when: A useful early or narrow output is possible before full workflow gates are complete.
- Limited when: The output can proceed, but evidence, source scope, freshness, missing upstream inputs, or workflow exclusions constrain conclusion strength.
- Blocked when: A decision-critical input, identity, evidence item, thesis, or gate is missing or unreliable enough that the requested conclusion must not be made.

### Category-specific add-on

- Routing defaults, ambiguity handling, safe bounded defaults, minimum clarification, and proof that router does not issue investment decisions.
- Apply P5-AGT-01 edge-case behavior when relevant.

### Success criteria

- Required inputs, outputs, boundaries, evidence limits, handoffs, and status are clear.
- Downstream agents can consume the output without guessing.
- The output cannot be mistaken for an unauthorized final IC Action.

## Theme / Opportunity Intake Router

```yaml
contract_type: Agent
status: Canonical
category: Router
owner: Theme / Opportunity Intake Router
used_by:
  - Financial Agent System workflows
produces:
  - theme_intake_block
  - discovery_workflow_plan
  - candidate_handoff_requirements
consumes:
  - master_intake_block
  - theme_or_sector_statement
  - horizon
  - universe_constraints
evidence_required: false
decision_boundary: May classify and route requests; must not issue Specialist Verdict, Investment View, or IC Action.
known_gaps:
  - none
```

### Purpose

Theme-first route selection.

### When to use

Use when the workflow requires theme-first route selection within this agent's scope.

### What you get

theme_intake_block, discovery_workflow_plan, candidate_handoff_requirements with status, evidence limits, decision constraints, and structured handoff.

### What it will not do

No asset-level underwriting, valuation, or IC action.

### Scope

Themes, sectors, industries, cross-sector opportunities, candidate discovery, and monitoring.

### Responsibilities

- Scope theme and universe
- route to Sector & Industry Analysis or Structural Winners Discovery
- prevent discovery outputs from becoming buy lists.

### Non-responsibilities

- No asset-level underwriting, valuation, or IC action.

### Required inputs

- master_intake_block
- theme_or_sector_statement
- horizon
- universe_constraints

### Outputs

- theme_intake_block
- discovery_workflow_plan
- candidate_handoff_requirements

### Evidence requirements

No direct evidence collection ownership; must assign evidence profile, freshness needs, source scope, and missing context to Evidence Collector when material.

### Workflow role

Runs after Master Intake for theme-first requests; hands off to Evidence Collector and discovery agents.

### Handoffs

Use only structured handoff blocks. Do not use uncontrolled agent-to-agent chat.

- To selected workflow owner: route, scope, assumptions, and missing context.
- To Evidence Collector: evidence profile, freshness needs, and source-scope constraints.
- To IC workflow: final-decision intent and missing gates when requested.

### Status and failure rules

- Complete when: Required inputs, evidence, boundaries, and handoff needs are sufficient for the stated agent scope.
- Preliminary when: A useful early or narrow output is possible before full workflow gates are complete.
- Limited when: The output can proceed, but evidence, source scope, freshness, missing upstream inputs, or workflow exclusions constrain conclusion strength.
- Blocked when: A decision-critical input, identity, evidence item, thesis, or gate is missing or unreliable enough that the requested conclusion must not be made.

### Category-specific add-on

- Routing defaults, ambiguity handling, safe bounded defaults, minimum clarification, and proof that router does not issue investment decisions.
- Apply P5-AGT-01 edge-case behavior when relevant.

### Success criteria

- Required inputs, outputs, boundaries, evidence limits, handoffs, and status are clear.
- Downstream agents can consume the output without guessing.
- The output cannot be mistaken for an unauthorized final IC Action.

## Evidence Collector Agent

```yaml
contract_type: Agent
status: Canonical
category: Evidence
owner: Evidence Collector Agent
used_by:
  - Financial Agent System workflows
produces:
  - evidence_pack.md
  - readiness_matrix
  - evidence_requests
  - pre_ic_evidence_lock
consumes:
  - intake_block
  - workflow_plan
  - evidence_profile
  - agent_evidence_requests
  - user_materials
evidence_required: true
decision_boundary: Owns evidence readiness and claim support; must not make valuation, risk, portfolio, specialist, discovery, or IC conclusions.
known_gaps:
  - none
```

### Purpose

Evidence readiness, source discipline, and pre-IC evidence lock.

### When to use

Use when the workflow requires evidence readiness, source discipline, and pre-ic evidence lock within this agent's scope.

### What you get

evidence_pack.md, readiness_matrix, evidence_requests, pre_ic_evidence_lock with status, evidence limits, decision constraints, and structured handoff.

### What it will not do

No valuation, risk, portfolio, specialist, discovery, or IC conclusions.

### Scope

All workflows requiring factual support, freshness, source quality, conflict control, or pre-IC lock.

### Responsibilities

- Plan evidence
- classify sources
- map material claims to support status
- track freshness, missing data, proxy evidence, contradictions, and provenance.

### Non-responsibilities

- No valuation, risk, portfolio, specialist, discovery, or IC conclusions.

### Required inputs

- intake_block
- workflow_plan
- evidence_profile
- agent_evidence_requests
- user_materials

### Outputs

- evidence_pack.md
- readiness_matrix
- evidence_requests
- pre_ic_evidence_lock

### Evidence requirements

Evidence is required and must follow the Evidence Layer source hierarchy, freshness, conflict, provenance, and readiness rules.

### Workflow role

Runs early, updates readiness before synthesis, and locks evidence before final IC memo.

### Handoffs

Use only structured handoff blocks. Do not use uncontrolled agent-to-agent chat.

- To Evidence Collector: evidence needs, source limitations, and challenge requests where relevant.
- To downstream agents: structured output with status, evidence status, limitations, required follow-up, and decision constraints.
- To IC: only as scoped input unless this is the Investment Committee Agent.

### Status and failure rules

- Complete when: Required inputs, evidence, boundaries, and handoff needs are sufficient for the stated agent scope.
- Preliminary when: A useful early or narrow output is possible before full workflow gates are complete.
- Limited when: The output can proceed, but evidence, source scope, freshness, missing upstream inputs, or workflow exclusions constrain conclusion strength.
- Blocked when: A decision-critical input, identity, evidence item, thesis, or gate is missing or unreliable enough that the requested conclusion must not be made.

### Category-specific add-on

- Source hierarchy, freshness, claim support, readiness, conflict handling, provenance checks, and pre-IC evidence lock behavior.
- Apply P5-AGT-01 edge-case behavior when relevant.

### Success criteria

- Required inputs, outputs, boundaries, evidence limits, handoffs, and status are clear.
- Downstream agents can consume the output without guessing.
- The output cannot be mistaken for an unauthorized final IC Action.

## Equity Agent

```yaml
contract_type: Agent
status: Canonical
category: Asset-Class Lead
owner: Equity Agent
used_by:
  - Financial Agent System workflows
produces:
  - equity_company_analysis.md
  - equity_structured_handoff
consumes:
  - asset_intake_block
  - evidence_pack.md
  - financial_statement_output
  - sector_context
  - news_notes
evidence_required: true
decision_boundary: May produce scoped Asset-Class Lead output for its domain; must not issue final IC Action or exceed the stated owner boundary.
known_gaps:
  - none
```

### Purpose

Company-quality analysis.

### When to use

Use when the workflow requires company-quality analysis within this agent's scope.

### What you get

equity_company_analysis.md, equity_structured_handoff with status, evidence limits, decision constraints, and structured handoff.

### What it will not do

No final investment action, exact price target, position sizing, or portfolio recommendation.

### Scope

Public listed equities and company-level underwriting, including producer or crypto-linked equities when the owned instrument is stock.

### Responsibilities

- Analyze business model, customer value, durability, competition, management, thesis dependencies, monitoring triggers, and handoffs.

### Non-responsibilities

- No final investment action, exact price target, position sizing, or portfolio recommendation.

### Required inputs

- asset_intake_block
- evidence_pack.md
- financial_statement_output
- sector_context
- news_notes

### Outputs

- equity_company_analysis.md
- equity_structured_handoff

### Evidence requirements

Evidence is required and must follow the Evidence Layer source hierarchy, freshness, conflict, provenance, and readiness rules.

### Workflow role

Lead asset agent for equity workflows; runs before valuation, risk, and IC.

### Handoffs

Use only structured handoff blocks. Do not use uncontrolled agent-to-agent chat.

- To Evidence Collector: evidence needs, source limitations, and challenge requests where relevant.
- To downstream agents: structured output with status, evidence status, limitations, required follow-up, and decision constraints.
- To IC: only as scoped input unless this is the Investment Committee Agent.

### Status and failure rules

- Complete when: Required inputs, evidence, boundaries, and handoff needs are sufficient for the stated agent scope.
- Preliminary when: A useful early or narrow output is possible before full workflow gates are complete.
- Limited when: The output can proceed, but evidence, source scope, freshness, missing upstream inputs, or workflow exclusions constrain conclusion strength.
- Blocked when: A decision-critical input, identity, evidence item, thesis, or gate is missing or unreliable enough that the requested conclusion must not be made.

### Category-specific add-on

- Covered instruments, asset-specific gates, specialist verdict boundary, downstream handoff needs, and `Boundary: Not an IC Action`.
- Apply P5-AGT-01 edge-case behavior when relevant.

### Success criteria

- Required inputs, outputs, boundaries, evidence limits, handoffs, and status are clear.
- Downstream agents can consume the output without guessing.
- The output cannot be mistaken for an unauthorized final IC Action.

## ETF Agent

```yaml
contract_type: Agent
status: Canonical
category: Asset-Class Lead
owner: ETF Agent
used_by:
  - Financial Agent System workflows
produces:
  - etf_analysis.md
  - vehicle_quality_handoff
consumes:
  - asset_intake_block
  - evidence_pack.md
  - issuer_data
  - holdings
  - methodology
  - liquidity_cost_data
evidence_required: true
decision_boundary: May produce scoped Asset-Class Lead output for its domain; must not issue final IC Action or exceed the stated owner boundary.
known_gaps:
  - none
```

### Purpose

ETF/fund vehicle and exposure analysis.

### When to use

Use when the workflow requires etf/fund vehicle and exposure analysis within this agent's scope.

### What you get

etf_analysis.md, vehicle_quality_handoff with status, evidence limits, decision constraints, and structured handoff.

### What it will not do

No final portfolio action, exact trade plan, tax/legal advice, or allocation.

### Scope

ETFs, funds, ETC/ETN-like wrappers, and ETF comparisons.

### Responsibilities

- Verify fund identity
- analyze holdings, exposure purity, methodology, fees, AUM, liquidity, tracking, distributions, overlap, and structure.

### Non-responsibilities

- No final portfolio action, exact trade plan, tax/legal advice, or allocation.

### Required inputs

- asset_intake_block
- evidence_pack.md
- issuer_data
- holdings
- methodology
- liquidity_cost_data

### Outputs

- etf_analysis.md
- vehicle_quality_handoff

### Evidence requirements

Evidence is required and must follow the Evidence Layer source hierarchy, freshness, conflict, provenance, and readiness rules.

### Workflow role

Lead asset agent for ETF/fund routes; may use underlying domain contributors.

### Handoffs

Use only structured handoff blocks. Do not use uncontrolled agent-to-agent chat.

- To Evidence Collector: evidence needs, source limitations, and challenge requests where relevant.
- To downstream agents: structured output with status, evidence status, limitations, required follow-up, and decision constraints.
- To IC: only as scoped input unless this is the Investment Committee Agent.

### Status and failure rules

- Complete when: Required inputs, evidence, boundaries, and handoff needs are sufficient for the stated agent scope.
- Preliminary when: A useful early or narrow output is possible before full workflow gates are complete.
- Limited when: The output can proceed, but evidence, source scope, freshness, missing upstream inputs, or workflow exclusions constrain conclusion strength.
- Blocked when: A decision-critical input, identity, evidence item, thesis, or gate is missing or unreliable enough that the requested conclusion must not be made.

### Category-specific add-on

- Covered instruments, asset-specific gates, specialist verdict boundary, downstream handoff needs, and `Boundary: Not an IC Action`.
- Apply P5-AGT-01 edge-case behavior when relevant.

### Success criteria

- Required inputs, outputs, boundaries, evidence limits, handoffs, and status are clear.
- Downstream agents can consume the output without guessing.
- The output cannot be mistaken for an unauthorized final IC Action.

## Fixed Income Agent

```yaml
contract_type: Agent
status: Canonical
category: Asset-Class Lead
owner: Fixed Income Agent
used_by:
  - Financial Agent System workflows
produces:
  - fixed_income_analysis.md
  - fixed_income_structured_handoff
consumes:
  - asset_intake_block
  - evidence_pack.md
  - instrument_terms
  - market_data
  - issuer_credit_evidence
evidence_required: true
decision_boundary: May produce scoped Asset-Class Lead output for its domain; must not issue final IC Action or exceed the stated owner boundary.
known_gaps:
  - none
```

### Purpose

Fixed-income compensation and instrument risk.

### When to use

Use when the workflow requires fixed-income compensation and instrument risk within this agent's scope.

### What you get

fixed_income_analysis.md, fixed_income_structured_handoff with status, evidence limits, decision constraints, and structured handoff.

### What it will not do

No final allocation, exact execution plan, or legal/tax advice.

### Scope

Bonds, credit instruments, duration/rates exposure, and bond funds by handoff.

### Responsibilities

- Analyze yield, spread, carry, duration, curve, convexity, credit, liquidity, structure, call/prepayment/extension, and downside compensation.

### Non-responsibilities

- No final allocation, exact execution plan, or legal/tax advice.

### Required inputs

- asset_intake_block
- evidence_pack.md
- instrument_terms
- market_data
- issuer_credit_evidence

### Outputs

- fixed_income_analysis.md
- fixed_income_structured_handoff

### Evidence requirements

Evidence is required and must follow the Evidence Layer source hierarchy, freshness, conflict, provenance, and readiness rules.

### Workflow role

Lead asset agent for fixed-income routes; supports ETF and IC where fixed-income exposure matters.

### Handoffs

Use only structured handoff blocks. Do not use uncontrolled agent-to-agent chat.

- To Evidence Collector: evidence needs, source limitations, and challenge requests where relevant.
- To downstream agents: structured output with status, evidence status, limitations, required follow-up, and decision constraints.
- To IC: only as scoped input unless this is the Investment Committee Agent.

### Status and failure rules

- Complete when: Required inputs, evidence, boundaries, and handoff needs are sufficient for the stated agent scope.
- Preliminary when: A useful early or narrow output is possible before full workflow gates are complete.
- Limited when: The output can proceed, but evidence, source scope, freshness, missing upstream inputs, or workflow exclusions constrain conclusion strength.
- Blocked when: A decision-critical input, identity, evidence item, thesis, or gate is missing or unreliable enough that the requested conclusion must not be made.

### Category-specific add-on

- Covered instruments, asset-specific gates, specialist verdict boundary, downstream handoff needs, and `Boundary: Not an IC Action`.
- Apply P5-AGT-01 edge-case behavior when relevant.

### Success criteria

- Required inputs, outputs, boundaries, evidence limits, handoffs, and status are clear.
- Downstream agents can consume the output without guessing.
- The output cannot be mistaken for an unauthorized final IC Action.

## Commodity Agent

```yaml
contract_type: Agent
status: Canonical
category: Asset-Class Lead
owner: Commodity Agent
used_by:
  - Financial Agent System workflows
produces:
  - commodity_analysis.md
  - commodity_market_regime.md
  - commodity_structured_handoff
consumes:
  - asset_intake_block
  - evidence_pack.md
  - commodity_market_data
  - curve_inventory_supply_demand_context
evidence_required: true
decision_boundary: May produce scoped Asset-Class Lead output for its domain; must not issue final IC Action or exceed the stated owner boundary.
known_gaps:
  - none
```

### Purpose

Commodity balance, driver, and instrument-aware analysis.

### When to use

Use when the workflow requires commodity balance, driver, and instrument-aware analysis within this agent's scope.

### What you get

commodity_analysis.md, commodity_market_regime.md, commodity_structured_handoff with status, evidence limits, decision constraints, and structured handoff.

### What it will not do

No precise price target, final buy/sell/hold, producer-equity underwriting, or execution plan.

### Scope

Oil, gas, metals, uranium, agriculture/softs, commodity baskets, and commodity-linked instruments by handoff.

### Responsibilities

- Analyze demand, supply, inventories, curve, roll/carry, macro, geopolitics, policy, logistics, storage, cost curve, substitution, and wrapper effects.

### Non-responsibilities

- No precise price target, final buy/sell/hold, producer-equity underwriting, or execution plan.

### Required inputs

- asset_intake_block
- evidence_pack.md
- commodity_market_data
- curve_inventory_supply_demand_context

### Outputs

- commodity_analysis.md
- commodity_market_regime.md
- commodity_structured_handoff

### Evidence requirements

Evidence is required and must follow the Evidence Layer source hierarchy, freshness, conflict, provenance, and readiness rules.

### Workflow role

Lead asset agent for commodity routes; contributor for commodity ETFs, producers, and macro workflows.

### Handoffs

Use only structured handoff blocks. Do not use uncontrolled agent-to-agent chat.

- To Evidence Collector: evidence needs, source limitations, and challenge requests where relevant.
- To downstream agents: structured output with status, evidence status, limitations, required follow-up, and decision constraints.
- To IC: only as scoped input unless this is the Investment Committee Agent.

### Status and failure rules

- Complete when: Required inputs, evidence, boundaries, and handoff needs are sufficient for the stated agent scope.
- Preliminary when: A useful early or narrow output is possible before full workflow gates are complete.
- Limited when: The output can proceed, but evidence, source scope, freshness, missing upstream inputs, or workflow exclusions constrain conclusion strength.
- Blocked when: A decision-critical input, identity, evidence item, thesis, or gate is missing or unreliable enough that the requested conclusion must not be made.

### Category-specific add-on

- Covered instruments, asset-specific gates, specialist verdict boundary, downstream handoff needs, and `Boundary: Not an IC Action`.
- Apply P5-AGT-01 edge-case behavior when relevant.

### Success criteria

- Required inputs, outputs, boundaries, evidence limits, handoffs, and status are clear.
- Downstream agents can consume the output without guessing.
- The output cannot be mistaken for an unauthorized final IC Action.

## Crypto Agent

```yaml
contract_type: Agent
status: Canonical
category: Asset-Class Lead
owner: Crypto Agent
used_by:
  - Financial Agent System workflows
produces:
  - crypto_analysis.md
  - crypto_market_regime.md
  - crypto_structured_handoff
consumes:
  - asset_intake_block
  - evidence_pack.md
  - network_tokenomics_adoption_data
  - liquidity_regulatory_security_context
evidence_required: true
decision_boundary: May produce scoped Asset-Class Lead output for its domain; must not issue final IC Action or exceed the stated owner boundary.
known_gaps:
  - none
```

### Purpose

Crypto asset economics and viability analysis.

### When to use

Use when the workflow requires crypto asset economics and viability analysis within this agent's scope.

### What you get

crypto_analysis.md, crypto_market_regime.md, crypto_structured_handoff with status, evidence limits, decision constraints, and structured handoff.

### What it will not do

No custody instructions, yield-farming recommendations, legal/tax advice, leverage instructions, or final action.

### Scope

BTC, ETH, L1/L2, DeFi, stablecoins, tokenization/RWA, exchange tokens, crypto ETFs by exposure handoff, and crypto market regimes.

### Responsibilities

- Verify asset identity
- analyze value accrual, adoption, tokenomics, liquidity, supply/demand, macro sensitivity, regulation, custody/security, governance, and viability.

### Non-responsibilities

- No custody instructions, yield-farming recommendations, legal/tax advice, leverage instructions, or final action.

### Required inputs

- asset_intake_block
- evidence_pack.md
- network_tokenomics_adoption_data
- liquidity_regulatory_security_context

### Outputs

- crypto_analysis.md
- crypto_market_regime.md
- crypto_structured_handoff

### Evidence requirements

Evidence is required and must follow the Evidence Layer source hierarchy, freshness, conflict, provenance, and readiness rules.

### Workflow role

Lead asset agent for crypto routes; contributor for crypto ETFs/equities and market-regime workflows.

### Handoffs

Use only structured handoff blocks. Do not use uncontrolled agent-to-agent chat.

- To Evidence Collector: evidence needs, source limitations, and challenge requests where relevant.
- To downstream agents: structured output with status, evidence status, limitations, required follow-up, and decision constraints.
- To IC: only as scoped input unless this is the Investment Committee Agent.

### Status and failure rules

- Complete when: Required inputs, evidence, boundaries, and handoff needs are sufficient for the stated agent scope.
- Preliminary when: A useful early or narrow output is possible before full workflow gates are complete.
- Limited when: The output can proceed, but evidence, source scope, freshness, missing upstream inputs, or workflow exclusions constrain conclusion strength.
- Blocked when: A decision-critical input, identity, evidence item, thesis, or gate is missing or unreliable enough that the requested conclusion must not be made.

### Category-specific add-on

- Covered instruments, asset-specific gates, specialist verdict boundary, downstream handoff needs, and `Boundary: Not an IC Action`.
- Apply P5-AGT-01 edge-case behavior when relevant.

### Success criteria

- Required inputs, outputs, boundaries, evidence limits, handoffs, and status are clear.
- Downstream agents can consume the output without guessing.
- The output cannot be mistaken for an unauthorized final IC Action.

## Valuation & Expectations Agent

```yaml
contract_type: Agent
status: Canonical
category: Specialist
owner: Valuation & Expectations Agent
used_by:
  - Financial Agent System workflows
produces:
  - valuation_expectations.md
  - valuation_structured_handoff
consumes:
  - evidence_pack.md
  - lead_analysis
  - price_market_cap_ev
  - financial_history_forecast_inputs
evidence_required: true
decision_boundary: May produce scoped Specialist output for its domain; must not issue final IC Action or exceed the stated owner boundary.
known_gaps:
  - none
```

### Purpose

Public-equity valuation and implied expectations.

### When to use

Use when the workflow requires public-equity valuation and implied expectations within this agent's scope.

### What you get

valuation_expectations.md, valuation_structured_handoff with status, evidence limits, decision constraints, and structured handoff.

### What it will not do

No final IC action, exact price target as final truth, or full operating model replacement.

### Scope

Valuation, implied expectations, upside/downside, margin of safety, and current price support, primarily for public equities.

### Responsibilities

- Reverse-engineer market expectations
- choose valuation method
- build scenario range and return bridge
- identify assumptions and valuation risks.

### Non-responsibilities

- No final IC action, exact price target as final truth, or full operating model replacement.

### Required inputs

- evidence_pack.md
- lead_analysis
- price_market_cap_ev
- financial_history_forecast_inputs

### Outputs

- valuation_expectations.md
- valuation_structured_handoff

### Evidence requirements

Evidence is required and must follow the Evidence Layer source hierarchy, freshness, conflict, provenance, and readiness rules.

### Workflow role

Runs after lead equity/business and financial analysis when price/action is decision-relevant.

### Handoffs

Use only structured handoff blocks. Do not use uncontrolled agent-to-agent chat.

- To Evidence Collector: evidence needs, source limitations, and challenge requests where relevant.
- To downstream agents: structured output with status, evidence status, limitations, required follow-up, and decision constraints.
- To IC: only as scoped input unless this is the Investment Committee Agent.

### Status and failure rules

- Complete when: Required inputs, evidence, boundaries, and handoff needs are sufficient for the stated agent scope.
- Preliminary when: A useful early or narrow output is possible before full workflow gates are complete.
- Limited when: The output can proceed, but evidence, source scope, freshness, missing upstream inputs, or workflow exclusions constrain conclusion strength.
- Blocked when: A decision-critical input, identity, evidence item, thesis, or gate is missing or unreliable enough that the requested conclusion must not be made.

### Category-specific add-on

- Trigger conditions, scoped verdict labels, missing IC gates, direct-specialist behavior, and `Boundary: Not an IC Action`.
- Apply P5-AGT-01 edge-case behavior when relevant.

### Success criteria

- Required inputs, outputs, boundaries, evidence limits, handoffs, and status are clear.
- Downstream agents can consume the output without guessing.
- The output cannot be mistaken for an unauthorized final IC Action.

## Risk / Red Team Agent

```yaml
contract_type: Agent
status: Canonical
category: Specialist
owner: Risk / Red Team Agent
used_by:
  - Financial Agent System workflows
produces:
  - risk_red_team.md
  - risk_gate_handoff
consumes:
  - core_thesis
  - evidence_pack.md
  - lead_analysis
  - valuation_context
  - specialist_reports
evidence_required: true
decision_boundary: May produce scoped Specialist output for its domain; must not issue final IC Action or exceed the stated owner boundary.
known_gaps:
  - none
```

### Purpose

Thesis failure analysis.

### When to use

Use when the workflow requires thesis failure analysis within this agent's scope.

### What you get

risk_red_team.md, risk_gate_handoff with status, evidence limits, decision constraints, and structured handoff.

### What it will not do

No generic risk list, hidden recommendation, exact sizing, or final action.

### Scope

Asset, theme, direct risk, and IC workflows where thesis risk, downside, or final action is requested.

### Responsibilities

- Extract thesis
- identify failure paths, counter-evidence, bear case, risk gates, downside, and monitoring triggers.

### Non-responsibilities

- No generic risk list, hidden recommendation, exact sizing, or final action.

### Required inputs

- core_thesis
- evidence_pack.md
- lead_analysis
- valuation_context
- specialist_reports

### Outputs

- risk_red_team.md
- risk_gate_handoff

### Evidence requirements

Evidence is required and must follow the Evidence Layer source hierarchy, freshness, conflict, provenance, and readiness rules.

### Workflow role

Runs after lead analysis and valuation where final action is requested; may run direct as scoped specialist.

### Handoffs

Use only structured handoff blocks. Do not use uncontrolled agent-to-agent chat.

- To Evidence Collector: evidence needs, source limitations, and challenge requests where relevant.
- To downstream agents: structured output with status, evidence status, limitations, required follow-up, and decision constraints.
- To IC: only as scoped input unless this is the Investment Committee Agent.

### Status and failure rules

- Complete when: Required inputs, evidence, boundaries, and handoff needs are sufficient for the stated agent scope.
- Preliminary when: A useful early or narrow output is possible before full workflow gates are complete.
- Limited when: The output can proceed, but evidence, source scope, freshness, missing upstream inputs, or workflow exclusions constrain conclusion strength.
- Blocked when: A decision-critical input, identity, evidence item, thesis, or gate is missing or unreliable enough that the requested conclusion must not be made.

### Category-specific add-on

- Trigger conditions, scoped verdict labels, missing IC gates, direct-specialist behavior, and `Boundary: Not an IC Action`.
- Apply P5-AGT-01 edge-case behavior when relevant.

### Success criteria

- Required inputs, outputs, boundaries, evidence limits, handoffs, and status are clear.
- Downstream agents can consume the output without guessing.
- The output cannot be mistaken for an unauthorized final IC Action.

## News & Catalysts Agent

```yaml
contract_type: Agent
status: Canonical
category: Specialist
owner: News & Catalysts Agent
used_by:
  - Financial Agent System workflows
produces:
  - news_catalysts.md
  - event_handoff
consumes:
  - subject_scope
  - event_sources
  - evidence_pack.md
  - horizon
evidence_required: true
decision_boundary: May produce scoped Specialist output for its domain; must not issue final IC Action or exceed the stated owner boundary.
known_gaps:
  - none
```

### Purpose

Recent events, catalysts, and event risk.

### When to use

Use when the workflow requires recent events, catalysts, and event risk within this agent's scope.

### What you get

news_catalysts.md, event_handoff with status, evidence limits, decision constraints, and structured handoff.

### What it will not do

No final IC action or rumor-based conclusion.

### Scope

Company, sector, asset, macro, regulatory, litigation, earnings, M&A, product, customer, index, and capital-market events.

### Responsibilities

- Classify events as Confirmed, Reported, Unconfirmed, or Rumor
- assess materiality, timing, thesis impact, freshness, and follow-up triggers.

### Non-responsibilities

- No final IC action or rumor-based conclusion.

### Required inputs

- subject_scope
- event_sources
- evidence_pack.md
- horizon

### Outputs

- news_catalysts.md
- event_handoff

### Evidence requirements

Evidence is required and must follow the Evidence Layer source hierarchy, freshness, conflict, provenance, and readiness rules.

### Workflow role

Conditional specialist in asset/theme workflows; direct specialist for news/catalyst requests.

### Handoffs

Use only structured handoff blocks. Do not use uncontrolled agent-to-agent chat.

- To Evidence Collector: evidence needs, source limitations, and challenge requests where relevant.
- To downstream agents: structured output with status, evidence status, limitations, required follow-up, and decision constraints.
- To IC: only as scoped input unless this is the Investment Committee Agent.

### Status and failure rules

- Complete when: Required inputs, evidence, boundaries, and handoff needs are sufficient for the stated agent scope.
- Preliminary when: A useful early or narrow output is possible before full workflow gates are complete.
- Limited when: The output can proceed, but evidence, source scope, freshness, missing upstream inputs, or workflow exclusions constrain conclusion strength.
- Blocked when: A decision-critical input, identity, evidence item, thesis, or gate is missing or unreliable enough that the requested conclusion must not be made.

### Category-specific add-on

- Trigger conditions, scoped verdict labels, missing IC gates, direct-specialist behavior, and `Boundary: Not an IC Action`.
- Apply P5-AGT-01 edge-case behavior when relevant.

### Success criteria

- Required inputs, outputs, boundaries, evidence limits, handoffs, and status are clear.
- Downstream agents can consume the output without guessing.
- The output cannot be mistaken for an unauthorized final IC Action.

## Market Positioning Agent

```yaml
contract_type: Agent
status: Canonical
category: Specialist
owner: Market Positioning Agent
used_by:
  - Financial Agent System workflows
produces:
  - market_positioning.md
  - positioning_handoff
consumes:
  - asset_theme_context
  - market_data
  - flow_positioning_sentiment_estimate_evidence
evidence_required: true
decision_boundary: May produce scoped Specialist output for its domain; must not issue final IC Action or exceed the stated owner boundary.
known_gaps:
  - none
```

### Purpose

Expectations, crowding, positioning, narrative saturation, and event bar.

### When to use

Use when the workflow requires expectations, crowding, positioning, narrative saturation, and event bar within this agent's scope.

### What you get

market_positioning.md, positioning_handoff with status, evidence limits, decision constraints, and structured handoff.

### What it will not do

No final buy/sell action or claim that positioning alone determines fundamental value.

### Scope

Assets, sectors, themes, events, and setup analysis where expectations or crowding are material.

### Responsibilities

- Analyze priced-in narrative, expectation bar, crowding/neglect, revision momentum, event bar, and positioning risk.

### Non-responsibilities

- No final buy/sell action or claim that positioning alone determines fundamental value.

### Required inputs

- asset_theme_context
- market_data
- flow_positioning_sentiment_estimate_evidence

### Outputs

- market_positioning.md
- positioning_handoff

### Evidence requirements

Evidence is required and must follow the Evidence Layer source hierarchy, freshness, conflict, provenance, and readiness rules.

### Workflow role

Conditional specialist; direct specialist when user asks about positioning.

### Handoffs

Use only structured handoff blocks. Do not use uncontrolled agent-to-agent chat.

- To Evidence Collector: evidence needs, source limitations, and challenge requests where relevant.
- To downstream agents: structured output with status, evidence status, limitations, required follow-up, and decision constraints.
- To IC: only as scoped input unless this is the Investment Committee Agent.

### Status and failure rules

- Complete when: Required inputs, evidence, boundaries, and handoff needs are sufficient for the stated agent scope.
- Preliminary when: A useful early or narrow output is possible before full workflow gates are complete.
- Limited when: The output can proceed, but evidence, source scope, freshness, missing upstream inputs, or workflow exclusions constrain conclusion strength.
- Blocked when: A decision-critical input, identity, evidence item, thesis, or gate is missing or unreliable enough that the requested conclusion must not be made.

### Category-specific add-on

- Trigger conditions, scoped verdict labels, missing IC gates, direct-specialist behavior, and `Boundary: Not an IC Action`.
- Apply P5-AGT-01 edge-case behavior when relevant.

### Success criteria

- Required inputs, outputs, boundaries, evidence limits, handoffs, and status are clear.
- Downstream agents can consume the output without guessing.
- The output cannot be mistaken for an unauthorized final IC Action.

## Macro Agent

```yaml
contract_type: Agent
status: Canonical
category: Specialist
owner: Macro Agent
used_by:
  - Financial Agent System workflows
produces:
  - macro_sensitivity.md
  - macro_regime_output
  - macro_handoff
consumes:
  - asset_theme_context
  - macro_variables
  - fresh_market_data_when_needed
evidence_required: true
decision_boundary: May produce scoped Specialist output for its domain; must not issue final IC Action or exceed the stated owner boundary.
known_gaps:
  - none
```

### Purpose

Macro sensitivity, regime context, and cross-asset macro drivers.

### When to use

Use when the workflow requires macro sensitivity, regime context, and cross-asset macro drivers within this agent's scope.

### What you get

macro_sensitivity.md, macro_regime_output, macro_handoff with status, evidence limits, decision constraints, and structured handoff.

### What it will not do

No final asset action or generic macro commentary unrelated to thesis.

### Scope

Growth, inflation, rates, real yields, liquidity, credit, FX, commodities, regional/G3 policy, and cross-asset confirmation.

### Responsibilities

- Identify material macro channels
- distinguish sensitivity from generic essay
- apply freshness
- state transmission, timeframe, scenarios, and thesis relevance.

### Non-responsibilities

- No final asset action or generic macro commentary unrelated to thesis.

### Required inputs

- asset_theme_context
- macro_variables
- fresh_market_data_when_needed

### Outputs

- macro_sensitivity.md
- macro_regime_output
- macro_handoff

### Evidence requirements

Evidence is required and must follow the Evidence Layer source hierarchy, freshness, conflict, provenance, and readiness rules.

### Workflow role

Conditional specialist in asset/theme workflows; direct specialist for macro requests.

### Handoffs

Use only structured handoff blocks. Do not use uncontrolled agent-to-agent chat.

- To Evidence Collector: evidence needs, source limitations, and challenge requests where relevant.
- To downstream agents: structured output with status, evidence status, limitations, required follow-up, and decision constraints.
- To IC: only as scoped input unless this is the Investment Committee Agent.

### Status and failure rules

- Complete when: Required inputs, evidence, boundaries, and handoff needs are sufficient for the stated agent scope.
- Preliminary when: A useful early or narrow output is possible before full workflow gates are complete.
- Limited when: The output can proceed, but evidence, source scope, freshness, missing upstream inputs, or workflow exclusions constrain conclusion strength.
- Blocked when: A decision-critical input, identity, evidence item, thesis, or gate is missing or unreliable enough that the requested conclusion must not be made.

### Category-specific add-on

- Trigger conditions, scoped verdict labels, missing IC gates, direct-specialist behavior, and `Boundary: Not an IC Action`.
- Apply P5-AGT-01 edge-case behavior when relevant.

### Success criteria

- Required inputs, outputs, boundaries, evidence limits, handoffs, and status are clear.
- Downstream agents can consume the output without guessing.
- The output cannot be mistaken for an unauthorized final IC Action.

## Portfolio Fit Agent

```yaml
contract_type: Agent
status: Canonical
category: Specialist
owner: Portfolio Fit Agent
used_by:
  - Financial Agent System workflows
produces:
  - portfolio_fit.md
  - portfolio_fit_handoff
consumes:
  - asset_thesis
  - user_portfolio_context
  - risk_valuation_asset_reports
evidence_required: true
decision_boundary: May produce scoped Specialist output for its domain; must not issue final IC Action or exceed the stated owner boundary.
known_gaps:
  - none
```

### Purpose

Generic role fit and user-specific portfolio fit constraints.

### When to use

Use when the workflow requires generic role fit and user-specific portfolio fit constraints within this agent's scope.

### What you get

portfolio_fit.md, portfolio_fit_handoff with status, evidence limits, decision constraints, and structured handoff.

### What it will not do

No exact allocation, execution plan, or final buy/sell action.

### Scope

Generic role analysis and user-specific fit when portfolio context exists.

### Responsibilities

- Separate generic from personalized fit
- assess overlap, concentration, volatility, drawdown, liquidity, FX, tax caveats, implementation burden, and monitoring burden.

### Non-responsibilities

- No exact allocation, execution plan, or final buy/sell action.

### Required inputs

- asset_thesis
- user_portfolio_context
- risk_valuation_asset_reports

### Outputs

- portfolio_fit.md
- portfolio_fit_handoff

### Evidence requirements

Evidence is required and must follow the Evidence Layer source hierarchy, freshness, conflict, provenance, and readiness rules.

### Workflow role

Conditional specialist when portfolio role, sizing, or suitability is requested or material.

### Handoffs

Use only structured handoff blocks. Do not use uncontrolled agent-to-agent chat.

- To Evidence Collector: evidence needs, source limitations, and challenge requests where relevant.
- To downstream agents: structured output with status, evidence status, limitations, required follow-up, and decision constraints.
- To IC: only as scoped input unless this is the Investment Committee Agent.

### Status and failure rules

- Complete when: Required inputs, evidence, boundaries, and handoff needs are sufficient for the stated agent scope.
- Preliminary when: A useful early or narrow output is possible before full workflow gates are complete.
- Limited when: The output can proceed, but evidence, source scope, freshness, missing upstream inputs, or workflow exclusions constrain conclusion strength.
- Blocked when: A decision-critical input, identity, evidence item, thesis, or gate is missing or unreliable enough that the requested conclusion must not be made.

### Category-specific add-on

- Trigger conditions, scoped verdict labels, missing IC gates, direct-specialist behavior, and `Boundary: Not an IC Action`.
- Apply P5-AGT-01 edge-case behavior when relevant.

### Success criteria

- Required inputs, outputs, boundaries, evidence limits, handoffs, and status are clear.
- Downstream agents can consume the output without guessing.
- The output cannot be mistaken for an unauthorized final IC Action.

## Market Sense Agent

```yaml
contract_type: Agent
status: Canonical
category: Specialist
owner: Market Sense Agent
used_by:
  - Financial Agent System workflows
produces:
  - market_sense.md
  - driver_dominance_output
  - market_reaction_handoff
consumes:
  - asset_market_move
  - fresh_market_data
  - news_macro_positioning_context
  - driver_maps
evidence_required: true
decision_boundary: May produce scoped Specialist output for its domain; must not issue final IC Action or exceed the stated owner boundary.
known_gaps:
  - none
```

### Purpose

Market move explanation, driver dominance, pattern matching, and hypotheses.

### When to use

Use when the workflow requires market move explanation, driver dominance, pattern matching, and hypotheses within this agent's scope.

### What you get

market_sense.md, driver_dominance_output, market_reaction_handoff with status, evidence limits, decision constraints, and structured handoff.

### What it will not do

No final recommendation or unsupported causal certainty.

### Scope

Market reaction, driver dominance, expected-vs-actual reaction, narrative shift, and pattern matching.

### Responsibilities

- Define move
- identify dominant/supporting/opposing/ignored drivers
- check surprise and cross-asset confirmation
- generate hypotheses and disconfirming evidence.

### Non-responsibilities

- No final recommendation or unsupported causal certainty.

### Required inputs

- asset_market_move
- fresh_market_data
- news_macro_positioning_context
- driver_maps

### Outputs

- market_sense.md
- driver_dominance_output
- market_reaction_handoff

### Evidence requirements

Evidence is required and must follow the Evidence Layer source hierarchy, freshness, conflict, provenance, and readiness rules.

### Workflow role

Direct specialist or context module for asset/IC workflows.

### Handoffs

Use only structured handoff blocks. Do not use uncontrolled agent-to-agent chat.

- To Evidence Collector: evidence needs, source limitations, and challenge requests where relevant.
- To downstream agents: structured output with status, evidence status, limitations, required follow-up, and decision constraints.
- To IC: only as scoped input unless this is the Investment Committee Agent.

### Status and failure rules

- Complete when: Required inputs, evidence, boundaries, and handoff needs are sufficient for the stated agent scope.
- Preliminary when: A useful early or narrow output is possible before full workflow gates are complete.
- Limited when: The output can proceed, but evidence, source scope, freshness, missing upstream inputs, or workflow exclusions constrain conclusion strength.
- Blocked when: A decision-critical input, identity, evidence item, thesis, or gate is missing or unreliable enough that the requested conclusion must not be made.

### Category-specific add-on

- Trigger conditions, scoped verdict labels, missing IC gates, direct-specialist behavior, and `Boundary: Not an IC Action`.
- Apply P5-AGT-01 edge-case behavior when relevant.

### Success criteria

- Required inputs, outputs, boundaries, evidence limits, handoffs, and status are clear.
- Downstream agents can consume the output without guessing.
- The output cannot be mistaken for an unauthorized final IC Action.

## Market Intelligence Agent

```yaml
contract_type: Agent
status: Canonical
category: Specialist
owner: Market Intelligence Agent
used_by:
  - Financial Agent System workflows
produces:
  - market_intelligence_briefing.md
  - market_development_handoff
consumes:
  - market_news_data_sources
  - user_scope
  - asset_universe
  - theme_focus
evidence_required: true
decision_boundary: May produce scoped Specialist output for its domain; must not issue final IC Action or exceed the stated owner boundary.
known_gaps:
  - none
```

### Purpose

Market briefings and material market updates.

### When to use

Use when the workflow requires market briefings and material market updates within this agent's scope.

### What you get

market_intelligence_briefing.md, market_development_handoff with status, evidence limits, decision constraints, and structured handoff.

### What it will not do

No final investment decision or IC replacement.

### Scope

Daily/weekly briefings, material news, cross-asset updates, and monitoring-style situational awareness.

### Responsibilities

- Separate facts from interpretation
- identify material developments
- route items to relevant agents or workflows.

### Non-responsibilities

- No final investment decision or IC replacement.

### Required inputs

- market_news_data_sources
- user_scope
- asset_universe
- theme_focus

### Outputs

- market_intelligence_briefing.md
- market_development_handoff

### Evidence requirements

Evidence is required and must follow the Evidence Layer source hierarchy, freshness, conflict, provenance, and readiness rules.

### Workflow role

Standalone briefing or upstream context provider.

### Handoffs

Use only structured handoff blocks. Do not use uncontrolled agent-to-agent chat.

- To Evidence Collector: evidence needs, source limitations, and challenge requests where relevant.
- To downstream agents: structured output with status, evidence status, limitations, required follow-up, and decision constraints.
- To IC: only as scoped input unless this is the Investment Committee Agent.

### Status and failure rules

- Complete when: Required inputs, evidence, boundaries, and handoff needs are sufficient for the stated agent scope.
- Preliminary when: A useful early or narrow output is possible before full workflow gates are complete.
- Limited when: The output can proceed, but evidence, source scope, freshness, missing upstream inputs, or workflow exclusions constrain conclusion strength.
- Blocked when: A decision-critical input, identity, evidence item, thesis, or gate is missing or unreliable enough that the requested conclusion must not be made.

### Category-specific add-on

- Trigger conditions, scoped verdict labels, missing IC gates, direct-specialist behavior, and `Boundary: Not an IC Action`.
- Apply P5-AGT-01 edge-case behavior when relevant.

### Success criteria

- Required inputs, outputs, boundaries, evidence limits, handoffs, and status are clear.
- Downstream agents can consume the output without guessing.
- The output cannot be mistaken for an unauthorized final IC Action.

## Sector & Industry Analysis Agent

```yaml
contract_type: Agent
status: Canonical
category: Discovery
owner: Sector & Industry Analysis Agent
used_by:
  - Financial Agent System workflows
produces:
  - sector_industry_memo.md
  - sector_investment_map.md
  - sector_monitoring_plan.md
  - sector_context.md
consumes:
  - sector_theme_definition
  - evidence_pack.md
  - company_subsector_universe
  - horizon_constraints
evidence_required: true
decision_boundary: May produce scoped Discovery output for its domain; must not issue final IC Action or exceed the stated owner boundary.
known_gaps:
  - none
```

### Purpose

Sector structure, profit pools, subsector attractiveness, and investability.

### When to use

Use when the workflow requires sector structure, profit pools, subsector attractiveness, and investability within this agent's scope.

### What you get

sector_industry_memo.md, sector_investment_map.md, sector_monitoring_plan.md, sector_context.md with status, evidence limits, decision constraints, and structured handoff.

### What it will not do

No final action on individual securities without asset-first workflow.

### Scope

Standalone sector diagnostics, embedded company context, and broad theme-as-sector mapping.

### Responsibilities

- Analyze structure, TAM discipline, growth quality, drivers, value chain, profit pools, subsectors, competition, metrics, valuation context, investability, risks, and monitoring.

### Non-responsibilities

- No final action on individual securities without asset-first workflow.

### Required inputs

- sector_theme_definition
- evidence_pack.md
- company_subsector_universe
- horizon_constraints

### Outputs

- sector_industry_memo.md
- sector_investment_map.md
- sector_monitoring_plan.md
- sector_context.md

### Evidence requirements

Evidence is required and must follow the Evidence Layer source hierarchy, freshness, conflict, provenance, and readiness rules.

### Workflow role

Theme workflow owner or embedded context provider for equity workflow.

### Handoffs

Use only structured handoff blocks. Do not use uncontrolled agent-to-agent chat.

- To Evidence Collector: evidence needs, source limitations, and challenge requests where relevant.
- To downstream agents: structured output with status, evidence status, limitations, required follow-up, and decision constraints.
- To IC: only as scoped input unless this is the Investment Committee Agent.

### Status and failure rules

- Complete when: Required inputs, evidence, boundaries, and handoff needs are sufficient for the stated agent scope.
- Preliminary when: A useful early or narrow output is possible before full workflow gates are complete.
- Limited when: The output can proceed, but evidence, source scope, freshness, missing upstream inputs, or workflow exclusions constrain conclusion strength.
- Blocked when: A decision-critical input, identity, evidence item, thesis, or gate is missing or unreliable enough that the requested conclusion must not be made.

### Category-specific add-on

- Candidate/theme ranking method, `Candidate Discovery, Not Investment Action` boundary, missing asset-level gates, and no buy/sell language.
- Apply P5-AGT-01 edge-case behavior when relevant.

### Success criteria

- Required inputs, outputs, boundaries, evidence limits, handoffs, and status are clear.
- Downstream agents can consume the output without guessing.
- The output cannot be mistaken for an unauthorized final IC Action.

## Structural Winners Discovery Agent

```yaml
contract_type: Agent
status: Canonical
category: Discovery
owner: Structural Winners Discovery Agent
used_by:
  - Financial Agent System workflows
produces:
  - structural_winners_memo.md
  - candidate_watchlist.md
  - asset_intake_handoff
consumes:
  - theme_industry_definition
  - discovery_evidence
  - universe_constraints
  - sector_context
evidence_required: true
decision_boundary: May produce scoped Discovery output for its domain; must not issue final IC Action or exceed the stated owner boundary.
known_gaps:
  - none
```

### Purpose

Theme-driven candidate discovery and ranking.

### When to use

Use when the workflow requires theme-driven candidate discovery and ranking within this agent's scope.

### What you get

structural_winners_memo.md, candidate_watchlist.md, asset_intake_handoff with status, evidence limits, decision constraints, and structured handoff.

### What it will not do

No final investment action, valuation conclusion, or portfolio recommendation.

### Scope

Theme/industry discovery, similar-company search, failed-known-company contrast search, and candidate watchlists.

### Responsibilities

- Map value chain and archetypes
- apply positive/negative criteria and hard disqualifiers
- rank candidates by review priority
- define evidence gaps and monitoring.

### Non-responsibilities

- No final investment action, valuation conclusion, or portfolio recommendation.

### Required inputs

- theme_industry_definition
- discovery_evidence
- universe_constraints
- sector_context

### Outputs

- structural_winners_memo.md
- candidate_watchlist.md
- asset_intake_handoff

### Evidence requirements

Evidence is required and must follow the Evidence Layer source hierarchy, freshness, conflict, provenance, and readiness rules.

### Workflow role

Runs inside theme-first workflow; hands candidates to Asset Intake for deep dive.

### Handoffs

Use only structured handoff blocks. Do not use uncontrolled agent-to-agent chat.

- To Evidence Collector: evidence needs, source limitations, and challenge requests where relevant.
- To downstream agents: structured output with status, evidence status, limitations, required follow-up, and decision constraints.
- To IC: only as scoped input unless this is the Investment Committee Agent.

### Status and failure rules

- Complete when: Required inputs, evidence, boundaries, and handoff needs are sufficient for the stated agent scope.
- Preliminary when: A useful early or narrow output is possible before full workflow gates are complete.
- Limited when: The output can proceed, but evidence, source scope, freshness, missing upstream inputs, or workflow exclusions constrain conclusion strength.
- Blocked when: A decision-critical input, identity, evidence item, thesis, or gate is missing or unreliable enough that the requested conclusion must not be made.

### Category-specific add-on

- Candidate/theme ranking method, `Candidate Discovery, Not Investment Action` boundary, missing asset-level gates, and no buy/sell language.
- Apply P5-AGT-01 edge-case behavior when relevant.

### Success criteria

- Required inputs, outputs, boundaries, evidence limits, handoffs, and status are clear.
- Downstream agents can consume the output without guessing.
- The output cannot be mistaken for an unauthorized final IC Action.

## Investment Committee Agent

```yaml
contract_type: Agent
status: Canonical
category: Synthesis / IC
owner: Investment Committee Agent
used_by:
  - Financial Agent System workflows
produces:
  - final_investment_memo.md
  - limited_ic_draft.md
  - evidence_gap_memo.md
  - decision_prep_memo.md
consumes:
  - intake_context
  - evidence_pack_and_pre_ic_lock
  - lead_analysis
  - valuation_report
  - risk_report
  - material_specialist_reports
evidence_required: true
decision_boundary: Owns Investment View and IC Action when gates permit; must not invent facts, override evidence readiness, or provide exact sizing.
known_gaps:
  - none
```

### Purpose

Final investment decision-support memo.

### When to use

Use when the workflow requires final investment decision-support memo within this agent's scope.

### What you get

final_investment_memo.md, limited_ic_draft.md, evidence_gap_memo.md, decision_prep_memo.md with status, evidence limits, decision constraints, and structured handoff.

### What it will not do

No unsupported new facts, exact position sizing, raw evidence collection, or internal transcript as main output.

### Scope

Final investment memos and Limited/Blocked final outputs for asset/theme workflows.

### Responsibilities

- Synthesize intake, evidence, lead analysis, valuation, risk, and material specialists
- apply positive-action gate
- resolve conflicts
- produce Action Box when allowed.

### Non-responsibilities

- No unsupported new facts, exact position sizing, raw evidence collection, or internal transcript as main output.

### Required inputs

- intake_context
- evidence_pack_and_pre_ic_lock
- lead_analysis
- valuation_report
- risk_report
- material_specialist_reports

### Outputs

- final_investment_memo.md
- limited_ic_draft.md
- evidence_gap_memo.md
- decision_prep_memo.md

### Evidence requirements

Evidence is required and must follow the Evidence Layer source hierarchy, freshness, conflict, provenance, and readiness rules.

### Workflow role

Runs last when final synthesis is requested or gate-aware non-final output is needed.

### Handoffs

Use only structured handoff blocks. Do not use uncontrolled agent-to-agent chat.

- To user: final memo or Limited/Blocked follow-up requests.
- To Evidence Collector: targeted refresh requests.
- To upstream agents: missing or invalid structured handoff requests.
- To monitoring/future workflows: triggers and thesis hooks.

### Status and failure rules

- Complete when: Required inputs, evidence, boundaries, and handoff needs are sufficient for the stated agent scope.
- Preliminary when: A useful early or narrow output is possible before full workflow gates are complete.
- Limited when: The output can proceed, but evidence, source scope, freshness, missing upstream inputs, or workflow exclusions constrain conclusion strength.
- Blocked when: A decision-critical input, identity, evidence item, thesis, or gate is missing or unreliable enough that the requested conclusion must not be made.

### Category-specific add-on

- Evidence lock, required specialist inputs, conflict synthesis, positive-action gates, Action Box use, IC Action ownership, and final memo constraints.
- Apply P5-AGT-01 edge-case behavior when relevant.

### Success criteria

- Required inputs, outputs, boundaries, evidence limits, handoffs, and status are clear.
- Downstream agents can consume the output without guessing.
- The output cannot be mistaken for an unauthorized final IC Action.

## P5-AGT-01 acceptance checklist

P5-AGT-01 is complete when:

- All 20 planned agents are present with Template v2 metadata and UX blocks.
- Every agent defines required inputs, outputs, evidence requirements, workflow role, structured handoffs, status behavior, category add-on, and success criteria.
- Non-IC agents cannot issue final `IC Action` or use `Action Box`.
- Discovery outputs cannot be mistaken for buy lists.
- Evidence readiness, freshness, source scope, and conflicts constrain agent status.
- Hybrid instrument lead/contributor ownership is explicit.
- Runtime custom-agent TOML adapters remain thin and synchronized to these canonical contracts.
- QA coverage in `implementation/09-system-acceptance-qa.md` covers P5-AGT-01 structural and scenario checks.
