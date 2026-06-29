# Canonical Skill Contracts

Status: Canonical skill-contract layer
Version: P5-SKL-01 normalized contracts

## Contract rule

Skills are repeatable analytical methods used by agents or workflows. They do not own final routing, evidence readiness, or IC action. The only gated exception is the Investment Committee Synthesis Method Skill when the Investment Committee Agent applies evidence lock and required IC gates. Every skill below follows Template v2 from `implementation/03-contract-templates.md`.

`implementation/11-skill-contracts.md` is the canonical source of truth for method-skill contracts. Runtime files under `.agents/skills/*/SKILL.md` are concise executable adapters synchronized to this document. Legacy `*-skill-prd.md`, method PRDs, frameworks, and playbooks are source material only when routed through `implementation/01-documentation-control.md` and `implementation/10-traceability-matrix.md`; canonical documents govern conflicts.

## Standard method-output requirement

Every skill output must include a human-readable method summary plus a structured handoff. The required method-output core is:

```markdown
## Method Output Summary
- Subject:
- Scope:
- Analysis Status: Complete for scoped method | Preliminary | Limited | Blocked
- IC Action Status: Not an IC Action for non-IC skills; gated Investment Committee status only for IC synthesis
- Evidence Status:
- Method Confidence: High | Medium | Low | Not Rateable, with reason

## Key Findings
- [Concise findings from this method only]

## Domain Findings
- [Domain-specific analytical sections required by the skill]

## Limitations
- [Missing, stale, conflicting, proxy, source-restricted, or excluded inputs]

## Missing IC Gates
- [Evidence, lead analysis, valuation, risk, implementation, portfolio, or context gates still required]

## Boundary
Boundary: Method output only; not an IC Action. IC synthesis uses the separate gated IC exception below.

## Structured Handoff
- Subject:
- Scope:
- Producing skill:
- Output status:
- Evidence status:
- Method confidence:
- Key findings:
- Limitations:
- Required follow-up:
- Decision constraints:
- Downstream relevance:
```

## Cross-skill guardrails

- Direct skill calls are allowed only as scoped method outputs with visible boundary and missing IC gates.
- Non-IC skills must not issue `IC Action`, use `Action Box`, provide exact allocation instructions, or present specialist output as final decision support.
- Evidence status, freshness, source restrictions, user-file provenance, and material conflicts constrain every skill conclusion.
- Freshness-sensitive requests split structural view from current-action view; current action requires current timestamped sources.
- User-provided files require provenance and sanity checks; user-only source scope must be marked `Limited by source scope` when material.
- Discovery outputs rank candidates only as review priorities and must show missing asset-level gates.
- Complex products may receive educational/mechanics explainers, but positive action is blocked until enhanced product and implementation gates pass.
- Cheap-looking assets trigger value-trap checks; expensive growth assets trigger growth-expectations bridge.
- Method Confidence means confidence in analytical support, not probability of future price outcome.

## P5-SKL-01 approved edge-case behavior

| Rule ID | Case | Canonical skill-contract behavior |
|---|---|---|
| P5-SKL-01-01 | Skill visibility | Integrated output by default; skill-level detail only on request or audit/debug mode. |
| P5-SKL-01-02 | Missing data | Block only decision-critical gaps; otherwise produce Preliminary/Limited scoped output with visible missing inputs. |
| P5-SKL-01-03 | Compact contracts | Skill contracts and runtime adapters stay concise; deep method detail remains supporting reference material. |
| P5-SKL-01-04 | Buy/sell/hold | Skills may give Preliminary Quick Take implications or scenario matrix but no final IC Action. |
| P5-SKL-01-05 | Freshness | Separate structural view from current-action view and require current timestamped sources for current claims. |
| P5-SKL-01-06 | Direct skill call | Allowed only as scoped method output with boundary and missing IC gates. |
| P5-SKL-01-07 | User files | Treat as source material requiring provenance and sanity checks. |
| P5-SKL-01-08 | Discovery | Candidate ranking is review priority, not buy list. |
| P5-SKL-01-09 | Hybrid instruments | Lead follows owned instrument/wrapper; underlying-driver skills are contributors. |
| P5-SKL-01-10 | Evidence conflict | Evidence status constrains conclusions; skills may challenge but not override readiness. |
| P5-SKL-01-11 | Output layers | Every skill output has human summary plus structured handoff. |
| P5-SKL-01-12 | Known gaps | Technical defaults from canonical docs are allowed; product/UX ambiguity is pending decision. |
| P5-SKL-01-13 | Workflow depth | Run minimum sufficient relevant skills by default; Quick/Standard/Full by request. |
| P5-SKL-01-14 | Sizing | Only illustrative or Portfolio Fit ranges; exact allocation instructions prohibited. |
| P5-SKL-01-15 | Complex products | Explainers allowed; positive action blocked until enhanced product gate. |
| P5-SKL-01-16 | Ownership | Agents own role/boundary/status/handoff; skills own method; references own deep detail. |
| P5-SKL-01-17 | Premature final reports | Use gate-aware non-final artifacts when gates are missing. |
| P5-SKL-01-18 | Output format | Shared method-output core plus domain-specific sections. |
| P5-SKL-01-19 | Source restrictions | Obey user restrictions and mark material limits `Limited by source scope`. |
| P5-SKL-01-20 | Complete status | Complete means `Complete for scoped method`, never Complete IC Action. |
| P5-SKL-01-21 | P8 separation | P5-SKL defines method-output schemas; P8 owns final IC memo schemas. |
| P5-SKL-01-22 | Canonical authority | `implementation/11-skill-contracts.md` is source of truth; runtime SKILL.md files are adapters. |
| P5-SKL-01-23 | Legacy | Legacy skill PRDs/frameworks are source material only; canonical docs win. |
| P5-SKL-01-24 | Confidence | Method Confidence is support confidence with reason, not forecast probability. |
| P5-SKL-01-25 | Value/growth traps | Relevant skills mark value-trap and growth-expectations triggers. |
| P5-SKL-01-26 | Rumors | Rumors only as `Unconfirmed / Rumor`, not facts. |
| P5-SKL-01-27 | Portfolio privacy | Without private data, generic role plus minimum context checklist only. |
| P5-SKL-01-28 | Run all agents | Means full relevant workflow, not literal all skills. |
| P5-SKL-01-29 | Ambiguous instruments | Safe default only when obvious; material ambiguity blocks final decision-level output. |

## Evidence Collection Method Skill

```yaml
contract_type: Skill
status: Canonical
owner: Evidence Collector Agent
used_by:
  - Evidence Collector Agent
produces:
  - evidence_pack.md
  - readiness_matrix
  - evidence_requests
  - pre_ic_evidence_lock
  - evidence-collection_structured_handoff
consumes:
  - intake_block
  - selected_workflow
  - evidence_profile
  - subject_instrument_theme
  - existing_source_notes_or_user_provided_context
evidence_required: true
decision_boundary: Method output only; no ownership outside scope; no final IC Action.
known_gaps:
  - none
```

### Purpose

Collect, classify, verify, and structure evidence for downstream analysis.

### When to use

- Evidence plan is required for any workflow or specialist output.

### What you get

A scoped method output for `Evidence Collection Method Skill` with method findings, evidence status, Method Confidence, limitations, missing IC gates, and structured handoff.

### What it will not do

It will not exceed the owning agent/workflow boundary, bypass evidence readiness, or issue final IC Action.

### Required inputs

- Intake block
- Selected workflow
- Evidence profile
- Subject/instrument/theme
- Existing source notes or user-provided context

If required inputs are missing, continue only when a safe Preliminary or Limited scoped output is allowed; otherwise return Blocked with the missing inputs.

### Step sequence

1. Define claim universe and materiality
2. Select source hierarchy and domain overlays
3. Collect and timestamp sources
4. Classify claim/source/freshness/access/support
5. Identify missing data, contradictions, and proxy evidence
6. Produce evidence pack, readiness matrix, and evidence requests
7. Perform pre-IC evidence lock where needed

