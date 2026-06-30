# Market Positioning Framework

<!-- reference-governance:start -->
## Reference Governance Metadata

Status: Supporting Reference  
Owner: Market Positioning  
Contributors: Market Sense; Evidence Collector; asset-class agents  
Used by: Market Positioning Agent; market-positioning skill  
Primary reference for: positioning, crowding, and flow framework examples  
Supporting reference for: market-pattern and risk-context interpretation  
Not responsible for: final decision; evidence readiness; routing; IC Action; agent ownership  
Freshness sensitivity: High  
Last reviewed: 2026-06-28  
Review trigger: Review quarterly or when positioning data availability, flow sources, or market-structure assumptions change.  
Owner review needed: No  
Split/index status: Indexed in implementation/reference-library-index.md  
Canonical authority: Advisory reference only. Canonical implementation documents govern active agent, skill, evidence, routing, and IC behavior.

<!-- reference-governance:end -->


## Objective

This framework provides advisory structure, definitions, source overlays, freshness nuances, evidence-ladder examples, positioning archetypes, output examples, and prohibited-language examples for Market Positioning analysis. `implementation/04-evidence-layer.md` governs evidence readiness and source authority.

It supports:

```text
market_positioning.md
focused_positioning_note.md
```

The framework is equity-first, with cross-asset extension hooks.

## Core Output Structure

## Market Positioning Analysis

## 1. Positioning Verdict Box

```text
Asset / Security:
As-of Date:
Output Status: Complete Market Positioning / Limited Market Positioning / Blocked Market Positioning

Market Belief:
Expectation Bar: High / Moderate / Low / Unclear
Revision Direction: Positive / Negative / Stable / Mixed / Unavailable
Positioning Skew: Crowded Long / Crowded Short / Under-owned / Balanced / Mixed / Unclear
Crowding / Neglect Signal: Confirmed / Probable / Possible / Unsupported / Not Material
Primary Positioning Archetype:
Secondary Archetypes:
Decision Relevance: High / Medium / Low
Confidence: High / Medium / Low
Key Limitation:
```

## 2. Scope, Status, and Data Freshness

```text
Scope:
Question Answered:
Time Horizon:
Evidence Pack Used:
Specialist Discovery Used:
Output Status:
Reason for Status:
Material Missing Data:
Freshness Summary:
```

## 3. Observable Evidence Snapshot

Use a compact table:

| Channel | Status | Source Type | Data Date / Period | Freshness | Direct or Proxy | Claim Strength |
|---|---|---|---|---|---|---|
| Consensus / Revisions |  |  |  |  |  |  |
| Ratings / Targets |  |  |  |  |  |  |
| Ownership / Holder Base |  |  |  |  |  |  |
| ETF / Fund Flows |  |  |  |  |  |  |
| Short Interest / Borrow |  |  |  |  |  |  |
| Options Positioning |  |  |  |  |  |  |
| Narrative / Sentiment |  |  |  |  |  |  |
| Price Reaction / Volume |  |  |  |  |  |  |

Allowed channel statuses:

```text
Complete
Limited
Missing
Not Material
```

Allowed claim strength:

```text
Strong
Moderate
Weak
Unsupported
```

## 4. Consensus / Revisions / Ratings

Cover:

```text
Consensus direction:
Revision direction:
Revision breadth:
Revision acceleration / deceleration:
Estimate dispersion:
Rating distribution:
Upgrade / downgrade trend:
Target direction:
Staleness caveat:
Interpretation:
```

Rules:

- consensus is a benchmark, not truth;
- sell-side is visible expectations, not buy-side truth;
- target price upside is not a valuation conclusion;
- stale targets must be labelled.

## 5. Ownership / Holder Base / Flows

Cover:

```text
Institutional ownership:
Holder concentration:
Recent disclosed changes:
Active vs passive exposure:
ETF / fund flows:
Sector / theme proxy flows:
Flow period:
Direct vs proxy status:
Filing lag:
Interpretation:
```

Rules:

- delayed filings support lag-aware claims only;
- proxy flows must not be overstated;
- high ownership does not automatically mean crowding;
- low ownership does not automatically mean opportunity.

## 6. Short Interest / Borrow / Options

Cover:

