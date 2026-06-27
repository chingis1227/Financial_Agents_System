# Evidence Collection Method Skill PRD

## 1. Purpose

This skill defines how to collect, classify, structure, verify, and hand off evidence for the Financial Agent System.

The method is evidence-first, claim-support based, source-aware, freshness-aware, and decision-materiality driven. Its purpose is to make investment analysis reliable without turning user-facing reports into source dumps or audit logs.

## 2. Core Method Sequence

### 2.1 Confirm Scope

Identify:

```text
Request type
Workflow
Target asset / theme / claim
Evidence mode
Evidence profile
Routing source
Decision risk
Downstream agents
User-provided context
```

If the request is ambiguous, classify provisionally and disclose uncertainty. Ask a clarifying question only when misclassification would materially change evidence requirements.

### 2.2 Define Evidence Requirements

Separate:

```text
Universal Core Evidence
Asset-Class Core Evidence
Conditional Decision Gates
Optional / Deferred Evidence
```

For asset-first workflows, universal core evidence normally includes:

- instrument identity and classification;
- user intake context;
- latest market-sensitive data;
- primary official source;
- material recent news check;
- source dates and freshness status;
- missing-data log.

Conditional decision gates include valuation / expectations evidence, Risk / Red Team evidence, market positioning, news / catalysts, macro, sector, and portfolio context when they are material to the decision.

### 2.3 Collect Evidence Registry-First

Use `source-registry-framework.md` first.

If a needed source is unavailable, stale, paywalled, or missing, use controlled fallback only for a specific evidence need.

Fallback sources must be:

- labeled;
- tiered;
- timestamped;
- assigned limitations;
- prevented from supporting claims beyond their reliability.

### 2.4 Classify Evidence Type

Each material evidence item should be classified as one of:

```text
Reported Fact
Official Guidance / Management Statement
Market Data
Estimate / Consensus Data
Model Output
Regulatory / Legal Disclosure
News Report
Analyst / Practitioner Interpretation
User-Provided Context
Proxy Evidence
Assumption
```

For each item, include:

```text
Can support:
Cannot support:
Required caution:
```

Example:

```text
Evidence Type: Official Guidance / Management Statement
Can support: Management's stated outlook and assumptions.
Cannot support: Independent verification that the outlook will be achieved.
Required caution: Treat as management claim, not external confirmation.
```

### 2.5 Build Claim Support Map

Map material claims, not broad investment conclusions and not every raw datapoint.

A claim belongs in the map if a downstream agent could use it to support analysis, limit a conclusion, request follow-up evidence, or affect final decision readiness.

Each claim should include:

```text
Claim:
Evidence:
Evidence Type:
Source:
Source Tier:
Source Date:
Accessed Date:
Data Period:
Freshness Requirement:
Freshness Status:
Claim Support Status:
Claim Strength:
Materiality:
Limitations:
Usable By:
Cannot Support:
```

Claim support statuses:

```text
Supported
Partially Supported
Proxy-Supported
Contradicted
Unsupported
Unable to Verify
Stale / Needs Refresh
Not Material for Current Workflow
```

### 2.6 Handle Missing and Proxy Evidence

Use the missing-data protocol:

```text
Missing Data:
Why It Matters:
Materiality:
Direct Source Attempted:
Reason Unavailable:
Proxy Used:
Proxy Source:
Proxy Logic:
What Proxy Can Support:
What Proxy Cannot Support:
Effect on Analytical Evidence:
Effect on Decision Evidence:
Required Follow-up:
```

Proxy evidence may support cautious inference or open risk items, but must not be presented as direct evidence.

### 2.7 Handle Contradictions

Use the contradiction protocol:

```text
Contradiction:
Source A:
Source B:
Nature of Conflict:
Source Hierarchy Assessment:
Freshness Assessment:
Which Claim Is Supported:
Which Claim Remains Unresolved:
Materiality:
Effect on Readiness:
Required Follow-up:
```

Rules:

- official / primary sources govern official facts;
- media interpretation does not override primary documents;
- management statements should not automatically override external evidence;
- provider conflicts should be recorded, not averaged mechanically;
- unresolved material contradictions reduce readiness;
- contradictions may be handed to Risk / Red Team or Market Sense as tensions or hypotheses.

### 2.8 Apply Freshness Rules

Freshness should depend on evidence type, data volatility, release cycle, and decision materiality.

