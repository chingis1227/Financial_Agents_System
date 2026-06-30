# Market Materiality Filter

<!-- reference-governance:start -->
## Reference Governance Metadata

Status: Supporting Reference  
Owner: Market Intelligence  
Contributors: News & Catalysts; Evidence Collector; Market Sense  
Used by: Market Intelligence Agent; market-intelligence-briefing skill; News & Catalysts  
Primary reference for: market-news materiality filtering  
Supporting reference for: briefing inclusion decisions and catalyst triage  
Not responsible for: final decision; evidence readiness; routing; IC Action; agent ownership  
Freshness sensitivity: Medium  
Last reviewed: 2026-06-28  
Review trigger: Review when market-intelligence workflow, catalyst taxonomy, or materiality criteria change.  
Owner review needed: No  
Split/index status: Indexed in implementation/reference-library-index.md  
Canonical authority: Advisory reference only. Canonical implementation documents govern active agent, skill, evidence, routing, and IC behavior.

<!-- reference-governance:end -->


## 1. Purpose

This reference supports the Market Intelligence Agent and `market-intelligence-briefing` skill.

It defines how to decide whether a news item is material enough to include in a Market Intelligence Brief.

The goal is to avoid headline dumping and focus on developments that matter for investors, asset prices, policy expectations, earnings, credit, commodities, FX, risk sentiment, or sector rotation.

## 2. Core Rule

Prioritize by market materiality, surprise, and likely pricing relevance — not by headline volume.

A news item should be included when it affects, or could plausibly affect:

- rates;
- inflation expectations;
- growth expectations;
- liquidity;
- credit;
- earnings;
- guidance;
- regulation;
- commodities;
- FX;
- risk sentiment;
- sector rotation;
- market structure;
- major investment themes.

## 3. Materiality Questions

Before including an item, ask:

1. Is it new or newly confirmed?
2. Is it surprising relative to expectations?
3. Does it affect a major market driver?
4. Could it change pricing, positioning, risk sentiment, or policy expectations?
5. Does it affect a major asset class, sector, large company, commodity, currency, or credit market?
6. Is there evidence of market reaction or likely market relevance?
7. Is it still active if older than 24 hours?
8. Is it duplicative of another item already included?
9. Is the source reliable enough?
10. Can the item be explained concisely with a clear market relevance?

If the answer is mostly no, exclude it.

## 4. High-Priority Items

### 4.1 Central Banks and Rates

Include:

- rate decisions;
- policy statements;
- speeches with market-moving guidance;
- minutes;
- balance sheet / liquidity operations;
- changes in policy reaction function;
- major changes in rate-cut or rate-hike expectations.

Affected drivers:

- Fed policy expectations;
- real yields;
- USD;
- valuation multiples;
- liquidity;
- credit spreads.

### 4.2 Macro Data

Include major releases when they are new, surprising, or market-moving:

- inflation;
- payrolls / unemployment;
- GDP;
- retail sales;
- consumption;
- PMI / ISM;
- industrial production;
- housing;
- trade;
- consumer confidence when market-relevant.

Affected drivers:

- growth;
- inflation;
- rates;
- earnings;
- sector rotation;
- risk sentiment.

### 4.3 Treasury, Fiscal, and Government Policy

Include:

- Treasury refunding;
- auction stress;
- major fiscal announcements;
- debt ceiling / shutdown developments;
- sanctions;
- tariffs;
- trade restrictions;
- industrial policy;
- tax policy changes.

Affected drivers:

- yields;
- term premium;
- USD;
- sector policy risk;
- inflation;
- supply chains.

### 4.4 Regulation and Enforcement

Include:

- major SEC / CFTC / FCA / ESMA actions;
- bank regulation;
- antitrust actions;
- crypto regulation;
- major approvals or rejections;
- court rulings with market impact;
- market structure rule changes.

Affected drivers:

- regulatory risk;
- sector valuation;
- company earnings;
- market access;
- liquidity;
- capital requirements.

### 4.5 Company Earnings and Corporate Disclosures

Include:

- major earnings surprises;
- guidance changes;
- margin warnings;
- large capex announcements;
- capital allocation changes;
- major M&A;
- management changes;
- strategic pivots;
- large 8-K / filing disclosures;
- major product or regulatory developments.

