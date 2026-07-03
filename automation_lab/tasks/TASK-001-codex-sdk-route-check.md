# TASK-001 — Codex SDK Route Check Scaffold

## Status

Complete for TASK-001 scope.

## Goal

Create the first working route-check scaffold for the Financial Agent Automation Lab.

## Value

This task proves the automation shell before connecting real Codex SDK execution. It verifies that prompts can be mapped to expected Financial Agent System routes and that results are logged in a repeatable format.

## Dependencies

- Python 3.13.0 or compatible Python 3.
- Main project exists at `C:\Users\ShumeikoYe\OneDrive\Documents\Financial Agent System`.
- Route cases are manually aligned with the main project's route cards and behavior fixtures.

## Scope

- Create Automation Lab structure.
- Initialize Git in Automation Lab.
- Create `.venv` without installing `openai-codex`.
- Add `fa_automation.py` CLI.
- Add mock route-check mode.
- Add live placeholder mode.
- Add route cases JSON.
- Add JSON run logs.
- Add unittest coverage for CLI + JSON log.
- Add README and ROADMAP.

## Out of Scope

- No real Codex SDK execution.
- No `openai-codex` installation.
- No `requirements.txt`.
- No `.gitignore`.
- No changes to Financial Agent System.
- No automatic sync with `tests/behavior/golden_prompts.yaml`.
- No investment analysis.
- No report generation.

## Inputs

- `config/route_check_cases.json`
- Main project root path.

## Outputs

- Console pass/fail summary.
- JSON run log under `runs/route-check/`.

## Implementation Plan

1. Create the Automation Lab folder and required subfolders.
2. Initialize Git.
3. Create `.venv`.
4. Add route cases JSON with six first cases.
5. Implement CLI route-check command.
6. Implement mock route resolver.
7. Implement live placeholder error path.
8. Write JSON run log.
9. Add unittest for CLI and JSON log.
10. Run checks and review Git status before commit.

## Test Plan

Run:

```powershell
.\.venv\Scripts\python.exe fa_automation.py route-check --mode mock
.\.venv\Scripts\python.exe -m unittest discover -s tests
```

Expected:

- mock CLI exits with code 0;
- JSON run log is created;
- log contains 6 cases;
- all cases pass;
- live mode exits with non-zero status and a clear placeholder error.

## Docs Synchronization

TASK-001 does not modify Financial Agent System. Main project validators are not required.

If any future task changes the main project, run:

```powershell
py -3 tools\validate_project_consistency.py
py -3 tools\validate_behavior_contracts.py
py -3 tools\validate_runtime_readiness.py
```

## Review Checklist

- [x] Mock route check passes.
- [x] JSON run log exists and has expected fields.
- [x] Unit tests pass.
- [x] Main project Git status remains clean.
- [x] `.venv` is not staged.
- [x] No accidental SDK dependency was added.
- [x] No root `.gitignore` or `requirements.txt` was created.

## Definition of Done

- Automation Lab exists.
- Git is initialized.
- `.venv` exists.
- README exists.
- ROADMAP exists.
- This task file exists.
- Route cases JSON exists.
- CLI exists.
- unittest exists.
- Mock route check works.
- Live mode returns a clear placeholder error.
- JSON run log is created.
- Tests pass.
- Financial Agent System remains unchanged.
- First commit can be made only after all checks pass.

## Risks / Notes

No `.gitignore` is used in TASK-001 by explicit decision. Before committing, check that `.venv/` is not staged.


