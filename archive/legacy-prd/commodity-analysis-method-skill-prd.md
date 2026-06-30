# Commodity Analysis Method Skill PRD

## Purpose

This skill defines the step-by-step method used by the Commodity Agent to analyze commodities and commodity-linked exposures.

The skill turns commodity narratives into evidence-tested investment analysis.

## Core Method Sequence

## Step 1 — Confirm User Intent

Determine whether the user wants:

- full commodity analysis;
- focused driver check;
- market regime view;
- instrument-aware check;
- comparison;
- scenario / shock analysis;
- investment decision support.

If the user asks “should I buy?” or similar, the Commodity Agent may answer as a specialist but must not issue final buy / sell / hold.

## Step 2 — Clarify Commodity and Instrument

Identify:

- commodity;
- benchmark or contract where relevant;
- region;
- investment instrument;
- time horizon;
- user objective.

Examples:

- gold bullion vs gold ETF vs gold miners;
- WTI vs Brent vs oil producer equity;
- Henry Hub gas vs LNG exposure;
- copper spot vs copper miner vs copper ETF;
- wheat futures vs agriculture equity basket.

If the instrument is unclear and materially affects the answer, ask or mark limitation.

## Step 3 — Classify Commodity Family

Classify into:

- energy;
- natural gas / LNG;
- precious metals;
- industrial metals / critical minerals;
- uranium;
- agriculture / softs;
- livestock;
- broad commodity basket.

Apply the relevant family playbook.

## Step 4 — Set Analysis Mode

Choose:

- Full Commodity Analysis;
- Focused Driver Check;
- Commodity Market Regime;
- Instrument-Aware Commodity Check;
- Scenario / Shock Mode;
- Comparison Mode.

## Step 5 — Establish Horizon

Separate thesis into:

- 0-3 months;
- 3-18 months;
- 2-10 years.

If the user gives a specific horizon, prioritize it but still flag conflicts across horizons.

## Step 6 — Gather Evidence

Prioritize:

1. official / primary data;
2. recognized commodity data providers;
3. institutional research;
4. reputable media for events;
5. weak commentary only as context.

Capture as-of dates.

If key data is unavailable, use access-aware fallback and reduce confidence.

## Step 7 — Build Demand Map

Identify who consumes or accumulates the commodity.

Include where relevant:

- industries;
- countries;
- importers;
- central banks;
- strategic reserve buyers;
- manufacturers;
- utilities;
- consumers;
- governments;
- investment vehicles.

Translate narratives into testable demand claims.

Ask:

- how large is incremental demand?
- when does it occur?
- where is it visible?
- is it durable?
- can it be substituted?
- is it already priced in?

## Step 8 — Build Supply Map

Identify who produces or can release the commodity.

Include where relevant:

- producing countries;
- producer groups;
- OPEC / policy actors;
- mines;
- shale producers;
- LNG capacity;
- crop acreage and yields;
- secondary supply;
- recycling;
- strategic reserves;
- project pipeline;
- spare capacity.

Ask:

- is supply constrained?
- can supply respond quickly?
- what is the marginal producer?
- what price incentivizes new supply?
- what bottlenecks exist?

## Step 9 — Analyze Inventories, Reserves, and Stocks

Separate:

- commercial inventories;
- exchange stocks;
- warehouse stocks;
- strategic reserves;
- above-ground stocks;
- geological reserves / resources;
- spare capacity.

Do not confuse long-term resources with near-term available supply.

## Step 10 — Analyze Cost Curve and Marginal Cost

Use cost curve as context, not guarantee.

Consider:

- cash cost;
- full-cycle cost;
- all-in sustaining cost;
- incentive price;
- shut-in economics;
- by-product credits;
- cost inflation;
- jurisdictional cost;
- capex cycle.

Never write that price cannot fall below marginal cost.

## Step 11 — Analyze Futures Curve / Roll / Carry

Assess:

- contango;
- backwardation;
- spot vs forward spread;
- roll yield;
- storage and financing cost;
- ETF / futures product implications;
- curve inversion or normalization.

