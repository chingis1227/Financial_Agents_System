# ETF Agent PRD

## Purpose

The ETF Agent analyzes exchange-traded funds as investment wrappers over underlying exposures, not as generic tickers.

Its core question is:

```text
What does this ETF actually own, what exposure does it provide, how good is the wrapper, how does it compare with alternatives, and what risks or overlaps are hidden?
```

The ETF Agent supports real investment research by identifying whether an ETF is a clean, diluted, risky, expensive, overlapping, or otherwise imperfect vehicle for a stated investment objective. It does not make the final buy / sell / hold decision.

## Core Doctrine

```text
ETF = wrapper + underlying exposure.
```

ETF analysis must separate:

1. ETF wrapper quality.
2. Underlying exposure quality.
3. Portfolio role and overlap implications.
4. Final investment action.

A good investment idea can have a bad ETF wrapper. A strong ETF wrapper can still provide unattractive underlying exposure. A low-cost ETF can still be a poor vehicle if it gives diluted, stale, illiquid, overconcentrated, or misunderstood exposure.

The ETF Agent must explicitly distinguish:

```text
thesis quality != vehicle quality
```

## Primary Responsibilities

The ETF Agent owns:

- ETF identity verification;
- ETF type classification;
- holdings breakdown;
- full holdings analysis when issuer holdings are available;
- top-holdings analysis when only partial data is available;
- index and methodology analysis;
- weighting, rebalancing, and reconstitution interpretation;
- ETF structure and wrapper analysis;
- expense ratio analysis in context;
- AUM, fund age, issuer quality, and closure-risk review;
- liquidity, bid-ask, premium / discount, and implementation caveats;
- tracking difference and tracking error review where available;
- historical performance and risk review as backward-looking evidence;
- yield source and sustainability review;
- peer ETF comparison;
- ETF overlap and false-diversification analysis;
- ETF replacement / substitution analysis;
- thematic exposure purity testing;
- factor exposure diagnosis;
- high-level look-through valuation exposure scan;
- active ETF process review;
- complex ETF special-risk mode;
- tax, domicile, listing, access, and wrapper caveats;
- vehicle-quality verdict and role-candidate framing;
- structured handoffs to specialist agents.

## Non-Responsibilities

The ETF Agent does not own:

- final buy / sell / hold recommendations;
- exact position sizing;
- final portfolio suitability;
- tax advice;
- legal advice;
- fiduciary suitability determinations;
- full company analysis for every holding;
- full valuation models;
- full macro regime analysis;
- full commodity supply-demand analysis;
- full crypto token, network, custody, or adoption thesis;
- full fixed-income duration, credit, spread, convexity, or issuer-quality model;
- final portfolio construction;
- detailed trading execution plan;
- final Investment Committee synthesis.

## Supported Instruments

The ETF Agent supports:

- broad equity ETFs;
- sector ETFs;
- thematic ETFs;
- factor ETFs;
- equal-weight ETFs;
- market-cap-weighted ETFs;
- active ETFs;
- bond ETFs;
- commodity ETFs;
- crypto ETFs;
- multi-asset ETFs;
- covered-call / options-income ETFs;
- leveraged ETFs;
- inverse ETFs;
- synthetic / swap-based ETFs;
- volatility-linked ETFs;
- currency-hedged ETFs;
- UCITS ETFs;
- US-listed ETFs;
- ETF share classes and trading lines.

Adjacent instruments must be labeled separately and routed or caveated as appropriate:

- ETNs;
- closed-end funds;
- mutual funds;
- structured notes;
- exchange-traded products that are not legally or economically ETF-like.

## Required Identity Verification

Before material analysis, the ETF Agent must verify the instrument identity where available:

- ticker;
- full fund name;
- issuer / sponsor;
- exchange / listing venue;
- ISIN and / or CUSIP when available;
- domicile;
- fund base currency;
- trading currency;
- share class;
- accumulating vs distributing policy;
- hedged vs unhedged status;
- active vs passive status;
- ETF vs ETN / CEF / mutual fund / other wrapper.

If ambiguity remains, the report must state the assumed instrument or ask a targeted clarification question when the ambiguity could materially change the analysis.

## Fund-Level vs Share-Class-Level Rule

The ETF Agent must separate fund-level analysis from share-class-level implementation analysis.

Fund-level analysis covers:

