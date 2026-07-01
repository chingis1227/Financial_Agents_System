# portfolio_fit.md - QQQ vs SCHG for long-term U.S. growth exposure

## Handoff metadata
- Artifact: `portfolio_fit.md`
- Subject: QQQ vs SCHG for long-term U.S. growth exposure
- Owner: Portfolio Fit Agent
- Producing agent/skill/workflow: Portfolio Fit Agent / smoke-test handoff
- Workflow: ETF internal full workflow smoke test
- Execution mode: Agent workflow with spawned subagents
- As-of date/time: 2026-06-30
- Output status: Limited
- Evidence status: Limited; no user portfolio data and no personalized holdings analysis
- Freshness status: Current for public ETF profile; no user data
- Source scope: Public sources only
- Evidence limits: No current holdings, objective, risk tolerance, account type, tax status, or constraints
- Key limitations: No current holdings, objective, risk tolerance, account type, tax status, or constraints
- Missing gates: User portfolio context; risk tolerance; objective; horizon; tax/account constraints
- Decision boundary: Boundary: Not an IC Action
- Downstream handoff: To IC as Limited portfolio-role input
- Required follow-up: Collect portfolio exposure buckets and objective before personalized fit

## Portfolio fit summary

QQQ and SCHG largely occupy the same portfolio role: U.S. large-cap growth / mega-cap growth tilt. QQQ is the narrower Nasdaq-100 expression; SCHG is broader and lower-cost. Neither should be treated as diversification away from U.S. mega-cap growth.

## Missing personal inputs

Current holdings, existing U.S. equity/growth/tech exposure, risk tolerance, objective, account type, tax constraints, and concentration limits are missing.


## Structured handoff
- Artifact: `portfolio_fit.md`
- Subject: QQQ vs SCHG for long-term U.S. growth exposure
- Scope: Generic portfolio role and overlap framing
- Owner: Portfolio Fit Agent
- Producing agent/skill/workflow: Portfolio Fit Agent / smoke-test handoff
- Workflow: ETF internal full workflow smoke test
- Execution mode: Agent workflow with spawned subagents
- As-of date/time: 2026-06-30
- Output status: Limited
- Evidence status: Limited; no user portfolio data and no personalized holdings analysis
- Freshness status: Current for public ETF profile; no user data
- Source scope: Public sources only
- Evidence limits: No current holdings, objective, risk tolerance, account type, tax status, or constraints
- Key limitations: No current holdings, objective, risk tolerance, account type, tax status, or constraints
- Key findings: QQQ and SCHG are overlapping U.S. large-cap growth sleeves; combining them likely increases concentration more than diversification
- Missing gates: User portfolio context; risk tolerance; objective; horizon; tax/account constraints
- Decision boundary: Boundary: Not an IC Action
- Decision constraints: No final buy/sell/hold/add/trim/exit; no exact allocation or trade instruction.
- Downstream handoff: To IC as Limited portfolio-role input
- Required follow-up: Collect portfolio exposure buckets and objective before personalized fit
