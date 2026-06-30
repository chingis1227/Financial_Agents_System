---
name: risk-red-team
description: Use to challenge a thesis, identify downside risks, and test failure modes.
---

# Risk / Red Team Method Skill

Runtime status: Runtime-Ready. Canonical source of truth: `implementation/11-skill-contracts.md`.

## Purpose

Challenge the thesis and identify material failure paths.

This runtime skill executes the reusable method contract without overriding agent, workflow, evidence, or IC boundaries.

## When to use

- A thesis, final action, or risk challenge is requested.

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

- Core thesis
- Evidence pack
- Lead analysis
- Valuation context for Complete Review
- Relevant specialists

If inputs are missing, continue only when a safe Preliminary or Limited scoped method output is allowed; otherwise return Blocked with missing inputs.

## Step sequence

1. Check input completeness
2. Extract thesis and assumptions
3. Apply materiality/anti-overbreaking discipline
4. Identify failure paths and bear case
5. Run mandatory risk gates
6. Include counter-evidence and challenge requests
7. Issue risk challenge verdict

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
- Full Cycle / Full Agent Workflow handoff must also include `## Handoff metadata` and use the exact `## Structured handoff` block and field names from `workflows/handoff_artifact_standard.md`; do not rename or omit required fields

Boundary wording: `Boundary: Not an IC Action. Method output only.`

## Cross-skill guardrails

- Direct skill calls are allowed only as scoped method outputs with boundary and missing IC gates; Full Cycle handoffs must use the controlled handoff fields.
- Non-IC outputs must not issue final `IC Action`, use `Action Box`, or provide exact allocation instructions.
- Evidence status, freshness, source restrictions, user-file provenance, and material conflicts constrain conclusions.
- Freshness-sensitive requests split structural view from current-action view.
- User-only source scope must be marked `Limited by source scope` when material.
- Complex products, value traps, expensive growth, ambiguous instruments, rumors, and portfolio-fit requests must use their canonical gates when relevant.

## Skill-specific guardrails

- Do not create generic risk lists or hidden recommendations.

## Failure states

- Complete when: Required inputs, evidence, boundary conditions, and domain checks are sufficient for `Complete for scoped method`; this does not imply Complete IC Action.
- Preliminary when: The skill can provide an explicit Quick Take or direct scoped method output before all method inputs are complete; in Full Cycle, return a structured handoff with `Limited` or `Blocked` module status instead of downgrading the workflow.
- Limited when: thesis/evidence exists but valuation/risk detail is incomplete.
- Blocked when: core thesis is undefined.


## Full Cycle behavior

Expected Full Cycle artifact: `risk_red_team.md`. The skill remains the method layer; the owning agent or workflow owns role, boundary, status, and handoff publication.

When this skill runs as part of a Full Cycle, it provides thesis challenge, failure paths, bear-case pressure tests, and risk-gate method handoff. It may fail the risk gate but must not issue buy/sell/hold action. If thesis, valuation, or evidence inputs are incomplete, mark the risk review `Limited` or `Blocked` and state what IC cannot conclude.

## Quality checks

- Output follows the canonical skill contract in `implementation/11-skill-contracts.md`.
- Output uses the required output core and structured handoff; for Full Cycle / Full Agent Workflow, it also includes `## Handoff metadata` and the controlled handoff fields from `workflows/handoff_artifact_standard.md`.
- Material claims are evidence-aware and limitations are visible.
- Boundary prevents unauthorized final action, exact sizing, or hidden recommendation.
- Downstream agents or IC can consume the result without hidden assumptions because owner, evidence limits, missing gates, and downstream handoff are explicit.
