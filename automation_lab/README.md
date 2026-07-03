# Financial Agent Automation Lab

Pre-production automation layer for the Financial Agent System.

## Source of truth

Financial Agent System remains the source of truth for investment rules, routing, agents, skills, and validation contracts.

Main project root:

```text
C:\Users\ShumeikoYe\OneDrive\Documents\Financial Agent System
```

This lab can automate and test workflows, but it must not redefine investment logic, route cards, agent contracts, skill behavior, evidence gates, or IC action rules.

## Current status

- TASK-001: route-check scaffold is complete.
- TASK-002: live Codex SDK route-check is implemented.
- TASK-003: draft data source maps are complete under `data_sources/`.
- TASK-004: guarded QUICK automation is implemented as `quick-run`.
- TASK-005: QUICK result quality control is implemented for structure, freshness boundary, and forbidden final-action markers.
- TASK-006: AGENT automation design is implemented as `agent-design` in design-only mock mode.
- TASK-007: QUICK answer public-data pilot is implemented as `quick-answer` for MSFT/equity.
- TASK-008: QUICK answer asset expansion is implemented for SPY, BTC, TLT, GLD, and `MSFT vs SPY vs BTC`.
- TASK-009: QUICK provider registry foundation is implemented in `quick_data/` with public providers, disabled API slots, source quality, freshness, fallback, and provider-error snapshots.
- TASK-010: QUICK output quality control v2 is implemented with `output_quality.json`, source/freshness notes, hidden-action checks, overconfidence checks, and risk-specificity checks.
- TASK-011: full AGENT MSFT/equity vertical slice is implemented as `agent-intake`, `agent-run`, and `validate-agent-run`.
- TASK-012: full AGENT equity workflow is generalized to supported equities v1: MSFT and AAPL.
- TASK-013: full AGENT equity workflow now resolves global public listed equities by instrument class: US common equities, US share classes, ADRs / foreign-issuer US listings, and direct non-US listings. Private companies and complex instruments are blocked as ordinary equity.
- TASK-013 bridge hardening: `agent-run --mode live` now launches real specialist attempts through the Financial Agent System Codex SDK CLI instead of requiring the unavailable Python `openai_codex` bridge.
- TASK-014: full AGENT validated smoke paths now cover ETF/fund, fixed income, crypto, commodity, and multi-asset comparison in addition to the global public-equity path. These paths create `investment_report.md`, `audit/`, source preflight, evidence pack, specialist handoffs, run manifest, and validation files. Mock mode is deterministic; live mode uses the same staged Codex SDK specialist launcher and remains Limited when live specialist/source gates do not complete.
- TASK-015: direct specialist execution is implemented as `specialist-run` / `validate-specialist-run` for RISK, VAL, MACRO, NEWS, PORTFOLIO, SECTOR, EVIDENCE, POSITIONING, INTEL, EQUITY, ETF, COMMODITY, CRYPTO, FI, WINNERS, and IC. Each run maps to exactly one specialist, saves `specialist_report.md` plus `audit/`, shows `Boundary: Not an IC Action`, and forbids final action language.
- TASK-016: live readiness doctor is implemented as `live-doctor`; it checks Automation Lab + Financial Agent System Codex SDK prerequisites, report-root writability, timeout/env settings, prompt-file transport, and public/no-key source assumptions before long live runs.
- TASK-017: live acceptance manifest is implemented as `live-acceptance`; it audits current QUICK, AGENT, direct specialist, and live-doctor artifacts, separates deterministic smoke coverage from real live `sdk_thread_id` evidence, and can fail with `--require-live` when live evidence is missing.
- TASK-018: structured portfolio-context input is implemented for `agent-run` through `--portfolio-context-json` and `--portfolio-context-file`; the context is written to audit, propagated to Portfolio Fit/report text, and does not unlock final action or exact sizing without gated IC conditions.
- TASK-019: live usage-limit handling is implemented; AGENT live retries stop when the Codex SDK reports a usage limit, audit records the reset hint, and `live-acceptance` reports `usage_limit_gaps` separately from smoke gaps.
- TASK-020: live acceptance is complete for the supported runtime matrix. QUICK live/public validation, full AGENT live packages for equity, ETF/fund, fixed income, crypto, commodity, and multi-asset comparison, and all direct specialist prefixes have real `sdk_thread_id` evidence; `live-acceptance --require-live` passes with no smoke, live, or usage-limit gaps.



## Unified repository location

Automation Lab is now integrated under the main repository at:

