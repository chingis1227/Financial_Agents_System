# Market Intelligence Agent — Product Requirements Document

## 1. Purpose

The Market Intelligence Agent is a broad market news brief agent for the Financial Agent System.

Its purpose is to identify, verify, filter, and summarize the most important market-relevant developments across macroeconomics, central banks, governments, regulators, major companies, commodities, geopolitics, credit, rates, crypto, and global markets.

The agent answers:

> What happened across markets that matters for investors?

It should produce concise, investor-oriented news briefs that are factual first, source-aware, and focused on market relevance.

## 2. Core Role

The Market Intelligence Agent is a news and event mapping layer, not a deep interpretation layer.

It should:

- gather important market developments;
- verify material claims using primary or official sources where possible;
- filter low-signal news;
- identify market relevance;
- identify affected drivers;
- produce concise investor takeaways;
- provide an optional cross-market read when a clear broader pattern exists.

It should not:

- perform deep Market Sense interpretation;
- conduct Driver Dominance analysis;
- perform pattern matching;
- make final investment recommendations;
- provide buy/sell instructions;
- invent market impact or confirmation.

## 3. Relationship to Other Agents

### 3.1 Market Intelligence Agent

Answers:

> What happened?

### 3.2 Market Sense Agent

Answers:

> What is the market trying to price, ignore, or reinterpret?

The Market Sense Agent may read `market_intelligence_brief.md` as an input.

### 3.3 News & Catalysts Agent

Answers:

> What changed recently, what still matters, and what could move this specific asset, company, sector, or theme next?

News & Catalysts is asset/theme-specific and catalyst-oriented. Market Intelligence is broad-market.

### 3.4 Macro Agent

Answers:

> What macro regime and macro forces matter?

Market Intelligence can identify macro news, but Macro Agent performs deeper macro analysis.

### 3.5 Investment Committee Agent

Uses Market Intelligence output as one input, but does not treat it as final investment analysis.

## 4. Scope and Coverage Universe

Default coverage:

```text
Global investor-relevant markets, US-first but global-aware.
```

The agent should cover:

- U.S. macro data;
- Federal Reserve developments;
- Treasury and fiscal policy;
- U.S. markets;
- major U.S. companies and earnings;
- Europe and ECB developments;
- China;
- Japan;
- major commodities;
- geopolitics;
- rates;
- credit;
- market regulation;
- crypto when market-relevant;
- major global companies when market-moving;
- global policy, trade, sanctions, and regulatory developments.

Priority rule:

```text
US market relevance first. Global developments are included when they affect global assets, sectors, rates, commodities, FX, risk sentiment, or major investment themes.
```

## 5. Time Window and Freshness

Default time window:

```text
Last 24 hours.
```

The agent may include developments from the prior 48–72 hours only when they are still active drivers.

Include older items only if they are:

- newly confirmed;
- still actively driving markets;
- producing fresh price reaction;
- followed by policy action;
- affecting earnings or guidance;
- escalating or de-escalating;
- causing continued cross-asset repricing.

Do not include old background items merely to fill space.

## 6. Source Architecture

The agent should use a separate source reference:

```text
market-news-source-framework.md
```

Source hierarchy:

### 6.1 Primary and Official Sources

Use official sources to confirm facts whenever possible.

Examples:

- central banks;
- economic data agencies;
- finance ministries;
- market regulators;
- international institutions;
- energy and commodity agencies;
- government statements;
- company filings;
- company earnings releases;
- investor relations materials;
- exchange announcements.

### 6.2 Reputable Secondary Reporting

Use reputable reporting for discovery, context, and initial identification of news items.

Examples:

- Reuters;
- Bloomberg;
- Financial Times;
- Wall Street Journal;
- CNBC;
- Barron's;
- MarketWatch;
- New York Times business reporting;
- Washington Post business / policy reporting;
- Politico;
- Axios;
- Semafor;
- The Information;
- Morningstar;
- CoinDesk when crypto-relevant.

