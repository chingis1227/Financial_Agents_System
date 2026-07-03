# TASK-002 — Live Codex SDK Route Check

## Status

Complete.

## Goal

Replace the TASK-001 live placeholder with real Codex SDK route classification for the Financial Agent System route cards.

## Value

This task proves that the Automation Lab can ask Codex, from the main Financial Agent System root, to classify one investment request into the expected runtime route without performing investment analysis or changing the main project.

## Dependencies

- TASK-001 is complete.
- Main project exists at `C:\Users\ShumeikoYe\OneDrive\Documents\Financial Agent System`.
- Automation Lab virtual environment exists.
- Live mode dependency is installed/documented in `requirements-live.txt`:

```text
openai-codex==0.1.0b3
```

## Scope

- Use the Codex Python SDK for `route-check --mode live`.
- Run one Codex classification per route case.
- Use the main project root as Codex working directory.
- Use read-only sandbox and deny-all approval mode.
- Ask Codex to classify only the route.
- Require strict JSON with `selected_route` and `reason`.
- Retry once when JSON is invalid.
- Compare `selected_route` to the expected route.
- Save JSON run logs in the existing route-check format, extended with live metadata as needed.
- Keep historical fixture path behavior intact.
- Add unit coverage for strict JSON parsing and live result handling without invoking the real SDK.

## Out of Scope

- No investment analysis.
- No report generation.
- No final IC Action.
- No changes to Financial Agent System.
- No route-card edits.
- No agent/skill edits.
- No data source map.
- No QUICK automation.
- No raw full Codex response storage.

## Inputs

- `config/route_check_cases.json`
- `PROJECT_STATE.md`, `AGENTS.md`, and `workflows/route_cards/investment_request_router.md` from the main Financial Agent System project.

## Outputs

- Console pass/fail summary.
- JSON run log under `runs/route-check/`.
- For live cases, each result may include:
  - `reason`;
  - `attempts`;
  - `mismatch`;
  - `error`;
  - `diagnostic_hint`.

## Implementation Plan

1. Install/document the live dependency separately from TASK-001 scaffold dependencies.
2. Add live Codex classifier with lazy SDK import.
3. Start Codex from the Financial Agent System root.
4. Run with read-only sandbox and deny-all approvals.
5. Build a per-case prompt that asks only for route classification.
6. Parse strict JSON only; reject Markdown/code-fenced output.
7. Retry once on invalid JSON.
8. Mark invalid JSON, SDK errors, or route mismatches as failed cases.
9. Preserve existing JSON log shape and add live fields only where useful.
10. Add unit tests for strict JSON and live evaluation logic without live network/runtime dependency.

## Test Plan

Run:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests
.\.venv\Scripts\python.exe fa_automation.py route-check --mode live
.\.venv\Scripts\python.exe fa_automation.py route-check --mode live
```

Expected:

- Unit tests pass.
- Historical fixture path still passes six cases.
- Live mode writes a JSON log.
- Live mode runs one Codex classification per case.
- Passing live mode requires all selected routes to match expected routes.
- If SDK/auth/runtime fails, live mode exits non-zero and records case-level failures without changing the main project.

## Docs Synchronization

TASK-002 modifies only the external Automation Lab. Main Financial Agent System validators are not required unless the main project is changed.

If the main project is changed in a future task, run:

```powershell
py -3 tools\validate_project_consistency.py
py -3 tools\validate_behavior_contracts.py
py -3 tools\validate_runtime_readiness.py
```

## Review Checklist

- [x] `route-check --mode live` still passes.
- [x] Unit tests pass.
- [x] `route-check --mode live` runs real Codex SDK classification.
- [x] Live mode uses main project root.
- [x] Live mode uses read-only sandbox.
- [x] Live mode does not create investment reports.
- [x] Live mode does not modify Financial Agent System.
- [x] Live mode records mismatches with diagnostic hints.
- [x] Full raw Codex responses are not stored.
- [x] Review sub-agent feedback considered before commit.

## Definition of Done

- Live placeholder is removed.
- `openai-codex` live dependency is documented.
- Live route check uses real Codex SDK.
- One case is classified per SDK call.
- Strict JSON parser and retry behavior exist.
- JSON logs are written for live mode.
- Historical fixture path remains green.
- Tests pass.
- Main Financial Agent System remains unchanged.
- Review feedback is addressed or consciously declined.
- TASK-002 commit is created only after green checks.

## Risks / Notes

- Live mode depends on Codex SDK availability and local authentication/configuration.
- The SDK is beta and may change; dependency is isolated in `requirements-live.txt`.
- Live run logs intentionally omit raw full Codex responses.



## Review Feedback Addressed

Review sub-agent score before fixes: 8/10.

Accepted and fixed before commit:

- strict JSON now rejects extra fields;
- live timeout no longer skips remaining cases by default;
- empty SDK final responses flow through invalid-JSON retry behavior;
- tests now cover extra JSON fields, retry success, retry failure, and SDK cwd/sandbox/approval parameters.