```text
C:\Users\ShumeikoYe\OneDrive\Documents\Financial Agent System\automation_lab
```

Use the main repository virtual environment from this directory:

```powershell
cd "C:\Users\ShumeikoYe\OneDrive\Documents\Financial Agent System\automation_lab"
..\.venv\Scripts\python.exe -m unittest discover -s tests -p "test_*.py"
```

Keep generated `runs/` and `data_runs/` local/ignored. Reader-facing AGENT reports remain outside the repo under `C:\Users\ShumeikoYe\OneDrive\Documents\Financial Agent Reports\`.

## Data source map draft

TASK-003 adds draft source maps under:

```text
data_sources/
```

These files are Automation Lab planning artifacts only. They do not create canonical source authority for the Financial Agent System.

## Live dependency

Route-check and QUICK live experiments may still use the optional Python live dependency:

```powershell
..\.venv\Scripts\python.exe -m pip install -r requirements-live.txt
```

The dependency file is intentionally named `requirements-live.txt` rather than `requirements.txt` so the TASK-001 no-dependency scaffold remains conceptually separate from TASK-002 live execution.

For `agent-run --mode live`, Automation Lab calls the main Financial Agent System Codex SDK CLI for equity and the supported non-equity AGENT routes:

```powershell
cd "C:\Users\ShumeikoYe\OneDrive\Documents\Financial Agent System"
npm.cmd install
npm.cmd run build
npm.cmd run codex:doctor
```



Build a live acceptance manifest from the artifacts currently on disk:

```powershell
..\.venv\Scripts\python.exe fa_automation.py live-acceptance
..\.venv\Scripts\python.exe fa_automation.py live-acceptance --require-live
```

`live-acceptance` does not pretend mock runs are live. It records which QUICK, AGENT routes, and direct specialist prefixes have validated smoke artifacts and which still lack real live `sdk_thread_id` evidence. The command writes JSON logs under `runs/live-acceptance/`.

When the Codex SDK reports a usage limit, live AGENT retries stop rather than spending another attempt. The reset hint is recorded in specialist audit files and summarized as `usage_limit_gaps` in `live-acceptance`.

Current live acceptance status after TASK-020: `live-acceptance --require-live` passes for QUICK live/public validation, all supported AGENT routes, and all direct specialist prefixes. The latest successful AGENT live route examples are MSFT/equity, SPY/ETF, TLT/fixed income, BTC/crypto, GLD/commodity, and MSFT-SPY-BTC/multi-asset comparison.

Check live readiness before long live runs:

```powershell
..\.venv\Scripts\python.exe fa_automation.py live-doctor
```

`live-doctor` writes a readiness JSON log under `runs/live-doctor/` and verifies the Automation Lab environment, Financial Agent System Codex SDK doctor, report-root write access, timeout settings, prompt-file transport, and the public/no-key data boundary.

Then run the Automation Lab live AGENT workflow. Use mock mode for deterministic validation and live mode for real Codex SDK specialist attempts:

```powershell
cd "C:\Users\ShumeikoYe\OneDrive\Documents\Financial Agent System\automation_lab"
..\.venv\Scripts\python.exe fa_automation.py agent-run --prompt "MSFT for 3 years" --continue-with-baseline --mode live
..\.venv\Scripts\python.exe fa_automation.py validate-agent-run
..\.venv\Scripts\python.exe fa_automation.py agent-run --prompt "SPY for 5 years" --continue-with-baseline --mode mock
..\.venv\Scripts\python.exe fa_automation.py agent-run --prompt "BTC for 3 years" --continue-with-baseline --mode mock
..\.venv\Scripts\python.exe fa_automation.py agent-run --prompt "TLT bond ETF" --continue-with-baseline --mode mock
..\.venv\Scripts\python.exe fa_automation.py agent-run --prompt "GLD gold ETF" --continue-with-baseline --mode mock
..\.venv\Scripts\python.exe fa_automation.py agent-run --prompt "MSFT vs SPY vs BTC" --continue-with-baseline --mode mock
..\.venv\Scripts\python.exe fa_automation.py validate-agent-run
```

`agent-run --mode live` uses `npm.cmd run codex:run -- --prompt-file "<temp prompt file>" --live --workspace "<Financial Agent System>" --sandbox read_only`. It records Codex SDK thread/log metadata in the specialist audit. Failed or timed-out specialist attempts remain attempted-only and keep the reader report Limited rather than pretending a complete IC workflow.

Full AGENT runs use a staged production runtime:

1. Stage 1 runs `evidence-collector`.
2. Stage 2 runs every non-IC specialist in parallel, capped by `FA_AUTOMATION_AGENT_MAX_PARALLEL_SPECIALISTS` (default `3`).
3. Stage 3 runs `investment-committee-agent` only after every upstream specialist required for Complete has succeeded.

Live timeout controls:

| Environment variable | Default | Meaning |
|---|---:|---|
| `FA_AUTOMATION_CODEX_SDK_TIMEOUT_SECONDS` | `900` | Maximum seconds for one Codex SDK specialist subprocess attempt. A failed first attempt may retry once, but each attempt is capped by remaining full-run budget. |
| `FA_AUTOMATION_AGENT_TOTAL_TIMEOUT_SECONDS` | `7200` | Hard wall-clock budget for one full `agent-run --mode live`; remaining budget caps specialist subprocess attempts and stops later waves/IC when exhausted. |
| `FA_AUTOMATION_AGENT_MAX_PARALLEL_SPECIALISTS` | `3` | Maximum parallel non-IC specialist runs. |
| `FA_AUTOMATION_CODEX_SDK_TIMEOUT_EQUITY_AGENT` | optional | Per-specialist override; use the specialist id converted to upper snake case. |
| `FA_AUTOMATION_CODEX_SDK_TIMEOUT_FINANCIAL_STATEMENT_ANALYSIS` | optional | Per-specialist override for financial-statement-analysis. |

`Complete` means `workflow_complete=true`, `analysis_status=Complete`, `ic_final_owner=true`, all equity specialists completed, every completed live specialist has a real `sdk_thread_id`, IC consumed every upstream handoff, source/evidence preflight is not Blocked, and the report validator passes. Any failed, missing, or timed-out specialist keeps `workflow_complete=false`, `analysis_status=Limited`, explains `stop_reason`, and makes the first report line start with `Report status: Limited`.

## Commands

Run mock route check:

```powershell
..\.venv\Scripts\python.exe fa_automation.py route-check --mode mock
```

Run default route check, equivalent to mock:

```powershell
..\.venv\Scripts\python.exe fa_automation.py route-check
```

Run live Codex SDK route check:

```powershell
..\.venv\Scripts\python.exe fa_automation.py route-check --mode live
```

Launch guarded QUICK first step in mock mode:

```powershell
..\.venv\Scripts\python.exe fa_automation.py quick-run --prompt "Microsoft for 3 years" --mode mock
```

Launch guarded QUICK first step in live mode:

```powershell
..\.venv\Scripts\python.exe fa_automation.py quick-run --prompt "Microsoft for 3 years" --mode live
```

`quick-run` adds the `QUICK:` prefix when omitted and is limited to the Quick Take first action: exactly three relevant questions, a `Status: Preliminary` or `Status: Limited` line, no saved investment report, no audit folder, and no final IC Action.

TASK-005 quality control requires `Status:` to be the first non-empty line, exactly three numbered questions, and `Status: Limited` plus an explicit freshness/current-source question when the prompt depends on today/latest/news/earnings/price action/current data.

Create the second QUICK step, a validated Quick Take answer from the prompt plus the three user answers. TASK-008 supports MSFT, SPY, BTC, TLT, GLD, and the limited comparison pilot `MSFT vs SPY vs BTC`:

```powershell
..\.venv\Scripts\python.exe fa_automation.py quick-answer --prompt "Microsoft for 3 years" --answer "3 years" --answer "No current position" --answer "No latest data requirement" --mode mock
```

Run the same step in live/public mode without API keys:

```powershell
..\.venv\Scripts\python.exe fa_automation.py quick-answer --prompt "Microsoft for 3 years" --answers-json '["3 years","No current position","Use public current sources if available"]' --mode live
```

TASK-008 mock examples:

```powershell
..\.venv\Scripts\python.exe fa_automation.py quick-answer --prompt "SPY for 5 years" --answer "5 years" --answer "No current position" --answer "No latest data requirement" --mode mock
..\.venv\Scripts\python.exe fa_automation.py quick-answer --prompt "BTC for 3 years" --answer "3 years" --answer "No current position" --answer "No latest data requirement" --mode mock
..\.venv\Scripts\python.exe fa_automation.py quick-answer --prompt "TLT bond ETF" --answer "3 years" --answer "No current position" --answer "No latest data requirement" --mode mock
..\.venv\Scripts\python.exe fa_automation.py quick-answer --prompt "GLD gold ETF" --answer "3 years" --answer "No current position" --answer "No latest data requirement" --mode mock
..\.venv\Scripts\python.exe fa_automation.py quick-answer --prompt "MSFT vs SPY vs BTC" --answer "3 years" --answer "No current position" --answer "No latest data requirement" --mode mock
```

`quick-run` only asks the required three intake questions. `quick-answer` takes the original prompt plus exactly three answers, gathers a minimal public-data snapshot, writes validation files, and returns a short Quick Take. Mock mode uses fixtures for stable tests. Live mode uses best-effort public sources without API keys; if price, recent events, or context are unavailable, the result is `Limited`, and if identity or minimum support is missing, the result is `Blocked`. TASK-009 adds the QUICK provider registry foundation without changing the CLI UX. TASK-010 adds output-quality control: every normal Quick Take includes `Source note` and `Freshness note`, and weak output quality is saved for debugging but not printed as a normal successful answer.

Validate a QUICK answer run:

```powershell
..\.venv\Scripts\python.exe fa_automation.py validate-quick-answer --run-dir "data_runs\quick\[timestamp]-MSFT"
```

QUICK answer runs write data snapshots under:

```text
data_runs/quick/[timestamp]-MSFT/
data_runs/quick/[timestamp]-SPY/
data_runs/quick/[timestamp]-BTC/
data_runs/quick/[timestamp]-TLT/
data_runs/quick/[timestamp]-GLD/
data_runs/quick/[timestamp]-MSFT-SPY-BTC/
```

Each run contains `source_snapshot.json`, `data_quality.json`, `quick_answer.json`, and `output_quality.json`. QUICK answer does not create an `investment_report.md` file or an `audit` folder, and it never emits final buy/sell/hold/add/trim/exit language or exact position sizing.

## QUICK output quality

TASK-010 adds deterministic output-quality checks in `quick_data/output_quality.py`. The checks do not call an AI judge, do not require API keys, and do not replace Evidence Collector. They verify that the generated Quick Take has:

- `Source note` describing the public/no-key QUICK snapshot and the Evidence Collector boundary;
- `Freshness note` describing current/latest-data needs or the absence of a freshness downgrade;
- risk language that is ticker-specific in mock mode and at least asset-class-specific in live mode;
- no hidden action phrases such as `start a position`, `accumulate`, `good entry`, `reduce exposure`, `avoid`, or `not investable`;
- no overconfident language such as `guaranteed`, `risk-free`, `definitely`, `strong opportunity`, or `high conviction`;
- no report/audit/AGENT execution claims.

If output quality fails, `quick-answer` still saves the run files, including `output_quality.json`, but it does not print the weak Quick Take as a normal successful answer. `validate-quick-answer` fails any run whose `output_quality.json` has `status: fail`.

## QUICK provider registry

TASK-009 moves QUICK data collection into `quick_data/` while keeping the same `quick-answer` and `validate-quick-answer` commands. The registry records public providers such as SEC submissions, Stooq public CSV, Yahoo public chart, and local static/mock context. Optional API providers such as Alpha Vantage, Financial Modeling Prep, and Nasdaq Data Link are registered as disabled future slots only; no API keys are required or used.

Snapshots now keep the old fields and add provider metadata: `schema_version`, `providers`, `provider_results`, `provider_errors`, `source_scope`, and `evidence_alignment`. Provider failures are stored in JSON so QUICK can degrade to `Limited` or `Blocked` without printing technical error dumps to the user. This is a QUICK pre-evidence snapshot, not an Evidence Collector `evidence_pack.md`; the main Financial Agent System remains the source of truth for evidence policy and full AGENT evidence locks.

Create an AGENT automation design plan in mock mode:

```powershell
..\.venv\Scripts\python.exe fa_automation.py agent-design --prompt "Microsoft for 3 years" --mode mock
```

`agent-design` adds the `AGENT:` prefix when omitted and creates a design-only plan for the large workflow. It does not run evidence collection, valuation, risk review, portfolio-fit review, subagents, IC synthesis, investment reports, or audit folders. The saved design validates exactly five intake questions, source-of-truth boundary, planned-versus-actual subagent truthfulness, route-card existence in the main project, planned subagent files, required evidence/freshness, lead-asset, material-context, valuation, risk, implementation/vehicle-quality, portfolio-fit, audit, and IC gates, and the rule that positive or final IC Action stays locked until required gates pass.


Run a direct specialist command. Direct specialist output is one analyst only, not an IC Action, and does not create a full AGENT `investment_report.md`:

```powershell
..\.venv\Scripts\python.exe fa_automation.py specialist-run --prompt "RISK: Nvidia" --mode mock
..\.venv\Scripts\python.exe fa_automation.py specialist-run --prompt "VAL: MSFT" --mode mock
..\.venv\Scripts\python.exe fa_automation.py specialist-run --prompt "ETF: SPY" --mode mock
..\.venv\Scripts\python.exe fa_automation.py specialist-run --prompt "IC: MSFT" --mode mock
..\.venv\Scripts\python.exe fa_automation.py validate-specialist-run
```

Direct specialist runs are saved under:

```text
C:\Users\ShumeikoYe\OneDrive\Documents\Financial Agent Reports\_specialists\[PREFIX-SUBJECT] yyyy-mm-dd hhmm\specialist_report.md
```

Each package includes `audit/specialist_manifest.json`, `audit/output_validation.json`, `audit/specialist_run_validation.json`, and one specialist handoff folder. Live mode uses the same Codex SDK launcher but still counts only the one mapped specialist; failed or missing live thread ids are not counted as completed live specialists.

Run a full AGENT workflow. TASK-013 supports dynamic public listed equity resolution instead of an MSFT/AAPL whitelist. TASK-014 adds validated smoke paths for ETF/fund, fixed income, crypto, commodity, and multi-asset comparison while preserving the Financial Agent System route cards as source of truth.

Examples:

```powershell
..\.venv\Scripts\python.exe fa_automation.py agent-intake --prompt "NVDA for 3 years"
..\.venv\Scripts\python.exe fa_automation.py agent-run --prompt "NVDA for 3 years" --answer "3 years" --answer "No current position" --answer "Quality compounder and valuation entry" --answer "Use latest public data if available" --answer "No portfolio context provided" --mode mock
..\.venv\Scripts\python.exe fa_automation.py validate-agent-run

