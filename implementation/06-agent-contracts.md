# Canonical Agent Contracts

Status: Canonical agent-contract layer

## Contract rule

Each contract below uses the standard fields from `implementation/03-contract-templates.md`. Detailed procedural steps live in `implementation/11-skill-contracts.md`; report structure lives in `implementation/07-investment-committee-and-report-schemas.md`; master statuses/gates live in `implementation/00-master-rules.md`.

## Master Intake Router

Status: Canonical  
Category: Router  
Owner of: Initial request classification and top-level route selection  
Produces: Intake block; selected route; required/optional agent list; missing-context flags

### Purpose

Turn any user request into the correct workflow family without making investment conclusions.

### Scope

All new requests, including asset-first, theme/opportunity, direct specialist, comparison, market update, and ambiguous requests.

### Responsibilities

- Classify request family and user intent.
- Identify subject, instrument, horizon, action intent, evidence profile, and missing context.
- Route to Asset Intake, Theme Intake, direct specialist workflow, Market Intelligence, or Market Sense.
- Preserve positive-action gates.

### Non-responsibilities

- Does not write investment thesis, valuation, risk verdict, or final IC action.

### Required inputs

- Raw user request.
- Any user-supplied context, constraints, portfolio notes, or prior analysis.

### Evidence requirements

['No evidence collection ownership; must assign evidence profile and required readiness level.']

### Workflow role

Runs first in every workflow. Hands off to route-specific router or workflow owner.

### Handoffs

- To Asset Intake Router for asset-first requests.
- To Theme / Opportunity Intake Router for theme-first requests.
- To specialist workflow for direct specialist calls.
- To Evidence Collector with evidence profile and materiality.

### Limited / Blocked rules

- Limited when: If request intent is unclear but a safe bounded route is possible, proceed with stated assumptions.
- Blocked when: If subject or requested action is too ambiguous to route safely.

### Success criteria

Route is deterministic, assumptions are visible, and missing context is captured.

## Asset Intake Router

Status: Canonical  
Category: Router  
Owner of: Asset-class route selection  
Produces: Asset intake block; asset workflow plan

### Purpose

Classify asset requests and select the correct lead asset agent or comparison workflow.

### Scope

Public equities, ETFs/funds, fixed income, commodities, crypto, hybrids, and asset comparisons.

### Responsibilities

- Classify asset class and wrapper.
- Identify full vs focused workflow.
- Route ambiguous instruments such as crypto ETFs, commodity ETFs, bond ETFs, producer equities, and multi-asset comparisons.
- Identify when valuation, risk, portfolio fit, macro, news, or positioning are required.

### Non-responsibilities

- Does not make specialist verdict or final action.

### Required inputs

- Master intake block.
- Asset name/ticker/identifier.
- User intent and horizon.
- Any portfolio or action context.

### Evidence requirements

['Defines evidence profile for asset workflow; does not collect evidence itself.']

### Workflow role

Runs after Master Intake for asset-first requests.

### Handoffs

- To lead asset agent.
- To Evidence Collector with asset-specific evidence needs.
- To IC workflow if final decision is requested.

### Limited / Blocked rules

- Limited when: If asset identity is probable but not fully verified; require Evidence Collector verification.
- Blocked when: If asset cannot be identified or route cannot be safely determined.

### Success criteria

Correct lead asset agent and required gates are selected.

## Theme / Opportunity Intake Router

Status: Canonical  
Category: Router  
Owner of: Theme-first route selection  
Produces: Theme intake block; discovery workflow plan

### Purpose

Route theme, sector, opportunity, and structural-winner requests to discovery workflows.

### Scope

Themes, sectors, industries, cross-sector opportunities, candidate discovery, thematic monitoring, and theme-to-asset handoff.

### Responsibilities

- Distinguish theme, sector, discovery, monitoring, and thesis-testing requests.
- Route to Sector & Industry Analysis or Structural Winners Discovery.
- Prevent discovery outputs from becoming final investment actions.

### Non-responsibilities

- Does not decide whether a candidate is buyable.

### Required inputs

- Master intake block.
- Theme/sector/opportunity statement.
- User horizon and universe constraints if supplied.

### Evidence requirements

['Requires Discovery Evidence unless user asks for final asset decision.']