Affected drivers:

- earnings revisions;
- guidance;
- margins;
- valuation;
- sector read-through;
- capex cycle;
- competitive dynamics.

### 4.6 Commodities and Energy

Include:

- oil supply disruptions;
- OPEC+ decisions;
- inventory shocks;
- IEA / EIA / OPEC revisions;
- major commodity price moves;
- sanctions affecting supply;
- weather or shipping disruptions;
- major demand revisions.

Affected drivers:

- inflation;
- commodity supply;
- energy equities;
- consumer sectors;
- airlines;
- rates;
- FX.

### 4.7 Geopolitics

Include only when market-relevant:

- conflict escalation / de-escalation;
- sanctions;
- trade restrictions;
- military developments affecting supply chains or commodities;
- nuclear / security risks;
- shipping lane disruptions;
- major diplomatic breakthroughs or breakdowns.

Affected drivers:

- risk sentiment;
- oil / gas risk premium;
- defense spending;
- safe-haven demand;
- supply chains;
- regional equities / FX.

### 4.8 Credit, Liquidity, and Financial Stability

Include:

- credit spread widening;
- bank stress;
- funding stress;
- major default / restructuring;
- liquidity facility changes;
- financial stability warnings;
- large fund blowups;
- market functioning issues.

Affected drivers:

- credit spreads;
- liquidity;
- risk sentiment;
- bank equities;
- refinancing risk;
- equity risk premium.

### 4.9 Crypto and Digital Assets

Include when market-relevant:

- major ETF flow developments;
- SEC / CFTC / court actions;
- major exchange developments;
- stablecoin regulation;
- institutional adoption;
- large security incidents;
- major protocol failures or upgrades.

Affected drivers:

- regulation;
- ETF flows;
- liquidity;
- risk appetite;
- leverage;
- institutional adoption.

### 4.10 Market Structure and Exchanges

Include:

- exchange outages;
- trading rule changes;
- settlement changes;
- short-selling bans;
- margin rule changes;
- index methodology changes with market impact.

Affected drivers:

- liquidity;
- market access;
- volatility;
- flows;
- positioning.

## 5. Deprioritize or Exclude

Exclude or heavily deprioritize:

- celebrity / lifestyle stories without market relevance;
- generic political commentary without policy or market impact;
- unconfirmed social media claims;
- duplicate articles with no new facts;
- minor analyst opinion changes without market relevance;
- scheduled events with no surprise or market reaction;
- small company news with no sector read-through;
- old background items;
- sensational headlines unsupported by primary facts;
- minor price moves without clear driver or relevance;
- repetitive rewrites of widely known stories.

## 6. Carryover Rule for 48–72 Hour Items

A prior item may be included if it is still active.

Include if:

- newly confirmed;
- still driving market prices;
- has a policy follow-up;
- caused fresh price reaction;
- escalated or de-escalated;
- affected earnings or guidance;
- triggered cross-asset repricing;
- changed market expectations since the original report.

Exclude if:

- it is only background;
- it is old and unchanged;
- there is no fresh market relevance;
- it merely repeats prior reporting.

## 7. Item Ranking

Rank items by:

1. Market impact or likely market impact.
2. Surprise vs expectations.
3. Breadth across asset classes or sectors.
4. Source confidence.
5. Freshness.
6. Relevance to active market drivers.
7. User relevance if the user specified an asset, sector, or theme.

## 8. Brief Size Control

Default:

- 5–10 items.

Use fewer if news flow is thin.

Use up to 12 only when genuinely justified.

Never pad the brief with weak items.

## 9. Driver Tags

Each included item should list affected drivers when relevant.

Common driver tags:

- Fed policy expectations
- Real yields
- USD
- Inflation expectations
- Growth expectations
- Oil risk premium
- Commodity supply
- Credit spreads
- Liquidity
- Earnings revisions
- Company guidance
- Regulation
- Geopolitics
- Risk sentiment
- Sector rotation
- FX
- Market structure
- ETF flows
- Positioning

## 10. Final Inclusion Test

Before including an item, the Market Intelligence Agent should be able to complete this sentence:

```text
This matters for investors because it affects [driver / asset class / sector / policy expectation / earnings path].
```

If the sentence cannot be completed honestly, exclude the item.
