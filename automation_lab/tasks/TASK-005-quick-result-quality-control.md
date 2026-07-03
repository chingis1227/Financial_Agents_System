# TASK-005 — QUICK Result Quality Control

Status: Complete
Date: 2026-07-01

## Goal

Add a stronger quality-control layer for Automation Lab `quick-run` outputs without changing the main Financial Agent System.

## Value

TASK-005 turns TASK-004 launch validation into a more explicit result-quality gate. It checks that QUICK remains a chat-only Preliminary/Limited intake step, handles freshness-dependent prompts conservatively, and records machine-readable quality checks in JSON run logs.

## Dependencies

- TASK-004 guarded QUICK automation is complete.
- Main Financial Agent System remains unchanged and authoritative.
- Quick Take route card requires exactly three questions as the first action.

## Scope

Implemented in Automation Lab only:

- stricter `validate_quick_output()` structure checks;
- status must be the first non-empty line;
- exactly one status line is allowed;
- questions must be numbered `1.`, `2.`, `3.`;
- freshness-dependent prompts are detected from the prompt text;
- freshness-dependent QUICK outputs must use `Status: Limited`;
- freshness-dependent QUICK outputs must ask an explicit freshness/current-source question;
- extra forbidden markers block subagent claims and analysis/recommendation sections;
- JSON logs include `quality_checks` with individual pass/fail dimensions;
- historical fixture QUICK output uses `Status: Limited` when the prompt is freshness-dependent.

## Out of scope

- No evidence fetching.
- No source ranking.
- No semantic scoring of answer quality beyond deterministic guardrails.
- No full investment report.
- No audit folder.
- No final IC Action.
- No exact position sizing or trade instruction.
- No changes to the main Financial Agent System repository.

## Implementation summary

TASK-005 keeps `quick-run` as a guarded first-step launcher. The new QC layer validates both output and prompt context. For ordinary prompts, accepted output must start with `Status: Preliminary` or `Status: Limited`, then provide exactly three numbered questions and avoid all final-action/report/audit markers. For freshness-dependent prompts such as `latest`, `today`, `news`, `earnings`, `price action`, or `current`, accepted output must be `Status: Limited` and one of the questions must explicitly cover freshness/current-source needs.

Live prompt instructions were tightened so live Codex runs are asked to use `Status: Limited` when current timestamped sources have not been gathered yet.

## Outputs

Each successful QUICK run log now includes:

- `validation.status`;
- `validation.question_count`;
- `validation.quality_checks`, including freshness, structure, no-report, no-audit, no-IC, no-final-action, no-sizing, no-subagent, and no-analysis-section checks.

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

Run historical fixture freshness QUICK launch:

```powershell
.\.venv\Scripts\python.exe fa_automation.py quick-run --prompt "latest Microsoft news" --mode live
```

## Docs synchronization note

TASK-005 changes only the Automation Lab. The main Financial Agent System validators are not required because no main project files are modified.

If a future task changes the main project, run its required validators:

```powershell
py -3 tools\validate_project_consistency.py
py -3 tools\validate_behavior_contracts.py
py -3 tools\validate_runtime_readiness.py
```

## Review checklist

- [x] QUICK output status is validated.
- [x] QUICK structure is validated.
- [x] Freshness-dependent prompts are Limited unless current sources are explicitly gathered later by a different workflow.
- [x] Freshness/current-source needs are visible in the three-question intake.
- [x] Final IC Action remains forbidden.
- [x] Final buy/sell/hold/add/trim/exit language remains forbidden.
- [x] Reports and audit folders remain forbidden.
- [x] Quality checks are recorded in run logs.
- [x] Main Financial Agent System is not modified.

## Definition of Done

TASK-005 is complete when:

- deterministic QUICK QC checks are implemented;
- unit tests cover structure, freshness, and forbidden marker failures;
- historical fixture QUICK logs include quality checks;
- existing route-check behavior still passes;
- README and ROADMAP reflect TASK-005;
- Git status contains only intended Automation Lab changes before commit.
