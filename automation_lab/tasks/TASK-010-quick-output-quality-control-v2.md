# TASK-010 - QUICK output quality control v2

## Goal

Strengthen `quick-answer` so each generated Quick Take is not only structurally valid, but also safe, honest about source/freshness limits, and specific enough for a preliminary QUICK filter.

## Value

TASK-010 reduces the risk that QUICK sounds like a final investment recommendation, hides weak data, uses generic risk language, or overstates confidence before the full AGENT / Evidence Collector / IC workflow exists.

## Dependencies

- TASK-007 `quick-answer` public-data snapshot flow.
- TASK-008 QUICK pilot assets and comparison.
- TASK-009 QUICK provider registry and data-quality metadata.
- Financial Agent System remains the source of truth for investment boundaries.

## Scope

- Add deterministic output-quality checks in `quick_data/output_quality.py`.
- Add `output_quality.json` to every quick-answer run.
- Add `Source note` and `Freshness note` to the Quick Take template.
- Extend `validate-quick-answer` to validate output quality.
- Detect hidden action language, overconfidence, generic risk, missing source notes, and missing freshness notes.
- Keep `Preliminary` only for complete, non-freshness-dependent quick snapshots.
- Update tests, README, ROADMAP, and this task document.

## Out of scope

- No AI/LLM judge.
- No API provider enablement.
- No Evidence Collector execution.
- No `evidence_pack.md`.
- No AGENT execution.
- No final IC Action.
- No `investment_report.md`.
- No `audit/` folder.
- No changes to the main Financial Agent System unless a direct rule conflict is found.

## Implementation plan

1. Create `quick_data/output_quality.py` with deterministic rule-based checks.
2. Generate an `output_quality.json` card for every `quick-answer` run.
3. Add `Source note` and `Freshness note` sections to generated Quick Takes.
4. Extend `quick_answer.json` with `output_quality_path` and `output_quality_result`.
5. Extend `validate-quick-answer` to require and validate `output_quality.json`.
6. Treat hard violations as command failures.
7. Save soft quality failures but do not print weak Quick Takes as normal successful output.
8. Add tests for file creation, sections, status correctness, risk specificity, hidden action language, overconfidence, validator behavior, and artifact boundaries.
9. Synchronize README and ROADMAP.

## Test plan

- Run all unit tests:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests
```

- Smoke `quick-run` mock.
- Smoke `quick-answer` mock for MSFT, SPY, BTC, TLT, GLD, and MSFT-SPY-BTC.
- Smoke `validate-quick-answer` on a generated run.
- Smoke live/public MSFT with current-data answer and verify no API keys are required.

## Docs synchronization note

README documents `output_quality.json`, new Quick Take notes, quality-fail behavior, and unchanged QUICK safety boundaries. ROADMAP marks TASK-010 complete and keeps TASK-011 AGENT equity/MSFT pilot as the next gated step.

## Review checklist

- [ ] `quick_data/output_quality.py` exists.
- [ ] `output_quality.json` is written.
- [ ] Quick Take includes `Source note`.
- [ ] Quick Take includes `Freshness note`.
- [ ] `validate-quick-answer` requires output quality.
- [ ] Hidden action phrases are rejected.
- [ ] Overconfidence is detected.
- [ ] Generic mock risks fail output quality.
- [ ] Live mode accepts asset-class-specific risk.
- [ ] Soft quality failures are saved but not printed as normal Quick Takes.
- [ ] Hard violations fail.
- [ ] No report/audit artifacts are created.
- [ ] README and ROADMAP are synchronized.
- [ ] Main Financial Agent System remains unchanged.
- [ ] `.venv/`, `runs/`, `data_runs/`, and caches are not staged.

## Definition of Done

TASK-010 is done when all unit tests pass, mock and live smoke checks work, output-quality files and validator checks are in place, QUICK remains free of final action language and exact sizing, report/audit artifacts are not created, docs are synchronized, and review sub-agent score is at least 9.0/10 after agreed fixes.
