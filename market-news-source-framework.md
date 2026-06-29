# Market News Source Framework

<!-- reference-governance:start -->
## Reference Governance Metadata

Status: Supporting Reference  
Owner: Market Intelligence  
Contributors: Evidence Collector; News & Catalysts; Macro Agent  
Used by: Market Intelligence Agent; market-intelligence-briefing skill; News & Catalysts  
Primary reference for: market-news source overlays  
Supporting reference for: news verification and market-context evidence packs  
Not responsible for: final decision; evidence readiness; routing; IC Action; agent ownership  
Freshness sensitivity: High  
Last reviewed: 2026-06-28  
Review trigger: Review quarterly or when news source reliability, access, or verification practices change.  
Owner review needed: No  
Split/index status: Indexed in implementation/reference-library-index.md  
Canonical authority: Advisory reference only. Canonical implementation documents govern active agent, skill, evidence, routing, and IC behavior.

<!-- reference-governance:end -->


## 1. Purpose

This reference supports the Market Intelligence Agent and `market-intelligence-briefing` skill.

It provides advisory source overlays for market news discovery, verification, and framing. `implementation/04-evidence-layer.md` governs evidence readiness and source authority.

Core rule:

```text
Use reporting for discovery.
Use official sources for confirmation when available.
Use institutional commentary for framing, not primary facts.
```

## 2. Advisory Source Trust Overlay

### Tier 1 — Primary and Official Sources

Use these sources to confirm facts whenever accessible.

### Tier 2 — Reputable Secondary Reporting

Use for discovery, context, and timely reporting.

### Tier 3 — Institutional Research and Market Commentary

Use for framing and market color, not primary confirmation unless the institution itself is the subject of the news.

### Tier 4 — Low-Confidence / Narrative Sources

Use only as weak context or idea discovery. Do not treat as confirmed evidence without stronger corroboration.

## 3. Tier 1 — Primary and Official Sources

## 3.1 Central Banks

Use for monetary policy decisions, minutes, speeches, financial stability reports, balance sheet updates, and official guidance.

- Federal Reserve
- European Central Bank
- Bank of England
- Bank of Japan
- People's Bank of China
- Swiss National Bank
- Bank of Canada
- Reserve Bank of Australia

Confirmation use:

- policy decisions;
- rate statements;
- press conferences;
- meeting minutes;
- speeches;
- balance sheet / liquidity facilities;
- financial stability publications.

## 3.2 U.S. Economic Data

Use for official macro releases.

- Bureau of Labor Statistics
- Bureau of Economic Analysis
- U.S. Census Bureau
- Institute for Supply Management
- U.S. Department of the Treasury

Confirmation use:

- CPI / PPI / payrolls / unemployment;
- GDP / income / consumption;
- retail sales / housing / trade;
- ISM manufacturing and services;
- Treasury refunding / auctions / fiscal data.

## 3.3 Treasury and Finance Ministries

Use for fiscal policy, debt issuance, sanctions, budget actions, and official policy announcements.

- United States Department of the Treasury
- European Commission
- German Federal Ministry of Finance
- Ministry of Finance of Japan
- Ministry of Finance of the People's Republic of China
- Other official finance ministries when relevant

## 3.4 Market Regulators

Use for investigations, enforcement, approvals, market structure, reporting, and regulatory changes.

- Securities and Exchange Commission
- Commodity Futures Trading Commission
- Federal Deposit Insurance Corporation
- Office of the Comptroller of the Currency
- Financial Conduct Authority
- European Securities and Markets Authority

## 3.5 International Institutions

Use for global macro, financial stability, growth forecasts, debt, trade, development, and systemic risk.

- International Monetary Fund
- World Bank
- Organisation for Economic Co-operation and Development
- Bank for International Settlements
- Financial Stability Board

## 3.6 Energy and Commodities

Use for supply-demand balances, inventories, production, forecasts, and commodity market structure.

- Organization of the Petroleum Exporting Countries
- International Energy Agency
- U.S. Energy Information Administration
- World Bank Commodity Markets

## 3.7 Geopolitics and Security

Use for official geopolitical, conflict, nuclear, sanctions, and international security developments.

- North Atlantic Treaty Organization
- United Nations
- International Atomic Energy Agency
- Official government defense / foreign affairs ministries
- Official sanctions authorities