```text
Short interest:
Short interest as % of float:
Days to cover:
Short interest change:
Borrow cost / availability:
Options volume:
Open interest:
Implied volatility:
Skew:
Put / call ratios:
Event implied move:
Interpretation:
```

Rules:

- high short interest alone does not prove squeeze risk;
- options activity is not direct sentiment translation;
- stale options data cannot support current squeeze or hedging claims;
- borrow data, if unavailable, must be disclosed.

## 7. Narrative / Sentiment Evidence

Classify narrative evidence:

```text
Strong
Moderate
Weak
Unsupported
```

Use:

```text
Key narrative:
Evidence sources:
Narrative breadth:
Narrative change:
Narrative saturation risk:
Limitations:
```

Rules:

- narrative must be observable, sourced, and dated;
- media attention is not proof of capital positioning;
- social media and anecdotal commentary are weak pointer evidence only;
- unsupported “everyone believes” claims are prohibited.

## 8. Price Reaction as Positioning Evidence

Cover:

```text
Pre-event move:
Event reaction:
Post-event follow-through or fade:
Relative performance:
Volume confirmation:
Multiple expansion / compression where available:
Interpretation:
```

Rules:

- price action is supporting evidence of expectations or participation pressure;
- it is not a technical trading signal;
- no support / resistance, breakout, stop-loss, or entry timing recommendations.

## 9. Signal Contradictions and Interpretation

Use template:

```text
Contradiction:
Possible Explanation:
Evidence Strength:
What Would Confirm:
What Would Disconfirm:
Downstream Handoff:
```

Common contradictions:

```text
Bullish ratings but falling revisions.
Positive results but weak price reaction.
High short interest but rising price.
Strong ownership but negative flows.
Positive revisions but multiple compression.
Strong narrative but weak estimate support.
```

## 10. Positioning Archetypes

Assign:

```text
Primary Archetype:
Secondary Archetype 1:
Secondary Archetype 2:
Evidence Strength:
Decision Relevance:
```

Controlled taxonomy:

```text
Crowded Long
Crowded Short
Probable Narrative Saturation
Under-owned / Neglected
Consensus Reset Underway
Positive Revision Momentum
Negative Revision Momentum
Event Bar Too High
Event Bar Low / Less Bad Than Feared
Short-Squeeze Setup
Positioning Unwind
Balanced / No Strong Signal
Unclear / Insufficient Evidence
```

## 11. Expectation / Positioning Risks and Opportunities

Use:

```text
Expectation Risk:
Crowding Risk:
Neglect / Under-Ownership Opportunity:
Squeeze / Unwind Risk:
Event-Bar Risk:
Narrative Fatigue Risk:
What Would Change the View:
```

This section must not issue final investment action.

## 12. Handoff to Valuation & Expectations

```text
Visible Expectations Handoff:
- Consensus / revision context:
- Market belief that valuation should test:
- Expectation bar:
- Areas where price-implied expectations may differ from visible expectations:
- Data limitations:
```

Do not perform reverse DCF or valuation attractiveness analysis.

## 13. Handoff to Risk / Red Team

```text
Positioning Risk Handoff:
- Risk mechanism:
- Evidence:
- Claim strength:
- Freshness caveat:
- What would confirm:
- What would disconfirm:
- Impact on thesis / valuation:
```

## 14. Handoff to News & Catalysts

```text
News / Catalyst Handoff:
- Event or catalyst whose reaction matters:
- Whether reaction suggests expectation reset:
- Whether revisions followed the event:
- Whether event bar appears high or low:
- Missing event evidence:
```

Do not recap all news.

## 15. Handoff to Market Sense / Macro

```text
Market Sense / Macro Handoff:
- Positioning or reaction pattern that may need explanation:
- Cross-asset / sector clues:
- Macro variable possibly influencing positioning:
- Confidence:
```

Use when price reaction or broad positioning requires interpretation beyond asset-specific positioning.

## 16. Handoff to Investment Committee

```text
IC Handoff:
- What the market appears to believe:
- What is already visible or likely recognized:
- Expectation bar:
- Crowding / neglect signal:
- Main positioning risk or opportunity:
- Decision relevance:
- Confidence / limitations:
- Required follow-up before positive action:
```

No final action.

## Appendix

## A. Source Table