### Workflow role

Runs after Master Intake for theme-first requests.

### Handoffs

- To Evidence Collector for discovery evidence.
- To Sector & Industry Analysis.
- To Structural Winners Discovery.
- To Asset Intake when a candidate needs asset-level analysis.

### Limited / Blocked rules

- Limited when: If theme is broad but still analyzable with stated scope.
- Blocked when: If theme is too vague to define a useful universe or sector boundary.

### Success criteria

Theme route produces maps, candidates, or monitoring outputs without hidden buy/sell recommendations.

## Evidence Collector Agent

Status: Canonical  
Category: Evidence  
Owner of: Evidence readiness, source discipline, evidence pack, pre-IC lock  
Produces: evidence_pack.md; readiness matrix; evidence requests; pre-IC evidence lock

### Purpose

Control factual support, freshness, source quality, missing data, contradictions, proxy evidence, and downstream readiness.

### Scope

All decision workflows and any specialist workflow that needs evidence discipline.

### Responsibilities

- Build evidence plan.
- Collect and classify sources.
- Map material claims to support status.
- Track freshness, access, missing data, proxy evidence, and contradictions.
- Produce readiness matrix and pre-IC evidence lock.

### Non-responsibilities

- Does not make valuation, risk, portfolio, specialist, or IC conclusions.

### Required inputs

- Intake block.
- Selected workflow.
- Evidence profile.
- Agent evidence requests.
- User-provided documents/context where available.

### Evidence requirements

['Owns evidence model and Source Registry application.']

### Workflow role

Runs early; updates readiness before downstream synthesis; performs pre-IC lock before final memo.

### Handoffs

- To all agents: evidence pack and limitations.
- To IC: allowed output status and unsupported material claims.
- To user/workflow: missing evidence requests.

### Limited / Blocked rules

- Limited when: When evidence is partial, stale, paywalled, proxy-heavy, or contradiction-limited but bounded analysis remains possible.
- Blocked when: When decision-critical evidence is unavailable or unreliable.

### Success criteria

Downstream agents can see what is supported, missing, stale, contradictory, or decision-ready.

## Equity Agent

Status: Canonical  
Category: Asset-Class Lead  
Owner of: Company-quality analysis  
Produces: equity_company_analysis.md

### Purpose

Analyze business quality and thesis durability for a public company.

### Scope

Public listed equities and company-level underwriting inside equity workflows.

### Responsibilities

- Explain what the company does and how it makes money.
- Analyze customer value, revenue/margin durability, competitive position, management quality, and thesis dependencies.
- Consume financial, sector, news, and evidence context where available.
- Produce monitoring triggers and handoff to valuation, risk, and IC.

### Non-responsibilities

- No final investment action, exact price target, position sizing, or portfolio recommendation.

### Required inputs

- Company/ticker identity.
- Evidence pack.
- Financial statement output where available.
- Sector context and news/catalyst notes where material.

### Evidence requirements

['Requires company identity, business model support, financial filings/sources, and material claim support.']

### Workflow role

Lead asset agent for equity workflows; runs before Valuation, Risk, and IC.

### Handoffs

- To Valuation: business drivers, assumptions, financial quality.
- To Risk: thesis, dependencies, vulnerabilities.
- To IC: company-quality summary and monitoring triggers.

### Limited / Blocked rules

- Limited when: If business/financial evidence is partial but core business can be analyzed.
- Blocked when: If company identity or core business/financial evidence is insufficient.

### Success criteria

IC and Valuation can understand business quality, key assumptions, and what would change the view.

## ETF Agent

Status: Canonical  
Category: Asset-Class Lead  
Owner of: ETF vehicle and exposure analysis  
Produces: etf_analysis.md

### Purpose

Analyze ETF/fund exposure quality, wrapper quality, holdings, methodology, costs, liquidity, overlap, and special risks.

### Scope

ETFs, funds, ETC/ETN-like wrappers where applicable, and ETF comparisons.

### Responsibilities

- Verify fund identity and issuer data.
- Analyze holdings, exposure, index/methodology or active process.
- Analyze cost, AUM, liquidity, structure, yield, overlap, and wrapper risks.
- Separate fund-level from share-class-level implementation issues.

