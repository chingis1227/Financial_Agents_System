# TASK-011 — Full AGENT MSFT/Equity Vertical Slice

Status: Complete
Date: 2026-07-02

## Goal

Implement the first real end-to-end `AGENT:` workflow for MSFT/equity in the Automation Lab while preserving the main Financial Agent System as the source of truth.

## Value

TASK-011 turns the AGENT path from design-only into a production-ish v1 vertical slice: intake, source preflight, evidence pack, specialist handoffs, reader-facing report, audit, and deterministic validation.

## Dependencies

- TASK-007 through TASK-010 QUICK/data/output-quality foundation is complete.
- TASK-006 AGENT design exists.
- Main Financial Agent System route cards and canonical rules remain authoritative.
- Live specialist execution depends on `openai-codex` live dependency when `--mode live` is used.

## Scope

Implemented in Automation Lab only:

- `agent-intake` asks exactly five questions and stops.
- `agent-run` supports MSFT/equity only.
- `validate-agent-run` validates latest or specified run.
- Deep MSFT source preflight with Required / Important / Nice-to-have source classes.
- Public/no-key baseline sources plus optional future API-compatible architecture.
- Evidence pack with claim support matrix, freshness, source tiers, missing/weak evidence, and pre-IC lock.
- Mock specialist handoffs for deterministic tests and live Codex SDK specialist-run contract for production use.
- Reader-facing `investment_report.md` plus technical `audit/` outside both repositories.

## Out of scope

- Multi-asset AGENT execution.
- Non-MSFT equity coverage.
- Full DCF spreadsheet model.
- Paid/paywalled scraping.
- Moving canonical rules from the main Financial Agent System into Automation Lab.
- Treating mock specialist outputs as production real subagent execution.

## Implementation plan

1. Add `agent_data/` source preflight, source registry, fetchers, and evidence pack builders.
2. Add fixture-first MSFT deep equity source pack for tests.
3. Add AGENT CLI commands and validation.
4. Generate report folder under `Financial Agent Reports\MSFT yyyy-mm-dd hhmm\`.
5. Save audit artifacts, raw specialist outputs, normalized handoffs, run manifest, and validation files.
6. Keep reader report clean and human-readable; keep technical labels in audit.

## Test plan

Run:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests
```

Smoke:

```powershell
.\.venv\Scripts\python.exe fa_automation.py agent-run --prompt "MSFT for 3 years" --answer "3 years" --answer "No current position" --answer "Quality compounder and valuation entry" --answer "Use latest public data if available" --answer "No portfolio context provided" --mode mock
.\.venv\Scripts\python.exe fa_automation.py validate-agent-run
```

## Docs synchronization note

README and ROADMAP document TASK-011 commands, report location, and audit boundary. Main Financial Agent System is unchanged unless a future rule/schema change is required; if changed, run its three validators.

## Review checklist

- [x] Design review loop reached >=9.0 before implementation.
- [x] `agent-intake` asks exactly five questions and stops.
- [x] `agent-run` records answered, unanswered, baseline assumptions, and portfolio-context limits.
- [x] Source preflight distinguishes required, important, and nice-to-have sources.
- [x] Evidence pack is not a QUICK snapshot.
- [x] Mock mode does not count as production real subagents.
- [x] Reader report hides runtime/debug labels.
- [x] Audit preserves technical statuses and raw outputs.
- [x] Validators and tests cover the run.

## Definition of Done

TASK-011 is complete when `agent-run` creates a validated MSFT `investment_report.md` and `audit/` outside both repositories, deterministic tests pass, mock smoke passes, live/public smoke is attempted or documented, and final review reaches >=9.0 with no must-fix items.
