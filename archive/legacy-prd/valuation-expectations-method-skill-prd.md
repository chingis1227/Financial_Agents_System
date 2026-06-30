# Valuation & Expectations Method Skill PRD

## Purpose

The Valuation & Expectations Method Skill defines how the Valuation & Expectations Agent evaluates public equity valuation in a disciplined, expectations-led, anti-hallucination framework.

The skill should help the agent avoid shallow conclusions such as:

```text
The stock is expensive because P/E is above history.
```

Instead, it should produce conclusions such as:

```text
The stock trades at a premium valuation, but part of the premium is justified by high ROIC, durable FCF growth, and strong balance sheet quality. However, reverse-implied expectations leave limited room for margin compression or growth disappointment.
```

## Core Doctrine

```text
Valuation = current price vs realistic future expectations.
```

The agent evaluates whether current valuation is justified by:

- growth;
- margins;
- FCF;
- ROIC;
- reinvestment needs;
- balance sheet risk;
- dilution;
- required return;
- terminal assumptions;
- market-implied expectations.

## Required Analytical Steps

## 1. Establish Data Integrity

Before analysis, verify:

- current share price and date;
- diluted share count;
- market cap;
- enterprise value bridge;
- net debt / net cash;
- latest financial statement period;
- reporting currency;
- trading currency;
- fiscal year basis;
- consensus estimate date, if used;
- peer data date, if used.

Do not invent missing numbers.

If data is incomplete, classify output as Complete, Limited, or Blocked.

## 2. Select Valuation Context

Identify:

- sector;
- business model;
- lifecycle stage;
- investment style;
- profitability status;
- cash-flow visibility;
- capital intensity;
- cyclicality;
- balance sheet risk.

Then apply relevant overlays:

```text
Quality compounder
Growth
Value
Cyclical
Turnaround
Distressed
Asset play
Yield / income
Speculative long-duration
```

## 3. Select Primary and Supporting Methods

The agent must explicitly select:

```text
Primary valuation method
Supporting valuation methods
Methods considered unreliable or not applicable
```

Examples:

- Quality compounder: FCF compounding / DCF primary; P/E and FCF yield supporting.
- Bank: P/TBV vs ROTCE primary; P/E and dividend capacity supporting.
- REIT: NAV / AFFO primary; dividend yield supporting.
- SaaS growth: EV/Gross Profit and implied mature FCF margin primary.
- Cyclical: mid-cycle EV/EBIT or EV/EBITDA primary.
- Biotech: probability-adjusted NPV primary.

## 4. Build Valuation Forecast Layer

The agent builds a valuation forecast layer, not a full operating model.

Minimum forecast elements where relevant:

- revenue growth;
- gross margin;
- EBIT / EBITDA margin;
- tax normalization;
- interest expense;
- EPS;
- FCF;
- FCF conversion;
- reinvestment needs;
- share count;
- dilution;
- buybacks;
- terminal growth;
- terminal multiple.

## 5. Assess Current Valuation

Use relevant metrics:

### Earnings-based

- trailing P/E;
- forward P/E;
- normalized P/E;
- adjusted P/E;
- EPS CAGR;
- earnings yield;
- PEG where useful.

### Enterprise value

- EV/Sales;
- EV/Gross Profit;
- EV/EBITDA;
- EV/EBIT;
- EV/NOPAT;
- EV/FCF;
- EV/Invested Capital.

### Cash flow

- FCF yield;
- P/FCF;
- EV/FCF;
- FCFF;
- FCFE;
- owner earnings;
- FCF conversion.

### Asset-based

- P/B;
- P/TBV;
- NAV;
- replacement value;
- liquidation value.

### Shareholder yield

- dividend yield;
- buyback yield;
- net buyback yield;
- shareholder yield;
- payout ratio;
- FCF payout ratio.

## 6. Assess Absolute and Quality-Adjusted Valuation

The agent must separate:

```text
Absolute valuation
Quality-adjusted valuation
```

Absolute valuation asks:

```text
Is the stock expensive or cheap versus market alternatives, rates, yields, history, and current cash generation?
```

Quality-adjusted valuation asks:

```text
Is the premium or discount justified by growth, ROIC, FCF durability, balance sheet quality, moat, and risk?
```

## 7. Reverse-Engineer Market Expectations

Estimate what the current price implies for:

- revenue CAGR;
- EPS growth;
- EBIT margin;
- EBITDA margin;
- FCF margin;
- ROIC;
- reinvestment;
- terminal growth;
- terminal multiple;
- forecast duration;
- cost of capital.

Required blocks:

```text
What must be true?
What would break the valuation case?
```

## 8. Build Scenario Valuation

Required scenarios:

```text
Bear
Base
Bull
```

Each scenario should include:

- key business assumptions;
- valuation method;
- implied value range;
- upside/downside;
- key dependency;
- key failure point.

No single-point target price.

## 9. Build Return Bridge

Explain expected shareholder return drivers:

- revenue growth;
- margin expansion/compression;
- EPS growth;
- FCF growth;
- multiple expansion/compression;
- dividends;
- buybacks;
- deleveraging;
- FX;
- cycle recovery.

