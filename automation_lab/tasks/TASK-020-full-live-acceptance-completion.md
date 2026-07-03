# TASK-020 - Full live acceptance completion

## Goal

Complete the supported production-like live runtime matrix for Financial Agent Automation Lab without pretending mock or partial runs are live.

## Value

The system now has real `sdk_thread_id` evidence for QUICK live/public validation, full AGENT live packages across the supported route matrix, and every direct specialist prefix.

## Scope

- Run live AGENT packages for:
  - equity: MSFT;
  - ETF/fund: SPY;
  - fixed income: TLT;
  - crypto: BTC;
  - commodity: GLD;
  - multi-asset comparison: MSFT vs SPY vs BTC.
- Validate each latest package with `validate-agent-run`.
- Run every direct specialist prefix in live mode and validate each package.
- Confirm `live-acceptance --require-live` passes with no smoke, live, or usage-limit gaps.

## Out of scope

- No hidden API-key data providers.
- No claim that future source/freshness failures cannot happen.
- No personal final action or exact sizing outside gated IC conditions.

## Evidence

Latest complete live route examples are saved under `C:\Users\ShumeikoYe\OneDrive\Documents\Financial Agent Reports\`:

- `MSFT 2026-07-03 0054\investment_report.md`
- `SPY 2026-07-03 0102\investment_report.md`
- `TLT 2026-07-03 0936\investment_report.md`
- `BTC 2026-07-03 0916\investment_report.md`
- `GLD 2026-07-03 0922\investment_report.md`
- `MSFT-SPY-BTC 2026-07-03 0929\investment_report.md`

Latest acceptance evidence:

- `live-acceptance --require-live`: pass
- smoke gaps: none
- live gaps: none
- usage-limit gaps: none

## Definition of Done

- All route examples validate.
- All direct specialist prefixes have live `sdk_thread_id` evidence.
- `live-acceptance --require-live` passes.
- README and ROADMAP are synchronized.
