# Routing and Workflow Contracts

Status: Canonical workflow implementation contract

Authority note: `implementation/00-master-rules.md` governs statuses, gates, user-facing labels, and IC action labels. `implementation/02-canonical-architecture.md` governs owner / contributor boundaries and edge-case architecture. This document applies those rules to route selection and workflow behavior.

## 1. Routing principles

Routers classify requests and select workflows. Routers do not produce final investment views.

Default route families:
1. Asset-first request.
2. Theme / opportunity request.
3. Direct specialist request.
4. Comparison request.
5. Market update / reaction request.

If the request is ambiguous, the router should either ask for the minimum missing context or choose the safest bounded route and label assumptions.

Default ambiguity behavior:
- If a useful preliminary answer is possible, choose the safest bounded route, label assumptions, and use Preliminary or Limited status.
- If a missing input is decision-critical and cannot be safely assumed, ask the minimum clarifying question.
- If the user asks for a fast answer, route to Quick Take / Preliminary rather than final IC Action.
- If the user asks for final decision support, route through the required evidence, asset / specialist, risk, valuation / expectations, and IC gates.
- If current evidence is material, attempt current evidence collection before producing action-oriented analysis.

## 2. Master Intake Router

Trigger: any new user request.

Responsibilities:
- Identify request family.
- Identify asset, theme, sector, instrument, horizon, action intent, and required evidence profile.
- Route to Asset Intake, Theme Intake, direct specialist workflow, or Market Intelligence / Market Sense workflow.
- Prevent premature positive action when valuation, risk, or evidence gates are missing.

Outputs:
- Intake block.
- Selected route.
- Required and optional agents.
- Missing context.
- Evidence profile.

## 3. Asset-first workflow

Trigger examples:
- Analyze NVDA / Apple / a bond / ETF / Bitcoin / oil / gold.
- Should I buy/add/hold/sell this asset?
- Compare two assets.

Sequence:
1. Master Intake Router.
2. Asset Intake Router.
3. Evidence Collector evidence plan.
4. Lead asset-class agent.
5. Required specialists based on decision type.
6. Evidence readiness update / pre-IC lock when final decision is requested.
7. Investment Committee synthesis if decision-support output is requested.

Asset routes:

| Route | Lead agent | Required output |
|---|---|---|
| Equity | Equity Agent | `equity_company_analysis.md`; financial statement output where needed. |
| ETF | ETF Agent | `etf_analysis.md`. |
| Fixed Income | Fixed Income Agent | `fixed_income_analysis.md`. |
| Commodity | Commodity Agent | `commodity_analysis.md` or `commodity_market_regime.md`. |
| Crypto | Crypto Agent | `crypto_analysis.md` or `crypto_market_regime.md`. |
| Comparison | Relevant lead agents + comparison/IC synthesis | Comparison memo with evidence limits. |

Positive action requires evidence readiness plus valuation/risk review when capital allocation is decision-relevant.

Asset-first edge-case behavior:
- If horizon, objective, risk tolerance, or position context is missing, provide a bounded answer with explicit assumptions or ask the minimum clarifying question; do not issue final IC Action.
- If the request may mean new buy, hold, add, trim, or exit, distinguish these cases and request position size, entry price, and portfolio weight before personalized final decision support.
- If the asset lacks classic cash-flow valuation, use the asset-class valuation equivalent or expectations analysis.
- If thesis quality is strong but valuation / expectations are unfavorable, separate quality verdict from investment view and use Watchlist / Defer only as non-IC signals unless IC synthesis issues a final `IC Action`.
- If implementation quality is weak, such as liquidity, spreads, vehicle quality, custody, fees, or accessibility, do not issue positive action without an implementation check and alternatives.

Comparison behavior:
- Relevant asset-class lead agents own their own analysis.
- If the user does not define "best", compare by standard criteria such as objective fit, risk, liquidity, valuation / expectations, implementation quality, and time horizon.
- Provide scenario winners where useful, but reserve final cross-asset IC Action for IC synthesis.

## 4. Equity deep-dive workflow