Baseline examples:

```text
Market price / market cap / yields / spreads: latest available; refresh before IC memo.
News / catalysts: latest relevant reporting; refresh if memo is produced later.
Earnings / filings: latest available filing or release.
Consensus / estimates: latest available; stale quickly around earnings or guidance changes.
ETF holdings / AUM / fees / methodology / liquidity / premium-discount / yield / peer and overlap inputs: latest issuer or official data where available; note reporting lag, holdings as-of dates, share-class differences, and fallback-source limitations.
Macro releases: latest official release for the relevant indicator.
Commodity inventories / futures curve: latest available for market-sensitive analysis.
Crypto market / on-chain / ETF flow data: latest available with provider and methodology caveats.
Sector / industry structure: recent enough for thesis relevance; not necessarily daily.
Regulatory / legal disclosures: latest official status; refresh if event-sensitive.
User portfolio context: as provided by user; state user-provided as-of date if known.
```

### 2.9 Perform Basic Normalization and Reconciliation

Allowed:

- normalize units, currencies, periods, and fiscal dates;
- reconcile inconsistent source values;
- calculate simple derived fields from sourced inputs;
- create bounded data snapshots;
- identify source mismatches and caveats.

Prohibited:

- valuation attractiveness conclusions;
- fair value conclusions;
- target prices;
- scenario conclusions;
- expected return;
- investment ranking.

### 2.10 Create Downstream Readiness Matrix

For each relevant downstream agent, classify:

```text
Ready
Ready with Caveat
Limited
Blocked
Not Required
```

Include practical meaning and required caution. A readiness label must not be bare; it must explain what the downstream agent can and cannot responsibly do.

### 2.11 Produce Evidence Pack or Scoped Artifact

Default:

```text
evidence_pack.md
```

Direct-call alternatives:

```text
evidence_readiness_note.md
evidence_verification_note.md
```

### 2.12 Maintain Living Evidence Layer

Specialist agents may submit structured evidence requests or evidence addition notices.

Material specialist-discovered evidence must be registered before it supports decision-relevant conclusions.

### 2.13 Pre-IC Evidence Lock

Before IC synthesis, confirm:

- evidence pack status;
- market data freshness;
- news / catalyst freshness;
- valuation-sensitive data freshness;
- registered specialist additions;
- unresolved gaps;
- unresolved contradictions;
- decision evidence sufficiency;
- allowed IC output status.

## 3. Anti-Hallucination Rules

The method must not:

- invent sources, facts, dates, figures, links, events, or conclusions;
- imply unavailable sources were checked;
- treat inaccessible premium data as verified;
- treat user hypotheses as facts;
- use AI summaries as material evidence;
- present proxy evidence as direct evidence;
- remove material caveats;
- strengthen claim support beyond source quality;
- silently ignore contradictions;
- issue investment conclusions under the Evidence Collector role.

## 4. Quote Discipline

Use direct quotes only when exact wording matters.

Quote selectively when relevant to:

- management guidance;
- legal / regulatory language;
- risk factors;
- covenants;
- ETF methodology;
- central bank wording;
- disputed or ambiguous claims.

Summarize straightforward facts instead of copying long excerpts. The evidence pack should preserve accuracy and auditability without becoming a repository of long source extracts.

## 5. Scoped Negative Evidence Statements

The agent may state that no material recent news was identified only within a defined source set, time window, and materiality threshold.

Template:

```text
Time Window Reviewed:
Sources Checked:
Search Terms / Source Categories:
Materiality Threshold:
Result:
Limitations:
Refresh Trigger:
```

Use bounded wording:

```text
No material recent news identified within the reviewed sources and time window.
```

Do not write an absolute claim that no news exists.

## 6. Access-Aware Evidence Handling

When preferred data is unavailable, paywalled, stale, or not checked, record:

```text
Preferred Source:
Access Status:
Fallback Source:
Fallback Quality:
What the Fallback Can Support:
What the Fallback Cannot Support:
Effect on Readiness:
Required Follow-up:
```

Fallback evidence must not appear equivalent to unavailable institutional-grade evidence.

## 7. Private Context Handling

User-provided private information should be minimized and separated from public evidence.

If private context is material, use a separate private context note or a clearly separated section. Do not include sensitive personal or portfolio details in public-looking source lists unless absolutely required.
