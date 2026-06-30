# risk_red_team.md - Gold risk red-team

## Handoff metadata
- Artifact: `risk_red_team.md`
- Subject: Gold commodity exposure for a 3-5 year decision-prep smoke test
- Owner: Risk / Red Team Agent
- Producing agent/skill/workflow: Risk / Red Team Agent / smoke-test handoff
- Workflow: Commodity Full Cycle smoke-test
- Execution mode: Delegated Full Agent Workflow
- As-of date/time: 2026-06-30
- Output status: Limited
- Evidence status: Limited; structural risk map is usable but not evidence-locked
- Freshness status: Refresh required for spot price, real yields, USD, flows, positioning, curve, and news
- Source scope: Public sources and delegated smoke-test subagent handoffs only
- Evidence limits: No current crowding model, macro scenario model, vehicle file, or liquidity stress test.
- Key limitations: Public-source smoke test; no paid flow tape; no intraday evidence lock; no personalized portfolio context.
- Missing gates: Evidence pack; macro; positioning; valuation; implementation; portfolio; news; IC synthesis
- Decision boundary: Boundary: Not an IC Action
- Downstream handoff: To downstream workflow modules and IC as a Limited smoke-test artifact
- Required follow-up: Stress-test real-yield/USD normalization, flow reversal, and vehicle mechanics before final IC use.

## Module summary

The risk module keeps the gold case from becoming a one-sided hedge story. It marks several unresolved downside paths.

## Smoke-test findings

Main failure paths are higher real yields, stronger USD, fading hedge demand, official-sector slowdown, ETF/futures outflows, liquidity liquidation, and unsuitable vehicle selection.

## Structured handoff
- Artifact: `risk_red_team.md`
- Subject: Gold commodity exposure for a 3-5 year decision-prep smoke test
- Scope: Challenge the gold thesis, failure paths, crowded hedge risk, real-rate/dollar shocks, no-cash-flow valuation limits, and instrument risks
- Owner: Risk / Red Team Agent
- Producing agent/skill/workflow: Risk / Red Team Agent / smoke-test handoff
- Workflow: Commodity Full Cycle smoke-test
- Execution mode: Delegated Full Agent Workflow
- As-of date/time: 2026-06-30
- Output status: Limited
- Evidence status: Limited; structural risk map is usable but not evidence-locked
- Freshness status: Refresh required for spot price, real yields, USD, flows, positioning, curve, and news
- Source scope: Public sources and delegated smoke-test subagent handoffs only
- Evidence limits: No current crowding model, macro scenario model, vehicle file, or liquidity stress test.
- Key limitations: Public-source smoke test; no paid flow tape; no intraday evidence lock; no personalized portfolio context.
- Key findings: Main failure paths are higher real yields, stronger USD, fading hedge demand, official-sector slowdown, ETF/futures outflows, liquidity liquidation, and unsuitable vehicle selection.
- Missing gates: Evidence pack; macro; positioning; valuation; implementation; portfolio; news; IC synthesis
- Decision boundary: Boundary: Not an IC Action
- Decision constraints: No final buy/sell/hold/add/trim/exit; no exact allocation or trade instruction.
- Downstream handoff: To downstream workflow modules and IC as a Limited smoke-test artifact
- Required follow-up: Stress-test real-yield/USD normalization, flow reversal, and vehicle mechanics before final IC use.
