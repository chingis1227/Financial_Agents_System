# macro_sensitivity.md - TLT fixed-income smoke-test artifact

## Handoff metadata
- Artifact: `macro_sensitivity.md`
- Subject: TLT as bond ETF / long-duration U.S. Treasury exposure smoke test
- Owner: Macro Agent
- Producing agent/skill/workflow: Macro Agent / smoke-test handoff
- Workflow: Fixed Income internal full workflow smoke test with ETF wrapper route
- Execution mode: Agent workflow with spawned subagents
- As-of date/time: 2026-06-30
- Output status: Complete for scoped macro handoff
- Evidence status: Current/recent public evidence; limited for exact June 30 market close and positioning
- Freshness status: Current for Fed/PCE/GDP/Treasury releases; recent for official yield series
- Source scope: Public sources and spawned-subagent smoke-test handoffs only
- Evidence limits: No full evidence pack, futures/OIS download, auction/flow/positioning check.
- Key limitations: Public-source smoke test; no full line-item holdings file; no June 30 closing curve lock; no personalized portfolio context.
- Missing gates: Evidence lock, fixed-income analysis, ETF analysis, valuation, risk, portfolio fit, positioning/news, IC synthesis
- Decision boundary: Boundary: Not an IC Action
- Downstream handoff: To downstream workflow modules and IC as a Complete for scoped macro handoff smoke-test artifact
- Required follow-up: Run fixed-income curve scenarios and ETF/implementation review before IC synthesis.

## Module summary

This artifact records the TLT spawned-subagent smoke-test module output in the canonical handoff format. It is a runtime readiness artifact, not a final investment recommendation.

## Smoke-test findings

TLT is dominated by long real yields and term premium; sticky inflation and heavy supply are adverse; disinflationary growth shock is favorable.

## Structured handoff
- Artifact: `macro_sensitivity.md`
- Subject: TLT as bond ETF / long-duration U.S. Treasury exposure smoke test
- Scope: Fed path, inflation, growth, real yields, term premium, fiscal/supply, recession/risk-off sensitivity
- Owner: Macro Agent
- Producing agent/skill/workflow: Macro Agent / smoke-test handoff
- Workflow: Fixed Income internal full workflow smoke test with ETF wrapper route
- Execution mode: Agent workflow with spawned subagents
- As-of date/time: 2026-06-30
- Output status: Complete for scoped macro handoff
- Evidence status: Current/recent public evidence; limited for exact June 30 market close and positioning
- Freshness status: Current for Fed/PCE/GDP/Treasury releases; recent for official yield series
- Source scope: Public sources and spawned-subagent smoke-test handoffs only
- Evidence limits: No full evidence pack, futures/OIS download, auction/flow/positioning check.
- Key limitations: Public-source smoke test; no full line-item holdings file; no June 30 closing curve lock; no personalized portfolio context.
- Key findings: TLT is dominated by long real yields and term premium; sticky inflation and heavy supply are adverse; disinflationary growth shock is favorable.
- Missing gates: Evidence lock, fixed-income analysis, ETF analysis, valuation, risk, portfolio fit, positioning/news, IC synthesis
- Decision boundary: Boundary: Not an IC Action
- Decision constraints: No final buy/sell/hold/add/trim/exit; no exact allocation, execution, or trade instruction.
- Downstream handoff: To downstream workflow modules and IC as a Complete for scoped macro handoff smoke-test artifact
- Required follow-up: Run fixed-income curve scenarios and ETF/implementation review before IC synthesis.