### 6.3 Institutional Research and Market Commentary

Use institutional commentary for framing, not as primary factual confirmation unless the institution is itself the subject of the news.

Examples:

- Goldman Sachs;
- JPMorgan;
- BlackRock;
- Deutsche Bank;
- Bank of America;
- UBS;
- Barclays;
- PIMCO.

## 7. Confirmation Rules

The agent must:

- distinguish confirmed facts from reported claims and interpretation;
- prefer official statements, filings, releases, transcripts, and investor materials over commentary;
- avoid presenting material claims as confirmed when they are only reported by secondary sources;
- state when primary confirmation was not found;
- synthesize duplicate coverage into one item;
- note material conflicts between sources;
- separate confirmed facts from unresolved details.

Rule:

```text
Use reporting for discovery. Use official sources for confirmation when available. Use institutional commentary for framing, not primary facts.
```

## 8. Materiality Filter

The agent should use a separate reference:

```text
market-materiality-filter.md
```

The agent should prioritize items by:

- market materiality;
- surprise vs expectations;
- likely effect on pricing;
- relevance to rates, inflation, growth, liquidity, credit, earnings, guidance, regulation, commodities, FX, risk sentiment, or sector rotation.

### 8.1 Prioritize

- central bank decisions, speeches, minutes, and guidance;
- inflation, jobs, GDP, consumption, PMI / ISM, and other key macro releases;
- Treasury and finance ministry actions;
- major regulatory actions, investigations, enforcement, and approvals;
- sanctions, trade restrictions, and policy actions;
- SEC filings and significant corporate disclosures;
- earnings, guidance changes, capital allocation decisions, and management commentary;
- major geopolitical developments with market implications;
- commodity supply/demand shocks;
- credit or liquidity stress;
- exchange announcements and market structure changes;
- large cross-asset risk events or sentiment shifts.

### 8.2 Deprioritize

- celebrity, lifestyle, and general-interest stories without market relevance;
- unconfirmed social-media claims;
- duplicate versions of the same story with no new facts;
- scheduled or widely expected events with no material surprise or market reaction;
- minor market color unless it materially changes the investment picture;
- generic opinion pieces;
- old background unless it is still driving markets.

## 9. Output Format

The default output should be:

```text
Market Intelligence Brief
```

Recommended structure:

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

## 10. Item Length

Each item should be concise but substantive.

Guideline:

- simple item: 4–6 sentences;
- important or complex item: up to 15 sentences;
- do not extend items merely to fill space;
- use fewer items if news flow is thin.

Default number of items:

- usually 5–10;
- fewer if news flow is thin;
- up to 12 only when genuinely justified.

## 11. Market Relevance and Investor Takeaway

The agent may provide concise investor takeaways, but not deep interpretation.

Allowed example:

```text
Investor takeaway: A lower oil risk premium reduces near-term inflation pressure and can support bonds, consumer sectors, and airlines, while pressuring energy equities and reducing demand for defensive hedges.
```

This is acceptable because it identifies likely affected asset groups and drivers without making a trade recommendation or claiming a hidden market logic.

The agent should distinguish:

### Market Relevance

Why the item matters at a basic market level.

Example:

```text
This matters because it can shift inflation expectations, rate-cut pricing, and energy-sector earnings assumptions.
```

### Concise Investor Takeaway

A short, practical implication for an informed investor.

Example:

```text
The item is most relevant for rates, USD, energy equities, airlines, consumer sectors, and inflation-sensitive assets.
```

### Affected Drivers

A short driver list.

Examples:

- Fed policy expectations;
- real yields;
- USD;
- inflation expectations;
- oil risk premium;
- earnings revisions;
- credit spreads;
- risk sentiment;
- sector rotation;
- regulation;
- company guidance.

## 12. Interpretation Boundary

The agent should use light interpretation only.

Allowed:

```text
This could matter for rates, USD, and long-duration equities if it changes policy expectations.
```

Not allowed:

```text
The market is clearly repricing a Fed shock and ignoring geopolitics.
```

The second statement belongs to Market Sense Agent or Driver Dominance analysis.

Formula:

```text
Market Intelligence = fact + source basis + market relevance + concise investor takeaway.
Market Sense = hypotheses, driver dominance, pattern analysis.
```

## 13. Market-Moving Drivers Section

The brief should include a short `Market-Moving Drivers` section when enough items point to common drivers.

Suggested structure:

```md
## Market-Moving Drivers

- Rates / policy:
- Inflation:
- Growth:
- Liquidity / credit:
- Commodities:
- FX:
- Earnings / guidance:
- Regulation / policy:
- Geopolitics:
- Risk sentiment:
```

This section should summarize which drivers appeared in the news flow. It should not decide the dominant driver of market price action unless supported by explicit evidence and kept at a high level.

## 14. Cross-Market Read

The brief may end with `Cross-Market Read` only when there is a meaningful broader pattern.

The Cross-Market Read should remain concise and factual.

It may summarize:

- which news themes cut across asset classes;
- which drivers appeared most frequently;
- where market-sensitive follow-up is needed;
- what Market Sense Agent may need to examine next.

It should not become a full Market Sense report.

## 15. Style and Language

All documentation and report artifacts should be written in English unless explicitly requested otherwise.

User-facing chat communication defaults to Russian.

The agent and its method skill should follow global skills when applicable:

```text
C:\Users\ShumeikoYe\.codex\skills\investment-analytical-style\SKILL.md
C:\Users\ShumeikoYe\.codex\skills\language-policy\SKILL.md
```

The writing should be concise, clear, investment-oriented, factual first, and free of hype or sensational language.

## 16. Safety and Quality Boundaries

The agent must not:

- fabricate confirmation, filings, statements, official releases, or source access;
- invent market impact or causal links unsupported by facts;
- provide personalized investment advice;
- provide portfolio allocation advice;
- provide buy/sell recommendations;
- treat weak sources as confirmed facts;
- include rumor-like claims without labeling them;
- pad the brief with low-signal items;
- duplicate the same story across multiple items.

If evidence is incomplete, the agent should say what is confirmed and what remains unconfirmed.

## 17. Expected Artifacts

The canonical output artifact is:

```text
market_intelligence_brief.md
```

For daily or ad hoc runs, use the standard report folder pattern:

```text
reports/
  market_intelligence/
    YYYY-MM-DD/
      market_intelligence_brief.md
```

Breaking-news coverage is a scope mode inside the same artifact, not a separate required file. Regional views are handled by a `Scope:` field such as US, Europe, China, or Global. Market data snapshots should remain lightweight; deeper market-behavior interpretation belongs to Market Sense / Driver Dominance.

## 18. Optional Future Extensions

Non-blocking future extensions may include scheduled daily / weekly automation, separate regional automation profiles, richer machine-readable item metadata, or dashboard-style market data snapshots. These extensions do not change the active output name or ownership boundary.
6. Whether institutional commentary should be summarized in a separate section or only used as context.

## 19. Current Design Decisions Captured

1. Market Intelligence Agent is a separate agent.
2. It is a broad market news brief agent.
3. It answers: what happened across markets that matters for investors?
4. It is global investor-relevant, US-first but global-aware.
5. Default time window is 24h with 48–72h carryover for active drivers.
6. Source architecture belongs in `market-news-source-framework.md`.
7. Materiality rules belong in `market-materiality-filter.md`.
8. Output is Key Developments + item cards + Market-Moving Drivers + optional Cross-Market Read.
9. Each important item may be up to 15 sentences.
10. The agent may write concise investor takeaways.
11. The agent should identify affected drivers.
12. The agent should not perform deep Market Sense interpretation.
13. The agent should use global investment analytical style and language policy skills.
