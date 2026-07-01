# valuation_expectations.md - QQQ vs SCHG for long-term U.S. growth exposure

## Handoff metadata
- Artifact: `valuation_expectations.md`
- Subject: QQQ vs SCHG for long-term U.S. growth exposure
- Owner: Valuation & Expectations Agent
- Producing agent/skill/workflow: Valuation & Expectations Agent / smoke-test handoff
- Workflow: ETF internal full workflow smoke test
- Execution mode: Agent workflow with spawned subagents
- As-of date/time: 2026-06-30
- Output status: Limited
- Evidence status: Limited; valuation uses proxy ETF and growth-equity metrics
- Freshness status: Current for cited public ETF data; Limited for forward fundamentals
- Source scope: Public sources only
- Evidence limits: No full holdings-level model, no consensus bridge, no risk/portfolio/IC gates
- Key limitations: No full holdings-level model, no consensus bridge, no risk/portfolio/IC gates
- Missing gates: ETF overlap; risk stress; portfolio fit; IC synthesis
- Decision boundary: Boundary: Not an IC Action
- Downstream handoff: To Risk, Portfolio Fit, and IC as expectations input
- Required follow-up: Build holdings-level valuation and scenario bridge before final memo

## Expectations bridge

Both QQQ and SCHG depend on strong U.S. large-cap growth earnings, especially AI/platform/semiconductor leaders. SCHG's lower fee and broader holdings help vehicle economics, but do not remove elevated growth valuation risk. QQQ has higher sensitivity to Nasdaq-100 leadership and AI/semiconductor concentration.

## What must be true

- Mega-cap growth earnings keep compounding.
- AI capex turns into durable cash-flow support.
- Real rates and equity risk premium do not force a major multiple reset.
- Leadership does not rotate sharply away from growth.


## Structured handoff
- Artifact: `valuation_expectations.md`
- Subject: QQQ vs SCHG for long-term U.S. growth exposure
- Scope: ETF/growth-exposure valuation expectations
- Owner: Valuation & Expectations Agent
- Producing agent/skill/workflow: Valuation & Expectations Agent / smoke-test handoff
- Workflow: ETF internal full workflow smoke test
- Execution mode: Agent workflow with spawned subagents
- As-of date/time: 2026-06-30
- Output status: Limited
- Evidence status: Limited; valuation uses proxy ETF and growth-equity metrics
- Freshness status: Current for cited public ETF data; Limited for forward fundamentals
- Source scope: Public sources only
- Evidence limits: No full holdings-level model, no consensus bridge, no risk/portfolio/IC gates
- Key limitations: No full holdings-level model, no consensus bridge, no risk/portfolio/IC gates
- Key findings: Both vehicles require durable mega-cap EPS growth; QQQ has higher concentrated AI/Nasdaq beta; SCHG is broader but not cheap
- Missing gates: ETF overlap; risk stress; portfolio fit; IC synthesis
- Decision boundary: Boundary: Not an IC Action
- Decision constraints: No final buy/sell/hold/add/trim/exit; no exact allocation or trade instruction.
- Downstream handoff: To Risk, Portfolio Fit, and IC as expectations input
- Required follow-up: Build holdings-level valuation and scenario bridge before final memo
