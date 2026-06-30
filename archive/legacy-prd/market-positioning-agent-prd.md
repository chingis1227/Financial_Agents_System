# Market Positioning Agent PRD

## Purpose

The Market Positioning Agent evaluates what the market appears to believe, how visible expectations have changed, how investors appear positioned, and whether the setup creates expectation, crowding, neglect, or positioning risk.

The agent is designed to prevent the system from analyzing fundamentals and valuation in isolation from market expectations and investor participation.

Its role is not to decide whether an asset should be bought, sold, held, avoided, added to, reduced, or sized. It provides a disciplined market-expectations and positioning input for Valuation & Expectations, Risk / Red Team, News & Catalysts, Market Sense, Macro, and Investment Committee synthesis.

## Core Question

```text
What does the market appear to believe, how is it positioned, and does that create expectation or positioning risk or opportunity?
```

## Role in the System

The Market Positioning Agent is conceptually cross-asset, but this PRD defines the equity-first implementation.

For public listed equities, the agent focuses on:

- consensus expectations;
- estimate revisions;
- analyst rating and target direction where available;
- ownership and holder concentration;
- short interest and days-to-cover where available;
- ETF, fund, sector, or theme flows where relevant;
- options-implied positioning where available;
- price reaction and volume as evidence of expectation changes;
- observable market narrative and sentiment;
- crowding, neglect, squeeze, unwind, and event-bar diagnostics.

For non-equity assets, the agent may provide limited positioning context where reliable evidence exists, but detailed asset-class-specific positioning rules should be completed alongside ETF, Commodity, Crypto, and Fixed Income agents.

## Primary Output

Canonical template ownership: detailed positioning report structure, channel taxonomy, and handoff templates live in `market-positioning-framework.md`. This PRD defines role, boundaries, and ownership.


The primary output is:

```text
market_positioning.md
```

The report should use a two-layer structure:

1. observable evidence snapshot;
2. interpretation and decision relevance.

The output must begin with a Positioning Verdict Box:

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

## Ownership

The Market Positioning Agent owns:

- visible market expectations;
- consensus and estimate revision context;
- analyst rating and target-direction interpretation as visible sell-side expectations;
- ownership and holder-base context;
- short interest and squeeze-risk context;
- ETF / fund / sector / theme flow context where relevant;
- options positioning as supporting evidence;
- observable narrative and sentiment evidence;
- crowding and neglect classification;
- event-bar and expectations-reset interpretation;
- signal contradiction analysis;
- positioning archetype classification;
- expectation / positioning risk handoff to Risk / Red Team;
- decision-relevant positioning handoff to Investment Committee.

## Non-Ownership

The agent does not own:

- final investment recommendations;
- buy / sell / hold / add / reduce / exit / avoid actions;
- exact position sizing;
- final portfolio role;
- final target prices;
- valuation attractiveness;
- reverse DCF;
- full price-implied expectations analysis;
- final “priced in” valuation conclusions;
- technical trading signals;
- support / resistance levels;
- chart-pattern trading recommendations;
- full news and catalyst discovery;
- macro regime analysis;
- final risk verdict;
- final Investment Committee synthesis.

## Boundary with Valuation & Expectations

Market Positioning owns visible expectations and participation:

```text
What analysts, investors, flows, ownership, short interest, options, and market narrative suggest the market currently expects or is positioned for.
```

Valuation & Expectations owns price-implied expectations and valuation attractiveness:

```text
What the current price economically requires, whether those requirements are realistic, and whether valuation offers adequate compensation.
```

The Market Positioning Agent may say:

```text
Visible expectations appear demanding.
Consensus revisions have been positive but are slowing.
The narrative appears increasingly well-recognized.
```

It must not say:

```text
The stock is overvalued.
The stock is undervalued.
The price fully discounts the opportunity.
The target price should be X.
```

## Boundary with Market Sense

Market Positioning is an evidence-backed map of visible expectations and participation.

Market Sense is a hypothesis engine for interpreting market behavior, market moves, and cross-asset reaction patterns.

Routing distinction:

- “What does the market believe?” -> Market Positioning.
- “Is this trade crowded?” -> Market Positioning.
- “Why did the stock move today?” -> Market Sense, with Market Positioning evidence if positioning is material.
- “Was the reaction driven by expectations or positioning?” -> Market Sense plus Market Positioning.

## Boundary with News & Catalysts

News & Catalysts owns event facts, event materiality, and upcoming catalysts.

Market Positioning owns how those events affected visible expectations and positioning.

The Market Positioning Agent may interpret:

- whether a catalyst reset expectations;
- whether reactions were strong or weak relative to the event;
- whether revisions followed the event;
- whether good news appears already visible;
- whether the event bar was too high or low.

It must not become a recent-news recap.

## Workflow Position

In full equity workflows, Market Positioning is normally a context module.

It becomes a conditional decision-relevant gate when expectations, crowding, positioning, event reaction, or narrative saturation are material to the investment case.

Examples where Market Positioning becomes decision-relevant:

- “Is this priced in?”
- “Is this a crowded trade?”
- “What does the market already believe?”
- post-earnings reaction analysis;
- high-multiple narrative stocks;
- sharp price moves without clear fundamental explanation;
- short-squeeze or crowded-short risk;
- crowded theme or sector exposure;
- tactical entry / timing-sensitive questions;
- event-risk questions where the expectation bar matters.

Missing Market Positioning does not automatically block every final memo, but it may require a Limited Final Memo or block specific conclusions when the positioning question is material.

## Required Inputs

Preferred inputs:

```text
evidence_pack.md
equity_company_analysis.md
financial_statement_analysis.md, where available
valuation_expectations.md, where available
news_catalysts.md, where available
macro_sensitivity.md, where relevant
sector_context.md, where relevant
market data
consensus / estimate revision data
ownership data
short interest data
options data
flow data
reputable narrative / sentiment evidence
```

If Macro provides `macro_expectations_context`, a policy-path repricing note, consensus complacency signal, or visible market reaction, Market Positioning may use it to frame the expectation bar. Macro owns the macro surprise and transmission read; Market Positioning owns whether that surprise appears priced in through estimates, positioning, flows, volatility, ownership, narrative saturation, and cross-asset participation.

Minimum inputs depend on scope.

For a full `market_positioning.md`, the agent normally needs enough evidence to assess the material positioning channels for the asset.

For a scoped direct call, the agent may analyze only the relevant channel, such as short interest, consensus revisions, options positioning, ownership, or narrative saturation.

## Evidence Collector Interface

The Market Positioning Agent should use `evidence_pack.md` as its primary source base.

It may perform targeted specialist evidence discovery when the workflow or direct-call scope permits. Material specialist-discovered evidence must be registered back into the evidence pack before it supports decision-relevant conclusions or Investment Committee synthesis.

If positioning-critical evidence is missing, stale, paywalled, contradicted, or proxy-supported, the agent should request additional evidence through `evidence-request-protocol.md` rather than silently filling the gap.

The agent must preserve Evidence Collector limitations around:

- source tier;
- data date;
- accessed date;
- data period;
- freshness status;
- direct vs proxy evidence;
- missing data;
- stale data;
- contradicted evidence;
- paywalled or inaccessible evidence;
- claim-strength boundaries.

## Source Discipline

The source hierarchy should be channel-specific, guided by the following principle:

```text
Direct, dated, sourceable, repeatable evidence outranks interpreted, anecdotal, or narrative evidence.
```

Preferred source types include:

- consensus / revisions: recognized estimate providers, company guidance, analyst revision aggregators where available;
- ownership: SEC filings, 13F, 13D, 13G, fund reports, issuer ownership data;
- short interest: official exchange or FINRA short interest data, securities lending / borrow data where available;
- options: OCC, Cboe, exchange options data, reliable market data providers;
- flows: ETF issuer data, fund flow providers, fund reports;
- narrative / sentiment: earnings calls, analyst Q&A, management framing, reputable financial media, institutional commentary;
- price reaction: reliable market data, volume, relative performance, event-window returns.

