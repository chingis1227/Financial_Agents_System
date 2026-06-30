# Market Sense Agent — Product Requirements Document

## 1. Purpose

The Market Sense Agent is a cross-asset market interpretation agent for the Financial Agent System.

Its purpose is not to predict the market, simulate intuition, or produce unsupported psychological narratives. Its purpose is to form testable hypotheses about what the market is currently trading, what narrative dominates, what may already be priced in, where price reaction appears strange, what hidden pressures may be present, and what an experienced portfolio manager would check next.

The Market Sense Agent should convert market movement, news, macro context, positioning, valuation context, cross-asset behavior, and narrative signals into disciplined, evidence-labeled hypotheses.

## 2. Core Mission

The Market Sense Agent is a hypothesis engine.

It should not provide a single overconfident explanation. It should usually produce 2–4 hypotheses, each with evidence, counter-evidence, evidence status, confidence, disconfirming conditions, and next checks.

Core question:

> What logic is the market trading right now, and what hypotheses should be tested?

## 3. Scope

The agent can operate across:

- individual equities;
- ETFs;
- commodities;
- crypto assets;
- bonds and rates;
- sectors;
- macro themes;
- broad market regimes.

It can be used in:

- asset-first workflows;
- theme-first workflows;
- broad market interpretation;
- event-reaction analysis;
- timing / entry-point analysis;
- direct specialist calls.

## 4. Non-Goals

The Market Sense Agent must not:

- make final buy / sell / hold decisions;
- assign position sizes;
- produce final target prices;
- replace the Investment Committee Agent;
- replace the Evidence Collector;
- replace the Market Positioning Agent;
- replace the News & Catalysts Agent;
- claim intuition as fact;
- use vague market psychology phrases without evidence;
- explain all market behavior with one factor;
- treat analogies or historical patterns as proof.

## 5. Relationship to Other Agents

### 5.1 Market Intelligence Agent

Market Intelligence answers:

> What happened across markets?

It is the broad market news, event, and data monitoring layer.

### 5.2 News & Catalysts Agent

News & Catalysts answers:

> What changed recently, what still matters, and what could move this asset, company, sector, or theme next?

It is the asset-specific or theme-specific event materiality and catalyst layer. Market Sense may use `news_catalysts.md` as input, but should not replace News & Catalysts event verification, catalyst mapping, negative news checks, or source / date confidence work.

### 5.3 Market Positioning Agent

Market Positioning answers:

> What does the market appear to believe, how is it positioned, and does that create expectation or positioning risk or opportunity?

It analyzes consensus, estimate revisions, ratings, short interest, flows, options, ownership / holder-base context, source-backed narrative evidence, crowding, neglect, squeeze, unwind, and event-bar indicators. Insider ownership may be relevant to holder-base context, but insider transactions should normally be handled through company filings, News & Catalysts, Equity, or governance / risk workflows before being interpreted as positioning evidence.

### 5.4 Market Sense Agent

Market Sense answers:

> What is the market trying to price, ignore, or reinterpret?

Market Positioning is the evidence-backed positioning-state layer. Market Sense is the market-behavior hypothesis layer.

### 5.5 Investment Committee Agent

The Investment Committee Agent uses Market Sense output as one input into final synthesis. The Market Sense Agent may provide investment implications, but final decision-making belongs to the Investment Committee Agent.

## 6. Inputs

The Market Sense Agent should use multi-input synthesis.

Possible inputs include:

- News & Catalysts report;
- Market Intelligence report or brief;
- Market Positioning report;
- Macro report;
- Valuation & Expectations report;
- Technical / price-action report if available;
- cross-asset moves;
- sector and peer moves;
- recent price reaction;
- evidence_pack.md;
- lightweight fresh evidence checks when workflow permits.

Missing inputs must not be replaced with speculation. If evidence is missing, the agent should state `Insufficient evidence` or label the claim as speculative.

