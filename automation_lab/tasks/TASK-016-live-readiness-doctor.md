# TASK-016 — Live readiness doctor

Status: Complete

## Goal

Add an audited readiness check for Automation Lab live mode before long Codex SDK specialist runs.

## Value

Live AGENT and direct specialist runs are expensive and can take a long time. `live-doctor` proves the local execution layer can reach the Financial Agent System Codex SDK doctor, write report/log artifacts, and parse timeout/env configuration before the user starts a live workflow.

## Scope

- Add `live-doctor` CLI command.
- Check Financial Agent System root, `AGENTS.md`, `package.json`, built Codex SDK CLI, Automation Lab `.venv`, tests directory, report-root writability, timeout/env settings, prompt-file transport, and public/no-key source boundary.
- Optionally run the Financial Agent System `npm.cmd run codex:doctor` check.
- Write JSON readiness logs under `runs/live-doctor/`.

## Out of scope

- Running investment analysis.
- Starting live AGENT specialists.
- Claiming live completion or `sdk_thread_id` evidence.

## Test plan

```powershell
.\.venv\Scripts\python.exe -m unittest tests.test_agent_run_cli.AgentRunTask011Tests.test_live_doctor_checks_prerequisites_and_writes_log
.\.venv\Scripts\python.exe fa_automation.py live-doctor
.\.venv\Scripts\python.exe -m unittest discover -s tests -p "test_*.py"
```

## Definition of Done

- `live-doctor` exits 0 when live prerequisites are present.
- A JSON readiness log is written.
- Tests verify key checks and live-mode coverage list.
- README and ROADMAP document the command and limitation.
