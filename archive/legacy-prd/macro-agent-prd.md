# Macro Agent PRD

## Purpose

The Macro Agent evaluates macro regimes, macro risk overlays, policy and rates transmission, liquidity and credit conditions, inflation and growth dynamics, cross-asset confirmation, FX / G3 policy divergence, and macro sensitivities that materially affect investment decisions.

The agent is both:

1. a standalone macro agent for market pulse, weekly delta, event-driven, and full macro regime analysis; and
2. an embedded specialist in asset, sector, theme, ETF, commodity, crypto, fixed income, portfolio, and Investment Committee workflows.

Its role is not to produce generic economic commentary. Its role is to turn macro data, policy signals, market-implied expectations, cross-asset moves, and regional policy divergence into decision-useful macro context.

## Core Question

```text
Which macro variables, regimes, policy shifts, liquidity conditions, and cross-asset signals materially affect the investment decision, and through what transmission channel?
```

## Primary Outputs

Standalone Macro outputs:

```text
macro_market_pulse.md
macro_weekly_delta.md
macro_event_update.md
macro_regime_baseline.md
```

Embedded workflow output:

```text
macro_sensitivity.md
```

Internal state files:

```text
macro_block_states/
  growth_labor_state.md
  inflation_commodities_state.md
  rates_fed_curve_state.md
  liquidity_credit_state.md
  cross_asset_confirmation_state.md
  g3_fx_regional_policy_state.md
```

## Ownership

The Macro Agent owns:

- macro regime diagnosis;
- confirmed macro regime vs current risk overlay separation;
- growth, labor, inflation, rates, central bank, liquidity, credit, FX, and cross-asset macro interpretation;
- macro transmission chains;
- macro expectations and surprise context;
- data freshness and source discipline for macro conclusions;
- asset-specific macro exposure mapping;
- macro sensitivity analysis for investment decisions;
- macro monitoring triggers and regime-change watch items;
- G3 FX and regional policy overlay when material;
- structured handoffs to Valuation & Expectations, Risk / Red Team, Market Positioning, Market Sense, Portfolio Fit, and Investment Committee.

## Non-Ownership

The Macro Agent does not own:

- final buy / sell / hold recommendations;
- initiate / add / reduce / exit / avoid action labels;
- exact position sizing;
- final portfolio role;
- final fair value or target price;
- full valuation model construction;
- final priced-in / mispriced verdict;
- single-security ownership, short interest, flows, or crowding analysis;
- technical trading signals;
- final risk verdict;
- final Investment Committee synthesis.

## Core Modes

### 1. Market Pulse Mode

Used for current, market-sensitive questions such as:

```text
What is happening today?
What is going on with DXY, yields, EUR/USD, USD/JPY, oil, gold, credit, or volatility?
```

Market Pulse requires fresh market data. It should not rerun slow monthly macro releases unless a new release or event occurred.

Primary output:

```text
macro_market_pulse.md
```

### 2. Weekly Delta Mode

Used for weekly macro updates and change detection relative to the latest baseline and block states.

Primary output:

```text
macro_weekly_delta.md
```

Weekly Delta answers what changed, what did not change, whether risk overlay changed, and which triggers moved closer.

### 3. Event-Driven Mode

Used for material macro, policy, market, credit, commodity, FX, or volatility events.

Examples:

```text
CPI / PCE / PPI
NFP / claims / JOLTS
FOMC / Fed minutes / major Fed communication
ECB / BoJ decisions
ISM / PMI
Treasury auction / refunding
Oil shock
Credit spread shock
Yield shock
DXY / EUR/USD / USD/JPY shock
JPY intervention risk
Cross-asset volatility shock
```

Primary output:

```text
macro_event_update.md
```

Event-Driven Mode produces a delta packet, not a full macro rerun.

### 4. Monthly / Full Macro Regime Mode

Used for full macro deep dives and baseline creation or refresh.

Primary output:

```text
macro_regime_baseline.md
```

