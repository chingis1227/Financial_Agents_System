# evidence_pack.md - QQQ vs SCHG for long-term U.S. growth exposure

## Handoff metadata
- Artifact: `evidence_pack.md`
- Subject: QQQ vs SCHG for long-term U.S. growth exposure
- Owner: Evidence Collector Agent
- Producing agent/skill/workflow: Evidence Collector Agent / smoke-test handoff
- Workflow: ETF internal full workflow smoke test
- Execution mode: Agent workflow with spawned subagents
- As-of date/time: 2026-06-30
- Output status: Limited
- Evidence status: Limited; official identity and fees supported; QQQ detailed holdings and current liquidity require refresh
- Freshness status: Mixed; SCHG current to 2026-06-29; QQQ official dynamic holdings were partially unavailable
- Source scope: Public sources only
- Evidence limits: Dynamic QQQ holdings limitation; no paid holdings export; no full same-day liquidity tape; no final evidence lock
- Key limitations: Dynamic QQQ holdings limitation; no paid holdings export; no full same-day liquidity tape; no final evidence lock
- Missing gates: Current QQQ holdings export; same-day liquidity; overlap; valuation; risk; portfolio fit; IC synthesis
- Decision boundary: Boundary: Not an IC Action
- Downstream handoff: To ETF Analysis, Valuation, Risk, Portfolio Fit, context modules, and IC as Limited evidence input
- Required follow-up: Refresh official holdings exports and same-day liquidity data before final IC use

## Evidence summary

The evidence handoff supports route identity and high-level comparison only. QQQ is treated as an Invesco Nasdaq-100 ETF; SCHG is treated as Schwab's U.S. large-cap growth ETF. SCHG official data provided richer current holdings detail than QQQ during this run, so final evidence lock remains unavailable.

## Claim support map

| Claim | Status | Note |
|---|---|---|
| QQQ is Nasdaq-100 exposure | Supported | Invesco official pages identify the fund and exposure. |
| QQQ expense ratio is 0.18% | Supported | Invesco official page. |
| SCHG tracks Dow Jones U.S. Large-Cap Growth Total Stock Market Index | Supported | Schwab official page. |
| SCHG expense ratio is 0.040% and holdings count is 197 | Supported | Schwab official page as of 2026-06-29. |
| Full QQQ/SCHG holdings overlap | Limited | Requires current holdings export and overlap file. |


## Source and provenance table

| Evidence channel | Source locator / provenance | Smoke-test use | Freshness limit |
|---|---|---|---|
| QQQ identity and fee | Invesco official QQQ fund page; checked in smoke run dated 2026-06-30 | Fund identity, index exposure, expense ratio | Dynamic holdings export still requires refresh |
| SCHG identity, fee, and holdings count | Schwab official SCHG fund page; cited as current to 2026-06-29 in smoke run | Fund identity, benchmark, fee, holdings count | Same-day holdings export should be refreshed before final IC use |
| Comparative overlap and liquidity | Required downstream official holdings/liquidity exports | Determines exposure purity and implementation risk | Not locked in this smoke fixture |


## Structured handoff
- Artifact: `evidence_pack.md`
- Subject: QQQ vs SCHG for long-term U.S. growth exposure
- Scope: Official ETF-page evidence intake
- Owner: Evidence Collector Agent
- Producing agent/skill/workflow: Evidence Collector Agent / smoke-test handoff
- Workflow: ETF internal full workflow smoke test
- Execution mode: Agent workflow with spawned subagents
- As-of date/time: 2026-06-30
- Output status: Limited
- Evidence status: Limited; official identity and fees supported; QQQ detailed holdings and current liquidity require refresh
- Freshness status: Mixed; SCHG current to 2026-06-29; QQQ official dynamic holdings were partially unavailable
- Source scope: Public sources only
- Evidence limits: Dynamic QQQ holdings limitation; no paid holdings export; no full same-day liquidity tape; no final evidence lock
- Key limitations: Dynamic QQQ holdings limitation; no paid holdings export; no full same-day liquidity tape; no final evidence lock
- Key findings: QQQ tracks Nasdaq-100 with 0.18% fee; SCHG tracks Dow Jones U.S. Large-Cap Growth with 0.040% fee and 197 holdings
- Missing gates: Current QQQ holdings export; same-day liquidity; overlap; valuation; risk; portfolio fit; IC synthesis
- Decision boundary: Boundary: Not an IC Action
- Decision constraints: No final buy/sell/hold/add/trim/exit; no exact allocation or trade instruction.
- Downstream handoff: To ETF Analysis, Valuation, Risk, Portfolio Fit, context modules, and IC as Limited evidence input
- Required follow-up: Refresh official holdings exports and same-day liquidity data before final IC use