- underlying holdings;
- index;
- methodology;
- issuer;
- broad structure;
- exposure;
- core fund economics.

Share-class-level analysis covers:

- trading currency;
- exchange / venue;
- accumulating vs distributing status;
- hedged vs unhedged status;
- share-class liquidity;
- bid-ask spread;
- tax / domicile / access caveats.

The agent must not mix these levels when comparing UCITS share classes, currency lines, accumulating / distributing lines, or hedged / unhedged versions.

## Main Output Artifact

The ETF Agent's primary artifact is:

```text
etf_analysis.md
```

The artifact is modular. It can run in these modes:

1. Single ETF review.
2. ETF comparison.
3. ETF discovery / shortlist.
4. ETF overlap analysis.
5. ETF replacement / substitution analysis.
6. Thematic ETF purity check.
7. Complex ETF special-risk review.
8. Active ETF review.
9. ETF-as-expression-of-theme analysis.
10. ETF-vs-direct-holding wrapper tradeoff.

## User-Facing Status Rule

The system may internally use:

```text
Complete / Limited / Blocked
```

The main user-facing ETF report should not display bureaucratic status labels by default.

Instead:

- if evidence is sufficient, write the analysis normally;
- if evidence is limited, include a specific Data Notes / Limitations section;
- if analysis is blocked, plainly explain why no reliable conclusion can be made.

Example user-facing limitation:

```text
Data note: Holdings are based on the latest issuer top-10 disclosure rather than a full holdings file, so overlap and concentration estimates are approximate.
```

## Source Hierarchy

### Primary Sources

The ETF Agent should prioritize:

- ETF issuer website;
- issuer holdings file;
- fund fact sheet;
- prospectus;
- statement of additional information, where relevant;
- index methodology document;
- index provider documentation;
- regulatory filings;
- exchange data;
- official NAV / premium-discount data where available;
- official fund distribution disclosures where available.

### Secondary / Fallback Sources

The ETF Agent may use reputable secondary sources for comparison, performance, liquidity, peer discovery, and sanity checks:

- Morningstar;
- ETF.com;
- ETF Database;
- ETF Research Center;
- issuer comparison tools;
- reputable broker / market-data pages;
- official exchange pages;
- recognized financial data providers.

Secondary sources may support analysis, but material holdings, structure, and methodology claims should be verified against issuer or official documents when available.

### ETFRC Overlap Tool

ETF Research Center's overlap tool may be used as a secondary overlap source and sanity check:

```text
https://www.etfrc.com/funds/overlap.php
```

It does not replace issuer holdings files as primary evidence. If ETFRC or another overlap tool conflicts with issuer holdings data, issuer or official holdings data takes precedence unless the issuer data is stale or incomplete and the limitation is clearly stated.

## Freshness Rules

For current investment analysis, the ETF Agent must refresh decision-relevant data when internet access is available:

- holdings;
- AUM;
- expense ratio;
- index / methodology;
- performance;
- yield;
- distributions;
- liquidity;
- average volume;
- bid-ask spread where available;
- premium / discount where available;
- peer ETF metrics;
- overlap inputs.

Every decision-critical data point should include source and as-of date in the evidence pack and compact source notes in the main report.

If data is stale, incomplete, paywalled, derived from a fallback source, or only partially disclosed, the ETF Agent must say so.

## Holdings Rule

The ETF Agent should use full issuer holdings files when available.

If only top holdings are available:

- analysis may proceed;
- full-portfolio claims are prohibited;
- overlap, concentration, and exposure conclusions must be labeled approximate;
- limitations must be explicit.

Full holdings snapshots should live in the evidence pack or appendix when available. The main memo should show decision-relevant holdings summaries:

- top holdings;
- top 10 / top 20 weight;
- largest holding weight;
- concentration indicators;
- sector, country, factor, asset-class, currency, and derivative exposure buckets where relevant;
- key risk drivers.

## Reported Holdings vs Economic Exposure

The ETF Agent must distinguish accounting / reported holdings from economic exposure when derivatives, futures, swaps, options, collateral, or leverage are involved.

For derivative-based ETFs, the agent should review where available:

- notional exposure;
- collateral;
- counterparties;
- futures roll mechanics;
- option overlay;
- leverage factor;
- daily reset;
- tracking implications;
- counterparty and collateral risks.

This is especially important for commodity, leveraged, inverse, synthetic, covered-call, volatility-linked, and some bond ETFs.

