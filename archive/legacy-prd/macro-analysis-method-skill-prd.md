# Macro Analysis Method Skill PRD

## Purpose

The Macro Analysis Method Skill defines how the Macro Agent performs standalone and embedded macro analysis. It operationalizes the Macro Agent PRD and governs mode routing, playbook orchestration, evidence handling, freshness discipline, regime-change discipline, conflict resolution, expectations / surprise analysis, and downstream handoffs.

## Core Doctrine

```text
Macro analysis is not macro storytelling. It is disciplined analysis of regime, transmission, surprise, market confirmation, and investment sensitivity.
```

The skill must distinguish:

1. official data;
2. market pricing;
3. consensus expectations;
4. macro interpretation;
5. investment transmission;
6. uncertainty and limitations.

It must not convert macro analysis into final investment action.

## Step 1 — Classify Invocation Context

Classify the request as:

```text
Standalone Macro Call
Embedded Asset / Sector / Theme Workflow
Direct Specialist Macro Question
Investment Committee Support
```

If embedded, identify available artifacts:

```text
evidence_pack.md
asset / security analysis
valuation_expectations.md
market_positioning.md
news_catalysts.md
risk_red_team.md
portfolio_fit.md
prior macro_regime_baseline.md
macro_block_states
```

## Step 2 — Select Mode

Use intent-based routing.

```text
"today", "now", "latest", "markets", "DXY", "yields", "EUR/USD", "USD/JPY"
-> Market Pulse Mode

"weekly", "what changed", "this week"
-> Weekly Delta Mode

"CPI", "NFP", "FOMC", "ECB", "BoJ", "oil shock", "yield shock", "credit shock"
-> Event-Driven Mode

"deep dive", "full macro", "macro regime", "monthly"
-> Monthly / Full Macro Regime Mode

specific asset / security / ETF / sector / commodity / bond / crypto
-> Asset-Specific Macro Sensitivity Mode
```

Ask a clarifying question only when mode ambiguity would materially change the answer and cannot be reasonably inferred.

## Step 3 — Establish Evidence Readiness

Use the Evidence Pack first when available. For standalone calls, collect or verify evidence directly.

Classify evidence readiness:

```text
Complete Macro Output
Limited Macro Output
Blocked Macro Output
```

Status discipline is mandatory internally, but user-facing prominence depends on severity.

Block if the requested current macro conclusion depends on unavailable fresh market data or unverifiable official event facts.

## Step 4 — Apply Freshness / Cadence Discipline

Market-sensitive variables require fresh data:

```text
Treasury yields
real yields
yield curve
DXY
EUR/USD
USD/JPY
oil
gold
copper when relevant
VIX / MOVE
credit spreads
equity indexes
market-implied policy path
```

Slow official releases may be carried forward with timestamp:

```text
CPI / PCE / PPI
NFP / JOLTS / ISM / PMI
GDP
Tankan
SLOOS
ECB / BoJ / Fed projections
national accounts
```

Do not fake-refresh monthly or quarterly data. Carry forward the last official release with date.

Use carry-forward explicitly: if a slow official series has not updated, preserve the latest official value, release date, and next expected release window instead of inventing a new datapoint.

## Step 5 — Select Playbooks

Use materiality-gated orchestration.

### Market Pulse Mode

Default:

- Rates, Fed & Yield Curve;
- Liquidity & Credit;
- Cross-Asset Macro Confirmation;
- G3 overlay if FX / Europe / Japan / policy divergence is material.

### Weekly Delta Mode

Check all blocks. Analyze deeply only where fresh releases, market moves, trigger changes, or contradictions exist.

### Event-Driven Mode

Run affected block plus Cross-Asset Confirmation.

Examples:

```text
CPI -> Inflation & Commodities + Rates + Cross-Asset
NFP -> Growth & Labor + Rates + Cross-Asset
FOMC -> Rates + Liquidity + Cross-Asset
ECB decision -> G3 Overlay + Rates + Cross-Asset
BoJ decision -> G3 Overlay + Rates + Cross-Asset
Credit spread shock -> Liquidity & Credit + Cross-Asset + Risk handoff
Oil shock -> Inflation & Commodities + Cross-Asset + G3 if EUR/JPY impact is material
```

### Full Macro Regime Mode

Run all core playbooks and compact G3 check by default.

### Asset-Specific Macro Sensitivity Mode

