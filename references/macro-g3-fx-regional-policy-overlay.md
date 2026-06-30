# G3 FX & Regional Policy Overlay

<!-- reference-governance:start -->
## Reference Governance Metadata

Status: Supporting Reference  
Owner: Macro Agent  
Contributors: Market Sense; Fixed Income Agent; Commodity Agent  
Used by: Macro Agent; macro-analysis skill  
Primary reference for: G3, FX, and regional policy overlays  
Supporting reference for: rates, FX, commodities, and cross-asset regime interpretation  
Not responsible for: final decision; evidence readiness; routing; IC Action; agent ownership  
Freshness sensitivity: High  
Last reviewed: 2026-06-28  
Review trigger: Review quarterly or when major central-bank, FX, fiscal, or regional policy regimes change materially.  
Owner review needed: No  
Split/index status: Indexed in implementation/reference-library-index.md  
Canonical authority: Advisory reference only. Canonical implementation documents govern active agent, skill, evidence, routing, and IC behavior.

<!-- reference-governance:end -->


## Purpose

The G3 FX & Regional Policy Overlay gives the Macro Agent a disciplined, Pareto-style way to analyze USD, EUR, JPY, ECB policy, BoJ policy, Europe macro, Japan macro, and policy divergence without turning every macro run into a full global macro report.

It is a conditional overlay, not a permanent sixth core block.

## Core Question

```text
Are USD, EUR, JPY, ECB policy, BoJ policy, or Europe / Japan macro conditions materially affecting the macro regime, risk overlay, asset sensitivity, or investment thesis?
```

## Activation Rules

Activate the overlay when the user asks about:

```text
DXY
EUR/USD
USD/JPY
ECB
BoJ
Europe macro
Japan macro
G3 rates
policy divergence
carry trade
yen intervention
European equities / ETFs
Japanese equities / ETFs
FX-sensitive assets
```

Activate in asset-specific workflows when material to:

```text
European company / ETF
Japanese company / ETF
global ETF with Europe or Japan exposure
exporter / importer margin sensitivity
gold / commodities where USD matters
Treasuries / global rates thesis
crypto / liquidity-sensitive assets
luxury / autos / industrials
banks / insurers
EM assets affected by USD or yen carry
```

In full standalone macro reports, include compact G3 check by default.

## Boundary

This overlay does not own:

- full country-level political analysis;
- detailed fiscal analysis for every euro area country;
- full FX trading recommendation;
- technical FX levels;
- final priced-in verdict;
- final investment action.

It owns the macro transmission relevance of G3 FX and regional policy.

## Europe / ECB Pareto Framework

### Core Europe Question

```text
Is euro area policy, inflation, growth, Germany manufacturing/export sensitivity, or EUR/USD materially affecting the macro setup or asset under review?
```

### Primary Drivers

```text
ECB policy stance / deposit rate
market-implied ECB path
euro area HICP / core / services inflation
wages / negotiated wages
euro area composite PMI
Germany manufacturing / Ifo / exports
France / Italy / Spain as secondary confirmation
EUR/USD and Fed-ECB rate differential
Bund yields
BTP-Bund / peripheral spreads where sovereign risk matters
energy / gas sensitivity
trade and external demand
```

### Why Germany Matters

Germany is the largest EU economy and a key manufacturing / export node. Manufacturing-heavy economies can have stronger output sensitivity to ECB policy changes. Therefore, German manufacturing and export indicators can be disproportionately useful for Europe risk analysis, especially for industrials, autos, chemicals, capital goods, luxury demand, and China-linked themes.

Do not reduce euro area analysis to Germany alone. Use Germany as a Pareto node and France / Italy / Spain as confirmation when relevant.

### Europe Regime Labels

```text
ECB restrictive / growth-constrained
ECB easing / growth relief
sticky services inflation
wage-driven inflation persistence
manufacturing recession / services resilience
energy shock overlay
sovereign spread stress watch
EUR policy-divergence pressure
mixed Europe signal
```

### Europe Transmission Channels

```text
ECB policy -> Bund yields -> European equities / banks / duration
Fed-ECB divergence -> EUR/USD -> exporters / importers / inflation
Germany manufacturing -> industrial earnings / global trade signal
wages / services inflation -> ECB constraint
energy prices -> inflation / margins / consumer real income
peripheral spreads -> banks / sovereign risk / risk appetite
```

### Europe Output Fields

```text
europe_overlay:
  relevance: low / medium / high
  ecb_stance:
  market_implied_ecb_path:
  inflation_signal:
  wage_signal:
  growth_signal:
  germany_node_signal:
  france_italy_spain_confirmation:
  eur_usd_signal:
  sovereign_spread_signal:
  energy_sensitivity:
  transmission:
  confidence:
  limitations:
```

## Japan / BoJ Pareto Framework

### Core Japan Question

```text
Is BoJ normalization, JGB yields, USD/JPY, wage-price dynamics, Tankan, or carry-trade risk materially affecting the macro setup or asset under review?
```

### Primary Drivers

