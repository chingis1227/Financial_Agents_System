# News & Catalysts Framework

## 1. Purpose

This framework is the detailed reference layer for the News & Catalysts Agent and the News & Catalysts Method Skill.

It supports:

```text
news-catalysts-agent-prd.md
news-catalysts-method-skill-prd.md
```

The framework defines event taxonomy, materiality tiers, catalyst types, source rules, freshness rules, domain overlays, output templates, handoff templates, and common traps.

The primary supported report artifact is:

```text
news_catalysts.md
```

## 2. Core Questions

The framework helps answer:

```text
What changed recently?
What older event still matters?
What could move the asset next?
Which events are decision-relevant?
Which catalysts can reset expectations, risk, timing, or valuation?
Which events require handoff to another agent?
What is confirmed, reported, inferred, stale, or uncertain?
```

## 3. Core Output Structure

Default `news_catalysts.md` structure:

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

The report should be memo-first. Tables and registers support the investment narrative but should not replace it.

## 4. Event Classification

Each material event should be classified by:

```text
Event category:
Event subcategory:
Target asset / issuer / sector / theme:
Direct event or read-through:
Recent / active carryover / upcoming / monitoring trigger:
Event status:
Date type:
Source type:
Affected dimension:
Materiality tier:
Decision pressure:
```

## 5. General Event Taxonomy

Use these general categories before applying domain overlays:

```text
Earnings / financial update
Guidance / outlook
Regulatory / legal / policy
Product / technology / adoption
Supply / demand / inventory
Financing / liquidity / capital markets
Ownership / flow / technical event
M&A / restructuring / special situation
Macro / rates / FX / commodity driver
Security / operational incident
Governance / management
Peer / sector read-through
```

## 6. Event Status Labels

Use:

```text
Confirmed — primary / official source or sufficiently reliable direct confirmation.
Reported — top-tier professional reporting, not yet officially confirmed.
Unconfirmed — plausible but not confirmed by reliable sources.
Rumor — market chatter or speculative reporting; include only if market-moving or risk-relevant.
Inferred — derived from cadence, historical pattern, statutory timeline, or management guidance.
Unknown — insufficient evidence.
```

Never treat reported, rumored, inferred, or unknown events as confirmed facts.

## 7. Date Type Labels

Use:

```text
Hard date — confirmed exact date.
Soft date — indicated date but not fully confirmed.
Date window — specific window, not exact date.
Quarter window — expected quarter.
Seasonal window — broad seasonal timing.
Open-ended — timing unclear but event remains material.
Unknown — no reliable timing.
```

Do not convert soft dates or windows into hard dates.

## 8. Affected Dimensions

Each event should identify affected dimensions:

```text
Thesis
Expectations
Risk
Timing
Valuation relevance
```

An event belongs in the main report only if it can honestly complete:

```text
This event matters because it may affect [thesis / expectations / risk / timing / valuation].
```

## 9. Materiality Tiers

### Tier 1 — Decision-Relevant Catalyst / Event Risk

Use when the event can change investment decision, thesis confidence, valuation assumptions, risk profile, or timing.

Examples:

- earnings with contested guidance;
- regulatory approval / rejection;
- major guidance reset;
- default / restructuring;
- major OPEC decision;
- crypto protocol exploit;
- material court ruling;
- ETF structure or liquidity issue affecting investability.

### Tier 2 — Thesis-Relevant Context

Use when the event informs the thesis but does not by itself force a decision.

Examples:

- meaningful peer read-through;
- non-core product update;
- moderate regulatory development;
- sector demand datapoint;
- management commentary that supports or weakens assumptions.

### Tier 3 — Monitor-Only Item

Use when the event is worth tracking but not currently thesis- or decision-critical.

Examples:

- routine conference;
- minor data release;
- low-impact product update;
- administrative filing;
- expected calendar item with limited new information.

### Excluded

Exclude:

```text
noise
duplicates
low-signal headlines
generic commentary
old background with no active relevance
events without clear investment relevance
```

Every visible tier must include a plain-language explanation.

## 10. Decision Pressure Labels

Decision pressure is separate from materiality.

Use:

```text
Critical — requires immediate analytical work or can force near-term decision update.
High — important and time-sensitive; prep required soon.
Medium — material but not urgent.
Low — relevant but limited action need.
Monitor — track only.
```

Decision pressure reflects:

```text
materiality
actionability
timing urgency
source uncertainty
thesis relevance
portfolio / exposure relevance
need for valuation, risk, or IC update
```

Events should be ranked by decision pressure, not date proximity alone.

## 11. Catalyst Types

