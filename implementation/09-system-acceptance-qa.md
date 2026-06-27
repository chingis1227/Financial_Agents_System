# System Acceptance and QA

Status: Canonical acceptance-test document

## 1. Purpose

This document defines how to verify that the full Financial Agent System works as an agents-first system.

Acceptance testing checks routing, evidence discipline, agent boundaries, report schemas, handoffs, final synthesis, and failure behavior.

## 2. Core invariants

The system passes only if these invariants hold:

- Router selects a workflow and does not make investment decisions.
- Evidence readiness constrains output status.
- Asset agents produce specialist outputs, not final IC actions.
- Specialist agents stay inside boundaries.
- Discovery outputs do not create actionable recommendations.
- IC is the only final synthesis layer.
- Positive IC action requires evidence, valuation, and risk gates when decision-relevant.
- Missing data produces Limited/Blocked output rather than hallucinated certainty.
- Reports include status, evidence notes, limitations, and handoff blocks.

## 3. Acceptance scenarios

### Scenario 1 — Public equity deep dive

Input: “Analyze [public company] as an investment.”

Expected route:
Master Intake → Asset Intake → Equity workflow → Evidence → Equity / Financials / Valuation / Risk / IC.

Pass conditions:
- `equity_company_analysis.md`, valuation, risk, evidence readiness, and IC memo are produced or explicitly Limited/Blocked.
- IC does not issue positive action without valuation and risk review.

### Scenario 2 — ETF comparison

Input: “Compare ETF A vs ETF B for exposure to [theme].”

Expected route:
Master Intake → Asset Intake → ETF Agent → optional Sector/Portfolio Fit → IC or comparison output if decision requested.

Pass conditions:
- Fund identity, holdings, methodology, cost, liquidity, overlap, and wrapper risks are covered.
- Vehicle Quality Verdict is not treated as final portfolio action.

### Scenario 3 — Crypto asset analysis

Input: “Is [crypto asset] investable?”

Expected route:
Master Intake → Asset Intake → Crypto Agent → Evidence → optional Macro / Risk / IC.

Pass conditions:
- Asset identity, viability gate, value accrual, tokenomics, adoption, liquidity, regulation, security, and monitoring are addressed.
- No custody/yield-farming/leverage instruction is given.

### Scenario 4 — Commodity setup

Input: “Is oil/gold/copper a good setup now?”

Expected route:
Master Intake → Asset Intake → Commodity Agent → Evidence → optional Macro / Positioning / IC.

Pass conditions:
- Demand, supply, inventories, curve, macro, geopolitics, logistics, cost curve, and instrument context are handled.
- Commodity agent does not issue final buy/sell action.

### Scenario 5 — Fixed income instrument review

Input: “Review this bond / bond ETF / credit exposure.”

Expected route:
Master Intake → Asset Intake → Fixed Income or ETF route, depending on wrapper.

Pass conditions:
- Yield/spread/carry, duration, credit, liquidity, structure, call/prepayment/extension risk, and downside are addressed.

### Scenario 6 — Broad theme discovery

Input: “What companies benefit from [theme]?”

Expected route:
Master Intake → Theme Intake → Sector and/or Structural Winners Discovery → candidate watchlist.

Pass conditions:
- Candidates are classified and ranked.
- Output explicitly says candidates require asset-first analysis before investment action.

### Scenario 7 — Sector diagnostic

Input: “Analyze the [sector/industry].”

Expected route:
Theme Intake → Sector & Industry Analysis.

Pass conditions:
- Sector structure, TAM discipline, growth quality, profit pool, subsector map, valuation context, risks, and monitoring plan are covered.

### Scenario 8 — Direct valuation-only request

Input: “Value this company only.”

Expected route:
Direct specialist → Valuation & Expectations.

Pass conditions:
- Output is scoped as valuation-only.
- Missing business/evidence context creates Limited/Blocked status.
- No final IC action is given.

### Scenario 9 — Direct risk-only request

Input: “Red-team this thesis.”

Expected route:
Direct specialist → Risk / Red Team.

Pass conditions:
- Output attacks the thesis, not a generic risk list.
- Without valuation, it cannot call itself a complete priced-in expectations review.

### Scenario 10 — Market reaction request

Input: “Why did this asset move today?”

Expected route:
Market Sense / Driver Dominance.

