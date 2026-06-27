# Commodity Analysis Framework

## Purpose

This framework defines the standard outputs for the Commodity Agent.

The outputs are memo-first, simple enough for a user to read, and structured enough for downstream agents.

## Output 1 — commodity_analysis.md

Used for a specific commodity or commodity-linked exposure.

### 1. Executive View

Plain-language answer.

Include:

- main commodity conclusion;
- whether the market looks tight, balanced, loose, stretched, or shock-driven;
- what matters most;
- whether further investment analysis is supported;
- one-line key risk.

No jargon-heavy opening.

### 2. Commodity Identity and Instrument Context

Specify:

- commodity;
- benchmark / contract if relevant;
- region;
- instrument;
- exposure type;
- user horizon;
- analysis mode.

Clarify if the exposure is:

- spot / physical;
- futures;
- ETF / ETC;
- producer equity;
- miner;
- royalty / streamer;
- broad basket;
- leveraged / inverse product.

### 3. Thesis by Horizon

Separate:

- near-term: 0-3 months;
- medium-term: 3-18 months;
- long-term: 2-10 years.

Explain conflicts across horizons.

### 4. Demand Map

Show who buys or consumes the commodity.

Include where relevant:

- industries;
- countries;
- central banks;
- strategic reserves;
- governments;
- utilities;
- consumers;
- manufacturers;
- investment demand.

Each major demand claim should be evidence-testable.

### 5. Supply Map

Show who produces or releases supply.

Include where relevant:

- producer countries;
- producer groups;
- OPEC / policy actors;
- mines;
- shale;
- LNG capacity;
- crops;
- recycling;
- secondary supply;
- project pipeline;
- spare capacity.

### 6. Inventories / Reserves / Trade Flows

Separate:

- commercial inventories;
- exchange inventories;
- strategic reserves;
- above-ground stocks;
- geological reserves / resources;
- spare capacity;
- trade flows.

Explain whether inventories confirm or contradict the thesis.

### 7. Futures Curve / Roll / Carry

Explain:

- contango / backwardation;
- roll yield;
- what the curve implies;
- whether curve supports or weakens the thesis;
- impact on futures-based products.

User-facing language must be simple.

### 8. Macro Sensitivity

Analyze commodity-specific sensitivity to:

- USD;
- real rates;
- inflation;
- growth;
- China cycle;
- liquidity;
- FX;
- recession risk.

If macro is decisive, hand off to Macro Agent.

### 9. Geopolitics / Policy Layer

Analyze:

- sanctions;
- war / shipping disruption;
- tariffs;
- export bans;
- OPEC / producer policy;
- strategic reserve release / refill;
- industrial policy;
- energy transition policy.

Explain transmission into supply, demand, transport, or inventories.

### 10. Storage / Logistics / Transport

Where material, include:

- storage capacity;
- freight;
- pipelines;
- ports;
- LNG shipping;
- chokepoints;
- warehouse queues;
- regional basis;
- spoilage.

### 11. Cost Curve / Marginal Cost / Incentive Price

Discuss:

- marginal producer;
- incentive price;
- cost curve;
- shut-in economics;
- capex cycle;
- cost inflation.

Do not treat cost as a guaranteed price floor.

### 12. Substitution Risk

Explain whether high prices may destroy or redirect demand.

Include substitutes and timing.

### 13. Valuation Context

Classify price as:

- supported;
- stretched;
- cheap but risky;
- dependent on tight scenario;
- vulnerable to normalization;
- unclear / data-limited.

No precise price targets unless externally sourced and clearly caveated.

### 14. Instrument-Aware Check

Explain whether the instrument cleanly expresses the commodity view.

Flag:

- roll drag;
- contango;
- leverage / inverse reset;
- broad basket contamination;
- producer equity impurity;
- ETF wrapper issues;
- liquidity;
- tracking risk.

Hand off as needed.

### 15. Trap Checklist

State the main traps checked.

Do not include a bureaucratic checklist unless useful; summarize material traps in plain language.

