# TASK-007 - QUICK answer public data v1

Status: Complete

## Goal

Implement the first real `quick-answer` execution path for the QUICK workflow, using MSFT/equity as the pilot asset.

## Value

This task turns QUICK from an intake-only launch into a safe two-step workflow:

1. `quick-run` asks exactly three questions.
2. `quick-answer` accepts the original prompt plus the three answers, gathers a minimal public-data snapshot, validates a short Quick Take, and saves run evidence.

## Dependencies

- Financial Agent System remains the source of truth for QUICK boundaries.
- Existing `quick-run` behavior from TASK-004/TASK-005.
- Public data only; no API keys are required.
- Mock fixtures for stable tests.

## Scope

- Add `quick-answer`.
- Support `--mode mock` and `--mode live`.
- Use MSFT/equity as the first pilot.
- Save `source_snapshot.json`, `data_quality.json`, and `quick_answer.json` under `data_runs/quick/[timestamp]-MSFT/`.
- Save a run log under `runs/quick/`.
- Add `validate-quick-answer`.
- Add unit and CLI tests for happy path and guardrails.
- Update README and ROADMAP.

## Out of scope

- Full AGENT workflow.
- Investment reports.
- Audit folders.
- Final IC decision.
- Exact position sizing or trade instruction.
- Full valuation model.
- Paid or authenticated data providers.
- Non-MSFT asset expansion.

## Implementation plan

1. Add data-run and fixture directories.
2. Detect MSFT/Microsoft identity.
3. Build mock data collection from fixtures.
4. Build live/public best-effort collection from SEC submissions and public price source.
5. Assess status as `Preliminary`, `Limited`, or `Blocked`.
6. Generate the required Quick Take sections.
7. Validate files, status, forbidden language, required sections, and absence of report/audit artifacts.
8. Add CLI and tests.

## Test plan

- MSFT/Microsoft identity detection.
- Prompt normalization.
- Three answers required.
- Empty answers rejected.
- Mock snapshot schema.
- Data-quality schema.
- Quick-answer JSON schema.
- Missing price or recent events downgrades to `Limited`.
- Missing identity or unsupported asset becomes `Blocked`.
- Missing fixture becomes controlled `Blocked`.
- No `investment_report.md`.
- No `audit` folder.
- No final action language.
- No exact sizing.
- Required sections exist.
- CLI creates one data-run folder and one run log.
- Validator passes for the mock happy path.

Live/public smoke is intentionally best-effort and should not be a brittle unit test. If public sources are unavailable, the command should not crash; it should return `Limited` or `Blocked` with missing-data explanation.

## Docs synchronization note

README and ROADMAP were updated. The Financial Agent System project was not changed.

## Review checklist

- `quick-run` still asks exactly three questions.
- `quick-answer` accepts prompt plus exactly three answers.
- Mock MSFT scenario is stable.
- Live/public mode requires no API keys.
- Snapshot files are created.
- Run log is created.
- Validator passes.
- Output stays short and safe.
- No report/audit artifact is created.
- No final action language or exact sizing appears in the generated answer.
- `.venv/` is not staged.

## Definition of Done

TASK-007 is done only when tests pass, documentation is synchronized, `validate-quick-answer` passes for the mock scenario, and the main Financial Agent System repository remains unchanged unless a source-rule conflict requires a separate validated change.
