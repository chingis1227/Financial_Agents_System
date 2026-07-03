# TASK-015 — Direct specialist execution

Status: Complete

## Goal

Operationalize direct specialist prefixes in the Automation Lab without expanding them into full AGENT workflows.

## Value

Users can run commands such as `RISK: Nvidia`, `VAL: MSFT`, `ETF: SPY`, `CRYPTO: BTC`, `FI: TLT`, or `IC: MSFT` through a validated execution path that preserves the Financial Agent System direct-specialist boundary.

## Scope

- Add `specialist-run` for supported direct specialist prefixes.
- Add `validate-specialist-run` for saved direct specialist packages.
- Map each prefix to exactly one specialist.
- Save `specialist_report.md` and `audit/` under `Financial Agent Reports\_specialists\`.
- Require `Boundary: Not an IC Action` and reject final action language.
- Preserve live truthfulness: live completion requires a real `sdk_thread_id`; failed live attempts are not counted as completed specialists.

## Out of scope

- Final IC Action.
- Full AGENT report packaging.
- Multi-specialist fan-out from a direct specialist command.
- Moving canonical specialist logic out of the Financial Agent System.

## Test plan

```powershell
.\.venv\Scripts\python.exe -m unittest tests.test_agent_run_cli.AgentRunTask011Tests.test_direct_specialist_run_routes_one_specialist_and_validates tests.test_agent_run_cli.AgentRunTask011Tests.test_direct_specialist_rejects_missing_prefix
.\.venv\Scripts\python.exe -m unittest discover -s tests -p "test_*.py"
```

## Definition of Done

- Each tested prefix maps to one expected specialist.
- Report starts with or contains `Boundary: Not an IC Action`.
- Validation fails on missing prefix, final-action language, missing artifacts, or multi-specialist expansion.
- README and ROADMAP document commands, saved path, and limitations.