Map the asset or thesis to macro exposure archetypes and run only material playbooks.

## Step 6 — Evaluate Expectations / Surprise

Where available, analyze data relative to expectations.

Use:

```text
macro_expectations_context:
  market_implied_policy_path
  consensus_release_expectations
  actual_vs_consensus
  surprise_direction
  surprise_magnitude
  immediate_market_reaction
  macro_surprise_type
```

Macro Agent identifies expectations and surprise. Market Positioning / Market Sense determine whether the move is fully priced.

See `macro-expectations-surprise-framework.md`.

## Step 7 — Analyze Immediate Market Reaction

For events and market pulse, record immediate cross-asset reaction where relevant:

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
credit
VIX / MOVE
crypto if relevant
```

Classify reaction:

```text
reaction_confirms_macro_surprise
reaction_contradicts_macro_surprise
reaction_muted
reaction_unstable / unclear
```

If reaction is anomalous, create a Market Sense handoff rather than over-interpreting.

## Step 8 — Apply Regime Framework

Use:

```text
Core Growth x Inflation Regime
Dominant Regime Driver
Policy / Rates / Liquidity Stance
Current Risk Overlay
Dominant Transmission Channel
Asset Sensitivity Map
```

Regime-change standard:

```text
Depth
Diffusion
Duration
Transmission
Market Discounting
```

Do not change confirmed regime from one release or one market move unless it is an exceptional systemic shock and even then label the confirmed regime as under review until confirmation arrives.

## Step 9 — Resolve Conflicts

When signals conflict, do not smooth over them.

Classify conflict type:

```text
data vs market pricing
hard data vs soft data
current data vs leading indicators
nominal vs real variables
policy signal vs market-implied path
US vs G3 divergence
growth signal vs inflation signal
liquidity support vs credit deterioration
cross-asset confirmation mismatch
```

Then state:

```text
which signal deserves more weight now
why
what would resolve the conflict
whether confidence is reduced
handoff needed
```

## Step 10 — Build Transmission Chain

Every material macro conclusion should identify the path into assets or the thesis.

Examples:

```text
real yields -> discount rates -> long-duration equities / gold / long bonds
USD strength -> imported inflation / EM funding / commodity pressure
credit spreads -> refinancing cost -> capex / defaults / risk appetite
oil shock -> inflation expectations -> Fed constraint -> consumer real income
BoJ normalization -> JGB yields / yen -> carry trade -> global risk appetite
ECB easing -> EUR / Bund yields -> European banks / exporters / luxury demand
```

## Step 11 — Produce Mode-Specific Output

Use the applicable framework:

```text
macro_market_pulse.md
macro_weekly_delta.md
macro_event_update.md
macro_regime_baseline.md
macro_sensitivity.md
```

Begin with layered output:

```text
Verdict
What changed
Why it matters
What to watch
```

Put detailed evidence, source logs, and limitations below.

### Market Pulse Output Template

Use for `macro_market_pulse.md`:

```text
## Macro Market Pulse
1. Pulse Verdict
   - what moved
   - why it matters
   - regime impact: none / watch item / risk overlay / transition watch
2. Market Moves Snapshot
   - yields / curve / real yields
   - DXY / EUR/USD / USD/JPY
   - oil / gold / copper
   - credit spreads
   - VIX / MOVE
   - equities / breadth
   - crypto if relevant
3. Signal vs Noise
4. Transmission Chain Today
5. What Changed vs Latest Baseline
6. G3 FX / ECB / BoJ Check, if relevant
7. Asset Classes Most Sensitive Today
8. Trigger Watch
9. Evidence Freshness / Source Log
10. What to Watch Next
```

Market Pulse must not rewrite `macro_regime_baseline.md` by default. It should identify changes in risk overlay, market-sensitive asset classes, and trigger watch.

### Weekly Delta Output Template

Use for `macro_weekly_delta.md`:

```text
## Macro Weekly Delta
1. Weekly Verdict
   - confirmed regime change? yes/no
   - risk overlay change? yes/no
   - confidence change
   - most important weekly signal
2. Baseline Comparison
   - prior baseline
   - current weekly view
   - what changed
   - what did not change
3. Block Delta Summary
   - Growth & Labor
   - Inflation & Commodities
   - Rates / Fed / Yield Curve
   - Liquidity & Credit
   - Cross-Asset Confirmation
   - G3 FX if material
