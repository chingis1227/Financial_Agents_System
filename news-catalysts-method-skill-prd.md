# News & Catalysts Method Skill — Product Requirements Document

## 1. Purpose

The News & Catalysts Method Skill defines the reusable method used by the News & Catalysts Agent to identify, verify, classify, prioritize, and communicate recent events, active carryover developments, upcoming catalysts, monitoring triggers, and event-related handoffs.

The skill answers:

> How should event flow be converted into decision-useful investment context without becoming a headline dump, rumor amplifier, or substitute for valuation, risk, market positioning, market sense, or final investment judgment?

This skill supports the News & Catalysts Agent defined in:

```text
news-catalysts-agent-prd.md
```

The primary output supported by this skill is:

```text
news_catalysts.md
```

## 2. Method Doctrine

The method is an evidence-first event-materiality workflow.

Core workflow logic:

```text
Source-backed event discovery
→ expected-event checklist
→ event verification
→ event classification
→ materiality and decision-pressure ranking
→ catalyst mapping
→ directional impact assessment
→ catalyst failure flagging
→ structured handoff generation
→ memo-first report construction
```

The method must not invent catalysts, events, dates, or implications. It should find what is source-backed, test for missing event categories using domain checklists, and clearly label uncertainty.

## 3. Use Cases

Use this skill for:

- full asset-first investment workflows requiring event freshness;
- focused News & Catalysts reviews;
- direct-call catalyst scans;
- recent event reviews;
- upcoming catalyst maps;
- post-event updates;
- refreshes of prior catalyst maps;
- theme / sector catalyst scans;
- ETF, commodity, crypto, fixed income, and equity event reviews.

Do not use this skill to:

- produce final investment recommendations;
- build full valuation models;
- assign target prices;
- perform full risk red-team analysis;
- explain market psychology or driver dominance;
- provide position sizing, hedge sizing, or trading instructions;
- replace Market Sense, Market Positioning, Valuation, Risk / Red Team, Macro, or Investment Committee.

## 4. Core Workflow

### Step 1 — Define Scope and Mode

Classify the request by mode:

```text
Full News & Catalysts Review
Preliminary Catalyst Scan
Post-Event Update
Refresh / Change Log Update
Single-Event Review
Sector / Theme Catalyst Review
```

Classify domain mode:

```text
Equity / Company
ETF
Commodity
Crypto
Fixed Income
Sector / Industry
Theme / Opportunity
```

Define:

```text
Target asset / sector / theme:
User decision context:
Relevant horizon:
Recent news window:
Active carryover window:
Upcoming catalyst window:
Required output depth:
Source limitations:
```

### Step 2 — Set Time Windows

Default windows:

```text
Recent news: last 30 days
Active carryover: up to 90 days if unresolved or still material
Upcoming catalysts: normally next 3-12 months
Breaking / fast-moving mode: last 24h-7d
```

Adjust by asset class and event type.

The method must state:

```text
Report as-of:
News window checked:
Upcoming catalyst window:
Last source refresh:
```

### Step 3 — Build Source Plan

Use source-backed discovery first.

Preferred source hierarchy:

```text
1. Primary / official sources
2. Top-tier professional reporting
3. Specialist / domain sources
4. Institutional commentary and research
5. User-provided assumptions or private context, clearly labeled
6. Weak / rumor sources only when the claim itself is market-moving
```

The method should use professional news sources for discovery and fast-moving confirmation, but primary / official sources remain the highest-confidence confirmation layer when available.

Every material event should capture:

```text
Source name:
Source date:
Event date / window:
Accessed / checked date:
Source confidence:
Date confidence:
Event status:
Freshness status:
```

### Step 4 — Source-Backed Event Discovery

Identify events supported by sources.

Collect:

```text
Recent events:
Active carryover events:
Upcoming catalysts:
Monitoring triggers:
Peer / sector read-through events:
Potential rumor / reported claims:
```

The method must avoid padding the review with low-signal headlines.

### Step 5 — Expected-Event Checklist

After source-backed discovery, apply the relevant domain checklist from `news-catalysts-framework.md`.

The checklist is used to ask:

```text
What material event categories should exist or be checked for this asset class?
```

Examples:

