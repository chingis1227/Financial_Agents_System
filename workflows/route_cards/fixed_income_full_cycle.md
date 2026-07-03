# Fixed Income AGENT Workflow Route Card

Status: Runtime route card
Authority: Subordinate to `workflows/fixed_income_full_cycle.md` and canonical implementation documents.

## Trigger

Use for bonds, bond ETFs, Treasury duration, credit exposure, spreads, yield, carry, maturity, currency, or fixed-income portfolio role.

## Required first action

Ask exactly 5 fixed-income questions in one block and wait. Resolve instrument, wrapper, maturity, currency, and credit/rates exposure if ambiguous.

## Required modules

- evidence collection and freshness check
- fixed-income analysis
- ETF/wrapper analysis when the vehicle is a fund
- macro/rates context
- valuation / expectations equivalent
- risk / red-team review
- portfolio fit / duration/credit role
- positioning/news/market sense when material
- IC synthesis

## Allowed output

Saved `investment_report.md` plus `audit/`, or gate-aware Limited / Blocked artifact.

## Forbidden output

No final yield/duration/credit action without instrument identity, freshness, structure, liquidity, risk, and portfolio gates.

## Downgrade rules

If instrument terms or rate/credit data are stale or ambiguous, use Limited / Blocked.

## Validation expectations

TLT prompt must route to fixed-income / bond ETF AGENT workflow and require 5 questions.

## Core vs materiality-triggered modules

Core modules: Evidence, asset-class lead, Macro where relevant, Valuation / expectations equivalent, Risk, Portfolio Fit, and IC synthesis. Equity also includes Sector / Industry and Financial Statement Analysis when decision-relevant. Fixed Income includes ETF agent when wrapper/fund structure matters. Multi-asset comparison includes relevant asset-class leads and scenario comparison synthesis.

Materiality-triggered modules: News & Catalysts, Market Positioning, Market Sense / Driver Dominance, Market Intelligence, and Structural Winners. Record Include / Skip plus reason under the Materiality Gate. Long-term ownership prompts usually skip News / Positioning / Market Sense unless material; tactical today/latest/entry/price-action prompts usually include them.

Every large workflow must maintain a Thesis Spine, separate Quality vs Entry, record Portfolio Fit Level 0-4, and require IC Conflict Resolution with Key Internal Conflicts, What Would Change Our Mind, and Monitoring Triggers.
