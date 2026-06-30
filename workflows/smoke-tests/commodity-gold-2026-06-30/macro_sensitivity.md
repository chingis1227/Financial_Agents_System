# macro_sensitivity.md - Gold macro sensitivity

## Handoff metadata
- Artifact: `macro_sensitivity.md`
- Subject: Gold commodity exposure for a 3-5 year decision-prep smoke test
- Owner: Macro Agent
- Producing agent/skill/workflow: Macro Agent / smoke-test handoff
- Workflow: Commodity Full Cycle smoke-test
- Execution mode: Delegated Full Agent Workflow
- As-of date/time: 2026-06-30
- Output status: Limited
- Evidence status: Limited; scenario map is usable but needs synchronized macro data for final decision support
- Freshness status: Refresh required for real yields, nominal yields, DXY, breakevens, Fed pricing, liquidity, and risk-stress indicators
- Source scope: Public sources and delegated smoke-test subagent handoffs only
- Evidence limits: No full scenario model; no synchronized market close dataset; no current Fed-pricing lock.
- Key limitations: Public-source smoke test; no paid flow tape; no intraday evidence lock; no personalized portfolio context.
- Missing gates: Real-rate scenario table; USD path; Fed pricing; inflation surprise analysis; liquidity/stress check; IC synthesis
- Decision boundary: Boundary: Not an IC Action
- Downstream handoff: To downstream workflow modules and IC as a Limited smoke-test artifact
- Required follow-up: Build a timestamped macro sensitivity table before IC-stage use.

## Module summary

The macro module keeps gold from being treated as a generic ?safe asset?: it can benefit from stress or inflation fear, but can be pressured by higher real yields and a stronger dollar.

## Smoke-test findings

Gold sensitivity is dominated by real yields, USD, inflation volatility, monetary credibility, liquidity stress, and geopolitical risk; these forces can conflict.

## Structured handoff
- Artifact: `macro_sensitivity.md`
- Subject: Gold commodity exposure for a 3-5 year decision-prep smoke test
- Scope: Real-rate, dollar, inflation, liquidity, Fed, and geopolitical transmission to gold
- Owner: Macro Agent
- Producing agent/skill/workflow: Macro Agent / smoke-test handoff
- Workflow: Commodity Full Cycle smoke-test
- Execution mode: Delegated Full Agent Workflow
- As-of date/time: 2026-06-30
- Output status: Limited
- Evidence status: Limited; scenario map is usable but needs synchronized macro data for final decision support
- Freshness status: Refresh required for real yields, nominal yields, DXY, breakevens, Fed pricing, liquidity, and risk-stress indicators
- Source scope: Public sources and delegated smoke-test subagent handoffs only
- Evidence limits: No full scenario model; no synchronized market close dataset; no current Fed-pricing lock.
- Key limitations: Public-source smoke test; no paid flow tape; no intraday evidence lock; no personalized portfolio context.
- Key findings: Gold sensitivity is dominated by real yields, USD, inflation volatility, monetary credibility, liquidity stress, and geopolitical risk; these forces can conflict.
- Missing gates: Real-rate scenario table; USD path; Fed pricing; inflation surprise analysis; liquidity/stress check; IC synthesis
- Decision boundary: Boundary: Not an IC Action
- Decision constraints: No final buy/sell/hold/add/trim/exit; no exact allocation or trade instruction.
- Downstream handoff: To downstream workflow modules and IC as a Limited smoke-test artifact
- Required follow-up: Build a timestamped macro sensitivity table before IC-stage use.