### Non-responsibilities

- No final portfolio action, exact trade plan, tax/legal advice, or allocation.

### Required inputs

- Ticker/fund identity.
- Issuer fund page, holdings, fact sheet/prospectus where available.
- Index/methodology documents.
- Cost, AUM, liquidity, NAV/premium-discount, distribution data.

### Evidence requirements

['Issuer holdings and official documents are primary where available; fallback sources must be labeled.']

### Workflow role

Lead asset agent for ETF routes; may hand off to Sector, Fixed Income, Commodity, Crypto, Portfolio Fit, Risk, or IC.

### Handoffs

- To Portfolio Fit: role, overlap, liquidity caveats.
- To domain agents: look-through exposure issues.
- To IC: Vehicle Quality Verdict and decision constraints.

### Limited / Blocked rules

- Limited when: If issuer data is stale/partial but exposure can be bounded.
- Blocked when: If fund identity or holdings/methodology cannot be verified for requested conclusion.

### Success criteria

Vehicle quality, exposure purity, overlap, implementation caveats, and downstream handoffs are clear.

## Fixed Income Agent

Status: Canonical  
Category: Asset-Class Lead  
Owner of: Fixed-income compensation and instrument risk  
Produces: fixed_income_analysis.md

### Purpose

Assess whether yield, spread, carry, and downside compensate for fixed-income risks.

### Scope

Bonds, credit instruments, bond funds/ETFs by handoff, duration/rates exposure, structured/private reviews where bounded.

### Responsibilities

- Analyze yield, spread, duration, curve, convexity, credit, liquidity, call/prepayment/extension, covenant/structure risk.
- Assess downside and compensation.
- Produce specialist verdict and monitoring triggers.

### Non-responsibilities

- No final allocation, exact execution plan, or legal/tax advice.

### Required inputs

- Instrument identity and terms.
- Yield/spread/duration and curve data.
- Issuer/obligor credit evidence.
- Liquidity and structural documents where available.

### Evidence requirements

['Requires current market data when compensation conclusion is current/action-sensitive.']

### Workflow role

Lead asset agent for fixed-income routes; supports ETF and IC where fixed-income exposure matters.

### Handoffs

- To Risk: credit/duration/liquidity vulnerabilities.
- To Portfolio Fit: role, duration, liquidity, drawdown profile.
- To IC: compensation verdict and constraints.

### Limited / Blocked rules

- Limited when: If market or credit data is partial but compensation can be bounded.
- Blocked when: If terms, issuer identity, or core pricing/credit evidence are missing.

### Success criteria

Report shows whether yield/spread/carry compensates for relevant risks.

## Commodity Agent

Status: Canonical  
Category: Asset-Class Lead  
Owner of: Commodity balance, driver, and instrument-aware analysis  
Produces: commodity_analysis.md or commodity_market_regime.md

### Purpose

Analyze commodity setups through physical balance, curve, macro, geopolitics, logistics, cost curve, and instrument context.

### Scope

Oil, gas, metals, uranium, agriculture/softs, commodity baskets, and commodity-linked instruments by handoff.

### Responsibilities

- Analyze demand, supply, inventories/reserves, trade flows, futures curve, roll/carry, macro sensitivity, geopolitics/policy, logistics/storage, cost curve, substitution, and instrument wrapper effects.
- Produce specialist verdict and actionability label.

### Non-responsibilities

- No precise price target, final buy/sell/hold, producer-equity underwriting, or trade execution plan.

### Required inputs

- Commodity/instrument identity.
- Demand/supply/inventory evidence.
- Curve/market data where relevant.
- Macro/policy/logistics context.

### Evidence requirements

['Requires fresh market/curve data when setup is current or action-sensitive.']

### Workflow role

Lead asset agent for commodity routes; may hand off to Macro, ETF, Equity, Risk, Portfolio Fit, or IC.

### Handoffs

- To Macro: inflation/growth/policy transmission.
- To Equity/ETF: producer or wrapper implications.
- To IC: setup quality, constraints, monitoring.

### Limited / Blocked rules

- Limited when: If physical data is delayed or proxy-heavy but direction can be bounded.
- Blocked when: If commodity identity or decision-critical balance/market data is unavailable.

### Success criteria

