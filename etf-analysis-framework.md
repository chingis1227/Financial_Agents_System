# ETF Analysis Framework

<!-- reference-governance:start -->
## Reference Governance Metadata

Status: Supporting Reference  
Owner: ETF Agent  
Contributors: Evidence Collector; Portfolio Fit; Risk Red Team; Valuation/Expectations  
Used by: ETF Agent; etf-analysis skill  
Primary reference for: ETF vehicle and exposure analysis examples  
Supporting reference for: implementation quality, vehicle-quality, and portfolio-fit context  
Not responsible for: final decision; evidence readiness; routing; IC Action; agent ownership  
Freshness sensitivity: Medium  
Last reviewed: 2026-06-28  
Review trigger: Review when ETF structure, disclosure, liquidity, or wrapper-analysis conventions change.  
Owner review needed: No  
Split/index status: Indexed in implementation/reference-library-index.md  
Canonical authority: Advisory reference only. Canonical implementation documents govern active agent, skill, evidence, routing, and IC behavior.

<!-- reference-governance:end -->


## Purpose

This framework defines the standard structure and analytical principles for ETF Agent outputs.

The primary output artifact is:

```text
etf_analysis.md
```

The artifact is memo-first, modular, evidence-aware, and designed for practical investment decision support. It should explain what the ETF really owns, how it is constructed, whether it is a clean or diluted exposure vehicle, how it compares with alternatives, and what risks or overlaps matter.

It must not produce final buy / sell / hold recommendations.

## Standard `etf_analysis.md` Structure

```text
## ETF Analysis: [Ticker / Fund Name]

## 1. Executive Summary

## 2. ETF Identity

## 3. Intended Use Case / Role Candidate

## 4. Exposure Diagnosis

## 5. Holdings and Concentration

## 6. Index / Methodology / Active Process

## 7. Cost, AUM, Liquidity, and Structure

## 8. Performance and Risk History

## 9. Yield and Distribution Quality, if relevant

## 10. Peer Comparison, if relevant

## 11. Overlap / False Diversification, if relevant

## 12. Thematic / Factor / Sector Purity, if relevant

## 13. Look-Through Valuation Exposure, if relevant

## 14. Special-Risk Mode, if relevant

## 15. Tax / Domicile / Wrapper / Access Caveats

## 16. Red Flags and Open Questions

## 17. Vehicle-Quality Verdict

## 18. Handoffs Needed

## 19. Data Notes / Limitations

## Appendix: Full Holdings Snapshot, if available
```

Sections should be included only when useful. A narrow factual request does not require a full ETF due diligence memo.

## Core Analytical Questions

ETF Agent should answer:

1. What exact instrument is being analyzed?
2. What does the ETF actually own?
3. What exposure does it really provide?
4. Is the ETF a clean or diluted expression of the idea?
5. How is the ETF constructed?
6. What index, methodology, or active process drives holdings changes?
7. How does rebalancing or reconstitution affect exposure?
8. How concentrated is it?
9. What are the largest risk drivers?
10. What does it cost, and is the cost justified?
11. Is the ETF liquid enough for the likely use case?
12. Does it track what it claims to track?
13. How has it behaved historically?
14. What drove historical performance?
15. Is yield sustainable or misleading?
16. How does it compare with close alternatives?
17. Does it overlap with existing ETFs or portfolio holdings?
18. Does it create false diversification?
19. Is there material look-through valuation exposure?
20. Are there structure, tax, domicile, liquidity, methodology, or access traps?
21. What role could it plausibly play?
22. What further specialist analysis is needed?

## ETF Role Candidates

Possible role labels:

- core broad-market exposure;
- core candidate;
- satellite exposure;
- thematic satellite;
- tactical exposure;
- hedge;
- income vehicle;
- factor tilt;
- sector exposure;
- commodity access wrapper;
- crypto access wrapper;
- duration / credit vehicle;
- diversifier;
- poor diversifier;
- watchlist only;
- unsuitable for stated role;
- trading vehicle, not core holding;
- replacement candidate;
- custom-basket route candidate.

