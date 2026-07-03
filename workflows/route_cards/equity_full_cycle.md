# Equity AGENT Workflow Route Card

Status: Runtime route card
Authority: Subordinate to `workflows/equity_full_cycle.md` and canonical implementation documents.

## Trigger

Use for concrete public-equity or company investment-action requests such as buy, invest, hold, sell, add, start exposure, or evaluate for a multi-year horizon.

## Required first action

Ask exactly 5 relevant equity questions in one block and wait. If the user says continue or equivalent, use approved baseline assumptions only.

## Required modules

- request intake and asset identity check
- evidence collection and freshness check
- document evidence parsing for accessible SEC filings, issuer releases, public articles, PDFs, or raw text when supplied/discovered; parsed claims feed the Evidence Pack only
- macro context
- sector / industry context
- equity company analysis
- financial statement analysis when material
- valuation / expectations
- risk / red-team review
- portfolio fit / limited portfolio fit
- IC synthesis

## Allowed output

Saved `investment_report.md` plus `audit/`, or a gate-aware Limited / Blocked artifact if required gates cannot be completed.

## Forbidden output

- No `QUICK:` route unless explicitly requested.
- No final buy/sell/hold/add/trim/exit language outside IC synthesis.
- No agent workflow execution claim unless subagents actually spawned.

## Downgrade rules

Missing portfolio context limits Portfolio Fit and IC Action Status. Missing freshness/evidence can require Evidence Gap Memo or Limited IC Draft.

## Validation expectations

Microsoft investment prompt must map to `equity_full_cycle`, require 5 questions, and forbid Quick Take without explicit request.

## Reader-facing memo cleanup

Equity `investment_report.md` must use clean investment language. Internal `Limited` / `Blocked` statuses, gates, source tiers, source-access/provider failures, handoff metadata, and module-status tables stay in `audit/`. If direct valuation inputs are weak, use proxy valuation from growth, margins, cash flow, balance sheet, dilution, EV/Sales, peer ranges, historical multiples, guidance, or asset-class equivalents; do not stop solely because one direct metric is absent. Small-cap, foreign, and illiquid equities should emphasize disclosure quality, liquidity, balance sheet, cash burn, dilution, governance, survival risk, and scenario range without complaining that the system did not find data.

## Core vs materiality-triggered modules

Core modules: Evidence, asset-class lead, Macro where relevant, Valuation / expectations equivalent, Risk, Portfolio Fit, and IC synthesis. Equity also includes Sector / Industry and Financial Statement Analysis when decision-relevant. Fixed Income includes ETF agent when wrapper/fund structure matters. Multi-asset comparison includes relevant asset-class leads and scenario comparison synthesis.

Materiality-triggered modules: News & Catalysts, Market Positioning, Market Sense / Driver Dominance, Market Intelligence, and Structural Winners. Record Include / Skip plus reason under the Materiality Gate. Long-term ownership prompts usually skip News / Positioning / Market Sense unless material; tactical today/latest/entry/price-action prompts usually include them.

Every large workflow must maintain a Thesis Spine, separate Quality vs Entry, record Portfolio Fit Level 0-4, and require IC Conflict Resolution with Key Internal Conflicts, What Would Change Our Mind, and Monitoring Triggers.
