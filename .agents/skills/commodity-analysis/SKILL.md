---
name: commodity-analysis
description: Use for scoped commodity or commodity-linked exposure analysis after the investment workflow router selects a commodity route. Covers supply/demand, macro sensitivity, curve/positioning context, and specialist handoff; does not issue final IC Action.
---

# Commodity Analysis Method Skill

Runtime status: Runtime-Ready. Canonical source of truth: `implementation/11-skill-contracts.md`.

## Purpose

Analyze commodity setup through balance, curve, macro, policy, logistics, and instrument context.

This runtime skill executes the reusable method contract without overriding agent, workflow, evidence, or IC boundaries.

## When to use

- Commodity setup, regime, or instrument analysis is requested.

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
- `workflows/handoff_artifact_standard.md` when producing Full Cycle or Full Agent Workflow handoffs

Conditional references:

- `implementation/03-contract-templates.md` when editing or validating contracts
- `implementation/09-system-acceptance-qa.md` when running QA or acceptance checks
- `implementation/10-traceability-matrix.md` when using legacy detail
- `implementation/13-codex-runtime-architecture.md` when runtime packaging rules matter

## Required inputs

- Commodity/instrument identity
- Demand/supply/inventory evidence
- Curve/market data
- Macro/policy/logistics context

If inputs are missing, continue only when a safe Preliminary or Limited scoped method output is allowed; otherwise return Blocked with missing inputs.

## Step sequence

1. Classify commodity family and mode
2. Build demand map
3. Build supply map
4. Analyze inventories/reserves/flows
5. Analyze cost curve and curve/roll/carry
6. Analyze macro/geopolitics/logistics/substitution
7. Assess instrument context
8. Produce verdict, actionability label, triggers

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
- Structured Handoff using the controlled fields from `workflows/handoff_artifact_standard.md` when part of Full Cycle / Full Agent Workflow
- Full Cycle handoff must include owner, output status, evidence status, evidence limits, missing gates, decision boundary, downstream handoff, and required follow-up

Boundary wording: `Boundary: Method output only; not an IC Action.`

## Cross-skill guardrails

- Direct skill calls are allowed only as scoped method outputs with boundary and missing IC gates; Full Cycle handoffs must use the controlled handoff fields.
- Non-IC outputs must not issue final `IC Action`, use `Action Box`, or provide exact allocation instructions.
- Evidence status, freshness, source restrictions, user-file provenance, and material conflicts constrain conclusions.
- Freshness-sensitive requests split structural view from current-action view.
- User-only source scope must be marked `Limited by source scope` when material.
- Complex products, value traps, expensive growth, ambiguous instruments, rumors, and portfolio-fit requests must use their canonical gates when relevant.

## Skill-specific guardrails

- Do not issue precise price target or final buy/sell/hold.

## Failure states

- Complete when: Required inputs, evidence, boundary conditions, and domain checks are sufficient for `Complete for scoped method`; this does not imply Complete IC Action.
- Preliminary when: The skill can provide an explicit Quick Take or direct scoped method output before all method inputs are complete; in Full Cycle, return a structured handoff with `Limited` or `Blocked` module status instead of downgrading the workflow.
- Limited when: physical data is delayed/proxy-heavy.
- Blocked when: identity or decision-critical balance data is unavailable.


## Full Cycle behavior

When this skill runs as part of a commodity Full Cycle, it owns physical balance, curve/carry, inventories, macro sensitivity, policy/geopolitics, cost curve, and instrument-context handoff. It must not convert commodity setup quality into final IC Action. If current balance, curve, or vehicle data is missing, mark the module `Limited` or `Blocked`.

## Quality checks

- Output follows the canonical skill contract in `implementation/11-skill-contracts.md`.
- Output uses the required output core and, for Full Cycle, the controlled handoff fields from `workflows/handoff_artifact_standard.md`.
- Material claims are evidence-aware and limitations are visible.
- Boundary prevents unauthorized final action, exact sizing, or hidden recommendation.
- Downstream agents or IC can consume the result without hidden assumptions because owner, evidence limits, missing gates, and downstream handoff are explicit.
