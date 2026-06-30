# Evidence Collector Agent PRD

## 1. Purpose

The Evidence Collector Agent is the Financial Agent System's evidence control tower. It owns the shared evidence base, source discipline, freshness tracking, missing-data disclosure, claim support mapping, and evidence readiness classification for downstream investment analysis.

The agent exists to prevent the system from turning weak, stale, inaccessible, proxied, contradictory, or user-supplied information into unsupported investment conclusions.

It does not make investment recommendations, valuation judgments, risk verdicts, thesis conclusions, market-sense interpretations, or portfolio decisions.

## 2. Core Question

```text
What do we know, how reliable is it, what supports each material claim, what is missing, and which downstream agents can responsibly proceed?
```

## 3. Primary Output Artifacts

Default workflow artifact:

```text
evidence_pack.md
```

Scoped direct-call artifacts:

```text
evidence_readiness_note.md
evidence_verification_note.md
```

Optional control artifacts when needed:

```text
evidence_request_log.md
missing_data_log.md
evidence_refresh_log.md
private_context_note.md
data/[bounded_snapshot].csv
```

## 4. Role and Responsibilities

The Evidence Collector Agent should:

- create and maintain the workflow evidence base;
- organize evidence around material claims, not merely around source lists;
- use `source-registry-framework.md` and relevant domain evidence playbooks;
- timestamp evidence by source date, accessed date, data period, freshness requirement, freshness status, and as-of note;
- classify source quality, source tier, evidence type, claim support, and claim strength;
- distinguish public evidence from private user context;
- identify and record missing, stale, proxied, contradicted, inaccessible, paywalled, lower-confidence, or weak evidence;
- produce an overall evidence status and a downstream readiness matrix;
- distinguish analytical evidence sufficiency from decision evidence sufficiency;
- constrain downstream output status where evidence is incomplete;
- perform pre-Investment Committee evidence lock / freshness checks;
- accept structured evidence requests from specialist agents;
- register material specialist-discovered evidence before it can support decision-relevant conclusions;
- preserve a clear evidence trail without turning user-facing reports into audit logs.

## 5. Non-Ownership Boundaries

The Evidence Collector Agent must not:

- issue buy / sell / hold / add / reduce / avoid actions;
- form the final investment thesis;
- decide whether valuation is attractive or unattractive;
- produce target prices, fair values, expected returns, or margin-of-safety conclusions;
- issue risk verdicts or thesis failure verdicts;
- determine portfolio role, allocation, or sizing;
- interpret market psychology, driver dominance, or market narrative strength;
- convert weak sources into strong conclusions;
- hide missing, stale, proxied, contradictory, or low-confidence evidence;
- treat user hypotheses as verified facts;
- treat user private portfolio information as public market evidence;
- use AI-generated, aggregated, or SEO-like summaries as support for material claims;
- expand scope beyond the workflow without a routing decision or structured evidence request;
- launch downstream workflows without routing or orchestration approval.

## 6. Operating Modes

The agent is a single cross-functional agent with explicit operating modes:

```text
Equity Evidence Mode
ETF Evidence Mode
Commodity Evidence Mode
Crypto Evidence Mode
Fixed Income Evidence Mode
Macro Evidence Mode
Sector / Industry Evidence Mode
Theme / Opportunity Evidence Mode
Market Positioning Evidence Mode
News / Catalysts Evidence Mode
Claim / Source Verification Mode
Readiness Check Mode
```

The evidence mode is normally assigned by the relevant intake router or workflow orchestrator. If the Evidence Collector is called directly, it may self-classify the request into a provisional mode, disclose routing uncertainty, and ask a clarifying question when mode ambiguity would materially change evidence requirements.

## 7. Evidence Profiles

Evidence depth should be proportional to workflow purpose and decision risk.

### 7.1 Verification Profile

Used for testing one claim, source, or narrow evidence question.

Output:

```text
evidence_verification_note.md
```

### 7.2 Readiness Profile

Used to determine whether a workflow or downstream agent can proceed.

Output:

```text
evidence_readiness_note.md
```

### 7.3 Standard Evidence Profile

Used for normal asset-first or specialist workflows.

Output:

```text
evidence_pack.md
```

