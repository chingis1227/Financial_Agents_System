# Macro Regime Framework

## Objective

This framework defines how the Macro Agent diagnoses macro regimes, separates confirmed regimes from risk overlays, applies regime-change discipline, maintains macro baseline memory, handles scenarios, and maps macro regimes into asset sensitivity.

It supports:

```text
macro_regime_baseline.md
macro_weekly_delta.md
macro_event_update.md
macro_market_pulse.md
macro_sensitivity.md
```

## Core Principle

```text
A macro regime is not a slogan. It is a layered diagnosis of growth, inflation, policy, liquidity, credit, cross-asset confirmation, transmission, and market discounting.
```

## Layered Regime Taxonomy

Macro Agent should describe the regime through layers:

```text
1. Core Growth x Inflation Regime
2. Dominant Regime Driver
3. Policy / Rates / Liquidity Stance
4. Current Risk Overlay
5. Dominant Transmission Channel
6. Asset Sensitivity Map
```

Avoid relying only on labels such as soft landing, no landing, stagflation, or Goldilocks. These can be used as shorthand only after the mechanism is described.

## 1. Core Growth x Inflation Regime

Classify the core backdrop:

```text
Resilient growth + disinflation
Resilient growth + sticky inflation
Reacceleration / reflation
Growth slowdown + disinflation
Growth slowdown + sticky inflation
Stagflationary pressure
Recessionary disinflation
Supply-shock inflation pressure
Mixed / transition regime
```

## 2. Dominant Regime Driver

Classify the dominant driver:

```text
Growth-led
Inflation-led
Fed / rates-led
Liquidity / credit-led
Market-pricing-led
Fiscal / term-premium-led
FX / dollar-led
G3 policy-divergence-led
Commodity / supply-shock-led
Mixed transition
```

For the selected driver, state:

```text
why it dominates
which blocks confirm it
which blocks contradict it
what would weaken it
what regime it pushes toward
```

## 3. Policy / Rates / Liquidity Stance

Assess:

```text
Fed stance
real-yield pressure
yield curve message
market-implied policy path
liquidity impulse
credit conditions
ECB / BoJ divergence when material
```

Do not confuse market pricing with official policy intent.

## 4. Confirmed Regime vs Risk Overlay

Separate:

```text
Confirmed Macro Regime = what the majority of hard data, policy, liquidity, credit, and market pricing currently support.
Current Risk Overlay = what could become dominant if specific triggers confirm.
```

Examples:

```text
Confirmed regime: resilient disinflationary expansion
Risk overlay: higher-for-longer real-yield pressure

Confirmed regime: late-cycle expansion with sticky services inflation
Risk overlay: credit-caution risk from widening spreads and tighter lending standards

Confirmed regime: moderate Japan reflation normalization
Risk overlay: carry-trade unwind / JPY intervention risk
```

Rules:

- Do not describe a risk overlay as the confirmed regime without cross-block confirmation.
- A single hot CPI print can raise inflation risk overlay but does not prove inflation regime transition.
- A single oil move can raise stagflation pressure but does not prove stagflation.
- Weak market breadth can raise market fragility but does not prove risk-off without volatility and credit confirmation.
- JPY weakness can raise intervention and carry-trade risk but does not prove a global deleveraging event.

## 5. Regime-Change Standard

A confirmed regime change requires:

```text
Depth
Diffusion
Duration
Transmission
Market Discounting
```

### Depth

The move or data change is economically or market materially large.

### Diffusion

The signal is confirmed across multiple macro blocks, indicators, markets, regions, or transmission channels.

Practical block diffusion check:

```text
1 block confirms = signal / watch item
2 blocks confirm = risk overlay
3 blocks confirm = possible regime transition
4-5 blocks confirm = high-conviction regime shift
```

This is the practical 3-of-5 diffusion check: three confirming macro blocks can justify a possible transition watch, but it is not sufficient alone for a final regime-change declaration without depth, duration, transmission, and market-discounting review.

### Duration

The signal persists beyond a one-off print or one-day move, except for exceptional systemic shocks.

### Transmission

There is a clear channel into rates, FX, credit, liquidity, earnings, margins, valuation, household income, or risk appetite.

### Market Discounting

Assess what changed relative to expectations and what appears already repriced. Macro Agent identifies the expectation reset; Market Positioning and Market Sense handle final priced-in conclusions.

## Exceptional Shock Override

Some events may immediately elevate risk overlay or transition watch before full diffusion arrives:

```text
emergency central bank action
credit / funding seizure
major oil or energy supply shock
Treasury market dysfunction
inflation shock that changes central bank reaction function
labor break confirmed by claims / payrolls / credit
USD funding stress
disorderly JPY carry unwind
sovereign spread shock in Europe
```

