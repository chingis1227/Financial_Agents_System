# Macro Expectations and Surprise Framework

## Purpose

This framework defines how the Macro Agent analyzes macro data, policy events, and market moves relative to expectations.

Macro impact depends not only on what happened, but on what happened relative to what the market and consensus expected.

## Core Principle

```text
Macro Agent identifies expectations, surprise, and immediate market reaction. Market Positioning and Market Sense determine whether the market has fully priced the implications.
```

## Scope

Applies to:

```text
CPI / PCE / PPI
NFP / unemployment / wages / claims
ISM / PMI / JOLTS / retail sales / GDP
FOMC / Fed minutes / Fed speeches
ECB / BoJ policy decisions
Treasury auctions / refunding
oil / commodity shocks
yield / FX / credit / volatility shocks
DXY / EUR/USD / USD/JPY moves
```

## Expectations Sources

Use source-purpose labels.

### Consensus Release Expectations

Examples:

```text
survey consensus for CPI / NFP / GDP / PMI
central bank projection ranges
professional forecaster consensus
institutional data provider consensus
```

### Market-Implied Expectations

Examples:

```text
FedWatch / futures / OIS
ECB-implied policy path
BoJ-implied path when available
Treasury curve and real yields
breakevens
option-implied moves
FX forwards / rate differentials
```

Important:

```text
Market-implied expectations are market pricing, not official intent.
```

## Required Fields

For any material event:

```text
macro_expectations_context:
  event:
  release_or_event_time:
  actual:
  prior:
  consensus_or_market_expectation:
  surprise_direction:
  surprise_magnitude:
  revisions:
  source:
  data_as_of:
  market_implied_context_before_event:
  immediate_market_reaction:
  macro_surprise_type:
  confidence:
  limitations:
```

## Surprise Classification

```text
inflation upside surprise
inflation downside surprise
growth upside surprise
growth downside surprise
labor tightening surprise
labor weakening surprise
hawkish policy surprise
dovish policy surprise
liquidity-positive surprise
liquidity-negative surprise
credit-stress surprise
FX / dollar shock
commodity supply shock
mixed surprise
no material surprise
```

## Market Reaction Capture

Record reaction when relevant:

```text
yields
curve
real yields
DXY
EUR/USD
USD/JPY
gold
oil
equities
credit spreads
VIX / MOVE
crypto if relevant
```

Classify:

```text
reaction_confirms_macro_surprise
reaction_contradicts_macro_surprise
reaction_muted
reaction_unstable / unclear
```

## Interpretation Discipline

Allowed:

```text
The release was above consensus and initially pushed market-implied policy rates higher.
The decision itself was largely expected, but guidance was more hawkish than market pricing implied.
The market reaction was muted, suggesting the event may have been anticipated or offset by another driver; Market Sense should test this.
```

Prohibited:

```text
This is fully priced in.
The market is wrong.
The asset should be bought because the event was a positive surprise.
The Fed will definitely cut in September.
```

## Handoffs

### To Market Positioning

```text
expectation_reset_risk:
policy_path_repricing:
consensus_complacency:
visible_market_repricing:
crowded_macro_view_to_check:
```

### To Market Sense

```text
reaction_anomaly:
possible_interpretations_to_test:
market_reaction_vs_macro_surprise:
cross_asset_contradiction:
```

### To Valuation

```text
discount_rate_assumption_change:
earnings_cycle_assumption_change:
margin_assumption_change:
terminal_growth_assumption_change:
required_sensitivity_tests:
```

### To Risk / Red Team

```text
new_failure_path:
trigger_moved_closer:
macro_tail_risk:
confirmation_needed:
```

## Examples

### CPI Surprise

```text
Actual CPI above consensus
Market reaction: 2Y yields higher, DXY stronger, equities lower
Interpretation: hawkish inflation surprise confirmed by rates and FX
Handoff: Valuation should test higher discount-rate pressure; Risk should test higher-for-longer failure path
```

### Expected Fed Hike, Hawkish Guidance

```text
Rate decision expected by market pricing
Statement / press conference more hawkish than expected
Market reaction: cuts repriced lower, 2Y higher
Interpretation: surprise is in guidance, not decision
```

### Hot CPI, Yields Fall

```text
Actual inflation above consensus
Market reaction contradicts surprise
Possible explanations to test: positioning unwind, growth concern, already priced, liquidity driver
Handoff: Market Sense should interpret reaction anomaly
```

## Evidence and Freshness

If consensus or market-implied expectations are missing:

```text
Output Status: Limited
Limitation: surprise context incomplete
Allowed conclusion: actual data direction and historical comparison
Not allowed: strong claim about market surprise
```

If actual release cannot be verified:

```text
Output Status: Blocked for event conclusion
```

## Source Rules

- Use official release for actual data.
- Use reputable consensus / market data source for expectations.
- Use market data for immediate reaction.
- Label all market-implied paths as market pricing.
- Do not cite unsourced social-media claims as consensus.
