# Fixed Income internal full workflow Workflow Runbook

```yaml
contract_type: Workflow
status: Runtime Runbook
authority_level: Subordinate to canonical implementation documents
owner: Asset Intake Router / Investment Committee Agent
route: Fixed income / bond ETF / rates or credit exposure
used_by:
  - the user asks about a bond, bond ETF, Treasury duration exposure, credit exposure, yield, spread, carry, or fixed-income role in a portfolio
produces:
  - agent_workflow_audit.md
  - evidence_pack.md
  - etf_analysis.md
  - fixed_income_analysis.md
  - macro_sensitivity.md
  - valuation_expectations.md
  - risk_red_team.md
  - portfolio_fit.md
  - market_positioning.md
  - news_catalysts.md
  - market_sense.md
  - market_intelligence_briefing.md
  - decision_prep_memo.md
evidence_required: true
final_output_owner: Investment Committee Agent
decision_boundary: This runbook orchestrates the route. It does not create new IC Action rules, does not let non-IC agents issue final investment actions, and does not override canonical evidence, routing, report-schema, or language rules.
known_gaps:
  - none for runtime-runbook scope
```

Authority: this runtime runbook is subordinate to `implementation/00-master-rules.md`, `implementation/01-documentation-control.md`, `implementation/04-evidence-layer.md`, `implementation/05-routing-and-workflows.md`, `implementation/06-agent-contracts.md`, `implementation/07-investment-committee-and-report-schemas.md`, `implementation/11-skill-contracts.md`, `implementation/13-codex-runtime-architecture.md`, and `workflows/handoff_artifact_standard.md`. If this runbook conflicts with a canonical implementation document, the canonical document governs and the conflict must be surfaced as a source issue.

## Execution modes

Audit/run metadata must record exactly one controlled execution mode before the Runtime Execution Plan. Ordinary user-facing chat should hide technical runtime blocks unless the user explicitly asks for workflow/debug/audit details:

| Execution mode | Meaning | Requirement |
|---|---|---|
| `Non-delegated audit fallback` | The main Codex session executes the full workflow modules itself. | Do not claim that subagents ran. Use artifact-equivalent handoff summaries when separate files are not produced. |
| `Agent workflow with spawned subagents` | Relevant subagents are actually spawned and return structured handoff artifacts or artifact-equivalent summaries. | List spawned agents, skipped agents with reasons, consumed handoffs, and spawn limitations. |

An internal full workflow is the analytical route. `Agent workflow with spawned subagents` is the controlled execution mode when subagents actually run. They are not synonyms.

## Artifact selection

| Gate state | Required IC-stage artifact |
|---|---|
| Portfolio context is missing but analysis is useful for decision preparation | `decision_prep_memo.md` |
| Evidence, source access, freshness, provenance, or conflicts are the main limiting issue | `evidence_gap_memo.md` |
| Non-evidence analytical gates remain incomplete | `limited_ic_draft.md` |
| All required gates are complete and IC schemas allow final action | `final_investment_memo.md` |

Smoke tests default to `decision_prep_memo.md` and must not force `final_investment_memo.md`.

## Handoff rules

Every included module must produce a structured handoff artifact or artifact-equivalent summary using `workflows/handoff_artifact_standard.md`. Non-IC artifacts must state `Boundary: Not an IC Action` when action language could be inferred. Non-IC agents must not use `Action Box`, final buy/sell/hold/add/trim/exit language, exact trade instructions, or exact position sizing.

## Module statuses

Use only these module-status tokens: `Complete`, `Limited`, `Blocked`, `Not material`, or `Skipped with reason`. A workflow is not valid unless every included module has one visible valid status.


## Trigger

Use this workflow when the user asks about a bond, bond ETF, Treasury duration exposure, credit exposure, yield, spread, carry, or fixed-income role in a portfolio. If identity, wrapper, structure, currency, or instrument terms materially change the route, ask the minimum clarifying question before decision-critical analysis.

## What you get

A controlled Fixed income / bond ETF / rates or credit exposure workflow from intake through evidence, lead route analysis, relevant specialists, portfolio fit, and Investment Committee synthesis. For concrete-asset large-workflow work, `Agent workflow with spawned subagents` with relevant subagents is the canonical default when those subagents are available and actually spawned; if no subagents actually run, record `Non-delegated audit fallback` instead.

## Required agents and modules

