# risk_red_team.md - TLT fixed-income smoke-test artifact

## Handoff metadata
- Artifact: `risk_red_team.md`
- Subject: TLT as bond ETF / long-duration U.S. Treasury exposure smoke test
- Owner: Risk / Red Team Agent
- Producing agent/skill/workflow: Risk / Red Team Agent / smoke-test handoff
- Workflow: Fixed Income Full Cycle smoke-test with ETF wrapper route
- Execution mode: Delegated Full Agent Workflow
- As-of date/time: 2026-06-30
- Output status: Limited
- Evidence status: Limited but usable for smoke-test scope
- Freshness status: Near-current public data
- Source scope: Public sources and delegated smoke-test subagent handoffs only
- Evidence limits: No full evidence pack, no portfolio context, no full valuation scenario.
- Key limitations: Public-source smoke test; no full line-item holdings file; no June 30 closing curve lock; no personalized portfolio context.
- Missing gates: Evidence, valuation, macro, fixed-income/ETF analysis, portfolio fit, IC synthesis
- Decision boundary: Boundary: Not an IC Action
- Downstream handoff: To downstream workflow modules and IC as a Limited smoke-test artifact
- Required follow-up: Build full downside scenarios and portfolio stress test before IC conclusion.

## Module summary

This artifact records the TLT delegated smoke-test module output in the canonical handoff format. It is a runtime readiness artifact, not a final investment recommendation.

## Smoke-test findings

Macro-duration, inflation, term-premium, steepening, tracking/liquidity stress, and hedge-failure risks are material.

## Structured handoff
- Artifact: `risk_red_team.md`
- Subject: TLT as bond ETF / long-duration U.S. Treasury exposure smoke test
- Scope: Duration drawdown, inflation persistence, term premium/fiscal supply, curve steepening, ETF liquidity/tracking, portfolio hedge failure
- Owner: Risk / Red Team Agent
- Producing agent/skill/workflow: Risk / Red Team Agent / smoke-test handoff
- Workflow: Fixed Income Full Cycle smoke-test with ETF wrapper route
- Execution mode: Delegated Full Agent Workflow
- As-of date/time: 2026-06-30
- Output status: Limited
- Evidence status: Limited but usable for smoke-test scope
- Freshness status: Near-current public data
- Source scope: Public sources and delegated smoke-test subagent handoffs only
- Evidence limits: No full evidence pack, no portfolio context, no full valuation scenario.
- Key limitations: Public-source smoke test; no full line-item holdings file; no June 30 closing curve lock; no personalized portfolio context.
- Key findings: Macro-duration, inflation, term-premium, steepening, tracking/liquidity stress, and hedge-failure risks are material.
- Missing gates: Evidence, valuation, macro, fixed-income/ETF analysis, portfolio fit, IC synthesis
- Decision boundary: Boundary: Not an IC Action
- Decision constraints: No final buy/sell/hold/add/trim/exit; no exact allocation, execution, or trade instruction.
- Downstream handoff: To downstream workflow modules and IC as a Limited smoke-test artifact
- Required follow-up: Build full downside scenarios and portfolio stress test before IC conclusion.
