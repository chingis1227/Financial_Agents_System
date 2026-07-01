# Documentation Sync Contract

Status: Canonical documentation-sync contract

## Purpose

This document defines the synchronization rules that keep the Financial Agent System from drifting when runtime files, canonical documents, skills, agents, workflow runbooks, route cards, validators, or operational reports change.

It implements the project's TDD-like documentation behavior: rules must map to fixtures, fixtures must map to validators, and validators must pass before work is considered complete.

## OpenAI / Codex practice basis

This contract follows official OpenAI / Codex best practices: keep `AGENTS.md` practical, make repeated workflows into skills, use validation and done criteria, keep custom agents narrow, and treat subagents as real only when actually spawned. Future API-backed orchestration may use OpenAI Agents SDK manager/handoff/tool patterns, guardrails, and traces.

## Required sync behavior

| Change type | Required synchronized updates |
|---|---|
| New or changed current runtime behavior | Update `PROJECT_STATE.md`, affected route card, behavior fixtures, and validators. |
| New or changed canonical rule | Update the canonical document, registry if status changes, route cards if runtime-facing, and behavior fixtures if behavior changes. |
| New workflow runbook or route card | Register it in `implementation/01-documentation-control.md`, update `PROJECT_STATE.md`, and update runtime readiness validation. |
| New skill or material skill trigger change | Update the skill description, related route card, and skill validation checks. |
| New custom agent or material agent behavior change | Update canonical agent contract, runtime agent file, handoff expectations, and validation checks. |
| New operational report | Register it as supporting, historical, superseded, or current evidence; do not let it silently override `PROJECT_STATE.md`. |
| Archived or moved document | Update registry, `PROJECT_STATE.md`, and validators so archived files are not used as daily runtime sources. |

## Current-state rule

`PROJECT_STATE.md` is the current-state summary. Historical reports, archived PRDs, task logs, and old readiness reports do not override it. If an older report conflicts with current canonical rules or `PROJECT_STATE.md`, mark the older report as supporting historical or superseded.

## Fixture rule

Any new behavior rule that affects routing, question count, output boundary, freshness, subagent spawning, report packaging, or IC gates must have a fixture under `tests/behavior/` before the work is complete.

## Validation rule

After documentation, workflow, skill, agent, route-card, fixture, or validator changes, run:

```powershell
py -3 tools\validate_project_consistency.py
py -3 tools\validate_behavior_contracts.py
py -3 tools\validate_runtime_readiness.py
```

If validation fails, either fix the project state or report a source issue. Do not mark the task complete while validation fails.

## Historical build-document rule

`archive/project-history/TASKS.md` and `archive/project-history/IMPLEMENTATION_BACKLOG.md` are historical build records. They may be read for provenance, but they are not daily runtime instructions and must not appear in active runtime reading order.

## Acceptance checks

This contract is satisfied when:

- `PROJECT_STATE.md` exists and reflects current operational state.
- Active runtime route cards exist and are registered.
- Behavior fixtures cover the golden prompts.
- Validators fail on stale registry, stale route, missing route card, missing workflow-router skill, or archived docs in active runtime order.
- `AGENTS.md` remains concise and points to the current-state and route-card layer.
