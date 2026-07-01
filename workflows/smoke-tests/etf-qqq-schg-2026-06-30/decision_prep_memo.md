# decision_prep_memo.md - QQQ vs SCHG for long-term U.S. growth exposure

## Handoff metadata
- Artifact: `decision_prep_memo.md`
- Subject: QQQ vs SCHG for long-term U.S. growth exposure
- Owner: Investment Committee Agent
- Producing agent/skill/workflow: Investment Committee Agent / investment-committee-synthesis skill
- Workflow: ETF internal full workflow smoke test
- Execution mode: Agent workflow with spawned subagents
- As-of date/time: 2026-06-30
- Output status: Limited
- Evidence status: Limited; public sources and spawned-subagent handoffs support decision preparation but not final IC Action
- Freshness status: Mixed; enough for smoke-test decision preparation, not final evidence lock
- Source scope: Public sources only
- Evidence limits: No user portfolio, incomplete current QQQ holdings export, no full valuation bridge, no complete flow/positioning dataset, no tax/access review
- Key limitations: Portfolio Fit is not personalized; valuation, risk, implementation, and evidence-lock gates remain Limited
- Missing gates: Portfolio context; pre-IC evidence lock; valuation/expectations bridge; risk stress; implementation review; macro/positioning/news refresh
- Decision boundary: IC-stage decision-preparation artifact only; no final IC Action
- Downstream handoff: To final memo only after missing gates are closed
- Required follow-up: Close portfolio context, refresh evidence, complete valuation/risk/implementation checks, then rerun IC synthesis

## IC metadata
- Analysis Status: Limited
- IC Action Status: Limited
- Decision Confidence: Not Rateable for final action; Medium-Low for working comparison

## Runtime Execution Plan

Execution mode: `Agent workflow with spawned subagents`.

The ETF smoke test actually spawned route-relevant subagents and consumed their handoff summaries. The final artifact is `decision_prep_memo.md` because the smoke test has no portfolio context and several IC gates remain Limited.

| Module | Status | Basis / limitation |
|---|---:|---|
| Master Intake Router | Complete | ETF comparison route identified. |
| Asset Intake Router | Complete | QQQ and SCHG routed as U.S.-listed equity ETFs. |
| Evidence Collector | Limited | Official identity/fee evidence collected; QQQ current holdings export and full liquidity refresh remain Limited. |
| ETF Agent | Limited | Wrapper and exposure comparison completed; full implementation review not complete. |
| Valuation & Expectations | Limited | Growth-equity expectations framed; no full holdings-level valuation bridge. |
| Risk / Red Team | Limited | Concentration, rate, AI, drawdown, and crowding risks identified; full stress test not complete. |
| Portfolio Fit | Limited | Generic role only; no user portfolio. |
| Macro | Limited | Structural rate/liquidity sensitivity only. |
| Market Positioning | Limited | Crowding/flows are proxy-heavy. |
| News & Catalysts | Complete | Scoped catalyst handoff completed. |
| Market Sense | Limited | Driver map only; no exact move window. |
| Market Intelligence | Limited | Context briefing only; full flow tape not validated. |
| Sector Context | Complete | Sector/profit-pool context completed. |
| IC Synthesis | Limited | Non-final decision-prep artifact only. |

## Decision-Prep Box

- IC Action Status: Limited.
- Final action: Not authorized.
- Working view: QQQ is the more concentrated Nasdaq-100 / liquidity / AI-beta expression; SCHG is the broader and lower-cost U.S. large-cap growth expression.
- Why not final: no portfolio context, no final evidence lock, incomplete valuation/risk/positioning/implementation gates.

## Consumed handoff artifacts

- `evidence_pack.md`
- `etf_analysis.md`
- `valuation_expectations.md`
- `risk_red_team.md`
- `portfolio_fit.md`
- `macro_sensitivity.md`
- `market_positioning.md`
- `news_catalysts.md`
- `market_sense.md`
- `market_intelligence_briefing.md`
- `sector_context.md`

## Working synthesis