4. Key Releases / Market Moves vs Expectations
5. Signal vs Noise
6. Conflicts / Contradictions
7. Trigger Watch Changes
8. Scenario / Risk Overlay Changes
9. Asset Sensitivity Changes
10. Evidence Freshness / Limitations
11. Required Updates to Block States
```

Weekly Delta is synthesis of change versus baseline, not a full macro rerun.

### Event Update Output Template

Use for `macro_event_update.md`:

```text
## Macro Event Update
1. Event Verdict
   - event type
   - affected macro blocks
   - surprise vs expectations
   - regime impact: none / watch item / risk overlay / transition watch
2. Event Facts
   - actual
   - prior
   - consensus / market-implied expectation
   - source
   - timestamp
3. Immediate Market Reaction
   - yields / curve / real yields
   - DXY / EUR/USD / USD/JPY
   - equities / credit / volatility
   - commodities / gold / crypto if relevant
4. Affected Block Analysis
5. Transmission Channel
6. Confirmed Regime vs Risk Overlay Impact
7. Scenario / Trigger Update
8. Conflict Check
9. Downstream Handoffs
   - Market Sense
   - Market Positioning
   - Valuation
   - Risk / Red Team
   - Investment Committee
10. Evidence / Freshness / Limitations
11. Required Follow-Up
```

Event Update is a delta packet, not a full macro report.

### Macro Block State Template

Use for internal state files in `macro_block_states/`:

```text
## [Block] State
- last_updated:
- data_cutoff:
- current_block_verdict:
- current_regime_role: defining / confirming / stabilizing / risk-overlay / secondary
- key_signals:
- active_triggers:
- latest_releases_used:
- next_known_releases:
- confidence:
- limitations:
```

Block states are short memory cards, not user-facing full reports.

## Step 12 — Prepare Downstream Handoffs

Always include structured handoffs when relevant.

### Valuation

```text
discount_rate_pressure
real_yield_direction
earnings_cycle_pressure
margin_pressure
terminal_growth_risk
multiple_sensitivity
required_valuation_tests
```

### Risk / Red Team

```text
failure_path
affected_thesis_component
trigger
transmission
severity
time_horizon
evidence_status
risk_agent_request
```

### Market Positioning / Market Sense

```text
expectation_reset_risk
policy_path_repricing
reaction_anomaly
possible_interpretations_to_test
```

## Step 13 — Recommended State Updates

After standalone weekly, event, or full macro work, recommend state updates but do not save them without explicit user approval.

The agent should show a proposed patch / save updates plan first; only after explicit user approval may it write or overwrite `macro_regime_baseline.md` or `macro_block_states/*`.

```text
Recommended State Updates:
- macro_regime_baseline.md: update / no update + reason
- growth_labor_state.md: update / no update + reason
- inflation_commodities_state.md: update / no update + reason
- rates_fed_curve_state.md: update / no update + reason
- liquidity_credit_state.md: update / no update + reason
- cross_asset_confirmation_state.md: update / no update + reason
- g3_fx_regional_policy_state.md: update / no update + reason
- monitoring triggers: add / remove / modify + reason
```

## Prohibited Behaviors

The skill must not:

- present stale market data as current;
- confuse market-implied policy expectations with official central bank intent;
- treat consensus as truth;
- declare a regime change from one release without diffusion and transmission;
- overstate an early warning signal as a crisis forecast;
- use numeric probabilities or scores by default;
- provide final buy / sell / hold recommendations;
- produce exact target prices or fair values;
- make final priced-in or mispriced conclusions;
- hide material limitations in the appendix when they affect the main conclusion.

## Scenario and Probability Discipline

Use qualitative scenario weighting by default:

```text
base case: dominant / plausible / weakening
bull case: plausible / secondary / rising
bear case: contained / rising / elevated
tail risk: low / rising / elevated
```

Use numeric probabilities only when:

- the user requests them;
- a prior baseline already used a probability map;
- market-implied data or model context supports them;
- the output is a standalone macro regime report;
- uncertainty and judgmental nature are disclosed.

## Professional Methodology Anchors

The method reflects professional concepts from NBER cycle dating, OECD leading indicators, BIS early warning and financial cycle work, Fed transmission and financial stability frameworks, ECB and BoJ policy frameworks, IMF financial soundness indicators, and practitioner macro sensitivity research.
