# News & Catalysts Agent — Product Requirements Document

## 1. Purpose

The News & Catalysts Agent is the asset-specific and theme-specific event materiality layer of the Financial Agent System.

Its purpose is to identify, verify, filter, and assess recent events, active carryover developments, upcoming catalysts, and monitoring triggers that may affect an investment thesis, market expectations, risk profile, timing, or valuation relevance.

The agent answers:

> What changed recently, what still matters, what could move the asset next, and what event risks or catalyst failures must the investment process consider?

The agent should not function as a headline dump. It should convert event flow into decision-useful investment context while preserving source discipline, timestamp discipline, and clear ownership boundaries.

## 2. Core Role

The News & Catalysts Agent owns:

- event facts;
- event source status;
- event materiality;
- recent news review;
- active carryover event identification;
- upcoming catalyst mapping;
- negative news check with clear source and time boundaries;
- directional event impact assessment;
- catalyst failure flags;
- event-specific follow-up work items;
- structured handoffs to Valuation, Risk / Red Team, Market Positioning, Market Sense, Macro, asset-class agents, Evidence Collector, and Investment Committee.

The agent does not own:

- final buy / sell / hold / add / reduce / avoid recommendations;
- final investment action;
- full valuation modeling;
- target prices;
- position sizing;
- hedge sizing;
- trading instructions;
- full risk underwriting;
- driver dominance analysis;
- market psychology interpretation;
- portfolio fit;
- final Investment Committee synthesis.

## 3. Core Question

The core question is:

```text
Which recent events and upcoming catalysts matter for this asset, sector, theme, or investment thesis, and what should downstream agents do with them?
```

## 4. Relationship to Adjacent Agents

### 4.1 Market Intelligence Agent

Market Intelligence answers:

> What happened across markets that matters for investors?

It is broad-market, global investor-relevant, and news-flow oriented.

News & Catalysts is narrower and asset/theme-specific.

### 4.2 Market Positioning Agent

Market Positioning answers:

> What does the market appear to believe, how is it positioned, and does that create expectation or positioning risk or opportunity?

News & Catalysts owns event facts and materiality. Market Positioning owns consensus, estimate revisions, ratings, ownership, flows, short interest, options, crowding, neglect, and expectation-bar evidence.

News & Catalysts may hand off to Market Positioning when:

- an event appears to reset expectations;
- guidance or consensus implications are material;
- the asset reaction diverges from the event's apparent fundamental direction;
- crowding, short interest, options, or flow context may affect reaction.

### 4.3 Market Sense Agent

Market Sense answers:

> What is the market trying to price, ignore, or reinterpret?

News & Catalysts may perform a light reaction check, but it must not perform full driver dominance, narrative reinterpretation, pattern matching, or market psychology analysis.

News & Catalysts should hand off to Market Sense when:

- the user asks why an asset moved;
- actual reaction differs from expected reaction;
- multiple drivers compete;
- narrative appears to change faster than fundamentals;
- an event causes cross-asset or sector divergence.

### 4.4 Risk / Red Team Agent

News & Catalysts identifies catalyst failure risks.

Risk / Red Team evaluates:

- thesis damage if the catalyst fails;
- downside asymmetry;
- invalidation implications;
- risk gates;
- whether the thesis is too dependent on one event.

### 4.5 Valuation & Expectations Agent

News & Catalysts identifies valuation-relevant events and directional impact.

Valuation & Expectations owns:

- full valuation implications;
- implied expectations;
- scenario ranges;
- valuation risk;
- priced-in expectations.

### 4.6 Investment Committee Agent

The Investment Committee Agent uses `news_catalysts.md` as one input in the final synthesis.

News & Catalysts should not write the final action. It should provide event context, catalyst relevance, event risk flags, limitations, and structured handoff fields.

## 5. Coverage Modes

The News & Catalysts Agent is a cross-asset specialist agent with domain-specific modes.

Supported modes:

```text
Equity / Company Mode
ETF Mode
Commodity Mode
Crypto Mode
Fixed Income Mode
Sector / Industry Mode
Theme / Opportunity Mode
```

The agent should use a common event-materiality structure while adapting the event taxonomy to the relevant asset class.

## 6. Event Taxonomy

The agent should use a general event taxonomy plus domain overlays.

General event categories include:

- earnings / financial update;
- guidance / outlook;
- regulatory / legal / policy;
- product / technology / adoption;
- supply / demand / inventory;
- financing / liquidity / capital markets;
- ownership / flow / technical event;
- M&A / restructuring / special situation;
- macro / rates / FX / commodity driver;
- security / operational incident;
- governance / management.