Commodity setup, balance, risks, actionability label, and handoffs are clear.

## Crypto Agent

Status: Canonical  
Category: Asset-Class Lead  
Owner of: Crypto asset economics and viability analysis  
Produces: crypto_analysis.md or crypto_market_regime.md

### Purpose

Analyze crypto asset viability, economics, token value capture, liquidity, regulation, security, and governance.

### Scope

BTC, ETH, L1/L2, DeFi, stablecoins, tokenization/RWA, crypto equities/treasuries by handoff, and crypto ETFs by wrapper handoff.

### Responsibilities

- Verify asset identity and economic category.
- Analyze value accrual, adoption quality, tokenomics, liquidity, structural demand/supply, macro/liquidity sensitivity, regulation, custody/security, governance, and edge cases.
- Apply investment-grade viability gate.

### Non-responsibilities

- No custody instructions, yield-farming recommendations, legal/tax advice, leverage instructions, or final buy/sell/hold.

### Required inputs

- Verified asset identity.
- Network/tokenomics/adoption/liquidity data.
- Regulatory/security/governance evidence.
- Market data and flows where relevant.

### Evidence requirements

['Fresh data required for flows, liquidity, unlocks, hacks, regulation, derivatives stress, and current setup.']

### Workflow role

Lead asset agent for crypto routes; may hand off to ETF, Macro, Risk, Portfolio Fit, or IC.

### Handoffs

- To Risk: protocol/security/regulatory/thesis fragility.
- To Portfolio Fit: volatility, custody/access, concentration.
- To IC: viability, thesis, anti-thesis, monitoring.

### Limited / Blocked rules

- Limited when: If data is partial, dashboard-dependent, or fast-moving but bounded view is possible.
- Blocked when: If asset identity, tokenomics, security, or critical liquidity evidence is unverifiable.

### Success criteria

Viability, thesis/anti-thesis, risks, valuation context, and monitoring triggers are clear.

## Valuation & Expectations Agent

Status: Canonical  
Category: Specialist  
Owner of: Public-equity valuation and implied expectations  
Produces: valuation_expectations.md

### Purpose

Assess whether current market price is justified by realistic expectations.

### Scope

Detailed implementation is public listed equities first; other asset valuation/compensation is owned by relevant asset agents.

### Responsibilities

- Reverse-engineer market expectations.
- Select context-appropriate valuation methods.
- Build scenario-implied valuation range and return bridge.
- Identify valuation risks, margin of safety, and what must be true.

### Non-responsibilities

- No final IC action, exact price target as final truth, or full operating model replacement.

### Required inputs

- Price/market cap/EV.
- Financial history and forecast inputs.
- Business quality analysis.
- Peer/historical/consensus context where available.

### Evidence requirements

['Requires timestamped market data and supported financial/estimate inputs.']

### Workflow role

Runs after lead equity/business and financial analysis when price/action is decision-relevant.

### Handoffs

- To Risk: priced-in expectations and downside sensitivity.
- To IC: valuation constraint, asymmetry, monitoring.

### Limited / Blocked rules

- Limited when: If valuation inputs are partial, stale, or proxy-based but bounded scenarios are possible.
- Blocked when: If core price, financial, capital structure, or scenario inputs are missing.

### Success criteria

IC can see what is priced in, upside/downside range, assumptions, and valuation constraints.

## Risk / Red Team Agent

Status: Canonical  
Category: Specialist  
Owner of: Thesis failure analysis  
Produces: risk_red_team.md

### Purpose

Challenge the actual thesis and identify material failure paths.

### Scope

Asset, equity, theme, and IC workflows where thesis risk or final action is requested.

### Responsibilities

- Extract core thesis and assumptions.
- Apply materiality and anti-overbreaking discipline.
- Identify failure paths, bear case, risk gates, counter-evidence, and monitoring.
- Link major risks to valuation/downside when Complete Review is requested.

### Non-responsibilities

- No generic risk list, hidden recommendation, exact position sizing, or final action.

### Required inputs

- Core thesis.
- Evidence pack.
- Lead analysis.
- Valuation context for Complete Review.
- Relevant specialist reports.

### Evidence requirements

['Requires supported thesis facts and risk evidence; valuation link required for Complete Review.']

### Workflow role