Keep the method output scoped to the owning agent or workflow.

### Output contract

- Must use the standard method-output core from this document.
- Must state scope, assumptions, evidence status, Analysis Status, Method Confidence, limitations, missing IC gates, boundary, and structured handoff.
- Domain Findings must map to the step sequence and include only findings supported by the evidence status.
- Expected downstream artifact or section: `evidence_pack.md`, `readiness_matrix`, `evidence_requests`, and `pre_ic_evidence_lock`.
- Must not substitute for final IC memo schemas; P8-IC-01 owns final IC report schemas.

### Guardrails

- Do not make investment, valuation, risk, or portfolio conclusions.
- Follow statuses, confidence, evidence display, source-scope, freshness, conflict, and writing rules in `implementation/00-master-rules.md`.
- Follow evidence readiness, provenance, source hierarchy, and pre-IC lock rules in `implementation/04-evidence-layer.md`.

### Failure states

- Complete when: Required inputs, evidence, boundary conditions, and domain checks are sufficient for `Complete for scoped method`; this does not imply Complete IC Action.
- Preliminary when: The skill can provide an early, narrow, or Quick Take-style method view before all method inputs or workflow gates are complete.
- Limited when: evidence is partial/stale/proxy-heavy.
- Blocked when: decision-critical support is unavailable.

### Quality checks

- Material claims have support status and missing data is visible.
- Output does not exceed the owning agent boundary.
- Material claims are evidence-aware.
- Required Template v2 metadata and UX blocks are present.
- Output uses the standard method-output core and structured handoff.
- Boundary prevents unauthorized IC Action, Action Box, exact sizing, or hidden recommendation.

## Equity Company Analysis Method Skill

```yaml
contract_type: Skill
status: Canonical
owner: Equity Agent
used_by:
  - Equity Agent
produces:
  - equity_company_analysis.md
  - equity-company-analysis_structured_handoff
consumes:
  - company_ticker_identity
  - evidence_pack
  - financial_analysis_where_available
  - sector_news_context_where_material
evidence_required: true
decision_boundary: Method output only; no ownership outside scope; no final IC Action.
known_gaps:
  - none
```

### Purpose

Analyze company business quality and thesis durability.

### When to use

- An equity company-quality report is required or requested.

### What you get

A scoped method output for `Equity Company Analysis Method Skill` with method findings, evidence status, Method Confidence, limitations, missing IC gates, and structured handoff.

### What it will not do

It will not exceed the owning agent/workflow boundary, bypass evidence readiness, or issue final IC Action.

### Required inputs

- Company/ticker identity
- Evidence pack
- Financial analysis where available
- Sector/news context where material

If required inputs are missing, continue only when a safe Preliminary or Limited scoped output is allowed; otherwise return Blocked with the missing inputs.

### Step sequence

1. Define business and revenue model
2. Assess customer value and demand quality
3. Analyze revenue/margin durability
4. Assess competitive position and management quality
5. Read through financial evidence
6. Define thesis dependencies, breakpoints, and monitoring triggers

Keep the method output scoped to the owning agent or workflow.

### Output contract

- Must use the standard method-output core from this document.
- Must state scope, assumptions, evidence status, Analysis Status, Method Confidence, limitations, missing IC gates, boundary, and structured handoff.
- Domain Findings must map to the step sequence and include only findings supported by the evidence status.
- Expected downstream artifact or section: `equity_company_analysis.md`.
- Must not substitute for final IC memo schemas; P8-IC-01 owns final IC report schemas.

### Guardrails

- Do not convert business quality into final stock action.
- Follow statuses, confidence, evidence display, source-scope, freshness, conflict, and writing rules in `implementation/00-master-rules.md`.
- Follow evidence readiness, provenance, source hierarchy, and pre-IC lock rules in `implementation/04-evidence-layer.md`.

### Failure states

- Complete when: Required inputs, evidence, boundary conditions, and domain checks are sufficient for `Complete for scoped method`; this does not imply Complete IC Action.
- Preliminary when: The skill can provide an early, narrow, or Quick Take-style method view before all method inputs or workflow gates are complete.
- Limited when: company/financial evidence is partial.
- Blocked when: identity or core business evidence is missing.

### Quality checks

- Business quality is separated from stock attractiveness.
- Output does not exceed the owning agent boundary.
- Material claims are evidence-aware.
- Required Template v2 metadata and UX blocks are present.
- Output uses the standard method-output core and structured handoff.
- Boundary prevents unauthorized IC Action, Action Box, exact sizing, or hidden recommendation.

## Financial Statement Analysis Skill

```yaml
contract_type: Skill
status: Canonical
owner: Equity Agent
used_by:
  - Equity Agent
  - Valuation
  - Risk
  - IC
produces:
  - equity_company_analysis.md
  - financial-statement-analysis_structured_handoff
consumes:
  - latest_statements
  - historical_financials
  - segment_share_count_capital_allocation_data_where_available
evidence_required: true
decision_boundary: Method output only; no ownership outside scope; no final IC Action.
known_gaps:
  - none
```

### Purpose

Diagnose financial quality and risk from statements.

### When to use

- Financial quality is material to company analysis, valuation, risk, or IC.

### What you get

A scoped method output for `Financial Statement Analysis Skill` with method findings, evidence status, Method Confidence, limitations, missing IC gates, and structured handoff.

### What it will not do

It will not exceed the owning agent/workflow boundary, bypass evidence readiness, or issue final IC Action.

### Required inputs

- Latest statements
- Historical financials
- Segment/share count/capital allocation data where available

If required inputs are missing, continue only when a safe Preliminary or Limited scoped output is allowed; otherwise return Blocked with the missing inputs.

### Step sequence

1. Analyze revenue quality
2. Analyze margin structure
3. Analyze cash flow and FCF conversion
4. Analyze balance sheet and liquidity
5. Analyze working capital/accounting quality
6. Analyze dilution and capital allocation
7. Identify red flags and trend breaks

Keep the method output scoped to the owning agent or workflow.

### Output contract

- Must use the standard method-output core from this document.
- Must state scope, assumptions, evidence status, Analysis Status, Method Confidence, limitations, missing IC gates, boundary, and structured handoff.
- Domain Findings must map to the step sequence and include only findings supported by the evidence status.
- Expected downstream artifact or section: `equity_company_analysis.md`.
- Must not substitute for final IC memo schemas; P8-IC-01 owns final IC report schemas.

### Guardrails

- Do not invent missing financial line items or replace valuation.
- Follow statuses, confidence, evidence display, source-scope, freshness, conflict, and writing rules in `implementation/00-master-rules.md`.
- Follow evidence readiness, provenance, source hierarchy, and pre-IC lock rules in `implementation/04-evidence-layer.md`.

### Failure states

- Complete when: Required inputs, evidence, boundary conditions, and domain checks are sufficient for `Complete for scoped method`; this does not imply Complete IC Action.
- Preliminary when: The skill can provide an early, narrow, or Quick Take-style method view before all method inputs or workflow gates are complete.
- Limited when: history is partial.
- Blocked when: core financial data is unavailable.

### Quality checks

- Financial trends and risks are clear for Equity, Valuation, Risk, and IC.
- Output does not exceed the owning agent boundary.
- Material claims are evidence-aware.
- Required Template v2 metadata and UX blocks are present.
- Output uses the standard method-output core and structured handoff.
- Boundary prevents unauthorized IC Action, Action Box, exact sizing, or hidden recommendation.

## Valuation & Expectations Method Skill

```yaml
contract_type: Skill
status: Canonical
owner: Valuation & Expectations Agent
used_by:
  - Valuation & Expectations Agent
produces:
  - valuation_expectations.md
  - valuation-expectations_structured_handoff
consumes:
  - price_market_cap_ev
  - financial_history_and_forecast_inputs
  - business-quality_assumptions
  - peer_historical_consensus_context_where_available
evidence_required: true
decision_boundary: Method output only; no ownership outside scope; no final IC Action.
known_gaps:
  - none
```

### Purpose

Assess whether market price is justified by realistic expectations.