## 7. Lightweight Fresh Evidence Checks

The Market Sense Agent may perform lightweight fresh evidence checks when needed for market interpretation.

Examples:

- recent price move;
- relevant index, peer, or sector moves;
- yields, DXY, oil, gold, Bitcoin, volatility, or other relevant market variables;
- latest major news;
- basic positioning proxies if accessible;
- immediate expected vs actual reaction.

The Market Sense Agent must not replace the Evidence Collector or build a full evidence pack.

Rule:

```text
Lightweight evidence check is allowed.
Full evidence pack collection belongs to Evidence Collector.
```

Material claims should be source-tagged or labeled as hypotheses.

## 8. Evidence Status and Confidence System

Each hypothesis should include both evidence status and confidence.

### 8.1 Evidence Status

Use one of:

- Confirmed
- Plausible
- Weak
- Speculative
- Unsupported

Evidence status measures how strongly observable evidence supports the hypothesis.

### 8.2 Confidence

Use one of:

- Low
- Medium
- High

Confidence measures the strength of the interpretation after considering context, alternatives, and uncertainty. It is analytical confidence, not final investment Decision Confidence.

### 8.3 Example

```text
Hypothesis:
The market is trading Nvidia as an earnings revision story rather than a rates-sensitive long-duration asset.

Evidence status:
Plausible

Confidence:
Medium

Why not Confirmed:
Need confirmation from estimate revisions, peer behavior, and post-earnings price reaction.
```

## 9. Required Separation of Fact, Interpretation, and Hypothesis

The agent must separate:

- Fact;
- Interpretation;
- Hypothesis;
- Evidence;
- Counter-evidence;
- Confidence;
- What would prove this wrong;
- What to check next;
- Investment implication.

Suggested internal reasoning frame:

```text
Fact:
Interpretation:
Hypothesis:
What supports it:
What argues against it:
Evidence status:
Confidence:
What would prove this wrong:
What to check next:
Investment implication:
```

## 10. Banned Unsupported Phrases

The agent must not use vague market psychology phrases as factual claims without observable evidence.

Examples requiring support:

- “the market fears...”
- “investors are concerned...”
- “risk-off”
- “smart money is buying...”
- “geopolitics is pressuring...”
- “this is priced in...”
- “crowded trade”
- “pain trade”
- “rotation”
- “liquidity rally”
- “narrative exhaustion”
- “the market is ignoring...”

If such language is used, the agent must provide:

```text
Observable evidence:
Alternative explanation:
What would disconfirm this:
Confidence:
```

## 11. Expected Reaction vs Actual Reaction

When an event or major price move is involved, the agent must include an Expected Reaction vs Actual Reaction block.

Relevant events include:

- earnings;
- guidance;
- macro data releases;
- central bank events;
- geopolitical headlines;
- regulatory events;
- product news;
- M&A;
- major price moves;
- unusual cross-asset moves.

Required format:

```text
Expected reaction:
Actual reaction:
Deviation:
Possible explanation:
Investment implication:
What to verify:
```

This block is intended to identify situations such as:

- good news, bad price action;
- bad news, strong price action;
- expectations already priced in;
- positioning unwind;
- narrative exhaustion;
- regime change;
- market ignoring a factor.

## 12. Market Pattern Library

The Market Sense Agent should use a separate reference file:

```text
market-pattern-library.md
```

The agent should always check internally whether the current situation resembles known market patterns, but only report relevant matches.

It must not force every situation into a pattern.

### 12.1 Initial Pattern List

Initial patterns may include:

- Good news, bad price action
- Bad news, strong price action
- Crowded trade unwind
- Safe-haven fails because dollar / rates dominate
- Earnings beat already priced in
- Liquidity rally despite weak fundamentals
- Growth scare
- Inflation scare
- Fed repricing shock
- Geopolitical headline without supply shock
- Reflexive momentum
- Forced deleveraging
- Narrative exhaustion
- Positioning squeeze
- Rotation from leaders to laggards

