# Valuation & Expectations Framework

## Objective

This framework defines the practical checklist used by the Valuation & Expectations Agent when producing `valuation_expectations.md`.

The framework is designed for public listed equities and supports global coverage, with US-first source depth where available.

## Core Output Structure

```text
## Valuation & Expectations Analysis

## 1. Valuation Summary
## 2. What Is Priced In
## 3. Current Valuation Snapshot
## 4. Absolute vs Quality-Adjusted Valuation
## 5. Primary Valuation Method
## 6. Supporting Valuation Methods
## 7. Scenario-Implied Valuation Range
## 8. Return Bridge
## 9. Margin of Safety and Asymmetry
## 10. Key Valuation Risks
## 11. What Must Be True
## 12. What Would Break the Valuation Case
## 13. Monitoring Signals
## 14. Handoff to Investment Committee

## Appendix
A. Source and Timestamp Log
B. Data Confidence
C. Valuation Confidence
D. Calculation Summary
E. Peer Set and Comparability
F. Multiples Table
G. Accounting Adjustments
H. Sensitivity Summary
I. Misleading Metric Checklist
```

## Main Report Rules

The main report must be clean and decision-useful.

Include only:

- valuation conclusion;
- current valuation setup;
- expectations embedded in price;
- key scenario ranges;
- major risk/reward drivers;
- critical caveats;
- what must be true;
- what would break the case;
- handoff.

Move technical detail to appendix unless it changes the conclusion.

## Valuation Labels

The agent must provide two separate valuation labels:

```text
12-24M Valuation Setup:
Attractive / Reasonable / Fair / Demanding / Stretched / Speculative

3-5Y Intrinsic / Compounding View:
Attractive / Reasonable / Fair / Demanding / Stretched / Speculative
```

These labels are valuation judgments, not investment recommendations.

## Minimum Dataset

### Core required fields

- current price;
- price date;
- diluted share count;
- market cap;
- capital structure;
- net debt / net cash;
- enterprise value where relevant;
- latest financial statements;
- revenue base;
- earnings or loss base;
- cash flow or cash burn base;
- balance sheet / liquidity;
- fiscal year basis;
- reporting currency;
- trading currency;
- valuation currency;
- source timestamps.

### Sector-specific fields

#### Banks

- P/TBV;
- ROE;
- ROTCE;
- CET1;
- NIM;
- credit losses;
- loan growth;
- deposit cost;
- capital return capacity.

#### Insurance

- P/B;
- P/TBV;
- ROE;
- combined ratio;
- underwriting margin;
- investment income;
- reserve adequacy;
- solvency capital.

#### REITs

- FFO;
- AFFO;
- NAV;
- cap rates;
- occupancy;
- same-store NOI;
- leverage;
- dividend coverage.

#### SaaS / Software

- revenue / ARR growth;
- gross margin;
- NRR / retention where available;
- Rule of 40;
- FCF margin;
- SBC;
- CAC payback where available;
- implied mature margin.

#### Energy / Natural Resources

- production;
- reserves;
- NAV;
- commodity assumptions;
- breakeven price;
- FCF yield;
- capex intensity;
- commodity sensitivity.

#### Cyclicals / Industrials

- mid-cycle revenue;
- mid-cycle margin;
- backlog;
- order trends;
- peak/trough earnings;
- normalized FCF.

#### Biotech / Pharma

- pipeline stage;
- probability-adjusted NPV;
- patent cliff;
- R&D productivity;
- cash runway;
- product concentration;
- regulatory milestones.

## Source Hierarchy

### Tier 1 - Official / primary

- annual reports;
- 10-K / 10-Q / 20-F / 6-K;
- earnings releases;
- investor presentations;
- official company filings;
- exchange data;
- regulator filings.

### Tier 2 - Reliable market and estimate data

- Bloomberg;
- FactSet;
- LSEG / Refinitiv;
- S&P Capital IQ;
- Morningstar;
- Koyfin;
- Visible Alpha;
- official exchange / index providers.

### Tier 3 - Professional context

- CFA Institute;
- Damodaran / NYU;
- McKinsey;
- Morgan Stanley / asset-manager research;
- J.P. Morgan Asset Management;
- BlackRock;
- reputable sell-side research.

### Tier 4 - Use with caution

- financial websites;
- scraped datasets;
- blogs;
- unsourced summaries;
- old articles;
- AI-generated summaries.

Tier 4 sources cannot support core valuation numbers unless verified.

## Required Cross-Checks

Where data is available, verify:

```text
Market cap = price x diluted shares
EV = market cap + debt + leases + preferred equity + minority interest - cash
P/E = price / EPS
EV/EBITDA = EV / EBITDA
FCF yield = FCF / market cap
Net debt = debt - cash
```

Flag inconsistencies.

## Peer Comparability Scoring

Peer comparison is required when possible, but cannot be mechanical.

Score peers on:

- business model;
- revenue model;
- growth;
- margin structure;
- ROIC;
- capital intensity;
- leverage;
- cyclicality;
- geography;
- regulation;
- accounting comparability.

Peer analysis must state:

```text
Reliable
Partially reliable
Weak / directional only
```

## Historical Range Rules

Historical valuation ranges are context, not verdict.

Adjust interpretation for:

- rate regime;
- growth regime;
- margin structure;
- business mix changes;
- ROIC changes;
- leverage changes;
- accounting changes;
- cycle position.

## Accounting Adjustment Checklist

Review:

- reported vs adjusted EPS;
- analyst-normalized EPS;
- SBC;
- restructuring;
- impairments;
- acquisition amortization;
- lease adjustments;
- pension costs;
- tax normalization;
- FX;
- working capital distortions;
- litigation charges;
- discontinued operations;
- recurring "one-offs".