### When to use

- Price/action or valuation context is decision-relevant.

### What you get

A scoped method output for `Valuation & Expectations Method Skill` with method findings, evidence status, Method Confidence, limitations, missing IC gates, and structured handoff.

### What it will not do

It will not exceed the owning agent/workflow boundary, bypass evidence readiness, or issue final IC Action.

### Required inputs

- Price/market cap/EV
- Financial history and forecast inputs
- Business-quality assumptions
- Peer/historical/consensus context where available

If required inputs are missing, continue only when a safe Preliminary or Limited scoped output is allowed; otherwise return Blocked with the missing inputs.

### Step sequence

1. Check data integrity
2. Select valuation context and methods
3. Reverse-engineer implied expectations
4. Build scenario valuation range
5. Build return bridge
6. Reconcile methods and risks
7. Define monitoring signals

Keep the method output scoped to the owning agent or workflow.

### Output contract

- Must use the standard method-output core from this document.
- Must state scope, assumptions, evidence status, Analysis Status, Method Confidence, limitations, missing IC gates, boundary, and structured handoff.
- Domain Findings must map to the step sequence and include only findings supported by the evidence status.
- Expected downstream artifact or section: `valuation_expectations.md`.
- Must not substitute for final IC memo schemas; P8-IC-01 owns final IC report schemas.

### Guardrails

- Do not present point target as truth or issue final IC action.
- Follow statuses, confidence, evidence display, source-scope, freshness, conflict, and writing rules in `implementation/00-master-rules.md`.
- Follow evidence readiness, provenance, source hierarchy, and pre-IC lock rules in `implementation/04-evidence-layer.md`.

### Failure states

- Complete when: Required inputs, evidence, boundary conditions, and domain checks are sufficient for `Complete for scoped method`; this does not imply Complete IC Action.
- Preliminary when: The skill can provide an early, narrow, or Quick Take-style method view before all method inputs or workflow gates are complete.
- Limited when: inputs are partial/proxy.
- Blocked when: core price/financial/capital-structure inputs are missing.

### Quality checks

- IC can see what is priced in and what must be true.
- Output does not exceed the owning agent boundary.
- Material claims are evidence-aware.
- Required Template v2 metadata and UX blocks are present.
- Output uses the standard method-output core and structured handoff.
- Boundary prevents unauthorized IC Action, Action Box, exact sizing, or hidden recommendation.

## Risk / Red Team Method Skill

```yaml
contract_type: Skill
status: Canonical
owner: Risk / Red Team Agent
used_by:
  - Risk / Red Team Agent
produces:
  - risk_red_team.md
  - risk-red-team_structured_handoff
consumes:
  - core_thesis
  - evidence_pack
  - lead_analysis
  - valuation_context_for_complete_review
  - relevant_specialists
evidence_required: true
decision_boundary: Method output only; no ownership outside scope; no final IC Action.
known_gaps:
  - none
```

### Purpose

Challenge the thesis and identify material failure paths.

### When to use

- A thesis, final action, or risk challenge is requested.

### What you get

A scoped method output for `Risk / Red Team Method Skill` with method findings, evidence status, Method Confidence, limitations, missing IC gates, and structured handoff.

### What it will not do

It will not exceed the owning agent/workflow boundary, bypass evidence readiness, or issue final IC Action.

### Required inputs

- Core thesis
- Evidence pack
- Lead analysis
- Valuation context for Complete Review
- Relevant specialists

If required inputs are missing, continue only when a safe Preliminary or Limited scoped output is allowed; otherwise return Blocked with the missing inputs.

### Step sequence

1. Check input completeness
2. Extract thesis and assumptions
3. Apply materiality/anti-overbreaking discipline
4. Identify failure paths and bear case
5. Run mandatory risk gates
6. Include counter-evidence and challenge requests
7. Issue risk challenge verdict

Keep the method output scoped to the owning agent or workflow.

### Output contract

- Must use the standard method-output core from this document.
- Must state scope, assumptions, evidence status, Analysis Status, Method Confidence, limitations, missing IC gates, boundary, and structured handoff.
- Domain Findings must map to the step sequence and include only findings supported by the evidence status.
- Expected downstream artifact or section: `risk_red_team.md`.
- Must not substitute for final IC memo schemas; P8-IC-01 owns final IC report schemas.

### Guardrails

- Do not create generic risk lists or hidden recommendations.
- Follow statuses, confidence, evidence display, source-scope, freshness, conflict, and writing rules in `implementation/00-master-rules.md`.
- Follow evidence readiness, provenance, source hierarchy, and pre-IC lock rules in `implementation/04-evidence-layer.md`.

### Failure states

- Complete when: Required inputs, evidence, boundary conditions, and domain checks are sufficient for `Complete for scoped method`; this does not imply Complete IC Action.
- Preliminary when: The skill can provide an early, narrow, or Quick Take-style method view before all method inputs or workflow gates are complete.
- Limited when: thesis/evidence exists but valuation/risk detail is incomplete.
- Blocked when: core thesis is undefined.

### Quality checks

- Risks have transmission mechanism and valuation link where required.
- Output does not exceed the owning agent boundary.
- Material claims are evidence-aware.
- Required Template v2 metadata and UX blocks are present.
- Output uses the standard method-output core and structured handoff.
- Boundary prevents unauthorized IC Action, Action Box, exact sizing, or hidden recommendation.

## Investment Committee Synthesis Method Skill

IC exception: this is the only method skill that may support `Action Box`, `Investment View`, or `IC Action`, and only inside the Investment Committee Agent after evidence lock and required gates pass. When those gates do not pass, it produces a gate-aware non-final artifact.

```yaml
contract_type: Skill
status: Canonical
owner: Investment Committee Agent
used_by:
  - Investment Committee Agent
produces:
  - final_investment_memo.md
  - investment-committee-synthesis_structured_handoff
consumes:
  - intake_context
  - evidence_pack_and_pre-ic_lock
  - lead_analysis
  - valuation_and_risk_when_decision-relevant
  - material_specialist_reports
evidence_required: true
decision_boundary: IC synthesis method only; final IC Action allowed only when IC evidence lock and gates permit.
known_gaps:
  - none
```

### Purpose

Integrate evidence and specialist reports into final decision-support memo.

### When to use

- Final decision-support output is requested.

### What you get

A scoped method output for `Investment Committee Synthesis Method Skill` with method findings, evidence status, Method Confidence, limitations, missing IC gates, and structured handoff.

### What it will not do

It will not exceed the Investment Committee boundary, bypass evidence readiness, or issue final IC Action unless evidence lock and required IC gates pass.

### Required inputs

- Intake context
- Evidence pack and pre-IC lock
- Lead analysis
- Valuation and Risk when decision-relevant
- Material specialist reports

If required inputs are missing, continue only when a safe Preliminary or Limited scoped output is allowed; otherwise return Blocked with the missing inputs.

### Step sequence

1. Check required inputs and evidence lock
2. Identify core debate and assumptions
3. Integrate business, valuation, risk, catalyst, macro, positioning, and portfolio context
4. Apply positive-action gate
5. Produce Action Box, Investment View, IC Action, confidence, monitoring, and follow-up requests

Keep the method output scoped to the owning agent or workflow.

### Output contract

- Must use the standard method-output core from this document.
- Must state scope, assumptions, evidence status, Analysis Status, Method Confidence, limitations, missing IC gates, boundary, and structured handoff.
- Domain Findings must map to the step sequence and include only findings supported by the evidence status.
- Expected downstream artifact or section: `final_investment_memo.md`.
- Must not substitute for final IC memo schemas; P8-IC-01 owns final IC report schemas.

### Guardrails

- Do not invent facts, expose internal transcript, or provide exact position sizing.
- Follow statuses, confidence, evidence display, source-scope, freshness, conflict, and writing rules in `implementation/00-master-rules.md`.
- Follow evidence readiness, provenance, source hierarchy, and pre-IC lock rules in `implementation/04-evidence-layer.md`.

### Failure states