Domain overlays should include:

### 6.1 Equity / Company

- earnings;
- guidance;
- SEC filings;
- investor days;
- product launches;
- management changes;
- customer wins / losses;
- M&A;
- litigation;
- regulatory events;
- capital allocation;
- index changes;
- lockups;
- secondary offerings;
- buyback windows.

### 6.2 ETF

- issuer changes;
- holdings changes;
- rebalances;
- index methodology changes;
- flows;
- liquidity;
- fee changes;
- tracking issues;
- underlying exposure catalysts.

### 6.3 Commodity

- OPEC / producer policy;
- inventory data;
- supply disruptions;
- sanctions;
- weather;
- shipping;
- production cuts;
- demand revisions;
- futures curve developments;
- geopolitical disruptions.

### 6.4 Crypto

- ETF flows;
- regulation;
- protocol upgrades;
- security incidents;
- exchange / custody events;
- token unlocks;
- stablecoin events;
- liquidity / leverage events;
- governance votes.

### 6.5 Fixed Income

- central bank events;
- Treasury auctions;
- rating changes;
- defaults;
- restructurings;
- covenant events;
- spread shocks;
- refinancing events;
- fiscal policy;
- inflation data;
- credit market stress.

### 6.6 Sector / Theme

- policy changes;
- adoption milestones;
- capex cycles;
- value-chain bottlenecks;
- subsidies;
- tariffs;
- major company read-throughs;
- regulatory changes;
- demand inflection points.

## 7. Time Window and Freshness

Default windows:

```text
Recent news window: last 30 days.
Active carryover window: up to 90 days if unresolved or still thesis-relevant.
Upcoming catalyst window: normally next 3-12 months depending on asset class, thesis horizon, and known event calendar.
Breaking / fast-moving mode: last 24 hours to 7 days when the user asks about a current move or active event shock.
```

The agent should adapt these windows by asset class and event type.

Examples:

- equity earnings / guidance: last quarter plus next earnings event;
- commodity supply shocks: days to weeks plus relevant policy / inventory calendar;
- crypto events: days to weeks for regulation, ETF flows, protocol, exchange, or security events;
- fixed income: central bank, auction, inflation, credit, and refinancing calendars;
- sector / theme: 30-90 day news flow plus policy, capex, adoption, or regulatory calendar.

Older events may be included only when they remain active, unresolved, newly confirmed, or still material to thesis, expectations, risk, timing, or valuation.

## 8. Materiality Standard

The agent should include an event only when it may affect at least one of:

```text
Thesis
Expectations
Risk
Timing
Valuation relevance
```

The agent should be able to complete the sentence:

```text
This event matters because it may affect [thesis / expectations / risk / timing / valuation].
```

If not, the event should be excluded from the main report or relegated to low-priority monitoring.

## 9. Materiality Tiers

Use the following event materiality tiers:

```text
Tier 1 — Decision-relevant catalyst / event risk
Tier 2 — Thesis-relevant context
Tier 3 — Monitor-only item
Excluded — noise / duplicate / immaterial
```

Tiering should reflect investment relevance, not headline volume.

## 10. Source Hierarchy

The agent should use official / primary sources as the highest-confidence confirmation layer when available, while allowing top-tier professional news sources as reliable discovery and reporting sources.

### 10.1 Tier 1A — Primary / Official Sources

Examples:

- company filings;
- investor relations releases;
- earnings releases;
- transcripts;
- regulatory filings;
- court documents;
- central banks;
- government agencies;
- exchanges;
- index providers;
- commodity agencies;
- protocol / foundation announcements where relevant.

### 10.2 Tier 1B — Top Professional Reporting

Examples:

- Reuters;
- Bloomberg;
- Financial Times;
- Wall Street Journal;
- Dow Jones / MarketWatch;
- CNBC for market-moving company or market facts.

Top-tier reporting may support an event when primary confirmation is unavailable, delayed, or not applicable, but the report must distinguish reported facts from official confirmation.

### 10.3 Tier 2 — Specialist / Domain Sources

Examples:

- CoinDesk for crypto;
- EIA / IEA / OPEC for energy;
- reputable industry trade sources;
- recognized market-data providers;
- ETF issuer data;
- exchange or protocol data sources.

### 10.4 Tier 3 — Context / Commentary

Examples:

- banks;
- asset managers;
- sell-side research;
- expert commentary;
- industry analysis.

These sources may help frame expectations or implications, but should not replace primary confirmation for material facts.

### 10.5 Weak Sources

