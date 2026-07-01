# market_positioning.md - Gold market positioning

## Handoff metadata
- Artifact: `market_positioning.md`
- Subject: Gold commodity exposure for a 3-5 year decision-prep smoke test
- Owner: Market Positioning Agent
- Producing agent/skill/workflow: Market Positioning Agent / smoke-test handoff
- Workflow: Commodity internal full workflow smoke test
- Execution mode: Agent workflow with spawned subagents
- As-of date/time: 2026-06-30
- Output status: Limited
- Evidence status: Limited public-data evidence; no pre-IC evidence lock
- Freshness status: Mixed; CFTC and WGC inputs lag current market conditions
- Source scope: Public sources and spawned-subagent smoke-test handoffs only
- Evidence limits: No proprietary CTA, option-dealer, OTC, physical-flow, or institutional positioning data.
- Key limitations: Public-source smoke test; no paid flow tape; no intraday evidence lock; no personalized portfolio context.
- Missing gates: Next CFTC report; June ETF flows; options/skew; CTA exposure; physical flow; current real-yield and dollar close
- Decision boundary: Boundary: Not an IC Action
- Downstream handoff: To downstream workflow modules and IC as a Limited smoke-test artifact
- Required follow-up: Refresh positioning and flow evidence before IC use.

## Module summary

The positioning module identifies a positive but not fully verified crowding risk: the setup can weaken if real yields/USD remain firm and long exposure unwinds.

## Smoke-test findings

Gold positioning appears net long and narrative-saturated around central-bank demand, USD debasement, real rates, and the $4,000/oz area; ETF flows require June confirmation.

## Structured handoff
- Artifact: `market_positioning.md`
- Subject: Gold commodity exposure for a 3-5 year decision-prep smoke test
- Scope: Positioning, flows, narrative saturation, crowding, dollar/real-rate sensitivity, and source limits
- Owner: Market Positioning Agent
- Producing agent/skill/workflow: Market Positioning Agent / smoke-test handoff
- Workflow: Commodity internal full workflow smoke test
- Execution mode: Agent workflow with spawned subagents
- As-of date/time: 2026-06-30
- Output status: Limited
- Evidence status: Limited public-data evidence; no pre-IC evidence lock
- Freshness status: Mixed; CFTC and WGC inputs lag current market conditions
- Source scope: Public sources and spawned-subagent smoke-test handoffs only
- Evidence limits: No proprietary CTA, option-dealer, OTC, physical-flow, or institutional positioning data.
- Key limitations: Public-source smoke test; no paid flow tape; no intraday evidence lock; no personalized portfolio context.
- Key findings: Gold positioning appears net long and narrative-saturated around central-bank demand, USD debasement, real rates, and the $4,000/oz area; ETF flows require June confirmation.
- Missing gates: Next CFTC report; June ETF flows; options/skew; CTA exposure; physical flow; current real-yield and dollar close
- Decision boundary: Boundary: Not an IC Action
- Decision constraints: No final buy/sell/hold/add/trim/exit; no exact allocation or trade instruction.
- Downstream handoff: To downstream workflow modules and IC as a Limited smoke-test artifact
- Required follow-up: Refresh positioning and flow evidence before IC use.