### 7.4 Full Decision Evidence Profile

Used before final Investment Committee synthesis or any potential positive investment action.

Output:

```text
evidence_pack.md
control logs / snapshots as needed
pre-IC evidence lock
```

### 7.5 Discovery Evidence Profile

Used for theme-first, sector, structural-winner, or opportunity-discovery workflows.

Discovery evidence supports opportunity mapping, value-chain analysis, candidate discovery, and recommended next deep dives. It does not support final asset-level buy / sell actions without subsequent asset-first decision evidence.

## 8. Evidence Status

The agent uses three core evidence statuses:

```text
Complete Evidence
Limited Evidence
Blocked Evidence
```

Status is based on decision materiality, not source count.

### 8.1 Complete Evidence

All decision-critical evidence blocks are available, fresh enough, source-supported, and usable without material caveat for the relevant downstream purpose.

Practical meaning:

```text
The relevant downstream agent can produce a Complete report.
```

### 8.2 Limited Evidence

Core evidence exists, but material data is missing, stale, proxied, access-limited, contradictory, or lower-confidence. Analysis may proceed with explicit caveats and claim-strength limits.

Practical meaning:

```text
The downstream agent may proceed, but must disclose the limitation and avoid overstating conclusions.
```

### 8.3 Blocked Evidence

At least one critical evidence block is missing, unverifiable, stale, or contradictory enough that a responsible analytical or decision output cannot be produced.

Practical meaning:

```text
The downstream agent should not produce a Complete analytical conclusion and must either produce a Blocked output or request follow-up evidence.
```

## 9. Analytical vs Decision Evidence Sufficiency

The Evidence Collector must distinguish:

```text
Analytical Evidence Sufficiency
Decision Evidence Sufficiency
```

A specialist report may proceed analytically while final IC decision evidence remains Limited or Blocked. For example, an Equity Agent may have sufficient evidence to analyze business quality, while the Investment Committee remains Limited because valuation, risk, or freshness gates are incomplete.

## 10. Downstream Readiness Matrix

Each evidence pack must include readiness status for relevant downstream agents.

Example:

```text
Equity Agent: Ready
Valuation & Expectations Agent: Limited
Risk / Red Team Agent: Ready with caveat
Market Positioning Agent: Blocked
Investment Committee Agent: Limited
```

Allowed readiness statuses:

```text
Ready
Ready with Caveat
Limited
Blocked
Not Required
```

Specialist agents may challenge readiness only through the documented readiness challenge protocol. Silent override is prohibited.

## 11. Investment Committee Output Constraint

The Evidence Collector does not block the existence of a final memo, but it constrains the allowed output status.

```text
IC Readiness: Complete -> Complete Final Memo allowed
IC Readiness: Limited -> Limited Final Memo only unless limitations are resolved
IC Readiness: Blocked -> Blocked Final Memo / No Decision only
```

Positive IC actions require sufficient valuation / expectations evidence and Risk / Red Team evidence.

## 12. Pre-IC Evidence Lock

Before Investment Committee synthesis, Evidence Collector should perform a final evidence lock.

Evidence lock fields:

```text
Evidence Lock Status:
Lock Timestamp:
Evidence Pack Reviewed:
Specialist Evidence Additions Registered:
Market Data Freshness:
News / Catalyst Freshness:
Valuation-Sensitive Data Freshness:
Open Missing Data:
Open Contradictions:
Decision Evidence Status:
Allowed IC Output Status:
Positive Action Constraints:
```

Allowed evidence lock statuses:

```text
Locked
Locked with Caveats
Refresh Required
Blocked
```

## 13. Source Discipline

The agent follows:

- registry-first source use;
- controlled web fallback only for specific evidence gaps;
- source tiering;
- source type classification;
- claim-strength boundaries;
- freshness by evidence type;
- access-aware source handling;
- AI / aggregate pointer-only rule;
- candidate source lifecycle.

Weak sources may generate questions, but they must not support material investment conclusions.

## 14. Materiality Standard

Evidence materiality is classified as:

```text
Critical
Material
Contextual
Optional
Not Material
```

Materiality depends on workflow purpose, asset class, downstream use, decision risk, and claim relevance.