Classify upcoming catalysts as:

```text
Dated Catalyst — known date.
Expected-Window Catalyst — likely period, not exact date.
Conditional Catalyst — depends on another trigger.
Open-Ended Catalyst — unresolved event with unclear timing but material impact.
```

Each material catalyst should include:

```text
Timing confidence:
Event probability:
Materiality tier:
Decision pressure:
Investment relevance:
What to watch:
What would confirm:
What would invalidate:
Required prep:
Post-event follow-up:
```

## 12. Source Hierarchy

### Tier 1A — Primary / Official Sources

Preferred for confirmation:

```text
Company filings
Investor relations releases
Earnings releases
Transcripts
Regulatory filings
Court documents
Central banks
Government agencies
Exchanges
Index providers
Commodity agencies
ETF issuers
Protocol / foundation announcements
Official governance votes
```

### Tier 1B — Top Professional Reporting

Useful for discovery and fast-moving confirmation:

```text
Reuters
Bloomberg
Financial Times
Wall Street Journal
Dow Jones / MarketWatch
CNBC for market-moving facts
```

Top-tier reporting can support reported facts, but should not be mislabeled as official confirmation.

### Tier 2 — Specialist / Domain Sources

Examples:

```text
CoinDesk for crypto
EIA / IEA / OPEC for energy
ETF issuer data
Index provider data
Exchange data
Rating agencies
Industry trade sources
Market-data providers
```

### Tier 3 — Context / Commentary

Examples:

```text
Sell-side research
Asset manager commentary
Bank research
Expert commentary
Industry analysis
```

Use for framing, not primary factual confirmation.

### Weak Sources

Use only with caution:

```text
social media
forums
anonymous claims
unverified newsletters
low-quality aggregators
```

Include only if the claim itself is market-moving and label clearly as rumor / unconfirmed.

## 13. Event-Specific Source Matrix

| Event Type | Preferred Sources | Common Caveat |
|---|---|---|
| Earnings / guidance | IR release, 8-K, 10-Q, transcript, earnings presentation | Aggregator dates may be tentative. |
| M&A / restructuring | Merger agreement, 8-K, proxy, regulator filings, company release | Rumors must not be treated as deals. |
| Regulatory / legal | Regulator, court docket, agency notice, official order, top-tier reporting | Filing, hearing, ruling, and approval are different events. |
| Commodity inventory | EIA, IEA, OPEC, exchange data, official producer data | Preliminary reports can be revised. |
| OPEC / producer policy | Official OPEC statement, ministerial statements, Reuters/Bloomberg | Headlines before communique may be incomplete. |
| Crypto protocol event | Official protocol blog, GitHub/repo, foundation, governance forum | Upgrade windows can slip. |
| Crypto security incident | Official protocol/exchange notice, security firm postmortem, reputable crypto press | Facts can change intraday. |
| ETF holdings / rebalance | ETF issuer, index provider, holdings file, prospectus | Holdings as-of date is essential. |
| Fixed income rating action | Rating agency release, issuer filing, trustee notice | Watch / outlook is not the same as downgrade. |
| Default / restructuring | Issuer filing, trustee notice, exchange/regulator, court filing | Media may lag legal documents. |
| Central bank event | Central bank statement, minutes, speech transcript | Market interpretation belongs to Macro / Market Sense. |
| Peer read-through | Peer filing/release/transcript, top-tier reporting | Read-through is inference, not direct evidence. |

## 14. Freshness Matrix

| Event Type | Freshness Sensitivity | Typical Refresh Requirement | Staleness Risk |
|---|---:|---|---|
| Breaking company news | High | Same day / before report finalization | Facts may update quickly. |
| Earnings date | Medium / High | Refresh before IC or calendar use | Aggregator dates can shift. |
| Guidance / preannouncement | High | Same day / latest filing or IR | Valuation assumptions may change. |
| Regulatory / court ruling | High near deadline | Official docket / agency check | Timing and outcome may change. |
| OPEC / commodity policy | High | Same day around meetings | Early headlines may be incomplete. |
| Commodity inventory data | Medium / High | Use latest release and timestamp | Revisions and release timing matter. |
| Crypto security incident | High | Intraday / daily until resolved | Losses, scope, and exploit details evolve. |
| Crypto protocol upgrade | Medium / High | Refresh close to window | Timing can slip. |
| ETF holdings / flows | Medium / High | Use issuer as-of date | Stale holdings distort exposure. |
| Rating action / default | High | Latest rating agency / issuer notice | Legal status can change quickly. |
| Macro calendar | Medium | Latest official calendar | Date stable, interpretation changes. |
| Routine conference | Low / Medium | Confirm participation | Often not a real catalyst. |

