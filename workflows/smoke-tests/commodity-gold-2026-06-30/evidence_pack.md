# evidence_pack.md - Gold commodity evidence pack

## Handoff metadata
- Artifact: `evidence_pack.md`
- Subject: Gold commodity exposure for a 3-5 year decision-prep smoke test
- Owner: Evidence Collector Agent
- Producing agent/skill/workflow: Evidence Collector Agent / smoke-test handoff
- Workflow: Commodity internal full workflow smoke test
- Execution mode: Agent workflow with spawned subagents
- As-of date/time: 2026-06-30
- Output status: Limited
- Evidence status: Limited; public current/recent sources are usable for smoke testing but not a final IC evidence lock
- Freshness status: Mixed; market-sensitive gold, real-rate, dollar, ETF-flow, CFTC, and official-sector data require refresh before final use
- Source scope: Public sources and spawned-subagent smoke-test handoffs only
- Evidence limits: Gold price and dollar proxies are current/recent; WGC official-sector and ETF data are lagged; CFTC positioning is lagged; no final evidence lock.
- Key limitations: Public-source smoke test; no paid flow tape; no intraday evidence lock; no personalized portfolio context.
- Missing gates: Updated gold price; real yields; DXY; WGC ETF flows; central-bank data; CFTC positioning; vehicle review; IC synthesis
- Decision boundary: Boundary: Not an IC Action
- Downstream handoff: To downstream workflow modules and IC as a Limited smoke-test artifact
- Required follow-up: Refresh all market-sensitive evidence after the 2026-06-30 close and lock sources before final IC use.

## Module summary

The evidence pack confirms that gold should be treated as a commodity route, not an equity, crypto, or fixed-income route. The smoke test has enough evidence structure to verify workflow operation, but not enough locked freshness for final decision support.

## Smoke-test findings

Gold evidence map identifies real yields, USD, official-sector demand, ETF flows, futures positioning, inflation, and geopolitics as required evidence channels.

## Source and provenance table

| Evidence channel | Representative source / provenance | Smoke-test use | Freshness limit |
|---|---|---|---|
| Gold price / market backdrop | Trading Economics / public market-data proxies | Current price and drawdown context | Requires post-close refresh |
| Official-sector demand | World Gold Council central-bank demand and reserve survey | Structural demand support | WGC data lag monthly/quarterly |
| ETF flows | World Gold Council gold ETF flows | Investor demand and flow pressure | June data incomplete |
| Real yields / dollar | FRED / Treasury / DXY public proxies | Macro opportunity-cost channel | Same-day close needed |
| Futures positioning | CFTC COT gold reports | Crowding and unwind risk | Weekly lag |

## Structured handoff
- Artifact: `evidence_pack.md`
- Subject: Gold commodity exposure for a 3-5 year decision-prep smoke test
- Scope: Evidence readiness for gold commodity route
- Owner: Evidence Collector Agent
- Producing agent/skill/workflow: Evidence Collector Agent / smoke-test handoff
- Workflow: Commodity internal full workflow smoke test
- Execution mode: Agent workflow with spawned subagents
- As-of date/time: 2026-06-30
- Output status: Limited
- Evidence status: Limited; public current/recent sources are usable for smoke testing but not a final IC evidence lock
- Freshness status: Mixed; market-sensitive gold, real-rate, dollar, ETF-flow, CFTC, and official-sector data require refresh before final use
- Source scope: Public sources and spawned-subagent smoke-test handoffs only
- Evidence limits: Gold price and dollar proxies are current/recent; WGC official-sector and ETF data are lagged; CFTC positioning is lagged; no final evidence lock.
- Key limitations: Public-source smoke test; no paid flow tape; no intraday evidence lock; no personalized portfolio context.
- Key findings: Gold evidence map identifies real yields, USD, official-sector demand, ETF flows, futures positioning, inflation, and geopolitics as required evidence channels.
- Missing gates: Updated gold price; real yields; DXY; WGC ETF flows; central-bank data; CFTC positioning; vehicle review; IC synthesis
- Decision boundary: Boundary: Not an IC Action
- Decision constraints: No final buy/sell/hold/add/trim/exit; no exact allocation or trade instruction.
- Downstream handoff: To downstream workflow modules and IC as a Limited smoke-test artifact
- Required follow-up: Refresh all market-sensitive evidence after the 2026-06-30 close and lock sources before final IC use.
