# portfolio_fit.md - TLT fixed-income smoke-test artifact

## Handoff metadata
- Artifact: `portfolio_fit.md`
- Subject: TLT as bond ETF / long-duration U.S. Treasury exposure smoke test
- Owner: Portfolio Fit Agent
- Producing agent/skill/workflow: Portfolio Fit Agent / smoke-test handoff
- Workflow: Fixed Income internal full workflow smoke test with ETF wrapper route
- Execution mode: Agent workflow with spawned subagents
- As-of date/time: 2026-06-30
- Output status: Limited
- Evidence status: Limited official fund data; no portfolio file or IC evidence lock
- Freshness status: Recent official fund characteristics; no full evidence lock
- Source scope: Public sources and spawned-subagent smoke-test handoffs only
- Evidence limits: No user portfolio context; no complete risk/valuation/implementation package.
- Key limitations: Public-source smoke test; no full line-item holdings file; no June 30 closing curve lock; no personalized portfolio context.
- Missing gates: Portfolio context, risk, valuation/expectations, ETF implementation, IC synthesis
- Decision boundary: Boundary: Not an IC Action
- Downstream handoff: To downstream workflow modules and IC as a Limited smoke-test artifact
- Required follow-up: Collect current exposures, objective, horizon, risk tolerance, income need, and account/tax constraints.

## Module summary

This artifact records the TLT spawned-subagent smoke-test module output in the canonical handoff format. It is a runtime readiness artifact, not a final investment recommendation.

## Smoke-test findings

TLT can serve as duration hedge, income, and risk-off exposure; drawdown and equity-correlation behavior are regime-dependent.

## Structured handoff
- Artifact: `portfolio_fit.md`
- Subject: TLT as bond ETF / long-duration U.S. Treasury exposure smoke test
- Scope: Generic portfolio role and personalization gate
- Owner: Portfolio Fit Agent
- Producing agent/skill/workflow: Portfolio Fit Agent / smoke-test handoff
- Workflow: Fixed Income internal full workflow smoke test with ETF wrapper route
- Execution mode: Agent workflow with spawned subagents
- As-of date/time: 2026-06-30
- Output status: Limited
- Evidence status: Limited official fund data; no portfolio file or IC evidence lock
- Freshness status: Recent official fund characteristics; no full evidence lock
- Source scope: Public sources and spawned-subagent smoke-test handoffs only
- Evidence limits: No user portfolio context; no complete risk/valuation/implementation package.
- Key limitations: Public-source smoke test; no full line-item holdings file; no June 30 closing curve lock; no personalized portfolio context.
- Key findings: TLT can serve as duration hedge, income, and risk-off exposure; drawdown and equity-correlation behavior are regime-dependent.
- Missing gates: Portfolio context, risk, valuation/expectations, ETF implementation, IC synthesis
- Decision boundary: Boundary: Not an IC Action
- Decision constraints: No final buy/sell/hold/add/trim/exit; no exact allocation, execution, or trade instruction.
- Downstream handoff: To downstream workflow modules and IC as a Limited smoke-test artifact
- Required follow-up: Collect current exposures, objective, horizon, risk tolerance, income need, and account/tax constraints.
