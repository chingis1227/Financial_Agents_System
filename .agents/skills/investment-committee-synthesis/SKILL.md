---
name: investment-committee-synthesis
description: Use for IC synthesis after evidence and specialist gates are ready.
---

# Investment Committee Synthesis Method Skill

Runtime status: Runtime-Ready. Canonical source of truth: `implementation/11-skill-contracts.md`.

## Purpose

Integrate evidence and specialist reports into final decision-support memo.

This runtime skill executes the reusable method contract inside the Investment Committee Agent. It is the only runtime skill that may support `Action Box`, `Investment View`, or `IC Action`, and only after evidence lock and required gates pass.

## When to use

- Final decision-support output is requested.

Use only after reading `AGENTS.md` and the canonical documents needed for the task.

## What you get

A scoped method output with method findings, evidence status, Method Confidence, limitations, missing IC gates, and structured handoff.

## What it will not do

It must not bypass evidence readiness, source limitations, workflow routing, or IC gates. If gates are missing, produce a gate-aware non-final artifact rather than a final IC action. Legacy PRDs are source material only through the registry and traceability matrix.

## Required canonical documents

Read only the canonical documents needed for the task. Default required set:

- `implementation/00-master-rules.md`
- `implementation/01-documentation-control.md`
- `implementation/04-evidence-layer.md`
- `implementation/06-agent-contracts.md` for owning agent boundaries
- `implementation/11-skill-contracts.md` for this skill contract

Conditional references:

- `implementation/03-contract-templates.md` when editing or validating contracts
- `implementation/09-system-acceptance-qa.md` when running QA or acceptance checks
- `implementation/10-traceability-matrix.md` when using legacy detail
- `implementation/13-codex-runtime-architecture.md` when runtime packaging rules matter

## Required inputs

- Intake context
- Evidence pack and pre-IC lock
- Lead analysis
- Valuation and Risk when decision-relevant
- Material specialist reports

If inputs are missing, continue only when a safe Preliminary or Limited scoped method output is allowed; otherwise return Blocked with missing inputs.

## Step sequence

1. Check required inputs and evidence lock
2. Identify core debate and assumptions
3. Integrate business, valuation, risk, catalyst, macro, positioning, and portfolio context
4. Apply positive-action gate
5. Produce Action Box, Investment View, IC Action, confidence, monitoring, and follow-up requests

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
- Structured Handoff

Boundary wording: `Boundary: IC synthesis method only; IC Action is allowed only after evidence lock and required IC gates pass.`

## Cross-skill guardrails

- Direct skill calls are allowed only as scoped method outputs with boundary and missing IC gates.
- Non-IC outputs must not issue final `IC Action`, use `Action Box`, or provide exact allocation instructions.
- Evidence status, freshness, source restrictions, user-file provenance, and material conflicts constrain conclusions.
- Freshness-sensitive requests split structural view from current-action view.
- User-only source scope must be marked `Limited by source scope` when material.
- Complex products, value traps, expensive growth, ambiguous instruments, rumors, and portfolio-fit requests must use their canonical gates when relevant.

## Skill-specific guardrails

- Do not invent facts, expose internal transcript, or provide exact position sizing.

## Failure states

- Complete when: Required inputs, evidence, boundary conditions, and domain checks are sufficient for `Complete for scoped method`; this does not imply Complete IC Action.
- Preliminary when: The skill can provide an early, narrow, or Quick Take-style method view before all method inputs or workflow gates are complete.
- Limited when: useful but constrained.
- Blocked when: required evidence/valuation/risk/lead analysis is missing.

## Quality checks

- Output follows the canonical skill contract in `implementation/11-skill-contracts.md`.
- Output uses the required output core and structured handoff.
- Material claims are evidence-aware and limitations are visible.
- Boundary prevents unauthorized final action, exact sizing, or hidden recommendation.
- Downstream agents or IC can consume the result without hidden assumptions.
