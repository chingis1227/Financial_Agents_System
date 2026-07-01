# Standard Contract Templates

Status: Canonical template specification
Version: Template v2
Applies to: Agent, Skill, Workflow, and Report contracts

## 1. Purpose and operating model

These templates make future normalization work decision-complete. They define the minimum contract shape needed before legacy PRDs, skills, workflows, and report schemas can be normalized without implementers inventing missing fields.

P2-TPL-01 is a template layer only. It does not normalize every legacy PRD, generate runtime agents, or implement workflows. Those tasks remain in later agent, skill, routing, evidence, IC, and QA work items.

## 2. Template principles

- Use compact runtime contracts. Long methodologies, examples, analytical playbooks, and market details belong in supporting references unless they are required guardrails.
- Use Markdown for human readability plus a compact YAML metadata header for validation.
- If required information is missing, write `Known gaps / Pending decision`; do not silently fill gaps with assumptions.
- Agent contracts own role, scope, boundaries, inputs, outputs, status behavior, and handoffs.
- Skill contracts own repeatable method, step sequence, guardrails, failure states, and quality checks.
- Frameworks and references may provide report shape, examples, labels, and analytical detail, but they do not override canonical contracts.
- Source policies point to the central Evidence Layer unless a domain-specific overlay is explicitly required.
- Direct specialist outputs, discovery outputs, and quick takes must not masquerade as final IC actions.

## 3. Required metadata header

Every contract must include a compact metadata block immediately after the Markdown title. The generic metadata fields below are the minimum required fields for validation.

```yaml
contract_type: Agent | Skill | Workflow | Report
status: Canonical | Draft | Deprecated
owner: [agent, workflow owner, or documentation owner]
used_by:
  - [agent/workflow/report]
produces:
  - [artifact or structured output]
consumes:
  - [input artifact/context]
evidence_required: true | false
decision_boundary: [what this contract may and may not decide]
known_gaps:
  - [Known gaps / Pending decision, or none]
```

Additional metadata is allowed when useful, such as `category`, `trigger`, `artifact`, `final_output_owner`, or `source_refs`.

## 4. User-facing UX block

Each Agent, Skill, Workflow, and Report contract must include these short plain-language sections:

```markdown
## When to use
[User request or workflow situation that should trigger this contract.]

## What you get
[The practical user-facing output or internal handoff produced.]

## What it will not do
[Important boundaries in plain language.]
```

## 5. Agent Contract Template

Use this structure for every agent.

````markdown
# [Agent Name] - Agent Contract

```yaml
contract_type: Agent
status: Canonical | Draft | Deprecated
category: Router | Evidence | Asset-Class Lead | Specialist | Discovery | Synthesis / IC
owner: [agent name]
used_by:
  - [workflow/router]
produces:
  - [report artifact]
  - [structured handoff]
consumes:
  - [input artifact/context]
evidence_required: true | false
decision_boundary: [allowed verdicts and prohibited decisions]
known_gaps:
  - [Known gaps / Pending decision, or none]
```

## Purpose
[What this agent exists to answer.]

## When to use
[User request or workflow trigger.]

## What you get
[Expected practical output.]

## What it will not do
[Boundaries and prohibited ownership.]

## Scope
[Situations, instruments, workflows, and exclusions.]

## Responsibilities
- [Owned responsibility]

## Non-responsibilities
- [Boundary / prohibited ownership]

## Required inputs
- [Input artifact or context]

## Outputs
- [Report artifact]
- [Structured handoff]

## Evidence requirements
- [Freshness, source, readiness, and evidence profile requirements]

## Workflow role
[When it runs and dependencies.]

## Handoffs
Use only structured handoff blocks. Do not use uncontrolled agent-to-agent chat.

- To Evidence Collector: [requests/challenges]
- To downstream agents: [structured output]
- To IC: [final handoff block]

## Status and failure rules
- Complete when: [...]
- Preliminary when: [...]
- Limited when: [...]
- Blocked when: [...]

## Category-specific add-on
[Required add-on from section 6.]

## Success criteria
- [Observable completion condition]
````

## 6. Agent category-specific add-ons

Every Agent Contract uses the base template plus the add-on for its category.

