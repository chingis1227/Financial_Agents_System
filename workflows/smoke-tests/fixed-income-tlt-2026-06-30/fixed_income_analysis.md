# fixed_income_analysis.md - TLT fixed-income smoke-test artifact

## Handoff metadata
- Artifact: `fixed_income_analysis.md`
- Subject: TLT as bond ETF / long-duration U.S. Treasury exposure smoke test
- Owner: Fixed Income Agent
- Producing agent/skill/workflow: Fixed Income Agent / smoke-test handoff
- Workflow: Fixed Income Full Cycle smoke-test with ETF wrapper route
- Execution mode: Delegated Full Agent Workflow
- As-of date/time: 2026-06-30
- Output status: Complete for scoped fixed-income method
- Evidence status: Limited; mostly 2026-06-26 to 2026-06-29 public data
- Freshness status: No June 30 close; latest official curve data lag
- Source scope: Public sources and delegated smoke-test subagent handoffs only
- Evidence limits: No full ETF/risk/portfolio/IC package; no current close lock.
- Key limitations: Public-source smoke test; no full line-item holdings file; no June 30 closing curve lock; no personalized portfolio context.
- Missing gates: ETF vehicle review, macro, valuation, risk, portfolio fit, market positioning/flows, IC synthesis
- Decision boundary: Boundary: Not an IC Action
- Downstream handoff: To downstream workflow modules and IC as a Complete for scoped fixed-income method smoke-test artifact
- Required follow-up: Refresh closing curve and run scenario stress before IC use.

## Module summary

This artifact records the TLT delegated smoke-test module output in the canonical handoff format. It is a runtime readiness artifact, not a final investment recommendation.

## Smoke-test findings

TLT has 4.85% SEC yield, 15.44-year effective duration, 26.05-year maturity; carry absorbs only about 31 bp of adverse annual parallel rate movement; +100 bp shock remains severe.

## Structured handoff
- Artifact: `fixed_income_analysis.md`
- Subject: TLT as bond ETF / long-duration U.S. Treasury exposure smoke test
- Scope: Yield, duration, curve, convexity, real rates/inflation, term premium, carry, drawdown compensation
- Owner: Fixed Income Agent
- Producing agent/skill/workflow: Fixed Income Agent / smoke-test handoff
- Workflow: Fixed Income Full Cycle smoke-test with ETF wrapper route
- Execution mode: Delegated Full Agent Workflow
- As-of date/time: 2026-06-30
- Output status: Complete for scoped fixed-income method
- Evidence status: Limited; mostly 2026-06-26 to 2026-06-29 public data
- Freshness status: No June 30 close; latest official curve data lag
- Source scope: Public sources and delegated smoke-test subagent handoffs only
- Evidence limits: No full ETF/risk/portfolio/IC package; no current close lock.
- Key limitations: Public-source smoke test; no full line-item holdings file; no June 30 closing curve lock; no personalized portfolio context.
- Key findings: TLT has 4.85% SEC yield, 15.44-year effective duration, 26.05-year maturity; carry absorbs only about 31 bp of adverse annual parallel rate movement; +100 bp shock remains severe.
- Missing gates: ETF vehicle review, macro, valuation, risk, portfolio fit, market positioning/flows, IC synthesis
- Decision boundary: Boundary: Not an IC Action
- Decision constraints: No final buy/sell/hold/add/trim/exit; no exact allocation, execution, or trade instruction.
- Downstream handoff: To downstream workflow modules and IC as a Complete for scoped fixed-income method smoke-test artifact
- Required follow-up: Refresh closing curve and run scenario stress before IC use.
