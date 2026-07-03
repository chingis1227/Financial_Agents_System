---
name: equity-company-analysis
description: Use for scoped public-company equity analysis after the investment workflow router selects an equity route. Covers business quality, moat, growth, financial context handoff, and thesis boundaries; does not issue final IC Action.
---

# Equity Company Analysis Method Skill

Runtime status: Runtime-Ready. Canonical source of truth: `implementation/11-skill-contracts.md`.

## Purpose

Analyze company business quality and thesis durability.

This runtime skill executes the reusable method contract without overriding agent, workflow, evidence, or IC boundaries.

## When to use

- An equity company-quality report is required or requested.

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

- Company/ticker identity
- Evidence pack
- Financial analysis where available
- Sector/news context where material

If inputs are missing, continue only when a safe Preliminary or Limited scoped method output is allowed; otherwise return Blocked with missing inputs.

## Step sequence

1. Define business and revenue model
2. Assess customer value and demand quality
3. Analyze revenue/margin durability
4. Assess competitive position and management quality
5. Read through financial evidence
6. Define thesis dependencies, breakpoints, and monitoring triggers

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

- Do not convert business quality into final stock action.

## Failure states

- Complete when: Required inputs, evidence, boundary conditions, and domain checks are sufficient for `Complete for scoped method`; this does not imply Complete IC Action.
- Preliminary when: The skill can provide an explicit Quick Take or direct scoped method output before all method inputs are complete; in large workflow, return a structured handoff with `Limited` or `Blocked` module status instead of downgrading the workflow.
- Limited when: company/financial evidence is partial.
- Blocked when: identity or core business evidence is missing.


## Large workflow behavior

Expected large-workflow artifact: `equity_company_analysis.md`. The skill remains the method layer; the owning agent or workflow owns role, boundary, status, and handoff publication.

When this skill runs as part of an equity large workflow, it provides the business-quality and thesis-durability method handoff for the Equity Agent and IC. It must separate business quality from stock attractiveness and must not issue final action language. If financial, sector, or news inputs are incomplete, mark the method output `Limited` and name the missing downstream gates.

## Quality checks

- Output follows the canonical skill contract in `implementation/11-skill-contracts.md`.
- Output uses the required output core and structured handoff; for large workflow / spawned-subagent workflow, it also includes `## Handoff metadata` and the controlled handoff fields from `workflows/handoff_artifact_standard.md`.
- Material claims are evidence-aware and limitations are visible.
- Boundary prevents unauthorized final action, exact sizing, or hidden recommendation.
- Downstream agents or IC can consume the result without hidden assumptions because owner, evidence limits, missing gates, and downstream handoff are explicit.

## Small-cap / foreign / illiquid memo behavior

Do not expect Nvidia-level disclosure from every equity. For small-cap, foreign, or illiquid names, shift the analysis toward disclosure quality, liquidity, balance sheet, cash burn, dilution risk, governance, survival risk, and scenario range. In `investment_report.md`, do not write that the system did not find data; explain that investment risk is higher because transparency is lower and valuation is sensitive to fewer key assumptions.