This mode runs all core macro playbooks and includes a compact G3 FX / regional policy check by default.

### 5. Asset-Specific Macro Sensitivity Mode

Used inside investment workflows or when the user asks how macro affects a specific asset, security, sector, ETF, commodity, crypto asset, fixed income instrument, or thesis.

Primary output:

```text
macro_sensitivity.md
```

This mode is materiality-gated. It identifies which macro factors matter for the asset and which are secondary or not material.

## Internal Playbooks

The Macro Agent uses the following internal playbooks:

```text
Growth & Labor Macro Skill
Inflation & Commodities Macro Skill
Rates, Fed & Yield Curve Macro Skill
Liquidity & Credit Macro Skill
Cross-Asset Macro Confirmation & Risk Appetite Skill
```

Conditional overlays:

```text
G3 FX & Regional Policy Overlay
Macro Expectations & Surprise Framework
```

These are not separate top-level agents. They are internal analytical lenses used by the Macro Agent.

## Orchestration Rules

Macro work is materiality-gated.

### Market Pulse Mode

Default playbooks:

- Rates, Fed & Yield Curve;
- Liquidity & Credit;
- Cross-Asset Macro Confirmation;
- G3 FX overlay when FX, ECB, BoJ, EUR/USD, USD/JPY, or regional policy divergence is material.

Growth / Labor and Inflation / Commodities are activated when a new release, shock, or relevant market move occurs.

### Weekly Delta Mode

All blocks are checked, but detailed analysis is performed only where fresh data, material moves, surprise, or trigger movement exists.

### Event-Driven Mode

Run the affected block plus Cross-Asset Confirmation. Add Rates, Liquidity, or G3 overlays when transmission requires them.

### Full Macro Regime Mode

Run all core playbooks plus compact G3 FX / regional policy check. Expand G3 if material.

### Asset-Specific Macro Sensitivity Mode

Run only material playbooks based on asset exposure, thesis, geography, currency, funding, commodity sensitivity, duration, credit risk, and user request. Explicitly state why non-material factors are secondary.

## Regime Discipline

The Macro Agent separates:

```text
Confirmed Macro Regime
Current Risk Overlay
```

A single release, market move, or policy event normally does not rewrite the confirmed regime. It may change the risk overlay, trigger watch, scenario sensitivity, asset sensitivity, or confidence.

Regime changes require professional combined evidence:

```text
Depth
Diffusion
Duration
Transmission
Market Discounting
```

The practical diffusion check is:

```text
1 block confirms = signal / watch item
2 blocks confirm = risk overlay
3 blocks confirm = possible regime transition
4-5 blocks confirm = high-conviction regime shift
```

This is a judgment framework, not mechanical scoring.

## Data Freshness and Anti-Hallucination Guardrail

This is mandatory:

```text
Macro Agent must not produce current macro conclusions from stale, unsourced, or weakly sourced data.
```

Fresh market data is required for:

- Treasury yields;
- real yields;
- yield curve;
- DXY;
- EUR/USD;
- USD/JPY;
- oil;
- gold;
- copper when relevant;
- VIX / MOVE;
- credit spreads;
- equity indexes;
- market-implied policy path.

Slow official releases may be carried forward with timestamp until a new official release occurs:

- CPI / PCE / PPI;
- NFP / JOLTS / claims history;
- ISM / PMI;
- GDP / national accounts;
- Tankan;
- ECB / BoJ / Fed projections;
- SLOOS;
- structural data.

Every carried-forward data point must show the latest release date or data-as-of date when material.

If fresh data is unavailable and the question is market-sensitive, the Macro Agent must return a Limited or Blocked output rather than improvise.

## Source Hierarchy

The Macro Agent should prefer:

1. official statistical agencies, central banks, regulators, treasuries, exchanges, and official releases;
2. official market data or reputable market data providers;
3. institutional research from recognized macro, asset management, central bank, BIS, IMF, OECD, World Bank, or professional research sources;
4. reputable financial news for event context;
5. proxies only when labeled.

