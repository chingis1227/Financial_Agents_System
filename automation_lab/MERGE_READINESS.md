# Automation Lab Merge Readiness

Status: Current integration checklist
Last updated: 2026-07-03

## Purpose

`automation_lab/` is now the integrated execution/orchestration layer inside the `Financial Agent System` repository.

The integration removes the need for a second GitHub repository and keeps the system in one GitHub repository while preserving the architecture boundary:

- Financial Agent System remains the source of truth for investment rules, route cards, agents, skills, evidence policy, IC gates, report schemas, and validation contracts.
- Automation Lab owns CLI orchestration, deterministic smoke runs, public/no-key data snapshots, live Codex SDK specialist execution, report-package creation, audit files, and live-acceptance manifests.

## Repository requirements

- `automation_lab/` must not contain a nested `.git/` directory.
- Local/generated Lab folders must not be committed:
  - `automation_lab/.venv/`
  - `automation_lab/runs/`
  - `automation_lab/data_runs/`
  - `automation_lab/.pytest_cache/`
  - `automation_lab/**/__pycache__/`
- Reader-facing full-workflow reports remain outside the repository under:

```text
C:\Users\ShumeikoYe\OneDrive\Documents\Financial Agent Reports\
```

## Runtime requirements

- `fa_automation.py` must resolve the main project root from `FA_AUTOMATION_PROJECT_ROOT` when set, otherwise from `automation_lab/..`.
- Live AGENT runs must use the main Financial Agent System Codex SDK control layer.
- Automation Lab must not redefine canonical investment logic that belongs to `implementation/`, `workflows/route_cards/`, `.codex/agents/`, or `.agents/skills/`.
- Live acceptance must distinguish deterministic smoke coverage from real live `sdk_thread_id` evidence.

## Required checks

From the main repository root:

```powershell
py -3 tools\validate_project_consistency.py
py -3 tools\validate_behavior_contracts.py
py -3 tools\validate_runtime_readiness.py
npm.cmd run build
npm.cmd test
npm.cmd run codex:doctor
npm.cmd run codex:run -- --prompt "QUICK: Microsoft" --dry-run
cd automation_lab
..\.venv\Scripts\python.exe -m unittest discover -s tests -p "test_*.py"
..\.venv\Scripts\python.exe fa_automation.py live-acceptance --require-live
cd ..
```

## Readiness criteria

The merged repository is ready when:

1. Financial Agent System validators pass.
2. Codex SDK build/test/doctor/dry-run checks pass.
3. Automation Lab unit tests pass from `automation_lab/` using the main repository virtual environment.
4. `live-acceptance --require-live` passes or, if current live artifacts have been intentionally cleaned, the gap is reported honestly rather than downgraded silently.
5. `README.md`, `PROJECT_STATE.md`, and this file all point to `automation_lab/` as the integrated execution layer.
6. Git staging does not include generated `runs/`, `data_runs/`, virtual environments, or Python caches.