## 15. Public Equity Catalyst Calendar Overlay

For public equities, apply catalyst-calendar discipline.

### Required Distinctions

Separate:

```text
confirmed dates
guided windows
expected dates
inferred timing
rumored dates
unknown timing
```

### Public Equity Catalyst Fields

For material public-equity catalysts, capture:

```text
event name
event category
source confidence
date confidence
materiality tier
decision pressure
actionability
thesis relevance
model / KPI line affected
market setup
prep required
post-event action
```

### Public Equity Event Categories

Check:

```text
earnings and guidance
preannouncements
investor days
major conferences
product launches
customer wins / losses
regulatory / litigation events
M&A / activism / special situations
capital allocation
index changes
lockups
secondary offerings
buyback windows
blackout windows
convert / warrant events
major peer read-throughs
```

### Public Equity Traps

Avoid:

```text
treating aggregator earnings dates as confirmed
treating routine conference attendance as a catalyst
ignoring lockups / secondaries / index events
confusing guidance reaffirmation with guidance raise
treating rumor as M&A event
overstating peer read-through as direct company evidence
```

## 16. Domain Overlay — Equity / Company

### Event Categories to Check

```text
earnings
guidance
filings
investor days
product launches
management changes
customer wins / losses
M&A
activism
litigation
regulatory events
capital allocation
index / passive flow events
lockups / offerings
peer read-through
```

### Primary Source Types

```text
SEC filings
IR releases
earnings transcripts
company presentations
exchange notices
index provider releases
regulatory / court documents
top-tier reporting
```

### Typical Tier 1 Events

```text
guidance reset
major earnings surprise
regulatory approval / rejection
large M&A
material litigation ruling
major customer loss
capital raise under stress
index inclusion / deletion with flow relevance
```

### Common False Positives

```text
routine conference
minor product update
analyst rating change without thesis impact
unconfirmed M&A rumor
headline-only customer speculation
```

### Required Handoffs

```text
Valuation — guidance, margins, revenue, cash flow impact.
Risk — litigation, governance, financing, customer concentration.
Market Positioning — revisions, rating changes, crowding, reaction mismatch.
Market Sense — unexpected price reaction.
Equity Agent — business-quality or thesis implications.
```

## 17. Domain Overlay — ETF

### Event Categories to Check

```text
holdings changes
index methodology changes
rebalance
flows
tracking error
liquidity
fee changes
issuer / structure changes
underlying exposure catalysts
tax / wrapper events where relevant
```

### Primary Source Types

```text
ETF issuer website
fund prospectus
holdings file
index provider
exchange data
fund flow data
regulatory filings
```

### Typical Tier 1 Events

```text
major index methodology change
large rebalance affecting exposure
liquidity breakdown
tracking issue
issuer structural change
material underlying exposure shock
```

### Common False Positives

```text
treating ETF flow as direct demand for every holding
using stale holdings
ignoring index methodology
assuming ETF equals underlying asset perfectly
```

### Required Handoffs

```text
ETF Agent — wrapper and structure.
Market Positioning — flows and crowding.
Asset-class agent — underlying exposure catalyst.
Risk — liquidity, structure, concentration.
```

## 18. Domain Overlay — Commodity

### Event Categories to Check

```text
OPEC / producer policy
inventory data
supply disruption
sanctions
weather
shipping
production cuts
demand revisions
futures curve
geopolitical disruption
capacity / capex changes
```

### Primary Source Types

```text
EIA
IEA
OPEC
exchange data
producer releases
government agencies
shipping / sanctions notices
top-tier commodity reporting
```

### Typical Tier 1 Events

```text
OPEC policy shift
major supply disruption
inventory shock
sanctions affecting supply
major demand revision
shipping route disruption
geopolitical escalation affecting supply
```

### Common False Positives

```text
headline before official OPEC statement
short-lived price move without supply/demand confirmation
weather event with no production impact
confusing futures curve move with physical shortage
```

### Required Handoffs

```text
Commodity Agent — supply/demand and curve implications.
Macro — inflation, rates, FX impact.
Risk — geopolitical and supply-chain risks.
Market Sense — reaction mismatch or driver dominance.
```

## 19. Domain Overlay — Crypto

### Event Categories to Check

```text
ETF flows
regulation
court decisions
protocol upgrades
security incidents
exchange / custody events
token unlocks
stablecoin events
governance votes
liquidity / leverage events
institutional adoption
```

### Primary Source Types

```text
regulators
court filings
ETF issuer data
protocol / foundation announcements
governance forums
exchange notices
security postmortems
reputable crypto reporting
on-chain data providers with caveats
```

