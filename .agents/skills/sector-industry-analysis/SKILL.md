---
name: sector-industry-analysis
description: Use for sector, industry, value-chain, and competitive-context analysis.
---

# Sector & Industry Analysis Method Skill

Runtime status: Runtime-Ready. Canonical source of truth: `implementation/11-skill-contracts.md`.

## Purpose

Analyze sector structure, economics, profit pools, drivers, investability, risks, and monitoring.

This runtime skill executes the reusable method contract without overriding agent, workflow, evidence, or IC boundaries.

## When to use

- Sector/industry/theme-as-sector analysis is requested or embedded in equity workflow.

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

- Sector/theme definition
- Evidence pack
- Relevant companies/subsectors
- User horizon/universe constraints

If inputs are missing, continue only when a safe Preliminary or Limited scoped method output is allowed; otherwise return Blocked with missing inputs.

## Step sequence

1. Classify scope
2. Build evidence plan
3. Analyze structure/TAM/growth quality
4. Map value chain/profit pools/subsectors
5. Assess competition/drivers/valuation/investability
6. Build anti-thesis and monitoring
7. Produce sector outputs

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

- Do not make individual security final action.

## Failure states

- Complete when: Required inputs, evidence, boundary conditions, and domain checks are sufficient for `Complete for scoped method`; this does not imply Complete IC Action.
- Preliminary when: The skill can provide an explicit Quick Take or direct scoped method output before all method inputs are complete; in Full Cycle, return a structured handoff with `Limited` or `Blocked` module status instead of downgrading the workflow.
- Limited when: boundaries/data are partial.
- Blocked when: scope/evidence is too weak.


## Full Cycle behavior

When this skill runs as part of a Full Cycle, it owns sector structure, profit pools, competitive context, and industry-level risk handoff. It provides context for the asset workflow and IC, not security-level final action. If sector context is not material, the module may be marked `Not material`; if material data is partial, mark it `Limited`.

## Quality checks

- Output follows the canonical skill contract in `implementation/11-skill-contracts.md`.
- Output uses the required output core and, for Full Cycle, the controlled handoff fields from `workflows/handoff_artifact_standard.md`.
- Material claims are evidence-aware and limitations are visible.
- Boundary prevents unauthorized final action, exact sizing, or hidden recommendation.
- Downstream agents or IC can consume the result without hidden assumptions because owner, evidence limits, missing gates, and downstream handoff are explicit.
