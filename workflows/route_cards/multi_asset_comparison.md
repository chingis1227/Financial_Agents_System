# Multi-Asset AGENT Comparison Route Card

Status: Runtime route card
Authority: Subordinate to `workflows/multi_asset_full_agent_workflow.md` and canonical implementation documents.

## Trigger

Use when the user compares assets across classes, such as BTC vs gold vs QQQ vs TLT, or asks for the best asset without a single asset-class route being sufficient.

## Required first action

Ask exactly 5 comparison questions in one block and wait, unless the user explicitly requests Quick Take.

## Required modules

- evidence collection and source scope
- common role-based criteria
- asset-class-specific analysis for each included asset
- macro context
- valuation / expectations equivalent by asset class
- risk / red-team review
- portfolio fit / limited portfolio fit
- IC synthesis or decision-prep comparison

## Allowed output

Scenario-based comparison, role-based winners, and gate-aware decision-prep output.

## Forbidden output

No universal winner or final allocation without user objective, portfolio context, evidence, risk, valuation, and IC gates.

## Downgrade rules

If criteria are undefined, use default criteria but label the output Limited and scenario-based.

## Validation expectations

QQQ vs SCHG and BTC/gold/QQQ/TLT prompts must route to comparison or ETF route with no premature final action.

## Reader-facing memo cleanup

Comparison reports must not expose runtime labels, gates, source tiers, provider failures, or handoff metadata in `investment_report.md`. Uneven or proxy-heavy evidence is described as lower confidence, scenario range, or dependence on fresh market data. Full technical comparability and source-status records stay in `audit/`.

## Core vs materiality-triggered modules

Core modules: Evidence, asset-class lead, Macro where relevant, Valuation / expectations equivalent, Risk, Portfolio Fit, and IC synthesis. Equity also includes Sector / Industry and Financial Statement Analysis when decision-relevant. Fixed Income includes ETF agent when wrapper/fund structure matters. Multi-asset comparison includes relevant asset-class leads and scenario comparison synthesis.

Materiality-triggered modules: News & Catalysts, Market Positioning, Market Sense / Driver Dominance, Market Intelligence, and Structural Winners. Record Include / Skip plus reason under the Materiality Gate. Long-term ownership prompts usually skip News / Positioning / Market Sense unless material; tactical today/latest/entry/price-action prompts usually include them.

Every large workflow must maintain a Thesis Spine, separate Quality vs Entry, record Portfolio Fit Level 0-4, and require IC Conflict Resolution with Key Internal Conflicts, What Would Change Our Mind, and Monitoring Triggers.