..\.venv\Scripts\python.exe fa_automation.py agent-run --prompt "MSFT for 3 years" --continue-with-baseline --portfolio-context-json '{"holdings":[{"ticker":"MSFT","weight":"4%"},{"ticker":"SPY","weight":"35%"}],"cash":"8%","risk_limits":{"max_single_name_weight":"7%","max_drawdown_tolerance":"15%"},"horizon":"3 years","constraints":["USD portfolio","no leverage"],"existing_exposure":"large-cap technology through SPY","objective":"quality growth with controlled concentration"}' --mode mock
..\.venv\Scripts\python.exe fa_automation.py validate-agent-run

..\.venv\Scripts\python.exe fa_automation.py agent-run --prompt "BABA for 3 years" --continue-with-baseline --mode mock
..\.venv\Scripts\python.exe fa_automation.py validate-agent-run

..\.venv\Scripts\python.exe fa_automation.py agent-run --prompt "ASML.AS for 3 years" --continue-with-baseline --mode mock
..\.venv\Scripts\python.exe fa_automation.py validate-agent-run

..\.venv\Scripts\python.exe fa_automation.py agent-run --prompt "SPY for 5 years" --continue-with-baseline --mode mock
..\.venv\Scripts\python.exe fa_automation.py agent-run --prompt "BTC for 3 years" --continue-with-baseline --mode mock
..\.venv\Scripts\python.exe fa_automation.py agent-run --prompt "TLT bond ETF" --continue-with-baseline --mode mock
..\.venv\Scripts\python.exe fa_automation.py agent-run --prompt "GLD gold ETF" --continue-with-baseline --mode mock
..\.venv\Scripts\python.exe fa_automation.py agent-run --prompt "MSFT vs SPY vs BTC" --continue-with-baseline --mode mock
..\.venv\Scripts\python.exe fa_automation.py validate-agent-run
```

`agent-intake` asks exactly five AGENT questions and stops. `agent-run` resolves the requested supported asset or comparison, classifies the route, builds a public/no-key source preflight, creates an evidence pack, runs route-relevant specialist handoffs where available, writes the reader-facing report, and validates the package. It accepts 1-5 answers and records approved baseline assumptions for missing answers; zero-answer execution requires `--continue-with-baseline`. Structured portfolio context can be supplied with `--portfolio-context-json` or `--portfolio-context-file`; supported fields are `holdings`, `cash`, `risk_limits`, `horizon`, `constraints`, `existing_exposure`, and `objective`.

Supported ordinary public-equity paths include US common equities, US share classes, ADRs / foreign-issuer US listings, and direct non-US listings when public sources are sufficient. Supported non-equity validated smoke paths include ETF/fund examples such as SPY, fixed-income examples such as TLT, crypto examples such as BTC, commodity exposure examples such as GLD/gold, and comparison examples such as MSFT vs SPY vs BTC. ADRs are explicitly flagged with underlying issuer / country / currency / reporting / liquidity / regulatory risk notes. Private companies such as OpenAI, SpaceX, or Stripe and complex instruments such as preferred shares, options, warrants, rights, units, and complex OTC-like inputs do not pass as ordinary equity.

TASK-013 writes the reader-facing report outside both repositories under:

```text
C:\Users\ShumeikoYe\OneDrive\Documents\Financial Agent Reports\[TICKER] yyyy-mm-dd hhmm\investment_report.md
```

The same folder contains `audit/` with resolver result, source candidates, provider results, source preflight, source inventory, `portfolio_context.json`, evidence pack, specialist raw outputs, normalized handoffs, validation files, and run manifest. The reader-facing report is a clean investment memo with an Evidence Status Summary and key limitations, while technical runtime details remain in audit. Mock mode is deterministic for tests and does not count as production real-subagent execution. Live mode uses public/no-key source preflight and separate Codex SDK specialist runs where available.

Optional: choose a Codex model for live `route-check` or live `quick-run`:

```powershell
$env:FA_AUTOMATION_CODEX_MODEL='gpt-5.5'
..\.venv\Scripts\python.exe fa_automation.py route-check --mode live
```

Optional: increase the live per-case timeout for slower SDK runs in `route-check` or `quick-run`:

```powershell
$env:FA_AUTOMATION_LIVE_TIMEOUT_SECONDS='120'
..\.venv\Scripts\python.exe fa_automation.py route-check --mode live
```

Run tests:

```powershell
..\.venv\Scripts\python.exe -m unittest discover -s tests
```

## Run logs

Route-check logs are JSON files stored under:

```text
runs/route-check/
```

QUICK launch logs are JSON files stored under:

```text
runs/quick/
```

Live logs preserve the TASK-001 shape and may add per-case fields such as `reason`, `attempts`, `mismatch`, `error`, and `diagnostic_hint`.

Successful QUICK logs include `validation.quality_checks` so structure, freshness, no-report, no-audit, no-IC, no-final-action, no-sizing, and no-subagent checks are visible.

QUICK answer logs are also stored under:

```text
runs/quick/
```

They point to the corresponding `data_runs/quick/[timestamp]-ASSET/` snapshot folder and record the validator result plus output-quality status.

AGENT design logs are JSON files stored under:

```text
runs/agent-design/
```

Successful AGENT design logs include the selected route, exactly five intake questions, planned subagents, an empty `actual_subagents_run` list, required gate coverage, and the future report/audit boundary under `C:\Users\ShumeikoYe\OneDrive\Documents\Financial Agent Reports\[ASSET] yyyy-mm-dd hhmm\`.

## Safety boundaries

For `route-check`, `quick-run`, and `agent-design`, live mode must:

- run Codex from the Financial Agent System root;
- classify only the route for `route-check`;
- ask only the required three QUICK intake questions for `quick-run`;
- use read-only sandbox and deny-all approval mode;
- not perform investment analysis;
- not create investment reports;
- not modify route cards, agents, skills, or validators;
- not issue final IC Action;
- not store raw full Codex responses for route classification;
- store only the guarded QUICK first-step output for `quick-run`, after the lightweight Preliminary/Limited and three-question validation passes.
- reject freshness-dependent QUICK output unless it remains Limited and asks about current/timestamped source needs.
- reject weak QUICK answers through `output_quality.json` when source notes, freshness notes, risk specificity, action-language, or overconfidence checks fail.
- keep `agent-design` design-only; it may plan relevant subagents and gates, but it must not claim subagents executed or create future AGENT report/audit artifacts.

For TASK-013/TASK-014 `agent-run --mode live`, live mode is different by design: it may run the full supported AGENT workflow for resolved supported assets/comparisons, create `investment_report.md` and `audit/` outside the repositories, and execute real Codex SDK specialist runs after the source preflight hard gate passes.

## Notes

- `.gitignore` excludes local environments, caches, run logs, and generated quick data snapshots.
- Before any commit, verify `.venv/`, `runs/`, `data_runs/`, and `__pycache__/` are not staged.
