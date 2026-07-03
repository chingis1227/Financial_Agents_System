# TASK-013 — Full Global Public Equity AGENT Cycle

Status: Complete
Date: 2026-07-02

## Goal

Make `agent-run` a real public-equity workflow for global listed equities, not a narrow MSFT/AAPL demo.

TASK-013 implements dynamic instrument resolution, public/no-key source collection, evidence readiness, reader report generation, audit artifacts, and validation for public listed equities across US common equities, US share classes, ADRs / foreign issuers listed in the US, and direct non-US listings.

## Fixed decisions

- Support public listed equities globally: US equities, ADRs, direct non-US listings, and share classes.
- US equities use the deep public path: ticker -> CIK -> SEC submissions -> companyfacts -> filings -> price/history -> report/audit.
- ADRs are supported, but explicitly marked as ADR / foreign issuer and carry an ADR gate: underlying issuer, country, currency, reporting, liquidity, regulator/delisting risk.
- Non-US direct listings use issuer IR, annual/interim reports, exchange/regulator candidates, Stooq/Yahoo public price data, and search/IR candidates where available. If source quality is weak, output is Limited or Blocked.
- Private companies are not ordinary public-equity investment targets; they are blocked as public equity and can only be used for ecosystem context / proxy search later.
- Complex instruments such as preferred shares, options, warrants, rights, units, and complex OTC-like instruments are not treated as ordinary equity.
- No API keys are used. TASK-013 uses public/free/no-key sources only.
- Price provider order: Stooq first, official exchange/issuer quote where available, Yahoo/yfinance-style public chart fallback.
- Source candidates and provider results are stored in `audit/`.
- Reader output remains `investment_report.md`; technical evidence/source/runtime details remain under `audit/`.
- Old behavior saying TASK-012 supports only MSFT/AAPL is removed from runtime behavior.

## Implementation scope

Automation Lab only, unless a real canonical conflict is found in the main Financial Agent System. No canonical investment rules are moved into this lab.

Implemented / targeted components:

- `agent_data/equity_resolver.py`: dynamic public-equity resolver and instrument classification.
- `agent_data/equity_preflight.py`: resolver-driven mock/live source preflight for US, ADR, and non-US equities.
- `agent_data/source_fetchers.py`: public source helpers including Stooq-first quote/history and SEC foreign-issuer forms.
- `agent_data/source_registry.py`: TASK-013 source registry and required/important/nice-to-have source definitions.
- `fa_automation.py`: AGENT intake/run/report/manifest/validator updates.
- `tests/`: regression, dynamic US equity, share class, ADR, non-US, private, complex-instrument, evidence, freshness, and clean-report tests.
- `README.md`, `ROADMAP.md`, and this task document.

## Definition of Done

TASK-013 is complete only when:

- MSFT/AAPL whitelist is gone from runtime behavior.
- Any public equity request is classified by instrument type rather than hardcoded ticker.
- US equities, share classes, ADRs, and non-US listed equities have working public-source collection paths.
- Private companies and complex instruments are handled honestly and not misclassified.
- `investment_report.md` plus `audit/` are produced according to report/audit rules.
- Evidence gaps produce Limited/Blocked output, not fabricated analysis.
- Mock tests and live smokes pass or downgrade with recorded reasons.
- `agent-run --mode live` invokes the Financial Agent System Codex SDK CLI through `npm.cmd`; Python `openai_codex` is not required for AGENT specialist execution.
- Specialist audit records `codex_execution_path`, Codex SDK project root, SDK log dir, SDK thread id, SDK error, subprocess exit code, timeout seconds/source, started/completed timestamps, duration seconds, and attempt history.
- Live execution is staged: `evidence-collector` first; all non-IC specialists in parallel with `FA_AUTOMATION_AGENT_MAX_PARALLEL_SPECIALISTS`; `investment-committee-agent` only after all upstream specialist handoffs required for Complete succeed.
- Live production timeout defaults are `FA_AUTOMATION_CODEX_SDK_TIMEOUT_SECONDS=900` per specialist subprocess attempt, `FA_AUTOMATION_AGENT_TOTAL_TIMEOUT_SECONDS=7200` as a hard full-run wall-clock budget, and `FA_AUTOMATION_AGENT_MAX_PARALLEL_SPECIALISTS=3`, with per-specialist overrides such as `FA_AUTOMATION_CODEX_SDK_TIMEOUT_EQUITY_AGENT` and `FA_AUTOMATION_CODEX_SDK_TIMEOUT_FINANCIAL_STATEMENT_ANALYSIS`. A failed first attempt may retry once only inside the remaining full-run budget.
- Failed and timed-out live specialist attempts remain in `attempted_subagents` only and do not appear in `actual_subagents_run`.
- A full live MSFT smoke reaches `workflow_complete=true`, `analysis_status=Complete`, `ic_final_owner=true`, `production_real_subagents=true`, and `failed_required_specialists=[]`.
- Every item in `actual_subagents_run` has a non-empty `sdk_thread_id` in live mode, and `actual_subagents_run.length == AGENT_SPECIALISTS_EQUITY.length`.
- IC `consumed_handoff_ids` includes every upstream specialist handoff.
- Successful Complete reports start with `Report status: Complete`; failed/timeout/partial specialist paths start with `Report status: Limited` and explain `stop_reason` in the manifest.
- Validators enforce global public-equity behavior.
- README, ROADMAP, and TASK-013 are synchronized.
- Mandatory review sub-agent loop reaches >=9.0/10 with GPT 5.5, Reasoning Medium, Speed Standard not Fast.
- No known conceptual gap remains that would require a later task just to finish the equity cycle.

