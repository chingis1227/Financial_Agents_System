# TASK-009 - QUICK provider registry v1

## Goal

Create a dedicated QUICK data layer with a provider registry, source-quality metadata, freshness handling, fallback behavior, provider-error capture, and disabled future API-provider slots while preserving the existing `quick-answer` CLI and snapshot compatibility.

## Value

TASK-009 makes QUICK data collection more reliable and easier to extend without turning QUICK into the full Evidence Collector workflow. It gives each public source an explicit contract, records provider failures in JSON snapshots, and prepares clean future integration points for API providers.

## Accepted decisions

- TASK-009 is a foundation for future providers, not a production data layer.
- QUICK data logic moves from `fa_automation.py` into `quick_data/`.
- `fa_automation.py` remains the CLI and orchestration layer.
- CLI UX stays unchanged.
- Existing snapshot fields remain compatible.
- New provider fields are additive.
- API providers are disabled slots only; no API keys are required or used.
- Provider errors are written to snapshot JSON, not dumped into user-facing stdout.
- Freshness is assessed by component type.
- Provider fallback follows registry priority.
- Source quality levels are `official`, `public_market`, `static_context`, `mock`, `disabled_api`, and `failed`.
- TASK-009 does not change the main Financial Agent System repository.

## Relationship to Evidence Collector

TASK-009 does not replace Evidence Collector. QUICK snapshots are pre-evidence / public-data snapshots for a short Quick Take. Evidence Collector remains the owner of `evidence_pack.md`, full source-readiness control, and pre-IC evidence lock in the full AGENT workflow.

The QUICK provider registry aligns with Evidence Collector concepts by labeling source scope, quality, freshness, missing data, and provider errors, so future AGENT/Evidence Collector workflows can use or re-check these snapshots.

## Dependencies

- TASK-007 `quick-answer` public-data snapshot flow.
- TASK-008 multi-asset QUICK pilot set.
- Financial Agent System evidence and QUICK boundaries remain the source of truth.

## Scope

- Add `quick_data/` package.
- Move QUICK identity, provider, registry, snapshot, and quality logic into that package.
- Register current mock, static, SEC, Stooq, and Yahoo public providers.
- Register disabled API slots for Alpha Vantage, Financial Modeling Prep, and Nasdaq Data Link.
- Preserve `source_snapshot.json`, `data_quality.json`, and `quick_answer.json` compatibility.
- Extend validator and tests for provider metadata and errors.
- Update README and ROADMAP.

## Out of scope

- No new supported assets.
- No arbitrary comparisons.
- No paid/authenticated API provider integration.
- No Evidence Collector execution.
- No `evidence_pack.md`.
- No `investment_report.md`.
- No `audit/` folder.
- No final IC Action or buy/sell/hold/add/trim/exit language.
- No main Financial Agent System changes.

## Implementation plan

1. Add `quick_data/identity.py`, `providers.py`, `registry.py`, `snapshot.py`, `quality.py`, and `__init__.py`.
2. Move current QUICK identity detection and slugs into `identity.py`.
3. Define provider metadata/result contracts in `providers.py`.
4. Add provider registry and disabled API slots in `registry.py`.
5. Move mock/live snapshot creation into `snapshot.py`.
6. Move freshness and status logic into `quality.py`.
7. Keep `fa_automation.py` as CLI plus answer rendering/validation.
8. Add additive snapshot fields: `schema_version`, `providers`, `provider_results`, `provider_errors`, `source_scope`, and `evidence_alignment`.
9. Add provider/freshness summaries to `data_quality.json`.
10. Extend validator and tests.

## Test plan

- Run all unit tests with `./.venv/Scripts/python.exe -m unittest discover -s tests`.
- Verify registry contains public providers.
- Verify disabled API slots are present but not executed.
- Verify provider priority fallback order.
- Verify provider errors appear in snapshot.
- Verify stale or missing price downgrades to Limited.
- Verify missing identity remains Blocked.
- Verify old snapshot fields remain present.
- Verify new provider fields are present.
- Verify CLI UX remains unchanged.
- Verify no report/audit artifacts are created.
- Run mock smoke scenarios for MSFT and MSFT-SPY-BTC.
- Run live/public smoke without API keys.

## Docs synchronization note

README documents the provider registry, unchanged CLI, public/no-key behavior, disabled API slots, provider errors in snapshots, and the Evidence Collector boundary. ROADMAP marks TASK-009 complete and identifies TASK-010 as the next quality-control step.

## Review checklist

- [ ] `quick_data/` exists.
- [ ] `quick-answer` still works.
- [ ] `quick-run` still works.
- [ ] CLI UX is unchanged.
- [ ] Provider registry exists.
- [ ] Public providers are registered.
- [ ] Disabled API slots exist and do not require keys.
- [ ] Provider errors are saved to snapshot JSON.
- [ ] Freshness is component-aware.
- [ ] Existing snapshot fields remain.
- [ ] New provider fields are present.
- [ ] Validator passes.
- [ ] Unit tests pass.
- [ ] README and ROADMAP are synchronized.
- [ ] Main Financial Agent System is unchanged.
- [ ] `.venv/`, `runs/`, `data_runs/`, and caches are not staged.

## Definition of Done

TASK-009 is done when all tests pass, QUICK mock and live smoke checks work without API keys, provider registry metadata and provider results are saved in snapshots, validator checks the new fields, docs are synchronized, no final action/report/audit boundaries are violated, and review sub-agent score is at least 9.0/10 after agreed fixes.