- Complete when: Required inputs, evidence, boundary conditions, and domain checks are sufficient for `Complete for scoped method`; this does not imply Complete IC Action.
- Preliminary when: The skill can provide an early, narrow, or Quick Take-style method view before all method inputs or workflow gates are complete.
- Limited when: useful but constrained.
- Blocked when: required evidence/valuation/risk/lead analysis is missing.

### Quality checks

- Memo is decision-oriented, evidence-constrained, and includes monitoring.
- Output does not exceed the owning agent boundary.
- Material claims are evidence-aware.
- Required Template v2 metadata and UX blocks are present.
- Output uses the standard method-output core and structured handoff.
- Boundary prevents unauthorized IC Action, Action Box, exact sizing, or hidden recommendation.

## ETF Analysis Method Skill

```yaml
contract_type: Skill
status: Canonical
owner: ETF Agent
used_by:
  - ETF Agent
produces:
  - etf_analysis.md
  - etf-analysis_structured_handoff
consumes:
  - ticker_fund_identity
  - issuer_holdings_fund_documents
  - index_methodology
  - cost_aum_liquidity_distribution_data
evidence_required: true
decision_boundary: Method output only; no ownership outside scope; no final IC Action.
known_gaps:
  - none
```

### Purpose

Analyze ETF vehicle quality and exposure.

### When to use

- ETF/fund analysis or comparison is requested.

### What you get

A scoped method output for `ETF Analysis Method Skill` with method findings, evidence status, Method Confidence, limitations, missing IC gates, and structured handoff.

### What it will not do

It will not exceed the owning agent/workflow boundary, bypass evidence readiness, or issue final IC Action.

### Required inputs

- Ticker/fund identity
- Issuer holdings/fund documents
- Index/methodology
- Cost/AUM/liquidity/distribution data

If required inputs are missing, continue only when a safe Preliminary or Limited scoped output is allowed; otherwise return Blocked with the missing inputs.

### Step sequence

1. Verify fund identity
2. Separate fund vs share-class issues
3. Analyze holdings/exposure/concentration
4. Analyze methodology/active process
5. Assess cost/AUM/liquidity/structure
6. Assess yield/overlap/special risks
7. Produce Vehicle Quality Verdict

Keep the method output scoped to the owning agent or workflow.

### Output contract

- Must use the standard method-output core from this document.
- Must state scope, assumptions, evidence status, Analysis Status, Method Confidence, limitations, missing IC gates, boundary, and structured handoff.
- Domain Findings must map to the step sequence and include only findings supported by the evidence status.
- Expected downstream artifact or section: `etf_analysis.md`.
- Must not substitute for final IC memo schemas; P8-IC-01 owns final IC report schemas.

### Guardrails

- Do not issue final portfolio action, tax/legal advice, or exact execution plan.
- Follow statuses, confidence, evidence display, source-scope, freshness, conflict, and writing rules in `implementation/00-master-rules.md`.
- Follow evidence readiness, provenance, source hierarchy, and pre-IC lock rules in `implementation/04-evidence-layer.md`.

### Failure states

- Complete when: Required inputs, evidence, boundary conditions, and domain checks are sufficient for `Complete for scoped method`; this does not imply Complete IC Action.
- Preliminary when: The skill can provide an early, narrow, or Quick Take-style method view before all method inputs or workflow gates are complete.
- Limited when: issuer data is stale/partial.
- Blocked when: identity/holdings/methodology cannot be verified.

### Quality checks

- Vehicle quality and exposure purity are clear.
- Output does not exceed the owning agent boundary.
- Material claims are evidence-aware.
- Required Template v2 metadata and UX blocks are present.
- Output uses the standard method-output core and structured handoff.
- Boundary prevents unauthorized IC Action, Action Box, exact sizing, or hidden recommendation.

## Fixed Income Analysis Method Skill

```yaml
contract_type: Skill
status: Canonical
owner: Fixed Income Agent
used_by:
  - Fixed Income Agent
produces:
  - fixed_income_analysis.md
  - fixed-income-analysis_structured_handoff
consumes:
  - instrument_identity_terms
  - yield_spread_duration_data
  - issuer_obligor_credit_evidence
  - liquidity_structure_evidence
evidence_required: true
decision_boundary: Method output only; no ownership outside scope; no final IC Action.
known_gaps:
  - none
```

### Purpose

Analyze compensation and risk for fixed-income instruments.

### When to use

- Fixed-income instrument or exposure review is requested.

### What you get

A scoped method output for `Fixed Income Analysis Method Skill` with method findings, evidence status, Method Confidence, limitations, missing IC gates, and structured handoff.

### What it will not do

It will not exceed the owning agent/workflow boundary, bypass evidence readiness, or issue final IC Action.

### Required inputs

- Instrument identity/terms
- Yield/spread/duration data
- Issuer/obligor credit evidence
- Liquidity/structure evidence

If required inputs are missing, continue only when a safe Preliminary or Limited scoped output is allowed; otherwise return Blocked with the missing inputs.

### Step sequence

1. Verify instrument and terms
2. Analyze yield/spread/carry
3. Analyze duration/curve/convexity
4. Assess credit and liquidity
5. Assess call/prepayment/extension/covenants
6. Build downside scenario
7. Issue compensation verdict

Keep the method output scoped to the owning agent or workflow.

### Output contract

- Must use the standard method-output core from this document.
- Must state scope, assumptions, evidence status, Analysis Status, Method Confidence, limitations, missing IC gates, boundary, and structured handoff.
- Domain Findings must map to the step sequence and include only findings supported by the evidence status.
- Expected downstream artifact or section: `fixed_income_analysis.md`.
- Must not substitute for final IC memo schemas; P8-IC-01 owns final IC report schemas.

### Guardrails

- Do not provide final allocation or exact execution plan.
- Follow statuses, confidence, evidence display, source-scope, freshness, conflict, and writing rules in `implementation/00-master-rules.md`.
- Follow evidence readiness, provenance, source hierarchy, and pre-IC lock rules in `implementation/04-evidence-layer.md`.

### Failure states

- Complete when: Required inputs, evidence, boundary conditions, and domain checks are sufficient for `Complete for scoped method`; this does not imply Complete IC Action.
- Preliminary when: The skill can provide an early, narrow, or Quick Take-style method view before all method inputs or workflow gates are complete.
- Limited when: market/credit data is partial.
- Blocked when: terms or pricing/credit evidence are missing.

### Quality checks

- Compensation for duration/credit/liquidity/structure risk is clear.
- Output does not exceed the owning agent boundary.
- Material claims are evidence-aware.
- Required Template v2 metadata and UX blocks are present.
- Output uses the standard method-output core and structured handoff.
- Boundary prevents unauthorized IC Action, Action Box, exact sizing, or hidden recommendation.

## Commodity Analysis Method Skill

```yaml
contract_type: Skill
status: Canonical
owner: Commodity Agent
used_by:
  - Commodity Agent
produces:
  - commodity_analysis.md or commodity_market_regime.md
  - commodity-analysis_structured_handoff
consumes:
  - commodity_instrument_identity
  - demand_supply_inventory_evidence
  - curve_market_data
  - macro_policy_logistics_context
evidence_required: true
decision_boundary: Method output only; no ownership outside scope; no final IC Action.
known_gaps:
  - none
```

### Purpose

Analyze commodity setup through balance, curve, macro, policy, logistics, and instrument context.

### When to use

- Commodity setup, regime, or instrument analysis is requested.

### What you get

A scoped method output for `Commodity Analysis Method Skill` with method findings, evidence status, Method Confidence, limitations, missing IC gates, and structured handoff.

### What it will not do

It will not exceed the owning agent/workflow boundary, bypass evidence readiness, or issue final IC Action.

### Required inputs

- Commodity/instrument identity
- Demand/supply/inventory evidence
- Curve/market data
- Macro/policy/logistics context

If required inputs are missing, continue only when a safe Preliminary or Limited scoped output is allowed; otherwise return Blocked with the missing inputs.

### Step sequence

