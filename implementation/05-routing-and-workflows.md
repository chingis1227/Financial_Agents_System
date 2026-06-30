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
- If the user asks for a fast / short / quick-take answer, ask exactly 3 relevant questions in one block, wait for the user's next message, then route to chat-only Quick Take / Preliminary; do not create `investment_report.md` or `audit`, and do not present it as final IC Action.
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

Full Cycle default triggers for concrete assets include concrete-asset capital-decision wording such as whether to invest, buy, add, hold, sell, start exposure, no current position, multi-year horizon, `should I invest`, `should I buy`, and `worth buying`. Quick Take is allowed instead only when the user explicitly asks for short / fast / quick take / no full cycle / preliminary output.

Execution-mode routing rule:
- Ordinary concrete-asset investment-action requests route to `Delegated Full Agent Workflow` by default, using only relevant subagents/modules for the selected workflow.
- Delegation must be real: use `Delegated Full Agent Workflow` only when relevant subagents are actually spawned and return structured handoffs or artifact-equivalent summaries. If delegated tooling is unavailable or no subagents are actually spawned, use `Single-agent Full Cycle` in audit metadata and do not imply delegated execution.
- Ordinary chat must not show `Execution mode`, Runtime Execution Plan, agent lists, skipped-agent lists, handoff metadata, module statuses, technical gate tables, runtime gate metadata, or canonical artifact names unless the user explicitly asks for workflow/debug/audit details. These details are recorded in `audit\run_metadata.md` and related audit files. Do show reader-facing conclusion status, material limitations, and missing checks needed for a final personalized decision.
- If the user says "run all agents", select all relevant workflow agents, not every configured agent. Record included/excluded agents and reasons in audit; show them in chat only on explicit request.

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
3. Parallel or staged context work: Equity Company Analysis, Financial Statement Analysis, Sector / Industry Context, Macro Context, News, and Market Positioning where material. Macro and sector / industry are default equity modules; they may be Limited, Not material, or Skipped with reason only with an audit-recorded justification.
4. Valuation & Expectations.
5. Risk / Red Team.
6. Pre-IC evidence lock.
7. Investment Committee memo.

Required Full Cycle artifacts and modules:
- User-facing saved report: `investment_report.md`.
- Audit metadata: `audit\run_metadata.md`, `audit\sources.md` when available, `audit\intake.md`, and one handoff/report for every actually run subagent or module.
- Evidence pack / evidence readiness.
- Macro context by default for every full asset workflow.
- Sector / industry context by default for equity.
- `equity_company_analysis.md` for equity workflows.
- Financial statement analysis output when financial quality is decision-relevant.
- `valuation_expectations.md` when price/action is decision-relevant.
- `risk_red_team.md` when final action or decision-preparation is requested.
- `portfolio_fit.md` or Limited Portfolio Fit when portfolio/user context is material.
- Internal IC-stage gate-aware artifact: `decision_prep_memo.md`, `limited_ic_draft.md`, `evidence_gap_memo.md`, or `final_investment_memo.md` only when IC schemas allow it. These canonical artifact names stay in audit/internal metadata unless the user asks for technical detail.

Conditional additional reports:
- `news_catalysts.md`.
- `market_positioning.md`.
- driver dominance / market sense / implementation checks when material.

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


## 8. Codex runtime workflow-to-skill activation map

This table is the compact P1A-CODEX-02 runtime bridge between workflow selection and repo-scoped skills. Canonical workflow sequencing remains governed by the sections above; this map only tells Codex which reusable method skills to activate when a workflow requires them.