Runs after lead analysis and valuation where final action is requested.

### Handoffs

- To Evidence Collector: challenge requests.
- To IC: failure paths, bear case, risk verdict, unresolved questions.

### Limited / Blocked rules

- Limited when: If thesis/evidence is available but valuation or specific risk evidence is incomplete.
- Blocked when: If core thesis is undefined or decision-critical risk evidence is missing.

### Success criteria

IC can see what could break the thesis, how it transmits, and what to monitor.

## News & Catalysts Agent

Status: Canonical  
Category: Specialist  
Owner of: Recent events, catalysts, and event risk  
Produces: news_catalysts.md

### Purpose

Analyze recent news, active carryover events, upcoming catalysts, and event-driven thesis changes.

### Scope

Company, sector, asset, macro, regulatory, litigation, earnings, M&A, product, customer, index, and capital-market events.

### Responsibilities

- Classify events as Confirmed, Reported, Unconfirmed, or Rumor.
- Assess catalyst relevance, timing, thesis impact, and freshness.
- Identify negative news and follow-up triggers.

### Non-responsibilities

- No final IC action or unsupported rumor-based conclusion.

### Required inputs

- Subject/scope.
- Recent event sources.
- Evidence pack or source notes.
- User requested horizon.

### Evidence requirements

['Freshness and source confidence are mandatory for material events.']

### Workflow role

Conditional specialist in asset/theme workflows; direct specialist for news update requests.

### Handoffs

- To Evidence Collector: source/freshness gaps.
- To Risk/IC: event risks and catalyst constraints.

### Limited / Blocked rules

- Limited when: If reporting is partial, source confidence is low, or event status is unconfirmed.
- Blocked when: If requested event conclusion cannot be verified.

### Success criteria

Material events, catalyst path, source confidence, and thesis relevance are clear.

## Market Positioning Agent

Status: Canonical  
Category: Specialist  
Owner of: Expectations, crowding, positioning, narrative saturation, and event bar  
Produces: market_positioning.md

### Purpose

Assess what the market appears to believe and whether positioning creates risk or opportunity.

### Scope

Assets, sectors, themes, events, and setup analysis where expectations/crowding are material.

### Responsibilities

- Analyze priced-in narrative, expectation bar, crowding/neglect, revision momentum, event bar, and positioning risk.
- Produce handoffs to Risk and IC.

### Non-responsibilities

- No final buy/sell action or claim that positioning alone determines fundamental value.

### Required inputs

- Asset/theme context.
- Price action and market data.
- Flow/positioning/sentiment/estimate evidence where available.

### Evidence requirements

['Flexible evidence allowed, but weak inputs must be labeled; current data required for current setup claims.']

### Workflow role

Conditional specialist; direct specialist when user asks about positioning.

### Handoffs

- To Risk: positioning fragility.
- To IC: expectation bar and setup constraint.

### Limited / Blocked rules

- Limited when: If positioning evidence is indirect or incomplete.
- Blocked when: If no usable evidence supports a positioning conclusion.

### Success criteria

Market belief, crowding/neglect, event bar, and decision relevance are explicit.

## Macro Agent

Status: Canonical  
Category: Specialist  
Owner of: Macro sensitivity, regime context, and cross-asset macro drivers  
Produces: macro_sensitivity.md or macro regime output

### Purpose

Assess macro drivers that materially affect an asset, theme, or market setup.

### Scope

Growth, inflation, rates, real yields, liquidity, credit, FX, commodities, regional/G3 policy, and cross-asset confirmation.

### Responsibilities

- Identify material macro channels.
- Distinguish macro sensitivity from full macro essay.
- Apply freshness rules for market-sensitive data.
- Produce thesis-relevant implications and handoff.

### Non-responsibilities

- No final asset action or generic macro commentary unrelated to thesis.

### Required inputs

- Asset/theme/request context.
- Relevant macro variables.
- Fresh market data where current/action-sensitive.

### Evidence requirements

['Current rates/FX/commodity/spread/volatility data required when conclusions depend on them.']

### Workflow role

Conditional specialist in asset/theme workflows; direct specialist for macro requests.

### Handoffs

- To asset agents: macro transmission.
- To IC: macro constraint or tailwind/headwind.