- Equity: earnings, guidance, filings, investor day, M&A, litigation, regulation, management, index changes.
- Commodity: OPEC, inventories, supply disruption, sanctions, weather, shipping, producer policy.
- Crypto: ETF flows, regulation, protocol upgrades, security incidents, token unlocks, exchange / custody events.
- Fixed income: central banks, auctions, ratings, defaults, refinancing, spreads, covenants.
- ETF: holdings, rebalance, index methodology, issuer, flows, tracking, liquidity, underlying catalysts.
- Sector / theme: policy, adoption, capex, subsidies, tariffs, value-chain bottlenecks, major read-throughs.

Checklist items must not be treated as facts unless supported by evidence. If no evidence is found, mark as:

```text
Not found within checked source boundaries
Inferred
Unconfirmed
Needs refresh
```

## 5. Event Classification

Classify each candidate event by:

```text
Event category:
Event subcategory:
Asset / issuer / theme:
Direct event or read-through:
Past / recent / active carryover / upcoming / monitoring trigger:
Status:
Date type:
Source type:
Affected dimension:
```

Status labels:

```text
Confirmed
Reported
Unconfirmed
Rumor
Inferred
Unknown
```

Date type labels:

```text
Hard date
Soft date
Date window
Quarter window
Seasonal window
Open-ended
Unknown
```

Affected dimensions:

```text
Thesis
Expectations
Risk
Timing
Valuation relevance
```

## 6. Materiality Test

An event should be included only if it can honestly complete:

```text
This event matters because it may affect [thesis / expectations / risk / timing / valuation].
```

If not, exclude it or place it in low-priority monitoring.

Materiality tiers:

```text
Tier 1 — Decision-relevant catalyst / event risk
Tier 2 — Thesis-relevant context
Tier 3 — Monitor-only item
Excluded — noise / duplicate / immaterial
```

Every visible tier must include a human explanation.

Example:

```text
Tier 1 — Decision-relevant catalyst.
Why: The upcoming earnings report may reset FY revenue guidance and margin expectations, which are central to the valuation case.
```

Do not present bare labels without practical meaning.

## 7. Optional Internal Scoring

The method may use internal scoring for discipline, but the user-facing report should prefer materiality tiers and concise rationale unless a detailed catalyst register is requested.

Optional internal dimensions:

```text
Materiality: 1-5
Actionability: 1-5
Date confidence: High / Moderate / Low
Source confidence: High / Moderate / Low
Decision pressure: Critical / High / Medium / Low / Monitor
```

The method must avoid fake precision. Scores are prioritization aids, not investment probabilities.

## 8. Decision-Pressure Ranking

Events should be ranked by decision pressure, not date proximity alone.

Decision pressure reflects:

```text
Materiality
Actionability
Timing urgency
Source uncertainty
Thesis relevance
Exposure relevance
Potential to force valuation, risk, or IC update
```

A near-term low-impact event should not outrank a later thesis-defining event.

## 9. Depth by Tier

### Tier 1 / Critical Events

Apply full event underwriting:

```text
Source check
Event status
Date confidence
Expectation frame
Directional impact
Catalyst failure risk
Required handoffs
Prep work
Post-event follow-up
Evidence limitations
```

### Tier 2 Events

Apply moderate review:

```text
Source check
Materiality rationale
Affected dimensions
Basic directional impact
Handoff if needed
```

### Tier 3 Events

Apply light monitoring:

```text
Short note
Monitoring relevance
No deep underwriting unless escalated
```

## 10. Catalyst Mapping

Classify upcoming catalysts as:

```text
Dated Catalyst
Expected-Window Catalyst
Conditional Catalyst
Open-Ended Catalyst
```

For each material catalyst, capture:

```text
Timing confidence:
Event probability:
Materiality tier:
Investment relevance:
What to watch:
What would confirm:
What would invalidate:
Required prep:
Post-event follow-up:
```

The method must not turn inferred windows into exact dates.

## 11. Directional Impact Assessment

The method may assess directional impact but not full valuation impact.

Allowed fields:

```text
Likely revenue impact: positive / negative / uncertain
Likely margin impact: positive / negative / uncertain
Likely expectation impact: raises / lowers / resets / unclear
Likely risk impact: increases / reduces / creates binary risk
Valuation relevance: low / moderate / high
```