| Workflow family | Lead router / agent | Required repo skills | Conditional repo skills | Completion handoff |
|---|---|---|---|---|
| Master intake / request classification | Master Intake Router | None | Evidence Collection when facts must be checked before routing | Route selection block |
| Asset-first analysis | Asset Intake Router plus asset-class lead | Evidence Collection; Macro; asset-class skill matching the instrument | Valuation & Expectations; Risk / Red Team; News & Catalysts; Market Positioning; Macro; Portfolio Fit; Driver Dominance | Asset specialist handoff or IC-ready package |
| Equity deep dive | Equity Agent | Evidence Collection; Macro; Sector & Industry Analysis; Equity Company Analysis; Financial Statement Analysis | Valuation & Expectations; Risk / Red Team; News & Catalysts; Market Positioning; Portfolio Fit; Driver Dominance | `equity_company_analysis.md` plus downstream specialist handoffs |
| ETF / fund review | ETF Agent | Evidence Collection; Macro; ETF Analysis | Market Positioning; Portfolio Fit; Risk / Red Team; News & Catalysts | `etf_analysis.md` plus IC or portfolio-fit handoff |
| Fixed income review | Fixed Income Agent | Evidence Collection; Macro; Fixed Income Analysis | Risk / Red Team; Portfolio Fit; News & Catalysts | `fixed_income_analysis.md` plus IC handoff when requested |
| Commodity review | Commodity Agent | Evidence Collection; Macro; Commodity Analysis | Market Positioning; News & Catalysts; Risk / Red Team; Portfolio Fit | `commodity_analysis.md` plus IC handoff when requested |
| Crypto review | Crypto Agent | Evidence Collection; Macro; Crypto Analysis | Market Positioning; News & Catalysts; Risk / Red Team; Portfolio Fit | `crypto_analysis.md` plus IC handoff when requested |
| Theme / opportunity workflow | Theme / Opportunity Intake Router | Evidence Collection; Sector & Industry Analysis | Structural Winner Discovery; Market Intelligence Briefing; Macro; News & Catalysts | Theme map, candidate list, and asset-intake handoff |
| Structural winner discovery | Structural Winners Discovery Agent | Evidence Collection; Structural Winner Discovery | Sector & Industry Analysis; Driver Dominance; Market Intelligence Briefing | `structural_winners_memo.md` and `candidate_watchlist.md` |
| Direct valuation request | Valuation & Expectations Agent | Evidence Collection; Valuation & Expectations | Financial Statement Analysis; Risk / Red Team | `valuation_expectations.md`; not an IC Action |
| Direct risk request | Risk / Red Team Agent | Evidence Collection; Risk / Red Team | News & Catalysts; Macro; Valuation & Expectations | `risk_red_team_report.md`; not an IC Action |
| Market update / latest / news | Market Intelligence Agent or News & Catalysts Agent | Evidence Collection; Market Intelligence Briefing or News & Catalysts | Market Sense Hypothesis Engine; Market Positioning; Macro | Market briefing, event handoff, or Limited freshness note |
| Market sense / price-action hypothesis | Market Sense Agent | Evidence Collection; Market Sense Hypothesis Engine | Market Positioning; News & Catalysts; Macro | Hypothesis handoff; not evidence or IC replacement |
| Portfolio fit request | Portfolio Fit Agent | Evidence Collection; Portfolio Fit | Risk / Red Team; Macro; asset-class skill matching the instrument | `portfolio_fit_report.md`; exact sizing remains out of scope |
| Final IC synthesis | Investment Committee Agent | Evidence Collection; Investment Committee Synthesis | Valuation & Expectations; Risk / Red Team; Portfolio Fit; other material specialists | Internal `final_investment_memo.md` only when gates are complete; saved user-facing Full Cycle output remains `investment_report.md` |

## 9. Update workflow

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

## 10. Completion rules

A workflow is Complete only when required reports and evidence readiness are sufficient for the requested scope.

A workflow is Limited when it can answer the request with material limitations.

A workflow is Blocked when decision-critical evidence or required upstream analysis is missing.

A workflow is Preliminary when it is a narrow scan, early read, or direct specialist output that cannot support final action.

## 11. P4-RTE-01 routing edge-case behavior

These decisions canonicalize master, asset, theme, comparison, market, update, and direct-specialist routing behavior. They apply the master rules, architecture boundaries, and evidence-layer constraints; they do not override those documents.