## User-Facing Status Style

Internal system states may be:

```text
Complete
Limited
Blocked
```

The main user-facing memo should not show those labels by default.

Use plain-language notes instead.

Instead of:

```text
Status: Limited
```

Use:

```text
Data note: Holdings are based on the latest issuer top-10 disclosure rather than a full holdings file, so overlap and concentration estimates are approximate.
```

Blocked example:

```text
I cannot produce a reliable ETF analysis because the instrument could not be verified as an ETF and no reliable holdings or structure data is available.
```

## Section Guidance

### 1. Executive Summary

Should include:

- what the ETF is;
- what exposure it provides;
- strongest vehicle positives;
- main red flags;
- whether it is a clean or diluted exposure;
- role candidate;
- key data limitations.

Do not include final buy / sell / hold.

### 2. ETF Identity

Include:

- ticker;
- fund name;
- issuer;
- exchange;
- domicile;
- ISIN / CUSIP where available;
- fund base currency;
- trading currency;
- share class;
- accumulating / distributing;
- hedged / unhedged;
- active / passive;
- index, if passive;
- inception date;
- ETF vs ETN / CEF / other wrapper check.

### 3. Intended Use Case / Role Candidate

Clarify or infer whether the ETF is being considered for:

- core exposure;
- satellite exposure;
- tactical trade;
- income;
- hedge;
- diversification;
- thematic exposure;
- factor tilt;
- replacement;
- comparison;
- direct asset access.

If unclear, discuss multiple plausible role candidates.

### 4. Exposure Diagnosis

Explain:

- underlying asset class;
- sector / industry / country / factor exposures;
- currency exposure;
- duration / credit / commodity / crypto beta where relevant;
- whether exposure is direct or indirect;
- whether ETF is clean, diluted, or mixed.

### 5. Holdings and Concentration

Main memo should include:

- number of holdings;
- top 10 holdings;
- top 10 weight;
- largest holding weight;
- top 20 weight where useful;
- sector / country / factor buckets;
- single-name or cluster concentration;
- key risk drivers.

Full holdings should be kept in appendix / evidence pack when available.

Use context-aware concentration judgments. Concentration is not automatically bad if it is intentional and consistent with role.

### 6. Index / Methodology / Active Process

For passive ETFs, include:

- official index;
- index provider;
- selection rules;
- weighting rules;
- rebalance / reconstitution schedule;
- caps and constraints;
- liquidity screens;
- inclusion / exclusion rules;
- methodology risks;
- investment impact of rebalancing.

For active ETFs, include:

- mandate;
- manager / issuer credibility;
- transparency;
- benchmark;
- turnover;
- style drift;
- holdings drift;
- fee justification;
- performance attribution caveats.

### 7. Cost, AUM, Liquidity, and Structure

Include:

- expense ratio;
- fee vs peers;
- AUM;
- fund age;
- issuer quality;
- closure risk;
- average volume;
- spread where available;
- premium / discount where available;
- underlying liquidity;
- replication type;
- sampling / full replication;
- synthetic / swap / futures / options exposure;
- securities lending where material;
- implementation caveats.

### 8. Performance and Risk History

Use historical performance as descriptive evidence, not a forward-looking verdict.

Include where available:

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
- peer comparison;
- tracking difference;
- tracking error.

Explain drivers of performance.

### 9. Yield and Distribution Quality

For income-relevant ETFs, distinguish:

- SEC yield;
- distribution yield;
- trailing yield;
- coupons;
- dividends;
- option premium;
- capital gains;
- return of capital;
- leverage;
- FX effects;
- NAV erosion.

High yield is not automatically attractive.

### 10. Peer Comparison

Compare by use-case fit, not universal ranking.

Useful comparison dimensions:

```text
Exposure
Holdings
Concentration
Methodology
Fee
AUM
Liquidity
Tracking
Performance
Risk
Yield
Domicile
Tax caveats
Overlap
Use-case fit
```