1. Classify commodity family and mode
2. Build demand map
3. Build supply map
4. Analyze inventories/reserves/flows
5. Analyze cost curve and curve/roll/carry
6. Analyze macro/geopolitics/logistics/substitution
7. Assess instrument context
8. Produce verdict, actionability label, triggers

Keep the method output scoped to the owning agent or workflow.

### Output contract

- Must use the standard method-output core from this document.
- Must state scope, assumptions, evidence status, Analysis Status, Method Confidence, limitations, missing IC gates, boundary, and structured handoff.
- Domain Findings must map to the step sequence and include only findings supported by the evidence status.
- Expected downstream artifact or section: `commodity_analysis.md or commodity_market_regime.md`.
- Must not substitute for final IC memo schemas; P8-IC-01 owns final IC report schemas.

### Guardrails

- Do not issue precise price target or final buy/sell/hold.
- Follow statuses, confidence, evidence display, source-scope, freshness, conflict, and writing rules in `implementation/00-master-rules.md`.
- Follow evidence readiness, provenance, source hierarchy, and pre-IC lock rules in `implementation/04-evidence-layer.md`.

### Failure states

- Complete when: Required inputs, evidence, boundary conditions, and domain checks are sufficient for `Complete for scoped method`; this does not imply Complete IC Action.
- Preliminary when: The skill can provide an early, narrow, or Quick Take-style method view before all method inputs or workflow gates are complete.
- Limited when: physical data is delayed/proxy-heavy.
- Blocked when: identity or decision-critical balance data is unavailable.

### Quality checks

- Setup, balance, risks, and handoffs are clear.
- Output does not exceed the owning agent boundary.
- Material claims are evidence-aware.
- Required Template v2 metadata and UX blocks are present.
- Output uses the standard method-output core and structured handoff.
- Boundary prevents unauthorized IC Action, Action Box, exact sizing, or hidden recommendation.

## Crypto Analysis Method Skill

```yaml
contract_type: Skill
status: Canonical
owner: Crypto Agent
used_by:
  - Crypto Agent
produces:
  - crypto_analysis.md or crypto_market_regime.md
  - crypto-analysis_structured_handoff
consumes:
  - verified_asset_identity
  - network_tokenomics_adoption_liquidity_data
  - regulatory_security_governance_evidence
  - market_data_flows_where_relevant
evidence_required: true
decision_boundary: Method output only; no ownership outside scope; no final IC Action.
known_gaps:
  - none
```

### Purpose

Analyze crypto asset viability, value accrual, adoption, tokenomics, liquidity, regulation, and security.

### When to use

- Crypto asset/regime analysis is requested.

### What you get

A scoped method output for `Crypto Analysis Method Skill` with method findings, evidence status, Method Confidence, limitations, missing IC gates, and structured handoff.

### What it will not do

It will not exceed the owning agent/workflow boundary, bypass evidence readiness, or issue final IC Action.

### Required inputs

- Verified asset identity
- Network/tokenomics/adoption/liquidity data
- Regulatory/security/governance evidence
- Market data/flows where relevant

If required inputs are missing, continue only when a safe Preliminary or Limited scoped output is allowed; otherwise return Blocked with the missing inputs.

### Step sequence

1. Verify identity and category
2. Apply investment-grade viability gate
3. Analyze network economics/adoption/tokenomics
4. Analyze liquidity/structure/demand/supply
5. Analyze macro/liquidity/regulation/security/governance
6. Run edge-case checks
7. Produce verdict and monitoring triggers

Keep the method output scoped to the owning agent or workflow.

### Output contract

- Must use the standard method-output core from this document.
- Must state scope, assumptions, evidence status, Analysis Status, Method Confidence, limitations, missing IC gates, boundary, and structured handoff.
- Domain Findings must map to the step sequence and include only findings supported by the evidence status.
- Expected downstream artifact or section: `crypto_analysis.md or crypto_market_regime.md`.
- Must not substitute for final IC memo schemas; P8-IC-01 owns final IC report schemas.

### Guardrails

- Do not give custody, yield-farming, leverage, legal/tax, or final buy/sell instructions.
- Follow statuses, confidence, evidence display, source-scope, freshness, conflict, and writing rules in `implementation/00-master-rules.md`.
- Follow evidence readiness, provenance, source hierarchy, and pre-IC lock rules in `implementation/04-evidence-layer.md`.

### Failure states

- Complete when: Required inputs, evidence, boundary conditions, and domain checks are sufficient for `Complete for scoped method`; this does not imply Complete IC Action.
- Preliminary when: The skill can provide an early, narrow, or Quick Take-style method view before all method inputs or workflow gates are complete.
- Limited when: data is partial/fast-moving.
- Blocked when: identity/tokenomics/security/liquidity evidence is unverifiable.

### Quality checks

- Viability, thesis, anti-thesis, risks, and triggers are clear.
- Output does not exceed the owning agent boundary.
- Material claims are evidence-aware.
- Required Template v2 metadata and UX blocks are present.
- Output uses the standard method-output core and structured handoff.
- Boundary prevents unauthorized IC Action, Action Box, exact sizing, or hidden recommendation.

## Macro Analysis Method Skill

```yaml
contract_type: Skill
status: Canonical
owner: Macro Agent
used_by:
  - Macro Agent
produces:
  - macro_sensitivity.md or macro regime output
  - macro-analysis_structured_handoff
consumes:
  - asset_theme_context
  - relevant_macro_variables
  - fresh_market_data_when_current_action-sensitive
evidence_required: true
decision_boundary: Method output only; no ownership outside scope; no final IC Action.
known_gaps:
  - none
```

### Purpose

Analyze macro sensitivity, regime context, surprises, and transmission into assets.

### When to use

- Macro sensitivity or macro regime context is material/requested.

### What you get

A scoped method output for `Macro Analysis Method Skill` with method findings, evidence status, Method Confidence, limitations, missing IC gates, and structured handoff.

### What it will not do

It will not exceed the owning agent/workflow boundary, bypass evidence readiness, or issue final IC Action.

### Required inputs

- Asset/theme context
- Relevant macro variables
- Fresh market data when current/action-sensitive

If required inputs are missing, continue only when a safe Preliminary or Limited scoped output is allowed; otherwise return Blocked with the missing inputs.

### Step sequence

1. Define macro channels
2. Separate sensitivity from generic macro essay
3. Check growth/inflation/rates/liquidity/credit/FX/commodity channels
4. Check freshness
5. Assess thesis relevance
6. Produce handoff

Keep the method output scoped to the owning agent or workflow.

### Output contract

- Must use the standard method-output core from this document.
- Must state scope, assumptions, evidence status, Analysis Status, Method Confidence, limitations, missing IC gates, boundary, and structured handoff.
- Domain Findings must map to the step sequence and include only findings supported by the evidence status.
- Expected downstream artifact or section: `macro_sensitivity.md or macro regime output`.
- Must not substitute for final IC memo schemas; P8-IC-01 owns final IC report schemas.

### Guardrails

- Do not provide generic macro commentary unrelated to thesis.
- Follow statuses, confidence, evidence display, source-scope, freshness, conflict, and writing rules in `implementation/00-master-rules.md`.
- Follow evidence readiness, provenance, source hierarchy, and pre-IC lock rules in `implementation/04-evidence-layer.md`.

### Failure states

- Complete when: Required inputs, evidence, boundary conditions, and domain checks are sufficient for `Complete for scoped method`; this does not imply Complete IC Action.
- Preliminary when: The skill can provide an early, narrow, or Quick Take-style method view before all method inputs or workflow gates are complete.
- Limited when: data is stale/partial.
- Blocked when: decision-critical current data is unavailable.

### Quality checks

- Macro drivers and thesis relevance are explicit.
- Output does not exceed the owning agent boundary.
- Material claims are evidence-aware.
- Required Template v2 metadata and UX blocks are present.
- Output uses the standard method-output core and structured handoff.
- Boundary prevents unauthorized IC Action, Action Box, exact sizing, or hidden recommendation.

## News & Catalysts Method Skill

