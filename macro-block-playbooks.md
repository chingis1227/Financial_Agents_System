# Macro Block Playbooks

## Purpose

This document defines the Macro Agent's internal analytical playbooks. These are not separate top-level agents. They are specialist lenses invoked by the Macro Agent according to mode, event, and materiality.

Core playbooks:

```text
1. Growth & Labor
2. Inflation & Commodities
3. Rates, Fed & Yield Curve
4. Liquidity & Credit
5. Cross-Asset Macro Confirmation & Risk Appetite
```

Conditional overlays:

```text
G3 FX & Regional Policy Overlay
Macro Expectations & Surprise Framework
```

See:

```text
macro-g3-fx-regional-policy-overlay.md
macro-expectations-surprise-framework.md
macro-indicator-cadence-source-registry.md
```

## Shared Playbook Rules

Each playbook must produce:

```text
block_verdict
what_changed
signal_vs_noise
key_evidence
expectations_or_surprise_context, if relevant
transmission_channel
active_triggers
confidence
limitations
handoff_implications
```

Each playbook must distinguish:

```text
official data
market pricing
survey data
nowcast / model output
institutional interpretation
proxy evidence
```

No playbook may produce a final investment recommendation.

## 1. Growth & Labor Playbook

### Core Question

```text
Is growth broad, private-sector-led, real, and durable, and is the labor market tight, cooling, slowing, or breaking?
```

### Key Focus Areas

- real personal income less transfers;
- nonfarm payrolls and revisions;
- unemployment rate and labor force participation;
- wage growth;
- initial and continuing jobless claims;
- real PCE and retail control group;
- ISM / PMI new orders and employment;
- housing activity and mortgage rates;
- consumer stress indicators as early warnings.

### Weekly / Pulse Use

Focus on:

```text
new claims data
new labor releases
material revisions
material nowcast changes
high-frequency housing / consumer signals when relevant
```

Do not rerun the full labor framework without new data.

### Regime Labels

Allowed labels:

```text
resilient labor market
cooling but healthy labor market
late-cycle labor cooling
labor-market deterioration watch
recessionary labor break
mixed / revision-sensitive labor signal
```

### Transmission Channels

```text
income -> consumption -> revenues / margins
labor tightness -> wages -> services inflation -> Fed constraint
labor deterioration -> demand slowdown -> earnings risk -> credit risk
housing / mortgage rates -> construction / consumer wealth / banks
```

## 2. Inflation & Commodities Playbook

### Core Question

```text
Are inflation pressures easing, sticky, reaccelerating, or being reshaped by commodities, wages, expectations, FX, or supply shocks?
```

### Key Focus Areas

- CPI / core CPI;
- PCE / core PCE;
- 3m / 6m annualized momentum;
- services inflation;
- shelter and wage-sensitive categories;
- PPI and import prices;
- inflation expectations and breakevens;
- oil, gasoline, diesel, natural gas;
- copper and industrial commodities;
- inventories and curve structure where relevant.

### Regime Labels

```text
disinflation intact
sticky services inflation
inflation reacceleration watch
commodity-driven inflation pressure
supply-shock inflation overlay
inflation expectations risk
mixed inflation signal
```

### Commodity Split

Classify commodity moves:

```text
healthy reflation
energy supply shock
demand deterioration
China / global manufacturing signal
safe-haven / crisis premium
USD-driven move
```

Do not treat one oil move as regime change without pass-through or policy relevance.

## 3. Rates, Fed & Yield Curve Playbook

### Core Question

```text
What is the policy path, yield curve, real-yield, and term-premium signal, and how does it transmit into assets and the economy?
```

### Key Focus Areas

- FOMC decision, statement, minutes, SEP, Chair press conference;
- Fed speakers when materially changing reaction function;
- market-implied policy path;
- 2Y, 5Y, 10Y, 30Y Treasury yields;
- real yields;
- breakevens;
- 2s10s and 3m10y curve;
- curve shape: bull steepening, bear steepening, bull flattening, bear flattening;
- Treasury auctions, refunding, issuance, buybacks;
- term premium;
- MOVE;
- mortgage rates.

### Required Distinction

```text
Official Fed reaction function != market-implied policy path
```

FedWatch / OIS / futures are market pricing, not official intent.

### Regime Labels

```text
higher-for-longer pressure
dovish repricing
policy optionality improving
real-yield tightening
term-premium / fiscal pressure
recessionary cuts pricing
mixed curve signal
```

## 4. Liquidity & Credit Playbook

### Core Question

```text
Are liquidity, funding, bank lending, and credit conditions supporting risk assets, tightening transmission, or signaling stress?
```

### Key Focus Areas

- Fed balance sheet;
- bank reserves;
- TGA;
- ON RRP;
- net liquidity proxy, labeled as proxy;
- SOFR / EFFR / IORB spreads;
- repo and funding stress;
- IG and HY spreads;
- credit issuance and refinancing;
- SLOOS;
- bank lending;
- consumer and corporate delinquencies;
- regional bank or funding stress;
- private credit when evidence exists.

### Required Distinction

```text
market liquidity != real-economy credit transmission
```

A liquidity-supportive market backdrop can coexist with deteriorating private credit.

### Regime Labels

```text
liquidity supportive
liquidity neutral
liquidity draining
credit calm
credit caution
credit stress
funding stress watch
mixed liquidity / credit signal
```

## 5. Cross-Asset Macro Confirmation & Risk Appetite Playbook

### Core Question

```text
Do cross-asset prices confirm, contradict, or complicate the macro regime and risk overlay?
```

### Scope

This playbook is not a full Market Positioning Agent and not a Market Sense replacement.

It examines macro-relevant market confirmation:

- yields / curve / real yields;
- DXY / FX stress;
- oil / copper / gold;
- credit spreads;
- VIX / MOVE;
- equities / breadth / cyclicals vs defensives;
- crypto as liquidity beta when relevant.

It does not own:

- single-stock positioning;
- analyst revisions;
- ownership / holder-base analysis;
- full flow analysis;
- final priced-in verdict;
- trade timing.

### Reaction Classifications

```text
confirms macro surprise
contradicts macro surprise
muted reaction
unstable / unclear reaction
positioning-sensitive reaction requiring Market Sense
```

### Handoffs

To Market Sense when reaction is anomalous.

To Market Positioning when expectation bar, crowding, or visible positioning may explain reaction.

To Risk / Red Team when cross-asset stress identifies a thesis failure path.

## G3 FX & Regional Policy Overlay

The G3 overlay is conditional. It is activated when FX, Europe, Japan, regional policy divergence, or asset geography is material.

In full standalone macro reports, include a compact G3 check by default.

See `macro-g3-fx-regional-policy-overlay.md`.

## Macro Expectations & Surprise Framework

Every material macro release, policy event, or market pricing move should be evaluated relative to expectations where available.

See `macro-expectations-surprise-framework.md`.

## Playbook Output Template

Each playbook should be compressible into:

```text
Block Verdict:
Current Role: regime-defining / confirming / stabilizing / risk-overlay / secondary
What Changed:
Signal vs Noise:
Key Evidence:
Expectation / Surprise Context:
Transmission:
Active Triggers:
Confidence:
Limitations:
Handoffs:
```

## Prohibited Behavior

Playbooks must not:

- overstate one indicator;
- ignore contradictory evidence;
- invent latest data;
- treat market pricing as official policy;
- hide stale data;
- produce final investment actions;
- create numeric scores by default;
- turn early warning signals into crisis verdicts without confirmation.