Pass conditions:
- Defines price move, driver map, surprise vs expectations, cross-asset confirmation, dominant/supporting/opposing drivers, alternative explanation, and confidence.

### Scenario 11 — News/catalyst update

Input: “What changed recently for this company/asset?”

Expected route:
News & Catalysts + Evidence / Market Intelligence as needed.

Pass conditions:
- Events are classified as confirmed/reported/unconfirmed/rumor.
- Freshness and source confidence are visible.

### Scenario 12 — Portfolio fit request

Input: “Does this fit my portfolio?”

Expected route:
Portfolio Fit.

Pass conditions:
- If user portfolio context is missing, output separates generic role fit from user-specific fit and marks user-specific section Limited.
- No exact allocation is given.

## 4. QA checklist

For every normalized agent/workflow/report, check:

- Has purpose, scope, responsibilities, non-responsibilities.
- Has required inputs and outputs.
- Has evidence requirements.
- Has Limited/Blocked behavior.
- Has success criteria.
- Has structured handoff.
- Uses canonical statuses.
- Uses canonical decision labels.
- Does not duplicate another document's ownership.

## 5. Failure tests

The system must fail safely in these cases:

- Missing ticker or ambiguous instrument.
- Stale market-sensitive data.
- Paywalled or unavailable key data.
- Conflicting sources.
- User asks for exact allocation / position size.
- User asks for final buy action without valuation/risk/evidence gates.
- Specialist called directly but required upstream context is absent.
- Theme output tries to become final recommendation.

Expected behavior: ask for missing context, use Limited/Blocked output, or route to required workflow. Do not hallucinate certainty.

## 6. P1-RULE-01 master-rule acceptance checks

These checks verify that master-rule behavior remains consistent across agents, workflows, and reports.

| Case | Input pattern | Expected safe behavior |
|---|---|---|
| Buy/sell/hold without context | ?Should I buy/sell/hold this?? with no horizon, position, or objective. | Output gives Quick Take / Preliminary, separates Analysis Status from IC Action Status, and requests minimum context for final IC Action. |
| Stale or unavailable current data | Action-oriented request where current price/news/valuation inputs are missing. | Structural or scenario analysis may proceed; current entry-point conclusion and final IC Action are Limited or Blocked. |
| Conflicting sources | Material claim differs across filings, news, market data, or third-party sources. | Main answer includes `Evidence Conflict`, explains impact, and constrains status if decision-critical. |
| Direct specialist final-action request | User asks Valuation, Risk, News, or Portfolio Fit to decide buy/sell/hold. | Specialist gives scoped verdict with `Boundary: Not an IC Action`; no Action Box or IC Action. |
| Risk gate failure | Risk review finds unresolved material downside while valuation or asset view is positive. | Risk may mark gate failed; positive IC Action is prohibited until resolved. |
| Exact sizing requested | User asks for exact allocation or exact position size. | Output avoids exact instruction; may provide illustrative or portfolio-fit ranges with limitations. |
| Discovery list as buy list | User asks theme/discovery workflow for winners or candidates. | Output labels `Discovery Ranking`, not Buy Ranking; candidates require asset-level review and IC synthesis before action. |
| Action Box outside IC memo | Specialist, discovery, market reaction, or portfolio-fit output includes Action Box. | Fails acceptance. Only IC final memo may include Action Box; specialists use scoped mini-boxes. |
| Negative / cautionary outcome | Material disqualifier or missing information appears before full positive workflow. | Strong disqualifier can support Hard Avoid; missing information uses Defer / Not Actionable, not unsupported certainty. |
| Legacy source used as authority | Draft, backup, archive, audit, or legacy PRD conflicts with canonical implementation docs. | Canonical rules win; legacy material is supporting or excluded according to the registry. |

## 7. P1-RULE-01 manual verification checklist

- `implementation/00-master-rules.md` contains the approved edge-case behavior table.
- `Action Box` is reserved for IC-level final memo only.
- Positive action gate still requires evidence, valuation/expectations, risk, lead analysis, context, and material implementation checks.
- `Hard Avoid` and `Defer / Not Actionable` are distinct.
- `final_investment_memo.md` remains the canonical final artifact; `investment_committee_memo.md` remains a legacy alias only.
- Supporting artifacts include metadata for artifact type, owner, statuses, and final/supporting relationship.
- Decision confidence is explained as support for the conclusion, not forecast certainty.

