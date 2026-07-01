# commodity_analysis.md - Gold commodity analysis

## Handoff metadata
- Artifact: `commodity_analysis.md`
- Subject: Gold commodity exposure for a 3-5 year decision-prep smoke test
- Owner: Commodity Agent
- Producing agent/skill/workflow: Commodity Agent / smoke-test handoff
- Workflow: Commodity internal full workflow smoke test
- Execution mode: Agent workflow with spawned subagents
- As-of date/time: 2026-06-30
- Output status: Limited
- Evidence status: Limited; gold supply/demand and official-sector context are partly supported, but live physical balance and vehicle details are not locked
- Freshness status: Mixed; official-sector and ETF evidence lag current trading conditions
- Source scope: Public sources and spawned-subagent smoke-test handoffs only
- Evidence limits: No complete live physical-demand, refinery, bar/coin premium, futures-curve, or vehicle implementation pack.
- Key limitations: Public-source smoke test; no paid flow tape; no intraday evidence lock; no personalized portfolio context.
- Missing gates: Physical balance; official-sector refresh; ETF/futures flows; curve/carry; vehicle selection; risk and IC synthesis
- Decision boundary: Boundary: Not an IC Action
- Downstream handoff: To downstream workflow modules and IC as a Limited smoke-test artifact
- Required follow-up: Add refreshed physical, official-sector, ETF, CFTC, curve, and instrument evidence before final IC synthesis.

## Module summary

The commodity module confirms gold requires a different checklist from equities: the key questions are reserve demand, opportunity cost, currency, inflation, geopolitical premia, flows, and implementation vehicle.

## Smoke-test findings

Gold is driven less by industrial balance and more by reserve demand, real rates, USD, inflation/geopolitical hedging, ETF/futures flows, and vehicle implementation.

## Structured handoff
- Artifact: `commodity_analysis.md`
- Subject: Gold commodity exposure for a 3-5 year decision-prep smoke test
- Scope: Commodity setup, physical balance, curve, policy, and instrument context for gold
- Owner: Commodity Agent
- Producing agent/skill/workflow: Commodity Agent / smoke-test handoff
- Workflow: Commodity internal full workflow smoke test
- Execution mode: Agent workflow with spawned subagents
- As-of date/time: 2026-06-30
- Output status: Limited
- Evidence status: Limited; gold supply/demand and official-sector context are partly supported, but live physical balance and vehicle details are not locked
- Freshness status: Mixed; official-sector and ETF evidence lag current trading conditions
- Source scope: Public sources and spawned-subagent smoke-test handoffs only
- Evidence limits: No complete live physical-demand, refinery, bar/coin premium, futures-curve, or vehicle implementation pack.
- Key limitations: Public-source smoke test; no paid flow tape; no intraday evidence lock; no personalized portfolio context.
- Key findings: Gold is driven less by industrial balance and more by reserve demand, real rates, USD, inflation/geopolitical hedging, ETF/futures flows, and vehicle implementation.
- Missing gates: Physical balance; official-sector refresh; ETF/futures flows; curve/carry; vehicle selection; risk and IC synthesis
- Decision boundary: Boundary: Not an IC Action
- Decision constraints: No final buy/sell/hold/add/trim/exit; no exact allocation or trade instruction.
- Downstream handoff: To downstream workflow modules and IC as a Limited smoke-test artifact
- Required follow-up: Add refreshed physical, official-sector, ETF, CFTC, curve, and instrument evidence before final IC synthesis.