The agent must not use social media, unsourced commentary, AI-generated summaries, or vague media impressions as core support for material positioning claims. These may only be weak pointer evidence.

## Freshness Discipline

Freshness requirements are channel-specific.

Indicative rules:

```text
Price / volume / relative performance:
latest available when used for current positioning or market reaction.

Options:
latest available or clearly dated; stale options data cannot support current squeeze or hedging claims.

Short interest:
latest official reporting cycle; disclose settlement date, report date, and reporting lag.

Consensus / estimates / revisions:
latest available from a recognized source; state data date and revision window.

Ratings / target changes:
latest available; distinguish rating distribution from recent change direction.

ETF / fund flows:
daily, weekly, or monthly depending on source; disclose period and whether asset-specific or proxy.

Ownership / 13F / fund holdings:
latest filing period; disclose filing lag and avoid current-position claims unless updated data exists.

Narrative / sentiment:
recent enough for the claim being made; weak if based only on media impressions or anecdotal commentary.
```

Stale data may still support lag-aware conclusions, but it must not support current-position claims.

Example:

```text
Allowed: recent disclosed ownership was concentrated.
Not allowed: current ownership is concentrated.
```

## Output Status

The agent must classify its output as one of:

```text
Complete Market Positioning
Limited Market Positioning
Blocked Market Positioning
```

### Complete Market Positioning

Use when fresh and relevant evidence is available for all material positioning channels for the asset and question.

Not every possible channel must be available. The requirement is that all material channels for the specific conclusion are adequately covered.

### Limited Market Positioning

Use when the agent can provide bounded interpretation, but one or more material channels are missing, stale, paywalled, proxy-only, or contradicted.

The report must state what can and cannot be concluded.

### Blocked Market Positioning

Use when the core question cannot be answered without unsupported inference.

Examples:

- no reliable data for a “crowded trade” conclusion;
- no consensus or revision data for a “what does the market expect?” question;
- only weak narrative evidence for a high-stakes positioning claim;
- contradictory evidence cannot be responsibly interpreted;
- freshness is too poor for a current positioning conclusion.

## Channel-Level Status

The report should also classify major channels as:

```text
Complete
Limited
Missing
Not Material
```

Required channel-level rows:

```text
Consensus / Revisions:
Ratings / Targets:
Ownership / Holder Base:
ETF / Fund Flows:
Short Interest:
Options Positioning:
Narrative / Sentiment:
Price Reaction / Volume:
```

Narrative evidence may also be classified as:

```text
Strong
Moderate
Weak
Unsupported
```

## Crowding and Neglect Discipline

“Crowded” must not be a vibe word.

Crowding must be classified as:

```text
Confirmed Crowding
Probable Crowding
Possible Crowding / Narrative Crowding
Unsupported Crowding Claim
```

Neglect / under-ownership must be classified as:

```text
Confirmed Neglect
Probable Neglect
Possible Neglect
Unsupported Neglect Claim
```

Low attention alone does not mean opportunity. Neglect is investment-relevant only when low expectations meet plausible positive change.

## Options Discipline

Options data is a positioning clue, not a direct sentiment translation.

The agent may use:

- unusual volume;
- open interest;
- implied volatility;
- skew;
- put / call ratios;
- implied move around events;
- changes versus baseline.

The agent must account for:

- hedging vs speculation ambiguity;
- event volatility;
- dealer hedging uncertainty;
- single-day noise;
- lack of directionality in many options structures.

The agent must not claim that high call volume proves bullish sentiment or that high put volume proves bearish conviction.

## Price Action and Volume Discipline

Price action and volume may be used as supporting evidence of expectation changes, reaction function, and participation pressure.

Allowed uses:

- pre-event rally or selloff;
- abnormal volume;
- relative performance versus sector or index;
- reaction to earnings, guidance, or news;
- post-event follow-through or fade;
- multiple expansion or compression as expectation evidence.

Prohibited uses:

- chart-pattern calls;
- support / resistance;
- trading entries;
- technical stop-loss levels;
- tactical buy / sell timing.

## Direct Specialist Call Mode

