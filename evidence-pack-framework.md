# Evidence Pack Framework

## 1. Purpose

`evidence_pack.md` is the shared claim-support evidence artifact for a workflow. It is not a source dump.

The evidence pack should show:

- what material claims are supported;
- what evidence supports each claim;
- what source type and source tier support the claim;
- what is missing, stale, proxied, contradicted, or inaccessible;
- which downstream agents can responsibly proceed;
- what type of final output the evidence base can support.

## 2. Standard Structure

```text
1. Evidence Pack Header
2. Evidence Readiness Summary
3. Downstream Readiness Matrix
4. Key Supported Claims
5. Claim Support Map
6. Evidence by Analytical Area
7. Missing / Stale / Proxied Evidence
8. Contradictions and Unresolved Evidence Conflicts
9. Source Quality and Access Notes
10. Downstream Evidence Handoff Blocks
11. Evidence Requests and Refresh Notes
12. Source Register Appendix
13. Data Snapshot Appendix, if applicable
```

## 3. Evidence Pack Header

```text
Target:
Workflow:
Evidence Mode:
Evidence Profile:
Routing Source:
Prepared Date:
Prepared By:
Market Data As-of:
Evidence Status:
Analytical Evidence Status:
Decision Evidence Status:
Allowed IC Output Status:
```

## 4. Evidence Readiness Summary

The readiness summary should be concise and practical.

Template:

```text
Overall Evidence Status:
Primary Supported Areas:
Primary Limitations:
Critical Missing Data:
Refresh Required:
Practical Meaning:
```

Avoid bare labels. If the status is Limited or Blocked, explain what that practically prevents.

## 5. Downstream Readiness Matrix

Template:

```text
Agent / Module:
Readiness Status:
Practical Meaning:
Key Supported Claims:
Key Limitations:
Required Follow-up:
```

Allowed readiness statuses:

```text
Ready
Ready with Caveat
Limited
Blocked
Not Required
```

## 6. Key Supported Claims

Include only material claims that downstream agents may use.

Avoid broad investment conclusions such as:

```text
The stock is attractive.
Risks are manageable.
Valuation is reasonable.
```

Prefer bounded evidence claims such as:

```text
The latest filing confirms the company has no material net debt position.
Consensus estimates are unavailable from a high-quality source in the current evidence pack.
Recent regulatory news is material to the risk review.
```

## 7. Claim Support Map

Template:

```text
Claim:
Support Status:
Evidence:
Evidence Type:
Source Tier:
Source Date:
Accessed Date:
Data Period:
Freshness Requirement:
Freshness Status:
Materiality:
Claim Strength:
Limitations:
Usable By:
Cannot Support:
```

Support statuses:

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

## 8. Evidence by Analytical Area

Use relevant sections only:

```text
Instrument Identity
User Intake Context
Market Data
Company / Issuer / Protocol Evidence
Financials / Fundamentals
Valuation Inputs
Sector / Industry
News / Catalysts
Macro
Market Positioning
Risk-Relevant Evidence
Portfolio-Relevant Evidence
Private User Context Reference
```

## 9. Missing / Stale / Proxied Evidence

Template:

```text
Evidence Gap:
Materiality:
Why It Matters:
Source Attempted:
Reason Unavailable:
Proxy Used:
Proxy Source:
Proxy Logic:
Proxy Limitations:
Effect on Analytical Evidence:
Effect on Decision Evidence:
Required Follow-up:
```

Missing data should not be buried. If the missing evidence affects readiness, say so directly.

## 10. Contradictions and Unresolved Evidence Conflicts

Template:

```text
Evidence Conflict:
Sources Involved:
Nature of Conflict:
Source Hierarchy Assessment:
Freshness Assessment:
Materiality:
Current Treatment:
Readiness Impact:
Follow-up Needed:
```

Unresolved material contradictions should remain visible to downstream agents and the Investment Committee.

## 11. Source Quality and Access Notes

Include when applicable:

```text
Preferred Sources Unavailable:
Paywalled Sources:
Fallback Sources:
Pointer-Only Sources:
Source Tier Constraints:
Registry Candidates:
Deprecated / Rejected Sources:
```

## 12. Downstream Evidence Handoff Blocks

The evidence pack should remain the single source of truth while giving each downstream agent a scoped handoff.

### 12.1 Equity Agent Handoff

```text
Usable Claims:
Key Evidence:
Missing / Proxied Evidence:
Readiness:
Required Caution:
```

### 12.2 Valuation & Expectations Agent Handoff

```text
Usable Valuation Inputs:
Market Data As-of:
Estimate / Consensus Availability:
Missing Valuation-Critical Evidence:
Readiness:
Required Caution:
```

### 12.3 Risk / Red Team Agent Handoff

```text
Thesis-Critical Evidence:
Open Risk Evidence Gaps:
Contradictions:
Proxy-Supported Claims:
Readiness:
Required Caution:
```

### 12.4 Macro Agent Handoff

```text
Macro-Relevant Claims:
Key Macro Data:
Data Freshness:
Missing / Stale Macro Evidence:
Readiness:
Required Caution:
```

### 12.5 News & Catalysts Agent Handoff

```text
Recent Events Identified:
News Check Window:
Active Carryover Events:
Upcoming Catalyst Window:
Material Catalyst Evidence:
Event Status Labels:
Source / Date Confidence:
Negative News Check Boundaries:
Source Conflicts / Unconfirmed Claims:
Refresh Required:
Readiness:
Required Caution:
```

### 12.6 Market Positioning Agent Handoff

```text
Consensus / Expectations Evidence:
Revision / Ratings Evidence:
Ownership / Holder-Base Evidence:
Flow Evidence:
Short Interest / Borrow Evidence:
Options / Volatility Evidence:
Narrative / Sentiment Evidence:
Price Reaction / Volume Evidence:
Channel-Level Status:
Freshness Caveats:
Direct vs Proxy Evidence:
Unavailable Positioning Data:
Readiness:
Required Caution:
```

### 12.7 Investment Committee Handoff

```text
Decision Evidence Status:
Allowed IC Output Status:
Evidence Lock Status:
Material Caveats:
Positive Action Constraints:
Required Follow-up:
```

## 13. Evidence Requests and Refresh Notes

Include only if applicable.

Template:

```text
Requesting Agent:
Target Claim / Question:
Status:
Evidence Added:
Readiness Change:
```

## 14. Source Register Appendix

Template:

```text
Source:
URL / Location:
Source Category:
Source Tier:
Evidence Type:
Source Date:
Accessed Date:
Data Period:
Freshness Status:
Used For:
Limitations:
Registry Status:
```

## 15. Data Snapshot Appendix

Use only when decision-critical.

Each snapshot must include:

```text
File:
Dataset:
Source:
As-of Date:
Accessed Date:
Units:
Currency:
Period:
Limitations:
Used By:
```

Raw data should be bounded. The main evidence pack should stay readable.

## 16. Workflow-Specific Naming

Default asset-first and general workflows should use:

```text
evidence_pack.md
```

Workflow-specific exceptions are allowed when they improve clarity:

```text
sector_evidence_pack.md
theme_evidence_pack.md
evidence_readiness_note.md
evidence_verification_note.md
private_context_note.md
```
