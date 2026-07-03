# TASK-008 - QUICK answer asset expansion v1

## Goal

Expand `quick-answer` from the TASK-007 MSFT/equity pilot to the agreed QUICK pilot set: SPY, BTC, TLT, GLD, and `MSFT vs SPY vs BTC`.

## Value

QUICK becomes a broader triage layer across major asset classes while preserving the Financial Agent System boundaries: short preliminary output, no final IC Action, no report/audit artifacts, and no exact sizing.

## Decisions

- Keep this as QUICK, not AGENT.
- Keep `quick-run` as the first step with exactly three questions.
- Keep `quick-answer` as the second step consuming prompt plus exactly three answers.
- Historical fixture fixtures are required and stable for tests.
- Live mode is best-effort without API keys and may return Limited when public data is incomplete.
- Do not build a provider registry in TASK-008; defer it to TASK-009.
- Support only the comparison pilot `MSFT vs SPY vs BTC`, not arbitrary comparisons.
- Keep one common Quick Take template with asset-specific content inside the data/risk sections.
- Do not change the main Financial Agent System repository.

## Dependencies

- TASK-007 `quick-answer`, `validate-quick-answer`, snapshot files, and guardrails.
- Financial Agent System remains the source of truth for QUICK rules.

## Scope

- Add identity detection for SPY, BTC/Bitcoin, TLT, GLD/gold ETF, and `MSFT vs SPY vs BTC`.
- Add historical fixture fixtures for new pilots.
- Add live best-effort public-data paths for new pilots.
- Add asset-specific Quick Take context while preserving the common template.
- Extend validator and tests for the new asset types.
- Update README, ROADMAP, and generated-artifact hygiene.

## Out of scope

- Full provider registry.
- Paid or authenticated data providers.
- Full valuation model.
- Full risk-red-team workflow.
- Full AGENT execution.
- Arbitrary multi-asset comparisons.
- Any final buy/sell/hold/add/trim/exit action or exact sizing.

## Implementation plan

1. Extend identity seeds and prompt detection for the five TASK-008 pilots.
2. Add fixture loading support for comparison slugs.
3. Add historical fixture fixtures for SPY, BTC, TLT, GLD, and MSFT-SPY-BTC.
4. Add static quick context for ETF, crypto, bond ETF, commodity ETF, and comparison outputs.
5. Extend live snapshots to use static context plus best-effort public price retrieval.
6. Keep missing public data as Limited/Blocked rather than crashing.
7. Extend Quick Take rendering with asset-specific `What the quick data shows` lines.
8. Extend validation for comparison component identities.
9. Update tests and docs.

## Test plan

- Run all unit tests with `./.venv/Scripts/python.exe -m unittest discover -s tests`.
- Test identity detection for each new pilot.
- Test historical fixture snapshots and generated answer sections for each new pilot.
- Test missing context/price degrades to Limited.
- Test CLI historical fixture scenarios create snapshot folders with expected slugs.
- Validate each generated quick-answer run.
- Run live smoke checks manually for SPY, BTC, TLT, GLD, and MSFT vs SPY vs BTC.

## Docs synchronization note

README documents supported assets, historical fixture vs live behavior, snapshot paths, and QUICK boundaries. ROADMAP records TASK-008 as complete and keeps TASK-009 provider registry as the next data-layer step.

## Review checklist

- [ ] TASK-007 behavior still passes.
- [ ] `quick-run` still works.
- [ ] `quick-answer` works for MSFT, SPY, BTC, TLT, GLD, and MSFT-SPY-BTC.
- [ ] Historical fixture scenarios are stable and tested.
- [ ] Live scenarios require no API keys and do not crash.
- [ ] Missing public data gives Limited or Blocked.
- [ ] No `investment_report.md` or `audit/` is created.
- [ ] No final action language or exact sizing appears.
- [ ] README and ROADMAP are synchronized.
- [ ] Main Financial Agent System is unchanged.
- [ ] `.venv/`, `runs/`, `data_runs/`, and caches are not staged.

## Definition of Done

TASK-008 is done when all tests pass, all five new pilot scenarios generate validated QUICK snapshots in historical fixture path, live smoke checks do not require API keys or crash, docs are updated, generated artifacts are ignored/cleaned, and the main Financial Agent System remains untouched.
