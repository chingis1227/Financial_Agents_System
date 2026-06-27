# Market Sense Hypothesis Engine Skill — Product Requirements Document

## 1. Purpose

The `market-sense-hypothesis-engine` skill is the core reusable methodology for the Market Sense Agent.

Its purpose is to convert market facts, price reactions, news, macro signals, positioning data, valuation context, and cross-asset behavior into disciplined, testable market hypotheses.

The skill should not predict markets, simulate intuition, or make final investment decisions. It should structure market interpretation in a way that separates observable evidence from interpretation and speculation.

## 2. Relationship to Market Sense Agent

The Market Sense Agent is the role. The `market-sense-hypothesis-engine` skill is the method.

```text
Market Sense Agent
  uses:
    market-sense-hypothesis-engine skill
      references:
        market-pattern-library.md
```

The agent should remain concise and role-based. The detailed reasoning workflow belongs in this skill.

## 3. Core Question

The skill should help answer:

> What logic is the market trading right now, and what hypotheses should be tested?

It should produce a disciplined interpretation, not a single unsupported explanation.

## 4. Supported Use Cases

The skill should support:

- asset-specific market interpretation;
- theme-specific market interpretation;
- broad market sense briefs;
- event reaction analysis;
- strange price reaction analysis;
- timing / entry interpretation;
- narrative and expectation analysis;
- direct specialist calls to Market Sense Agent.

## 5. Inputs

The skill may use:

- user request;
- evidence_pack.md;
- market intelligence report;
- news/catalysts report;
- market positioning report;
- macro report;
- valuation/expectations report;
- technical or price-action report;
- cross-asset market data;
- sector and peer moves;
- lightweight fresh evidence checks where workflow permits;
- market-pattern-library.md.

Missing inputs must be explicitly labeled. The skill must not fill missing data with confident interpretation.

## 6. Operating Principles

### 6.1 Hypothesis First, Not Oracle

The skill should normally produce 2–4 hypotheses.

Each hypothesis must include:

- hypothesis statement;
- supporting evidence;
- counter-evidence or alternative explanation;
- evidence status;
- confidence;
- what would prove it wrong;
- what to check next;
- investment implication.

### 6.2 Separate Fact, Interpretation, and Hypothesis

The skill must always distinguish:

- Fact: observable or source-backed information.
- Interpretation: what the facts may mean.
- Hypothesis: a testable explanation.
- Evidence: what supports the hypothesis.
- Counter-evidence: what argues against it.
- Next checks: what should be verified before relying on it.

### 6.3 No Unsupported Market Psychology

The skill must not use vague market psychology phrases unless supported by observable evidence.

Restricted phrases include:

- the market fears;
- investors are concerned;
- risk-off;
- smart money is buying;
- geopolitics is pressuring;
- priced in;
- crowded trade;
- pain trade;
- rotation;
- liquidity rally;
- narrative exhaustion;
- the market is ignoring.

If such language is used, the skill must provide:

```text
Observable evidence:
Alternative explanation:
What would disconfirm this:
Confidence:
```

### 6.4 Pattern Library Is an Aid, Not Proof

The skill should use `market-pattern-library.md` to identify possible analogies, but patterns are not evidence by themselves.

The skill must ask:

- Which pattern might this resemble?
- What matches?
- What does not match?
- What false positives are possible?
- What evidence would confirm or reject the analogy?

If no pattern clearly fits, the correct answer is:

```text
No clear pattern confirmed. Evidence is insufficient.
```

## 7. Evidence Status and Confidence

Each hypothesis should have both evidence status and confidence.

### 7.1 Evidence Status

Use:

- Confirmed
- Plausible
- Weak
- Speculative
- Unsupported

### 7.2 Confidence

Use:

- Low
- Medium
- High

### 7.3 Interpretation

Evidence status measures support from observable evidence.

Confidence measures the strength of the interpretation after considering alternatives and uncertainty. It is analytical confidence, not final investment Decision Confidence.

A hypothesis can be Plausible with Low confidence if some evidence exists but alternatives remain strong.

## 8. Required Workflow

The skill should follow this sequence:

### Step 1 — Define the Situation

Clarify:

- asset / market / theme;
- time horizon of the move;
- relevant event or catalyst;
- user’s question;
- whether this is asset-specific or broad market mode.

### Step 2 — Collect or Read Inputs

Use available reports first. If the workflow allows, perform lightweight fresh evidence checks for market interpretation.

Do not build a full evidence pack unless explicitly assigned.

### Step 3 — Identify Observable Facts

List only source-backed or observable facts.

Examples:

- price move;
- peer move;
- yield move;
- dollar move;
- ETF flow;
- credit spread change;
- earnings guidance;
- news event;
- options or positioning signal.

### Step 4 — Identify What the Market Appears to Be Trading

Form an interpretation of which variables seem to matter now.

Examples:

- earnings revisions;
- rates / real yields;
- liquidity;
- geopolitical supply shock;
- positioning unwind;
- narrative exhaustion;
- credit stress;
- policy easing expectations.

### Step 5 — Compare Expected vs Actual Reaction

If an event or material price move is involved, include:

```text
Expected reaction:
Actual reaction:
Deviation:
Possible explanation:
Investment implication:
What to verify:
```

### Step 6 — Check Pattern Library

Use `market-pattern-library.md` to identify 1–3 candidate patterns.

For each relevant match, state:

- candidate pattern;
- what matches;
- what does not match;
- analogy strength: Weak / Moderate / Strong;
- false-positive risks;
- what to verify.

### Step 7 — Generate Hypotheses

Generate 2–4 hypotheses.

Each hypothesis should be testable, not vague.

Bad:

```text
The market is worried.
```

Good:

```text
The market may be treating the asset as a real-yield / dollar-sensitive asset rather than a geopolitical hedge.
```

### Step 8 — Rank Hypotheses

Rank hypotheses by:

- evidence strength;
- explanatory power;
- consistency with cross-asset behavior;
- weakness of alternatives;
- investment relevance.

### Step 9 — State What Would Prove the Main Hypothesis Wrong

Every main hypothesis must include disconfirmation conditions.

Example:

```text
This hypothesis would weaken if real yields stabilize and the dollar stops rising, but gold continues to fall.
```

### Step 10 — Produce Investment Implication

The skill may provide investment implications, but not final recommendations.

Allowed:

- this argues for caution;
- avoid chasing without confirmation;
- wait for validation;
- the move may be more about positioning than fundamentals;
- buying here is mainly a bet on X, not Y;
- this should be passed to the Investment Committee as a key uncertainty.

Not allowed:

- buy;
- sell;
- allocate X%;
- final target price;
- final investment decision.

## 9. Pattern Decision Tree

The skill should use the following routing logic before reading detailed patterns:

```text
Is there a specific event or headline?
  -> Check Event Reaction Patterns.

Is price reacting strangely relative to the headline?
  -> Check Expected vs Actual Reaction and Event Reaction Patterns.

Is positioning, crowding, short interest, options, or flow central?
  -> Check Positioning / Flow Patterns.

Are rates, real yields, dollar, liquidity, or central-bank expectations moving?
  -> Check Macro / Rates / Liquidity Patterns.

Are multiple asset classes moving together in a regime-like way?
  -> Check Cross-Asset / Regime Patterns.

Are credit spreads, volatility, funding, or liquidity stress rising?
  -> Check Stress / Deleveraging Patterns.

Is the situation commodity/geopolitical/supply-demand driven?
  -> Check Commodity / Geopolitical Patterns.

Is the story widely known and no longer moving price?
  -> Check Expectations / Narrative Patterns.
```

## 10. Output Formats

### 10.1 Asset / Theme Market Sense Report

```md
## Market Sense Report

## 1. Situation Snapshot
## 2. Observable Facts
## 3. Current Market Mood
## 4. Dominant Narrative
## 5. What the Market Is Trading Now
## 6. What the Market Is Ignoring
## 7. Expected vs Actual Reaction
## 8. Pattern Match
## 9. Hypothesis Table
## 10. Main Interpretation
## 11. Counter-Hypothesis
## 12. What Would Prove This Wrong
## 13. What to Check Next
## 14. Investment Implication
## 15. Evidence Limits
```

Hypothesis table:

```md
| Hypothesis | Evidence | Against / Alternative | Evidence Status | Confidence | Investment Implication | What to Check Next |
|---|---|---|---|---|---|---|
```

### 10.2 Broad Market Sense Brief

```md
## Market Sense Brief

## Current Market Mood
## Dominant Narratives
## Cross-Asset Signals
## What the Market Is Trading
## What the Market Is Ignoring
## Strange Reactions
## Main Hypotheses
## Counter-Hypotheses
## Confidence and Evidence Status
## What to Check Next
## Portfolio / Watchlist Implications
## Evidence Limits
```

## 11. Quality Checks

Before finalizing output, the skill should verify:

- every factual claim has evidence or is labeled as assumption;
- interpretations are not presented as facts;
- vague market psychology phrases have observable support;
- each hypothesis has counter-evidence or alternative explanation;
- pattern matches are not forced;
- confidence is not overstated;
- missing evidence is disclosed;
- investment implication is not a final recommendation.

## 12. Non-Goals

The skill should not:

- build a full evidence pack;
- replace Market Intelligence Agent;
- replace Market Positioning Agent;
- replace News & Catalysts Agent;
- replace Macro Agent;
- replace Valuation & Expectations Agent;
- replace Investment Committee Agent;
- produce price targets;
- produce buy/sell recommendations;
- generate unsupported market psychology narratives.

## 13. Current Design Decisions Captured

1. The skill is a hypothesis engine.
2. It supports cross-asset market interpretation.
3. It uses multi-input synthesis.
4. It may perform lightweight fresh evidence checks.
5. It must separate facts, interpretations, and hypotheses.
6. It uses evidence status and confidence for every hypothesis.
7. It bans unsupported market psychology phrases.
8. It requires Expected vs Actual Reaction when an event or major price move is involved.
9. It uses `market-pattern-library.md` as a reference.
10. Pattern matching is an aid, not proof.
11. It may provide investment implications but no final recommendation.
12. It supports both Market Sense Report and Market Sense Brief outputs.
