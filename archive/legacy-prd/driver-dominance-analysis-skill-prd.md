# Driver Dominance Analysis Skill — Product Requirements Document

## 1. Purpose

The `driver-dominance-analysis` skill is a reusable methodology for identifying which market driver, or driver cluster, is currently dominating an asset's price reaction and why.

The skill is designed for use by the Market Sense Agent. It should not be implemented as a standalone agent in v0 unless a later promoted workflow explicitly changes that ownership.

The core task is not to list all drivers of an asset. The core task is to determine which driver is marginally important right now, which drivers are supporting or opposing the move, which drivers were ignored or overridden, and what evidence supports that interpretation.

## 2. Relationship to Market Sense Agent

The Market Sense Agent is the broader market interpretation role. The `driver-dominance-analysis` skill is a specialized method inside that agent.

```text
Market Sense Agent
  uses:
    market-sense-hypothesis-engine skill
    driver-dominance-analysis skill
      references:
        asset-driver-maps.md
        market-pattern-library.md
```

The skill should complement, not replace, the Market Sense Hypothesis Engine. Driver Dominance explains the current driver hierarchy; the Hypothesis Engine converts that analysis into testable market hypotheses.

## 3. Core Question

The skill should answer:

> Which driver is currently dominating the asset's price reaction, and why did that driver matter more than other relevant drivers?

Secondary questions:

- What changed relative to expectations?
- What was already priced in?
- Which related markets confirm or contradict the explanation?
- Which drivers should have mattered but were ignored or overridden?
- Is the move fundamental, positioning-driven, technical, narrative-driven, or macro-driven?

## 4. Core Principle

The central rule:

```text
Markets react to marginal changes in expectations, not static facts.
```

Examples:

Bad reasoning:

```text
Geopolitics is tense, so gold should rise.
```

Better reasoning:

```text
Geopolitical risk may support gold, but the marginal new information was higher real yields and a stronger dollar, while geopolitical risk was already partly priced in.
```

Bad reasoning:

```text
Rates are high, so growth stocks should fall.
```

Better reasoning:

```text
The question is whether rates moved higher than expected and whether earnings revisions were strong enough to offset discount-rate pressure.
```

## 5. Scope

The skill should support cross-asset driver analysis across:

- equities;
- ETFs;
- commodities;
- crypto assets;
- bonds and rates;
- sectors;
- themes;
- broad market indices.

It should be especially useful when several drivers point in different directions.

## 6. Required Inputs

The skill may use:

- user request;
- asset or theme being analyzed;
- relevant price move;
- time window of the move;
- asset-driver-maps.md;
- evidence_pack.md;
- news/catalysts report;
- macro report;
- market positioning report;
- valuation/expectations report;
- technical / price-action report;
- market-pattern-library.md after driver analysis;
- lightweight fresh evidence checks where workflow permits.

If required inputs are unavailable, the skill should label the limitation instead of inventing an explanation.

## 7. Asset Driver Map

The skill should begin by identifying the relevant asset driver map.

The active reference file is:

```text
asset-driver-maps.md
```

The driver map answers:

> Which drivers usually matter for this asset or asset type?

It does not answer:

> Which driver dominates right now?

That is the job of this skill.

## 8. Required Workflow

### Step 1 — Define the Price Move

Identify:

- asset;
- time window;
- direction and magnitude of move;
- relevant event or catalyst;
- whether the move is absolute, relative to peers, or relative to expectations.

### Step 2 — Select Asset Driver Map

Use `asset-driver-maps.md` to identify the normal driver set for the asset.

Examples:

- Gold: real yields, USD, Fed expectations, inflation expectations, geopolitics, ETF flows, central bank buying, positioning.
- AI semiconductor equity: AI capex expectations, data center growth, margins, hyperscaler spending, earnings revisions, valuation, rates, competition, positioning.
- Bitcoin: liquidity, real rates, dollar, ETF flows, stablecoin supply, leverage, regulation, risk appetite, narrative cycle.

### Step 3 — Detect Current Market Context

Determine the current regime or context.

Examples:

- inflation panic;
- growth scare;
- liquidity rally;
- AI momentum;
- risk-off;
- commodity shock;
- central bank repricing;
- geopolitical headline risk;
- credit stress;
- positioning unwind.

The same fact can have different effects in different regimes.

### Step 4 — Detect the Surprise / Marginal Change

Ask:

- What did the market expect before the event?
- What actually happened?
- What changed relative to expectations?
- Was the new information better, worse, or merely different than expected?
- Did expectations change more than the headline fact?

Examples:

- High CPI can be bullish for gold if it was below feared levels.
- Strong earnings can be bearish for a stock if the market expected even stronger guidance.
- Geopolitical tension may not move oil if no physical supply shock occurred.

### Step 5 — Check What Was Already Priced In

Assess whether the thesis or driver was already reflected in price.

Examples:

- Gold had already rallied on geopolitical risk.
- Nvidia already traded at a premium for AI growth.
- Bitcoin had already rallied before ETF approval.
- Uranium stocks had already priced in supply deficit narrative.
- Oil already included geopolitical risk premium.

If a driver was already priced in, new positive news may not move the asset further.

### Step 6 — Cross-Asset Confirmation

Do not explain one asset in isolation.

Check related markets.

Examples for gold:

- DXY;
- real yields;
- Treasury yields;
- rate-cut expectations;
- silver;
- gold miners;
- ETF flows;
- CFTC positioning.

Examples for AI semiconductor equity:

- semiconductor peers;
- Nasdaq;
- AI-related stocks;
- hyperscaler capex commentary;
- yields;
- dollar;
- earnings revisions;
- options positioning.

### Step 7 — Build Driver Battle Matrix

Construct a table showing the driver conflict.

Required format:

```md
| Driver | Normal Impact | Current Signal | Directional Effect | Strength | Evidence | Notes |
|---|---|---|---|---|---|---|
```

Directional Effect should use:

- Positive
- Negative
- Mixed
- Neutral / Not material
- Insufficient evidence

Strength should use:

- Low
- Medium
- High
- Insufficient evidence

The skill should not use numeric scores by default, to avoid false precision.

### Step 8 — Identify Dominant Driver or Driver Cluster

The skill may identify either:

- one dominant driver; or
- one dominant driver cluster.

A driver cluster is appropriate when 2–3 related factors operate through the same mechanism.

Example:

```text
Dominant driver cluster:
Real yields + USD + Fed policy repricing

Primary mechanism:
Higher real yields and stronger dollar outweighed geopolitical support because the marginal change came from rate-cut repricing, while geopolitical risk was already partly priced in.
```

The dominant cluster should not contain more than 2–3 factors unless there is a clear reason.

### Step 9 — Identify Supporting Drivers

Supporting drivers are secondary factors that reinforce the dominant driver.

Example:

- reduced rate-cut expectations;
- stretched prior rally;
- profit-taking;
- weak ETF flows;
- crowded positioning.

### Step 10 — Identify Opposing Drivers

Opposing drivers are factors that should have worked in the other direction.

Example:

- geopolitical risk should normally support gold;
- strong earnings should normally support a stock;
- weak data should normally hurt cyclicals.

### Step 11 — Identify Ignored / Overridden Drivers

This is mandatory.

The skill must explain why an obvious driver did not dominate.

Required format:

```md
## Ignored / Overridden Drivers

| Driver | Why It Normally Matters | Why It Did Not Dominate Now | Evidence |
|---|---|---|---|
```

Example:

```md
| Geopolitical risk | Usually supports safe-haven demand | Market reaction was dominated by stronger USD and rising real yields; geopolitical premium may have been partly priced in | Gold down, DXY up, real yields up, miners weak |
```

### Step 12 — Alternative Explanation

Every conclusion should include an alternative explanation.

Example:

```text
Alternative explanation:
The move may be profit-taking after an extended rally rather than a durable driver shift.
```

### Step 13 — Confidence

Use:

- Low
- Medium
- High

Confidence should depend on:

- evidence quality;
- cross-asset confirmation;
- strength of driver conflict;
- clarity of surprise;
- whether alternative explanations remain plausible;
- freshness of data.

### Step 14 — Pattern Match After Driver Analysis

Only after driver analysis is complete, check `market-pattern-library.md`.