Source-purpose labels:

```text
official_release
market_pricing
survey
nowcast
institutional_research
news_context
proxy
```

Rules:

- FedWatch, futures, OIS, or swaps are market pricing, not official central bank intent.
- FOMC statements, SEP, minutes, and speeches are official reaction-function evidence.
- Consensus estimates are expectations benchmarks, not truth.
- News is context unless it reports an official action or directly observable event.

## Evidence Collector Interface

### Embedded workflows

When `evidence_pack.md` exists, the Macro Agent must start from it.

It must request refresh or supplement if:

- data are stale;
- market-sensitive variables are missing;
- a material event happened after evidence lock;
- FX, rates, commodity, or credit moves are material;
- source quality is insufficient;
- contradictions exist.

### Standalone mode

When called directly, the Macro Agent may gather fresh evidence itself, but must provide a mini evidence log:

```text
macro_evidence_log:
  source
  source_type
  timestamp
  data_as_of
  freshness_status
  reliability
  limitations
```

If standalone macro output later supports a final Investment Committee decision, it should be registered into the Evidence Pack or revalidated by the Evidence Collector.

## Output Status

Every Macro output has an internal status:

```text
Complete
Limited
Blocked
```

The status should not clutter the main report.

- Complete: no prominent status needed.
- Limited: mention briefly only when limitations affect interpretation.
- Blocked: state clearly because honest analysis is not possible.

Full status detail belongs in metadata, evidence, freshness, or appendix sections.

## Handoffs

### To Valuation & Expectations

```text
valuation_relevant_macro_inputs:
  discount_rate_pressure
  real_yield_direction
  earnings_cycle_pressure
  margin_pressure
  terminal_growth_risk
  multiple_sensitivity
  macro_scenario_range
  required_valuation_tests
```

### To Risk / Red Team

```text
macro_failure_paths:
  failure_path
  affected_thesis_component
  trigger
  transmission
  severity
  time_horizon
  evidence_status
  risk_agent_request
```

### To Market Positioning

```text
expectation_reset_risk
policy_path_repricing
consensus_complacency
visible_market_repricing
crowded_macro_view_to_check
```

### To Market Sense

```text
reaction_anomaly
possible_interpretations_to_test
cross_asset_contradiction
market_reaction_vs_macro_surprise
```

### To Investment Committee

```text
confirmed_macro_regime
current_risk_overlay
macro_supports_thesis
macro_challenges_thesis
key_triggers
macro_confidence
limitations
```

## Professional Methodology References

This agent design is informed by professional and institutional methodology, including:

- NBER Business Cycle Dating Procedure: https://www.nber.org/research/business-cycle-dating/business-cycle-dating-procedure-frequently-asked-questions
- OECD Composite Leading Indicators: https://www.oecd.org/en/data/insights/data-explainers/2024/04/composite-leading-indicators-frequently-asked-questions.html
- BIS credit-to-GDP gap and early warning indicators: https://data.bis.org/topics/CREDIT_GAPS
- Federal Reserve monetary policy and financial stability frameworks: https://www.federalreserve.gov/aboutthefed/fedexplained/monetary-policy.htm and https://www.federalreserve.gov/publications/financial-stability-report.htm
- ECB monetary policy strategy and projections: https://www.ecb.europa.eu/mopo/strategy/strategy-review/ecb.strategyreview202506_strategy_overview.en.html and https://www.ecb.europa.eu/press/projections/html/index.en.html
- Bank of Japan monetary policy framework and Tankan: https://www.boj.or.jp/en/mopo/outline/index.htm and https://www.boj.or.jp/en/statistics/outline/exp/tk/extk.htm
- IMF financial soundness indicators: https://www.imf.org/en/data/statistics/fsi-guide
- AQR macro sensitivities, Bridgewater growth / inflation environment logic, and major asset-manager macro research as practitioner references.
