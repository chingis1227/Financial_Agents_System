# spawned-subagent workflow Handoff Artifact Standard

```yaml
contract_type: Runtime Standard
standard_id: SESSION04-HANDOFF-01
status: Runtime Standard
version: 1.0
authority_level: Subordinate to canonical implementation documents
owner: Codex Runtime Architecture / Investment Committee Agent
used_by:
  - Non-delegated audit fallback workflows
  - Agent workflow with spawned subagents runs
  - Equity large-workflow workflow
produces:
  - structured_handoff_artifacts
consumes:
  - runtime_execution_plan
  - module_outputs
  - evidence_pack
evidence_required: true
decision_boundary: This standard defines handoff artifacts and minimum required fields. It does not create new IC Action rules, does not let non-IC agents issue final buy/sell/hold language, and does not override report schemas.
known_gaps:
  - none
```

Authority: this runtime standard is assembled from `implementation/00-master-rules.md`, `implementation/04-evidence-layer.md`, `implementation/05-routing-and-workflows.md`, `implementation/06-agent-contracts.md`, `implementation/07-investment-committee-and-report-schemas.md`, and `implementation/13-codex-runtime-architecture.md`. If this standard conflicts with those canonical documents, the canonical documents govern and the conflict is a source issue under `implementation/01-documentation-control.md`.

## Purpose

Every internal full workflow or spawned-subagent workflow module must leave an auditable `.md` handoff artifact or artifact-equivalent `.md` handoff summary before downstream synthesis uses it. The Investment Committee may synthesize only from validated handoff artifacts, artifact-equivalent handoff summaries, the runtime execution plan, and the pre-IC evidence lock. Unstructured agent-to-agent chat is not valid IC input.