## Capital Allocation Checklist

Assess valuation impact of:

- reinvestment;
- dividends;
- buybacks;
- net buyback yield;
- M&A;
- debt paydown;
- dilution;
- ROIC on reinvestment;
- per-share value creation.

## Share Count Bridge

Review:

- basic shares;
- diluted shares;
- SBC dilution;
- options / RSUs;
- convertibles;
- warrants;
- equity issuance;
- buybacks;
- net share count change.

## Scenario Valuation Template

```text
Bear Case:
- Business outcome:
- Key assumptions:
- Valuation method:
- Implied value range:
- Downside:
- What causes this case:

Base Case:
- Business outcome:
- Key assumptions:
- Valuation method:
- Implied value range:
- Upside/downside:
- What must be true:

Bull Case:
- Business outcome:
- Key assumptions:
- Valuation method:
- Implied value range:
- Upside:
- What causes this case:
```

## Return Bridge Template

```text
Expected return drivers:
- Revenue growth:
- Margin expansion/compression:
- EPS growth:
- FCF growth:
- Multiple expansion/compression:
- Dividends:
- Buybacks:
- Deleveraging:
- FX:
- Cycle recovery:
```

## Required Risk Flags

```text
[ ] Valuation depends on multiple expansion
[ ] Terminal value dominates valuation
[ ] Consensus estimates appear aggressive
[ ] Margins are above normalized level
[ ] EPS growth is buyback-driven
[ ] FCF is temporarily inflated
[ ] Peer set is weak
[ ] Leverage amplifies downside
[ ] Dilution is material
[ ] Rate sensitivity is high
[ ] Regulatory/legal overhang affects valuation
[ ] Accounting adjustments are material
[ ] Sell-side target dispersion is high
[ ] Path to profitability is uncertain
[ ] Margin of safety is limited
[ ] Permanent capital impairment risk exists
[ ] Current premium may be sentiment-driven
```

## Misleading Metric Checklist

Flag materially misleading metrics in the main report.

Full appendix checklist:

```text
[ ] P/E misleading
[ ] Forward P/E misleading
[ ] EV/EBITDA misleading
[ ] EV/Sales misleading
[ ] FCF yield misleading
[ ] P/B misleading
[ ] Adjusted EPS misleading
[ ] Peer multiple misleading
[ ] Historical range misleading
[ ] Consensus estimate misleading
```

## Trap Diagnostics

```text
Value Trap Risk:
Low multiple may be justified by deteriorating fundamentals.

Quality Trap Risk:
High-quality business may already price in too much perfection.

Growth Trap Risk:
Growth may fail to convert into FCF or per-share value.
```

## Advanced Valuation Dependency Checks

### Terminal Value / Long-Duration Dependency

Flag when valuation relies heavily on:

- terminal value;
- exit multiple;
- mature margins;
- distant cash flows;
- long explicit forecast period;
- low discount-rate assumptions;
- continued high growth beyond visible evidence.

Main report should surface this only when it changes the valuation conclusion. Appendix should include the detailed sensitivity.

### Multiple Durability

Assess whether the current premium or discount is durable.

Check:

- quality-backed premium;
- scarcity premium;
- sentiment-backed premium;
- rate-sensitive premium;
- justified discount;
- temporary discount;
- risk of multiple compression;
- risk of unjustified mean-reversion assumption.

### Liquidity / Float / Market Access

When material, assess whether valuation requires a liquidity or market-access adjustment.

Check:

- market cap;
- free float;
- average daily trading volume;
- ownership concentration;
- ADR liquidity;
- index inclusion / exclusion;
- governance or country discount;
- small-cap liquidity premium.

### Regulatory / Legal Overhang

When material, reflect regulatory or legal overhang through:

- valuation discount;
- required-return adjustment;
- scenario downside;
- confidence downgrade;
- probability-weighted liability;
- terminal value haircut.

Full legal adjudication remains with Risk / Red Team.

### Sum-of-the-Parts Trigger

Use SOTP when consolidated valuation obscures materially different assets or segment economics.

Triggers:

- conglomerate structure;
- holding company discount;
- listed subsidiaries;
- significant non-core assets;
- mixed financial and industrial businesses;
- materially different growth, margin, or capital intensity by segment;
- hidden real estate, investment assets, or regulated assets.
## Strategic / M&A Value

Strategic value may be included only when supported by evidence.

Otherwise, treat it as upside optionality, not base case.

Evidence may include:

- sector consolidation history;
- unique assets;
- credible buyer universe;
- precedent transactions;
- regulatory feasibility;
- activist pressure;
- prior bids or reported interest.

## Structured Handoff Block

Every report must end with:

```text
valuation_status:
12_24m_valuation_label:
3_5y_valuation_label:
primary_valuation_method:
supporting_methods:
scenario_value_range:
bear_case_downside:
base_case_upside:
bull_case_upside:
implied_expectations:
what_must_be_true:
what_breaks_case:
margin_of_safety:
valuation_asymmetry:
data_confidence:
valuation_confidence:
risk_flags:
misleading_metrics:
monitoring_signals:
handoff_note:
```

## Final Standard

A good Valuation & Expectations output does not say only:

```text
The stock trades at 28x forward P/E.
```

It says:

```text
The stock trades at 28x forward EPS. This premium is partly supported by high ROIC, durable FCF conversion, and strong balance sheet quality. However, the current price implies sustained high-single-digit revenue growth, stable margins, and limited multiple compression. The valuation is reasonable only if those expectations remain intact; otherwise, downside is driven primarily by multiple compression and lower FCF conversion.
```

