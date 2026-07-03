# ETF AGENT Workflow Route Card

Status: Runtime route card
Authority: Subordinate to `workflows/etf_full_cycle.md` and canonical implementation documents.

## Trigger

Use for ETF/fund wrapper decisions, ETF comparisons, exposure quality, holdings, methodology, fees, liquidity, tracking, overlap, or wrapper implementation quality.

## Required first action

Ask exactly 5 ETF/fund questions in one block and wait.

## Required modules

- evidence collection and freshness check
- ETF / wrapper analysis
- underlying exposure valuation / expectations
- macro context
- sector context when exposure makes it material
- risk / red-team review
- portfolio fit / overlap review
- market positioning / news / market sense when material
- IC synthesis

## Allowed output

Saved `investment_report.md` plus `audit/`, usually `decision_prep_memo.md` when portfolio context is missing.

## Forbidden output

No final IC Action before wrapper, evidence, risk, valuation-equivalent, and portfolio gates are closed.

## Downgrade rules

If the ETF identity, share class, currency, leverage, inverse mechanics, or holdings are ambiguous, ask before decision-critical analysis.

## Validation expectations

QQQ vs SCHG prompt must map to ETF / multi-asset comparison and preserve no-final-action boundary unless gates pass.

## Core vs materiality-triggered modules

Core modules: Evidence, asset-class lead, Macro where relevant, Valuation / expectations equivalent, Risk, Portfolio Fit, and IC synthesis. Equity also includes Sector / Industry and Financial Statement Analysis when decision-relevant. Fixed Income includes ETF agent when wrapper/fund structure matters. Multi-asset comparison includes relevant asset-class leads and scenario comparison synthesis.

Materiality-triggered modules: News & Catalysts, Market Positioning, Market Sense / Driver Dominance, Market Intelligence, and Structural Winners. Record Include / Skip plus reason under the Materiality Gate. Long-term ownership prompts usually skip News / Positioning / Market Sense unless material; tactical today/latest/entry/price-action prompts usually include them.

Every large workflow must maintain a Thesis Spine, separate Quality vs Entry, record Portfolio Fit Level 0-4, and require IC Conflict Resolution with Key Internal Conflicts, What Would Change Our Mind, and Monitoring Triggers.
