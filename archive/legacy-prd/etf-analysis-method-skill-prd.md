# ETF Analysis Method Skill PRD

## Purpose

This skill defines the repeatable method used by the ETF Agent to analyze exchange-traded funds as wrappers over underlying exposures.

The method is designed to produce professional, evidence-aware, decision-useful ETF analysis without making final buy / sell / hold recommendations.

Primary output:

```text
etf_analysis.md
```

## Core Method Sequence

```text
Identify instrument
-> classify ETF type
-> refresh current data
-> analyze holdings
-> analyze methodology
-> analyze wrapper and structure
-> analyze cost and liquidity
-> analyze performance and risk history
-> compare peers
-> check overlap and false diversification
-> scan look-through valuation exposure where material
-> identify red flags
-> produce vehicle-quality verdict
-> hand off where needed
```

## Step 1 — Confirm User Intent

Classify the request type:

- single ETF review;
- ETF comparison;
- ETF discovery / shortlist;
- ETF overlap analysis;
- ETF replacement / substitution;
- thematic ETF purity check;
- complex ETF special-risk review;
- active ETF review;
- ETF-as-expression-of-theme analysis;
- ETF-vs-direct-holding tradeoff;
- factual ETF query.

Identify or infer intended role:

- core exposure;
- satellite exposure;
- tactical trade;
- hedge;
- income;
- factor tilt;
- sector / theme expression;
- duration / credit bet;
- commodity access;
- crypto access;
- diversification;
- cash-like / defensive role;
- replacement / simplification.

If intent is unclear, evaluate across plausible role candidates rather than pretending one universal verdict exists.

## Step 2 — Identify the Instrument

Confirm where available:

- ticker;
- full fund name;
- issuer;
- exchange;
- domicile;
- ISIN / CUSIP;
- legal wrapper type;
- ETF vs ETN / CEF / mutual fund / other;
- active vs passive;
- index tracked, if any;
- inception date;
- fund base currency;
- trading currency;
- accumulating vs distributing share class;
- hedged vs unhedged share class.

If the ticker or share class is ambiguous, state the assumed instrument or ask one targeted clarification question if the ambiguity would materially change the answer.

## Step 3 — Separate Fund-Level and Share-Class-Level Facts

Fund-level facts:

- holdings;
- index;
- methodology;
- issuer;
- broad structure;
- exposure;
- portfolio construction.

Share-class-level facts:

- exchange;
- trading currency;
- hedge status;
- accumulating / distributing status;
- spread;
- venue-specific liquidity;
- access / tax / domicile caveats.

Do not compare share classes as if all implementation details are identical.

## Step 4 — Classify ETF Type

Classify into one or more:

- broad equity;
- sector;
- thematic;
- factor;
- equal-weight;
- bond;
- commodity;
- crypto;
- multi-asset;
- active;
- leveraged;
- inverse;
- options-income / covered-call;
- synthetic / swap-based;
- futures-based;
- volatility-linked;
- currency-hedged;
- UCITS;
- US-listed;
- young / limited-track-record ETF;
- low-AUM / niche ETF.

ETF type determines which method modules are mandatory.

## Step 5 — Refresh Current Data

For current investment analysis, collect or refresh:

- latest holdings;
- holdings as-of date;
- expense ratio;
- AUM;
- inception date;
- issuer;
- index;
- methodology;
- rebalance and reconstitution rules;
- liquidity;
- average daily volume;
- bid-ask spread where available;
- premium / discount where available;
- performance history;
- risk metrics where available;
- yield and distribution data;
- peer metrics;
- overlap data;
- tax / domicile / access caveats where relevant.

Every decision-critical field needs source and as-of date in the evidence pack. The main memo should show compact source notes for the most important fields.

## Step 6 — Apply Source Hierarchy

Use issuer and official sources first:

1. issuer holdings files;
2. issuer pages;
3. fact sheets;
4. prospectus / SAI;
5. index methodology documents;
6. index provider pages;
7. regulatory filings;
8. official exchange data;
9. official NAV / premium-discount data.

Use reputable secondary sources for fallback or comparison:

- Morningstar;
- ETF.com;
- ETF Database;
- ETF Research Center;
- broker / market-data pages;
- recognized financial data providers.

ETFRC's overlap tool may be used as secondary overlap evidence or sanity check, not as a substitute for issuer holdings files when those are available.

## Step 7 — Holdings Breakdown

Use the full issuer holdings file when available.

Calculate or summarize:

- number of holdings;
- top 10 holdings;
- top 20 holdings where useful;
- top 10 weight;
- top 20 weight;
- largest holding weight;
- single-name concentration;
- sector exposure;
- industry exposure where relevant;
- country / region exposure;
- factor exposure;
- currency exposure;
- asset-class exposure;
- derivative / cash / collateral exposure where relevant.

