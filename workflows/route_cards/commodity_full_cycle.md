# Commodity AGENT Workflow Route Card

Status: Runtime route card
Authority: Subordinate to `workflows/commodity_full_cycle.md` and canonical implementation documents.

## Trigger

Use for gold, oil, copper, uranium, agricultural commodities, or commodity-linked exposures when the user asks about investability, attractiveness, hedging role, or capital allocation.

## Required first action

Ask exactly 5 commodity questions in one block and wait.

## Required modules

- evidence collection and freshness check
- commodity analysis
- macro context
- supply/demand and futures curve context when material
- valuation / expectations equivalent
- positioning, news, and market sense when material
- risk / red-team review
- portfolio fit / limited portfolio fit
- IC synthesis

## Allowed output

Saved `investment_report.md` plus `audit/`, or a gate-aware Limited / Blocked artifact.

## Forbidden output

No current setup conclusion without fresh market-sensitive data when the prompt says now/latest/today.

## Downgrade rules

Use Limited / Blocked when price, yields, FX, futures curve, inventory, or event data is stale or unavailable.

## Validation expectations

Gold latest/setup prompt must require freshness treatment and route to commodity AGENT workflow unless the user uses `QUICK:`.

## Core vs materiality-triggered modules

Core modules: Evidence, asset-class lead, Macro where relevant, Valuation / expectations equivalent, Risk, Portfolio Fit, and IC synthesis. Equity also includes Sector / Industry and Financial Statement Analysis when decision-relevant. Fixed Income includes ETF agent when wrapper/fund structure matters. Multi-asset comparison includes relevant asset-class leads and scenario comparison synthesis.

Materiality-triggered modules: News & Catalysts, Market Positioning, Market Sense / Driver Dominance, Market Intelligence, and Structural Winners. Record Include / Skip plus reason under the Materiality Gate. Long-term ownership prompts usually skip News / Positioning / Market Sense unless material; tactical today/latest/entry/price-action prompts usually include them.

Every large workflow must maintain a Thesis Spine, separate Quality vs Entry, record Portfolio Fit Level 0-4, and require IC Conflict Resolution with Key Internal Conflicts, What Would Change Our Mind, and Monitoring Triggers.