### 16. Specialist Verdict

Use labels such as:

- Fundamentally Supported;
- Fundamentally Stretched;
- Tight but Fragile;
- Oversupplied / Weak Balance;
- Macro-Supported;
- Macro-Headwind;
- Event-Driven / Shock-Driven;
- Instrument-Impaired;
- Narrative-Heavy / Data-Light;
- Unclear / Data-Limited.

Explain in one paragraph.

### 17. Actionability

Use:

- Actionable Positive Setup;
- Actionable Negative / Avoid-for-Now Setup;
- Watchlist / Wait-for-Trigger;
- Hedge / Diversifier Candidate;
- Tactical-Only Setup;
- Too Data-Limited.

Do not use buy / sell / hold.

### 18. Monitoring Triggers

Include:

- demand trigger;
- supply trigger;
- inventory trigger;
- curve trigger;
- macro trigger;
- policy / geopolitics trigger;
- instrument trigger;
- thesis-break trigger.

### 19. Evidence Notes and Limitations

Include:

- source;
- as-of date;
- what it supports;
- source quality;
- limitation.

Main text should remain readable; evidence detail belongs here.

### 20. Structured Handoff

```text
commodity_identity:
instrument_context:
analysis_mode:
time_horizon:
demand_rating:
demand_explanation:
supply_rating:
supply_explanation:
inventory_signal:
inventory_explanation:
curve_roll_signal:
curve_roll_explanation:
macro_sensitivity:
geopolitics_policy_sensitivity:
valuation_context:
instrument_fit:
specialist_verdict:
actionability_label:
confidence_by_block:
key_evidence_as_of:
unresolved_questions:
required_downstream_agents:
thesis_breaking_risks:
monitoring_triggers:
```

## Output 2 — commodity_market_regime.md

Used for broad commodity market review.

### 1. Executive Regime View

Classify overall commodity regime as:

- tight;
- loose;
- mixed;
- shock-driven;
- inflationary;
- disinflationary;
- growth-sensitive;
- policy-distorted.

### 2. Cross-Commodity Heatmap

Cover:

- energy;
- precious metals;
- industrial metals;
- uranium;
- agriculture / softs;
- broad baskets.

Use qualitative labels with human explanations.

### 3. Inflation Pressure Signal

Explain whether commodities are adding or reducing inflation pressure.

### 4. Growth Signal

Explain whether commodities confirm or contradict global growth.

### 5. Supply Shock Map

Identify where supply shocks are real, temporary, or structural.

### 6. Demand Strength Map

Highlight China, US, India, Europe, EM demand, central banks, industry-specific demand, and policy demand where relevant.

### 7. Inventory / Reserve Signal

Explain where stocks are tight or loose.

### 8. Curve / Carry Environment

Explain which areas have supportive or adverse curve structure.

### 9. Policy / Geopolitics Layer

Summarize major commodity-relevant policy and geopolitical factors.

### 10. Best / Worst Setup Areas

Identify stronger and weaker commodity setups without final buy / sell / hold.

### 11. Risks and Narrative Traps

Identify over-owned narratives and weak data areas.

### 12. Handoffs

Route to:

- Macro Agent;
- ETF Agent;
- Market Positioning Agent;
- Portfolio Fit Agent;
- Risk / Red Team;
- Investment Committee.

## Rating System

Labels must always include human explanations.

Bad:

```text
Demand: Strong
```

Good:

```text
Demand: Strong — China grid demand and India import demand are improving, while supply response remains slow.
```

## Confidence Blocks

Confidence should be assessed by block:

- demand visibility;
- supply visibility;
- inventory evidence;
- futures curve signal;
- macro sensitivity;
- policy / geopolitical risk;
- instrument fit;
- overall thesis confidence.

## User-Facing Style

The main report should use simple investment language.

Technical terms are allowed only when explained.

Appendices may be more technical.

## Internal Status

Internal states:

- Complete;
- Limited;
- Blocked.

Avoid bureaucratic user-facing status labels unless critical.