If only top holdings are available, proceed with explicit limitations and do not infer full portfolio composition.

## Step 8 — Top-Holdings Risk Driver Scan

Identify what actually drives ETF behavior:

- single-name dependency;
- mega-cap concentration;
- earnings / catalyst concentration;
- valuation concentration;
- country / geopolitical risk;
- supply-chain clusters;
- sector clusters;
- factor tilts;
- hidden beta;
- exposure to a small number of dominant issuers.

This is a risk-driver scan, not full company analysis. If specific holdings dominate the ETF thesis, hand off to Equity / Valuation / Sector / Risk as needed.

## Step 9 — Concentration Review

Use context-aware concentration thresholds.

Assess concentration relative to:

- ETF category;
- stated role;
- methodology;
- peer norms;
- user intent;
- expected diversification level.

Concentration is acceptable only when it is intentional, disclosed, and consistent with intended role. If an ETF appears diversified but depends heavily on a few holdings, flag false diversification.

## Step 10 — Reported Holdings vs Economic Exposure

For derivative, futures, swap, options, or collateral-heavy ETFs, distinguish:

- accounting holdings;
- collateral;
- notional exposure;
- economic exposure;
- leverage;
- reset mechanics;
- option overlay;
- futures roll;
- counterparty exposure;
- tracking implications.

Do not treat Treasury collateral in a futures-based product as the true investment exposure.

## Step 11 — Index and Methodology Analysis

For passive or rules-based ETFs, review:

- index provider;
- index name;
- eligibility rules;
- selection rules;
- weighting scheme;
- cap rules;
- liquidity screens;
- sector / country rules;
- inclusion / exclusion rules;
- rebalance schedule;
- reconstitution schedule;
- methodology risks.

Explain the investment impact of rebalance / reconstitution rules:

- selling winners / buying laggards;
- maintaining factor tilt;
- resetting concentration;
- increasing turnover;
- cost drag;
- tax / wrapper implications;
- maturity bucket updates;
- leverage reset;
- performance behavior.

## Step 12 — Active ETF Analysis

For active ETFs, review:

- strategy mandate;
- management team / issuer credibility;
- benchmark relevance;
- holdings transparency;
- active share where available;
- turnover;
- holdings drift;
- style drift;
- fee justification;
- capacity;
- performance attribution;
- risk controls.

Do not assume an active ETF will continue to hold the same exposure just because current holdings show it today.

## Step 13 — Structure and Wrapper Analysis

Analyze where relevant:

- physical replication;
- full replication vs sampling;
- synthetic / swap exposure;
- futures exposure;
- options overlay;
- securities lending;
- collateral policy;
- counterparty exposure;
- accumulating vs distributing policy;
- UCITS vs US ETF;
- tax / domicile caveats;
- creation / redemption mechanism;
- premium / discount;
- fund age;
- closure risk;
- listing / access constraints.

## Step 14 — Cost Analysis

Assess expense ratio relative to:

- peer alternatives;
- exposure quality;
- index or strategy complexity;
- active-management value;
- tracking quality;
- liquidity;
- tax wrapper;
- domicile / access advantages;
- value delivered.

Do not treat the lowest fee as automatically best.

## Step 15 — Issuer Quality and Closure Risk

Review issuer quality through:

- scale / reputation;
- disclosure quality;
- product support;
- operational complexity;
- securities lending policy;
- sponsor-specific risks.

Assess closure risk through:

- AUM;
- fund age;
- net flows;
- trading volume;
- issuer support;
- product-line redundancy;
- niche relevance;
- market adoption.

Low AUM is a caution, not an automatic rejection.

## Step 16 — Liquidity and Implementation Caveats

Analyze:

- AUM;
- average daily volume;
- bid-ask spread;
- premium / discount;
- underlying holdings liquidity;
- creation / redemption conditions;
- market-hours mismatch;
- fund closure risk;
- trade-size relevance;
- holding-period relevance.

Provide practical caveats where material:

- spreads can matter;
- limit orders may be preferable when spreads are wide;
- premiums / discounts can widen in stress;
- ETF market hours may not match underlying holdings market hours.

Do not provide a detailed execution plan unless a separate execution module exists.

## Step 17 — Tracking Review

Where relevant and available, analyze:

- tracking difference;
- tracking error;
- causes of tracking difference;
- fees;
- taxes;
- securities lending;
- sampling;
- cash drag;
- futures roll;
- currency hedging;
- market-hours mismatch;
- premium / discount.

This is especially important for passive, synthetic, commodity, bond, international, and sampled-replication ETFs.

## Step 18 — Performance and Risk History

Historical performance is backward-looking evidence.

Review where available:

- YTD return;
- 1Y return;
- 3Y return;
- 5Y return;
- 10Y return;
- since inception;
- volatility;
- max drawdown;
- Sharpe or risk-adjusted return where available;
- benchmark comparison;
- peer comparison.

Explain what drove performance:

- exposure;
- concentration;
- factor tilt;
- sector cycle;
- macro regime;
- FX;
- leverage;
- distributions;
- valuation rerating.

Do not imply that past returns alone make an ETF attractive.

## Step 19 — Yield and Distribution Quality

For income-relevant ETFs, distinguish:

- SEC yield;
- distribution yield;
- trailing yield;
- dividend income;
- coupon income;
- option premium;
- capital gains;
- return of capital;
- leverage;
- FX effects;
- NAV erosion.

High yield must trigger a source and sustainability check.

## Step 20 — Peer Comparison

Select 2-4 close peers for ordinary investment analysis unless the request is narrow or a broader screen is requested.

Compare by use-case fit:

- core exposure;
- satellite exposure;
- thematic purity;
- liquidity / trading;
- income;
- hedge;
- factor tilt;
- low cost;
- diversification;
- UCITS / access suitability.

Avoid universal best-ETF claims. Explain why each peer was selected.

## Step 21 — Benchmark Selection

Use two benchmark levels:

1. Official benchmark for tracking and methodology.
2. Decision benchmark for investment usefulness.

Explain benchmark choice. Avoid cherry-picked comparisons.

## Step 22 — Overlap Analysis

If reliable holdings data is available, calculate:

- common holdings count;
- overlap by weight;
- top-holdings duplication;
- top-10 overlap;
- top-25 overlap where useful;
- sector overlap;
- country / region overlap;
- factor overlap;
- duration / credit / commodity beta overlap where relevant.

Overlap can be calculated when holdings dates differ, but the output must show:

- source for each ETF;
- holdings as-of date;
- coverage level;
- whether full or partial holdings were used;
- precision limitation.

Use issuer files first. ETFRC and similar tools may support or sanity-check the result.

## Step 23 — False Diversification Check

Flag when the ETF or ETF combination appears diversified but is actually driven by repeated exposures:

- same mega-cap stocks;
- same sector;
- same factor;
- same country;
- same duration risk;
- same credit beta;
- same commodity beta;
- same crypto beta;
- same issuer / counterparty where relevant.

This is required when user portfolio context exists or when ETF comparison / replacement is requested.

## Step 24 — Thematic Purity Check

For thematic ETFs, classify holdings by relevance where feasible:

- pure-play;
- core beneficiary;
- adjacent beneficiary;
- generic exposure;
- weak / non-thematic holding.

Assess:

- directness of exposure;
- revenue / business-model linkage where feasible;
- top-holding relevance;
- diluted exposure;
- marketing-label risk;
- concentration in hype names;
- whether ETF is a good public-market expression of the theme.

If the ETF is a weak proxy but the idea may be attractive, separate ETF vehicle quality from thesis quality and recommend a better-expression route.

## Step 25 — Factor Exposure Check

For factor ETFs, evaluate:

- factor definition;
- selection rules;
- weighting rules;
- rebalance frequency;
- turnover;
- sector / country tilts;
- valuation tilt;
- concentration;
- cyclicality;
- crowding;
- holdings consistency with factor label.

## Step 26 — Look-Through Valuation Exposure Scan

When valuation is material to ETF vehicle quality, role suitability, peer comparison, or thematic / factor risk, perform a high-level look-through valuation exposure scan.

Use ETF-level, category-level, or holdings-level metrics where available:

- P/E;
- P/B;
- P/S;
- earnings yield;
- dividend yield where relevant;
- valuation versus category or peers;
- expensive-name concentration;
- growth / duration-like equity exposure;
- sector or factor valuation tilt.

Use this scan to answer:

- Is the ETF's exposure valuation-sensitive?
- Is performance dependent on expensive top holdings?
- Is the ETF cheaper or more expensive than close alternatives for a good reason?
- Does the ETF label hide a large growth / quality / value / duration valuation tilt?

Do not build full valuation models or imply a final mispricing conclusion. Full valuation and implied-expectations work belongs to Valuation & Expectations or the relevant asset-class specialist.

## Step 27 — Complex ETF Special-Risk Mode

Activate special-risk mode for:

- leveraged;
- inverse;
- options-income;
- volatility-linked;
- synthetic;
- swap-based;
- futures-based;
- crypto;
- opaque active;
- low-AUM niche products.

Explain:

- payoff mechanics;
- daily reset;
- compounding;
- volatility drag;
- derivative exposure;
- collateral;
- counterparty risk;
- roll yield;
- NAV erosion;
- intended holding period;
- distribution sustainability;
- misleading historical return / yield risk.

