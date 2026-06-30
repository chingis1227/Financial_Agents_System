# evidence_pack.md - TLT fixed-income smoke-test artifact

## Handoff metadata
- Artifact: `evidence_pack.md`
- Subject: TLT as bond ETF / long-duration U.S. Treasury exposure smoke test
- Owner: Evidence Collector Agent
- Producing agent/skill/workflow: Evidence Collector Agent / smoke-test handoff
- Workflow: Fixed Income Full Cycle smoke-test with ETF wrapper route
- Execution mode: Delegated Full Agent Workflow
- As-of date/time: 2026-06-30
- Output status: Limited
- Evidence status: Limited; issuer and Treasury sources support core claims, but current-day rates and full holdings remain missing
- Freshness status: Recent, with refresh required for 2026-06-30 Treasury curve and close-of-day TLT data
- Source scope: Public sources and delegated smoke-test subagent handoffs only
- Evidence limits: Fund data lags by one to four days; line-item holdings not extracted; no risk/valuation/portfolio work.
- Key limitations: Public-source smoke test; no full line-item holdings file; no June 30 closing curve lock; no personalized portfolio context.
- Missing gates: Full holdings file, same-day rate refresh, fixed-income/ETF analysis, macro, valuation, risk, portfolio fit, IC synthesis
- Decision boundary: Boundary: Not an IC Action
- Downstream handoff: To downstream workflow modules and IC as a Limited smoke-test artifact
- Required follow-up: Refresh official 2026-06-30 Treasury curve and TLT close/NAV; extract full holdings file.

## Module summary

This artifact records the TLT delegated smoke-test module output in the canonical handoff format. It is a runtime readiness artifact, not a final investment recommendation.

## Smoke-test findings

TLT identity, fund scale, long-duration Treasury exposure, yield/duration metrics, and latest available long-end Treasury rates are supported at summary level.

## Source and provenance table

| Evidence channel | Representative source / provenance | Smoke-test use | Freshness limit |
|---|---|---|---|
| ETF identity / characteristics | BlackRock / iShares TLT product page | Wrapper, AUM, duration, yield, fee, maturity | Issuer data lag one to several days |
| Nominal Treasury curve | U.S. Treasury daily par curve, FRED DGS20/DGS30 | 20Y/30Y yield anchor | June 30 close required |
| Real yields / term premium | Treasury real yield curve, FRED/SF Fed term-premium proxies | Real-rate and term-premium risk | Model/proxy lag |
| Fed / inflation / growth | Federal Reserve, BEA, BLS, Atlanta Fed | Macro regime and catalyst context | Release schedule lag |
| Positioning / flows | ETF.com, CFTC TFF | Duration demand/crowding | Third-party or weekly lag |

## Structured handoff
- Artifact: `evidence_pack.md`
- Subject: TLT as bond ETF / long-duration U.S. Treasury exposure smoke test
- Scope: ETF identity, Treasury duration/yield evidence, holdings/fund data, rates/freshness limits
- Owner: Evidence Collector Agent
- Producing agent/skill/workflow: Evidence Collector Agent / smoke-test handoff
- Workflow: Fixed Income Full Cycle smoke-test with ETF wrapper route
- Execution mode: Delegated Full Agent Workflow
- As-of date/time: 2026-06-30
- Output status: Limited
- Evidence status: Limited; issuer and Treasury sources support core claims, but current-day rates and full holdings remain missing
- Freshness status: Recent, with refresh required for 2026-06-30 Treasury curve and close-of-day TLT data
- Source scope: Public sources and delegated smoke-test subagent handoffs only
- Evidence limits: Fund data lags by one to four days; line-item holdings not extracted; no risk/valuation/portfolio work.
- Key limitations: Public-source smoke test; no full line-item holdings file; no June 30 closing curve lock; no personalized portfolio context.
- Key findings: TLT identity, fund scale, long-duration Treasury exposure, yield/duration metrics, and latest available long-end Treasury rates are supported at summary level.
- Missing gates: Full holdings file, same-day rate refresh, fixed-income/ETF analysis, macro, valuation, risk, portfolio fit, IC synthesis
- Decision boundary: Boundary: Not an IC Action
- Decision constraints: No final buy/sell/hold/add/trim/exit; no exact allocation, execution, or trade instruction.
- Downstream handoff: To downstream workflow modules and IC as a Limited smoke-test artifact
- Required follow-up: Refresh official 2026-06-30 Treasury curve and TLT close/NAV; extract full holdings file.
