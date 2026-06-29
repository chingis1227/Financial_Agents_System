# Macro Sensitivity Framework

<!-- reference-governance:start -->
## Reference Governance Metadata

Status: Supporting Reference  
Owner: Macro Agent  
Contributors: asset-class agents; Valuation/Expectations; Risk Red Team  
Used by: Macro Agent; macro-analysis skill; asset-class agents  
Primary reference for: macro sensitivity mapping  
Supporting reference for: asset-class risk, valuation, and scenario context  
Not responsible for: final decision; evidence readiness; routing; IC Action; agent ownership  
Freshness sensitivity: Medium  
Last reviewed: 2026-06-28  
Review trigger: Review when sensitivity taxonomy or cross-asset transmission assumptions change.  
Owner review needed: No  
Split/index status: Indexed in implementation/reference-library-index.md  
Canonical authority: Advisory reference only. Canonical implementation documents govern active agent, skill, evidence, routing, and IC behavior.

<!-- reference-governance:end -->


## Objective

This framework defines the embedded output `macro_sensitivity.md`. It is used when the Macro Agent analyzes how macro conditions affect a specific asset, security, sector, ETF, commodity, crypto asset, fixed income instrument, portfolio question, or investment thesis.

The output should be concise, structured, decision-useful, and handoff-oriented.

## Core Question

```text
Which macro variables materially matter for this investment decision, through what transmission channel, and what should downstream agents test?
```

## Output Structure

```text
## Macro Sensitivity

1. Macro Relevance Verdict
2. Asset / Thesis Macro Exposure Archetype
3. Material Macro Drivers Table
4. Non-Material / Secondary Macro Factors
5. Scenario Sensitivity
6. Valuation-Relevant Macro Inputs
7. Macro Failure Paths for Risk / Red Team
8. G3 FX & Regional Policy Inputs, if relevant
9. Monitoring Triggers
10. Evidence / Freshness / Limitations
11. Downstream Handoff Summary
```

## 1. Macro Relevance Verdict

Begin with a concise verdict:

```text
Macro Relevance: High / Medium / Low
Primary Macro Driver:
Current Macro Support / Challenge:
Most Important Transmission Channel:
Risk Overlay:
Confidence: Low / Medium / High
Key Limitation, if material:
```

Do not bury material limitations if they affect the verdict.

## 2. Asset / Thesis Macro Exposure Archetype

Classify the asset or thesis into one or more archetypes:

```text
Long-duration growth equity
Cyclical industrial
Defensive compounder
Bank / financial
Insurance / asset manager
Consumer discretionary
Consumer staple / defensive demand
Exporter / importer
Commodity producer
Energy producer
Gold / precious metals
Oil / energy commodity
Industrial commodity
Treasuries / duration
Credit instrument
Bond ETF
Equity ETF / regional ETF
Global multi-asset ETF
Real estate / REIT
EM / FX-sensitive asset
Bitcoin / crypto
Theme / basket
Other
```

For each archetype, identify the likely macro exposures.

## 3. Material Macro Drivers Table

Use a compact table:

| Factor | Current State | Direction of Change | Relevance | Transmission | Likely Impact | Evidence Status | Data Date |
|---|---|---|---|---|---|---|---|
| Real yields |  |  |  |  |  |  |  |
| Fed path / policy rate |  |  |  |  |  |  |  |
| Growth cycle |  |  |  |  |  |  |  |
| Inflation / wages |  |  |  |  |  |  |  |
| USD / FX |  |  |  |  |  |  |  |
| Credit spreads |  |  |  |  |  |  |  |
| Liquidity |  |  |  |  |  |  |  |
| Commodity inputs |  |  |  |  |  |  |  |
| G3 policy divergence |  |  |  |  |  |  |  |

Only include material factors. Add rows as needed.

Allowed relevance:

```text
High / Medium / Low / Not Material
```

Allowed evidence status:

```text
Fresh / Carried Forward / Limited / Proxy / Missing / Contradicted
```

## 4. Non-Material / Secondary Macro Factors

Explicitly state factors considered but not central:

```text
Factor:
Why secondary / not material now:
What would make it material:
```

This prevents checklist bloat while preserving coverage discipline.

## 5. Scenario Sensitivity

Use scenarios, not point forecasts:

```text
Base Macro Scenario:
Upside Macro Scenario:
Downside Macro Scenario:
Tail-Risk Macro Scenario, if relevant:
```

For each:

```text
mechanism
asset impact
valuation / risk implication
trigger that would confirm
trigger that would invalidate
```

## 6. Valuation-Relevant Macro Inputs

Provide structured handoff:

```text
valuation_relevant_macro_inputs:
  discount_rate_pressure: higher / lower / mixed / not material
  real_yield_direction: rising / falling / stable / mixed / not material
  earnings_cycle_pressure: positive / negative / mixed / not material
  margin_pressure: wage / commodity / FX / financing_cost / none / mixed
  terminal_growth_risk: higher / lower / mixed / not material
  multiple_sensitivity: long-duration / cyclical / defensive / commodity-linked / financials / FX-sensitive / other
  macro_scenario_range:
    bull_case_macro:
    base_case_macro:
    bear_case_macro:
  required_valuation_tests:
    - test higher discount rate
    - test lower terminal growth
    - test FX translation pressure
    - test commodity margin squeeze
    - test recessionary demand pressure
```

Macro Agent must not provide final fair value or target price.

## 7. Macro Failure Paths for Risk / Red Team

Provide structured handoff:

```text
macro_failure_paths:
  - failure_path:
    affected_thesis_component:
    trigger:
    transmission:
    severity: low / medium / high
    time_horizon: near / medium / long
    evidence_status: confirmed / watch / weak
    risk_agent_request:
```

Examples:

```text
real yields stay higher for longer
credit spreads widen and refinancing risk rises
USD strengthens and pressures EM demand or FX translation
oil shock squeezes consumer income and margins
BoJ normalization triggers carry-trade unwind
ECB easing fails to offset European demand weakness
```

## 8. G3 FX & Regional Policy Inputs

Include only if material.

```text
g3_fx_regional_policy_inputs:
  fx_pairs_relevant:
    - EUR/USD
    - USD/JPY
  regional_policy_relevance: low / medium / high
  fed_ecb_divergence: widening / narrowing / stable / not material
  fed_boj_divergence: widening / narrowing / stable / not material
  currency_translation_risk: positive / negative / mixed / not material
  importer_exporter_margin_effect: positive / negative / mixed / not material
  carry_trade_unwind_risk: low / rising / elevated / not material
  intervention_risk: low / rising / elevated / not material
  required_downstream_tests:
    - FX sensitivity test
    - local rates sensitivity
    - margin impact from currency move
    - demand shock from Europe/Japan slowdown
```

## 9. Monitoring Triggers

Use trigger map:

```text
monitoring_triggers:
  - trigger:
    current_status:
    threshold_or_condition:
    time_horizon:
    affected_macro_overlay:
    affected_asset_classes_or_thesis_components:
    evidence_needed:
    downstream_implication:
```

## 10. Evidence / Freshness / Limitations

Keep this concise in the main report. Put detail in appendix when needed.

Include:

```text
Evidence Pack Used: yes/no
Standalone Evidence Used: yes/no
Fresh Market Data Used: yes/no/not required
Carried-Forward Data:
Material Missing Data:
Output Status: Complete / Limited / Blocked
Key Limitations:
```

Do not make the user read long evidence diagnostics unless limitations are material.

## 11. Downstream Handoff Summary

End with a concise handoff:

```text
For Valuation:
For Risk / Red Team:
For Market Positioning:
For Market Sense:
For Investment Committee:
```

## Asset Archetype Guide

### Long-Duration Growth Equity

Typical macro drivers:

```text
real yields
discount rate
liquidity
USD
risk appetite
capex cycle if relevant
```

### Cyclical Industrial

```text
growth cycle
PMIs
capex cycle
credit
commodities
USD / trade
```

### Bank / Financial

```text
yield curve
credit quality
funding costs
deposit beta
loan growth
capital / regulation
```

### Gold / Precious Metals

```text
real yields
USD
inflation expectations
central bank demand
crisis premium
liquidity
```

### Oil / Energy

```text
supply / demand
inventories
geopolitics
USD
global growth
OPEC / policy
```

### Treasuries / Duration

```text
Fed path
inflation
real yields
term premium
fiscal supply
recession risk
foreign demand
```

### Bitcoin / Crypto

```text
liquidity
real yields
USD
risk appetite
ETF flows / regulation as non-macro adjacent inputs
leverage / funding stress
```

### European Equity / ETF

```text
ECB stance
EUR/USD
European growth / PMI
Germany manufacturing if relevant
energy prices
sovereign spreads if financials or periphery exposure matters
```

### Japanese Equity / ETF

```text
BoJ stance
USD/JPY
JGB yields
wage-price cycle
Tankan
export demand
carry-trade unwind risk
```

## Prohibited Conclusions

Macro Agent must not say:

```text
The asset is undervalued because macro is supportive.
The asset should be bought because rates are falling.
The market has fully priced this in.
The fair multiple should be X.
The position size should be Y.
```

Allowed:

```text
Falling real yields would support the valuation channel for long-duration equities and should be tested by Valuation.
USD strength is a material FX translation risk and should be stress-tested.
Macro currently supports the thesis through lower discount-rate pressure, but credit deterioration is a risk overlay.
```