Even then, use:

```text
Confirmed regime: unchanged / under review
Risk overlay: systemically elevated
Regime transition watch: active
Required confirmation: [specific blocks/data]
```

## Scenario Map

Use qualitative scenarios by default.

```text
Base scenario:
Upside / relief scenario:
Downside scenario:
Tail-risk scenario:
```

For each scenario include:

```text
mechanism
current support
what would confirm
what would invalidate
asset classes most sensitive
```

Numeric probabilities are optional only when justified by prior baseline, model, market-implied data, or user request.

## Regime Fragility

Use qualitative fragility by default:

```text
Low
Medium
High
```

Fragility reflects how vulnerable the confirmed regime is to shift over the next 1-3 months.

Drivers:

```text
cross-block agreement
dependence on one volatile variable
leading indicator deterioration
policy constraint
credit fragility
market breadth quality
liquidity durability
revision risk
concentration of market leadership
G3 policy divergence
```

Do not confuse confidence with fragility. A regime can be confidently diagnosed as fragile.

## Confidence Decomposition

When confidence matters, decompose it:

```text
data freshness
source quality
cross-block agreement
leading indicator clarity
market confirmation
policy clarity
credit confirmation
revision risk
```

Overall confidence:

```text
Low / Medium / High
```

Do not use High confidence when major blocks materially contradict each other without a clear explanation.

## Macro Regime Baseline Output

`macro_regime_baseline.md` should use:

```text
## Macro Regime Baseline

1. Baseline Metadata
2. Executive Macro Verdict
3. Regime Dashboard
4. Block State Summary
5. Expectations / Surprise Context
6. Dominant Transmission Chain
7. What Is Already Repriced vs What Requires Market Positioning / Market Sense Review
8. Scenario Map
9. Monitoring Triggers
10. Asset Sensitivity Map
11. Conflicts / Contradictions
12. Evidence Quality / Freshness / Limitations
13. Required Next Updates
```

## Baseline Metadata

Include:

```text
Report date / time
Data cutoff
Mode
Evidence status
Source freshness status
Prior baseline used
Block states used
```

## Regime Dashboard

Use a compact table:

| Layer | Current View | Direction | Confidence | Key Evidence | Limitation |
|---|---|---|---|---|---|
| Core Growth x Inflation |  |  |  |  |  |
| Dominant Driver |  |  |  |  |  |
| Policy / Rates |  |  |  |  |  |
| Liquidity / Credit |  |  |  |  |  |
| Cross-Asset Confirmation |  |  |  |  |  |
| G3 FX Overlay |  |  |  |  |  |
| Risk Overlay |  |  |  |  |  |

## Block State Summary

Summarize:

```text
Growth & Labor
Inflation & Commodities
Rates / Fed / Yield Curve
Liquidity & Credit
Cross-Asset Confirmation
G3 FX & Regional Policy, if material
```

For each:

```text
block verdict
role: regime-defining / confirming / stabilizing / risk-overlay / secondary
key evidence
active triggers
confidence
```

## Asset Sensitivity Map

Translate regime into likely asset sensitivities, not recommendations.

Examples:

```text
long-duration equities
cyclicals
defensives
financials
small caps
long bonds
T-bills / cash
gold
oil / commodities
USD
EUR
JPY
Bitcoin / crypto
EM assets
credit
```

## Monitoring Triggers

Every baseline should include trigger-based monitoring:

```text
trigger
current_status
threshold / qualitative condition
time_horizon
affected_macro_regime_or_overlay
affected_asset_classes
evidence_needed
downstream_implication
```

Thresholds may be quantitative only when supported by context and sources. Otherwise use qualitative trigger conditions.

## Required Next Updates

State the next data or event most likely to update the baseline:

```text
next CPI / PCE / NFP / claims / ISM / FOMC / ECB / BoJ / Tankan / Treasury event
market variable to monitor
trigger condition
which block state may update
```

## Professional Source Anchors

Key source logic:

- NBER: business cycle assessment uses multiple indicators, not one release.
- OECD CLI: leading indicators provide qualitative turning-point signals, not precise forecasts.
- BIS: credit and leverage indicators can be early warning signals for financial stress.
- Fed: policy and financial conditions transmit through rates, credit, asset prices, funding, and risk appetite.
- ECB: euro area analysis must account for HICP, wages, growth, trade, and cross-country heterogeneity.
- BoJ: Japan analysis must account for price stability, wage-price cycle, Tankan, JGBs, yen, and policy normalization.
