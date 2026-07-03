# TASK-004 — QUICK Automation

Status: Complete
Date: 2026-07-01

## Goal

Add an Automation Lab command that launches the Financial Agent System `QUICK:` workflow in a guarded way.

## Value

TASK-004 creates the first practical automation entrypoint for Quick Take without turning QUICK into a full investment workflow. It gives future TASK-005 quality-control work a concrete command and run-log shape to validate.

## Dependencies

- TASK-001 route-check scaffold is complete.
- TASK-002 live Codex SDK route-check is complete.
- TASK-003 data-source map draft is complete.
- Main Financial Agent System remains unchanged and authoritative.

## Scope

Implemented in Automation Lab only:

- `fa_automation.py quick-run --prompt ... --mode mock`
- `fa_automation.py quick-run --prompt ... --mode live`
- `QUICK:` prefix normalization when the prefix is omitted.
- JSON run logs under `runs/quick/`.
- Mock QUICK first-step output for deterministic tests.
- Live Codex SDK launch from the Financial Agent System root in read-only / deny-all mode.
- Lightweight QUICK output validation for status, exactly three questions, and forbidden final-action markers.
- Documentation and unittest coverage.

## Out of scope

- No full investment report generation.
- No `audit/` folder generation.
- No final IC Action.
- No Action Box.
- No final buy/sell/hold/add/trim/exit conclusion.
- No exact position sizing or exact trade instruction.
- No source fetching, freshness validation, or result quality scoring; those belong to TASK-005 or later.
- No changes to the main Financial Agent System repository.

## Implementation summary

`quick-run` launches only the Quick Take first action. The live prompt tells Codex to read `PROJECT_STATE.md`, `AGENTS.md`, and `workflows/route_cards/quick_take.md`, then ask exactly three relevant questions and stop. The launcher forbids full AGENT workflow behavior, subagent claims, file creation, saved reports, audit folders, final IC Action, Action Box, exact sizing, and final action conclusions.

Mock mode returns a deterministic Preliminary response with exactly three questions. Live mode uses the same Codex SDK pattern as route-check: Financial Agent System root, read-only sandbox, deny-all approval mode, optional model from `FA_AUTOMATION_CODEX_MODEL`, and timeout from `FA_AUTOMATION_LIVE_TIMEOUT_SECONDS`. The output is accepted only if it declares `Status: Preliminary` or `Status: Limited`, contains exactly three question lines, and avoids forbidden final-action/report/audit/sizing markers, including bare or labeled action conclusions such as `Buy`, `Conclusion: Hold`, `Action: trim`, or `Action: exit`.

## Outputs

Each QUICK run log includes:

- timestamp;
- mode;
- workflow = `quick_take`;
- project root;
- original prompt;
- normalized prompt;
- boundary status;
- no-report / no-audit / no-IC markers;
- validation status and question count;
- output.

## Test plan

Run Automation Lab tests:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests
```

Run mock route check to confirm existing behavior remains intact:

```powershell
.\.venv\Scripts\python.exe fa_automation.py route-check --mode mock
```

Run mock QUICK launch:

```powershell
.\.venv\Scripts\python.exe fa_automation.py quick-run --prompt "Microsoft for 3 years" --mode mock
```

Manual review:

- Confirm the main Financial Agent System repository is unchanged.
- Confirm `.venv/` is not staged.
- Confirm generated validation run logs are not committed unless intentionally selected.

## Docs synchronization note

TASK-004 changes only the Automation Lab. The main Financial Agent System validators are not required because no main project files are modified.

If a future task changes the main project, run its required validators:

```powershell
py -3 tools\validate_project_consistency.py
py -3 tools\validate_behavior_contracts.py
py -3 tools\validate_runtime_readiness.py
```

## Review checklist

- [x] QUICK automation is implemented in Automation Lab only.
- [x] Mock and live modes exist.
- [x] `QUICK:` prefix is normalized.
- [x] Live mode launches from the Financial Agent System root.
- [x] Live mode uses read-only sandbox and deny-all approval mode.
- [x] QUICK first action asks exactly three questions in mock mode.
- [x] The live prompt requires exactly three questions and stop.
- [x] Lightweight validation rejects live output that misses status, has the wrong question count, or contains forbidden final-action markers.
- [x] No report, audit, or IC Action is requested by the command.
- [x] No main Financial Agent System files are modified.

## Definition of Done

TASK-004 is complete when:

- `quick-run` exists in the CLI.
- Mock QUICK launch creates a JSON run log.
- Mock QUICK launch preserves Preliminary boundary.
- Live QUICK launch is wired through the Codex SDK in read-only / deny-all mode.
- Tests pass.
- Mock route-check still passes.
- README and ROADMAP reflect TASK-004.
- Git status contains only intended Automation Lab changes before commit.