Possible conclusions:

- best low-cost broad exposure;
- best pure thematic exposure;
- best liquidity / trading vehicle;
- best UCITS-accessible alternative;
- best income-oriented version;
- weakest proxy despite attractive name.

### 11. Overlap / False Diversification

Show where relevant:

- common holdings count;
- overlap by weight;
- top-10 overlap;
- top-25 overlap where useful;
- sector overlap;
- country overlap;
- factor overlap;
- duration / credit / commodity overlap where relevant;
- user portfolio overlap if portfolio context exists.

Flag false diversification when different-looking ETFs repeat the same economic exposure.

### 12. Thematic / Factor / Sector Purity

For thematic ETFs, classify holdings where feasible:

- pure-play;
- core beneficiary;
- adjacent beneficiary;
- generic exposure;
- weak / non-thematic holding.

For factor ETFs, check whether methodology and holdings actually deliver the stated factor exposure.

Do not accept ETF marketing labels without holdings and methodology support.

### 13. Look-Through Valuation Exposure

Use when valuation is material to the ETF's risk, peer comparison, or intended role.

Review where available:

- ETF-level valuation metrics;
- category valuation metrics;
- top-holdings valuation profile;
- P/E;
- P/B;
- P/S;
- earnings yield;
- dividend yield where relevant;
- expensive-name concentration;
- valuation versus peers;
- growth / duration-like equity exposure;
- value / quality / profitability tilt.

This section should identify valuation exposure, not produce a final valuation verdict. Full valuation and implied-expectations work belongs to Valuation & Expectations or the relevant asset-class specialist.

### 14. Special-Risk Mode

Use for:

- leveraged ETFs;
- inverse ETFs;
- covered-call / options-income ETFs;
- volatility-linked ETFs;
- synthetic / swap-based ETFs;
- commodity futures ETFs;
- crypto ETFs;
- opaque active ETFs;
- low-AUM niche ETFs.

Explain:

- payoff mechanics;
- daily reset;
- compounding;
- volatility drag;
- derivative exposure;
- roll mechanics;
- collateral;
- counterparty risk;
- distribution sustainability;
- NAV erosion;
- intended holding period;
- why yield or historical returns may mislead.

### 15. Tax / Domicile / Wrapper / Access Caveats

Flag when relevant:

- US ETF vs UCITS;
- accumulating vs distributing;
- withholding caveats;
- K-1 / partnership issues;
- PFIC caveats;
- US situs / estate-tax caveats;
- PRIIPs / KID availability;
- EU retail access restrictions for US ETFs;
- sanctions / country exposure;
- crypto regulatory status;
- listing / delisting / eligibility issues.

Do not provide personalized tax or legal advice.

### 16. Red Flags and Open Questions

Call out material unresolved issues:

- missing holdings;
- stale data;
- weak disclosure;
- low AUM;
- closure risk;
- high fee for diluted exposure;
- extreme concentration;
- weak thematic purity;
- false diversification;
- poor liquidity;
- wide spread;
- material premium / discount;
- tracking problems;
- synthetic opacity;
- counterparty risk;
- misunderstood leverage;
- NAV erosion;
- commodity roll risk;
- crypto custody / regulation risk;
- active style drift;
- tax / domicile issue;
- reported holdings not matching economic exposure.

### 17. Vehicle-Quality Verdict

Allowed format:

```text
Vehicle-quality verdict: [clear vehicle assessment], with [key positive] but [key limitation]. Plausible role: [role candidate].
```

Good examples:

```text
Vehicle-quality verdict: Clean broad-market core candidate, with low fee, strong liquidity, and minimal tracking concerns.
```

```text
Vehicle-quality verdict: Pure but concentrated thematic satellite. Useful for targeted exposure, but not a diversified core holding.
```

```text
Vehicle-quality verdict: Weak proxy for the stated theme. The ETF label suggests AI exposure, but holdings are dominated by generic mega-cap technology names.
```