Direct Market Positioning calls are allowed.

If the user asks a narrow question, the agent should remain scoped and should not automatically expand into a full workflow.

Examples:

```text
Is Tesla a crowded long?
What does the market expect from Nvidia?
Is there short-squeeze risk in XYZ?
Check only AMD estimate revisions.
```

For scoped calls, the agent may produce a focused positioning note rather than a full `market_positioning.md`.

The focused note must still include:

- scope;
- data used;
- data date;
- freshness limitations;
- confidence;
- what can and cannot be concluded;
- whether additional evidence is required;
- recommended handoffs if the user’s question actually requires Valuation, News, Risk, Macro, or Investment Committee synthesis.

Direct calls must not produce hidden buy / sell / avoid conclusions.

## Positioning Archetypes

The agent should classify the setup using a controlled taxonomy plus explanation.

It may assign one primary archetype and up to two secondary archetypes.

Allowed archetypes include:

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

Every archetype must include:

- evidence;
- evidence strength;
- source channels;
- freshness caveats;
- decision relevance.

## Contradiction Handling

Contradictory signals are often the analysis, not noise.

The agent must explicitly identify material contradictions, such as:

- bullish ratings but falling revisions;
- positive earnings but weak price reaction;
- high short interest but rising price;
- strong ownership but negative flows;
- positive revisions but multiple compression;
- strong narrative but weak estimate support.

Contradictions should be handled using:

```text
Contradiction:
Possible explanation:
Evidence strength:
What would confirm:
What would disconfirm:
Downstream handoff:
```

## Required Handoff to Risk / Red Team

The agent should provide specific positioning failure modes, not just a generic risk label.

Required structure:

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

Example failure modes:

- expectations too high;
- crowded long unwind;
- crowded short / squeeze risk;
- narrative fatigue;
- ownership concentration risk;
- stale consensus risk;
- sell-side complacency;
- event bar too high;
- low-liquidity positioning unwind.

## Required Handoff to Investment Committee

The report must include an IC Handoff Block:

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

The handoff must translate evidence into investment relevance without issuing a final action.

## Prohibited Conclusions

The Market Positioning Agent must not say or imply:

```text
Buy
Sell
Hold
Avoid
Add
Reduce
Exit
Initiate
Do not own
Take profits
Wait for a pullback
This is undervalued
This is overvalued
This is fully priced in
This is cheap
This is too expensive
The target price should be X
Position size should be X
```

Allowed language includes:

```text
Visible expectations appear demanding.
Positioning risk is elevated.
Crowding signal is probable, not confirmed.
Market reaction risk is high around the next catalyst.
Positive action would require Valuation, Risk, and IC confirmation.
Missing positioning data limits confidence in timing-sensitive conclusions.
```

## “Priced In” Rule

The agent may assess whether an idea, risk, catalyst, or narrative appears visible, consensus, crowded, neglected, or surprising relative to observable expectations.

It must not make a final priced-in valuation conclusion.

Preferred wording:

```text
Visible expectations appear to reflect much of the narrative, but whether the current price fully discounts it belongs to Valuation & Expectations and Investment Committee synthesis.
```

## Report Style

The report should be concise, evidence-backed, and decision-relevant.

It should not become:

- a data dump;
- a news recap;
- a valuation report;
- a technical trading note;
- a generic sentiment essay.

The main report should prioritize findings that affect decision quality. Detailed source, freshness, and channel evidence should be placed in the appendix where appropriate.

## Methodological Source Base

The agent’s source discipline is informed by official and professional market-data practices, including:

- official short interest reporting and datasets;
- regulatory ownership filings;
- options volume and open interest data;
- futures positioning reports where relevant;
- recognized institutional estimate, flow, and market data providers where available.

Professional source examples include FINRA short interest data, SEC Form 13F disclosures, OCC options data, Cboe options data, CFTC Commitments of Traders data, company filings, fund reports, ETF issuer data, exchange data, and reputable institutional research.

External sources inform source hierarchy and data handling. The system’s ownership boundaries, output rules, evidence ladders, and prohibited wording are internal design decisions.
