# risk_red_team.md - QQQ vs SCHG for long-term U.S. growth exposure

## Handoff metadata
- Artifact: `risk_red_team.md`
- Subject: QQQ vs SCHG for long-term U.S. growth exposure
- Owner: Risk / Red Team Agent
- Producing agent/skill/workflow: Risk / Red Team Agent / smoke-test handoff
- Workflow: ETF internal full workflow smoke test
- Execution mode: Agent workflow with spawned subagents
- As-of date/time: 2026-06-30
- Output status: Limited
- Evidence status: Limited public-data risk review; no full evidence pack or portfolio context
- Freshness status: Current for checked ETF metrics; incomplete for flows and positioning
- Source scope: Public sources only
- Evidence limits: No full stress test, no portfolio context, no complete flow/crowding dataset
- Key limitations: No full stress test, no portfolio context, no complete flow/crowding dataset
- Missing gates: ETF analysis completion; valuation stress; portfolio overlap; macro and positioning refresh
- Decision boundary: Boundary: Not an IC Action
- Downstream handoff: To Portfolio Fit and IC as risk-gate input
- Required follow-up: Run drawdown, concentration, rate, and overlap stress before final IC memo

## Risk gate summary

Risk gate is Limited. The wrapper/liquidity case does not fail, but positive IC use is not supported until concentration, AI expectations, drawdown tolerance, rate sensitivity, and portfolio overlap are bounded.

## Main risks

- Shared mega-cap growth and AI/semiconductor concentration.
- Growth-factor and rate-sensitivity reversal.
- Crowded positioning in mega-cap technology.
- Large historical drawdown potential in Nasdaq/growth exposures.
- Portfolio duplication with S&P 500, technology, semiconductor, or employer-stock exposure.


## Structured handoff
- Artifact: `risk_red_team.md`
- Subject: QQQ vs SCHG for long-term U.S. growth exposure
- Scope: Risk challenge for ETF comparison
- Owner: Risk / Red Team Agent
- Producing agent/skill/workflow: Risk / Red Team Agent / smoke-test handoff
- Workflow: ETF internal full workflow smoke test
- Execution mode: Agent workflow with spawned subagents
- As-of date/time: 2026-06-30
- Output status: Limited
- Evidence status: Limited public-data risk review; no full evidence pack or portfolio context
- Freshness status: Current for checked ETF metrics; incomplete for flows and positioning
- Source scope: Public sources only
- Evidence limits: No full stress test, no portfolio context, no complete flow/crowding dataset
- Key limitations: No full stress test, no portfolio context, no complete flow/crowding dataset
- Key findings: Dominant risks are mega-cap concentration, AI disappointment, rate sensitivity, drawdown, and crowding
- Missing gates: ETF analysis completion; valuation stress; portfolio overlap; macro and positioning refresh
- Decision boundary: Boundary: Not an IC Action
- Decision constraints: No final buy/sell/hold/add/trim/exit; no exact allocation or trade instruction.
- Downstream handoff: To Portfolio Fit and IC as risk-gate input
- Required follow-up: Run drawdown, concentration, rate, and overlap stress before final IC memo
