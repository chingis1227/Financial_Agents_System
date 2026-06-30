# decision_prep_memo.md - Gold decision-prep memo

## Handoff metadata
- Artifact: `decision_prep_memo.md`
- Subject: Gold commodity exposure for a 3-5 year decision-prep smoke test
- Owner: Investment Committee Agent
- Producing agent/skill/workflow: Investment Committee Agent / smoke-test handoff
- Workflow: Commodity Full Cycle smoke-test
- Execution mode: Delegated Full Agent Workflow
- As-of date/time: 2026-06-30
- Output status: Limited
- Evidence status: Limited; delegated module artifacts exist, but final evidence freshness and portfolio context remain open
- Freshness status: Needs refresh for market-sensitive inputs before any final memo
- Source scope: Public sources and delegated smoke-test subagent handoffs only
- Evidence limits: No personalized portfolio context; no final evidence lock; gold vehicle unspecified.
- Key limitations: Public-source smoke test; no paid flow tape; no intraday evidence lock; no personalized portfolio context.
- Missing gates: Current evidence lock; vehicle review; portfolio context; final IC synthesis
- Decision boundary: Decision-prep synthesis only; no final IC Action
- Downstream handoff: To downstream workflow modules and IC as a Limited smoke-test artifact
- Required follow-up: Refresh evidence, specify instrument, complete portfolio-fit context, and only then consider a final IC memo.

## Module summary

This is the final smoke-test artifact by design. It proves the delegated route can produce a gate-aware decision-preparation memo without forcing a final action.

## Smoke-test findings

Gold routes cleanly to a Commodity Full Cycle. The decision question should focus on real yields, USD, inflation/geopolitical hedging, central-bank demand, ETF/futures flows, vehicle implementation, and portfolio role.

## Decision-prep scenario logic

| Scenario | What would support it | What would break it | IC implication |
|---|---|---|---|
| Constructive reserve-diversification case | Central-bank demand remains above pre-2022 norms, real yields stabilize or fall, ETF outflows stop, USD pressure eases | Real yields rise, USD strengthens, official-sector demand slows, ETF/futures outflows accelerate | Keep as decision-prep only until current evidence and vehicle choice are locked |
| Range-bound hedge case | Gold retains portfolio hedge role but lacks fresh upside catalyst | Positioning remains crowded and inflation/real-rate data offset each other | Portfolio Fit remains Limited without user exposures |
| Downside unwind case | Higher real yields, stronger USD, lower geopolitical premium, flow liquidation | Renewed inflation/geopolitical shock or policy credibility concern | Risk gate remains open; no final action label |

## Consumed module synthesis

- Evidence identifies gold as a commodity route with fresh-data gaps in price, flows, real rates, and official-sector demand.
- Commodity analysis frames gold as reserve/hedge demand plus macro opportunity-cost, not a cash-flow asset.
- Macro, positioning, market-sense, and market-intelligence modules agree that real yields, USD, ETF/futures flows, and central-bank demand are the core driver set.
- Risk red-team highlights no-cash-flow valuation, crowded hedge risk, and vehicle-specific implementation risk.
- Portfolio Fit remains Limited because user holdings, objective, drawdown tolerance, and preferred instrument are unknown.

## Structured handoff
- Artifact: `decision_prep_memo.md`
- Subject: Gold commodity exposure for a 3-5 year decision-prep smoke test
- Scope: IC decision-prep synthesis for the gold commodity smoke test
- Owner: Investment Committee Agent
- Producing agent/skill/workflow: Investment Committee Agent / smoke-test handoff
- Workflow: Commodity Full Cycle smoke-test
- Execution mode: Delegated Full Agent Workflow
- As-of date/time: 2026-06-30
- Output status: Limited
- Evidence status: Limited; delegated module artifacts exist, but final evidence freshness and portfolio context remain open
- Freshness status: Needs refresh for market-sensitive inputs before any final memo
- Source scope: Public sources and delegated smoke-test subagent handoffs only
- Evidence limits: No personalized portfolio context; no final evidence lock; gold vehicle unspecified.
- Key limitations: Public-source smoke test; no paid flow tape; no intraday evidence lock; no personalized portfolio context.
- Key findings: Gold routes cleanly to a Commodity Full Cycle. The decision question should focus on real yields, USD, inflation/geopolitical hedging, central-bank demand, ETF/futures flows, vehicle implementation, and portfolio role.
- Missing gates: Current evidence lock; vehicle review; portfolio context; final IC synthesis
- Decision boundary: Decision-prep synthesis only; no final IC Action
- Decision constraints: No final buy/sell/hold/add/trim/exit; no exact allocation or trade instruction.
- Downstream handoff: To downstream workflow modules and IC as a Limited smoke-test artifact
- Required follow-up: Refresh evidence, specify instrument, complete portfolio-fit context, and only then consider a final IC memo.