## Index and Methodology Rule

For passive and rules-based ETFs, the ETF Agent must analyze the index as the source of portfolio construction.

The agent should review:

- index provider;
- official index name;
- eligibility rules;
- selection rules;
- weighting scheme;
- market-cap weighting vs equal weighting vs factor weighting;
- rebalance schedule;
- reconstitution schedule;
- caps;
- liquidity screens;
- sector / country rules;
- inclusion / exclusion rules;
- methodology risks.

The agent should explain how rebalance and reconstitution rules affect exposure, turnover, concentration, costs, tracking, and performance behavior.

Full methodology audits are reserved for complex, thematic, factor, leveraged, disputed, or methodology-sensitive ETFs.

## Active ETF Rule

Active ETFs require an active-management mode.

The ETF Agent should analyze:

- strategy mandate;
- manager / issuer credibility;
- benchmark relevance;
- holdings transparency;
- portfolio turnover;
- active share where available;
- style drift;
- holdings drift;
- fee justification;
- performance attribution;
- capacity and liquidity constraints where relevant;
- risk controls.

The agent should not treat active ETF holdings as if they were a static index basket.

## Peer Comparison Rule

When a user asks an investment question about one ETF, the ETF Agent should usually include a compact peer set of 2-4 close alternatives unless the request is purely factual.

ETF comparison should be by use-case fit, not by universal ranking.

Compare peers by:

- exposure purity;
- holdings;
- concentration;
- methodology;
- fee;
- AUM;
- liquidity;
- tracking quality;
- structure;
- domicile / tax caveats;
- historical performance;
- risk metrics;
- yield where relevant;
- overlap;
- intended role.

The agent must avoid claiming that one ETF is universally best across incompatible investor contexts.

## ETF Universe Rule

The ETF Agent should use user jurisdiction / access context when available.

If jurisdiction or access is unknown, the agent should separate:

- US-listed options;
- UCITS / Europe-listed options;
- other non-US options where relevant.

The agent must avoid declaring one universal best ETF across incompatible wrappers, listings, currencies, tax treatments, and access regimes.

## ETF Discovery / Shortlist Rule

The ETF Agent may run ETF discovery / shortlist mode for a theme, sector, factor, region, commodity, crypto, or fixed-income exposure.

ETF discovery should require:

- verified exposure relevance;
- basic investability;
- adequate disclosure;
- understandable structure;
- reasonable AUM / liquidity or explicit caveat;
- fee context;
- domicile / access caveats where relevant.

ETF name alone is never sufficient.

Young ETFs may be included if exposure and structure are credible, but the agent must flag limited track record, weak historical performance evidence, AUM / liquidity risk, and closure risk.

## Overlap and False-Diversification Rule

The ETF Agent must detect overlap:

- between ETF and the user's portfolio;
- between ETF and other ETFs;
- within the same theme;
- across different-looking themes.

The agent should flag:

- duplicated top holdings;
- top-10 and top-25 overlap where useful;
- sector overlap;
- country / region overlap;
- factor overlap;
- mega-cap concentration;
- duration overlap;
- commodity beta overlap;
- credit exposure overlap;
- issuer / counterparty overlap where relevant;
- false diversification;
- same exposure in different packaging.

If full holdings are available, overlap should be quantitative. If holdings dates differ, calculation may proceed, but the agent must show each source, holdings date, coverage, and limitation. If data is too stale or incomplete, overlap must be labeled approximate or not decision-grade.

## Thematic ETF Rule

The ETF Agent must not accept a thematic ETF label at face value.

It must test:

- exposure purity;
- top-holding relevance;
- business-model linkage;
- revenue linkage where feasible;
- diluted exposure;
- generic mega-cap filler;
- marketing-label risk;
- concentration in hype names;
- whether the ETF is actually a good proxy for the theme.

For thematic holdings, the agent should classify relevance where feasible:

- pure-play;
- core beneficiary;
- adjacent beneficiary;
- generic exposure;
- weak / non-thematic holding.

If the ETF is a weak proxy but the underlying theme may still be attractive, the agent should recommend an alternative-expression route rather than rejecting the theme automatically.

## Factor ETF Rule

Factor ETFs require factor-exposure mode.

The ETF Agent should analyze:

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
- whether holdings actually deliver the stated factor exposure.

Factor labels must not be accepted without holdings and methodology support.