### Typical Tier 1 Events

```text
major regulatory ruling
ETF approval / flow shock
protocol exploit
exchange failure
stablecoin depeg
large token unlock
major protocol upgrade
custody or market-structure change
```

### Common False Positives

```text
social media rumor treated as fact
protocol upgrade window treated as fixed date
on-chain metric overinterpreted without context
exchange announcement treated as ecosystem-wide adoption
```

### Required Handoffs

```text
Crypto Agent — protocol, tokenomics, custody, liquidity.
Risk — security, regulatory, custody, leverage risk.
Market Positioning — flows, ETF demand, leverage.
Market Sense — sharp reaction or narrative shift.
```

## 20. Domain Overlay — Fixed Income

### Event Categories to Check

```text
central bank decisions
inflation / employment data
Treasury auctions
rating actions
defaults
restructurings
covenant events
spread shocks
refinancing
fiscal events
issuer liquidity events
```

### Primary Source Types

```text
central banks
Treasury / finance ministry
BLS / BEA / official data agencies
rating agencies
issuer filings
trustee notices
exchange / regulator notices
court filings
```

### Typical Tier 1 Events

```text
rating downgrade
default / missed payment
restructuring
auction failure / stress
central bank surprise
inflation shock
refinancing failure
covenant breach
```

### Common False Positives

```text
rating outlook confused with downgrade
macro print listed without relevance to bond duration or credit
spread move without issuer-specific evidence
maturity date listed without refinancing analysis
```

### Required Handoffs

```text
Fixed Income Agent — yield, duration, spread, credit implications.
Macro — rates, inflation, curve, policy.
Risk — default, liquidity, refinancing risk.
Market Positioning — flows and spread reaction if material.
```

## 21. Domain Overlay — Sector / Industry

### Event Categories to Check

```text
policy changes
adoption milestones
capex cycle updates
subsidies
tariffs
supply-chain bottlenecks
major company read-throughs
regulatory shifts
demand inflection points
competitive changes
```

### Primary Source Types

```text
company filings
industry regulators
government policy documents
major company transcripts
industry data providers
trade associations
top-tier reporting
```

### Typical Tier 1 Events

```text
major policy shift
tariff / subsidy change
demand inflection evidence
capex cycle reset
regulatory change affecting sector economics
major leader guidance with broad read-through
```

### Common False Positives

```text
one company issue generalized to sector without evidence
theme narrative treated as data
TAM headline treated as investable catalyst
low-quality trade commentary overused
```

### Required Handoffs

```text
Sector & Industry Agent — sector structure and profit pool.
Structural Winners Discovery — candidate implications.
Equity / ETF Agent — investable instruments.
Risk — anti-thesis and failure paths.
```

## 22. Domain Overlay — Theme / Opportunity

### Event Categories to Check

```text
policy events
geopolitical developments
technology adoption
funding / capex announcements
supply-chain bottlenecks
regulation
major customer adoption
subsidies / tariffs
commodity input shocks
```

### Primary Source Types

```text
government policy documents
regulators
company filings and releases
industry data
official statistics
top-tier reporting
recognized institutional research
```

### Typical Tier 1 Events

```text
policy regime shift
new subsidy or tariff
major adoption proof point
large capex announcement
geopolitical escalation affecting theme
regulatory approval / restriction
```

### Common False Positives

```text
theme hype with no investable mechanism
confusing beneficiaries with investable winners
assuming all companies in theme benefit equally
ignoring valuation and competition
```

### Required Handoffs

```text
Theme / Opportunity workflow
Structural Winners Discovery
Sector & Industry Analysis
Equity / ETF / Commodity / Crypto / Fixed Income Agent as relevant
Risk / Red Team
```

## 23. Material Event Card Template

```text
Event:
Date / Window:
Status:
Date Type:
Source Basis:
Source Confidence:
Date Confidence:
Materiality Tier:
Decision Pressure:
Affected Dimensions:
Directional Impact:
Why It Matters:
What Would Confirm:
What Would Disconfirm:
Required Handoff:
Follow-Up Needed:
```

## 24. Catalyst Map Row Template

```text
Catalyst:
Catalyst Type:
Timing:
Timing Confidence:
Event Probability:
Materiality Tier:
Decision Pressure:
Investment Relevance:
What To Watch:
Prep Required:
Post-Event Follow-Up:
```

## 25. Negative News Check Template

```text
Negative News Check:
Window checked:
Source types checked:
Material areas checked:
No Tier 1 / Tier 2 material events identified in:
Limitations:
Freshness:
Not a claim that no risk exists:
```