In `Non-delegated audit fallback`, the main Codex session may create artifact-equivalent handoff summaries instead of spawned-agent files, but each included module must still be saved under `audit\` as its own clearly named `.md` handoff/report or module handoff file with the controlled artifact name and required fields below. If an `AGENT:` request cannot actually spawn relevant subagents, the user-facing saved report or chat output must be marked `Limited` and must not claim agent workflow execution. In `Agent workflow with spawned subagents`, spawned subagents must return separate structured handoff artifacts or clearly labeled artifact-equivalent summaries with the same fields, saved into the audit package before IC synthesis consumes them.

## Universal required fields

Each handoff artifact must include these fields near the top:

```markdown
## Handoff metadata
- Artifact:
- Subject:
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
- Missing gates:
- Decision boundary:
- Downstream handoff:
- Required follow-up:
```

Field rules:

- `Artifact` must use the controlled artifact name from the workflow or report schema.
- `Owner` must be a named agent, skill, or workflow owner from the runtime plan.
- `Output status` uses the base statuses `Complete`, `Limited`, `Blocked`, or `Preliminary`; module tables may also use `Not material` and `Skipped with reason` for excluded modules.
- `Evidence status` must state whether evidence is sufficient, limited, stale, conflicting, source-scoped, proxy-heavy, missing, or blocked for the artifact's scope.
- `Evidence limits` must describe material source, freshness, provenance, contradiction, access, proxy, or coverage limits.
- `Missing gates` must list unresolved evidence, valuation, risk, portfolio, implementation, identity, freshness, or specialist gates; use `None for this scope` only when true.
- `Decision boundary` must state whether the artifact is specialist input, evidence control, portfolio context, risk gate, or IC synthesis.
- `Downstream handoff` must name the next module(s) allowed to consume the artifact and the exact constraints that travel with it.

## Saved workflow package standard

Every full investment workflow creates a saved package outside the project repository:

```text
C:\Users\ShumeikoYe\OneDrive\Documents\Financial Agent Reports\[ASSET] yyyy-mm-dd hhmm\
```

Required package contents:

- `investment_report.md` — the exact reader-facing report reproduced in chat.
- `audit\run_metadata.md` — execution mode, runtime plan, included/excluded modules, actually spawned agents, fallback reason if no subagents were spawned, canonical internal artifact type, module statuses, and gate status.
- `audit\sources.md` — full source list and source/freshness notes when available.
- `audit\intake.md` — questions, answers, unanswered questions, and approved baseline assumptions used.
- one `.md` handoff/report for every actually run subagent or module.

Ordinary chat shows only the reader-facing report and the `investment_report.md` path. The audit path and technical materials are shown only when explicitly requested.

## Universal structured handoff block

Every artifact must end with or include this exact concise structured handoff block. Do not use alternate field names in new handoffs:

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

Compatibility mapping for older wording:

| Older / loose field | Controlled field to use now |
|---|---|
| `Status` | `Output status` |
| `Limitations` | `Key limitations` or `Evidence limits`, depending on meaning |
| `Downstream relevance` | `Downstream handoff` |
| `Downstream consumers` | `Downstream handoff` |
| `Producing skill` | `Producing agent/skill/workflow` |
| `Required follow-up` without recipient | `Required follow-up` plus recipient in `Downstream handoff` |

Non-IC artifacts that could be mistaken for final decision support must include:

```text
Boundary: Not an IC Action.
```

## Mandatory Equity large-workflow artifacts

These artifacts are the minimum handoff set for an Equity internal full workflow or public-equity spawned-subagent workflow. Conditional modules may add more artifacts, but they do not replace the mandatory set when their gates are material.

`decision_prep_memo.md` is the default IC-stage handoff artifact when the internal full workflow is otherwise usable but final action gates are not closed because portfolio context is missing. If evidence/freshness or other IC gates are the primary limitation, the required IC-stage handoff is the appropriate gate-aware IC artifact from `implementation/07-investment-committee-and-report-schemas.md`: `limited_ic_draft.md` or `evidence_gap_memo.md`. `final_investment_memo.md` is allowed only when canonical IC gates pass.

| Artifact | Owner | Required status and evidence fields | Required limitations and missing gates | Downstream handoff |
|---|---|---|---|---|
| `evidence_pack.md` | Evidence Collector Agent / Evidence Collection skill | Output status; evidence readiness; freshness status; source scope; claim-support map; pre-IC evidence lock status. | Missing sources, stale data, unavailable/premium data, conflicts, provenance issues, source-scope limits, proxy evidence, and evidence gates that constrain IC. | To Equity Agent, Financial Statement Analysis, Valuation, Risk, Portfolio Fit, conditional modules, and IC. It controls what claims downstream modules may use. |
| `macro_sensitivity.md` / `macro_context.md` | Macro Agent / Macro Analysis skill | Output status; macro evidence and freshness status; transmission relevance. | Missing or stale rates, inflation, growth, liquidity, FX, policy, or regime evidence; unclear transmission to the asset. | To lead asset agent, Valuation, Risk, Portfolio Fit, and IC as macro context. Must state `Boundary: Not an IC Action`. |
| `sector_context.md` / `sector_industry_analysis.md` | Sector / Industry Analysis Agent / skill | Output status; sector evidence status; industry structure and competitive context sufficiency. | Missing sector data, peer context, profit pool, regulatory, competitive, or cycle evidence. | To Equity Agent, Valuation, Risk, Portfolio Fit, and IC as sector/industry input. Must state `Boundary: Not an IC Action`. |
| `equity_company_analysis.md` | Equity Agent / Equity Company Analysis skill | Output status; evidence status inherited from `evidence_pack.md`; business/thesis evidence sufficiency. | Business-model limits, competitive/management/industry gaps, unsupported thesis claims, missing financial-statement inputs, missing valuation/risk/portfolio/IC gates. | To Valuation, Risk, Portfolio Fit, and IC as a scoped company-thesis input. Must state `Boundary: Not an IC Action`. |
| `financial_statement_analysis.md` | Financial Statement Analysis skill / Equity workflow contributor | Output status; filing/financial-data evidence status; accounting and cash-flow evidence sufficiency. | Missing filings, stale periods, restatement/accounting uncertainty, segment-data gaps, cash-flow quality limits, balance-sheet/dilution/capital-allocation gates. | To Equity Agent, Valuation, Risk, Portfolio Fit when relevant, and IC as financial-quality input. Must state `Boundary: Not an IC Action`. |
| `valuation_expectations.md` | Valuation & Expectations Agent / skill | Output status; valuation-input evidence status; price/freshness status; expectation-support status. | Missing current price, stale consensus/estimate inputs, weak valuation anchors, scenario sensitivity, assumption ranges, growth-expectations gaps, unsupported upside/downside claims. | To Risk, Portfolio Fit, and IC as valuation/expectations support. Must state `Boundary: Not an IC Action` and must not present an exact price target as final truth. |
| `risk_red_team.md` | Risk / Red Team Agent / skill | Output status; risk-evidence status; risk gate status; downside and counter-evidence support. | Unbounded downside, unresolved thesis breaks, missing stress cases, weak bear case evidence, risk-control gaps, implementation or liquidity gates when material. | To Portfolio Fit and IC as risk-gate input. Must state `Boundary: Not an IC Action` and must not issue buy/sell/hold. |
| `portfolio_fit.md` | Portfolio Fit Agent / skill | Output status; portfolio-context evidence status; personalization status; role-fit support. | Missing current position, objective, horizon, risk tolerance, exposure, constraints, overlap, sizing, tax/custody/access details when material. | To IC as portfolio role and personalization gate. Must state `Boundary: Not an IC Action` and must not provide exact trade instructions or exact allocation. |
| `decision_prep_memo.md` or other gate-aware IC artifact | Investment Committee Agent / IC synthesis skill | Output status; Analysis Status; IC Action Status; evidence/freshness status; confidence support; consumed handoff list. | Missing final-action gates, prohibited conclusions, portfolio/evidence/valuation/risk/implementation gaps, and what would upgrade to a Complete Final Memo. | Internal IC-stage artifact type recorded in audit. The user-facing saved file is always `investment_report.md`. `decision_prep_memo.md` is the default internal type when portfolio context is the remaining final-action gate; `limited_ic_draft.md` or `evidence_gap_memo.md` is used for other gate states. Non-final artifacts may provide working view only; no final positive IC Action and no `Action Box`. |

## IC consumption rule

Investment Committee synthesis must consume only:

1. the audit Runtime Execution Plan and module status table;
2. `evidence_pack.md` with pre-IC evidence lock or an explicitly Limited/Blocked evidence status;
3. required specialist handoff artifacts or artifact-equivalent summaries with the universal required fields;
4. conditional-module handoffs listed in the runtime plan when material;
5. user-provided context after provenance and sanity checks.

If a required artifact is missing, unstructured, stale, contradictory, or lacks owner/status/evidence limits/missing gates/downstream handoff, IC must either request the corrected handoff or select a gate-aware Limited/Blocked artifact such as `decision_prep_memo.md`, `limited_ic_draft.md`, or `evidence_gap_memo.md`. IC must not silently fill missing specialist work with assumptions.

## Non-IC action boundary

Evidence, asset, financial statement, valuation, risk, and portfolio artifacts are scoped inputs. They must not use `Action Box`, `IC Action`, final buy/sell/hold/add/trim/exit language, exact trade instructions, or exact position sizing. They may use scoped labels such as `Specialist Verdict`, `Valuation / Expectations Support`, `Risk Gate`, or `Portfolio Fit Box` only with `Boundary: Not an IC Action`.

## Artifact naming alignment

Use these controlled names for the mandatory Equity large-workflow handoff set. Macro and sector / industry handoffs are mandatory equity defaults unless audit records a justified `Not material` or `Skipped with reason`:

- `evidence_pack.md`
- `macro_sensitivity.md` / `macro_context.md`
- `sector_context.md` / `sector_industry_analysis.md`
- `equity_company_analysis.md`
- `financial_statement_analysis.md`
- `valuation_expectations.md`
- `risk_red_team.md`
- `portfolio_fit.md`
- one IC-stage gate-aware artifact: `decision_prep_memo.md` by default when portfolio context is the remaining final-action gate; otherwise `limited_ic_draft.md`, `evidence_gap_memo.md`, or `final_investment_memo.md` only when the IC schemas allow it

Final or gate-aware IC report names remain governed by `implementation/07-investment-committee-and-report-schemas.md`:

- `final_investment_memo.md`
- `decision_prep_memo.md`
- `limited_ic_draft.md`
- `evidence_gap_memo.md`

If a workflow needs a new artifact name, record it in the workflow runbook and check it against the IC report schemas. Do not invent an unofficial final-memo name.

## Quality checks

Before IC synthesis or final user-facing output, verify:

- Every included module has an artifact or artifact-equivalent summary.
- Every artifact has owner, output status, evidence status, evidence limits, missing gates, decision boundary, and downstream handoff.
- Evidence limits and missing gates are not hidden in prose.
- Non-IC artifacts include `Boundary: Not an IC Action` when action language could be inferred.
- IC consumed the listed handoffs, not raw chat.
- Artifact naming matches the workflow runbook and IC report schemas.
- The final artifact is gate-aware for the actual state of evidence, valuation, risk, portfolio, implementation, and freshness gates.

## Non-equity and multi-asset route-specific smoke-test artifact sets

The mandatory Equity internal full workflow set remains the reference pattern. The following route-specific smoke-test sets extend the same standard to ETF, commodity, crypto, fixed income, and multi-asset workflows. They are QA coverage fixtures, not permission to run irrelevant agents in ordinary workflows. Runtime routing still spawns only relevant modules, while macro remains a default full-asset-workflow module and any included module must leave an audit handoff before IC consumption.

### ETF large-workflow artifacts

Minimum smoke-test set for an ETF comparison such as QQQ vs SCHG:

- `agent_workflow_audit.md`
- `evidence_pack.md`
- `etf_analysis.md`
- `valuation_expectations.md`
- `risk_red_team.md`
- `portfolio_fit.md`
- `market_positioning.md`
- `macro_sensitivity.md`
- `news_catalysts.md`
- `market_sense.md`
- `market_intelligence_briefing.md`
- `sector_context.md`
- one IC-stage gate-aware artifact, defaulting to `decision_prep_memo.md` when portfolio context is missing

The ETF handoff must cover wrapper identity, methodology/index exposure, holdings, concentration, fees, liquidity, tracking, overlap, implementation limits, and whether the output is exposure analysis or a personal portfolio action.

### Commodity large-workflow artifacts

Minimum smoke-test set for a commodity setup such as gold:

- `agent_workflow_audit.md`
- `evidence_pack.md`
- `commodity_analysis.md`
- `macro_sensitivity.md`
- `market_positioning.md`
- `valuation_expectations.md`
- `risk_red_team.md`
- `portfolio_fit.md`
- `news_catalysts.md`
- `market_sense.md`
- `market_intelligence_briefing.md`
- one IC-stage gate-aware artifact, defaulting to `decision_prep_memo.md` when portfolio context is missing

The commodity handoff must cover physical balance, supply/demand, inventories, curve/term structure when relevant, macro transmission, policy, positioning, instrument choice, and implementation constraints.

### Crypto large-workflow artifacts

Minimum smoke-test set for a crypto asset such as BTC:

- `agent_workflow_audit.md`
- `evidence_pack.md`
- `crypto_analysis.md`
- `valuation_expectations.md`
- `macro_sensitivity.md`
- `market_positioning.md`
- `risk_red_team.md`
- `portfolio_fit.md`
- `news_catalysts.md`
- `market_sense.md`
- `market_intelligence_briefing.md`
- one IC-stage gate-aware artifact, defaulting to `decision_prep_memo.md` when portfolio context is missing

The crypto handoff must cover network use, token economics, liquidity, regulation, custody/security, implementation quality, protocol or exchange risks, drawdown behavior, and crypto-native valuation or expectations.

### Fixed Income large-workflow artifacts

Minimum smoke-test set for a bond ETF or fixed-income exposure such as TLT:

- `agent_workflow_audit.md`
- `evidence_pack.md`
- `etf_analysis.md` when the instrument is an ETF or fund wrapper
- `fixed_income_analysis.md`
- `macro_sensitivity.md`
- `valuation_expectations.md`
- `risk_red_team.md`
- `portfolio_fit.md`
- `market_positioning.md`
- `news_catalysts.md`
- `market_sense.md`
- `market_intelligence_briefing.md`
- one IC-stage gate-aware artifact, defaulting to `decision_prep_memo.md` when portfolio context is missing

The fixed-income handoff must separate wrapper quality from underlying yield, duration, curve, spread, credit, call/prepayment/extension, liquidity, tax/access, and implementation risks. A single-bond verdict is blocked until material instrument identifiers and terms are known.

### Multi-asset comparison artifacts

Minimum set for a cross-asset comparison such as BTC vs gold vs QQQ vs TLT:

- `agent_workflow_audit.md`
- `evidence_pack.md`
- every relevant asset-class lead artifact
- `valuation_expectations.md` or asset-class-equivalent expectations handoffs
- `macro_sensitivity.md`
- `market_positioning.md`
- `risk_red_team.md`
- `portfolio_fit.md`
- `cross_asset_comparison.md`
- one IC-stage gate-aware artifact, defaulting to `decision_prep_memo.md` when portfolio context is missing

The multi-asset handoff must use common criteria and asset-specific criteria. It must not declare an unconditional winner without the user's objective, portfolio context, and IC gates.

## Spawned-subagent smoke-test audit requirements

`agent_workflow_audit.md` is an operational audit artifact rather than a specialist handoff, but every smoke-test folder must include it. It must show:

- smoke-test subject and date;
- execution mode;
- expected final artifact;
- spawned agents with returned artifacts and statuses;
- skipped agents with reasons;
- required artifacts checklist;
- blocking issues and fixes attempted;
- final smoke-test result.

A spawned-subagent smoke test is not passed if a required agent was unavailable, a required artifact is missing, or an IC-stage artifact consumes unstructured chat instead of validated handoffs.