| Category | Required add-on |
|---|---|
| Router | Routing defaults, ambiguity handling, safe bounded defaults, escalation to clarification, and proof that router does not issue investment decisions. |
| Evidence | Source hierarchy, freshness rules, claim support statuses, readiness, conflict handling, provenance checks, and pre-IC evidence lock behavior. |
| Asset-Class Lead | Covered instruments, asset-specific gates, specialist verdict boundary, downstream handoff needs, and `Boundary: Not an IC Action`; IC handoff is input only. |
| Specialist | Trigger conditions, scoped verdict labels, missing IC gates, direct-specialist behavior, and `Boundary: Not an IC Action`. |
| Discovery | Candidate/theme ranking method, `Candidate Discovery, Not Investment Action` boundary, missing asset-level gates, and no buy/sell language. |
| Synthesis / IC | Evidence lock, required specialist inputs, conflict synthesis, positive-action gates, `Action Box` use, `IC Action`, and final memo constraints. |

## 7. Skill Contract Template

````markdown
# [Skill Name] - Skill Contract

```yaml
contract_type: Skill
status: Canonical | Draft | Deprecated
owner: [skill owner]
used_by:
  - [agent/workflow]
produces:
  - [method output or handoff]
consumes:
  - [required inputs]
evidence_required: true | false
decision_boundary: [method output only; no ownership outside scope]
known_gaps:
  - [Known gaps / Pending decision, or none]
```

## Purpose
[Repeatable method this skill performs.]

## When to use
[Trigger conditions.]

## What you get
[Method output.]

## What it will not do
[Prohibited behavior and decision boundary.]

## Required inputs
- [Required context/artifacts]

## Step sequence
1. [Step]
2. [Step]

## Output contract
- [Expected output]
- [Required fields]

## Guardrails
- [Prohibited behavior]

## Failure states
- Complete when: [...]
- Preliminary when: [...]
- Limited when: [...]
- Blocked when: [...]

## Quality checks
- [How to verify output quality]
````

## 8. Workflow Contract Template

````markdown
# [Workflow Name] - Workflow Contract

```yaml
contract_type: Workflow
status: Canonical | Draft | Deprecated
owner: [router/orchestrator]
used_by:
  - [request family]
produces:
  - [required reports]
consumes:
  - [entry inputs and evidence]
evidence_required: true | false
final_output_owner: [agent]
decision_boundary: [allowed final output and prohibited shortcuts]
known_gaps:
  - [Known gaps / Pending decision, or none]
```

## Trigger
[Request type.]

## When to use
[User request or workflow situation.]

## What you get
[Final workflow output and important intermediate outputs.]

## What it will not do
[Boundaries, shortcuts, and prohibited finality.]

## Entry conditions
- [What starts the workflow]

## Required agents
- [Agent]

## Optional / conditional agents
- [Agent and trigger]

## Sequence
1. Intake and routing
2. Evidence plan
3. Specialist execution
4. Evidence readiness check
5. Final synthesis or Limited/Blocked output

## Scoped mode
- Allowed when: [scoped user request or limited workflow]
- Excluded blocks: [what was not run]
- Maximum allowed status: [Preliminary/Limited/Complete for stated scoped output]
- Prohibited conclusions: [what cannot be concluded without excluded blocks]

## Required reports
- [artifact.md]

## Evidence requirements
- [readiness/freshness/source requirements]

## Completion rules
- Complete when: [...]
- Preliminary when: [...]
- Limited when: [...]
- Blocked when: [...]

## Positive action gates
- [If applicable]
````

## 9. Report Schema Template

````markdown
# [Report Name] - Report Schema

```yaml
contract_type: Report
status: Canonical | Draft | Deprecated
artifact: [file_name.md]
owner: [agent/skill]
used_by:
  - [agents/workflows]
produces:
  - [reader-facing report]
consumes:
  - [evidence/specialist/workflow inputs]
evidence_required: true | false
decision_boundary: [allowed labels and prohibited finality]
status_values:
  - Complete
  - Limited
  - Blocked
  - Preliminary
known_gaps:
  - [Known gaps / Pending decision, or none]
```

## When to use
[When this report should be produced.]

## What you get
[Reader-facing purpose.]

## What it will not do
[Boundary and prohibited labels.]

## Required metadata
- Subject:
- Request type:
- As-of date:
- Output status:
- Evidence status:
- Evidence limits:
- Key limitations:
- Missing gates:
- Source scope:
- Decision boundary:
- Downstream handoff:

## Required sections
1. Executive summary
2. Core analysis
3. Evidence notes and limitations
4. Monitoring / triggers
5. Structured handoff

## Optional sections
- [Conditional sections]

## Handoff block
- Downstream handoff:
- Required follow-up:
- Decision constraints:

## Status and failure rules
- Complete when: [...]
- Preliminary when: [...]
- Limited when: [...]
- Blocked when: [...]
````

## 10. Status and evidence failure-state rules

Every contract must define `Complete`, `Preliminary`, `Limited`, and `Blocked` behavior for its stated scope.

| Status | Template meaning |
|---|---|
| Complete | Required inputs and gates are sufficient for the stated scope. Complete specialist output does not imply complete IC action. |
| Preliminary | Early or narrow output that may improve with further workflow steps. Quick Takes are always Preliminary or Limited and never final IC Actions; if full gates are being completed, route or upgrade to internal full workflow / IC synthesis. |
| Limited | Output can proceed, but source scope, evidence quality, freshness, workflow exclusions, or missing gates constrain conclusion strength. |
| Blocked | The requested conclusion must not be made until required input, evidence, clarification, or gate resolution is available. |

Required evidence behaviors:

- Freshness-dependent requests such as today, now, latest, current price action, news, or earnings require current sources with timestamps; otherwise downgrade to Limited or Blocked.
- If the user restricts sources, respect the restriction and mark the output `Limited by source scope`.
- User-provided files require provenance and sanity checks before claims are used as evidence.
- Material conflicting sources trigger an `Evidence Conflict` note, authority ranking, materiality assessment, and Limited/Blocked status if decision-critical.
- Missing, stale, paywalled, proxy-heavy, or weak evidence must constrain claim strength and downstream conclusions.

## 11. Structured handoff block

Handoffs must be structured artifacts, not uncontrolled agent-to-agent chat.

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

For large workflow / spawned-subagent workflow runs, `workflows/handoff_artifact_standard.md` provides the executable field standard and compatibility mapping. New handoffs should use these controlled field names rather than aliases such as `Status`, `Limitations`, or `Downstream relevance`.

## 12. Decision label permissions

| Label | Allowed owner | Template rule |
|---|---|---|
| Specialist Verdict | Asset-class or specialist agent | Domain-specific conclusion only; must not be final IC action. |
| Actionability Label | Domain owner where explicitly defined, including asset-class, specialist, discovery, or IC workflow owner | Setup quality, watchlist/defer/not-actionable, or next-step priority label; non-IC outputs must state missing gates. |
| Vehicle Quality Verdict | ETF / wrapper / implementation-quality analysis | Quality of vehicle or wrapper only; not a portfolio action. |
| Quality Verdict | Asset-class or domain owner | Business, asset, theme, or vehicle quality only; not a statement that the asset is a good purchase now. |
| Valuation / Expectations Support | Valuation owner or asset-class equivalent | Whether price, expectations, or scenario payoff support the proposed decision. |
| Investment View | Investment Committee only | Integrated final view in the memo, constrained by evidence, valuation, risk, and implementation context. |
| IC Action | Investment Committee only | Final decision-support action label. Requires evidence lock and required gates. |

`Action Box` is reserved for IC-level final memos. Direct specialist reports, discovery outputs, market reaction notes, and non-IC workflow artifacts must use scoped boxes with `Boundary: Not an IC Action` when needed.

## 13. Gate catalogue for template add-ons

Use these gates when the trigger condition applies. A gate may be in an Agent, Skill, Workflow, or Report contract depending on ownership.