Required sequence:
1. Intake and routing.
2. Evidence pack.
3. Parallel or staged context work: Equity Company Analysis, Financial Statement Analysis, Sector Context, News, Market Positioning, Macro Sensitivity where material.
4. Valuation & Expectations.
5. Risk / Red Team.
6. Pre-IC evidence lock.
7. Investment Committee memo.

Required decision-gate reports:
- Evidence pack / evidence readiness.
- `equity_company_analysis.md`.
- Financial statement analysis output when financial quality is decision-relevant.
- `valuation_expectations.md` when price/action is decision-relevant.
- `risk_red_team.md` when final action is requested.
- `final_investment_memo.md` for final synthesis.

Conditional reports:
- `sector_context.md`.
- `news_catalysts.md`.
- `market_positioning.md`.
- `macro_sensitivity.md`.
- `portfolio_fit.md`.

## 5. Theme / opportunity workflow

Trigger examples:
- What benefits from AI power demand?
- Find structural winners in nuclear / defense / automation.
- Analyze a sector or theme.

Sequence:
1. Master Intake Router.
2. Theme / Opportunity Intake Router.
3. Evidence Collector discovery evidence plan.
4. Sector & Industry Analysis and/or Structural Winners Discovery.
5. Candidate ranking / investment map / monitoring plan.
6. Handoff to asset-first deep dive for any candidate that may become actionable.

Allowed outputs:
- `sector_industry_memo.md`.
- `sector_investment_map.md`.
- `sector_monitoring_plan.md`.
- `structural_winners_memo.md`.
- `candidate_watchlist.md`.

Restriction: candidate discovery is not a final investment action.

Theme / discovery edge-case behavior:
- Discovery may rank candidates and assign Actionability Labels as analysis priorities.
- Actionability Labels in discovery mean next-step priority, not buy / sell / hold and not final IC Action.
- Any candidate that may become actionable must be handed off to an asset-first workflow and IC before final action.

## 6. Direct specialist workflow

Trigger examples:
- Only value this company.
- Red-team this thesis.
- Why did this asset move today?
- Check recent catalysts.
- Check positioning or portfolio fit.

Rules:
- Specialist output must state scope.
- It must not present itself as final IC decision.
- Missing upstream inputs produce Preliminary, Limited, or Blocked status.
- Positive action requires escalation to the full decision workflow.

Direct specialist edge-case behavior:
- Direct calls to Risk, Valuation, News & Catalysts, Market Positioning, Macro, Portfolio Fit, Market Sense, or Market Intelligence are allowed.
- The specialist must label the output mode and state that it is not a final IC decision.
- If evidence is weak, the specialist may provide framework, scenario analysis, preliminary view, or checklist, but not final action.
- If Portfolio Fit is requested without portfolio data, provide generic fit by investor scenario, state assumptions, and provide a data checklist.
- News and market reaction outputs must distinguish confirmed, unconfirmed, and market-implied claims.

## 7. Market intelligence / market sense workflow

Market Intelligence owns briefing and situational market awareness.

Market Sense owns market reaction interpretation, driver dominance, and hypothesis generation.

These outputs can inform asset workflows or IC, but they do not replace evidence, valuation, risk, or final synthesis.

Market reaction behavior:
- Check the asset move against peers, sector, index, volume, rates, FX, commodity, or crypto beta where material.
- Rumors may be discussed only as unconfirmed inputs and must not be treated as facts.
- If no supported driver can be identified, return Low confidence or Limited status rather than inventing a causal explanation.

## 8. Update workflow

Trigger examples:
- Update the prior memo.
- What changed since the last view?
- Is the old thesis still valid?
- Update after earnings, guidance, macro release, price move, or catalyst.

Rules:
- Use delta-update by default: prior view, changed facts, unchanged thesis points, changed assumptions, catalyst status, impact on thesis, and updated status.
- If the prior memo or old thesis is unavailable, request it or perform fresh analysis with that limitation.
- If changes are material to action, route to renewed evidence collection and IC review.
- Do not silently treat a stale prior memo as current evidence.

## 9. Completion rules

A workflow is Complete only when required reports and evidence readiness are sufficient for the requested scope.

A workflow is Limited when it can answer the request with material limitations.

A workflow is Blocked when decision-critical evidence or required upstream analysis is missing.

A workflow is Preliminary when it is a narrow scan, early read, or direct specialist output that cannot support final action.
