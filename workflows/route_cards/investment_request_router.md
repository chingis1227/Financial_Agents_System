# Investment Request Router Route Card

Status: Runtime route card
Authority: Subordinate to canonical implementation documents and `PROJECT_STATE.md`.

## Trigger

Use before answering any `AGENT:`, `QUICK:`, specialist-command, or ordinary investment request that asks whether to buy, invest, hold, sell, add, compare, evaluate, rank, or analyze an asset for a portfolio or capital-allocation decision.

## Required first action

Classify command and intent before analysis:

| Command / intent | Route |
|---|---|
| `QUICK:` or explicit short / quick / fast / preliminary | `quick_take.md` |
| `AGENT:` plus concrete equity or public company action request | `equity_full_cycle.md` |
| `AGENT:` plus ETF/fund wrapper or ETF comparison | `etf_full_cycle.md` or `multi_asset_comparison.md` |
| `AGENT:` plus commodity or commodity-linked exposure | `commodity_full_cycle.md` |
| `AGENT:` plus crypto asset or crypto-linked exposure | `crypto_full_cycle.md` |
| `AGENT:` plus bond, bond ETF, yield, duration, credit, or rates exposure | `fixed_income_full_cycle.md` |
| `AGENT:` plus cross-asset comparison | `multi_asset_comparison.md` |
| Specialist command | `direct_specialist.md` |
| Ordinary concrete-asset investment-action or horizon-analysis request | Mandatory auto-dispatch to the appropriate asset/comparison route; `AGENT:` is a shortcut, not a prerequisite |

Automation Lab CLI auto-dispatch is a thin runtime wrapper over this table:

```powershell
automation_lab/fa_automation.py dispatch --prompt "<user request>"
```

It may add the appropriate internal `AGENT:`, `QUICK:`, or specialist prefix before calling the existing flow, but it must not add new investment rules or bypass the route-card and canonical-document boundaries.

## Ordinary request auto-dispatch contract

Any user prompt about an investment decision, buy, sell, hold, add, trim, exit, asset comparison, or analysis of a concrete asset for a time horizon must first record a routing decision through this router. Do not provide ordinary chat-only investment analysis before that decision.

Known equity identity normalization includes:

| User wording | Canonical identity | Route |
|---|---|---|
| `Fabrinet`, `Fabrynet`, `Fabryns`, `FN` | `Fabrinet` / `FN` | `equity_full_cycle.md` |

Numeric horizon ranges such as `3-5 years` / `3–5 лет` are horizon context, not ticker candidates.

## Specialist command mapping

| Prefix | Target agent |
|---|---|
| `RISK:` | `risk-red-team-agent` |
| `VAL:` | `valuation-expectations-agent` |
| `MACRO:` | `macro-agent` |
| `NEWS:` | `news-catalysts-agent` |
| `PORTFOLIO:` | `portfolio-fit-agent` |
| `SECTOR:` | `sector-industry-analysis-agent` |
| `EVIDENCE:` | `evidence-collector` |
| `POSITIONING:` | `market-positioning-agent` |
| `SENSE:` | `market-sense-agent` |
| `INTEL:` | `market-intelligence-agent` |
| `EQUITY:` | `equity-agent` |
| `ETF:` | `etf-agent` |
| `COMMODITY:` | `commodity-agent` |
| `CRYPTO:` | `crypto-agent` |
| `FI:` | `fixed-income-agent` |
| `WINNERS:` | `structural-winners-discovery-agent` |
| `IC:` | `investment-committee-agent` |

## Required questions

- `AGENT:` route: ask exactly 5 relevant questions in one block, then wait.
- `QUICK:` route: ask exactly 3 relevant questions in one block, then wait.
- Specialist command: confirm scope only if ambiguous; otherwise route directly to the mapped analyst.
- If asset identity, ticker, instrument, currency, maturity, or structure is ambiguous, count the clarification inside the required 5-question `AGENT:` block or 3-question `QUICK:` block wherever possible. Ask a separate blocking clarification only when the request is truly unroutable, such as an unresolved ticker/share-class/instrument conflict that prevents route selection.

## Forbidden output

- Do not answer a concrete-asset investment-action request as `QUICK:` unless the user explicitly asked for short / quick / fast / preliminary output.
- Do not issue final `IC Action` before IC gates pass.
- Do not claim agent workflow execution unless subagents were actually spawned.
- Do not present fallback execution as a user-selectable mode; keep fallback as audit metadata only.

## Downgrade rules

If required spawned subagents, evidence, freshness, valuation, risk, or portfolio gates are missing, use a gate-aware Limited / Blocked output or a non-final artifact route.

## Validation expectations

Golden prompts for `AGENT:`, `QUICK:`, every specialist command, Microsoft, Fabrinet/Fabrynet/Fabryns/FN, BTC, QQQ vs SCHG, gold, TLT, freshness, direct risk, unknown-asset clarification, `3-5` horizon parsing, and premature final memo must map to expected routes and target agents in `tests/behavior/golden_prompts.yaml` and runtime tests.


## Decision Mode / Horizon Gate

Every `AGENT:` workflow classifies one decision mode before modules run: Tactical setup, Medium-term thesis, Long-term ownership, Portfolio role, Discovery / opportunities, or Market reaction. The mode changes which optional modules are material.

## Materiality Gate

Before optional market modules run, record Include / Skip with a reason for News & Catalysts, Market Positioning, Market Intelligence, Market Sense / Driver Dominance, and Structural Winners. News is included for earnings, guidance, regulation, M&A, recent events, latest/today/now. Positioning is included for flows, crowding, sentiment, futures/ETF positioning, or event-bar questions. Market Sense is included for why-moved, price-action, market-reaction, and driver-dominance prompts. Structural Winners is included only for discovery / opportunities / theme-candidate work. Skipped optional agents must be recorded with reasons.

## Thesis Spine

Every large workflow creates and updates one Thesis Spine: core thesis; top 3 value drivers; top 3 risk drivers; what must be true; what would change the view; time horizon; key decision variable; current Asset / business quality, Valuation support, Entry setup, and Portfolio role status. Each included module states how it changes or confirms the Thesis Spine.