| Gate | Trigger | Required behavior |
|---|---|---|
| Ambiguous instrument gate | Ticker, listing, share class, maturity, currency, or structure is unclear. | Use safe bounded default with explicit assumption when obvious; ask clarification when materially ambiguous. |
| Freshness gate | Request depends on today/now/latest/earnings/current market data. | Require current sources and timestamps; otherwise Limited/Blocked. |
| Source-scope gate | User restricts sources to provided files, no internet, or named reports only. | Respect the restriction, show source scope, mark `Limited by source scope`, and list checks needed for full evidence. |
| Evidence-conflict gate | Material sources disagree on a claim. | Apply source authority ranking, materiality filter, visible `Evidence Conflict`, and Limited/Blocked status if decision-critical. |
| User-file provenance gate | User provides PDF, spreadsheet, screenshot, notes, deck, CSV, or portfolio export. | Record provenance/as-of/type, run sanity checks, state limitations, and do not treat file claims as authoritative automatically. |
| Scoped-workflow gate | User asks for partial workflow or excludes blocks. | State excluded blocks, maximum allowed status, missing gates, and prohibited conclusions. |
| Direct specialist gate | User asks a specialist to decide buy/sell/hold. | Provide scoped verdict only, `Boundary: Not an IC Action`, missing IC gates, and optional IC routing. |
| Quick Take gate | User asks for a short answer. | Use `Preliminary Quick Take` or `Limited Quick Take`; no final IC action. |
| Premature final-report gate | User asks for final report before gates. | Produce a gate-aware artifact such as `Preliminary Investment Brief`, `Limited IC Draft`, `Evidence Gap Memo`, `Decision-Prep Memo`, or `Specialist Summary`. |
| Complex-product gate | Leveraged/inverse ETF, options strategy, structured note, HY bond, crypto yield, VIX product, or similar. | Analyze structure, payoff/exposure mechanics, liquidity, leverage/path dependency, counterparty/issuer risk, and suitability constraints. |
| Value-trap gate | Asset looks cheap by multiples, drawdown, yield, or discount. | Analyze why cheap, earnings quality, balance sheet, cyclicality, structural decline, governance/accounting red flags, catalyst/path, and downside. |
| Growth-expectations gate | Asset has expensive growth valuation. | Bridge implied growth/margins/duration, what must go right, disappointment downside, sustaining catalyst, and compounding evidence. |
| Catalyst/path gate | Strong positive conclusion is considered. | Require catalyst, path to value realization, confirmation/invalidation evidence, timeframe, and monitoring triggers. |
| Portfolio-fit gate | User asks fit/sizing/context. | Separate General Portfolio Fit from Personalized Portfolio Fit; no personalized sizing without portfolio data and constraints. |
| Sparse-data / illiquidity gate | Private, microcap, OTC, illiquid, sparse-coverage, or poorly disclosed asset. | Map data availability, liquidity/pricing quality, source bias, stale quote risk, governance/disclosure risk, sizing constraints, and confidence downgrade. |
| ETF vehicle-quality gate | ETF, ETN, fund wrapper, or basket vehicle. | Assess exposure purity, methodology, fees, liquidity, tracking, concentration, structure/tax, alternatives, and Vehicle Quality Verdict. |
| Fixed-income terms gate | Bond or credit instrument lacks issue terms. | Without maturity/currency/seniority/yield, provide preliminary issuer credit overview only; no bond-level verdict. |
| Crypto-native risk gate | Crypto, token, stablecoin, DeFi, staking/yield, bridge, L2, exchange token. | Classify asset, custody/liquidity, tokenomics/unlocks, protocol/security, regulatory risk, on-chain quality, and DeFi/stablecoin checks. |
| Commodity-structure gate | Commodity, futures, commodity ETF/ETN, producer, or physical exposure. | Identify exposure type, curve/inventory, supply-demand, seasonality, roll yield, geopolitics/policy, and cost curve where relevant. |
| Macro transmission gate | Macro variable is linked to asset or portfolio outcome. | State surprise vs expectations, transmission mechanism, timeframe, sensitivity, positioning, scenarios, and falsification. |
| News materiality gate | News, catalysts, rumors, filings, price reaction. | Classify source type, timestamp, materiality, expected-vs-actual, affected driver, reaction vs fundamentals, horizon, and stale-news filter. |
| Discovery boundary gate | Theme/discovery output ranks candidates. | Label as `Candidate Discovery, Not Investment Action`, show ranking criteria and missing gates, and avoid buy/sell language. |
| Run-all-agents gate | User asks to run all agents. | Interpret as full relevant workflow; list included/excluded agents when useful. |

## 14. Top-35 P2-TPL-01 edge-case decisions

These decisions are canonicalized as template behavior and support the detailed template sections above.

