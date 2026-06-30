# market_positioning.md - TLT fixed-income smoke-test artifact

## Handoff metadata
- Artifact: `market_positioning.md`
- Subject: TLT as bond ETF / long-duration U.S. Treasury exposure smoke test
- Owner: Market Positioning Agent
- Producing agent/skill/workflow: Market Positioning Agent / smoke-test handoff
- Workflow: Fixed Income Full Cycle smoke-test with ETF wrapper route
- Execution mode: Delegated Full Agent Workflow
- As-of date/time: 2026-06-30
- Output status: Limited
- Evidence status: Limited public-data positioning read; source and lag limits remain
- Freshness status: Recent; ETF flow and CFTC positioning are delayed/revisable
- Source scope: Public sources and delegated smoke-test subagent handoffs only
- Evidence limits: ETF flows are delayed; CFTC data lag and are not DV01-normalized; no options/dealer/premium data.
- Key limitations: Public-source smoke test; no full line-item holdings file; no June 30 closing curve lock; no personalized portfolio context.
- Missing gates: Fresh ETF flows, next CFTC report, options/dealer data, portfolio and IC gates
- Decision boundary: Boundary: Not an IC Action
- Downstream handoff: To downstream workflow modules and IC as a Limited smoke-test artifact
- Required follow-up: Refresh ETF flows for June 30 and update CFTC after the next weekly release.

## Module summary

This artifact records the TLT delegated smoke-test module output in the canonical handoff format. It is a runtime readiness artifact, not a final investment recommendation.

## Smoke-test findings

Public evidence points to recent TLT ETF demand but not definitive all-investor duration crowding; futures positioning is split between asset managers and leveraged funds.

## Structured handoff
- Artifact: `market_positioning.md`
- Subject: TLT as bond ETF / long-duration U.S. Treasury exposure smoke test
- Scope: Treasury duration positioning, ETF flows, futures/spec positioning, curve/term-premium narrative, crowding, source limits
- Owner: Market Positioning Agent
- Producing agent/skill/workflow: Market Positioning Agent / smoke-test handoff
- Workflow: Fixed Income Full Cycle smoke-test with ETF wrapper route
- Execution mode: Delegated Full Agent Workflow
- As-of date/time: 2026-06-30
- Output status: Limited
- Evidence status: Limited public-data positioning read; source and lag limits remain
- Freshness status: Recent; ETF flow and CFTC positioning are delayed/revisable
- Source scope: Public sources and delegated smoke-test subagent handoffs only
- Evidence limits: ETF flows are delayed; CFTC data lag and are not DV01-normalized; no options/dealer/premium data.
- Key limitations: Public-source smoke test; no full line-item holdings file; no June 30 closing curve lock; no personalized portfolio context.
- Key findings: Public evidence points to recent TLT ETF demand but not definitive all-investor duration crowding; futures positioning is split between asset managers and leveraged funds.
- Missing gates: Fresh ETF flows, next CFTC report, options/dealer data, portfolio and IC gates
- Decision boundary: Boundary: Not an IC Action
- Decision constraints: No final buy/sell/hold/add/trim/exit; no exact allocation, execution, or trade instruction.
- Downstream handoff: To downstream workflow modules and IC as a Limited smoke-test artifact
- Required follow-up: Refresh ETF flows for June 30 and update CFTC after the next weekly release.