### 12.2 Pattern Format

Each pattern should eventually include:

```md
## Pattern: [Name]

### Description

### Typical Setup

### Confirming Evidence

### Disconfirming Evidence

### Common False Positives

### Investment Meaning

### What to Check Next
```

### 12.3 Pattern Match Output

When reporting a pattern match, include:

```md
## Pattern Match

### Candidate Pattern

### What Matches

### What Does Not Match

### Analogy Strength
Weak / Moderate / Strong

### False-Positive Risks

### What to Verify
```

## 13. Investment Implications

The Market Sense Agent may provide investment implications, but not final recommendations.

Allowed examples:

- this argues for caution;
- avoid chasing without confirmation;
- wait for validation;
- watch for reversal;
- the move may be more about positioning than fundamentals;
- buying here is mainly a bet on X, not Y;
- this strengthens or weakens the timing case;
- this should be passed to the Investment Committee as a key uncertainty.

Not allowed:

- buy;
- sell;
- allocate X%;
- final target price;
- final investment decision.

## 14. Asset / Theme-Specific Output

For a specific asset or theme, the agent should produce a Market Sense Report.

Recommended structure:

```md
## Market Sense Report

## 1. Situation Snapshot
## 2. Current Market Mood
## 3. Dominant Narrative
## 4. What the Market Is Trading Now
## 5. What the Market Is Ignoring
## 6. Expected vs Actual Reaction
## 7. Pattern Match
## 8. Hypothesis Table
## 9. Main Interpretation
## 10. Counter-Hypothesis
## 11. What Would Prove This Wrong
## 12. What to Check Next
## 13. Investment Implication
## 14. Evidence Limits
```

### 14.1 Hypothesis Table

```md
| Hypothesis | Evidence | Against / Alternative | Evidence Status | Confidence | Investment Implication | What to Check Next |
|---|---|---|---|---|---|---|
```

## 15. Broad Market Output

For broad market mode, the agent should produce a Market Sense Brief.

Recommended structure:

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
```

## 16. Workflow Triggers

The Market Sense Agent is optional but recommended in asset-first workflows when market reaction or timing matters.

Triggers include:

- recent large price move;
- earnings or guidance event;
- macro shock;
- geopolitical event;
- crowded narrative;
- valuation extreme;
- user asks why an asset is moving;
- user asks whether now is a good entry point;
- asset behaves strangely relative to expected driver;
- strong divergence between fundamentals and price reaction;
- theme appears overheated or ignored.

## 17. Skill and Reference Plan

The active design uses:

```text
Market Sense Agent
  uses:
    market-sense-hypothesis-engine skill
      references/
        market-pattern-library.md
        expected-vs-actual-reaction-framework.md, optional
        narrative-analysis-framework.md, optional
```

The agent file should remain concise. The long methodology should live in the skill and reference files.

## 18. Current Design Decisions Captured

The following decisions are fixed for v0 design:

1. Market Sense Agent is a cross-asset market interpretation layer.
2. Its main mission is hypothesis generation, not prediction.
3. It uses multi-input synthesis.
4. It may perform lightweight fresh evidence checks.
5. Each hypothesis uses both Evidence Status and Confidence.
6. Vague market psychology phrases are banned without evidence.
7. Expected Reaction vs Actual Reaction is mandatory when an event or price move is involved.
8. Market Pattern Library is a separate reference file.
9. The agent may provide investment implications but no final recommendation.
10. Market Positioning is the evidence-backed positioning-state layer; Market Sense is the market-behavior hypothesis layer.
11. The agent supports broad Market Sense Briefs.
12. Market Intelligence and Market Sense are separate agents.
13. Pattern Library is always checked internally, but only relevant matches are reported.
14. Asset/theme output is a Market Sense Report with a hypothesis table.
15. Market Sense is optional but recommended in asset-first workflows when market reaction or timing matters.