| Agent / module | Role | Required behavior |
|---|---|---|
| `master-intake-router` | Required | Produces or validates its route-specific handoff; must not exceed its decision boundary. |
| `asset-intake-router` | Required | Produces or validates its route-specific handoff; must not exceed its decision boundary. |
| `evidence-collector` | Required | Produces or validates its route-specific handoff; must not exceed its decision boundary. |
| `etf-agent` | Required | Produces or validates its route-specific handoff; must not exceed its decision boundary. |
| `fixed-income-agent` | Required | Produces or validates its route-specific handoff; must not exceed its decision boundary. |
| `macro-agent` | Required | Produces or validates its route-specific handoff; must not exceed its decision boundary. |
| `valuation-expectations-agent` | Required | Produces or validates its route-specific handoff; must not exceed its decision boundary. |
| `risk-red-team-agent` | Required | Produces or validates its route-specific handoff; must not exceed its decision boundary. |
| `portfolio-fit-agent` | Required | Produces or validates its route-specific handoff; must not exceed its decision boundary. |
| `market-positioning-agent` | Required | Produces or validates its route-specific handoff; must not exceed its decision boundary. |
| `news-catalysts-agent` | Required | Produces or validates its route-specific handoff; must not exceed its decision boundary. |
| `market-sense-agent` | Required | Produces or validates its route-specific handoff; must not exceed its decision boundary. |
| `market-intelligence-agent` | Required | Produces or validates its route-specific handoff; must not exceed its decision boundary. |
| `investment-committee-agent` | Required | Produces or validates its route-specific handoff; must not exceed its decision boundary. |

## Conditional agents

| Agent / module | Role | Include when |
|---|---|---|
| `equity-agent` | Conditional | Issuer equity context is material to credit risk or convertible/hybrid analysis. |
| `sector-industry-analysis-agent` | Conditional | Corporate credit sector, bank credit, HY, or sector-default risk is material. |
| `commodity-agent` | Conditional | Inflation/commodity hedge comparison is explicit. |
| `crypto-agent` | Conditional | User compares fixed income to crypto or yield products. |
| `structural-winners-discovery-agent` | Conditional | User asks for bond or credit candidate discovery. |

## Mandatory artifacts

- `agent_workflow_audit.md`
- `evidence_pack.md`
- `etf_analysis.md`
- `fixed_income_analysis.md`
- `macro_sensitivity.md`
- `valuation_expectations.md`
- `risk_red_team.md`
- `portfolio_fit.md`
- `market_positioning.md`
- `news_catalysts.md`
- `market_sense.md`
- `market_intelligence_briefing.md`
- `decision_prep_memo.md`

## Sequence

1. Master Intake Router classifies the request, subject, intent, time horizon, source scope, and missing context.
2. Asset Intake Router confirms the route and required gate set.
3. The audit/run metadata records `Execution mode` and a Runtime Execution Plan with included modules, excluded modules, rationale, and module statuses; ordinary chat does not show those technical blocks unless requested.
4. Evidence Collector produces `evidence_pack.md` and a pre-IC evidence status.
5. Lead route agent produces the route-specific analysis artifact.
6. Required specialist agents produce their handoffs.
7. Portfolio Fit marks personal fit `Limited` when portfolio context is missing.
8. Investment Committee consumes only validated handoffs and produces the correct gate-aware IC-stage artifact.

## Spawned-subagent smoke-test fixture

Primary fixture: TLT as a bond ETF and long-duration Treasury exposure.

Required spawned agents for the smoke test:

- `master-intake-router`
- `asset-intake-router`
- `evidence-collector`
- `etf-agent`
- `fixed-income-agent`
- `macro-agent`
- `valuation-expectations-agent`
- `risk-red-team-agent`
- `portfolio-fit-agent`
- `market-positioning-agent`
- `news-catalysts-agent`
- `market-sense-agent`
- `market-intelligence-agent`
- `investment-committee-agent`

The spawned-subagent smoke test must include both `Spawned agents` and `Skipped agents with reason`. Skipped agents are acceptable only when they are not relevant to the route, not because an obligatory handoff failed. If a required agent cannot start or does not return the required artifact, the smoke test is blocked until the cause is fixed and the workflow is rerun.

## Route-specific notes

Fixed-income analysis must separate wrapper analysis from underlying rate/credit exposure. TLT is a bond ETF, not an individual bond. A single-bond verdict requires issuer, maturity, coupon, currency, seniority, CUSIP/ISIN, price/yield, liquidity, and structure.

## Acceptance checks

- The route does not reuse Equity metrics when the asset class requires a different framework.
- Every required artifact exists or the smoke test is blocked until it can be produced.
- `decision_prep_memo.md` is used by default for smoke tests when portfolio context is missing.
- `final_investment_memo.md` appears only when all required IC gates pass.
- Non-IC artifacts preserve `Boundary: Not an IC Action` and do not contain final action wording.