```yaml
contract_type: Skill
status: Canonical
owner: News & Catalysts Agent
used_by:
  - News & Catalysts Agent
produces:
  - news_catalysts.md
  - news-catalysts_structured_handoff
consumes:
  - subject_and_scope
  - news_event_sources
  - evidence_freshness_requirements
evidence_required: true
decision_boundary: Method output only; no ownership outside scope; no final IC Action.
known_gaps:
  - none
```

### Purpose

Analyze recent events, catalyst path, event status, freshness, and investment relevance.

### When to use

- Recent events/catalysts are material or requested.

### What you get

A scoped method output for `News & Catalysts Method Skill` with method findings, evidence status, Method Confidence, limitations, missing IC gates, and structured handoff.

### What it will not do

It will not exceed the owning agent/workflow boundary, bypass evidence readiness, or issue final IC Action.

### Required inputs

- Subject and scope
- News/event sources
- Evidence freshness requirements

If required inputs are missing, continue only when a safe Preliminary or Limited scoped output is allowed; otherwise return Blocked with the missing inputs.

### Step sequence

1. Collect recent and carryover events
2. Classify event status
3. Assess source/date confidence
4. Map catalyst timing and thesis relevance
5. Run negative news check
6. Produce handoff

Keep the method output scoped to the owning agent or workflow.

### Output contract

- Must use the standard method-output core from this document.
- Must state scope, assumptions, evidence status, Analysis Status, Method Confidence, limitations, missing IC gates, boundary, and structured handoff.
- Domain Findings must map to the step sequence and include only findings supported by the evidence status.
- Expected downstream artifact or section: `news_catalysts.md`.
- Must not substitute for final IC memo schemas; P8-IC-01 owns final IC report schemas.

### Guardrails

- Do not treat rumor as confirmed or issue final action from news alone.
- Follow statuses, confidence, evidence display, source-scope, freshness, conflict, and writing rules in `implementation/00-master-rules.md`.
- Follow evidence readiness, provenance, source hierarchy, and pre-IC lock rules in `implementation/04-evidence-layer.md`.

### Failure states

- Complete when: Required inputs, evidence, boundary conditions, and domain checks are sufficient for `Complete for scoped method`; this does not imply Complete IC Action.
- Preliminary when: The skill can provide an early, narrow, or Quick Take-style method view before all method inputs or workflow gates are complete.
- Limited when: reporting is partial/low-confidence.
- Blocked when: requested event cannot be verified.

### Quality checks

- Event status, freshness, and thesis relevance are clear.
- Output does not exceed the owning agent boundary.
- Material claims are evidence-aware.
- Required Template v2 metadata and UX blocks are present.
- Output uses the standard method-output core and structured handoff.
- Boundary prevents unauthorized IC Action, Action Box, exact sizing, or hidden recommendation.

## Market Positioning Method Skill

```yaml
contract_type: Skill
status: Canonical
owner: Market Positioning Agent
used_by:
  - Market Positioning Agent
produces:
  - market_positioning.md
  - market-positioning_structured_handoff
consumes:
  - asset_theme_context
  - price_action_and_market_data
  - flow_positioning_sentiment_estimate_evidence_where_available
evidence_required: true
decision_boundary: Method output only; no ownership outside scope; no final IC Action.
known_gaps:
  - none
```

### Purpose

Analyze expectations, crowding, narrative saturation, event bar, and positioning risk.

### When to use

- Positioning/expectations/crowding is material or requested.

### What you get

A scoped method output for `Market Positioning Method Skill` with method findings, evidence status, Method Confidence, limitations, missing IC gates, and structured handoff.

### What it will not do

It will not exceed the owning agent/workflow boundary, bypass evidence readiness, or issue final IC Action.

### Required inputs

- Asset/theme context
- Price action and market data
- Flow/positioning/sentiment/estimate evidence where available

If required inputs are missing, continue only when a safe Preliminary or Limited scoped output is allowed; otherwise return Blocked with the missing inputs.

### Step sequence

1. Assess market belief
2. Assess priced-in expectations
3. Assess crowding/neglect
4. Assess event bar/revision momentum
5. Identify positioning risk/opportunity
6. Produce handoff

Keep the method output scoped to the owning agent or workflow.

### Output contract

- Must use the standard method-output core from this document.
- Must state scope, assumptions, evidence status, Analysis Status, Method Confidence, limitations, missing IC gates, boundary, and structured handoff.
- Domain Findings must map to the step sequence and include only findings supported by the evidence status.
- Expected downstream artifact or section: `market_positioning.md`.
- Must not substitute for final IC memo schemas; P8-IC-01 owns final IC report schemas.

### Guardrails

- Do not claim positioning alone determines fundamental value.
- Follow statuses, confidence, evidence display, source-scope, freshness, conflict, and writing rules in `implementation/00-master-rules.md`.
- Follow evidence readiness, provenance, source hierarchy, and pre-IC lock rules in `implementation/04-evidence-layer.md`.

### Failure states

- Complete when: Required inputs, evidence, boundary conditions, and domain checks are sufficient for `Complete for scoped method`; this does not imply Complete IC Action.
- Preliminary when: The skill can provide an early, narrow, or Quick Take-style method view before all method inputs or workflow gates are complete.
- Limited when: evidence is indirect/incomplete.
- Blocked when: no usable positioning evidence exists.

### Quality checks

- Expectation bar and decision relevance are explicit.
- Output does not exceed the owning agent boundary.
- Material claims are evidence-aware.
- Required Template v2 metadata and UX blocks are present.
- Output uses the standard method-output core and structured handoff.
- Boundary prevents unauthorized IC Action, Action Box, exact sizing, or hidden recommendation.

## Portfolio Fit Method Skill

```yaml
contract_type: Skill
status: Canonical
owner: Portfolio Fit Agent
used_by:
  - Portfolio Fit Agent
produces:
  - portfolio_fit.md
  - portfolio-fit_structured_handoff
consumes:
  - asset_thesis
  - user_portfolio_context_where_available
  - risk_valuation_asset_reports_where_available
evidence_required: true
decision_boundary: Method output only; no ownership outside scope; no final IC Action.
known_gaps:
  - none
```

### Purpose

Assess generic role fit and user-specific portfolio fit.

### When to use

- Portfolio role/suitability is requested or material.

### What you get

A scoped method output for `Portfolio Fit Method Skill` with method findings, evidence status, Method Confidence, limitations, missing IC gates, and structured handoff.

### What it will not do

It will not exceed the owning agent/workflow boundary, bypass evidence readiness, or issue final IC Action.

### Required inputs

- Asset/thesis
- User portfolio context where available
- Risk/valuation/asset reports where available

If required inputs are missing, continue only when a safe Preliminary or Limited scoped output is allowed; otherwise return Blocked with the missing inputs.

### Step sequence

1. Assess generic role
2. Assess user-specific fit if context exists
3. Check overlap/concentration/risk/liquidity/FX/tax caveats
4. Assess monitoring burden
5. Produce IC handoff

Keep the method output scoped to the owning agent or workflow.

### Output contract

- Must use the standard method-output core from this document.
- Must state scope, assumptions, evidence status, Analysis Status, Method Confidence, limitations, missing IC gates, boundary, and structured handoff.
- Domain Findings must map to the step sequence and include only findings supported by the evidence status.
- Expected downstream artifact or section: `portfolio_fit.md`.
- Must not substitute for final IC memo schemas; P8-IC-01 owns final IC report schemas.

### Guardrails

- Do not give exact allocation or final buy/sell action.
- Follow statuses, confidence, evidence display, source-scope, freshness, conflict, and writing rules in `implementation/00-master-rules.md`.
- Follow evidence readiness, provenance, source hierarchy, and pre-IC lock rules in `implementation/04-evidence-layer.md`.

### Failure states

- Complete when: Required inputs, evidence, boundary conditions, and domain checks are sufficient for `Complete for scoped method`; this does not imply Complete IC Action.
- Preliminary when: The skill can provide an early, narrow, or Quick Take-style method view before all method inputs or workflow gates are complete.
- Limited when: user portfolio context is missing.
- Blocked when: user-specific answer is required but context is unavailable.