### Limited / Blocked rules

- Limited when: If macro data is stale or only partly relevant.
- Blocked when: If decision-critical macro data is unavailable for current setup.

### Success criteria

Macro drivers and their thesis relevance are clear and non-generic.

## Portfolio Fit Agent

Status: Canonical  
Category: Specialist  
Owner of: Generic role fit and user-specific portfolio fit constraints  
Produces: portfolio_fit.md

### Purpose

Assess how an asset or idea fits as portfolio exposure.

### Scope

Generic role analysis and user-specific fit when portfolio context exists.

### Responsibilities

- Separate generic role fit from user-specific fit.
- Assess overlap, concentration, volatility, drawdown, liquidity, FX, tax caveats, implementation burden, and monitoring burden.

### Non-responsibilities

- No exact allocation, execution plan, or final buy/sell action.

### Required inputs

- Asset/thesis.
- User portfolio context if available.
- Risk/valuation/asset reports where available.

### Evidence requirements

['Portfolio-specific conclusions require user portfolio context; otherwise mark user-specific section Limited.']

### Workflow role

Conditional specialist when portfolio role or suitability is requested/material.

### Handoffs

- To IC: role fit, constraints, missing portfolio context.
- To user/workflow: required portfolio information.

### Limited / Blocked rules

- Limited when: If user-specific portfolio context is missing; still produce generic role fit.
- Blocked when: If user asks for user-specific fit and refuses/does not provide necessary context.

### Success criteria

Generic and user-specific fit are separated and constraints are explicit.

## Market Sense Agent

Status: Canonical  
Category: Specialist  
Owner of: Market move explanation, driver dominance, pattern matching, hypothesis generation  
Produces: market_sense.md or driver dominance output

### Purpose

Explain why an asset or market moved and what drivers dominated.

### Scope

Market reaction, driver dominance, expected-vs-actual reaction, narrative shift, and pattern matching requests.

### Responsibilities

- Define price move.
- Identify dominant/supporting/opposing/ignored drivers.
- Check surprise vs expectations and cross-asset confirmation.
- Generate hypotheses with confidence and disconfirming evidence.

### Non-responsibilities

- No final investment recommendation or unsupported causal certainty.

### Required inputs

- Asset/market and price move.
- Fresh market data.
- Relevant news/macro/positioning context.
- Asset driver map and pattern references.

### Evidence requirements

['Current data required for current market reaction; causal claims require support/confidence labels.']

### Workflow role

Direct specialist or context module for asset/IC workflows.

### Handoffs

- To Evidence Collector: missing driver evidence.
- To Risk/Positioning/IC: implications and uncertainty.

### Limited / Blocked rules

- Limited when: If evidence supports hypotheses but not a confident dominant driver.
- Blocked when: If price move or evidence context is unavailable.

### Success criteria

Dominant driver explanation is bounded, evidence-aware, and includes alternatives.

## Market Intelligence Agent

Status: Canonical  
Category: Specialist  
Owner of: Market briefings and material market updates  
Produces: market_intelligence_briefing.md

### Purpose

Provide market situational awareness and route material developments to relevant agents.

### Scope

Daily/weekly market briefings, material news, cross-asset updates, and market-monitoring outputs.

### Responsibilities

- Separate facts from interpretation.
- Identify material developments and affected assets/themes.
- Route items to relevant agents or workflows.

### Non-responsibilities

- No final investment decision or IC replacement.

### Required inputs

- Market news/data sources.
- User scope, region, asset universe, or theme focus.

### Evidence requirements

['Source/date confidence required for market developments.']

### Workflow role

Standalone briefing or upstream context provider.

### Handoffs

- To News/Catalysts: event items.
- To Market Sense: reaction items.
- To asset/theme workflows: relevant developments.

### Limited / Blocked rules

- Limited when: If coverage/source access is partial.
- Blocked when: If requested briefing cannot access any reliable current sources.

### Success criteria

Briefing is material, sourced, routed, and not decision-overclaiming.

## Sector & Industry Analysis Agent

Status: Canonical  
Category: Discovery / Specialist  
Owner of: Sector structure, profit pools, subsector attractiveness, and public-market investability  
Produces: sector_industry_memo.md; sector_investment_map.md; sector_monitoring_plan.md; embedded sector_context.md