## Look-Through Valuation Exposure Rule

The ETF Agent may perform a high-level look-through valuation exposure scan when valuation is material to ETF vehicle quality or role suitability.

This scan may use ETF-level, category-level, or holdings-level valuation metrics where available, including:

- P/E;
- P/B;
- P/S;
- earnings yield;
- dividend yield where relevant;
- valuation versus category or peers;
- concentration in expensive top holdings;
- growth / duration-like equity exposure;
- value, quality, profitability, or margin profile where available.

The purpose is to identify whether the ETF is exposed to expensive, cheap, crowded, rate-sensitive, or valuation-dependent holdings. It is not a full valuation model, reverse DCF, or implied-expectations analysis.

Full valuation work belongs to Valuation & Expectations, Equity, Fixed Income, Commodity, Crypto, or other asset-class specialists as appropriate.

## Complex ETF Special-Risk Rule

Special-risk mode applies to:

- leveraged ETFs;
- inverse ETFs;
- covered-call / options-income ETFs;
- volatility-linked ETFs;
- synthetic ETFs;
- swap-based ETFs;
- futures-based commodity ETFs;
- crypto ETFs;
- low-AUM niche ETFs;
- opaque active ETFs.

Special-risk mode must explain:

- payoff mechanics;
- daily reset;
- compounding;
- volatility drag;
- derivative exposure;
- counterparty risk;
- collateral;
- distribution sustainability;
- NAV erosion;
- intended holding period;
- why historical returns or yield may mislead.

The ETF Agent must not describe leveraged, inverse, volatility-linked, synthetic, or options-income products as ordinary diversified long-term ETF holdings.

## Commodity ETF Rule

Commodity ETFs require exposure-type classification:

- physical-backed;
- futures-based;
- swap-based;
- producer-equity ETF;
- broad commodity basket;
- currency-hedged;
- leveraged / inverse variants.

The ETF Agent owns wrapper, structure, tracking, liquidity, issuer quality, fees, AUM, benchmark, and tax / wrapper caveats. The Commodity Agent owns the underlying commodity thesis, including supply-demand, demand by industry / country / central bank or reserve actor where material, inventories / reserves, futures curve, roll / carry, marginal cost, geopolitics, policy, seasonality, storage / logistics, substitution risk, and commodity-specific macro sensitivity. Broad commodity baskets require Commodity Agent exposure decomposition rather than being treated as automatically diversified inflation hedges.

## Bond ETF Rule

Bond ETFs require fixed-income exposure classification:

- Treasury;
- corporate;
- high yield;
- municipal;
- TIPS / inflation-linked;
- international;
- emerging-market debt;
- duration bucket;
- maturity bucket;
- credit quality;
- yield type;
- currency exposure;
- spread sensitivity;
- call / convexity risk where relevant.

The ETF Agent owns wrapper, holdings, liquidity, structure, tracking, and share-class caveats. The Fixed Income Agent owns duration, curve, credit, spread, convexity, yield interpretation, individual bond vs fund economics, and fixed-income compensation adequacy using `fixed-income-agent-prd.md`, `fixed-income-framework.md`, and `fixed-income-instrument-playbooks.md`. The Macro Agent owns rates, inflation, policy, FX, and liquidity regime.

## Crypto ETF Rule

Crypto ETFs require structure and exposure classification:

- spot;
- futures-based;
- leveraged / inverse;
- crypto-equity basket;
- multi-token basket;
- custody-dependent;
- jurisdiction-dependent.

The ETF Agent owns wrapper, holdings / exposure, liquidity, tracking, fee, custody / wrapper caveats, premium / discount, and regulatory wrapper issues. The Crypto Agent owns token, network, adoption, regulation, security, custody, and speculative narrative risk analysis.

## Currency Exposure Rule

The ETF Agent should identify:

- trading currency;
- fund base currency;
- underlying currency exposure;
- hedged vs unhedged share class;
- hedge cost / carry caveat;
- FX contribution to returns where material.

The Macro Agent should be called when FX materially affects the ETF thesis.

## Yield Rule

ETF yield must be analyzed through source and sustainability.

The ETF Agent should distinguish:

- SEC yield;
- distribution yield;
- trailing yield;
- dividends;
- coupons;
- option premium;
- capital gains;
- return of capital;
- leverage;
- currency effects;
- NAV erosion.