### Quality checks

- Generic and user-specific fit are separated.
- Output does not exceed the owning agent boundary.
- Material claims are evidence-aware.
- Required Template v2 metadata and UX blocks are present.
- Output uses the standard method-output core and structured handoff.
- Boundary prevents unauthorized IC Action, Action Box, exact sizing, or hidden recommendation.

## Sector & Industry Analysis Method Skill

```yaml
contract_type: Skill
status: Canonical
owner: Sector & Industry Analysis Agent
used_by:
  - Sector & Industry Analysis Agent
produces:
  - sector_industry_memo.md
  - sector_investment_map.md
  - sector_monitoring_plan.md
  - sector_context.md
  - sector-industry-analysis_structured_handoff
consumes:
  - sector_theme_definition
  - evidence_pack
  - relevant_companies_subsectors
  - user_horizon_universe_constraints
evidence_required: true
decision_boundary: Method output only; no ownership outside scope; no final IC Action.
known_gaps:
  - none
```

### Purpose

Analyze sector structure, economics, profit pools, drivers, investability, risks, and monitoring.

### When to use

- Sector/industry/theme-as-sector analysis is requested or embedded in equity workflow.

### What you get

A scoped method output for `Sector & Industry Analysis Method Skill` with method findings, evidence status, Method Confidence, limitations, missing IC gates, and structured handoff.

### What it will not do

It will not exceed the owning agent/workflow boundary, bypass evidence readiness, or issue final IC Action.

### Required inputs

- Sector/theme definition
- Evidence pack
- Relevant companies/subsectors
- User horizon/universe constraints

If required inputs are missing, continue only when a safe Preliminary or Limited scoped output is allowed; otherwise return Blocked with the missing inputs.

### Step sequence

1. Classify scope
2. Build evidence plan
3. Analyze structure/TAM/growth quality
4. Map value chain/profit pools/subsectors
5. Assess competition/drivers/valuation/investability
6. Build anti-thesis and monitoring
7. Produce sector outputs

Keep the method output scoped to the owning agent or workflow.

### Output contract

- Must use the standard method-output core from this document.
- Must state scope, assumptions, evidence status, Analysis Status, Method Confidence, limitations, missing IC gates, boundary, and structured handoff.
- Domain Findings must map to the step sequence and include only findings supported by the evidence status.
- Expected downstream artifact or section: `sector_industry_memo.md`, `sector_investment_map.md`, `sector_monitoring_plan.md`, and `sector_context.md`.
- Must not substitute for final IC memo schemas; P8-IC-01 owns final IC report schemas.

### Guardrails

- Do not make individual security final action.
- Follow statuses, confidence, evidence display, source-scope, freshness, conflict, and writing rules in `implementation/00-master-rules.md`.
- Follow evidence readiness, provenance, source hierarchy, and pre-IC lock rules in `implementation/04-evidence-layer.md`.

### Failure states

- Complete when: Required inputs, evidence, boundary conditions, and domain checks are sufficient for `Complete for scoped method`; this does not imply Complete IC Action.
- Preliminary when: The skill can provide an early, narrow, or Quick Take-style method view before all method inputs or workflow gates are complete.
- Limited when: boundaries/data are partial.
- Blocked when: scope/evidence is too weak.

### Quality checks

- Sector attractiveness, risks, and monitoring plan are clear.
- Output does not exceed the owning agent boundary.
- Material claims are evidence-aware.
- Required Template v2 metadata and UX blocks are present.
- Output uses the standard method-output core and structured handoff.
- Boundary prevents unauthorized IC Action, Action Box, exact sizing, or hidden recommendation.

## Structural Winner Discovery Method Skill

```yaml
contract_type: Skill
status: Canonical
owner: Structural Winners Discovery Agent
used_by:
  - Structural Winners Discovery Agent
produces:
  - structural_winners_memo.md
  - candidate_watchlist.md
  - structural-winner-discovery_structured_handoff
consumes:
  - theme_industry_definition
  - discovery_evidence
  - universe_constraints
  - sector_context_where_available
evidence_required: true
decision_boundary: Method output only; no ownership outside scope; no final IC Action.
known_gaps:
  - none
```

### Purpose

Discover and rank structural winner candidates within a theme.

### When to use

- Theme-driven candidate discovery is requested.

### What you get

A scoped method output for `Structural Winner Discovery Method Skill` with method findings, evidence status, Method Confidence, limitations, missing IC gates, and structured handoff.

### What it will not do

It will not exceed the owning agent/workflow boundary, bypass evidence readiness, or issue final IC Action.

### Required inputs

- Theme/industry definition
- Discovery evidence
- Universe constraints
- Sector context where available

If required inputs are missing, continue only when a safe Preliminary or Limited scoped output is allowed; otherwise return Blocked with the missing inputs.

### Step sequence

1. Interpret theme
2. Map value chain
3. Identify candidate archetypes
4. Apply positive/negative criteria and disqualifiers
5. Assess evidence/customer/demand/moat/management
6. Rank candidates
7. Produce watchlist and handoff

Keep the method output scoped to the owning agent or workflow.

### Output contract

- Must use the standard method-output core from this document.
- Must state scope, assumptions, evidence status, Analysis Status, Method Confidence, limitations, missing IC gates, boundary, and structured handoff.
- Domain Findings must map to the step sequence and include only findings supported by the evidence status.
- Expected downstream artifact or section: `structural_winners_memo.md` and `candidate_watchlist.md`.
- Must not substitute for final IC memo schemas; P8-IC-01 owns final IC report schemas.

### Guardrails

- Do not make candidates investment-actionable.
- Follow statuses, confidence, evidence display, source-scope, freshness, conflict, and writing rules in `implementation/00-master-rules.md`.
- Follow evidence readiness, provenance, source hierarchy, and pre-IC lock rules in `implementation/04-evidence-layer.md`.

### Failure states

- Complete when: Required inputs, evidence, boundary conditions, and domain checks are sufficient for `Complete for scoped method`; this does not imply Complete IC Action.
- Preliminary when: The skill can provide an early, narrow, or Quick Take-style method view before all method inputs or workflow gates are complete.
- Limited when: universe/evidence is partial.
- Blocked when: theme cannot define a universe.

### Quality checks

- Candidates are ranked with rationale, caveats, and next-step handoff.
- Output does not exceed the owning agent boundary.
- Material claims are evidence-aware.
- Required Template v2 metadata and UX blocks are present.
- Output uses the standard method-output core and structured handoff.
- Boundary prevents unauthorized IC Action, Action Box, exact sizing, or hidden recommendation.

## Driver Dominance Analysis Skill

```yaml
contract_type: Skill
status: Canonical
owner: Market Sense Agent
used_by:
  - Market Sense Agent
produces:
  - market_sense.md or driver dominance output
  - driver-dominance-analysis_structured_handoff
consumes:
  - asset_and_price_move
  - current_market_context
  - relevant_asset-driver_map
  - fresh_market_evidence_data_where_needed
evidence_required: true
decision_boundary: Method output only; no ownership outside scope; no final IC Action.
known_gaps:
  - none
```

### Purpose

Explain which driver or driver cluster dominated a market move.

### When to use

- User asks why an asset moved or which driver mattered most.

### What you get

A scoped method output for `Driver Dominance Analysis Skill` with method findings, evidence status, Method Confidence, limitations, missing IC gates, and structured handoff.

### What it will not do

It will not exceed the owning agent/workflow boundary, bypass evidence readiness, or issue final IC Action.

### Required inputs

- Asset and price move
- Current market context
- Relevant asset-driver map
- Fresh market/evidence data where needed

If required inputs are missing, continue only when a safe Preliminary or Limited scoped output is allowed; otherwise return Blocked with the missing inputs.

### Step sequence

1. Define price move
2. Select driver map
3. Detect context and surprise
4. Check what was priced in
5. Build driver battle matrix
6. Identify dominant/supporting/opposing/ignored drivers
7. Provide confirmation, alternative explanation, confidence, implication

