---
name: valuation-expectations
description: Use for scoped valuation and expectations work: what is priced in, scenario support, multiples/DCF or asset-class equivalent, and valuation gates; does not issue final IC Action.
---

# Valuation & Expectations Method Skill

Runtime status: Runtime-Ready. Canonical source of truth: `implementation/11-skill-contracts.md`.

## Purpose

Assess whether market price is justified by realistic expectations.

This runtime skill executes the reusable method contract without overriding agent, workflow, evidence, or IC boundaries.

## When to use

- Price/action or valuation context is decision-relevant.

Use only after reading `AGENTS.md` and the canonical documents needed for the task.

## What you get

A scoped method output with method findings, evidence status, Method Confidence, limitations, missing IC gates, and structured handoff.

## What it will not do

It must not bypass evidence readiness, source limitations, workflow routing, or IC gates. Legacy PRDs are source material only through the registry and traceability matrix.

## Required canonical documents

Read only the canonical documents needed for the task. Default required set:

- `implementation/00-master-rules.md`
- `implementation/01-documentation-control.md`
- `implementation/04-evidence-layer.md`
- `implementation/06-agent-contracts.md` for owning agent boundaries
- `implementation/11-skill-contracts.md` for this skill contract
- `workflows/handoff_artifact_standard.md` when producing large workflow or spawned-subagent workflow handoffs

Conditional references:

- `implementation/03-contract-templates.md` when editing or validating contracts
- `implementation/09-system-acceptance-qa.md` when running QA or acceptance checks
- `implementation/10-traceability-matrix.md` when using legacy detail
- `implementation/13-codex-runtime-architecture.md` when runtime packaging rules matter

## Required inputs

- Price/market cap/EV
- Financial history and forecast inputs
- Business-quality assumptions
- Peer/historical/consensus context where available

If inputs are missing, continue only when a safe Preliminary or Limited scoped method output is allowed; otherwise return Blocked with missing inputs.

## Step sequence

1. Check data integrity
2. Select valuation context and methods
3. Reverse-engineer implied expectations
4. Build scenario valuation range
5. Build return bridge
6. Reconcile methods and risks
7. Define monitoring signals

Keep the method output scoped to the owning agent or workflow.

## Required output core

Every output must include:

- Method Output Summary
- Analysis Status (`Complete for scoped method`, `Preliminary`, `Limited`, or `Blocked`)
- IC Action Status
- Evidence Status
- Method Confidence with reason
- Key Findings
- Domain Findings
- Limitations
- Missing IC Gates
- Boundary
- `## Structured handoff` using the controlled fields from `workflows/handoff_artifact_standard.md`
- large workflow / spawned-subagent workflow handoff must also include `## Handoff metadata` and use the exact `## Structured handoff` block and field names from `workflows/handoff_artifact_standard.md`; do not rename or omit required fields

Boundary wording: `Boundary: Not an IC Action. Method output only.`

## Cross-skill guardrails

- Direct skill calls are allowed only as scoped method outputs with boundary and missing IC gates; large-workflow handoffs must use the controlled handoff fields.
- Non-IC outputs must not issue final `IC Action`, use `Action Box`, or provide exact allocation instructions.
- Evidence status, freshness, source restrictions, user-file provenance, and material conflicts constrain conclusions.
- Freshness-sensitive requests split structural view from current-action view.
- User-only source scope must be marked `Limited by source scope` when material.
- Complex products, value traps, expensive growth, ambiguous instruments, rumors, and portfolio-fit requests must use their canonical gates when relevant.

## Skill-specific guardrails

- Do not present point target as truth or issue final IC action.

## Failure states

- Complete when: Required inputs, evidence, boundary conditions, and domain checks are sufficient for `Complete for scoped method`; this does not imply Complete IC Action.
- Preliminary when: The skill can provide an explicit Quick Take or direct scoped method output before all method inputs are complete; in large workflow, return a structured handoff with `Limited` or `Blocked` module status instead of downgrading the workflow.
- Limited when: inputs are partial/proxy.
- Blocked when: core price/financial/capital-structure inputs are missing.


## Large workflow behavior

Expected large-workflow artifact: `valuation_expectations.md`. The skill remains the method layer; the owning agent or workflow owns role, boundary, status, and handoff publication.

When this skill runs as part of a large workflow, it provides valuation context, implied expectations, scenario range, and return-bridge method handoff. It must not issue final IC Action or present a point target as truth. If price, share count, financial history, or forecast assumptions are incomplete, mark valuation support `Limited` or `Blocked`.

## Quality checks

- Output follows the canonical skill contract in `implementation/11-skill-contracts.md`.
- Output uses the required output core and structured handoff; for large workflow / spawned-subagent workflow, it also includes `## Handoff metadata` and the controlled handoff fields from `workflows/handoff_artifact_standard.md`.
- Material claims are evidence-aware and limitations are visible.
- Boundary prevents unauthorized final action, exact sizing, or hidden recommendation.
- Downstream agents or IC can consume the result without hidden assumptions because owner, evidence limits, missing gates, and downstream handoff are explicit.

## Reader-facing valuation constraint language

Use direct valuation inputs first. If they are absent, use proxy valuation: revenue growth, gross/operating margin, cash flow, balance sheet, dilution, EV/Sales, peer range, historical own multiples, guidance, or asset-class-equivalent valuation. If proxy anchors are strong enough, provide a working valuation view. If they are too weak, do not state cheap/expensive as a firm conclusion; say the investment conclusion on price is not justified now or that valuation is sensitive to key assumptions. Keep `Limited`, `Blocked`, source-tier, provider, paywall, and not-found wording out of `investment_report.md`; preserve it in audit.

## Institutional workflow update

Separate Valuation / Expectations Support from Asset Quality View and explain entry setup rather than quality alone.

Every included module must state how it changes or confirms the Thesis Spine and must preserve `Boundary: Not an IC Action` when it is a direct specialist output.
