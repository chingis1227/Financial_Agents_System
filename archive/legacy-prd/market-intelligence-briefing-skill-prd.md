# Market Intelligence Briefing Skill — Product Requirements Document

## 1. Purpose

The `market-intelligence-briefing` skill is the reusable methodology for the Market Intelligence Agent.

Its purpose is to identify, verify, filter, and summarize the most important investor-relevant market developments within a defined time window.

The skill should produce a structured Market Intelligence Brief that is factual first, source-aware, concise, and useful to an informed investor.

## 2. Relationship to Market Intelligence Agent

The Market Intelligence Agent is the role. The `market-intelligence-briefing` skill is the method.

```text
Market Intelligence Agent
  uses:
    market-intelligence-briefing skill
      references:
        market-news-source-framework.md
        market-materiality-filter.md
```

The agent should remain concise and role-based. The detailed news-gathering, verification, filtering, and briefing workflow belongs in this skill.

## 3. Core Question

The skill should help answer:

> What happened across markets that matters for investors?

The skill should not answer:

> What hidden logic is the market trading?

That belongs to Market Sense Agent.

## 4. Supported Use Cases

The skill should support:

- daily market intelligence brief;
- ad hoc market news brief;
- broad market event summary;
- macro / policy news scan;
- cross-market development summary;
- investor-relevant news filtering;
- direct user requests such as “what happened in markets today?”

## 5. Default Scope

Default coverage:

```text
Global investor-relevant markets, US-first but global-aware.
```

Default time window:

```text
Last 24 hours, with 48–72h carryover for active drivers.
```

Include older items only when they are newly confirmed, still driving markets, producing fresh price reaction, followed by policy action, affecting earnings/guidance, escalating/de-escalating, or causing continued cross-asset repricing.

## 6. Required Inputs

The skill may use:

- user request;
- requested time window;
- requested geography or asset focus;
- market-news-source-framework.md;
- market-materiality-filter.md;
- official sources;
- reputable secondary reporting;
- institutional commentary for framing;
- market data snapshots where needed for basic relevance;
- previously generated market intelligence briefs when useful.

## 7. Source Method

The skill should follow this source hierarchy:

1. Official and primary sources for confirmation.
2. Reputable secondary reporting for discovery and context.
3. Institutional commentary for framing and interpretation, not primary facts.

Rule:

```text
Use reporting for discovery. Use official sources for confirmation when available. Use institutional commentary for framing, not primary facts.
```

The active reference `market-news-source-framework.md` defines detailed source lists and source confidence rules.

## 8. Confirmation Rules

The skill must:

- confirm material claims with official or primary sources when accessible;
- state when only secondary reporting was found;
- distinguish confirmed facts from reported claims;
- avoid inventing source access or confirmation;
- synthesize duplicate coverage into one item;
- note material source conflicts;
- separate unresolved details from confirmed facts.

If an important claim cannot be confirmed, the skill should write:

```text
Primary confirmation was not found in the available sources; this remains based on reputable reporting.
```

or similar wording.

## 9. Materiality Method

The skill should prioritize by market materiality, not headline volume.

The active reference `market-materiality-filter.md` defines the detailed filtering logic.

High-priority categories include:

- central bank decisions, speeches, minutes, and guidance;
- inflation, jobs, GDP, consumption, PMI / ISM, and other macro releases;
- Treasury and finance ministry actions;
- major regulatory actions;
- sanctions, trade restrictions, and policy changes;
- SEC filings and significant corporate disclosures;
- earnings, guidance changes, and capital allocation decisions;
- major geopolitical developments with market implications;
- commodity supply/demand shocks;
- credit or liquidity stress;
- exchange announcements and market structure changes;
- large cross-asset risk events or sentiment shifts.

Deprioritize:

- duplicate coverage;
- social media rumors;
- celebrity / lifestyle / non-market stories;
- scheduled events with no surprise or market relevance;
- minor market color;
- generic opinion pieces;
- old background unless still driving markets.

## 10. Required Workflow

### Step 1 — Define the Run

Clarify:

- time window;
- geography;
- asset class focus, if any;
- whether the user wants a broad market brief or focused brief.

Default:

```text
Broad market brief, last 24 hours, US-first but global-aware.
```

### Step 2 — Surface Candidate Items

Use reputable public reporting and official calendars/releases to identify candidate developments.

Candidate categories:

- macro;
- central banks;
- rates;
- credit;
- equities;
- major companies;
- commodities;
- geopolitics;
- regulation;
- policy;
- crypto;
- market structure;
- cross-asset moves.

### Step 3 — Confirm Material Facts

For each candidate item, check whether primary confirmation exists.

Examples:

- central bank statement or speech;
- official economic data release;
- regulatory release;
- company filing;
- earnings release;
- official government statement;
- EIA / IEA / OPEC report;
- exchange announcement.

### Step 4 — Filter by Materiality

Apply the materiality filter:

