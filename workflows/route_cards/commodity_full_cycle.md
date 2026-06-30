# Commodity Full Cycle Route Card

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

Gold latest/setup prompt must require freshness treatment and route to commodity Full Cycle unless explicitly Quick Take.