If valuation impact is material, create a Valuation & Expectations handoff.

## 12. Catalyst Failure Risk

For material catalysts, identify failure risk.

News & Catalysts owns:

```text
Catalyst:
Expected / required outcome:
Failure mode:
Timing risk:
Source confidence:
Why failure would matter:
Risk handoff:
```

Risk / Red Team owns:

```text
Thesis damage
Downside asymmetry
Invalidation implications
Risk gates
```

## 13. Negative News Check

The method must support bounded negative-news conclusions.

Use this structure:

```text
No Tier 1 / Tier 2 material events were identified within [window] based on [source types checked].
Limitations: [what may not be covered].
Freshness: [last checked].
This is not a claim that no risk exists.
```

Never write vague statements such as:

```text
No news found.
Nothing happened.
No risk.
```

without source and window boundaries.

## 14. Source Conflict Protocol

When sources conflict:

```text
1. Identify the conflict.
2. Prefer primary / official source when available.
3. If no primary source exists, compare top-tier reporting.
4. Label the event as conflicting / source-limited.
5. Downgrade source or date confidence.
6. State what cannot be concluded.
7. Create refresh / verification request if material.
8. Prevent exact-date treatment if timing is uncertain.
```

Do not silently choose the most convenient source.

## 15. Rumor / Unconfirmed Claim Protocol

Rumors and unconfirmed claims may be included only if they are market-moving or materially risk-relevant.

Required fields:

```text
Status: Reported / Unconfirmed / Rumor
Source basis:
Why it matters:
What would confirm:
What would disconfirm:
Do not treat as base-case fact.
```

## 16. Light Reaction Check

The method may include a light reaction check.

Allowed:

```text
Event expectation: positive / negative / mixed / uncertain
Observed reaction: price up / down / muted / volatile / not checked
Reaction note: factual and limited
Needs Market Sense?: Yes / No
Needs Market Positioning?: Yes / No
```

Do not perform driver dominance, market psychology, or pattern analysis.

## 17. Peer / Sector Read-Through

Peer and sector read-through is allowed only when materially relevant and clearly labeled as inference.

Fields:

```text
Direct Event:
Read-Through Target:
Read-Through Type:
Confidence:
Investment Relevance:
Required Handoff:
```

Read-through types:

```text
Demand
Pricing
Margin
Regulation
Supply chain
Adoption
Competitive displacement
Financing / liquidity
```

## 18. Structured Handoff Generator

For each required handoff, use:

```text
Target Agent:
Reason:
Event / Catalyst:
Affected Dimension:
Required Work:
Priority:
Deadline / Timing:
Evidence Basis:
Confidence:
Required for Complete IC?: Yes / No
```

Possible handoff targets:

```text
Evidence Collector
Valuation & Expectations
Risk / Red Team
Market Positioning
Market Sense
Macro
Equity / ETF / Commodity / Crypto / Fixed Income Agent
Sector & Industry Analysis
Investment Committee
```

## 19. Prep and Follow-Up Work Items

For Tier 1 and high-decision-pressure catalysts, create work items.

Examples:

```text
Model update required
KPI checklist required
Questions for management
Source refresh required
Scenario check required
Risk review required
Valuation update required
Post-event follow-up required
```

Do not recommend trades, sizing, hedges, or option structures.

## 20. Post-Event Update Mode

Use Post-Event Update Mode after a catalyst occurs.

Workflow:

```text
1. Identify prior expected catalyst.
2. Confirm what happened.
3. Compare expected vs actual event outcome.
4. Update status: occurred / delayed / canceled / unresolved / superseded.
5. Assess directional impact.
6. Trigger Valuation / Risk / Market Positioning / Market Sense handoffs.
7. Update monitoring triggers.
```

This mode must not become a full thesis update, full valuation update, or Market Sense report.

## 21. Refresh / Change Log Mode

When refreshing a prior report or catalyst map, include a refresh change log.

Fields:

```text
Events added:
Events updated:
Events canceled / superseded:
Dates changed:
Confidence changed:
Source status changed:
New limitations:
Follow-up items opened:
Follow-up items closed:
Last refresh timestamp:
```

