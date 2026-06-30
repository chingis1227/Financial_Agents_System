# Commodity Full Cycle Workflow Runbook

```yaml
contract_type: Workflow
status: Runtime Runbook
authority_level: Subordinate to canonical implementation documents
owner: Asset Intake Router / Investment Committee Agent
route: Commodity / commodity-linked exposure
used_by:
  - the user asks whether gold, oil, copper, or another commodity is attractive, investable, cheap, or suitable for a capital-allocation horizon
produces:
  - delegated_workflow_audit.md
  - evidence_pack.md
  - commodity_analysis.md
  - macro_sensitivity.md
  - market_positioning.md
  - valuation_expectations.md
  - risk_red_team.md
  - portfolio_fit.md
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
| `Single-agent Full Cycle` | The main Codex session executes the full workflow modules itself. | Do not claim that subagents ran. Use artifact-equivalent handoff summaries when separate files are not produced. |
| `Delegated Full Agent Workflow` | Relevant subagents are actually spawned and return structured handoff artifacts or artifact-equivalent summaries. | List spawned agents, skipped agents with reasons, consumed handoffs, and delegation limitations. |

A Full Cycle is the analytical route. A delegated workflow is the runtime mode. They are not synonyms.

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

Use this workflow when the user asks whether gold, oil, copper, or another commodity is attractive, investable, cheap, or suitable for a capital-allocation horizon. If identity, wrapper, structure, currency, or instrument terms materially change the route, ask the minimum clarifying question before decision-critical analysis.

## What you get

A controlled Commodity / commodity-linked exposure workflow from intake through evidence, lead route analysis, relevant specialists, portfolio fit, and Investment Committee synthesis. For concrete-asset Full Cycle work, delegated execution with relevant subagents is the canonical default when those subagents are available and actually spawned; if no subagents actually run, record `Single-agent Full Cycle` instead.

## Required agents and modules

| Agent / module | Role | Required behavior |
|---|---|---|
| `master-intake-router` | Required | Produces or validates its route-specific handoff; must not exceed its decision boundary. |
| `asset-intake-router` | Required | Produces or validates its route-specific handoff; must not exceed its decision boundary. |
| `evidence-collector` | Required | Produces or validates its route-specific handoff; must not exceed its decision boundary. |
| `commodity-agent` | Required | Produces or validates its route-specific handoff; must not exceed its decision boundary. |
| `macro-agent` | Required | Produces or validates its route-specific handoff; must not exceed its decision boundary. |
| `market-positioning-agent` | Required | Produces or validates its route-specific handoff; must not exceed its decision boundary. |
| `valuation-expectations-agent` | Required | Produces or validates its route-specific handoff; must not exceed its decision boundary. |
| `risk-red-team-agent` | Required | Produces or validates its route-specific handoff; must not exceed its decision boundary. |
| `portfolio-fit-agent` | Required | Produces or validates its route-specific handoff; must not exceed its decision boundary. |
| `news-catalysts-agent` | Required | Produces or validates its route-specific handoff; must not exceed its decision boundary. |
| `market-sense-agent` | Required | Produces or validates its route-specific handoff; must not exceed its decision boundary. |
| `market-intelligence-agent` | Required | Produces or validates its route-specific handoff; must not exceed its decision boundary. |
| `investment-committee-agent` | Required | Produces or validates its route-specific handoff; must not exceed its decision boundary. |

## Conditional agents

| Agent / module | Role | Include when |
|---|---|---|
| `etf-agent` | Conditional | Implementation is through GLD, IAU, futures ETF, commodity ETF, or another wrapper. |
| `equity-agent` | Conditional | User asks through miners, producers, or commodity-linked equities. |
| `fixed-income-agent` | Conditional | Rates, real yields, or Treasury alternatives are the explicit comparison. |
| `sector-industry-analysis-agent` | Conditional | Commodity producer sector structure is material. |
| `crypto-agent` | Conditional | User asks BTC vs gold or a crypto/commodity comparison. |

## Mandatory artifacts

- `delegated_workflow_audit.md`
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

## Delegated smoke-test fixture

Primary fixture: Gold setup as a commodity investment question.

Required spawned agents for the smoke test:

- `master-intake-router`
- `asset-intake-router`
- `evidence-collector`
- `commodity-agent`
- `macro-agent`
- `market-positioning-agent`
- `valuation-expectations-agent`
- `risk-red-team-agent`
- `portfolio-fit-agent`
- `news-catalysts-agent`
- `market-sense-agent`
- `market-intelligence-agent`
- `investment-committee-agent`

The delegated smoke test must include both `Spawned agents` and `Skipped agents with reason`. Skipped agents are acceptable only when they are not relevant to the route, not because an obligatory handoff failed. If a required agent cannot start or does not return the required artifact, the smoke test is blocked until the cause is fixed and the workflow is rerun.

## Route-specific notes

Commodity analysis must use physical balance, inventory, curve, macro, policy, positioning, instrument, and implementation context rather than company-style DCF. Gold requires real-rate, dollar, central-bank-demand, ETF-flow, positioning, and geopolitical context.

## Acceptance checks

- The route does not reuse Equity metrics when the asset class requires a different framework.
- Every required artifact exists or the smoke test is blocked until it can be produced.
- `decision_prep_memo.md` is used by default for smoke tests when portfolio context is missing.
- `final_investment_memo.md` appears only when all required IC gates pass.
- Non-IC artifacts preserve `Boundary: Not an IC Action` and do not contain final action wording.
