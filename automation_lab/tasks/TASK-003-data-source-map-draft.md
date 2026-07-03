# TASK-003 — Data Source Map Draft

Status: Complete
Date: 2026-07-01

## Goal

Create the first draft map of likely automatable data sources for future Financial Agent Automation Lab workflows.

## Value

TASK-003 gives the lab a practical inventory of source candidates before building QUICK automation or quality-control checks. It documents what each source can provide, likely freshness, access model, automation suitability, and fallback options.

## Dependencies

- TASK-001 route-check scaffold is complete.
- TASK-002 live Codex SDK route-check is complete.
- Main Financial Agent System remains unchanged and authoritative.

## Scope

Create draft files under:

```text
data_sources/
```

Files created:

- `data_sources/README.md`
- `data_sources/equity.md`
- `data_sources/crypto.md`
- `data_sources/etf.md`
- `data_sources/fixed_income.md`
- `data_sources/commodity.md`
- `data_sources/macro.md`
- `data_sources/news.md`

Each asset-class file includes:

- Source
- What it provides
- Freshness
- Free/paid
- Automatable
- Fallback if unavailable
- Notes

## Out of scope

- No canonical source policy for Financial Agent System.
- No authority ranking.
- No source-quality scoring.
- No credentials or secrets.
- No vendor integration code.
- No automated data pulls.
- No changes to the main Financial Agent System repository.

## Implementation summary

The draft map uses official or direct provider documentation where possible, including SEC EDGAR, FRED, U.S. Treasury Fiscal Data, BLS, BEA, EIA, CFTC, Alpha Vantage, Nasdaq Data Link, Financial Modeling Prep, CoinGecko, Binance, and CoinMarketCap.

The files are intentionally descriptive rather than prescriptive: they identify possible future automation inputs without changing evidence gates or source authority.

## Test plan

Run Automation Lab tests:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests
```

Run historical fixture route check to confirm existing CLI behavior remains intact:

```powershell
.\.venv\Scripts\python.exe fa_automation.py route-check --mode live
```

Manual review:

- Confirm all seven asset-class files exist.
- Confirm each file includes the required fields.
- Confirm no main Financial Agent System files changed.
- Confirm `.venv/` is not staged.

## Docs synchronization note

TASK-003 changes only the Automation Lab. The main Financial Agent System validators are not required unless the main project is modified.

If a future task changes the main project, run its required validators:

```powershell
py -3 tools\validate_project_consistency.py
py -3 tools\validate_behavior_contracts.py
py -3 tools\validate_runtime_readiness.py
```

## Review checklist

- [x] Draft source maps are in Automation Lab only.
- [x] Required seven asset-class files exist.
- [x] Each file covers source, what it provides, freshness, free/paid, automatable, and fallback.
- [x] No authority ranking added.
- [x] No canonical source policy added.
- [x] No secrets or API keys added.
- [x] Main Financial Agent System not modified.

## Definition of Done

TASK-003 is complete when:

- `data_sources/` exists.
- The seven required asset-class files exist.
- Each required file uses the expected source-map fields.
- `data_sources/README.md` states the draft/non-canonical boundary.
- `README.md` and `ROADMAP.md` reflect TASK-003 status.
- Automation Lab tests pass.
- Historical fixture route-check still passes.
- Git status contains only intended Automation Lab changes before commit.