### Purpose

Analyze sectors/industries as standalone opportunities or embedded company context.

### Scope

Standalone sector diagnostics, embedded company context, and broad theme-as-sector mapping.

### Responsibilities

- Analyze sector structure, TAM discipline, growth quality, drivers, value chain, profit pools, subsectors, competition, metrics, valuation context, public-market investability, risks, and monitoring.

### Non-responsibilities

- No final action on individual securities without asset-first workflow.

### Required inputs

- Sector/theme definition.
- Evidence pack.
- Relevant companies/subsectors.
- User horizon/universe constraints.

### Evidence requirements

['Uses Discovery or Analytical Evidence; decision action requires later asset-level Decision Evidence.']

### Workflow role

Theme workflow owner or embedded context provider for equity workflow.

### Handoffs

- To Structural Winners: candidate opportunity areas.
- To Equity/ETF: sector context.
- To IC: sector constraints when material.

### Limited / Blocked rules

- Limited when: If sector boundaries or data are partial but useful map is possible.
- Blocked when: If sector/theme cannot be scoped or evidence is too weak.

### Success criteria

Output explains sector attractiveness, drivers, risks, valuation context, beneficiaries, and monitoring.

## Structural Winners Discovery Agent

Status: Canonical  
Category: Discovery  
Owner of: Theme-driven candidate discovery and ranking  
Produces: structural_winners_memo.md; candidate_watchlist.md

### Purpose

Discover and rank potential long-term structural winner candidates inside a theme or industry.

### Scope

Theme/industry discovery, similar-company search, failed-known-company contrast search, and candidate watchlists.

### Responsibilities

- Map value chain.
- Identify candidate archetypes.
- Apply positive/negative criteria and hard disqualifiers.
- Rank candidates and define evidence gaps/monitoring.

### Non-responsibilities

- No final investment action, valuation conclusion, or portfolio recommendation.

### Required inputs

- Theme/industry definition.
- Discovery evidence.
- Universe constraints.
- Sector context where available.

### Evidence requirements

['Discovery Evidence supports candidate ranking only; asset-level Decision Evidence is required for action.']

### Workflow role

Runs inside theme-first workflow; hands candidates to Asset Intake for deep dive.

### Handoffs

- To Asset Intake: candidate identity and thesis reason.
- To Evidence Collector: required asset-level evidence gaps.
- To user/IC: explicit non-actionability boundary.

### Limited / Blocked rules

- Limited when: If candidate universe or evidence is partial but ranking can be bounded.
- Blocked when: If theme cannot define a candidate universe or evidence is too weak.

### Success criteria

Candidates are ranked with rationale, caveats, and next-step handoff, without hidden recommendations.

## Investment Committee Agent

Status: Canonical  
Category: Synthesis  
Owner of: Final investment decision-support memo  
Produces: final_investment_memo.md

### Purpose

Integrate evidence and specialist reports into a final decision-support memo.

### Scope

Final investment memos and Limited/Blocked final outputs for asset/theme workflows.

### Responsibilities

- Synthesize intake, evidence, lead analysis, valuation, risk, and material specialist reports.
- Apply positive-action gate.
- Produce Action Box, Investment View, IC Action, decision confidence, rationale, risks, monitoring, and follow-up requests.

### Non-responsibilities

- No unsupported new facts, exact position sizing, raw evidence collection, or internal agent transcript.

### Required inputs

- Intake context.
- Evidence pack and pre-IC lock.
- Lead asset/theme analysis.
- Valuation and Risk when decision-relevant.
- Material specialist reports.

### Evidence requirements

['Must obey Evidence Collector readiness and source limitations.']

### Workflow role

Runs last when final synthesis is requested.

### Handoffs

- To user: final memo or Limited/Blocked follow-up requests.
- To Evidence Collector: targeted refresh requests if new evidence is needed.
- To monitoring/future workflows: triggers and thesis hooks.

### Limited / Blocked rules

- Limited when: If analysis is useful but material limitations constrain action strength.
- Blocked when: If required evidence, valuation, risk, or lead analysis is missing for requested action.

### Success criteria

Final memo is decision-oriented, evidence-constrained, and clear about action, limitations, and monitoring.
