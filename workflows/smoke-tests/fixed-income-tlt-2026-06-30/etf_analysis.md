# etf_analysis.md - TLT fixed-income smoke-test artifact

## Handoff metadata
- Artifact: `etf_analysis.md`
- Subject: TLT as bond ETF / long-duration U.S. Treasury exposure smoke test
- Owner: ETF Agent
- Producing agent/skill/workflow: ETF Agent / smoke-test handoff
- Workflow: Fixed Income internal full workflow smoke test with ETF wrapper route
- Execution mode: Agent workflow with spawned subagents
- As-of date/time: 2026-06-30
- Output status: Complete for scoped ETF wrapper handoff
- Evidence status: Limited issuer/index public evidence
- Freshness status: Recent issuer data; live order book not reviewed
- Source scope: Public sources and spawned-subagent smoke-test handoffs only
- Evidence limits: No live order-book, creation/redemption basket audit, independent tracking-error model, tax analysis, or portfolio context.
- Key limitations: Public-source smoke test; no full line-item holdings file; no June 30 closing curve lock; no personalized portfolio context.
- Missing gates: Fixed-income compensation, macro/rates, valuation/expectations, risk, portfolio fit, IC synthesis
- Decision boundary: Boundary: Not an IC Action
- Downstream handoff: To downstream workflow modules and IC as a Complete for scoped ETF wrapper handoff smoke-test artifact
- Required follow-up: Run fixed-income and portfolio gates before IC use.

## Module summary

This artifact records the TLT spawned-subagent smoke-test module output in the canonical handoff format. It is a runtime readiness artifact, not a final investment recommendation.

## Smoke-test findings

TLT wrapper quality is high; exposure purity is very high; implementation risk is mainly long-end rate sensitivity, not wrapper structure.

## Structured handoff
- Artifact: `etf_analysis.md`
- Subject: TLT as bond ETF / long-duration U.S. Treasury exposure smoke test
- Scope: Wrapper quality, exposure purity, duration exposure, liquidity, tracking, fees, implementation risks
- Owner: ETF Agent
- Producing agent/skill/workflow: ETF Agent / smoke-test handoff
- Workflow: Fixed Income internal full workflow smoke test with ETF wrapper route
- Execution mode: Agent workflow with spawned subagents
- As-of date/time: 2026-06-30
- Output status: Complete for scoped ETF wrapper handoff
- Evidence status: Limited issuer/index public evidence
- Freshness status: Recent issuer data; live order book not reviewed
- Source scope: Public sources and spawned-subagent smoke-test handoffs only
- Evidence limits: No live order-book, creation/redemption basket audit, independent tracking-error model, tax analysis, or portfolio context.
- Key limitations: Public-source smoke test; no full line-item holdings file; no June 30 closing curve lock; no personalized portfolio context.
- Key findings: TLT wrapper quality is high; exposure purity is very high; implementation risk is mainly long-end rate sensitivity, not wrapper structure.
- Missing gates: Fixed-income compensation, macro/rates, valuation/expectations, risk, portfolio fit, IC synthesis
- Decision boundary: Boundary: Not an IC Action
- Decision constraints: No final buy/sell/hold/add/trim/exit; no exact allocation, execution, or trade instruction.
- Downstream handoff: To downstream workflow modules and IC as a Complete for scoped ETF wrapper handoff smoke-test artifact
- Required follow-up: Run fixed-income and portfolio gates before IC use.