A change log is not required for the first standalone review.

## 22. Preliminary Catalyst Scan Mode

Use for quick direct calls or explicitly lightweight requests.

Output:

```text
Preliminary Catalyst Scan
Scoped window:
Top 3-7 catalysts / events:
Source confidence:
Major limitations:
Needs Full Review?: Yes / No
No final recommendation.
```

This mode is not decision-grade unless explicitly upgraded to a full review.

## 23. Memo-First Report Construction

The report should be memo-first, not table-first.

Default construction:

```text
1. Executive Event View
2. What changed and why it matters
3. Active carryover events
4. Upcoming catalyst path
5. Decision-pressure events
6. Negative news check
7. Handoffs / follow-up work
8. Evidence quality notes
9. Detailed event table / appendix
```

Tables should support the narrative, not replace investment reasoning.

## 24. Evidence Quality Notes

Every full report should include evidence quality notes:

```text
Source types used:
Freshness:
Source limitations:
Unconfirmed / reported claims:
Conflicts:
Stale items:
Refresh required:
Evidence returned to Evidence Collector:
```

## 25. Confidentiality / MNPI Guardrail

When user-provided private notes, internal research, portfolio context, emails, or meeting notes are used, the method must:

- separate public evidence from private user context;
- label user-provided assumptions and notes;
- not present private notes as public facts;
- flag possible MNPI indicators;
- avoid external-clean output if private context is included;
- preserve confidentiality in evidence notes.

This is a lightweight guardrail, not a full institutional compliance system.

## 26. Output Status Logic

Supported statuses:

```text
Complete News & Catalysts Review
Limited News & Catalysts Review
Blocked News & Catalysts Review
Preliminary Catalyst Scan
```

Use `Complete` when:

```text
Material recent events and upcoming catalysts were checked with adequate source quality and freshness.
```

Use `Limited` when:

```text
The review is useful but source gaps, stale data, unavailable calendars, uncertain timing, or limited access affect confidence.
```

Use `Blocked` when:

```text
Key event information is unavailable, contradictory, stale, or inaccessible, and the missing information is decision-critical.
```

Use `Preliminary Catalyst Scan` when:

```text
The user requested a quick bounded scan or the work was intentionally limited.
```

## 27. Prohibited Method Behavior

The skill must not:

- invent events, dates, sources, links, filings, earnings dates, regulatory deadlines, trial readouts, OPEC meetings, protocol upgrades, ratings actions, or court dates;
- treat rumors or reported claims as confirmed;
- turn inferred windows into exact dates;
- rank by date proximity alone;
- show bare tiers or scores without human explanation;
- include headlines merely to fill space;
- claim no material news without checked window and source boundaries;
- perform final valuation conclusions;
- perform full risk underwriting;
- perform Market Sense driver dominance;
- issue final investment recommendations;
- provide position sizing, hedge sizing, or trading instructions;
- mix private user context with public evidence without labeling;
- launder weak evidence into strong catalyst conclusions.

## 28. Relationship to Framework

This skill should rely on `news-catalysts-framework.md` for:

```text
Detailed event taxonomy
Domain-specific checklists
Source hierarchy examples
Materiality tier definitions
Catalyst type definitions
Output templates
Handoff field definitions
Public-equity catalyst-calendar overlay
Cross-asset event examples
```

The skill defines the workflow. The framework defines the detailed reference material.

## 29. Current Design Decisions Captured

1. The skill uses an evidence-first event-materiality workflow.
2. It combines source-backed discovery with expected-event checklists.
3. It uses qualitative tiers, optional internal scoring, and human explanations.
4. It ranks events by decision pressure, not date proximity alone.
5. Domain checklists live in the framework, not inside the skill PRD.
6. Event underwriting depth depends on tier and decision pressure.
7. Negative-news conclusions must be bounded by source and time window.
8. Source conflicts require explicit handling.
9. Handoffs must be structured.
10. Reports should be memo-first with supporting tables.
11. Post-Event Update Mode is supported.
12. Refresh / Change Log Mode is supported for update workflows.
13. Preliminary Catalyst Scan Mode is supported for quick direct calls.
14. Lightweight confidentiality / MNPI guardrails are required.
