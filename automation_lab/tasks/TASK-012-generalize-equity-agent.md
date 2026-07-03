# TASK-012 — Generalize Full Equity AGENT Beyond MSFT

Status: Complete
Date: 2026-07-02

## Goal

Generalize the full `AGENT:` equity workflow from the TASK-011 MSFT-only vertical slice to a supported-equity v1 path covering MSFT and AAPL.

## Value

TASK-012 proves the full AGENT architecture is not hardcoded to one company. It keeps MSFT as the regression baseline and adds AAPL as a second large public-equity target with the same source preflight, evidence pack, specialist handoffs, reader-facing report, audit, and validation structure.

## Dependencies

- TASK-011 full MSFT/equity vertical slice is present in the Automation Lab working tree.
- Main Financial Agent System remains the source of truth for routing, evidence, IC gates, language, and report boundaries.
- Public/no-key source providers remain the baseline for live mode.

## Scope

Implemented in Automation Lab only:

- Supported equity identity layer for MSFT and AAPL.
- Generic supported-equity `agent-run`, `agent-intake`, and `validate-agent-run` behavior.
- Asset-parametric source preflight using selected ticker and CIK.
- AAPL historical fixture evidence fixture.
- Generic evidence pack claims and reader report generation by subject.
- Validation that checks selected subject identity instead of MSFT-only identity.
- Tests for MSFT regression, AAPL execution, latest supported-equity validation, unsupported-asset rejection, source freshness, evidence gaps, and mock-subagent boundaries.

## Out of scope

- ETF, crypto, fixed income, commodity, or multi-asset full AGENT execution.
- Paid/API-key provider integration.
- Moving canonical investment rules from the main Financial Agent System into the Automation Lab.
- Treating historical fixture specialist outputs as production real subagent execution.

## Implementation plan

1. Add supported equity identity metadata for MSFT and AAPL.
2. Generalize the source registry and preflight builder from MSFT-only to supported-equity subject identity.
3. Add AAPL fixture and keep MSFT fixture as regression baseline.
4. Update AGENT CLI runtime to detect supported equity ticker, create ticker-specific report folders, and generate subject-specific report/audit artifacts.
5. Update validators to check selected subject identity and supported-equity latest-run discovery.
6. Synchronize README, ROADMAP, and this task document.
7. Run deterministic tests, historical fixture smokes, live/public smoke attempt, final repository checks, and sub-agent review loop.

## Test plan

Required checks:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests
.\.venv\Scripts\python.exe fa_automation.py agent-run --prompt "MSFT for 3 years" --answer "3 years" --answer "No current position" --answer "Quality compounder and valuation entry" --answer "Use latest public data if available" --answer "No portfolio context provided" --mode live
.\.venv\Scripts\python.exe fa_automation.py validate-agent-run
.\.venv\Scripts\python.exe fa_automation.py agent-run --prompt "AAPL for 3 years" --answer "3 years" --answer "No current position" --answer "Quality compounder and valuation entry" --answer "Use latest public data if available" --answer "No portfolio context provided" --mode live
.\.venv\Scripts\python.exe fa_automation.py validate-agent-run
```

Live/public AAPL smoke should be attempted. If public data, SDK dependency, or timeout fails, record the limitation and do not fake production readiness.

## Docs synchronization note

README and ROADMAP are synchronized for TASK-012. The main Financial Agent System was not changed; therefore its three validators are not required for this task.

## Review checklist

- [x] `agent-run` supports MSFT and AAPL.
- [x] Unsupported assets remain blocked.
- [x] Source preflight uses selected CIK and ticker.
- [x] Validator checks selected subject identity, not MSFT only.
- [x] AAPL fixture exists and tests pass.
- [x] Reader report is subject-specific and avoids hardcoded MSFT narrative for AAPL.
- [x] Technical labels and runtime details remain in `audit/`.
- [x] Historical fixture path does not count as production real subagents.
- [x] README and ROADMAP are synchronized.
- [x] Final sub-agent review loop reached >=9.0. Final reviewer score: 9/10; no must-fix issues.

## Final validation evidence

Latest local validation after second-review fixes:

- Unit tests: `126 tests OK` via `.\.venv\Scripts\python.exe -m unittest discover -s tests`.
- MSFT historical fixture smoke: `agent-run` plus `validate-agent-run` passed.
- AAPL historical fixture smoke: `agent-run` plus `validate-agent-run` passed.
- AAPL Russian historical fixture smoke: `agent-run` plus `validate-agent-run` passed, with natural Russian reader-facing report headings and no mojibake.
- AAPL live/public smoke: attempted; stopped before normal report generation because required source preflight marked the latest AAPL 8-K stale under the current 45-day freshness hard gate. This was not claimed as a successful live run.
- `git diff --check`: no whitespace errors; Git reported only a CRLF normalization warning for `fa_automation.py`.
- Main Financial Agent System: unchanged / clean git status, so its three validators were not required.

Sub-agent review loop:

- Review 1: 8/10. Must-fix: historical fixture freshness would age out. Addressed by current-date stamping of historical fixture freshness-sensitive source records and added regression test.
- Review 2: 8/10. Must-fix: Russian report mojibake and pending task-doc evidence. Addressed by Unicode-safe Russian report template, Russian AAPL validation test, and this evidence update.
- Review 3: 9/10. No must-fix issues. Done conditional only on recording this score in this task document; recorded here.

## Definition of Done

TASK-012 is complete when tests pass, MSFT and AAPL historical fixture smokes validate, live/public AAPL smoke is attempted or limitation-recorded, docs are synchronized, final repository checks pass, and final sub-agent review reaches >=9.0 with no must-fix issues.
