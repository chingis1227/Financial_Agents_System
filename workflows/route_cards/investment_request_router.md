# Investment Request Router Route Card

Status: Runtime route card
Authority: Subordinate to canonical implementation documents and `PROJECT_STATE.md`.

## Trigger

Use before answering any request that asks whether to buy, invest, hold, sell, add, compare, evaluate, rank, or analyze an asset for a portfolio or capital-allocation decision.

## Required first action

Classify intent before analysis:

| Intent | Route |
|---|---|
| Explicit short / quick / fast / preliminary | `quick_take.md` |
| Concrete equity or public company action request | `equity_full_cycle.md` |
| ETF/fund wrapper or ETF comparison | `etf_full_cycle.md` or `multi_asset_comparison.md` |
| Commodity or commodity-linked exposure | `commodity_full_cycle.md` |
| Crypto asset or crypto-linked exposure | `crypto_full_cycle.md` |
| Bond, bond ETF, yield, duration, credit, or rates exposure | `fixed_income_full_cycle.md` |
| Cross-asset comparison | `multi_asset_comparison.md` |
| Direct specialist-only request | `direct_specialist.md` |

## Required questions

- Full Cycle route: ask exactly 5 relevant questions in one block, then wait.
- Quick Take route: ask exactly 3 relevant questions in one block, then wait.
- If asset identity, ticker, instrument, currency, maturity, or structure is ambiguous, resolve that blocking ambiguity before the 5 or 3 questions.

## Forbidden output

- Do not answer a concrete-asset investment-action request as a Quick Take unless the user explicitly asked for short / quick / fast / preliminary output.
- Do not issue final `IC Action` before IC gates pass.
- Do not claim delegated execution unless subagents were actually spawned.

## Downgrade rules

If required evidence, freshness, valuation, risk, or portfolio gates are missing, use a gate-aware Limited / Blocked output or a non-final artifact route.

## Validation expectations

Golden prompts for Microsoft, BTC, QQQ vs SCHG, gold, TLT, freshness, direct risk, and premature final memo must map to the expected route in `tests/behavior/golden_prompts.yaml`.
