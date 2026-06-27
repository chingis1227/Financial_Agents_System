# Source Registry Framework

## 1. Purpose

The source registry defines how the Financial Agent System admits, tiers, restricts, and retires sources. It is not merely a static source list. It is a quality-control framework for source reliability, claim strength, freshness, and evidence usability.

The source registry should help answer:

```text
Can this source support this claim, at this strength, for this workflow?
```

## 2. Source Admission Principles

A source is more useful when it is:

- primary or official;
- directly relevant to the claim;
- verifiable;
- current enough for the data type;
- methodologically transparent;
- institutionally credible;
- consistent with other high-quality sources or clearly reconcilable;
- accessible enough to preserve a repeatable evidence trail.

## 3. Source Tiers

### 3.1 Tier 1 — Primary / Official Sources

Examples:

```text
Company filings
Company investor relations
Regulatory filings
Exchange data
Central bank releases
Official statistics
ETF issuer documents
Bond offering documents
Index methodology documents
Protocol documentation where applicable
```

Can support:

- reported facts;
- official disclosures;
- legal / regulatory facts;
- issuer-level data;
- official methodology;
- policy decisions.

### 3.2 Tier 2 — Recognized Data Providers / Institutional Sources

Examples:

```text
Recognized market data providers
Consensus estimate providers
Index providers
Fund flow providers
Ownership / positioning datasets
Institutional research datasets
Specialist industry datasets
```

Can support:

- market data;
- estimates;
- revisions;
- flows;
- ownership;
- positioning;
- sector metrics.

Limitations must include provider, date, coverage, methodology, and access caveats where relevant.

### 3.3 Tier 3 — Reputable Financial Media / Practitioner Research

Examples:

```text
Reuters
Bloomberg
Financial Times
Wall Street Journal
Major asset manager research
Consulting / audit / industry research
Specialist trade publications
Recognized practitioner research
```

Can support:

- news;
- catalysts;
- context;
- corroborating evidence;
- practitioner interpretation.

Tier 3 sources should not by themselves support strong financial facts when primary sources are available.

### 3.4 Tier 4 — Commentary / Social / Unsourced / Low-Control Sources

Examples:

```text
Blogs
Social media posts
Message boards
SEO content
Promotional material
Unverified newsletters
Unattributed commentary
```

Can support:

- hypothesis generation;
- sentiment signals;
- pointers for verification.

Cannot support:

- material factual claims;
- valuation inputs;
- risk verdicts;
- final IC action.

Core rule:

```text
Weak sources may generate questions, not conclusions.
```

## 4. Pointer-Only Sources

AI-generated summaries, automated summaries, SEO-like pages, and aggregated content are pointer-only.

They may be used to:

- discover possible primary sources;
- identify events that require verification;
- generate search leads;
- compare against verified sources as weak context.

They must not support:

- material factual claims;
- valuation inputs;
- management guidance;
- regulatory facts;
- risk conclusions;
- final IC decision logic.

## 5. Controlled Fallback Rules

Fallback research is allowed only when:

- the registry does not cover the required evidence;
- the preferred source is unavailable, stale, paywalled, or inaccessible;
- the evidence need is specific;
- the fallback source is labeled and tiered;
- the claim-strength boundary is explicit.

Fallback source entry:

```text
Fallback Source:
Reason Used:
Preferred Source Gap:
Proposed Tier:
Can Support:
Cannot Support:
Registry Action Recommended:
```

Fallback sources should not appear equivalent to preferred sources unless they meet the same admission standard.

## 6. Access Status

Each preferred or fallback source should be classified when access matters:

```text
Available
Unavailable
Paywalled
User-Provided
Not Checked
Stale
Not Material
```

If premium data is unavailable, the evidence pack should state the effect on readiness rather than pretending institutional-grade evidence was reviewed.

## 7. Source Lifecycle

Fallback and newly discovered sources should follow a lifecycle:

```text
Candidate Source
Reviewed Source
Accepted Source
Restricted Source
Deprecated Source
Rejected Source
```

### Candidate Source

A source found through fallback that may be useful for future workflows.