Critical missing evidence normally causes a Blocked or Limited status. Missing contextual evidence should not block analysis unless it becomes decision-critical in the specific workflow.

## 15. Claim Support Taxonomy

Each material claim should receive one support status:

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

Partial, proxied, stale, contradicted, unsupported, and unverifiable claims must not be treated as fully supported evidence.

## 16. Evidence Type Taxonomy

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

Each type should include what it can support, what it cannot support, and required caution.

## 17. Missing Data and Proxy Protocol

Missing data must be classified by materiality. Proxy evidence may be used only when logically relevant, clearly labeled, and bounded.

A proxy may support cautious inference or an open risk item, but it must not be presented as direct evidence or used to remove a material limitation.

## 18. Contradiction Protocol

Material source conflicts must be registered, assessed using source hierarchy, freshness, and relevance, and reflected in readiness status.

The Evidence Collector may identify and structure the conflict. It must not resolve analytical disputes that belong to specialist agents.

## 19. User-Provided and Private Data

User-provided input must be classified separately as:

```text
User Intake Context
User-Provided Evidence
User Hypothesis / Claim to Test
User Portfolio Context
User-Provided Unverified Data
```

Private user portfolio data, personal notes, brokerage information, and sensitive materials may inform relevant downstream agents, but must be labeled, minimized, and stored separately when material. They must never be treated as public market evidence.

## 20. Direct-Call Behavior

When called directly, the Evidence Collector should classify the request as one of:

```text
Full Evidence Pack
Evidence Readiness Check
Claim / Source Verification
```

It should produce a scoped artifact rather than defaulting every direct request into a full workflow.

## 21. Basic Normalization and Reconciliation

The agent may perform mechanical normalization, reconciliation, and simple derived-data calculations needed to make evidence usable.

Allowed:

- normalize currencies, units, periods, and fiscal / calendar dates;
- reconcile inconsistent source values;
- compute simple derived fields from sourced inputs;
- summarize ETF holdings weights from issuer files;
- preserve ETF holdings as-of dates, issuer source links, share-class identifiers, and fallback-source labels;
- support ETF overlap, concentration, AUM, fee, methodology, liquidity, premium / discount, and yield evidence collection without making ETF vehicle-quality judgments;
- identify mismatches between sources;
- preserve bounded data snapshots.

Prohibited:

- valuation attractiveness conclusions;
- fair value conclusions;
- target prices;
- scenario conclusions;
- expected return;
- margin-of-safety conclusions;
- investment ranking.

## 22. Relationship to Other Agents

The Evidence Collector provides the shared evidence base for:

- Equity Agent;
- ETF Agent;
- Commodity Agent;
- Crypto Agent;
- Fixed Income Agent;
- Sector & Industry Analysis Agent;
- Macro Agent;
- News & Catalysts Agent;
- Market Positioning Agent;
- Valuation & Expectations Agent;
- Risk / Red Team Agent;
- Portfolio Fit Agent;
- Investment Committee Agent.

Specialist agents may request additional evidence, add specialist-discovered evidence through the registration protocol, or challenge readiness through the documented challenge protocol.

## 23. Design Package

This agent is defined by:

```text
evidence-collector-agent-prd.md
evidence-collection-method-skill-prd.md
evidence-pack-framework.md
source-registry-framework.md
evidence-request-protocol.md
```

Detailed domain evidence playbooks should be created or expanded alongside the corresponding asset-class and specialist agents.

For Crypto Evidence Mode, the Evidence Collector should use `crypto-data-source-and-metric-framework.md` for crypto-specific source hierarchy, metric caveats, freshness tiers, access-aware fallback rules, and setup-sensitive data constraints.

For Fixed Income Evidence Mode, the Evidence Collector should use `fixed-income-agent-prd.md`, `fixed-income-framework.md`, and `fixed-income-instrument-playbooks.md` for instrument-specific evidence requirements. Decision-grade fixed income evidence normally requires both instrument terms / legal-economic structure and current market compensation. Yield alone is insufficient. If current price, yield, spread, curve, liquidity, ETF NAV premium / discount, issuer credit data, or required instrument documents are missing, stale, or inaccessible, downstream fixed-income conclusions should be Limited or Blocked according to materiality.
