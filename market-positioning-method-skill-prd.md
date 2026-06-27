# Market Positioning Method Skill PRD

## Purpose

The Market Positioning Method Skill defines how to analyze visible market expectations, investor positioning, crowding, neglect, revisions, flows, short interest, options, price reaction, and narrative evidence.

It operationalizes the Market Positioning Agent PRD and produces the analytical basis for `market_positioning.md` or a scoped positioning note.

## Core Doctrine

```text
Market positioning is not sentiment guessing. It is evidence-backed analysis of visible expectations and participation.
```

The skill must separate:

1. observable data;
2. inferred market belief;
3. positioning risk or opportunity;
4. downstream decision relevance.

It must never convert positioning analysis into a final investment action.

## Required Analytical Steps

## 1. Establish Scope

Classify the request as one of:

```text
Full Market Positioning Report
Focused Consensus / Revisions Check
Focused Crowding Check
Focused Short Interest / Squeeze Check
Focused Ownership / Holder Base Check
Focused Options Positioning Check
Focused Flow Check
Focused Narrative / Sentiment Check
Event-Bar / Reaction Check
```

If the user asked a narrow question, remain narrow. Do not expand into a full investment workflow unless the user requests a full decision.

State:

```text
Scope:
Asset / security:
Time horizon:
Question being answered:
What this skill can conclude:
What this skill cannot conclude:
```

## 2. Establish Evidence Readiness

Use `evidence_pack.md` when available.

Check whether relevant evidence is:

```text
Available
Missing
Stale
Proxy-only
Contradicted
Paywalled / inaccessible
Not material
```

If material evidence is missing, decide whether the output can be:

```text
Complete Market Positioning
Limited Market Positioning
Blocked Market Positioning
```

If evidence is insufficient for the requested conclusion, block the specific conclusion rather than improvising.

## 3. Build Channel-Level Evidence Map

Assess material channels:

```text
Consensus / Revisions
Ratings / Targets
Ownership / Holder Base
ETF / Fund Flows
Short Interest / Borrow
Options Positioning
Narrative / Sentiment
Price Reaction / Volume
```

For each channel record:

```text
Data available:
Source:
Source tier:
Data date:
Accessed date:
Data period:
Freshness status:
Direct or proxy:
Channel status:
Claim strength allowed:
```

## 4. Analyze Consensus and Estimate Revisions

Assess:

- current consensus direction;
- revenue / EPS / margin / cash-flow revision trend where available;
- revision breadth;
- revision acceleration or deceleration;
- estimate dispersion;
- whether revisions changed after a catalyst;
- whether consensus appears stale relative to recent events.

Do not treat consensus as truth.

Allowed conclusions:

```text
Visible expectations are rising.
Visible expectations are falling.
Consensus appears stable.
Consensus appears stale.
Revision momentum is positive but slowing.
Estimate dispersion suggests uncertainty.
```

Prohibited conclusions:

```text
The stock is attractive because consensus has upside.
Consensus proves the thesis.
Consensus target implies fair value.
```

## 5. Analyze Ratings and Target Direction

Use sell-side ratings and targets as visible-expectations evidence, not market truth.

Assess:

- rating distribution;
- upgrade / downgrade trend;
- target price revision direction;
- dispersion;
- whether targets appear stale after price movement;
- whether rating skew conflicts with estimate revisions.

Allowed:

```text
Sell-side visible expectations are favorable.
Sell-side optimism appears stale relative to falling revisions.
Target direction has improved, but target upside may reflect stale price inputs.
```

Prohibited:

```text
Analysts have 25% upside, therefore the market expects 25% upside.
```

## 6. Analyze Ownership and Holder Base

Assess:

- institutional ownership;
- insider ownership where relevant;
- holder concentration;
- recent disclosed ownership changes;
- fund overlap;
- active vs passive exposure where available;
- filing lag.

Do not claim current ownership from delayed filings unless updated data exists.

Allowed:

```text
Recent disclosed ownership was concentrated.
The holder base appears institutionally well-owned based on latest filings.
Ownership evidence is stale and cannot support current crowding by itself.
```