| Rule ID | Decision |
|---|---|
| P2-TPL-01-01 | Use practical templates with explicit `Known gaps / Pending decision`, not hidden assumptions. |
| P2-TPL-01-02 | Keep contracts compact; move long details to supporting references. |
| P2-TPL-01-03 | Separate Agent role/boundary ownership from Skill method/quality-check ownership. |
| P2-TPL-01-04 | Use base Agent template plus category-specific required add-ons. |
| P2-TPL-01-05 | Include `When to use`, `What you get`, and `What it will not do` UX blocks. |
| P2-TPL-01-06 | Use Markdown plus compact metadata header. |
| P2-TPL-01-07 | Require metadata minimum: `contract_type`, `status`, `owner`, `used_by`, `produces`, `consumes`, `evidence_required`, `decision_boundary`, and `known_gaps`. |
| P2-TPL-01-08 | Require evidence failure states in every contract. |
| P2-TPL-01-09 | Allow direct specialist outputs only as scoped verdicts with boundary and missing IC gates. |
| P2-TPL-01-10 | Allow Quick Takes only as Preliminary or Limited. |
| P2-TPL-01-11 | Use gate-aware non-final artifacts when final gates are missing. |
| P2-TPL-01-12 | Use safe bounded default plus explicit assumptions for instruments; clarify material ambiguity. |
| P2-TPL-01-13 | Require current sources for freshness-dependent requests; otherwise downgrade status. |
| P2-TPL-01-14 | Respect source restrictions and mark `Limited by source scope`. |
| P2-TPL-01-15 | Use conflict protocol with materiality filter. |
| P2-TPL-01-16 | Require user-file provenance and sanity checks before evidence use. |
| P2-TPL-01-17 | Permit scoped workflow mode with exclusions, status limit, and prohibited conclusions. |
| P2-TPL-01-18 | Distinguish Preliminary from Limited. |
| P2-TPL-01-19 | Treat `run all agents` as full relevant workflow, not literal all agents. |
| P2-TPL-01-20 | Use structured handoff blocks only. |
| P2-TPL-01-21 | Add label permissions matrix and reserve `IC Action` for IC. |
| P2-TPL-01-22 | Allow discovery ranking only as non-actionable candidate ranking. |
| P2-TPL-01-23 | Require complex-product gate. |
| P2-TPL-01-24 | Require value-trap gate for cheap-looking assets. |
| P2-TPL-01-25 | Require growth-expectations bridge for expensive growth assets. |
| P2-TPL-01-26 | Require catalyst/path gate before strong positive conclusions. |
| P2-TPL-01-27 | Separate General Portfolio Fit from Personalized Portfolio Fit. |
| P2-TPL-01-28 | Require sparse-data / illiquidity gate and confidence downgrade. |
| P2-TPL-01-29 | Require ETF vehicle-quality gate and Vehicle Quality Verdict. |
| P2-TPL-01-30 | Require fixed-income instrument-terms gate. |
| P2-TPL-01-31 | Require crypto-native risk gate. |
| P2-TPL-01-32 | Require commodity-structure gate. |
| P2-TPL-01-33 | Require macro transmission gate. |
| P2-TPL-01-34 | Require news materiality gate. |
| P2-TPL-01-35 | Use checklist plus scenario-based QA, not field-presence checks alone. |

## 15. Normalization rule

When converting legacy PRDs:

- Agent PRD owns scope, responsibility, boundaries, and outputs.
- Method Skill PRD owns procedure and quality checks.
- Framework owns report shape, labels, examples, and reference material.
- Source policies point to the central Evidence Layer unless truly domain-specific.
- Success criteria must be explicit; `Final Standard` can be retained only if mapped to Success Criteria.
- Missing required fields must be marked as `Known gaps / Pending decision`.
- Legacy detail that expands but does not change canonical behavior may be referenced as supporting detail.
- Legacy detail that conflicts with canonical templates or master rules must be recorded as a source issue and not used as an active rule.

## 16. Template acceptance checklist

P2-TPL-01 is complete when:

- Agent, Skill, Workflow, and Report templates each include required metadata, `known_gaps`, and UX blocks.
- Category-specific add-ons exist for Router, Evidence, Asset-Class Lead, Specialist, Discovery, and Synthesis / IC agents.
- Every template has Complete, Preliminary, Limited, and Blocked behavior.
- Label permissions prevent non-IC contracts from issuing final IC Actions.
- Structured handoff block is defined as the only handoff format.
- Gate catalogue covers ambiguity, freshness, source restrictions, conflicts, user files, scoped workflows, complex products, value traps, expensive growth, catalyst/path, portfolio fit, sparse data, ETF, fixed income, crypto, commodities, macro, and news/catalysts.
- Scenario-based QA exists in `implementation/09-system-acceptance-qa.md`.