```text
BoJ policy stance / rate path
JGB yields and curve
BoJ bond purchase normalization
USD/JPY and US-Japan rate differential
FX intervention risk / MOF language
CPI / core CPI / services inflation
wages / real wages / Shunto wage momentum
private consumption / real income
Tankan business conditions
exports / global manufacturing / semiconductors
carry-trade unwind risk
```

### Why Japan Is Different

Japan's macro structure reflects decades of ultra-low rates, deflation risk, BoJ unconventional policy, and large global funding / carry-trade implications. The key question is often not simply whether inflation is high, but whether inflation is becoming sustainable through wages, domestic demand, and policy normalization.

USD/JPY matters because yen weakness can import inflation, pressure real incomes, affect exporters, create intervention risk, and influence global carry trades.

### Japan Regime Labels

```text
BoJ normalization
reflation cycle building
wage-price cycle confirmation
imported inflation pressure
JPY intervention watch
carry-trade unwind risk
global risk spillover risk
JGB volatility / policy normalization pressure
mixed Japan signal
```

### Japan Transmission Channels

```text
BoJ policy -> JGB yields -> USD/JPY -> carry trade / global risk appetite
JPY weakness -> imported inflation -> real income / consumption
wages -> sustainable inflation -> BoJ normalization
Tankan -> business confidence / capex / exports
JGB yields -> domestic financials / insurers / global duration demand
carry unwind -> global deleveraging / volatility / risk assets
```

### Japan Output Fields

```text
japan_overlay:
  relevance: low / medium / high
  boj_stance:
  market_implied_boj_path:
  jgb_signal:
  usd_jpy_signal:
  intervention_risk:
  inflation_signal:
  wage_price_cycle_signal:
  tankan_signal:
  export_signal:
  carry_trade_unwind_risk:
  transmission:
  confidence:
  limitations:
```

## FX Framework

### Core FX Pairs

```text
DXY
EUR/USD
USD/JPY
```

Optional when material:

```text
GBP/USD
USD/CNH
commodity FX
EM FX
```

### FX Driver Classification

Classify FX moves by likely driver:

```text
rate differential
real-yield differential
policy divergence
growth divergence
inflation divergence
risk-on / risk-off
safe-haven demand
current account / trade shock
intervention / policy signal
carry-trade positioning
USD liquidity stress
```

Do not assume every FX move has one driver. If unclear, label mixed and hand off to Market Sense if reaction matters.

## Handoff Fields for `macro_sensitivity.md`

Use when G3 is material:

```text
g3_fx_regional_policy_inputs:
  fx_pairs_relevant:
    - DXY
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

## Sources and Freshness

### Europe / ECB Primary Sources

- ECB decisions, speeches, Economic Bulletin, and projections;
- Eurostat HICP, GDP, labor, and national accounts;
- national sources for Germany, France, Italy, Spain where material;
- market data for EUR/USD, Bunds, peripheral spreads;
- institutional research for interpretation.

### Japan / BoJ Primary Sources

- BoJ policy statements and Outlook for Economic Activity and Prices;
- BoJ Tankan;
- Japan Statistics Bureau / official CPI and labor data;
- Japan MOF for FX intervention operations and authority;
- market data for USD/JPY and JGBs;
- institutional research for carry-trade interpretation.

## Professional References

- ECB monetary policy strategy: https://www.ecb.europa.eu/mopo/strategy/strategy-review/ecb.strategyreview202506_strategy_overview.en.html
- ECB macroeconomic projections: https://www.ecb.europa.eu/press/projections/html/index.en.html
- Eurostat national accounts and GDP: https://ec.europa.eu/eurostat/statistics-explained/index.php?title=National_accounts_and_GDP
- Fed research on euro area monetary transmission heterogeneity: https://www.federalreserve.gov/econres/notes/feds-notes/country-specific-effects-of-euro-area-monetary-policy-the-role-of-sectoral-differences-20241112.html
- BoJ monetary policy outline: https://www.boj.or.jp/en/mopo/outline/index.htm
- BoJ Tankan explanation: https://www.boj.or.jp/en/statistics/outline/exp/tk/extk.htm
- BoJ FX intervention explanation: https://www.boj.or.jp/en/about/education/oshiete/intl/g19.htm
- Japan MOF foreign exchange intervention operations: https://www.mof.go.jp/english/policy/international_policy/reference/feio/index.html
- PIMCO on BoJ policy shift: https://www.pimco.com/sg/en/insights/bank-of-japan-policy-shift-ushers-in-a-new-era-for-investors
- Wellington on JPY intervention: https://www.wellington.com/en/insights/japanese-yen-intervention
- Capital Group on yen carry risks: https://www.capitalgroup.com/intermediaries/be/en/insights/articles/unwinding-of-yen-carry-trade-presents-risks.html

## Prohibited Behavior

Do not:

- treat Europe as Germany only;
- treat Japan as a normal G7 rates cycle without considering BoJ normalization and yen carry;
- confuse MOF FX intervention authority with BoJ monetary policy ownership;
- use FX moves without fresh data;
- make FX trading recommendations;
- overstate intervention rumors without official confirmation or reliable sourcing;
- claim policy divergence is priced in without Market Positioning / Market Sense support.