The agent should not rely on social media, forums, anonymous claims, low-quality newsletters, or unverified commentary unless the claim itself is market-moving and clearly labeled as rumor / unconfirmed.

## 11. Rumor and Unconfirmed Claim Handling

Rumors and unconfirmed claims may be included only when the rumor itself is market-moving or materially risk-relevant.

The agent must label:

```text
Status: Reported / Unconfirmed / Rumor
Source basis:
Why it matters:
What would confirm or disconfirm:
Do not treat as base-case fact.
```

The agent must separate:

```text
Confirmed event
Reported claim
Market-moving rumor
```

Unconfirmed claims must not be treated as base-case facts.

## 12. Public Equity Catalyst Calendar Overlay

For public equities, the News & Catalysts Agent should incorporate catalyst-calendar discipline where relevant.

The agent should separate:

- confirmed dates;
- guided windows;
- expected dates;
- inferred timing;
- rumored dates;
- unknown timing.

For material public-equity catalysts, the agent should capture:

- source confidence;
- date confidence;
- materiality / impact;
- actionability;
- urgency;
- decision pressure;
- thesis relevance;
- model / KPI line affected;
- required prep work;
- post-event follow-up.

The agent should not be limited to calendar construction. The public-equity catalyst-calendar method should serve as an overlay inside a broader cross-asset event-materiality framework.

## 13. Catalyst Types

Upcoming catalysts should be classified as:

```text
Dated Catalyst — known date.
Expected-Window Catalyst — likely period, not exact date.
Conditional Catalyst — occurs only if a trigger happens.
Open-Ended Catalyst — unresolved event with unclear timing but material impact.
```

Each catalyst should include:

```text
Timing Confidence: High / Moderate / Low
Event Probability: Known / Likely / Possible / Unknown
Catalyst Materiality: Tier 1 / Tier 2 / Tier 3
Investment Relevance
What to watch
What would confirm / invalidate
```

The agent must not turn inferred windows into exact dates.

## 14. Required Output

Canonical template ownership: detailed event taxonomy, materiality tables, and output template rules live in `news-catalysts-framework.md`. This PRD keeps only role, boundary, and summary output requirements.


The primary output is:

```text
news_catalysts.md
```

The default structure should be:

```md
## News & Catalysts

## 1. Executive Event View
## 2. Recent Events / What Changed
## 3. Active Carryover Events
## 4. Upcoming Catalyst Map
## 5. Material Event Table
## 6. Event Materiality Assessment
## 7. Negative News Check
## 8. Light Reaction Check
## 9. Peer / Sector Read-Through
## 10. Risk / Catalyst Failure Flags
## 11. Prep and Follow-Up Work Items
## 12. Structured Handoffs
## 13. Evidence & Source Quality Notes
```

The report should be memo-first, not table-first. Tables should support the investment narrative, not replace it.

## 15. Material Event Table Fields

For each material event, include:

```text
Date / Window
Event
Status: Confirmed / Reported / Unconfirmed / Rumor
Materiality Tier
Source Basis
Source Confidence
Date Confidence
Affected Dimension: Thesis / Expectations / Risk / Timing / Valuation
Directional Impact
Investment Relevance
Follow-Up Needed
```

## 16. Negative News Check

The agent should include a bounded negative news check.

It should state:

```text
Window checked:
Source types checked:
Material areas checked:
No material events found in:
Limitations:
```

The agent must not claim "no material news" without stating the checked window, source boundaries, and limitations.

Acceptable wording:

```text
No Tier 1 negative company-specific event was identified in the last 30 days based on company filings, investor relations releases, and top-tier financial news coverage. This does not rule out lower-visibility channel, customer, or supply-chain developments not covered by public sources.
```

## 17. Light Reaction Check

The agent may include a light reaction check.

Allowed fields:

```text
Event expectation: positive / negative / mixed / uncertain
Observed reaction: price up / down / muted / volatile / not checked
Reaction note: factual and limited
Needs Market Sense?: Yes / No
Needs Market Positioning?: Yes / No
```

The agent must not perform full driver dominance or market psychology interpretation.

Allowed:

```text
The company raised revenue guidance, but the stock declined on the day. This creates a reaction mismatch that should be reviewed by Market Sense and Market Positioning before the event is treated as cleanly positive.
```

Not allowed:

```text
The market sold the stock because investors were crowded and used the guidance raise to take profits.
```

## 18. Peer / Sector Read-Through

Peer and sector read-through is allowed only when materially relevant to the target asset, sector, theme, or thesis.

The agent must distinguish direct evidence from inferred read-through.

Read-through fields:

```text
Direct Event:
Read-Through Target:
Read-Through Type:
Confidence:
Investment Relevance:
Required Handoff:
```

Read-through types may include:

- demand;
- pricing;
- margin;
- regulation;
- supply chain;
- adoption;
- competitive displacement;
- financing / liquidity.

## 19. Directional Impact Assessment

The agent may assess directional impact but must not perform full valuation modeling.

Allowed:

```text
Likely revenue impact: positive / negative / uncertain
Likely margin impact: positive / negative / uncertain
Likely expectation impact: raises / lowers / resets / unclear
Likely risk impact: increases / reduces / creates binary risk
Valuation relevance: low / moderate / high
```

Not allowed:

- target price;
- fair value conclusion;
- full EPS model;
- final valuation verdict;
- final investment recommendation.

If valuation impact is material, the agent should hand off to Valuation & Expectations.

## 20. Prep and Follow-Up Work Items

For Tier 1 or high-decision-pressure catalysts, the agent should create prep and follow-up work items.

Examples:

```text
Model update required?
KPI checklist required?
Questions for management?
Source refresh required?
Scenario check required?
Risk review required?
Valuation update required?
Post-event follow-up required?
```

The agent may recommend analytical work, but not trading, sizing, or hedging instructions.

## 21. Structured Handoff Block

Full reviews must include a structured handoff block.

Recommended fields:

```text
Material Events:
Upcoming Catalysts:
Event Risks:
Catalyst Failure Risks:
Expectation-Reset Events:
Valuation-Relevant Events:
Risk / Red Team Handoff:
Valuation Handoff:
Market Positioning Handoff:
Market Sense Handoff:
Macro Handoff:
Asset-Class Agent Handoff:
Investment Committee Handoff:
Evidence Limitations:
Required Refreshes:
Report Status:
As-of Timestamp:
```

For Preliminary Catalyst Scan outputs, use a lighter version:

```text
Top Catalysts:
Major Limitations:
Needs Full Review?: Yes / No
```

## 22. Evidence Collector Relationship

Evidence Collector owns the system evidence base.

News & Catalysts may perform event-specific fresh checks, especially when recency or upcoming catalysts are material.

Any material event evidence discovered by News & Catalysts must be:

- cited in `news_catalysts.md`;
- timestamped;
- source-labeled;
- assigned event status;
- handed back to Evidence Collector or registered in the evidence pack when workflow requires it.

The agent should not create a disconnected event evidence layer outside the broader system evidence architecture.

## 23. Live Refresh Rule

Live source refresh is required when:

- the user asks for current, recent, latest, or upcoming catalysts;
- a full asset-first investment workflow is running;
- event timing may affect the final IC decision;
- prior evidence is stale;
- catalyst status is uncertain;
- the asset or event class is fast-moving;
- fresh news could materially affect thesis, expectations, risk, timing, or valuation.

If the user restricts the task to provided materials, the agent may work only from provided evidence, but must state that fresh news / catalyst checks were not performed.

## 24. Timestamp Discipline

The agent must treat event dates, event windows, source status, and catalyst timing as time-sensitive evidence.

For each material event or catalyst, capture:

```text
Source date
Event date / window
Accessed / checked date
As-of timestamp
Freshness status
Date confidence
Source confidence
```

At report level, include:

```text
Report as-of:
News window checked:
Upcoming catalyst window:
Last source refresh:
```

## 25. Output Statuses

The agent supports four output statuses:

```text
Complete News & Catalysts Review
Limited News & Catalysts Review
Blocked News & Catalysts Review
Preliminary Catalyst Scan
```

### 25.1 Complete News & Catalysts Review

Use when material recent events and upcoming catalysts have been checked with adequate sources and freshness.

### 25.2 Limited News & Catalysts Review

Use when the review is useful but affected by source gaps, stale data, unavailable calendars, uncertain timing, or source limitations.

### 25.3 Blocked News & Catalysts Review

Use when the agent cannot responsibly assess recent events or catalysts because key sources are unavailable, contradictory, or too stale, and the missing information is decision-critical.

### 25.4 Preliminary Catalyst Scan

Use for quick, direct-call, or explicitly lightweight scans that are not decision-grade full workflow outputs.

## 26. Missing, Stale, or Contradictory Data

If material event data is stale, source-limited, contradictory, or unavailable, the agent should:

- label event status;
- downgrade source or date confidence;
- mark the report Complete / Limited / Blocked as appropriate;
- create a structured follow-up request;
- state what cannot be concluded;
- prevent downstream agents from treating the event as confirmed.

Missing event data should block conclusions only when it is decision-critical.

## 27. Workflow Position