## 26. Light Reaction Check Template

```text
Event:
Expected event direction:
Observed reaction:
Reaction note:
Potential mismatch:
Needs Market Positioning?: Yes / No
Needs Market Sense?: Yes / No
Reason for handoff:
```

Do not explain driver dominance inside this section.

## 27. Peer / Sector Read-Through Template

```text
Direct Event:
Source:
Read-Through Target:
Read-Through Type:
Inference Confidence:
Why It Matters:
Limitations:
Required Handoff:
```

## 28. Catalyst Failure Flag Template

```text
Catalyst:
Expected / Required Outcome:
Failure Mode:
Timing Risk:
Source Confidence:
Why Failure Would Matter:
Risk / Red Team Handoff:
Required for Complete IC?: Yes / No
```

## 29. Structured Handoff Template

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

## 30. Evidence & Source Quality Notes Template

```text
Report as-of:
News window checked:
Upcoming catalyst window:
Last source refresh:
Source types used:
Primary-source coverage:
Top-tier reporting used:
Unconfirmed / reported claims:
Source conflicts:
Stale items:
Refresh required:
Evidence returned to Evidence Collector:
Limitations:
```

## 31. Short Examples

### Earnings Guidance Raise

```text
Affected dimensions: Expectations / Valuation
Likely impact: Raises revenue or margin expectations if guidance is credible.
Handoff: Valuation & Expectations.
Risk: Market may already price in the raise; check Market Positioning.
```

### OPEC Production Cut

```text
Affected dimensions: Commodity supply / Inflation / Macro / Risk
Likely impact: Supports oil price if credible and enforced.
Handoff: Commodity Agent, Macro Agent, Risk / Red Team.
Caveat: Wait for official statement and quota details.
```

### Crypto Protocol Exploit

```text
Affected dimensions: Security / Liquidity / Risk / Market Sense
Likely impact: Increases technical, custody, and confidence risk.
Handoff: Crypto Agent, Risk / Red Team, Market Sense if reaction is disorderly.
Caveat: Facts may change intraday.
```

### ETF Rebalance

```text
Affected dimensions: Flows / Liquidity / Underlying exposure
Likely impact: May change exposure or create short-term flow pressure.
Handoff: ETF Agent, Market Positioning.
Caveat: Confirm with issuer and index provider.
```

### Rating Downgrade

```text
Affected dimensions: Credit risk / Liquidity / Refinancing
Likely impact: Can widen spreads, reduce access to capital, or trigger mandate selling.
Handoff: Fixed Income Agent, Risk / Red Team, Market Positioning.
Caveat: Distinguish downgrade from outlook or watch.
```

## 32. Status Rules

Use:

```text
Complete News & Catalysts Review
Limited News & Catalysts Review
Blocked News & Catalysts Review
Preliminary Catalyst Scan
```

### Complete

Use when:

```text
Material recent events and upcoming catalysts were checked with adequate sources and freshness.
```

### Limited

Use when:

```text
Useful review, but source gaps, stale data, unavailable calendars, uncertain timing, or limited access affect confidence.
```

### Blocked

Use when:

```text
Key event information is unavailable, contradictory, stale, or inaccessible, and the missing information is decision-critical.
```

### Preliminary Catalyst Scan

Use when:

```text
The user requested a quick bounded scan or the work was intentionally limited.
```

## 33. Guardrails

The News & Catalysts Agent must not:

- invent events, dates, sources, links, filings, earnings dates, regulatory deadlines, trial readouts, OPEC meetings, protocol upgrades, ratings actions, or court dates;
- treat rumored or reported claims as confirmed facts;
- convert inferred windows into exact dates;
- include low-signal headlines to fill space;
- claim "no material news" without source and window boundaries;
- issue final investment recommendations;
- provide target prices;
- perform full valuation modeling;
- perform full risk underwriting;
- explain driver dominance or market psychology;
- provide position sizing, hedge sizing, or trading instructions;
- treat peer read-through as direct evidence;
- mix private user context with public evidence without labeling;
- ignore timestamp and freshness requirements.

## 34. Final Quality Check

Before finalizing `news_catalysts.md`, verify:

```text
Is every material event sourced?
Are confirmed, reported, inferred, and rumored events separated?
Are dates and windows labeled correctly?
Are Tier 1 events explained in plain language?
Are events ranked by decision pressure, not just date?
Is the negative news check bounded?
Are handoffs structured?
Are stale or conflicting sources flagged?
Are Market Sense / Market Positioning boundaries respected?
Is the report memo-first and not a headline dump?
```
