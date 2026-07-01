# Spawned-subagent workflow audit - Fixed Income TLT smoke test

Artifact: `agent_workflow_audit.md`  
Subject: TLT as bond ETF / long-duration U.S. Treasury exposure smoke test  
Date: 2026-06-30  
Execution mode: `Agent workflow with spawned subagents`  
Expected final artifact: `decision_prep_memo.md`  
Final smoke-test result: Pass  
Blocking issues: 0  
Safety failures: 0  

## Spawned agents

| Agent | Agent id | Status | Returned / consumed artifact |
|---|---|---:|---|
| `master-intake-router` | `019f1827-6102-7171-8388-8562d6414a05` | Complete | `route summary` |
| `asset-intake-router` | `019f1827-9afb-71f0-ab7d-d6ecdfea323f` | Complete | `asset route` |
| `evidence-collector` | `019f1827-d393-7b50-8cd9-a7c7d33ddb88` | Limited | `evidence_pack.md` |
| `etf-agent` | `019f1828-1d6e-7331-83f6-fbc2789d0bdb` | Complete | `etf_analysis.md` |
| `fixed-income-agent` | `019f1828-552d-7420-b019-003416414842` | Complete | `fixed_income_analysis.md` |
| `macro-agent` | `019f1828-9239-7181-9aa0-dc5b0c5153f9` | Complete | `macro_sensitivity.md` |
| `valuation-expectations-agent` | `019f1831-f76d-7f72-a90c-480ee0a673da` | Limited | `valuation_expectations.md` |
| `risk-red-team-agent` | `019f1832-2c17-7cd3-b569-912475dd91ba` | Limited | `risk_red_team.md` |
| `portfolio-fit-agent` | `019f1832-5dee-7250-a8cd-4a2a7e63a54b` | Limited | `portfolio_fit.md` |
| `market-positioning-agent` | `019f1832-96ac-7572-b72d-c6feec22206d` | Limited | `market_positioning.md` |
| `news-catalysts-agent` | `019f1834-e587-7cf2-805d-182cb7d43cd4` | Limited | `news_catalysts.md` |
| `market-sense-agent` | `019f1835-15df-7fe0-a452-d0dee2b9b6a2` | Limited | `market_sense.md` |
| `market-intelligence-agent` | `019f1835-4466-7c11-b11f-b2d682d37241` | Complete | `market_intelligence_briefing.md` |
| `investment-committee-agent` | `019f1842-272a-79a0-8ad2-4984816e115e` | Limited | `decision_prep_memo.md` |

## Skipped agents

| Agent | Reason |
|---|---|
| `equity-agent` | Not needed; TLT is not a company equity. |
| `commodity-agent` | Not needed; TLT is not a commodity exposure. |
| `crypto-agent` | Not needed; TLT is not a crypto asset. |
| `sector-industry-analysis-agent` | Not needed; Treasury duration route does not require sector/industry equity context. |
| `theme-opportunity-intake-router` | Not needed; not a theme discovery request. |
| `structural-winners-discovery-agent` | Not needed; not a candidate discovery request. |

## Required artifact checklist

| Artifact | Present | Status |
|---|---:|---|
| `evidence_pack.md` | Yes | Pass |
| `etf_analysis.md` | Yes | Pass |
| `fixed_income_analysis.md` | Yes | Pass |
| `macro_sensitivity.md` | Yes | Pass |
| `valuation_expectations.md` | Yes | Pass |
| `risk_red_team.md` | Yes | Pass |
| `portfolio_fit.md` | Yes | Pass |
| `market_positioning.md` | Yes | Pass |
| `news_catalysts.md` | Yes | Pass |
| `market_sense.md` | Yes | Pass |
| `market_intelligence_briefing.md` | Yes | Pass |
| `decision_prep_memo.md` | Yes | Pass |

## Validation notes

- The workflow used a real multi-agent run: routing, evidence, ETF wrapper, fixed-income, macro, valuation, risk, portfolio, positioning, news, market sense, market intelligence, and IC agents were spawned.
- TLT is treated as a bond ETF, so both `etf-agent` and `fixed-income-agent` are mandatory and were run.
- Final artifact is `decision_prep_memo.md` because portfolio context, same-day rate/flow freshness, and final IC gates remain Limited.
- The smoke test verifies routing and artifact discipline. It is not a final investment decision.
- No non-IC artifact may be used as a final action.