High yield is not automatically attractive. Yield must not be equated with total return.

## Liquidity and Implementation Caveat Rule

The ETF Agent should evaluate liquidity through:

- AUM;
- average daily volume;
- bid-ask spread;
- premium / discount;
- underlying holdings liquidity;
- creation / redemption conditions;
- fund closure risk;
- intended holding period;
- trade-size relevance.

The ETF Agent may provide implementation caveats, such as spread awareness or limit-order caveats where relevant, but must not create a detailed execution plan.

## Closure Risk Rule

Closure risk should be assessed through:

- AUM;
- fund age;
- net flows;
- issuer support;
- product-line redundancy;
- liquidity;
- market adoption;
- evidence of continued sponsor commitment where available.

Low AUM is a caution, not an automatic rejection.

## Performance Rule

Historical performance is descriptive evidence, not a forward-looking verdict.

ETF Agent may report:

- YTD;
- 1Y;
- 3Y;
- 5Y;
- 10Y;
- since inception;
- volatility;
- max drawdown;
- Sharpe or risk-adjusted return where available;
- benchmark comparison;
- peer comparison.

The agent should explain what drove performance: exposure, concentration, factor tilt, sector cycle, macro regime, FX, leverage, dividends, valuation rerating, or other drivers.

## Benchmark Rule

The ETF Agent must separate:

1. Official tracking benchmark.
2. Decision benchmark.

The official benchmark is used for tracking, methodology, and performance versus the ETF's stated index.

The decision benchmark is used for investment usefulness and may include broader market benchmarks, sector ETFs, peer ETFs, commodity proxies, bond indexes, or intended-exposure proxies.

The agent must explain benchmark choice and avoid cherry-picked comparisons.

## Expense Ratio Rule

Expense ratio must be judged in context:

- exposure quality;
- peer alternatives;
- tracking quality;
- structure complexity;
- liquidity;
- tax wrapper;
- value delivered.

The cheapest ETF is not automatically best.

## Issuer Quality Rule

Issuer quality is part of vehicle-quality analysis.

The ETF Agent should assess:

- issuer scale / reputation;
- disclosure quality;
- closure risk;
- operational complexity;
- fund lineup support;
- securities lending policy where relevant;
- sponsor-specific risks.

This factor receives heavier weight for complex, small, niche, synthetic, crypto, leveraged, options-income, or active ETFs.

## Securities Lending Rule

The ETF Agent should review securities lending where disclosed and material.

Relevant fields include:

- lending policy;
- revenue split;
- collateral quality;
- counterparty exposure;
- whether lending offsets fees;
- effect on tracking difference;
- structure risk.

Deep securities-lending analysis is required only when lending materially affects ETF quality or risk.

## Tax / Domicile / Access Caveat Rule

The ETF Agent should flag material tax, domicile, distribution, withholding, listing, access, and wrapper issues when relevant.

Examples include:

- US ETF vs UCITS ETF;
- accumulating vs distributing share class;
- withholding tax caveats;
- K-1 / partnership issues;
- PFIC caveats;
- US situs / estate-tax caveats;
- PRIIPs / KID availability;
- US ETF access restrictions for EU retail investors;
- sanctions / country exposure;
- crypto ETF regulatory status;
- delisting / listing eligibility issues.

The ETF Agent must not provide personalized tax or legal advice.

## ETF-vs-Direct-Holding Rule

The ETF Agent may provide high-level ETF-vs-direct-holding wrapper tradeoffs, for example:

- TLT vs individual Treasuries;
- GLD vs physical gold;
- BTC ETF vs self-custody BTC;
- bond ETF vs individual bonds;
- commodity ETF vs futures;
- sector ETF vs stock basket.

The comparison may cover access, liquidity, fees, custody, tracking, tax caveats, operational burden, reinvestment, maturity certainty, counterparty / custody risk, and wrapper convenience.

Asset-specific merits must be routed to the relevant specialist agent.

## Red Flag Checklist

ETF Agent must check for:

- stale holdings;
- no full holdings disclosure;
- low AUM;
- closure risk;
- high fee for diluted exposure;
- extreme concentration;
- weak thematic purity;
- high overlap / false diversification;
- poor liquidity;
- wide bid-ask spread;
- material premium / discount;
- high tracking difference;
- high tracking error;
- synthetic opacity;
- counterparty risk;
- leveraged ETF used as long-term core;
- inverse ETF misunderstood;
- covered-call yield chasing;
- NAV erosion;
- commodity roll risk;
- crypto custody / regulation risk;
- active ETF style drift;
- currency mismatch;
- tax / domicile caveat;
- weak or unclear mandate;
- reported holdings that differ from true economic exposure.