Keep the method output scoped to the owning agent or workflow.

### Output contract

- Must use the standard method-output core from this document.
- Must state scope, assumptions, evidence status, Analysis Status, Method Confidence, limitations, missing IC gates, boundary, and structured handoff.
- Domain Findings must map to the step sequence and include only findings supported by the evidence status.
- Expected downstream artifact or section: `market_sense.md or driver dominance output`.
- Must not substitute for final IC memo schemas; P8-IC-01 owns final IC report schemas.

### Guardrails

- Do not overstate causality from weak evidence.
- Follow statuses, confidence, evidence display, source-scope, freshness, conflict, and writing rules in `implementation/00-master-rules.md`.
- Follow evidence readiness, provenance, source hierarchy, and pre-IC lock rules in `implementation/04-evidence-layer.md`.

### Failure states

- Complete when: Required inputs, evidence, boundary conditions, and domain checks are sufficient for `Complete for scoped method`; this does not imply Complete IC Action.
- Preliminary when: The skill can provide an early, narrow, or Quick Take-style method view before all method inputs or workflow gates are complete.
- Limited when: hypotheses are plausible but not confirmed.
- Blocked when: price move/context is unavailable.

### Quality checks

- Dominant driver explanation is bounded and evidence-aware.
- Output does not exceed the owning agent boundary.
- Material claims are evidence-aware.
- Required Template v2 metadata and UX blocks are present.
- Output uses the standard method-output core and structured handoff.
- Boundary prevents unauthorized IC Action, Action Box, exact sizing, or hidden recommendation.

## Market Sense Hypothesis Engine Skill

```yaml
contract_type: Skill
status: Canonical
owner: Market Sense Agent
used_by:
  - Market Sense Agent
produces:
  - market_sense.md or driver dominance output
  - market-sense-hypothesis-engine_structured_handoff
consumes:
  - market_observation_or_price_move
  - evidence_freshness_notes
  - pattern_reference_context_where_relevant
evidence_required: true
decision_boundary: Method output only; no ownership outside scope; no final IC Action.
known_gaps:
  - none
```

### Purpose

Generate plausible hypotheses for market moves or narrative shifts without overclaiming.

### When to use

- Market observation needs explanation but evidence is incomplete or multi-causal.

### What you get

A scoped method output for `Market Sense Hypothesis Engine Skill` with method findings, evidence status, Method Confidence, limitations, missing IC gates, and structured handoff.

### What it will not do

It will not exceed the owning agent/workflow boundary, bypass evidence readiness, or issue final IC Action.

### Required inputs

- Market observation or price move
- Evidence freshness notes
- Pattern/reference context where relevant

If required inputs are missing, continue only when a safe Preliminary or Limited scoped output is allowed; otherwise return Blocked with the missing inputs.

### Step sequence

1. Define observation
2. Generate candidate hypotheses
3. Map evidence for/against each hypothesis
4. Assign confidence
5. Identify confirm/disconfirm signals
6. Produce implications and handoff

Keep the method output scoped to the owning agent or workflow.

### Output contract

- Must use the standard method-output core from this document.
- Must state scope, assumptions, evidence status, Analysis Status, Method Confidence, limitations, missing IC gates, boundary, and structured handoff.
- Domain Findings must map to the step sequence and include only findings supported by the evidence status.
- Expected downstream artifact or section: `market_sense.md or driver dominance output`.
- Must not substitute for final IC memo schemas; P8-IC-01 owns final IC report schemas.

### Guardrails

- Do not turn hypotheses into facts or recommendations.
- Follow statuses, confidence, evidence display, source-scope, freshness, conflict, and writing rules in `implementation/00-master-rules.md`.
- Follow evidence readiness, provenance, source hierarchy, and pre-IC lock rules in `implementation/04-evidence-layer.md`.

### Failure states

- Complete when: Required inputs, evidence, boundary conditions, and domain checks are sufficient for `Complete for scoped method`; this does not imply Complete IC Action.
- Preliminary when: The skill can provide an early, narrow, or Quick Take-style method view before all method inputs or workflow gates are complete.
- Limited when: hypotheses are plausible but evidence is weak.
- Blocked when: observation cannot be defined.

### Quality checks

- Hypotheses include evidence status and disconfirming tests.
- Output does not exceed the owning agent boundary.
- Material claims are evidence-aware.
- Required Template v2 metadata and UX blocks are present.
- Output uses the standard method-output core and structured handoff.
- Boundary prevents unauthorized IC Action, Action Box, exact sizing, or hidden recommendation.

## Market Intelligence Briefing Skill

```yaml
contract_type: Skill
status: Canonical
owner: Market Intelligence Agent
used_by:
  - Market Intelligence Agent
produces:
  - market_intelligence_briefing.md
  - market-intelligence-briefing_structured_handoff
consumes:
  - market_news_data_sources
  - user_scope,_region,_asset_universe,_or_theme_focus
evidence_required: true
decision_boundary: Method output only; no ownership outside scope; no final IC Action.
known_gaps:
  - none
```

### Purpose

Produce market briefings that separate facts, relevance, and routing implications.

### When to use

- User asks for market briefing/update or workflow needs situational awareness.

### What you get

A scoped method output for `Market Intelligence Briefing Skill` with method findings, evidence status, Method Confidence, limitations, missing IC gates, and structured handoff.

### What it will not do

It will not exceed the owning agent/workflow boundary, bypass evidence readiness, or issue final IC Action.

### Required inputs

- Market news/data sources
- User scope, region, asset universe, or theme focus

If required inputs are missing, continue only when a safe Preliminary or Limited scoped output is allowed; otherwise return Blocked with the missing inputs.

### Step sequence

1. Collect material items
2. Separate facts from interpretation
3. Assess source/date confidence
4. Identify affected assets/themes
5. Route items to relevant agents
6. Produce briefing

Keep the method output scoped to the owning agent or workflow.

### Output contract

- Must use the standard method-output core from this document.
- Must state scope, assumptions, evidence status, Analysis Status, Method Confidence, limitations, missing IC gates, boundary, and structured handoff.
- Domain Findings must map to the step sequence and include only findings supported by the evidence status.
- Expected downstream artifact or section: `market_intelligence_briefing.md`.
- Must not substitute for final IC memo schemas; P8-IC-01 owns final IC report schemas.

### Guardrails

- Do not replace IC or issue final investment decision.
- Follow statuses, confidence, evidence display, source-scope, freshness, conflict, and writing rules in `implementation/00-master-rules.md`.
- Follow evidence readiness, provenance, source hierarchy, and pre-IC lock rules in `implementation/04-evidence-layer.md`.

### Failure states

- Complete when: Required inputs, evidence, boundary conditions, and domain checks are sufficient for `Complete for scoped method`; this does not imply Complete IC Action.
- Preliminary when: The skill can provide an early, narrow, or Quick Take-style method view before all method inputs or workflow gates are complete.
- Limited when: source coverage is partial.
- Blocked when: no reliable current sources are available.

### Quality checks

- Briefing is material, sourced, routed, and not decision-overclaiming.
- Output does not exceed the owning agent boundary.
- Material claims are evidence-aware.
- Required Template v2 metadata and UX blocks are present.
- Output uses the standard method-output core and structured handoff.
- Boundary prevents unauthorized IC Action, Action Box, exact sizing, or hidden recommendation.

## P5-SKL-01 acceptance checklist

- All 19 planned method skills are present with Template v2 metadata and UX blocks.
- Every skill defines required inputs, step sequence, output contract, guardrails, failure states, and quality checks.
- Every skill output uses human summary plus structured handoff.
- Non-IC skills cannot issue final `IC Action` or use `Action Box`.
- `Complete` for a skill means `Complete for scoped method` and does not imply Complete IC Action.
- Runtime `.agents/skills/*/SKILL.md` adapters remain concise and synchronized to this canonical document.
- QA coverage in `implementation/09-system-acceptance-qa.md` covers P5-SKL-01 structural and scenario checks.
