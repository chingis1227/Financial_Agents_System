# Delegated workflow audit - ETF QQQ vs SCHG smoke test

Artifact: `delegated_workflow_audit.md`  
Subject: QQQ vs SCHG for long-term U.S. growth exposure  
Date: 2026-06-30  
Execution mode: `Delegated Full Agent Workflow`  
Expected final artifact: `decision_prep_memo.md`  
Final smoke-test result: Pass  
Blocking issues: 0  
Safety failures: 0  

## Spawned agents

| Agent | Agent id | Status | Returned / consumed artifact |
|---|---|---:|---|
| `master-intake-router` | `019f17e7-f3eb-7f12-8125-561d045a0ddd` | Complete | `route summary` |
| `asset-intake-router` | `019f17e8-2fea-7773-8d39-a671301ae210` | Complete | `asset route` |
| `evidence-collector` | `019f17e8-6c68-7402-bd88-a4656b92b6e7` | Limited | `evidence_pack.md` |
| `etf-agent` | `019f17e8-bda4-7df2-90f7-dbafeb9b5798` | Limited | `etf_analysis.md` |
| `valuation-expectations-agent` | `019f17e9-010b-79a0-84d1-94b7403570f2` | Limited | `valuation_expectations.md` |
| `risk-red-team-agent` | `019f17e9-3dca-7522-9ec2-31caef8fabe7` | Limited | `risk_red_team.md` |
| `portfolio-fit-agent` | `019f17ed-99fd-7341-a108-0a1556b6adb4` | Limited | `portfolio_fit.md` |
| `macro-agent` | `019f17ed-da6d-7a81-bff1-54c123260df5` | Limited | `macro_sensitivity.md` |
| `market-positioning-agent` | `019f17ee-10d6-79f1-94f3-ddcbe1a78746` | Limited | `market_positioning.md` |
| `news-catalysts-agent` | `019f17ee-67db-77d1-82bf-9eaf36f085f5` | Complete | `news_catalysts.md` |
| `market-sense-agent` | `019f17ee-9f0d-7960-90ba-55e0e050fe56` | Limited | `market_sense.md` |
| `market-intelligence-agent` | `019f17ee-d80e-7652-84c5-356ce3dec331` | Limited | `market_intelligence_briefing.md` |
| `sector-industry-analysis-agent` | `019f17f2-d356-7a43-b4c3-a072e2356167` | Complete | `sector_context.md` |
| `investment-committee-agent` | `019f17f3-0f7d-79c2-b8c6-094b394555b3` | Limited | `decision_prep_memo.md` |

## Skipped agents

| Agent | Reason |
|---|---|
| `equity-agent` | Not needed; this is an ETF wrapper comparison, not single-company analysis. |
| `commodity-agent` | Not needed; no commodity exposure. |
| `crypto-agent` | Not needed; no crypto asset or wrapper. |
| `fixed-income-agent` | Not needed; QQQ/SCHG are equity growth ETFs, not bond funds. |
| `theme-opportunity-intake-router` | Not needed; not a theme discovery request. |
| `structural-winners-discovery-agent` | Not needed; not a candidate discovery request. |

## Required artifact checklist

| Artifact | Present | Status |
|---|---:|---|
| `evidence_pack.md` | Yes | Pass |
| `etf_analysis.md` | Yes | Pass |
| `valuation_expectations.md` | Yes | Pass |
| `risk_red_team.md` | Yes | Pass |
| `portfolio_fit.md` | Yes | Pass |
| `market_positioning.md` | Yes | Pass |
| `macro_sensitivity.md` | Yes | Pass |
| `news_catalysts.md` | Yes | Pass |
| `market_sense.md` | Yes | Pass |
| `market_intelligence_briefing.md` | Yes | Pass |
| `sector_context.md` | Yes | Pass |
| `decision_prep_memo.md` | Yes | Pass |

## Validation notes

- The workflow used a real multi-agent run: route, evidence, ETF, valuation, risk, portfolio, macro, positioning, news, market sense, market intelligence, sector, and IC agents were spawned.
- The IC subagent initially created a temporary root memo that described its local execution mode as single-agent. The canonical smoke-test artifact in this folder corrects the parent workflow record to `Delegated Full Agent Workflow`, because the parent workflow did spawn and consume subagent outputs.
- Final artifact is `decision_prep_memo.md` because portfolio context and several IC gates remain Limited.
- No non-IC artifact may be used as a final action.
