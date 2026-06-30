# Asset Intake Router PRD

## 1. Purpose

The Asset Intake Router handles asset-first requests after the Master Intake Router has classified a request as involving a specific asset, instrument, or asset comparison.

Its purpose is to determine the correct asset-class route, collect the minimum useful context, identify whether the request is full or focused, and launch the appropriate asset workflow.

## 2. Core Question

```text
What asset or instrument is being analyzed, what decision is the user trying to make, and which asset-specific route should run?
```

## 3. Asset Coverage

The Asset Intake Router covers:

- individual equities;
- ETFs;
- commodities;
- crypto assets;
- bonds and fixed income instruments;
- asset comparisons;
- asset updates;
- asset-level monitoring;
- portfolio role questions;
- valuation-only requests;
- risk-only requests;
- thesis-testing requests;
- market positioning and expectations requests;
- market reaction requests;
- financial statement analysis;
- red-flag checks;
- news and catalyst requests.

## 4. Primary Responsibilities

The Asset Intake Router owns:

- identifying the asset class;
- resolving ambiguous instruments;
- asking up to 3 relevant context questions;
- choosing full vs focused workflow;
- creating asset-level intake context;
- determining freshness requirements;
- identifying required specialist modules;
- preserving missing context;
- preventing narrow requests from becoming full workflows without approval.

## 5. Non-Responsibilities

The Asset Intake Router does not:

- perform valuation;
- perform risk analysis;
- write final investment memos;
- collect all evidence itself;
- issue investment actions;
- determine final position sizing;
- override specialist limitations.

## 6. Contextual Intake Rule

The router should ask up to 3 relevant questions when context is materially incomplete.

It should not ask a fixed questionnaire every time.

Default asset questions may include:

```text
1. Is this for a new position, existing holding, or watchlist?
2. What investment horizon matters most?
3. Is there a specific thesis, concern, or question to test?
```

If the user already provided this information, do not ask again.

Missing non-blocking context should be recorded as `missing_intake_context`.

## 7. Blocking vs Non-Blocking Context

Blocking context:

- unclear asset or instrument;
- unclear task type when routing cannot be inferred.

Non-blocking but important context:

- horizon;
- current exposure;
- portfolio role;
- thesis;
- risk tolerance;
- preferred instruments.

The workflow may proceed with missing non-blocking context, but final outputs must disclose limitations.

## 8. Asset-Class Routing

| Asset / Instrument | Route |
|---|---|
| Public company stock | Equity route |
| ETF | ETF route + underlying exposure route |
| Commodity | Commodity route |
| Crypto asset | Crypto route |
| Bond / fixed income | Fixed income route + macro context |
| Bond ETF | ETF route + fixed income route + macro context |
| Crypto ETF | ETF route + crypto route |
| Commodity ETF | ETF route + commodity route |
| Producer equity | Equity route + commodity / sector context |
| Ambiguous asset | Clarify instrument |

## 9. Ambiguous Instruments

If the asset name can imply materially different instruments, the router should ask one clarifying question.

Examples:

```text
Gold -> physical commodity, ETF, futures, or gold miners?
Oil -> commodity, futures, ETF, or energy equities?
Bitcoin -> BTC, Bitcoin ETF, or crypto-related equities?
Apple -> stock by default unless bonds are specified.
TLT -> ETF route with fixed income and macro context.
```

## 10. Full vs Focused Asset Workflows

Generic asset analysis defaults to full asset-first investment workflow.

Examples:

```text
“Analyze Nvidia” -> full asset workflow
“Should I buy Nvidia?” -> full asset workflow
“Analyze gold as an investment” -> full commodity / asset workflow
```

Focused requests remain focused.

Examples:

```text
“Nvidia valuation only” -> valuation route
“What are Tesla’s risks?” -> risk route
“Why did Bitcoin rise today?” -> market reaction route
“Explain TLT duration risk” -> fixed income / educational route
```

## 11. Asset Route Map

| User Intent | Route | Output | Limitation |
|---|---|---|---|
| General asset analysis | Full asset workflow | Final investment memo | Requires valuation and risk review |
| Buy / hold / sell decision | Full asset workflow | Final investment memo | Requires evidence sufficiency |
| Valuation question | Valuation & expectations | `valuation_expectations.md` | No final action |
| Risk question | Risk / red-team | `risk_red_team.md` | Preliminary if thesis or valuation missing |
| User thesis question | Thesis testing route | Thesis validation note | May recommend asset, valuation, risk, or macro routes |
| Market expectations / positioning | Market positioning route | `market_positioning.md` | Data availability may limit confidence |
| Financial statement question | Financial statement analysis | `financial_statement_analysis.md` | Not full investment decision |
| Red flags | Red-flag review | Red-flag note | Not full risk review |
| News / catalysts | News & catalysts | `news_catalysts.md` | No final action |
| Why price moved | Market reaction | Market reaction note | Requires fresh data |
| Macro sensitivity | Macro route | `macro_sensitivity.md` | No final action |
| Portfolio role | Portfolio fit | `portfolio_fit.md` | Needs portfolio context for personalized fit; generic role may proceed without it |
| Entry timing | Entry timing route | Entry timing note | No precise trading signal |
| Monitoring | Monitoring route | Monitoring plan | Requires thesis context |
| Update old analysis | Update route | Update memo | Needs prior analysis for full update |
| Compare assets | Comparison route | Comparison memo | Not full analysis of all assets unless requested |