## 7. Analyze ETF / Fund / Theme Flows

Assess:

- asset-specific fund flows where available;
- ETF flows into relevant sector/theme vehicles;
- issuer holdings and exposure;
- flow period;
- whether flows are direct or proxy;
- whether flows confirm or contradict price action.

Distinguish:

```text
Asset-specific flows
Sector proxy flows
Theme proxy flows
Factor proxy flows
```

Proxy flows must not be overstated.

## 8. Analyze Short Interest and Squeeze Risk

Assess:

- short interest level;
- short interest as % of float where available;
- days to cover;
- change in short interest;
- borrow cost / availability where available;
- liquidity;
- catalyst risk;
- price trend against shorts.

Classify short setup as:

```text
No material short signal
Elevated short interest
Crowded short
Possible squeeze setup
Probable squeeze setup
Confirmed squeeze dynamics
Insufficient evidence
```

A squeeze conclusion requires more than high short interest. Look for catalyst, price pressure, liquidity, volume, and positioning confirmation.

## 9. Analyze Options Positioning

Use options as supporting evidence, not direct sentiment translation.

Assess:

- unusual volume;
- open interest;
- put / call ratios;
- implied volatility;
- skew;
- event implied move;
- concentration by strike / expiry;
- change versus baseline.

Always consider:

```text
Hedging vs speculation ambiguity
Event-volatility trades
Dealer hedging uncertainty
Single-day noise
Spread structures
```

Allowed:

```text
Options activity suggests elevated event-related positioning, but direction is ambiguous.
Call open interest may support speculative upside interest, but is not standalone proof of bullish sentiment.
```

Prohibited:

```text
High call volume proves investors are bullish.
High put volume proves bearish conviction.
```

## 10. Analyze Price Reaction and Volume as Positioning Evidence

Use price action only as evidence of expectations, reaction function, and participation pressure.

Assess:

- pre-event rally / selloff;
- abnormal volume;
- relative performance vs index / sector / peers;
- reaction to earnings, guidance, news, or macro events;
- post-event follow-through or fade;
- multiple expansion / compression where available.

Allowed:

```text
The stock rallied into the event and faded despite positive headlines, supporting the inference that the expectation bar was high.
```

Prohibited:

```text
The chart failed resistance, so wait for a better entry.
```

## 11. Analyze Narrative and Sentiment Evidence

Narrative evidence must be observable, sourced, and dated.

Classify as:

```text
Strong
Moderate
Weak
Unsupported
```

Strong evidence may include repeated analyst, earnings-call, institutional, or reputable financial media framing supported by flows or positioning.

Weak evidence includes social media, anecdotal commentary, one-off headlines, or unsourced “investors believe” claims.

Do not treat narrative popularity as proof of capital positioning.

## 12. Identify Signal Contradictions

Material contradictions must be treated as diagnostic.

Examples:

```text
Bullish ratings but falling revisions
Positive results but weak price reaction
High short interest but rising price
Strong ownership but negative flows
Positive revisions but multiple compression
Strong narrative but weak estimate support
```

Use template:

```text
Contradiction:
Possible explanation:
Evidence strength:
What would confirm:
What would disconfirm:
Downstream handoff:
```

## 13. Infer Market Belief

After channel analysis, infer what the market appears to believe.

Use careful language:

```text
appears to
suggests
is consistent with
may indicate
supports the inference
```

Avoid unsupported universal claims:

```text
everyone believes
the market knows
investors clearly expect
```

Summarize:

```text
What the market appears to believe:
What evidence supports this:
What evidence contradicts it:
Confidence:
```

## 14. Assess Expectation Bar

Classify expectation bar:

```text
High
Moderate
Low
Unclear
```

Use evidence such as:

- positive revisions;
- premium valuation context from Valuation Agent where available;
- pre-event rally;
- bullish rating skew;
- narrative saturation;
- elevated options implied move;
- strong ownership / flows.

Do not conclude valuation attractiveness. Only assess visible expectation difficulty.

## 15. Classify Crowding

Use evidence ladder:

```text
Confirmed Crowding
Probable Crowding
Possible Crowding / Narrative Crowding
Unsupported Crowding Claim
```

