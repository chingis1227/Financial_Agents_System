# TASK-006 — AGENT Automation Design

Status: Complete
Date: 2026-07-01

## Goal

Design the large `AGENT:` automation path before implementing full workflow execution.

## Value

TASK-006 creates a deterministic, testable design layer for future AGENT automation while preserving the Financial Agent System as the source of truth. It prevents premature execution by validating intake, gates, artifact boundaries, and subagent truthfulness before any later task attempts evidence collection, specialist execution, report creation, audit folder creation, or final IC synthesis.

## Dependencies

- TASK-001 through TASK-005 are complete.
- Main Financial Agent System remains unchanged and authoritative.
- `AGENT:` route behavior is governed by the main project route cards and canonical implementation documents.

## Scope

Implemented in Automation Lab only:

- new `agent-design` CLI command;
- `AGENT:` prefix normalization;
- deterministic historical fixture route selection for the design plan;
- route-card mapping for AGENT full-cycle routes;
- route-specific five-question intake planning;
- planned subagent list by selected route;
- explicit empty `actual_subagents_run` list for design mode;
- required design meta-gate coverage for source-of-truth, five-question intake, subagent truthfulness, audit pack, and IC synthesis lock;
- required canonical IC-gate coverage for evidence/freshness, lead asset analysis, material context modules, valuation/expectations, risk/red-team, implementation/vehicle quality, and portfolio fit;
- artifact boundary for future reports under `C:\Users\ShumeikoYe\OneDrive\Documents\Financial Agent Reports`;
- future run-folder pattern `[ASSET] yyyy-mm-dd hhmm`;
- JSON run logs under `runs/agent-design/`;
- unit tests for CLI, validation, routing, gate coverage, and false subagent execution claims.

## Out of scope

- No evidence fetching.
- No valuation execution.
- No risk review execution.
- No portfolio-fit analysis.
- No subagent spawning by the `agent-design` command.
- No full investment report.
- No audit folder.
- No final IC Action.
- No changes to the main Financial Agent System repository.

## Implementation summary

`agent-design` creates a design-only plan for the large AGENT workflow. The command adds the `AGENT:` prefix when omitted, selects the expected full-cycle route in historical fixture path, generates exactly five route-specific intake questions, lists planned subagents, records that no subagents have executed, and validates the required workflow gates before writing a JSON run log.

The design deliberately separates planned subagents from actual subagents. `actual_subagents_run` must remain empty in design mode, and validation rejects text that claims subagents already executed.

The design gate model separates design meta-gates from canonical IC gates so future implementation cannot treat a meta-complete plan as enough for positive or final IC Action.

## Outputs

Each successful AGENT design log includes:

- `workflow: agent_automation_design`;
- selected route;
- normalized AGENT prompt;
- exactly five intake questions;
- planned subagents;
- empty `actual_subagents_run`;
- required gate coverage;
- validation quality checks;
- future report/audit boundary outside both repositories, including `[ASSET] yyyy-mm-dd hhmm\investment_report.md` plus `audit\`.

## Test plan

Run Automation Lab tests:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests
```

Run historical fixture route check:

```powershell
.\.venv\Scripts\python.exe fa_automation.py route-check --mode live
```

Run historical fixture QUICK launch:

```powershell
.\.venv\Scripts\python.exe fa_automation.py quick-run --prompt "Microsoft for 3 years" --mode live
```

Run historical fixture AGENT design:

```powershell
.\.venv\Scripts\python.exe fa_automation.py agent-design --prompt "Microsoft for 3 years" --mode live
```

## Docs synchronization note

TASK-006 changes only the Automation Lab. The main Financial Agent System validators are not required because no main project files are modified.

If a future task changes the main project, run its required validators:

```powershell
py -3 tools\validate_project_consistency.py
py -3 tools\validate_behavior_contracts.py
py -3 tools\validate_runtime_readiness.py
```

## Review checklist

- [x] AGENT design asks exactly five intake questions.
- [x] Design waits for the user after intake.
- [x] Main Financial Agent System remains the source of truth.
- [x] Planned subagents are separated from actual subagents.
- [x] Design mode cannot claim subagents executed.
- [x] Evidence/freshness gate is represented.
- [x] Lead asset/theme analysis gate is represented.
- [x] Material context modules gate is represented.
- [x] Valuation/expectations gate is represented.
- [x] Risk/red-team gate is represented.
- [x] Implementation/vehicle-quality gate is represented.
- [x] Portfolio-fit gate is represented.
- [x] Future report and audit boundaries are represented outside both repositories.
- [x] Positive or final IC Action remains locked until required gates pass; missing gates force Limited or Blocked output.
- [x] Main Financial Agent System is not modified.

## Definition of Done

TASK-006 is complete when:

- deterministic AGENT automation design is implemented;
- unit tests cover CLI output, five-question intake, gate validation, subagent truthfulness, and route-specific design;
- historical fixture route-check and QUICK behavior still pass;
- README and ROADMAP reflect TASK-006;
- Git status contains only intended Automation Lab changes before commit.
