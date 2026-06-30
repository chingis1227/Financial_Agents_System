---
name: market-sense-hypothesis-engine
description: Use for market-behavior hypotheses without replacing evidence or IC synthesis.
---

# Market Sense Hypothesis Engine Skill

Runtime status: Runtime-Ready. Canonical source of truth: `implementation/11-skill-contracts.md`.

## Purpose

Generate plausible hypotheses for market moves or narrative shifts without overclaiming.

This runtime skill executes the reusable method contract without overriding agent, workflow, evidence, or IC boundaries.

## When to use

- Market observation needs explanation but evidence is incomplete or multi-causal.

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

- Market observation or price move
- Evidence freshness notes
- Pattern/reference context where relevant

If inputs are missing, continue only when a safe Preliminary or Limited scoped method output is allowed; otherwise return Blocked with missing inputs.

## Step sequence

1. Define observation
2. Generate candidate hypotheses
3. Map evidence for/against each hypothesis
4. Assign confidence
5. Identify confirm/disconfirm signals
6. Produce implications and handoff

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

- Do not turn hypotheses into facts or recommendations.

## Full Cycle behavior

- In a Full Cycle, this skill produces a market-move hypothesis handoff only: observed move, plausible drivers, confidence, cross-asset checks, alternatives, and module status.
- It must not convert hypotheses into final causality claims or investment actions.
- If the move or observation cannot be defined, mark the module `Blocked`; if evidence is weak, mark it `Limited`.

## Failure states

- Complete when: Required inputs, evidence, boundary conditions, and domain checks are sufficient for `Complete for scoped method`; this does not imply Complete IC Action.
- Preliminary when: The skill can provide an explicit Quick Take or direct scoped method output before all method inputs are complete; in Full Cycle, return a structured handoff with `Limited` or `Blocked` module status instead of downgrading the workflow.
- Limited when: hypotheses are plausible but evidence is weak.
- Blocked when: observation cannot be defined.

## Quality checks

- Output follows the canonical skill contract in `implementation/11-skill-contracts.md`.
- Output uses the required output core and, for Full Cycle, the controlled handoff fields from `workflows/handoff_artifact_standard.md`.
- Material claims are evidence-aware and limitations are visible.
- Boundary prevents unauthorized final action, exact sizing, or hidden recommendation.
- Downstream agents or IC can consume the result without hidden assumptions because owner, evidence limits, missing gates, and downstream handoff are explicit.