### Reviewed Source

A source checked against admission criteria: provenance, credibility, update cycle, data coverage, limitations, and claim relevance.

### Accepted Source

A source approved for specific domains, claim types, or workflows.

### Restricted Source

A source usable only for limited purposes, such as context, corroboration, sentiment, or pointer use.

### Deprecated Source

A source that was previously useful but is now stale, unavailable, methodologically changed, or no longer reliable.

### Rejected Source

A source that should not be used because of weak provenance, promotional intent, unreliable data, lack of sourcing, AI generation, or other quality failures.

No fallback source becomes approved automatically.

## 8. Avoid / Restricted Source Rules

Avoid using the following for material claims:

- unsourced summaries;
- promotional materials;
- AI-generated pages;
- SEO pages;
- unattributed social content;
- stale pages without date;
- sources with unclear provenance;
- sources that cite no primary material;
- sources that materially conflict with primary evidence without explanation.

## 9. Claim-Strength Boundary

The strength of a claim must not exceed the reliability, freshness, and relevance of the source.

Examples:

```text
A company filing can support reported revenue.
A management call can support management's stated outlook, not independent proof that the outlook will occur.
A media report can support that an event was reported, but not replace official disclosure when official disclosure is required.
An AI summary can point to a possible event, but cannot support the event as fact.
A proxy can support a bounded inference, but cannot remove a direct-data limitation.
```

## 10. Domain Examples

Detailed domain playbooks should be created alongside the corresponding agents. The registry should preserve examples by domain without replacing domain playbooks.

Examples of preferred categories:

```text
Equities: company filings, investor relations, earnings releases, transcripts, official financial statements.
ETFs: issuer holdings files, issuer fund pages, fund prospectus / SAI, fact sheet, index methodology, AUM, fees, NAV / premium-discount data, distributions, liquidity data, exchange data, and reputable comparison / overlap tools such as ETFRC as secondary fallback rather than primary holdings evidence.
Commodities: official inventories, futures curve data, government agencies, exchanges, central banks, official crop / energy / customs / trade data, producer reports, recognized industry bodies, and family-specific sources such as EIA / IEA / OPEC for oil and gas, USDA / WASDE for agriculture, World Gold Council and central bank reserve data for gold, USGS and exchange warehouse data for metals, and nuclear industry / project data for uranium. Premium sources such as Bloomberg, LSEG / Refinitiv, S&P Global / Platts, Argus, Wood Mackenzie, Kpler, Vortexa, Fastmarkets, CME / ICE / LME data, and similar providers should be treated as recognized institutional sources where accessible; if unavailable, use explicit access-aware fallback and reduce claim strength as needed.
Crypto: protocol documentation, official network data, blockchain explorers and raw chain data where practical, reputable exchange data, ETF issuer flow data, official regulatory sources, transparent on-chain providers, professional crypto data providers with methodology notes, and dashboard / aggregator sources only with caveats. Detailed crypto source, metric, freshness, and fallback rules are defined in `crypto-data-source-and-metric-framework.md`.
Fixed Income: instrument terms and current market compensation both matter. Use issuer filings, debt schedules, offering memoranda, prospectuses, indentures, official statements for munis, Treasury and central-bank curve data, real-yield and breakeven data, current price / yield / spread / OAS data where accessible, credit ratings and rating reports as inputs rather than conclusions, ETF / fund issuer holdings files, fund fact sheets, SEC yield / distribution data, NAV premium-discount data, MSRB / EMMA muni disclosures, exchange / regulator data, and recognized institutional market-data sources where accessible. Missing current yield / spread / curve / liquidity data should reduce claim strength for current attractiveness conclusions.
Macro: central banks, official statistics, government agencies, recognized economic databases.
News / Catalysts: official releases, filings, reputable financial media, regulators, exchanges.
Market Positioning: consensus / revision providers where accessible, regulatory ownership filings, fund reports, ETF issuer flow data, official short interest, securities lending / borrow data where available, OCC / Cboe / exchange options data, CFTC COT for futures-linked exposures, reliable market data, and source-backed narrative evidence.
```