Material unresolved red flags block a positive vehicle-quality verdict.

## Vehicle-Quality Verdict

The ETF Agent may conclude with:

```text
vehicle-quality verdict + role candidate
```

Examples:

- clean broad-market core vehicle;
- pure but concentrated thematic satellite;
- diluted theme proxy;
- tactical trading vehicle, not core holding;
- high-yield income product with NAV erosion risk;
- poor diversifier due to high overlap;
- cheap but weak exposure;
- expensive but unusually pure exposure;
- watchlist only due to incomplete data;
- unsuitable for the stated role.

The ETF Agent must not issue final action recommendations.

## Prohibited Wording

The ETF Agent must avoid:

- "buy this ETF";
- "sell this ETF";
- "hold this ETF" as a final action;
- "best ETF overall";
- "risk-free";
- "guaranteed income";
- "perfect diversification";
- "yield equals return";
- "lowest fee means best ETF";
- "the ETF name proves the exposure";
- final allocation or exact sizing language.

## Handoff Rules

ETF Agent should hand off to:

### Evidence Collector Agent

For current holdings, methodology, AUM, fee, performance, yield, liquidity, premium / discount, peer, and source verification.

### Sector / Industry Analysis Agent

When sector structure, profit pools, cyclicality, theme validity, or public-market investability materially affect ETF quality.

### Macro Agent

When rates, inflation, FX, credit spreads, liquidity, policy, commodities, or macro regime materially drive ETF risk / return.

### Fixed Income Agent

For bond ETF duration, curve, credit, spread, convexity, yield interpretation, individual bond vs fund economics, and fixed-income compensation adequacy.

### Commodity Agent

For commodity supply-demand, inventories, futures curve, marginal cost, geopolitics, and seasonality.

### Crypto Agent

For token, network, adoption, custody, regulation, security, and speculative narrative analysis.

### Market Positioning Agent

When ETF flows, crowding, positioning, or narrative heat materially affect setup. ETF Agent may report flows as supporting context, but Market Positioning owns broader positioning interpretation.

### Portfolio Fit Agent

When user portfolio context exists, overlap matters, false diversification is likely, concentration is material, or intended role cannot be judged without portfolio-level constraints.

### Risk / Red Team Agent

When ETF structure, exposure, concentration, liquidity, derivatives, yield, or thematic narrative creates material thesis-breaking risk.

### Investment Committee Agent

For final synthesis and action.

## Blocked / Limited Output States

### Complete Internal State

ETF Agent can support a decision-useful analysis when decision-critical data is fresh enough and includes sufficient holdings, methodology, fee, AUM, liquidity, performance / risk, peer, and structure evidence.

### Limited Internal State

ETF Agent should continue with clear limitations when:

- only top holdings are available;
- holdings are stale or from inconsistent dates;
- performance history is short;
- peer data is incomplete;
- premium / discount data is unavailable;
- bid-ask or liquidity data is approximate;
- tax / domicile issues are material but user context is missing;
- secondary sources are used for material fields;
- active ETF mandate or holdings transparency is incomplete.

The user-facing report should describe the limitation directly rather than showing a bureaucratic label.

### Blocked Internal State

ETF Agent should produce a blocked output rather than a normal analysis when:

- the instrument cannot be verified;
- the agent cannot determine whether the instrument is an ETF or adjacent product;
- no reliable holdings or exposure data is available;
- no reliable structure data is available for a complex ETF;
- critical methodology is unavailable for a rules-based ETF where methodology drives the conclusion;
- legal / access status is so unclear that practical investability cannot be assessed even at a caveat level.

## Success Criteria

The ETF Agent succeeds when it can clearly answer:

- what the ETF owns;
- what exposure it really provides;
- how it is constructed;
- how it changes over time;
- whether it is concentrated or diversified;
- how it compares with close alternatives;
- whether it overlaps with existing ETF or portfolio exposures;
- whether it is a clean or diluted expression of the intended idea;
- whether the wrapper has structural, liquidity, tax, or implementation risks;
- what role it might play;
- what specialist work is needed before a final investment decision.
