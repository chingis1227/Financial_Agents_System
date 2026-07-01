# market_sense.md - TLT fixed-income smoke-test artifact

## Handoff metadata
- Artifact: `market_sense.md`
- Subject: TLT as bond ETF / long-duration U.S. Treasury exposure smoke test
- Owner: Market Sense Agent
- Producing agent/skill/workflow: Market Sense Agent / smoke-test handoff
- Workflow: Fixed Income internal full workflow smoke test with ETF wrapper route
- Execution mode: Agent workflow with spawned subagents
- As-of date/time: 2026-06-30
- Output status: Limited
- Evidence status: Current/recent, with flow and term-premium limits
- Freshness status: Partial current refresh
- Source scope: Public sources and spawned-subagent smoke-test handoffs only
- Evidence limits: Official June 30 yield close and full ETF-flow data missing.
- Key limitations: Public-source smoke test; no full line-item holdings file; no June 30 closing curve lock; no personalized portfolio context.
- Missing gates: Full evidence, valuation, risk, portfolio, IC
- Decision boundary: Boundary: Not an IC Action
- Downstream handoff: To downstream workflow modules and IC as a Limited smoke-test artifact
- Required follow-up: Refresh after official June 30 H.15/Treasury close and updated TLT shares/flows.

## Module summary

This artifact records the TLT spawned-subagent smoke-test module output in the canonical handoff format. It is a runtime readiness artifact, not a final investment recommendation.

## Smoke-test findings

Real-yield/long-duration channel appears dominant; Fed/inflation/supply are opposing or cross-current; risk-off and flows are not confirmed as dominant.

## Structured handoff
- Artifact: `market_sense.md`
- Subject: TLT as bond ETF / long-duration U.S. Treasury exposure smoke test
- Scope: Driver-dominance hypotheses for TLT moves
- Owner: Market Sense Agent
- Producing agent/skill/workflow: Market Sense Agent / smoke-test handoff
- Workflow: Fixed Income internal full workflow smoke test with ETF wrapper route
- Execution mode: Agent workflow with spawned subagents
- As-of date/time: 2026-06-30
- Output status: Limited
- Evidence status: Current/recent, with flow and term-premium limits
- Freshness status: Partial current refresh
- Source scope: Public sources and spawned-subagent smoke-test handoffs only
- Evidence limits: Official June 30 yield close and full ETF-flow data missing.
- Key limitations: Public-source smoke test; no full line-item holdings file; no June 30 closing curve lock; no personalized portfolio context.
- Key findings: Real-yield/long-duration channel appears dominant; Fed/inflation/supply are opposing or cross-current; risk-off and flows are not confirmed as dominant.
- Missing gates: Full evidence, valuation, risk, portfolio, IC
- Decision boundary: Boundary: Not an IC Action
- Decision constraints: No final buy/sell/hold/add/trim/exit; no exact allocation, execution, or trade instruction.
- Downstream handoff: To downstream workflow modules and IC as a Limited smoke-test artifact
- Required follow-up: Refresh after official June 30 H.15/Treasury close and updated TLT shares/flows.