| Claim | Source | Source Tier | Evidence Type | Data Date | Accessed Date | Data Period | Freshness | Direct / Proxy | Limitation |
|---|---|---|---|---|---|---|---|---|---|

## B. Missing / Stale / Proxy Evidence

```text
Missing Evidence:
Why It Matters:
Allowed Claim Strength:
What Would Be Needed:
```

## C. Channel-Level Notes

Detailed notes for each channel.

## D. “Priced In?” Caveat

Use when relevant:

```text
Visible expectations appear to reflect [theme / risk / catalyst], but whether the current price fully discounts it belongs to Valuation & Expectations and Investment Committee synthesis.
```

## Advisory Source Overlay

## General Principle

```text
Direct, dated, sourceable, repeatable evidence outranks interpreted, anecdotal, or narrative evidence.
```

## Channel-Specific Preferred Sources

### Consensus / Revisions

Preferred:

- recognized estimate providers;
- company guidance;
- analyst revision aggregators;
- reputable institutional data providers.

Use with caution:

- isolated analyst notes;
- financial media summaries of consensus;
- stale target price tables.

Do not use:

- unsourced “analysts expect” statements;
- AI-generated summaries as evidence.

### Ratings / Targets

Preferred:

- recognized analyst rating aggregators;
- institutional data providers;
- dated analyst actions where accessible.

Rules:

- distinguish rating distribution from rating changes;
- distinguish target price level from target direction;
- label stale targets.

### Ownership / Holder Base

Preferred:

- SEC filings;
- Form 13F;
- Form 13D;
- Form 13G;
- fund reports;
- issuer ownership data;
- reliable ownership data providers.

Rules:

- disclose filing lag;
- do not claim current ownership from delayed filings;
- identify passive vs active where possible.

### Short Interest / Borrow

Preferred:

- official exchange short interest;
- FINRA short interest;
- securities lending / borrow data where available;
- reliable market data providers.

Rules:

- disclose settlement / report date;
- disclose reporting lag;
- high short interest alone does not prove squeeze risk.

### Options

Preferred:

- OCC options volume and open interest;
- Cboe / exchange options statistics;
- reliable options market data providers;
- implied volatility, skew, and open interest datasets.

Rules:

- options are supporting evidence;
- distinguish volume from open interest;
- avoid direct sentiment translation;
- label event-volatility and hedging ambiguity.

### ETF / Fund Flows

Preferred:

- ETF issuer data;
- fund reports;
- recognized fund-flow providers;
- holdings data;
- sector or theme ETF data where relevant.

Rules:

- distinguish asset-specific from proxy flows;
- disclose flow period;
- avoid overstating theme flows as single-name flows.

### Narrative / Sentiment

Preferred:

- earnings call Q&A;
- management commentary;
- analyst language where accessible;
- institutional commentary;
- reputable financial media framing;
- repeated source-backed theme references.

Weak pointer only:

- social media;
- anecdotal investor commentary;
- one-off headlines;
- vague market chatter.

## Freshness Rules

## General Rule

Freshness is channel-specific.

Stale data may still support lag-aware conclusions, but must not support current-position claims.

## Channel Freshness

```text
Price / volume / relative performance:
latest available when used for current positioning or market reaction.

Options:
latest available or clearly dated; stale options data cannot support current squeeze or hedging claims.

Short interest:
latest official reporting cycle; disclose settlement date, report date, and reporting lag.

Consensus / estimates / revisions:
latest available from recognized source; state data date and revision window.

Ratings / target changes:
latest available; distinguish current rating distribution from recent change direction.

ETF / fund flows:
daily / weekly / monthly depending on source; disclose period and whether asset-specific or proxy.

Ownership / 13F / fund holdings:
latest filing period; disclose filing lag and avoid current-position claims unless updated data exists.

Narrative / sentiment:
recent enough for the claim being made; weak if based only on media impressions or anecdotal commentary.
```

## Evidence Ladders

## Crowding Ladder

### Confirmed Crowding

Requires multiple direct evidence channels, such as:

- concentrated ownership;
- strong recent inflows;
- options positioning confirmation;
- sector/theme flow concentration;
- fund overlap;
- crowded factor exposure;
- short or long positioning data.

### Probable Crowding

