# Multi-Asset spawned-subagent workflow Runbook

```yaml
contract_type: Workflow
status: Runtime Runbook
authority_level: Subordinate to canonical implementation documents
owner: Master Intake Router / Investment Committee Agent
route: Cross-asset comparison
used_by:
  - Cross-asset comparisons such as BTC vs gold vs QQQ vs TLT
produces:
  - agent_workflow_audit.md
  - evidence_pack.md
  - asset-class-specific handoff artifacts
  - cross_asset_comparison.md
  - portfolio_fit.md
  - decision_prep_memo.md
evidence_required: true
final_output_owner: Investment Committee Agent
decision_boundary: This runbook compares asset classes without declaring an absolute winner unless user criteria and IC gates support it.
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

Use this workflow when the user compares assets across different classes, for example BTC, gold, QQQ, and TLT, or asks which asset is better without a single asset-class route being sufficient.

## What you get

A normalized comparison that combines common criteria with asset-specific criteria. The workflow avoids forcing BTC, gold, ETFs, and fixed income into one inappropriate metric set.

## Required behavior

- Use common criteria: role, horizon, liquidity, drawdown, inflation/rate sensitivity, expected-return support, implementation quality, evidence quality, and portfolio role.
- Use asset-specific criteria: ETF wrapper quality for ETFs, physical/macro setup for commodities, crypto-native risk for crypto, and yield/duration/credit structure for fixed income.
- Do not declare an absolute winner without user objective, portfolio context, and IC gates.
- Default to `decision_prep_memo.md` when the comparison is useful but portfolio context is missing.

## Required agents and modules

- `master-intake-router`
- `asset-intake-router`
- `evidence-collector`
- one or more lead asset-class agents: `etf-agent`, `commodity-agent`, `crypto-agent`, `fixed-income-agent`, `equity-agent` when applicable
- `valuation-expectations-agent`
- `macro-agent`
- `market-positioning-agent`
- `risk-red-team-agent`
- `portfolio-fit-agent`
- `market-sense-agent` when driver explanation is material
- `market-intelligence-agent` when market context is material
- `investment-committee-agent`

## Mandatory artifacts

- `agent_workflow_audit.md`
- `evidence_pack.md`
- route-specific lead artifacts for every compared asset class
- `valuation_expectations.md` or asset-class-equivalent expectations handoff
- `macro_sensitivity.md`
- `market_positioning.md`
- `risk_red_team.md`
- `portfolio_fit.md`
- `cross_asset_comparison.md`
- `decision_prep_memo.md`

## Acceptance checks

- The workflow lists included and excluded agents with reasons.
- Each asset class is analyzed by its correct lead route.
- Common comparison criteria and asset-specific criteria are both visible.
- The final output does not turn a context-dependent comparison into an unconditional buy list.
