# Fixed Income Analysis Framework

<!-- reference-governance:start -->
## Reference Governance Metadata

Status: Supporting Reference  
Owner: Fixed Income Agent  
Contributors: Macro Agent; Risk Red Team; Valuation/Expectations  
Used by: Fixed Income Agent; fixed-income-analysis skill  
Primary reference for: fixed-income analysis framework examples  
Supporting reference for: duration, spread, credit, and macro-rate context  
Not responsible for: final decision; evidence readiness; routing; IC Action; agent ownership  
Freshness sensitivity: Medium  
Last reviewed: 2026-06-28  
Review trigger: Review when fixed-income skill contract, instrument taxonomy, or market-structure assumptions change.  
Owner review needed: No  
Split/index status: Indexed in implementation/reference-library-index.md  
Canonical authority: Advisory reference only. Canonical implementation documents govern active agent, skill, evidence, routing, and IC behavior.

<!-- reference-governance:end -->


## Purpose

This framework defines the output structure, evidence rules, metric discipline, scenario rules, verdict labels, and handoff format for fixed income analysis.

## Output - fixed_income_analysis.md

### 1. Executive Fixed Income Verdict

Include:

- instrument / exposure;
- specialist verdict;
- one-sentence investment meaning;
- primary support;
- primary risk;
- data confidence;
- whether Risk / Red Team escalation is required.

Do not use final buy / sell / hold language.

### 2. Instrument / Exposure Identity

Include:

- issuer / fund;
- instrument type;
- ticker / CUSIP / ISIN where available;
- maturity / weighted maturity;
- coupon type;
- currency;
- seniority;
- secured status;
- callable / convertible / floating / inflation-linked features;
- individual bond vs fund / ETF.

### 3. Role Candidate, Not Portfolio Decision

Classify possible role:

- income sleeve candidate;
- defensive / ballast candidate;
- duration hedge candidate;
- tactical duration exposure;
- credit carry exposure;
- inflation-linked exposure;
- liquidity sleeve;
- cash alternative candidate;
- yield-enhancement candidate;
- not suitable as safe-income substitute.

Portfolio Fit owns final suitability.

### 4. Current Market Compensation

Include relevant metrics:

- price / NAV;
- yield to maturity;
- yield to worst;
- yield to call;
- SEC yield;
- distribution yield;
- real yield;
- tax-equivalent yield framework;
- spread / OAS;
- curve point;
- as-of date / time.

Explain which yield matters most.

### 5. Return Driver Decomposition

Decompose expected fixed-income return drivers:

- carry;
- roll-down;
- rate movement;
- curve movement;
- spread movement;
- credit loss;
- liquidity;
- optionality;
- inflation;
- FX;
- fees / expenses.

### 6. Duration / Curve / Convexity Risk

Analyze:

- duration;
- maturity;
- rate shock sensitivity;
- curve steepening / flattening;
- convexity;
- extension / prepayment risk;
- long-duration downside.

### 7. Credit / Issuer / Collateral Quality

Analyze where relevant:

- rating and outlook;
- issuer quality;
- leverage;
- coverage;
- cash flow;
- debt maturity wall;
- liquidity;
- refinancing;
- seniority;
- collateral;
- covenant context;
- expected loss / recovery context.

### 8. Liquidity / Structure / Legal-Economic Terms

Analyze:

- issue size;
- trading liquidity;
- bid/ask;
- fund liquidity vs underlying liquidity;
- call features;
- conversion features;
- subordination;
- coupon deferral;
- collateral;
- tranche structure;
- private lock-up.

### 9. Individual Bond vs Fund Economics

For individual bonds:

- maturity;
- repayment if no default;
- hold-to-maturity vs mark-to-market risk;
- call risk;
- default risk;
- liquidity risk.

For funds:

- rolling exposure;
- no fixed maturity for investor by default;
- NAV fluctuation;
- duration and credit drift;
- distribution risk;
- ETF discount / premium;
- fund liquidity mismatch.

### 10. Scenario & Downside Stress Test

Minimum scenario coverage:

- rates up;
- rates down;
- curve shift;
- spread widening;
- credit deterioration;
- liquidity stress;
- call / prepayment / extension;
- inflation / real-rate shock;
- FX shock where relevant.

Use approximate math where useful:

```text
Approximate rate impact = -duration x rate shock
```

Do not imply precision beyond available data.

### 11. Relative Value / Alternatives

Compare with:

- Treasury alternatives;
- rating bucket;
- maturity bucket;
- peer bonds;
- bond ETFs;
- money market / T-bills / CDs;
- TIPS vs nominals;
- munis vs taxable equivalents;
- loan / FRN alternatives;
- cash-like alternatives.

### 12. Risk / Red Team Escalation

State whether escalation is:

- not required;
- recommended;
- required before action.

Explain why.

### 13. Monitoring Triggers

Include specific triggers by instrument type.

Examples:

- yield / real yield threshold;
- spread widening;
- downgrade / watch;
- leverage deterioration;
- maturity wall;
- NAV discount;
- liquidity deterioration;
- call / reset date;
- distribution cut;
- covenant issue;
- FX depreciation;
- reserves decline;
- collateral deterioration.

### 14. Evidence Notes and Limitations

Include:

- source basis;
- as-of dates;
- missing data;
- confidence impact;
- whether verdict is decision-grade.

Do not hide material limitations in footnotes.

### 15. Structured Handoff

Include handoffs to:

- Macro;
- ETF;
- Risk / Red Team;
- Portfolio Fit;
- Investment Committee;
- Evidence Collector.

## Metric Discipline

Use risk-block metrics, not terminal-style overload.

Core metrics where relevant:

- price / NAV;
- YTM;
- YTW;
- SEC yield;
- distribution yield;
- maturity / WAM;
- duration;
- convexity;
- spread / OAS;
- rating;
- seniority;
- call schedule;
- coupon type;
- issue size;
- liquidity;
- real yield;
- breakeven;
- FX exposure;
- NAV discount / premium;
- expense ratio.

## Confidence Blocks

Use:

```text
High
Medium
Low
Insufficient Basis
```

Confidence reflects evidence quality, freshness, structure visibility, and scenario clarity. It is not a probability forecast.

## Internal Status

Internal system status may be:

```text
Complete
Limited
Blocked
```

User-facing output should use plain language.

## User-Facing Style

Explain the investment meaning first.

Technical terms are allowed, but must be explained when material.

Appendices may be more technical.

## Specialist Verdict Labels

Use:

- Attractive risk-adjusted fixed-income exposure;
- Acceptable carry, with identified risks;
- Useful defensive / ballast candidate;
- Useful tactical duration exposure;
- Useful inflation-linked exposure;
- Credit carry opportunity, risk compensated;
- Compensation insufficient for risk;
- Yield trap / uncompensated downside risk;
- Structure or liquidity risk dominates yield;
- Not suitable as "safe income";
- Not decision-grade due to missing or stale data;
- Requires Risk / Red Team escalation before action.

Do not use numeric scores.

## Prohibited Behavior

Do not:

- treat yield as enough;
- call bond funds principal-protected;
- imply hold-to-maturity economics for ETFs;
- ignore call / prepayment / extension risk;
- accept ratings as conclusions;
- hide missing data;
- use final action language;
- overstate safety.