Order matters:

```text
1. Driver map
2. Context
3. Surprise
4. Priced-in check
5. Cross-asset confirmation
6. Driver Battle Matrix
7. Dominant driver / cluster
8. Ignored / overridden drivers
9. Pattern match
```

This prevents the agent from selecting a story first and fitting drivers afterward.

### Step 15 — Investment Implication

The skill may provide investment implications, but not final recommendations.

Allowed:

- this weakens the timing case;
- the move is more about rates than the asset’s core thesis;
- the thesis is not broken, but the current reaction function has changed;
- wait for confirmation in cross-asset drivers;
- do not interpret this as a pure geopolitical move;
- this should be escalated to Investment Committee as a key uncertainty.

Not allowed:

- buy;
- sell;
- allocate X%;
- final target price;
- final investment decision.

## 9. Output Format

The skill should produce a compact diagnostic memo plus Driver Battle Matrix.

Recommended structure:

```md
## Driver Dominance Analysis

## 1. Price Move
## 2. Asset Driver Map Used
## 3. Current Market Context
## 4. What Changed vs Expectations
## 5. What Was Already Priced In
## 6. Driver Battle Matrix
## 7. Dominant Driver / Driver Cluster
## 8. Supporting Drivers
## 9. Opposing Drivers
## 10. Ignored / Overridden Drivers
## 11. Why This Driver Dominated Now
## 12. Cross-Asset Confirmation
## 13. Pattern Match, If Relevant
## 14. Alternative Explanation
## 15. Confidence
## 16. Investment Implication
## 17. Evidence Limits
```

## 10. Guardrails

The skill must not:

- create a beautiful post-hoc story without evidence;
- explain everything with one factor when drivers conflict;
- ignore drivers that contradict the conclusion;
- make a conclusion without cross-asset checks when those checks are available;
- confuse level with change;
- confuse a good story with information not yet priced in;
- overstate confidence;
- use pattern matching before driver analysis;
- present speculation as fact.

## 11. Bad vs Better Reasoning Examples

### Gold

Bad:

```text
There is geopolitical tension, so gold should rise.
```

Better:

```text
Geopolitical tension is a positive driver for gold, but current cross-asset evidence suggests the dominant driver is higher real yields and a stronger dollar. Geopolitical risk may have been partly priced in or weaker than the rates/dollar repricing.
```

### Growth Equity

Bad:

```text
Rates are high, so growth stocks should fall.
```

Better:

```text
Higher rates are a negative driver for long-duration growth equities, but the stock may rise if earnings revisions and AI capex expectations are improving faster than discount-rate pressure.
```

### Oil

Bad:

```text
Geopolitics means oil should rise.
```

Better:

```text
Geopolitical headlines may support oil, but a durable move usually requires evidence of physical supply disruption, inventory draw, tighter futures curve, or higher risk premium confirmed by related markets.
```

## 12. Relationship to Active References

### 12.1 asset-driver-maps.md

The active `asset-driver-maps.md` reference defines normal driver maps by asset type.

v0 maps should include:

1. Gold
2. Oil
3. Broad equity index
4. Individual growth equity
5. AI / semiconductor equity
6. Banks / financials
7. Commodity producers
8. Bitcoin
9. Long-duration bonds / TLT
10. Credit / corporate bonds
11. USD / FX-sensitive assets
12. Thematic ETFs

### 12.2 market-pattern-library.md

The `market-pattern-library.md` reference should be used after driver analysis to classify the market pattern, if a relevant pattern exists.

## 13. Current Design Decisions Captured

1. `driver-dominance-analysis` is a skill inside Market Sense Agent, not a standalone agent in v0.
2. `asset-driver-maps.md` should be a separate reference.
3. v0 asset driver maps should cover a core cross-asset set.
4. Output should be a compact diagnostic memo plus Driver Battle Matrix.
5. Driver strength should be qualitative: Low / Medium / High.
6. The skill may identify a dominant driver cluster, not only one driver.
7. Ignored / Overridden Drivers is a mandatory block.
8. Market Pattern Library should be used only after driver analysis.
9. The core principle is that markets react to marginal changes in expectations, not static facts.