Distinguish:

```text
Return from compounding
Return from re-rating
Return from capital returns
Return from balance sheet repair
```

## 10. Reconcile Valuation Methods

If DCF, multiples, peer analysis, historical range, and FCF yield give different signals, explain why.

Required assessment:

- which method carries most weight;
- why methods diverge;
- which methods are misleading;
- what this implies for confidence.

## 11. Assess Valuation Risk Flags

Required checklist:

- valuation depends on multiple expansion;
- terminal value dominates;
- consensus appears aggressive;
- margins above normalized level;
- EPS growth driven by buybacks;
- FCF temporarily inflated;
- peer set weak;
- leverage high;
- dilution material;
- rate sensitivity high;
- accounting adjustments material;
- target price dispersion high;
- path-to-profitability uncertain;
- margin of safety limited;
- permanent capital impairment risk.

## 12. Trap Diagnostics

Explicitly test:

```text
Value trap risk
Quality trap risk
Growth trap risk
```

### Value trap

Low multiple may be justified by structural decline, weak FCF, leverage, poor ROIC, or governance risk.

### Quality trap

High-quality company may still be unattractive if valuation prices perfection.

### Growth trap

High growth may fail to create value if unit economics, reinvestment, dilution, or FCF conversion are weak.

## 13. Advanced Valuation Dependency Checks

The agent must run additional dependency checks when they materially affect the valuation conclusion.

### Terminal value / long-duration dependency

Flag when valuation relies heavily on distant cash flows, mature margin assumptions, terminal growth, or exit multiples.

Check:

- terminal value share of DCF where available;
- reliance on terminal multiple;
- reliance on mature margin expansion;
- duration of growth assumptions;
- WACC / cost of equity sensitivity;
- near-term cash-flow support versus distant cash-flow dependency.

### Multiple durability

Assess whether the current premium or discount can persist.

Check:

- why the current multiple exists;
- whether it is supported by ROIC, growth, FCF durability, balance sheet quality, or scarcity value;
- whether it is driven by sentiment, hype, rate regime, or temporary factors;
- what could cause multiple compression;
- whether peer premium / discount is sustainable.

### Catalyst timing / valuation realization risk

The agent does not own catalyst discovery, but must assess whether valuation upside depends on catalyst timing or re-rating.

Check:

- whether expected return can come from earnings / FCF compounding without multiple expansion;
- whether upside requires re-rating;
- whether the valuation case risks becoming a value trap without a catalyst;
- what event or evidence would likely change market expectations.

### Liquidity, float, and market-access discount

When material, assess whether valuation discount or required return is affected by:

- market cap and average daily trading volume;
- free float;
- ownership concentration;
- ADR liquidity;
- index inclusion / exclusion;
- small-cap liquidity premium;
- country, governance, or market-access discount.

Do not treat a peer discount as clean mispricing if liquidity, float, governance, or market-access limitations justify part of the discount.

### Regulatory / legal valuation overhang

The agent does not adjudicate legal risk, but must reflect material regulatory or legal overhangs as valuation inputs.

Possible treatments:

- multiple discount;
- higher required return;
- scenario downside;
- probability-weighted liability;
- capital requirement impact;
- revenue or margin impairment;
- terminal value haircut;
- lower valuation confidence.

### Sum-of-the-parts valuation

Use sum-of-the-parts valuation when consolidated multiples obscure materially different segment economics.

SOTP may be required for:

- conglomerates;
- holding companies;
- listed subsidiaries;
- non-core assets;
- materially different growth / margin / capital intensity by segment;
- regulated and unregulated business mixes;
- hidden real estate, investment assets, or financial assets.

### Tax, FX, and currency discipline

Normalize tax assumptions and currency effects where material.

Check:

- reported tax rate versus normalized tax rate;
- cash tax rate;
- NOLs and tax credits;
- one-off tax benefits;
- jurisdiction mix;
- reporting currency;
- trading currency;
- valuation currency;
- FX rate date;
- ADR ratio where relevant;
- FX sensitivity when it materially affects per-share value.
## 14. Confidence

Main report should include confidence only if it affects the conclusion.

Appendix must distinguish:

```text
Data Confidence
Valuation Confidence
```

Data Confidence depends on:

- source quality;
- freshness;
- completeness;
- reconciliation;
- consistency.

Valuation Confidence depends on:

- cash-flow visibility;
- cyclicality;
- forecast uncertainty;
- peer comparability;
- terminal value dependency;
- sensitivity to assumptions;
- accounting noise.

## 15. Monitoring Signals

Monitoring signals must be tied to implied expectations.

Examples:

```text
If revenue growth falls below X, current multiple becomes harder to justify.
If EBIT margin falls below Y, base-case valuation breaks.
If dilution exceeds Z, per-share value creation weakens.
If FCF conversion stays below A, headline EPS multiple is misleading.
```

## 16. Appendix Requirements

The appendix should include:

- source table;
- price and data timestamps;
- calculation summary;
- peer set;
- peer comparability scoring;
- assumption table;
- method reconciliation;
- sensitivity summary;
- accounting adjustments;
- data confidence;
- valuation confidence;
- misleading metric checklist.