```text
Vehicle-quality verdict: Income-oriented product with material NAV erosion and option-overwrite tradeoff. Yield should not be treated as free return.
```

Bad examples:

```text
Buy this ETF.
```

```text
This is the best ETF.
```

```text
Allocate 10%.
```

### 18. Handoffs Needed

Specify downstream needs:

- Evidence Collector;
- Sector / Industry;
- Macro;
- Fixed Income;
- Commodity;
- Crypto;
- Market Positioning;
- Portfolio Fit;
- Risk / Red Team;
- Investment Committee.

### 19. Data Notes / Limitations

Include compact source and as-of notes for:

- holdings;
- AUM;
- fee;
- methodology;
- performance;
- yield;
- liquidity;
- premium / discount;
- overlap;
- peers.

Full source details belong in the evidence pack.

## Red Flags That Block Positive Vehicle-Quality Verdict

ETF Agent should not give a positive vehicle-quality verdict if unresolved material issues include:

- holdings cannot be verified;
- ETF does not match stated theme;
- severe liquidity problem;
- high closure risk;
- extreme premium / discount;
- opaque synthetic exposure;
- misunderstood leverage or inverse exposure;
- high yield driven by NAV decay;
- severe false diversification;
- material tax / domicile issue ignored by user;
- active ETF with unclear mandate / style drift;
- commodity futures ETF misunderstood as spot exposure;
- crypto ETF structure misunderstood;
- reported holdings obscure true economic exposure.

## ETF Comparison Framework

For ETF comparisons, structure the conclusion by use case:

```text
Best low-cost broad exposure
Best clean / pure thematic exposure
Best liquidity / trading vehicle
Best UCITS-accessible alternative
Best income-oriented version
Best diversified version
Weakest proxy despite attractive name
Most overlap with existing holdings
Most structure risk
```

Do not produce one universal ranking unless the user has defined a single explicit objective.

## ETF Discovery / Shortlist Framework

When user asks for ETF ideas:

1. Define intended exposure.
2. Define investable universe.
3. Separate US-listed and UCITS / non-US options when jurisdiction is unknown.
4. Exclude obvious mismatches.
5. Verify exposure relevance.
6. Check basic investability.
7. Check AUM / liquidity.
8. Check fees.
9. Check holdings purity.
10. Flag young / low-AUM / low-liquidity caveats.
11. Produce shortlist.
12. Recommend which ETFs deserve full due diligence.

ETF name alone is never enough.

## Replacement / Substitution Framework

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

Allowed conclusion:

```text
This replacement reduces fees and improves liquidity but increases mega-cap growth concentration.
```

Prohibited conclusion:

```text
You should replace A with B now.
```

## ETF-vs-Direct-Holding Framework

When relevant, compare ETF wrapper to direct exposure:

- access;
- liquidity;
- fees;
- custody;
- tracking;
- tax caveats;
- operational burden;
- reinvestment;
- maturity certainty;
- counterparty / custody risk;
- diversification.

Examples:

- TLT vs individual Treasuries;
- GLD vs physical gold;
- BTC ETF vs self-custody BTC;
- bond ETF vs individual bonds;
- sector ETF vs stock basket.

ETF Agent may describe wrapper tradeoffs but must route asset-specific merits to specialist agents.

## Professional Source Standard

Preferred sources:

- issuer holdings files;
- issuer fact sheets;
- prospectuses;
- index methodology documents;
- regulatory filings;
- exchange data;
- official NAV / premium-discount sources;
- recognized financial data providers;
- ETFRC / similar tools as secondary overlap aids;
- Morningstar / ETF.com / ETF Database as fallback and comparison sources.

Avoid relying on unsourced summaries, SEO pages, stale aggregators, or AI-generated summaries for material ETF claims.

## Final Output Principle

The ETF memo should be concise but decision-useful:

```text
What do I actually own, how does this wrapper behave, where does it overlap, what can go wrong, and what further work is required before action?
```