Explain simply in user-facing output.

## Step 12 — Analyze Macro Sensitivity

Assess commodity-specific sensitivity to:

- USD;
- real rates;
- inflation;
- global growth;
- China cycle;
- credit and liquidity;
- FX;
- recession risk;
- policy regime.

Do not replace the Macro Agent’s full macro regime work.

## Step 13 — Analyze Geopolitics and Policy

Ask whether events affect:

- supply;
- demand;
- transport;
- sanctions;
- tariffs;
- export bans;
- strategic reserve releases / refills;
- import behavior;
- stockpiling;
- substitution;
- second-order effects.

Distinguish temporary shock from structural change.

## Step 14 — Analyze Storage, Logistics, and Transport

Where material, assess:

- storage capacity;
- shipping rates;
- chokepoints;
- pipeline capacity;
- LNG shipping;
- port disruptions;
- warehouse queues;
- regional basis;
- spoilage;
- sanctions rerouting.

## Step 15 — Analyze Substitution Risk

Ask:

- can users switch away from this commodity?
- at what price?
- how fast?
- to what substitute?
- is substitution temporary or structural?

## Step 16 — Analyze Market Expectations and Basic Positioning

Perform basic check:

- what is already reflected in price / curve?
- is the thesis consensus?
- are speculative positions crowded?
- do ETF flows confirm or contradict the story?
- is the market underreacting or overreacting?

Deep positioning belongs to Market Positioning Agent.

## Step 17 — Instrument-Aware Check

Classify instrument:

- physical;
- futures;
- physically backed ETF / ETC;
- futures-based ETF / ETC;
- producer equity;
- royalty / streaming company;
- broad basket;
- leveraged / inverse product.

Identify commodity-specific instrument problems.

Hand off wrapper or company analysis to the relevant agent.

## Step 18 — Valuation Context

Assess whether current price is:

- supported by physical balance;
- stretched versus fundamentals;
- below / near / above incentive price;
- dependent on tight scenario;
- vulnerable to normalization;
- supported / pressured by macro.

Do not create precise fair value targets.

## Step 19 — Scenario Analysis

For weather, war, sanctions, policy, and disruption risks, produce:

- base case;
- upside / tightness case;
- downside / normalization case;
- confirm / refute indicators.

Use probabilities only when justified. Otherwise use qualitative likelihood.

## Step 20 — Run Trap Checklist

Check required traps before producing verdict.

If a trap is material, surface it in plain language.

## Step 21 — Rate Blocks with Human Explanations

Use qualitative labels plus explanation:

- Demand: strong / mixed / weak.
- Supply: tight / balanced / loose.
- Inventories: low / normal / high.
- Curve: supportive / neutral / adverse.
- Macro: tailwind / neutral / headwind.
- Instrument fit: clean / imperfect / risky.
- Confidence: high / medium / low.

Every label needs a short human explanation.

## Step 22 — Determine Specialist Verdict

Select one or more:

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

## Step 23 — Determine Actionability

Select:

- Actionable Positive Setup;
- Actionable Negative / Avoid-for-Now Setup;
- Watchlist / Wait-for-Trigger;
- Hedge / Diversifier Candidate;
- Tactical-Only Setup;
- Too Data-Limited.

Do not provide final buy / sell / hold.

## Step 24 — Produce Monitoring Triggers

Include:

- demand triggers;
- supply triggers;
- inventory triggers;
- curve triggers;
- macro triggers;
- policy / geopolitics triggers;
- instrument triggers;
- thesis-break triggers.

## Step 25 — Produce Structured Handoff

Include:

- commodity identity;
- instrument context;
- horizon split;
- demand rating and explanation;
- supply rating and explanation;
- inventory signal and explanation;
- curve / roll signal and explanation;
- macro sensitivity;
- geopolitics / policy sensitivity;
- valuation context;
- actionability label;
- confidence by block;
- key evidence with as-of dates;
- unresolved questions;
- required downstream agents;
- thesis-breaking risks;
- monitoring triggers.