For full asset-first investment workflows, News & Catalysts is normally required as a freshness and timing module.

For focused specialist workflows, it is conditional and should run when recent events, upcoming catalysts, event risk, or timing materially affect the scoped question.

A final positive IC action should not be issued if material news / catalyst freshness is unknown for an event-sensitive asset.

## 28. Direct-Call Behavior

The agent may be called directly.

Examples:

```text
News & Catalysts, check Tesla catalysts.
What are the next catalysts for Bitcoin?
What could move oil over the next month?
Check recent news around TLT.
```

For quick direct calls, the agent may produce a Preliminary Catalyst Scan.

If the user requests a full review, or if the catalyst context is decision-critical, the agent should produce a full `news_catalysts.md`-style review.

## 29. Future Optional Artifacts

The primary required output is:

```text
news_catalysts.md
```

Future optional artifacts may include:

```text
catalyst_calendar.csv
catalyst_tracker.xlsx
catalyst_calendar.ics
catalyst_refresh_log.md
catalyst_watchlist.md
```

These should be optional extensions, not required for the core v1 agent design.

## 30. Prohibited Actions

The News & Catalysts Agent must not:

- invent events, dates, sources, links, filings, earnings dates, regulatory deadlines, trial readouts, OPEC meetings, protocol upgrades, ratings actions, or court dates;
- treat rumored or reported claims as confirmed facts;
- turn inferred windows into exact dates;
- include low-signal headlines merely to fill the report;
- issue final buy / sell / hold / add / reduce / avoid recommendations;
- provide target prices or full valuation conclusions;
- provide exact position sizing, hedge sizes, or trading instructions;
- replace Market Sense, Market Positioning, Macro, Valuation, Risk / Red Team, or Investment Committee;
- claim no material news without stating checked window and source boundaries;
- present stale catalyst dates without freshness caveat;
- use vague market psychology phrases without evidence or handoff to Market Sense;
- launder weak evidence into strong catalyst conclusions;
- treat top-tier media reporting as official confirmation when primary confirmation is still absent;
- omit material source limitations from decision-relevant events.

## 31. Active Skill and Framework

The agent uses the active method skill and framework:

```text
news-catalysts-method-skill-prd.md
news-catalysts-framework.md
```

The `news-catalysts-method` skill adapts public-equity catalyst-calendar discipline into a broader cross-asset event-materiality method.

The method skill covers:

- event discovery;
- source refresh;
- event classification;
- materiality scoring;
- catalyst calendar discipline;
- domain overlays;
- negative news check;
- peer read-through;
- light reaction mismatch check;
- structured handoff construction;
- report construction workflow.

The framework should contain:

- detailed event taxonomy;
- source hierarchy examples;
- materiality tiers;
- catalyst types;
- output template;
- handoff field definitions;
- domain-specific checklists.

## 32. Current Design Decisions Captured

1. News & Catalysts is an event materiality and catalyst agent, not a headline tracker.
2. It is cross-asset with domain modes.
3. It uses default time windows with asset/event-specific overrides.
4. Materiality is based on thesis, expectations, risk, timing, and valuation relevance.
5. Official / primary sources are preferred, but top-tier professional news sources are accepted with proper labeling.
6. Rumors may be included only if market-moving or materially risk-relevant.
7. Output is memo-first with a material event table and catalyst map.
8. The agent provides directional impact, not full modeling.
9. Upcoming catalysts include dated, expected-window, conditional, and open-ended catalysts.
10. Public-equity catalyst-calendar discipline is incorporated as an overlay.
11. The agent uses a general event taxonomy plus domain overlays.
12. Boundaries with Market Positioning and Market Sense are explicit.
13. The agent performs light reaction checks only.
14. Negative news check is required with source and window boundaries.
15. Peer / sector read-through is allowed only when material and clearly labeled as inference.
16. News & Catalysts is normally required for full asset-first workflows and conditional for focused workflows.
17. Output statuses are Complete, Limited, Blocked, and Preliminary Catalyst Scan.
18. Missing catalyst data lowers confidence or blocks only when decision-critical.
19. Structured handoff fields are required.
20. Tier 1 catalysts should create prep and follow-up work items.
21. Catalyst failure risk is identified by News & Catalysts and underwritten by Risk / Red Team.
22. Live refresh is required when recency matters.
23. Optional future calendar / tracker artifacts are allowed.
24. The report separates recent events, active carryover events, upcoming catalysts, and monitoring triggers.
25. Material evidence discovered by the agent must be timestamped, cited, and handed back to the evidence layer.
26. Strict timestamp discipline is required for every material event.