## 3.8 Companies and Markets

Use for company-specific facts, earnings, guidance, filings, ownership, and exchange announcements.

- SEC filings: 10-K, 10-Q, 8-K, S-1, DEF 14A, 13D, 13F
- Official company earnings releases
- Official company guidance updates
- Investor Relations materials
- Earnings call transcripts
- Investor presentations
- Official exchange announcements
- Exchange rule changes
- Official regulator investigations and enforcement actions

## 3.9 Governments

Use for official policy, sanctions, trade, regulation, fiscal, and geopolitical statements.

- White House releases
- Official government statements
- Finance ministry statements
- Regulatory agency releases
- Trade ministry releases
- Sanctions announcements
- Official press conferences
- Official policy documents

## 4. Tier 2 — Reputable Secondary Reporting

Use for discovery, context, and timely reporting.

Examples:

- Reuters
- Bloomberg
- CNBC
- Wall Street Journal
- Financial Times
- MarketWatch
- Investing.com
- Barron's
- New York Times
- Washington Post
- Politico
- Axios
- The Hill
- The Economist
- Semafor
- The Information
- CoinDesk
- Morningstar

Rules:

- Prefer Reuters, Bloomberg, FT, WSJ, and official-source-backed reporting for high-materiality items.
- If an item is material and an official source exists, attempt to confirm with the official source.
- If only secondary reporting is available, label the item as reported rather than officially confirmed.
- Do not duplicate multiple secondary articles about the same development unless they add material facts.

## 5. Tier 3 — Institutional Research and Market Commentary

Use for framing, market color, scenario context, and investor positioning language.

Examples:

- Goldman Sachs
- BlackRock
- JPMorgan
- Deutsche Bank
- Bank of America
- UBS
- Barclays
- PIMCO
- Morningstar research
- Major asset manager outlooks

Rules:

- Do not treat institutional commentary as primary confirmation of external facts.
- If an institution changes its own forecast or view, that fact may be reported as the institution's view.
- Clearly distinguish institutional view from confirmed macro or company facts.

Correct phrasing:

```text
JPMorgan analysts argued that the development could pressure credit spreads; this is institutional interpretation, not official confirmation.
```

## 6. Tier 4 — Low-Confidence / Narrative Sources

Examples:

- Social media
- Reddit
- YouTube
- Podcasts
- Informal newsletters
- Unverified blogs
- Partisan commentary
- Rumor accounts

Rules:

- Use only for idea discovery or sentiment context.
- Do not present as confirmed fact.
- Corroborate with stronger sources before inclusion.
- Avoid including unless the narrative itself is market-moving and clearly labeled.

## 7. Confirmation Language

Use clear source basis language.

### Officially confirmed

```text
Confirmed by the official [agency/company/central bank] release.
```

### Reported by reputable outlet

```text
Reported by Reuters; primary confirmation was not found in the available sources.
```

### Multiple reputable reports, no official confirmation

```text
Reported by multiple reputable outlets, but not yet confirmed by an official source.
```

### Institutional view

```text
This is an institutional view from [institution], not an official data release.
```

### Conflicting reports

```text
Reports differ on [detail]. Confirmed facts are [X]; unresolved points are [Y].
```

## 8. Source Use by News Type

| News Type | Discovery Sources | Confirmation Sources |
|---|---|---|
| Central bank decision | Reuters / Bloomberg / FT | Central bank statement, minutes, speech |
| Economic data | Reporting calendars / news | Official data agency release |
| Company earnings | News / market data | Company release, filing, transcript |
| Regulation | News | Regulator release, filing, enforcement notice |
| Geopolitics | News | Official government / UN / NATO / IAEA statements when available |
| Oil / commodities | News | EIA, IEA, OPEC, official inventory/supply data |
| Credit stress | News / market data | Credit spreads, regulator / central bank / official stability reports |
| Crypto regulation | CoinDesk / Reuters / Bloomberg | SEC/CFTC/court/regulator documents |

## 9. Final Rule

If the source basis is weak, the item should either be excluded or explicitly labeled as unconfirmed / low-confidence.

The Market Intelligence Agent should prefer fewer high-quality items over many weakly supported headlines.
