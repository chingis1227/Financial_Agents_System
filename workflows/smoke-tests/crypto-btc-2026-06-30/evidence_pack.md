# evidence_pack.md - BTC crypto smoke-test artifact

## Handoff metadata
- Artifact: `evidence_pack.md`
- Subject: BTC over a 3-year horizon for crypto decision-prep smoke test
- Owner: Evidence Collector Agent
- Producing agent/skill/workflow: Evidence Collector Agent / smoke-test handoff
- Workflow: Crypto Full Cycle smoke-test
- Execution mode: Delegated Full Agent Workflow
- As-of date/time: 2026-06-30
- Output status: Limited
- Evidence status: Limited for downstream IC use; pre-IC evidence lock not granted
- Freshness status: Current snapshot for market/on-chain; event-driven refresh required
- Source scope: Public sources and delegated smoke-test subagent handoffs only
- Evidence limits: No paid on-chain data, own-node validation, full venue-depth review, global regulatory scan, or user custody context.
- Key limitations: Public-source smoke test; no paid on-chain pack; no intraday evidence lock; no personalized portfolio context; implementation vehicle unspecified.
- Missing gates: Crypto, valuation-equivalent, macro, positioning, risk, portfolio fit, implementation, final freshness check
- Decision boundary: Boundary: Not an IC Action
- Downstream handoff: To downstream workflow modules and IC as a Limited smoke-test artifact
- Required follow-up: Complete missing evidence gates and rerun final freshness check before IC synthesis.

## Module summary

This artifact records the BTC delegated smoke-test module output in the canonical handoff format. It is a runtime readiness artifact, not a final investment recommendation.

## Smoke-test findings

BTC identity is clear; current market, on-chain, and liquidity snapshots exist; evidence is not sufficient for final decision support.

## Source and provenance table

| Evidence channel | Representative source / provenance | Smoke-test use | Freshness limit |
|---|---|---|---|
| Price / market cap | CoinGecko, exchange/finance quote proxies | BTC market anchor | Continuous refresh needed |
| ETF / institutional flows | Farside, Bitbo, CoinDesk flow references | Marginal demand and recent outflow pressure | Daily and vendor-revisable |
| On-chain / network | Blockchair, mempool.space, public hashrate references | Network activity and security context | Third-party APIs, not own-node verified |
| Macro / liquidity | FRED, Federal Reserve, public liquidity data | Liquidity, real-rate, USD transmission | Release lag and no intraday lock |
| Regulation / custody | SEC, CFTC, Treasury, issuer filings | Legal/access/custody gates | Jurisdiction and rulemaking can change quickly |

## Structured handoff
- Artifact: `evidence_pack.md`
- Subject: BTC over a 3-year horizon for crypto decision-prep smoke test
- Scope: Evidence readiness for BTC crypto route
- Owner: Evidence Collector Agent
- Producing agent/skill/workflow: Evidence Collector Agent / smoke-test handoff
- Workflow: Crypto Full Cycle smoke-test
- Execution mode: Delegated Full Agent Workflow
- As-of date/time: 2026-06-30
- Output status: Limited
- Evidence status: Limited for downstream IC use; pre-IC evidence lock not granted
- Freshness status: Current snapshot for market/on-chain; event-driven refresh required
- Source scope: Public sources and delegated smoke-test subagent handoffs only
- Evidence limits: No paid on-chain data, own-node validation, full venue-depth review, global regulatory scan, or user custody context.
- Key limitations: Public-source smoke test; no paid on-chain pack; no intraday evidence lock; no personalized portfolio context; implementation vehicle unspecified.
- Key findings: BTC identity is clear; current market, on-chain, and liquidity snapshots exist; evidence is not sufficient for final decision support.
- Missing gates: Crypto, valuation-equivalent, macro, positioning, risk, portfolio fit, implementation, final freshness check
- Decision boundary: Boundary: Not an IC Action
- Decision constraints: No final buy/sell/hold/add/trim/exit; no exact allocation, custody instruction, or trade instruction.
- Downstream handoff: To downstream workflow modules and IC as a Limited smoke-test artifact
- Required follow-up: Complete missing evidence gates and rerun final freshness check before IC synthesis.