- Does this affect rates, inflation, growth, liquidity, credit, earnings, guidance, regulation, commodities, FX, risk sentiment, or sector rotation?
- Was it surprising relative to expectations?
- Did it trigger or plausibly affect market pricing?
- Is it still active if older than 24 hours?
- Is it duplicate coverage or genuinely new information?

### Step 5 — Consolidate Duplicates

If several outlets cover the same story, synthesize them into one item.

Do not repeat the same development as multiple items unless there are materially distinct follow-ups.

### Step 6 — Draft Item Cards

Each item should include:

```md
### [Topic]
- What happened:
- Confirmation / source basis:
- Market relevance:
- Concise investor takeaway:
- Affected drivers:
```

### Step 7 — Identify Market-Moving Drivers

Summarize recurring drivers across items.

Possible driver categories:

- rates / policy;
- inflation;
- growth;
- liquidity / credit;
- commodities;
- FX;
- earnings / guidance;
- regulation / policy;
- geopolitics;
- risk sentiment;
- sector rotation.

This section should remain descriptive, not a deep driver-dominance analysis.

### Step 8 — Add Cross-Market Read If Justified

Include `Cross-Market Read` only if there is a meaningful broader pattern.

It should remain concise and factual.

It may say what Market Sense Agent should examine next, but it should not become a Market Sense report.

### Step 9 — Quality Check

Before finalizing, verify:

- no fabricated confirmation;
- facts and interpretation are separated;
- weakly sourced items are labeled;
- no duplicate items;
- no low-signal filler;
- concise investor takeaways do not become trade recommendations;
- item count is justified by news flow;
- older items are included only when still active.

## 11. Output Format

Default output:

```md
## Market Intelligence Brief

## Key Developments

### 1. [Topic]
- What happened:
- Confirmation / source basis:
- Market relevance:
- Concise investor takeaway:
- Affected drivers:

## Market-Moving Drivers

## Cross-Market Read
```

## 12. Item Length and Count

Default item count:

- 5–10 items in normal news flow;
- fewer if news flow is thin;
- up to 12 only when genuinely justified.

Item length:

- simple item: 4–6 sentences;
- important or complex item: up to 15 sentences;
- do not write long essays;
- do not pad.

## 13. Market Relevance vs Interpretation

The skill may provide light market relevance and concise investor takeaways.

Allowed:

```text
This matters because it can shift inflation expectations, rate-cut pricing, and energy-sector earnings assumptions.
```

Allowed:

```text
A lower oil risk premium reduces near-term inflation pressure and can support bonds, consumer sectors, and airlines, while pressuring energy equities and reducing demand for defensive hedges.
```

Not allowed:

```text
The market is clearly repricing a Fed shock and ignoring geopolitics.
```

That belongs to Market Sense / Driver Dominance.

## 14. Affected Drivers

Each item should identify affected drivers where relevant.

Examples:

- Fed policy expectations;
- real yields;
- USD;
- inflation expectations;
- oil risk premium;
- commodity supply;
- earnings revisions;
- company guidance;
- credit spreads;
- liquidity;
- risk sentiment;
- sector rotation;
- regulation;
- geopolitics.

## 15. Style and Language

The skill should follow the global skills when applicable:

```text
C:\Users\ShumeikoYe\.codex\skills\investment-analytical-style\SKILL.md
C:\Users\ShumeikoYe\.codex\skills\language-policy\SKILL.md
```

Report artifacts and project files should be written in English unless explicitly requested otherwise.

User-facing chat communication defaults to Russian.

## 16. Non-Goals

The skill should not:

- produce a Market Sense report;
- perform Driver Dominance analysis;
- perform market pattern matching;
- provide buy/sell recommendations;
- provide portfolio allocation advice;
- replace Macro Agent;
- replace News & Catalysts Agent;
- replace Investment Committee Agent;
- produce a long market essay by default;
- include rumor-like claims without labeling them;
- pad the brief with weak items.

## 17. Expected Artifact

The active implementation should produce:

```text
market_intelligence_brief.md
```

Canonical report path:

```text
reports/
  market_intelligence/
    YYYY-MM-DD/
      market_intelligence_brief.md
```

The path convention is fixed for v0 unless a later workflow-level PRD changes it.

## 18. Current Design Decisions Captured

1. `market-intelligence-briefing` is the method used by Market Intelligence Agent.
2. The skill produces a structured Market Intelligence Brief.
3. Default window is 24h with 48–72h carryover for active drivers.
4. Coverage is global investor-relevant, US-first but global-aware.
5. Source framework should be separate.
6. Materiality filter should be separate.
7. Each item includes what happened, source basis, market relevance, concise investor takeaway, and affected drivers.
8. Each important item may be up to 15 sentences.
9. Market-moving drivers section is included when relevant.
10. Cross-market read is optional and should remain concise.
11. The skill does not perform Market Sense or Driver Dominance analysis.
