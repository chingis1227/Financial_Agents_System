---
name: portfolio-fit
description: Use for scoped portfolio fit, role, overlap, sizing-context limits, diversification, risk tolerance, and scenario-based fit; does not issue final IC Action or exact allocation instructions.
---

# Portfolio Fit Method Skill

Runtime status: Runtime-Ready. Canonical source of truth: `implementation/11-skill-contracts.md`.

## Purpose

Assess generic role fit and user-specific portfolio fit.

This runtime skill executes the reusable method contract without overriding agent, workflow, evidence, or IC boundaries.

## When to use

- Portfolio role/suitability is requested or material.

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

- Asset/thesis
- User portfolio context where available
- Risk/valuation/asset reports where available, including source-backed risk/performance metrics when another owner has produced or verified them

If inputs are missing, continue only when a safe Preliminary or Limited scoped method output is allowed; otherwise return Blocked with missing inputs.

## Step sequence

1. Assess generic role
2. Assess user-specific fit if context exists
3. Check overlap/concentration/risk/liquidity/FX/tax caveats
4. Assess monitoring burden
5. Produce IC handoff

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

- Do not give exact allocation or final buy/sell action.
- If user portfolio context is missing, do not frame Portfolio Fit as a failed module in the reader-facing report. Use General Portfolio Role Mode: audit may record `Portfolio Fit: Limited / not personalized`, while `investment_report.md` shows only a plain Portfolio role / `Портфельная роль` section.
- Evidence Collector owns sources, dates, quotes, benchmark selection, and historical prices. Risk / Market Positioning / Market Sense own calculation or verification of beta, trailing return, volatility, max drawdown, correlation, and relative performance versus benchmark / sector / peers. Portfolio Fit may use those metrics to interpret core vs satellite role, concentration risk, overlap, risk contribution, drawdown tolerance, suitability constraints, and monitoring burden, but it is not the primary data/evidence owner.

## Failure states

- Complete when: Required inputs, evidence, boundary conditions, and domain checks are sufficient for `Complete for scoped method`; this does not imply Complete IC Action.
- Preliminary when: The skill can provide an explicit Quick Take or direct scoped method output before all method inputs are complete; in large workflow, return a structured handoff with `Limited` or `Blocked` module status instead of downgrading the workflow.
- Limited when: user portfolio context is missing for personalized fit; in reader-facing reports this is General Portfolio Role Mode, not failure wording.
- Blocked when: user-specific answer is required but context is unavailable.


## Large workflow behavior

Expected large-workflow artifact: `portfolio_fit.md`. The skill remains the method layer; the owning agent or workflow owns role, boundary, status, and handoff publication.

When this skill runs as part of a large workflow, it provides generic role fit and user-specific portfolio-fit method output when context exists. Missing portfolio data must not stop asset analysis, but it makes Portfolio Fit `Limited / not personalized` and prevents personalized final IC Action. Exact allocation instructions remain prohibited.

The main `investment_report.md` must present missing portfolio context as a general Portfolio role explanation. Technical labels such as `Portfolio Fit: Limited / not personalized`, missing gates, handoff metadata, and module status belong in `audit`.

## Quality checks

- Output follows the canonical skill contract in `implementation/11-skill-contracts.md`.
- Output uses the required output core and structured handoff; for large workflow / spawned-subagent workflow, it also includes `## Handoff metadata` and the controlled handoff fields from `workflows/handoff_artifact_standard.md`.
- Material claims are evidence-aware and limitations are visible.
- Boundary prevents unauthorized final action, exact sizing, or hidden recommendation.
- Downstream agents or IC can consume the result without hidden assumptions because owner, evidence limits, missing gates, and downstream handoff are explicit.
