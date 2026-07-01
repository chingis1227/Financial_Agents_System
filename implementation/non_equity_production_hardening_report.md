# Non-Equity Production Hardening Report

Date: 2026-06-30  
Scope: ETF, commodity, crypto, fixed income, and multi-asset runtime hardening.  
Status: Operational readiness hardening complete for the requested Level 2 smoke-test scope.  
Final readiness statement: 0 blocking issues after validator pass, subject to the limitations below.

## What was added or changed

- Added runtime workflow runbooks:
  - `workflows/etf_full_cycle.md`
  - `workflows/commodity_full_cycle.md`
  - `workflows/crypto_full_cycle.md`
  - `workflows/fixed_income_full_cycle.md`
  - `workflows/multi_asset_full_agent_workflow.md`
- Extended `workflows/handoff_artifact_standard.md` to cover ETF, Commodity, Crypto, Fixed Income, and Multi-asset artifact sets.
- Added read-only validator: `tools/validate_runtime_readiness.py`.
- Updated `README.md` with Russian user prompts and plain-language explanations for quick take, single-session large workflow, spawned-subagent workflow, and decision-prep memo.
- Created spawned-subagent smoke-test artifact folders for ETF, Commodity, Crypto, and Fixed Income.

## Smoke-test execution summary

| Route | Fixture | Status | Final artifact | Blocking issues |
|---|---|---:|---|---:|
| ETF | QQQ vs SCHG | Pass | `decision_prep_memo.md` | 0 |
| Commodity | Gold | Pass | `decision_prep_memo.md` | 0 |
| Crypto | BTC, 3-year horizon | Pass | `decision_prep_memo.md` | 0 |
| Fixed Income | TLT as bond ETF / long Treasury duration | Pass | `decision_prep_memo.md` | 0 |

## Agents launched by smoke test

### ETF: QQQ vs SCHG

Launched: master-intake-router, asset-intake-router, evidence-collector, etf-agent, valuation-expectations-agent, risk-red-team-agent, portfolio-fit-agent, macro-agent, market-positioning-agent, news-catalysts-agent, market-sense-agent, market-intelligence-agent, sector-industry-analysis-agent, investment-committee-agent.

### Commodity: Gold

Launched: master-intake-router, asset-intake-router, evidence-collector, commodity-agent, macro-agent, market-positioning-agent, valuation-expectations-agent, risk-red-team-agent, portfolio-fit-agent, news-catalysts-agent, market-sense-agent, market-intelligence-agent, investment-committee-agent.

### Crypto: BTC

Launched: master-intake-router, asset-intake-router, evidence-collector, crypto-agent, valuation-expectations-agent, macro-agent, market-positioning-agent, risk-red-team-agent, portfolio-fit-agent, news-catalysts-agent, market-sense-agent, market-intelligence-agent, investment-committee-agent.

### Fixed Income: TLT

Launched: master-intake-router, asset-intake-router, evidence-collector, etf-agent, fixed-income-agent, macro-agent, valuation-expectations-agent, risk-red-team-agent, portfolio-fit-agent, market-positioning-agent, news-catalysts-agent, market-sense-agent, market-intelligence-agent, investment-committee-agent.

## Errors found and fixed

- Some specialist subagents attempted to create root-level artifacts such as `etf_analysis.md`, `fixed_income_analysis.md`, or `market_intelligence_briefing.md`; those were removed from the project root and the canonical smoke-test artifacts were written under `workflows/smoke-tests/...`.
- The C: drive ran out of free space during a subagent close operation. Safe cache cleanup restored working space without deleting project files.
- Some subagent outputs reported their local execution as non-delegated. The parent smoke-test audit records the correct runtime mode as `Agent workflow with spawned subagents` because the parent workflow actually spawned and consumed multiple subagents.

## Validator coverage

`tools/validate_runtime_readiness.py` checks:

- Required workflow files exist and contain execution-mode and artifact-selection language.
- Required custom agents exist and parse as TOML.
- Repo skills have required contract sections.
- Handoff standard covers ETF, Commodity, Crypto, Fixed Income, and Multi-asset routes.
- Smoke-test folders and required artifacts exist.
- Every non-audit artifact has mandatory handoff metadata and structured handoff fields.
- Non-IC artifacts include `Boundary: Not an IC Action`.
- Smoke tests do not force `final_investment_memo.md`.
- Smoke artifacts avoid final buy/sell/hold/add/trim/exit wording patterns.
- README contains Russian examples and plain-language terms.
- This hardening report exists and reports the final status.

## Remaining limitations

- These smoke tests verify runtime routing and artifact discipline; they are not final investment recommendations.
- Final IC output remains blocked without fresh evidence lock, portfolio context, vehicle/custody details where relevant, and completed valuation/risk gates.
- Crypto remains more freshness-sensitive than ETF/fixed income because price, flows, on-chain, custody, and regulation can change quickly.
- Commodity and fixed-income current-market conclusions require updated post-close data before final decision support.
- Multi-asset workflow is now specified as a runtime contract, but a dedicated cross-asset spawned-subagent smoke test was not required in the current implementation plan beyond README and workflow support.

## Final readiness statement

For the requested Level 2 implementation scope, ETF, Commodity, Crypto, and Fixed Income routes are ready to run as spawned-subagent smoke-test workflows that produce `decision_prep_memo.md` by default and preserve IC gates. There are 0 blocking issues for runtime-readiness validation after the validator passes.

## Reviewer hardening updates

After the first reviewer score of 8.2/10, the following fixes were applied:

- README default-mode language was aligned with canonical rules: concrete-asset `AGENT:` workflow should use relevant spawned subagents when available; `Non-delegated audit fallback` is the fallback when subagents are unavailable or not actually spawned.
- Crypto and Fixed Income smoke-test audits were corrected so completed IC agents are no longer recorded as `Pending` while the smoke test is marked `Pass`.
- `run_log.md` provenance files were added to all four smoke-test folders.
- The validator was strengthened to fail unresolved required-agent statuses in passed audits and to require run-log provenance for each smoke test.

Final readiness statement remains: 0 blocking issues after validator pass.

## Second reviewer hardening updates

After the second reviewer score of 9.0/10, the following fixes were applied:

- Non-equity workflow runbooks were aligned with the canonical spawned-subagent workflow default rule.
- Source/provenance tables were added to Gold, BTC, and TLT evidence packs.
- Decision-prep scenario logic and consumed-module synthesis were added to Gold, BTC, and TLT decision memos.
- The validator now checks evidence provenance blocks and decision scenario/synthesis content.
- The older Microsoft smoke folder is explicitly marked out of scope for this non-equity Level 2 validation package.

Final readiness statement remains: 0 blocking issues after validator pass.