Confirmed or probable crowding should require direct evidence such as ownership concentration, fund flows, options positioning, short interest, or measurable participation.

Narrative-only evidence can support only Possible / Narrative Crowding.

## 16. Classify Neglect / Under-Ownership

Use evidence ladder:

```text
Confirmed Neglect
Probable Neglect
Possible Neglect
Unsupported Neglect Claim
```

Low attention alone is insufficient.

Neglect is investment-relevant only when low visible expectations coincide with plausible positive change, such as improving revisions, stabilizing fundamentals, new catalysts, or improving guidance.

## 17. Assign Positioning Archetypes

Assign one primary archetype and up to two secondary archetypes:

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

For each archetype include:

```text
Evidence:
Evidence strength:
Source channels:
Freshness caveats:
Decision relevance:
```

## 18. Determine Decision Relevance

Classify:

```text
High
Medium
Low
```

Decision relevance is high when positioning could materially affect:

- timing;
- risk/reward asymmetry;
- event risk;
- valuation tolerance;
- Risk / Red Team failure paths;
- IC confidence;
- ability to issue a Complete Final Memo.

Positioning is not automatically decision-relevant just because data exists.

## 19. Build Positioning Verdict Box

Required fields:

```text
Market Belief:
Expectation Bar:
Revision Direction:
Positioning Skew:
Crowding / Neglect Signal:
Primary Positioning Archetype:
Decision Relevance:
Confidence:
Output Status:
Key Limitation:
```

The verdict must describe market setup, not action.

## 20. Prepare Risk / Red Team Handoff

Create:

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

Focus on mechanisms, not labels.

## 21. Prepare Investment Committee Handoff

Create:

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

Do not issue final action.

## 22. Handle “Priced In?” Questions

If asked whether something is priced in, answer only in terms of visible expectations and positioning.

Allowed:

```text
The narrative appears well recognized.
Consensus revisions already reflect much of the improvement.
The expectation bar appears high.
```

Required caveat:

```text
Whether the current price fully discounts the narrative belongs to Valuation & Expectations and Investment Committee synthesis.
```

Prohibited:

```text
It is fully priced in.
The stock is overvalued.
The stock is undervalued.
```

## 23. Assign Output Status

Assign:

```text
Complete Market Positioning
Limited Market Positioning
Blocked Market Positioning
```

Also assign channel-level status:

```text
Complete
Limited
Missing
Not Material
```

The status must be based on materiality to the question, not on whether every possible channel is available.

## 24. Write the Report

Use the structure defined in `market-positioning-framework.md`.

Main report should be concise and decision-relevant.

Appendix should contain:

- detailed channel evidence;
- source table;
- freshness notes;
- missing data;
- proxy evidence;
- contradictions;
- claim-strength limitations.

## 25. Pre-Final Evidence Check

Before finalizing, verify:

```text
No unsupported crowding claim.
No unsupported neglect claim.
No final buy / sell / hold / avoid action.
No valuation attractiveness conclusion.
No target price.
No position sizing.
No technical trading signal.
No stale data used as current.
No narrative claim unsupported by source.
No options activity treated as direct sentiment.
All material evidence is sourced and dated.
All material limitations are disclosed.
Handoffs are structured.
Output status is justified.
```

## Style Anti-Generic Rule

Do not write generic market-sentiment commentary.

Bad:

```text
Sentiment is positive and the market likes the stock.
```

Better:

```text
Visible expectations appear favorable: consensus revisions have been positive over the last revision window, sell-side rating skew is constructive, and the stock has outperformed peers into the upcoming catalyst. However, options evidence is ambiguous and fund-flow data is unavailable, so crowding is not confirmed.
```

## Final Standard

A completed Market Positioning output should allow a downstream analyst to understand:

```text
what the market appears to believe;
which evidence supports that view;
how investors appear positioned;
whether expectations are high, low, mixed, or unclear;
whether crowding or neglect is confirmed, probable, possible, or unsupported;
what contradictions matter;
what Risk / Red Team should challenge;
what Investment Committee should incorporate;
what cannot be concluded.
```