For a long-term U.S. growth sleeve, QQQ and SCHG are both viable ETF wrappers but serve different roles. QQQ is more appropriate when the desired exposure is explicit Nasdaq-100 concentration, deep trading liquidity, and higher sensitivity to AI/technology leadership. SCHG is more appropriate when the desired exposure is broader U.S. large-cap growth at lower cost. This is a role comparison, not a final recommendation.

The dominant shared risk is that both exposures remain concentrated in the same mega-cap growth and AI/platform complex. The portfolio value of either ETF depends heavily on existing U.S. equity, S&P 500, technology, semiconductor, and single-stock exposure.

## Missing gates before final memo

| Gate | Status | Minimum follow-up |
|---|---:|---|
| Portfolio context | Limited | Provide current holdings, objective, risk tolerance, tax/account constraints, and concentration limits. |
| Evidence lock | Limited | Refresh official holdings, liquidity, spreads, tracking, and source conflicts. |
| Valuation | Limited | Build holdings-level valuation and growth-expectations bridge. |
| Risk | Limited | Run drawdown, rate, concentration, crowding, and overlap stress tests. |
| Implementation | Limited | Check account access, tax treatment, spreads, premium/discount, and trading needs. |

## Decision-prep scenario logic

| Scenario | What would support it | What would break it | IC implication |
|---|---|---|---|
| QQQ higher-conviction growth exposure | Nasdaq-100 mega-cap growth leadership persists, liquidity remains supportive, concentration risk is acceptable | Growth multiple compression, mega-cap crowding unwind, sector concentration shock | Requires portfolio overlap and valuation gates before final IC action |
| SCHG broader/cheaper growth exposure | Lower fee, broader holdings, and less index-specific concentration matter more than Nasdaq-100 purity | QQQ leaders keep outperforming and SCHG breadth dilutes upside | Decision-prep only without portfolio context |
| Neither final-action ready | Holdings, valuation, overlap, and portfolio context remain incomplete | Fresh holdings/valuation/portfolio data close gates | Keep output as `decision_prep_memo.md` |

## Consumed module synthesis

- Evidence supports fund identity and high-level fee/exposure comparison, while current holdings overlap and same-day liquidity require refresh.
- ETF analysis separates wrapper quality from exposure choice.
- Valuation, risk, macro, positioning, news, market-sense, market-intelligence, sector context, and portfolio-fit modules all remain gate-aware inputs rather than final action owners.
- IC synthesis remains Limited because portfolio context and several current-data gates are not fully closed.

## Structured handoff
- Artifact: `decision_prep_memo.md`
- Subject: QQQ vs SCHG for long-term U.S. growth exposure
- Scope: IC-stage decision preparation for ETF smoke-test route
- Owner: Investment Committee Agent
- Producing agent/skill/workflow: Investment Committee Agent / investment-committee-synthesis skill
- Workflow: ETF internal full workflow smoke test
- Execution mode: Agent workflow with spawned subagents
- As-of date/time: 2026-06-30
- Output status: Limited
- Evidence status: Limited; public sources and spawned-subagent handoffs support decision preparation but not final IC Action
- Freshness status: Mixed; enough for smoke-test decision preparation, not final evidence lock
- Source scope: Public sources only
- Evidence limits: No user portfolio, incomplete current QQQ holdings export, no full valuation bridge, no complete flow/positioning dataset, no tax/access review
- Key limitations: Portfolio Fit is not personalized; valuation, risk, implementation, and evidence-lock gates remain Limited
- Key findings: QQQ = concentrated Nasdaq-100/liquidity/AI-beta wrapper; SCHG = broader lower-cost large-cap growth wrapper; both overlap heavily in mega-cap growth
- Missing gates: Portfolio context; pre-IC evidence lock; valuation/expectations bridge; risk stress; implementation review; macro/positioning/news refresh
- Decision boundary: IC-stage decision-preparation artifact only; no final IC Action
- Decision constraints: No final buy/sell/hold/add/trim/exit; no exact allocation; no Action Box
- Downstream handoff: To final memo only after missing gates are closed
- Required follow-up: Close portfolio context, refresh evidence, complete valuation/risk/implementation checks, then rerun IC synthesis
