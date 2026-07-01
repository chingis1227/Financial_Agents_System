---
name: investment-committee-synthesis
description: Use only for Investment Committee synthesis after evidence and required module handoffs are available. Owns IC-level report synthesis and gate-aware action status under canonical report schemas.
---

# Investment Committee Synthesis Method Skill

Runtime status: Runtime-Ready. Canonical source of truth: `implementation/11-skill-contracts.md`.

## Purpose

Integrate evidence and specialist handoffs into gate-aware IC synthesis inside the Investment Committee Agent: final memo only when gates pass, otherwise Decision-Prep Memo, Limited IC Draft, or Evidence Gap Memo.

This runtime skill executes the reusable method contract inside the Investment Committee Agent. It may support assembly of `Action Box`, `Investment View`, or `IC Action` content only after evidence lock and required gates pass; the Investment Committee Agent owns any permitted issuance.

## When to use

- IC stage is reached after evidence lock and required specialist handoffs are available.
- Final decision-support output is requested and the Investment Committee Agent is applying gate-aware artifact selection.
- If evidence lock or required specialist handoffs are missing, use this skill only to support a Limited or Blocked gate-aware IC artifact.

Use only after reading `AGENTS.md` and the canonical documents needed for the task.

## What you get

A scoped method output for Investment Committee Agent issuance with method findings, evidence status, Method Confidence, limitations, missing IC gates, gate-aware artifact selection, consumed handoff list, and structured handoff. Expected artifacts are `final_investment_memo.md`, `decision_prep_memo.md`, `limited_ic_draft.md`, or `evidence_gap_memo.md` depending on gate state.

## What it will not do

It must not bypass evidence readiness, source limitations, workflow routing, or IC gates. If gates are missing, support a gate-aware non-final artifact rather than a final IC action; the Investment Committee Agent owns issuance. Legacy PRDs are source material only through the registry and traceability matrix.

## Required canonical documents

Read only the canonical documents needed for the task. Default required set:

- `implementation/00-master-rules.md`
- `implementation/01-documentation-control.md`
- `implementation/04-evidence-layer.md`
- `implementation/06-agent-contracts.md` for owning agent boundaries
- `implementation/07-investment-committee-and-report-schemas.md` for final and non-final IC report schemas
- `implementation/11-skill-contracts.md` for this skill contract
- `workflows/handoff_artifact_standard.md` when producing large workflow or spawned-subagent workflow handoffs

Conditional references:

- `implementation/03-contract-templates.md` when editing or validating contracts
- `implementation/09-system-acceptance-qa.md` when running QA or acceptance checks
- `implementation/10-traceability-matrix.md` when using legacy detail
- `implementation/13-codex-runtime-architecture.md` when runtime packaging rules matter

## Required inputs

- Intake context
- Evidence pack, pre-IC lock, and consumed-source/evidence-limit summary
- Lead analysis
- Valuation and Risk when decision-relevant
- Material specialist handoff artifacts or artifact-equivalent summaries using `workflows/handoff_artifact_standard.md`

If inputs are missing, continue only when a safe Preliminary or Limited scoped method output is allowed; otherwise return Blocked with missing inputs.

## Step sequence

1. Check required inputs and evidence lock
2. Identify core debate and assumptions
3. Integrate business, valuation, risk, catalyst, macro, positioning, and portfolio context
4. Apply positive-action gate
5. If final gates pass, support the Investment Committee Agent in assembling the gated IC artifact with Action Box, Investment View, IC Action, confidence, monitoring, and follow-up requests; otherwise support Decision-Prep Box / Evidence Gap / Limited IC framing with the gate-aware non-final artifact. The Investment Committee Agent owns issuance.

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

Boundary wording: `Boundary: IC synthesis method inside the Investment Committee Agent only. IC Action and Action Box are allowed only after evidence lock and required IC gates pass; the Investment Committee Agent owns issuance. If gates are missing, use Decision-Prep Box or another gate-aware non-final artifact.`

Direct `IC:` shortcut boundary wording: `Boundary: Not an IC Action. Committee-prep handoff only.`

## Cross-skill guardrails

- Direct skill calls are allowed only as scoped method outputs with boundary and missing IC gates; large-workflow handoffs must use the controlled handoff fields.
- Non-IC outputs must not issue final `IC Action`, use `Action Box`, or provide exact allocation instructions.
- Evidence status, freshness, source restrictions, user-file provenance, and material conflicts constrain conclusions.
- Freshness-sensitive requests split structural view from current-action view.
- User-only source scope must be marked `Limited by source scope` when material.
- Complex products, value traps, expensive growth, ambiguous instruments, rumors, and portfolio-fit requests must use their canonical gates when relevant.

## Skill-specific guardrails

- Do not invent facts, expose internal transcript, or provide exact position sizing.

## Failure states

- Complete when: Required inputs, evidence, boundary conditions, and domain checks are sufficient for `Complete for scoped method`; this does not imply Complete IC Action.
- Preliminary when: The skill can provide an explicit Quick Take or direct scoped method output before all method inputs are complete; in large workflow, return a structured handoff with `Limited` or `Blocked` module status instead of downgrading the workflow.
- Limited when: useful but constrained.
- Blocked when: required evidence/valuation/risk/lead analysis is missing.


## Large workflow behavior

When this skill runs as part of a large workflow, it integrates evidence and specialist handoffs into the allowed IC artifact. It requires evidence and specialist handoffs; if required handoffs are missing, unstructured, stale, or boundary-unsafe, mark IC synthesis `Limited` or `Blocked` and select a gate-aware non-final artifact. It may support `final_investment_memo.md` only when required gates pass; otherwise it must use `decision_prep_memo.md`, `limited_ic_draft.md`, or `evidence_gap_memo.md`. It must preserve the Runtime Execution Plan and must not bypass missing evidence, valuation, risk, or portfolio gates.

## Quality checks

- Output follows the canonical skill contract in `implementation/11-skill-contracts.md`.
- Output uses the required output core and structured handoff; for large workflow / spawned-subagent workflow, it also includes `## Handoff metadata` and the controlled handoff fields from `workflows/handoff_artifact_standard.md`.
- Material claims are evidence-aware and limitations are visible.
- IC output lists consumed handoffs and rejects missing, unstructured, stale, or boundary-unsafe inputs instead of silently filling gaps.
- Boundary prevents unauthorized final action, exact sizing, or hidden recommendation.
- Downstream agents or IC can consume the result without hidden assumptions because owner, evidence limits, missing gates, and downstream handoff are explicit.