| Rule ID | Case | Canonical behavior | Allowed output/status | Escalation |
|---|---|---|---|---|
| P4-RTE-01-01 | Concrete-asset question asks whether to invest, buy, add, sell, start exposure, or whether the asset is worth buying for a stated horizon / portfolio decision. | Ask 5 asset-specific questions, then route to asset-first Full Cycle by default; use relevant delegated subagents when available; record Runtime Execution Plan in `audit\run_metadata.md`; hide runtime blocks in ordinary chat. Quick Take is allowed only when explicitly requested as short / fast / quick take / no full cycle / preliminary. | Full Cycle output with Complete/Limited/Blocked status as gates permit; missing portfolio context internally defaults to `decision_prep_memo.md`; no final positive `IC Action` unless all gates pass. | If the user explicitly asks for Quick Take, ask 3 questions and provide Preliminary/Limited chat-only Quick Take; otherwise complete or visibly downgrade the delegated/default Full Cycle checklist. |
| P4-RTE-01-02 | User asks what to do with their position or uses personal-position language. | Treat as personal / position-specific decision support and ask only the minimum missing context before final personalization. | Preliminary scenario view until current position, horizon, risk/objective, and approximate exposure are known. | With enough context, route to Portfolio Fit and, when action is requested, IC workflow. |
| P4-RTE-01-03 | Ticker, listing, instrument, wrapper, share class, currency, maturity, or exposure is ambiguous. | Use a safe default with an explicit instrument assumption when obvious; ask clarification when ambiguity can materially change the conclusion. | Preliminary or Limited until identity is verified for decision-critical outputs. | Final, IC, or portfolio-specific outputs require identity check before conclusion. |
| P4-RTE-01-04 | Theme / opportunity request could be read as a buy list. | Route to Theme / Opportunity workflow and label results as discovery, candidate watchlist, or review priority, not buy ranking. | Discovery Ranking / Candidate Watchlist; not an IC Action. | User may select 1-3 candidates for asset-first review and IC synthesis. |
| P4-RTE-01-05 | Comparison request asks "what is better" without criteria. | Route to comparison workflow using default criteria and scenario winners rather than one absolute winner. | Scenario comparison; base-case winner only as Preliminary or after sufficient evidence, valuation, and risk. | Final cross-asset selection or allocation requires relevant asset-class work plus IC synthesis. |
| P4-RTE-01-06 | Direct specialist request implies buy/sell/hold. | Route to the requested specialist and provide scoped verdict plus decision implication. | Specialist Verdict with `Boundary: Not an IC Action`; list missing IC gates; no Action Box. | If final action is requested, offer or route to full decision workflow. |
| P4-RTE-01-07 | Market update / price-action request mixes facts, rumors, and signals. | Route to Market Sense, Market Intelligence, or News & Catalysts with a short summary plus separated facts, rumors, market-implied signals, cross-checks, hypothesis, and confidence. | Market reaction note; Preliminary or Limited when driver support is weak. | If the move changes actionability, route refreshed evidence to asset workflow and IC gates. |
| P4-RTE-01-08 | Fresh data is required but unavailable, stale, or not refreshed. | Provide structural or scenario analysis using last available timestamp where useful; do not pretend current data is available. | Limited structural view or Blocked current-action status. | Refresh decision-critical price, news, earnings, valuation, flow, spread, or liquidity data before current entry/action. |
| P4-RTE-01-09 | Material evidence sources conflict. | Apply source hierarchy, materiality, and recency/event timing; show material conflict when it affects conclusions. | Limited or Blocked if conflict is decision-critical; otherwise limitations note. | Resolve through targeted evidence request or refreshed source hierarchy review. |
| P4-RTE-01-10 | User asks for sizing, allocation, or "how much to buy". | Without portfolio context, provide only scenario-based ranges; with approximate context, route to Portfolio Fit. | Generic scenario ranges or Personalized Portfolio Fit support; no exact trade instruction. | Concentrated or high-risk exposure triggers Portfolio Fit and Risk gates before strong conclusions. |
| P4-RTE-01-11 | User asks to update a prior memo or prior thesis. | Use true delta-update only when prior memo/thesis is available; otherwise label as fresh/current analysis. | Delta-update when prior exists; otherwise Limited fresh analysis with disclaimer. | Material action impact routes to renewed evidence collection and IC review. |
| P4-RTE-01-12 | User asks for final memo/action before required gates are complete. | Do not issue `final_investment_memo.md` or positive IC Action. Produce gate-aware non-final artifact by default. | `Limited IC Draft`, `Preliminary Investment Brief`, `Evidence Gap Memo`, or `Decision-Prep Memo`. | If closing gates is costly or broad, ask whether to proceed with draft or complete gates first. |
| P4-RTE-01-13 | User says "run all agents". | Interpret as all relevant workflow agents, not literally every system agent; use `Delegated Full Agent Workflow` for relevant agents when actually spawned. | Workflow audit plan records execution mode, included/excluded agents or modules, and handoff requirements; ordinary chat shows these only if requested; Complete or positive IC Action Status only when all required gates pass. | Exhaustive panel may be offered, but irrelevant agents remain excluded, subagents must not be claimed unless actually spawned, and IC gates still govern action. |
| P4-RTE-01-14 | Complex or nonstandard product: leveraged/inverse ETF, option, structured note, HY bond, crypto yield, VIX-like product. | If educational, explain mechanics and risks; if action-oriented, route through enhanced structure, risk, and implementation gates. | Educational explainer or Limited enhanced decision workflow. | Positive action requires product mechanics, liquidity/implementation, risk, and relevant asset exposure gates. |
| P4-RTE-01-15 | Time horizon is missing. | Infer horizon from wording when clear; otherwise split short-term and long-term views. | Preliminary or Limited split-horizon output. | Final IC Action and personal decision support require explicit Time Horizon. |
| P4-RTE-01-16 | User restricts sources or asks not to refresh. | Respect the requested source scope and make the scope visible. | `Limited by source scope` when excluded checks are material; no unsupported full IC action. | List excluded decision-critical checks needed to upgrade analysis. |
| P4-RTE-01-17 | Risk / Red Team is negative while other blocks are positive. | Risk may create `Risk Gate: Failed`; IC remains final synthesis owner. | `Risk Gate: Failed`; `IC Action Status: Limited` or `Blocked`; no positive IC Action. | Resolve risk issue or route to IC for Limited/Blocked synthesis that shows the conflict. |
| P4-RTE-01-18 | Asset quality is strong but valuation / expectations support is weak. | Separate Quality Verdict from Valuation / Expectations Support and investment action. | Watchlist / Defer / entry-trigger framing as non-IC signal unless IC issues final action. | Positive IC Action requires valuation/expectations support or explicit IC treatment of the constraint. |
| P4-RTE-01-19 | Asset lacks classic cash-flow valuation. | Use asset-class valuation / expectations equivalent; avoid inappropriate DCF or multiples. | Limited valuation support when anchor is weak or proxy-heavy. | Weak anchors require stronger Risk review before any positive action. |
| P4-RTE-01-20 | One request contains multiple workflows. | Choose a primary route by main user intent and add only necessary supporting modules. | Scoped output with assumptions, excluded blocks, maximum status, and prohibited conclusions. | If scope is too broad, ask whether user wants Quick Take or full workflow before proceeding. |

Manual verification checklist:

- Stable IDs `P4-RTE-01-01` through `P4-RTE-01-20` are present with no gaps.
- Every rule identifies deterministic routing, safe fallback, allowed status, and escalation path.
- Routers do not issue final investment views or `IC Action`.
- Direct specialist, discovery, market reaction, and portfolio-fit routes preserve `Boundary: Not an IC Action` where relevant.
- Final action routes preserve evidence, valuation/expectations, risk, implementation, and IC gates.