## Step 28 — Asset-Class-Specific Routing

### Commodity ETFs

Classify physical-backed, futures-based, swap-based, producer-equity, broad basket, currency-hedged, leveraged / inverse. Route commodity thesis to Commodity Agent.

### Bond ETFs

Classify Treasury, corporate, high yield, muni, TIPS, international, EM debt, duration, maturity, credit quality, yield, currency, spread sensitivity, call / convexity risk. Route fixed-income thesis to Fixed Income Agent and macro drivers to Macro Agent.

### Crypto ETFs

Classify spot, futures, leveraged / inverse, crypto-equity basket, multi-token basket, custody-dependent, jurisdiction-dependent. Route token/network/adoption/regulation/security thesis to Crypto Agent.

### Sector / Thematic Equity ETFs

Route sector structure, profit pools, investability, and theme validity to Sector / Industry Analysis Agent when material.

## Step 29 — ETF-vs-Direct-Holding Tradeoff

When relevant, compare ETF wrapper to direct exposure at a high level:

- access;
- liquidity;
- fees;
- custody;
- tracking;
- taxes / wrapper caveats;
- operational burden;
- reinvestment;
- maturity certainty;
- counterparty / custody risk;
- diversification.

Do not make the final cross-asset selection.

## Step 30 — Replacement / Substitution Analysis

For replacing ETF A with ETF B, compare:

- exposure continuity;
- holdings overlap;
- what is gained;
- what is lost;
- fee difference;
- liquidity difference;
- tax / domicile implications;
- performance / risk difference;
- benchmark difference;
- role continuity;
- hidden concentration changes.

Do not issue the final replacement action.

## Step 31 — ETF Flow Context

ETF Agent may report ETF flows as supporting context for:

- adoption;
- demand;
- liquidity;
- narrative heat;
- crowding clues.

Market Positioning Agent owns broader positioning, crowding, and expectation-risk interpretation.

## Step 32 — ESG / Values / Exclusion Claims

If ESG, values, exclusions, fossil-free, weapons-free, religious-screen, China-exclusion, or similar claims are part of the ETF mandate, user intent, or material risk, test:

- methodology;
- exclusion rules;
- holdings consistency;
- greenwashing / label risk;
- controversial holdings exposure.

Distinguish methodology facts from value judgments.

## Step 33 — Red Flag Checklist

Check for:

- stale holdings;
- missing full holdings;
- low AUM;
- fund closure risk;
- excessive fee for diluted exposure;
- extreme concentration;
- weak thematic purity;
- high overlap;
- false diversification;
- poor liquidity;
- wide bid-ask spread;
- material premium / discount;
- poor tracking;
- synthetic opacity;
- counterparty risk;
- leverage misunderstood;
- inverse exposure misunderstood;
- covered-call yield chasing;
- NAV erosion;
- commodity roll risk;
- crypto custody / regulation risk;
- active ETF style drift;
- currency mismatch;
- tax / domicile caveat;
- access / listing issue;
- reported holdings not matching economic exposure.

Material unresolved red flags block a positive vehicle-quality verdict.

## Step 34 — Handoff Decision

Hand off when needed:

- Evidence Collector for source verification and current data;
- Sector / Industry for sector structure and theme validity;
- Macro for rates, inflation, FX, liquidity, policy, or credit regime;
- Fixed Income for duration, curve, credit, spread, convexity, yield;
- Commodity for supply-demand, inventories, futures curve, marginal cost;
- Crypto for token, network, custody, adoption, regulation, security;
- Market Positioning for crowding, flows, narrative, expectation-risk;
- Portfolio Fit for overlap, role suitability, concentration, user portfolio fit;
- Risk / Red Team for material ETF-specific or thesis-breaking risks;
- Investment Committee for final synthesis and action.

## Step 35 — Produce Vehicle-Quality Verdict

End with vehicle-quality verdict and role candidate, not final action.

Allowed examples:

- clean broad-market core candidate;
- pure but concentrated thematic satellite;
- diluted theme proxy;
- tactical trading vehicle, not core holding;
- income product with NAV erosion risk;
- poor diversifier due to high overlap;
- watchlist only because data is limited;
- unsuitable for the stated role due to unresolved structural risk.

Prohibited:

- buy;
- sell;
- hold as final action;
- allocate X%;
- best ETF overall;
- guaranteed income;
- risk-free;
- perfect diversification.

## Step 36 — Data Notes and Limitations

Include compact notes for decision-critical data:

- holdings source and as-of date;
- AUM and fee source;
- methodology source;
- performance source and period;
- yield source;
- liquidity source;
- premium / discount source;
- overlap source and holdings dates;
- peer data source;
- limitations.

Full source log belongs in the evidence pack.