## Required tests and smokes

Required automated test command:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests
```

Required mock smokes:

```powershell
.\.venv\Scripts\python.exe fa_automation.py agent-run --prompt "MSFT for 3 years" --continue-with-baseline --mode mock
.\.venv\Scripts\python.exe fa_automation.py validate-agent-run
.\.venv\Scripts\python.exe fa_automation.py agent-run --prompt "AAPL for 3 years" --continue-with-baseline --mode mock
.\.venv\Scripts\python.exe fa_automation.py validate-agent-run
.\.venv\Scripts\python.exe fa_automation.py agent-run --prompt "NVDA for 3 years" --continue-with-baseline --mode mock
.\.venv\Scripts\python.exe fa_automation.py validate-agent-run
.\.venv\Scripts\python.exe fa_automation.py agent-run --prompt "GOOGL for 3 years" --continue-with-baseline --mode mock
.\.venv\Scripts\python.exe fa_automation.py validate-agent-run
.\.venv\Scripts\python.exe fa_automation.py agent-run --prompt "BABA for 3 years" --continue-with-baseline --mode mock
.\.venv\Scripts\python.exe fa_automation.py validate-agent-run
.\.venv\Scripts\python.exe fa_automation.py agent-run --prompt "ASML.AS for 3 years" --continue-with-baseline --mode mock
.\.venv\Scripts\python.exe fa_automation.py validate-agent-run
```

Required live/public no-key smokes:

- `NVDA` — ordinary US equity.
- `GOOGL` — US share class.
- `BABA` — ADR / foreign issuer.
- `ASML.AS` — direct non-US listing; if unavailable, use `NESN.SW` fallback.

Each smoke must record report path, audit path, source statuses, evidence readiness, Complete/Limited/Blocked status, and downgrade reason.

Required full live Complete smoke command:

```powershell
$env:FA_AUTOMATION_CODEX_SDK_TIMEOUT_SECONDS='900'
$env:FA_AUTOMATION_AGENT_TOTAL_TIMEOUT_SECONDS='7200'
$env:FA_AUTOMATION_AGENT_MAX_PARALLEL_SPECIALISTS='3'
.\.venv\Scripts\python.exe fa_automation.py agent-run --prompt "MSFT for 3 years" --continue-with-baseline --mode live
.\.venv\Scripts\python.exe fa_automation.py validate-agent-run
```

Expected final manifest fields for the full live Complete smoke:

- `workflow_complete=true`
- `analysis_status=Complete`
- `ic_final_owner=true`
- `production_real_subagents=true`
- `failed_required_specialists=[]`
- every `actual_subagents_run[]` item has a non-empty `sdk_thread_id`
- `actual_subagents_run.length == AGENT_SPECIALISTS_EQUITY.length`
- IC `consumed_handoff_ids` contains every upstream specialist id
- `investment_report.md` first line starts with `Report status: Complete`

## Validation evidence

Current validation after implementation before mandatory review loop:

- Unit tests after review-cycle-2 fixes: `134 tests OK` via `.\.venv\Scripts\python.exe -m unittest discover -s tests`.
- Mock smokes passed and validated for: MSFT, AAPL, NVDA, GOOGL, BABA, ASML.AS.
- Initial mock smoke results were saved to `runs/task013_mock_validation.json`; post-review-1 mock smoke results were saved to `runs/task013_mock_validation_review1.json`; numeric non-US smoke results for `7203.T` and `9988.HK` were saved to `runs/task013_numeric_non_us_mock_smokes.json`.
- Live/public no-key smokes were run for: NVDA, GOOGL, BABA, ASML.AS; post-review-1 also added AMD as an unseeded-US dynamic SEC ticker smoke.
- Initial live smoke results were saved to `runs/task013_live_smokes.json` and `runs/task013_live_smoke_summary.json`; post-review-1 results were saved to `runs/task013_live_smokes_review1.json` and `runs/task013_live_smoke_summary_review1.json`.
- Live source/evidence outcomes:
  - NVDA: `us_common_equity`, Evidence readiness `Complete`, required source preflight passed, report/audit produced, `validate-agent-run` passed.
  - GOOGL: `us_share_class`, Evidence readiness `Complete`, required source preflight passed, report/audit produced, `validate-agent-run` passed.
  - BABA: `adr_or_foreign_issuer_us_listing`, Evidence readiness `Complete`, ADR/foreign issuer gate present, required source preflight passed, report/audit produced, `validate-agent-run` passed.
  - ASML.AS: `non_us_listed_equity`, Evidence readiness `Limited`; required non-US source categories are marked `partial` where issuer/regulator documents are candidates but not fully extracted/verified, and issuer event/news sources were missing, so the report records limitation instead of pretending full evidence.
- Short-timeout live smokes used `FA_AUTOMATION_LIVE_TIMEOUT_SECONDS=8` and therefore recorded `controlled_specialist_gap` for required specialist execution. CLI output and validator output explicitly say package validation passed with a controlled specialist gap; this is not claimed as production real-subagent readiness. A separate normal-timeout live proof run for NVDA used `FA_AUTOMATION_LIVE_TIMEOUT_SECONDS=120` and completed all 11 specialists, with `workflow_status=completed`, `production_real_subagents=true`, `full_agent_execution_status=complete`, and `validate-agent-run` pass. Results are saved in `runs/task013_live_specialist_proof_attempt.json` and `runs/task013_live_specialist_proof_summary.json`.
- Main Financial Agent System was not changed, so its three validators are not required for TASK-013 unless later edits touch that repo.

### Current implementation validation

- Unit tests after full live Complete hardening: `150 tests OK` via `py -3 -m unittest discover -s tests -p "test_*.py"`.
- Mock smokes: passed.
- Live smokes: passed for source/report/validator package with the source readiness statuses above; specialist runtime gap recorded honestly.
- Full live MSFT Complete smoke after final hard-timeout/report-sanitization fixes: `C:\Users\ShumeikoYe\OneDrive\Documents\Financial Agent Reports\MSFT 2026-07-02 2243\investment_report.md`.
  - `workflow_complete=true`
  - `analysis_status=Complete`
  - `ic_final_owner=true`
  - `production_real_subagents=true`
  - `failed_required_specialists=[]`
  - `actual_subagents_run` count `11`, all with real `sdk_thread_id`
  - IC consumed upstream handoff count `10`
  - report first line: `Report status: Complete - IC synthesis complete; not a personal position-sizing instruction.`
- `validate-agent-run`: passed for successful/limited mock and live smoke packages.
- Main Financial Agent System validators: not required because main project was not changed.

## Mandatory review loop record

Every review sub-agent must use GPT 5.5, Reasoning Medium, Speed Standard not Fast. Final accepted review score: 9/10.

| Cycle | Reviewer score | Main comments | Fixes made | Tests rerun | Accepted? |
|---|---:|---|---|---|---|
| 1 | 6/10 | Non-US proxies too synthetic; resolver static/generic; ADR gate weak; live specialist gap looked like completed; report too generic; provider audit not separate. | Marked non-US direct required proxies as `partial` and Limited; added structured ADR gate + validator checks; added `provider_results.json`; added evidence facts to report and specialist prompts; changed CLI/validator wording for controlled specialist gap; added AMD live smoke and regression tests. | `132 tests OK`; mock smokes review1; live smokes review1. | No ? fixes made and new review required. |
| 2 | 8/10 | Numeric non-US tickers like `7203.T` / `9988.HK` did not resolve; complex guard too broad; no successful normal-timeout live specialist proof. | Added numeric/global ticker parsing and seeds for `7203.T` / `9988.HK`; added Stooq suffixes `.T` -> `.jp` and `.HK`; narrowed complex-instrument regex to avoid false positives such as `human rights` or `United`; made non-US report wording avoid SEC/XBRL equivalence; ran normal-timeout NVDA live proof with all 11 specialists completed. | `134 tests OK`; numeric non-US mock smokes; NVDA live specialist proof. | No ? fixes made and new review required. |
| 3 | 9/10 | Accepted. No must-fix issues. Nice-to-have only: stale compatibility labels, more live non-US examples over time, comparison detection if expected later. | No code fixes required after this review. Recorded final accepted score and completion status. | `py_compile`, `git diff --check`, main repo status check. | Yes ? final accepted score >=9.0. |

## Final status

TASK-013 is complete. Review loop reached 9/10 with no must-fix issues. Remaining reviewer notes are nice-to-have only and do not leave a conceptual equity-cycle completion gap.