## 12. Positive Action Gate

The Asset Intake Router may route to a final investment decision only when the workflow can support valuation review, risk review, and evidence readiness.

If the user asks for a buy / add / sell / hold decision but required decision gates are unavailable, the route should produce a Limited or Blocked final memo rather than an unsupported action.

Positive actions require sufficient valuation work, risk review, and evidence readiness.

## 13. ETF Rule

ETFs must be analyzed as wrappers over underlying exposures.

The Asset Intake Router should route ETF requests to:

```text
ETF Agent + relevant underlying exposure route
```

ETF layer:

- exact instrument identity, including exchange, issuer, domicile, ISIN / CUSIP where available, share class, trading currency, distributing / accumulating, and hedged / unhedged status;
- holdings and weights;
- index / methodology / weighting / rebalance rules;
- expense ratio;
- liquidity;
- assets under management;
- issuer quality;
- structure;
- tracking;
- concentration;
- premium / discount where relevant;
- yield source and quality where relevant;
- tax, domicile, access, or wrapper caveats where relevant;
- overlap / false-diversification analysis where relevant.

Underlying exposure layer:

- equity / sector / commodity / crypto / fixed income / thematic / factor exposure;
- quality of the underlying exposure;
- risks of the underlying asset class;
- whether the ETF is an effective expression of the desired exposure.

Special ETF modes should be triggered when the instrument is active, thematic, factor-based, leveraged, inverse, options-income, synthetic, swap-based, volatility-linked, commodity-linked, crypto-linked, low-AUM, or otherwise complex.

## 14. Fixed Income Rule

Bond and fixed income requests require fixed income analysis plus macro context.

Analysis should consider:

- yield;
- yield type: yield to maturity, yield to worst, SEC yield, distribution yield, real yield, or tax-equivalent yield where relevant;
- duration;
- curve exposure;
- credit quality;
- spreads;
- liquidity;
- convexity where relevant;
- inflation sensitivity;
- rate scenarios;
- spread / credit deterioration scenarios;
- call, prepayment, extension, or structure risk where relevant;
- individual bond vs bond fund economics.

Bond ETFs require both ETF wrapper analysis and Fixed Income Agent exposure analysis. The ETF Agent owns wrapper quality, holdings, tracking, liquidity, fees, and NAV premium / discount. The Fixed Income Agent owns duration, curve, credit, spread, convexity, yield interpretation, and fixed-income compensation adequacy. Macro Agent owns rates, inflation, policy, FX, and liquidity regime.

High-yield, distressed, private credit, structured credit, subordinated / hybrid, preferred, convertible, EM debt, opaque, unusually high-yielding, or "safe income" contradiction cases should trigger Risk / Red Team escalation.

## 15. Commodity Rule

Commodity requests require Commodity Agent analysis.

The route should consider:

- commodity identity, benchmark, region, and exposure type;
- physical supply / demand balance;
- demand by industry, country, central bank, government, strategic reserve buyer, or end market where material;
- supply by region, producer group, project pipeline, cost curve, geology, OPEC / policy actor, or harvest cycle where material;
- commercial inventories, exchange stocks, strategic reserves, above-ground stocks, geological reserves / resources, and spare capacity;
- futures curve, roll yield, carry, contango / backwardation, and vehicle implications;
- marginal cost, cost curve, and incentive price as context rather than guaranteed price floors;
- geopolitics, sanctions, export bans, tariffs, OPEC / producer policy, storage, logistics, transport, and seasonality;
- macro sensitivity to USD, real rates, inflation, growth, China cycle, liquidity, and FX;
- substitution risk;
- investment vehicle.

If the instrument is unclear, clarify whether the user means physical commodity, futures, ETF / ETC, broad commodity basket, producer equity, miner, royalty / streaming company, or leveraged / inverse product.

Commodity ETF / ETC requests route to ETF Agent for wrapper quality and Commodity Agent for the underlying commodity thesis. Producer, miner, energy, royalty, or streaming equity requests route to Equity Agent for company analysis and Commodity Agent for commodity cycle / beta. Broad commodity baskets require exposure decomposition rather than being treated as automatically diversified inflation hedges.

## 16. Crypto Rule

Crypto assets require crypto-specific analysis.

The route should consider:

- asset identity and crypto economic classification;
- investment-grade viability gate;
- network usage, network economics, and tokenholder value capture;
- tokenomics, unlocks, emissions, supply pressure, and FDV / float risk;
- liquidity, market structure, derivatives, leverage, funding, and liquidations when setup matters;
- custody, protocol, smart-contract, bridge, oracle, governance, and security risk;
- regulation, with US-first and global-aware treatment;
- adoption quality, including the difference between real usage and subsidized / vanity metrics;
- ETF flows, corporate crypto treasury demand, stablecoin liquidity, and structural demand / supply where relevant;
- DeFi, staking, lending, and yield economics as an investment and risk layer, not operational yield advice;
- speculative narrative risk and weak-data guardrails;
- source reliability, freshness, and access-aware fallback rules.

Dedicated Crypto Agent design documents:

```text
crypto-agent-prd.md
crypto-analysis-method-skill-prd.md
crypto-analysis-framework.md
crypto-data-source-and-metric-framework.md
```

Primary crypto outputs:

```text
crypto_analysis.md
crypto_market_regime.md
```

Crypto ETFs require ETF wrapper analysis plus crypto exposure analysis. Crypto-linked equities require Equity Agent analysis plus Crypto Agent input on crypto exposure mechanics.

## 17. Equity Rule

For individual equities, route by user intent:

```text
General analysis -> full equity deep-dive workflow
Buy / sell / hold -> full equity deep-dive workflow
Valuation -> valuation route
Risks -> risk route
Price movement -> market reaction route
Financials -> financial statement route
Red flags -> red-flag route
Catalysts -> news and catalysts route
Portfolio role -> portfolio fit route
```

## 18. Comparison Rule

Asset comparisons use a dedicated comparison route.

The system should not automatically run full deep dives for each compared asset.

Comparison should focus on:

- suitability for the user's objective;
- quality;
- valuation;
- risk;
- catalysts;
- macro sensitivity;
- portfolio role;
- what would change the ranking.

## 19. Portfolio Context Rule

Portfolio context is required when the user asks for a capital action:

- buy;
- add;
- reduce;
- sell;
- position size;
- what to do with existing position;
- what to buy now.

Without portfolio context, the system must not give exact position sizing.

Portfolio Fit and Investment Committee workflows still must not provide exact position sizing. If future portfolio-construction functionality is introduced, exact sizing must route there rather than being improvised by an asset router or specialist agent.

## 20. Entry Timing Boundary

Entry timing analysis may discuss conditions, catalysts, valuation risk, positioning, and event risk.

It must not provide precise trading signals, guaranteed entry levels, or short-term price predictions.

The system may provide conditional timing guidance such as:

```text
Entry risk is elevated before earnings.
The setup improves if valuation resets or the next report confirms demand durability.
```

It should not present false precision.

## 21. Market Positioning Boundary

Requests about consensus, crowded trades, estimate revisions, ownership, flows, short interest, or what the market appears to believe should route to Market Positioning.

This route is distinct from valuation:

```text
Valuation asks whether the price is justified by realistic fundamentals.
Market positioning asks what visible expectations suggest, how investors appear positioned, and whether the setup creates expectation, crowding, neglect, or positioning risk.
```

If market positioning data is unavailable, stale, proxy-only, or paywalled, the output should disclose the limitation, use Complete / Limited / Blocked positioning status where relevant, and avoid overstating crowding, neglect, squeeze, or consensus conclusions.

## 22. Output Format vs Evidence Requirements

If the user asks for a quick, brief, deep, or detailed asset answer, the router may adapt the output format.

It must not lower the evidence threshold for investment actions.

Brief answers may be preliminary. Positive actions still require valuation, risk review, and evidence readiness.

## 23. Freshness Rule

Fresh data is mandatory for:

- current valuation;
- current price;
- market reaction;
- recent earnings;
- recent news;
- “today / yesterday / now” questions;
- updates after events.

## 24. Prior Analysis and Update Rule

For update requests, the router should first check whether a prior analysis exists.

If prior analysis exists, launch the update workflow and create a new dated work folder.

If prior analysis does not exist, route to market reaction, event analysis, or fresh full analysis depending on user intent.

Never overwrite the prior analysis.

## 25. Asset Intake Block

For asset workflows, the intake block should include:

```text
Original request:
Asset / instrument:
Asset class:
Route type:
User intent:
Decision type:
Horizon:
Current exposure:
Portfolio context:
Primary thesis / concern:
Clarifying questions and answers:
Missing context:
Freshness requirement:
Required modules:
Expected artifacts:
Scope limitations:
```

## 26. Full Asset Workflow Default

A generic asset request should normally launch the full asset-first investment workflow.

For equities, this means the Equity Deep Dive Workflow.

A complete final investment memo requires valuation and risk review. Positive actions require sufficient valuation work, risk review, and evidence readiness.

## 27. Success Criteria

The Asset Intake Router succeeds when:

- the correct asset class is identified;
- ambiguous instruments are clarified;
- narrow requests remain narrow;
- full asset requests launch the appropriate workflow;
- missing context is captured;
- freshness requirements are flagged;
- ETF, fixed income, commodity, and crypto instruments receive correct specialized routing.