Requires at least one direct evidence channel plus multiple supporting proxies.

Examples:

- ownership concentration plus narrative saturation;
- strong inflows plus price outperformance and bullish revisions;
- elevated options activity plus pre-event run-up and bullish rating skew.

### Possible Crowding / Narrative Crowding

Uses mostly indirect evidence:

- high media attention;
- strong momentum;
- common narrative;
- repeated analyst discussion;
- anecdotal investor focus.

This cannot support a confirmed crowding conclusion.

### Unsupported Crowding Claim

Use when evidence is missing, weak, stale, or only vibe-based.

## Neglect / Under-Ownership Ladder

### Confirmed Neglect

Requires direct evidence of low ownership / low coverage / weak flows / low attention plus plausible positive change.

### Probable Neglect

Requires some direct evidence plus confirming proxies, such as:

- limited analyst coverage;
- low institutional ownership;
- weak flows;
- low narrative attention;
- stabilizing revisions;
- improving guidance.

### Possible Neglect

Mostly indirect evidence:

- low media attention;
- limited sell-side discussion;
- muted reaction;
- low liquidity.

### Unsupported Neglect Claim

Use when the only evidence is that the asset is unpopular, or when weakness appears fundamentally justified.

## Short-Squeeze Ladder

```text
No material short signal
Elevated short interest
Crowded short
Possible squeeze setup
Probable squeeze setup
Confirmed squeeze dynamics
Insufficient evidence
```

A probable or confirmed squeeze setup requires more than high short interest. It should include a catalyst, price movement against shorts, liquidity constraints, volume confirmation, borrow stress where available, or options / positioning confirmation.

## Narrative Evidence Ladder

```text
Strong:
Repeated source-backed analyst, earnings-call, institutional, and reputable media framing, ideally supported by flows, revisions, or market reaction.

Moderate:
Repeated reputable-source references without strong direct positioning confirmation.

Weak:
Anecdotal commentary, social media, one-off stories, or vague market chatter.

Unsupported:
No reliable source support.
```

## Confidence Labels

Use:

```text
High
Medium
Low
```

High confidence requires direct, fresh, multi-channel evidence.

Medium confidence can use one direct channel plus supporting proxies.

Low confidence should be used for proxy-only, stale, incomplete, or contradictory evidence.

Confidence is not a probability.

## Output Status Labels

## Complete Market Positioning

Use when all material channels for the question have adequate evidence.

## Limited Market Positioning

Use when bounded interpretation is possible, but one or more material channels are missing, stale, proxy-only, paywalled, or contradicted.

## Blocked Market Positioning

Use when the core question cannot be answered without unsupported inference.

## Allowed Language

```text
Visible expectations appear demanding.
Consensus revisions have been positive but are slowing.
The expectation bar appears high.
The crowding signal is probable, not confirmed.
Narrative saturation appears possible.
Options activity suggests elevated event-related positioning, but direction is ambiguous.
Recent disclosed ownership was concentrated, but current ownership cannot be confirmed from delayed filings.
Missing fund-flow data limits confidence in the crowding conclusion.
```

## Prohibited Language

```text
Buy.
Sell.
Hold.
Avoid.
Add.
Reduce.
Exit.
Initiate.
Do not own this.
Take profits.
Wait for a pullback.
This is undervalued.
This is overvalued.
This is cheap.
This is too expensive.
This is fully priced in.
The target price should be X.
Position size should be X.
Everyone loves this stock.
High call volume proves bullish sentiment.
High short interest guarantees a squeeze.
Nobody talks about this, so it is a hidden gem.
```

## Focused Positioning Note Template

Use for direct scoped calls.

```text
## Focused Positioning Note

Scope:
Question:
Asset / Security:
As-of Date:
Output Status:

Short Answer:
Evidence Used:
Channel Status:
Freshness:
Conclusion Strength:
What Can Be Concluded:
What Cannot Be Concluded:
Recommended Handoff:
```

## Final Standard

A Market Positioning report is complete only if it:

- separates evidence from inference;
- states source and freshness limitations;
- avoids unsupported crowding or neglect claims;
- avoids final investment actions;
- avoids valuation conclusions;
- handles contradictions explicitly;
- provides structured handoffs;
- gives IC a concise decision-relevant input.
