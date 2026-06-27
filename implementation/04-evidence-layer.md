# Evidence Layer Contract

Status: Canonical evidence implementation contract

## 1. Purpose

The Evidence Layer controls source quality, claim support, freshness, missing data, contradictions, proxy evidence, and readiness for downstream analysis.

Evidence Collector is the system's evidence control tower. It does not make valuation, risk, portfolio, or final investment decisions.

## 2. Canonical evidence components

| Component | Role |
|---|---|
| Evidence Collector Agent | Coordinates evidence collection, evidence pack, readiness, and evidence lock. |
| Evidence Collection Skill | Repeatable method for collecting, classifying, and validating evidence. |
| Evidence Pack | Structured repository of sources, claims, support status, freshness, limitations, and handoffs. |
| Evidence Request Protocol | Method for specialists to request missing evidence or challenge readiness. |
| Source Registry | Central source hierarchy and source-quality policy. |
| Domain overlays | Asset-specific source rules; they supplement Source Registry but do not replace it. |

## 3. Evidence model

Each material claim should be mapped to these fields:

| Field | Required values / notes |
|---|---|
| Claim | The factual or analytical statement being supported. |
| Claim type | Reported Fact, Official Guidance, Market Data, Estimate/Consensus, Regulatory/Legal, News Report, Analyst Interpretation, User-Provided Context, Proxy Evidence, Model Output. |
| Source | Name/link/document reference. |
| Source tier | Tier 1, Tier 2, Tier 3, Tier 4, Pointer-Only, Restricted, Deprecated. |
| Freshness status | Current, Recent, Stale but Usable, Refresh Required, Event-Driven Refresh Required, Unknown. |
| Support status | Supported, Partially Supported, Proxy-Supported, Contradicted, Unsupported, Not Checked. |
| Access status | Available, Paywalled, Inaccessible, Partial, User-Provided, Not Found. |
| Materiality | Decision-Critical, Important, Contextual, Low. |
| Limitation | Missing/stale/proxy/conflicting caveat. |

## 4. Source hierarchy

Default hierarchy:

1. Tier 1 — primary / official sources.
2. Tier 2 — recognized data providers, institutional sources, reputable exchanges, filings, issuer materials.
3. Tier 3 — reputable financial media, practitioner research, expert commentary.
4. Tier 4 — commentary, social, low-control narrative sources.
5. Pointer-only — AI summaries, SEO pages, unsourced aggregators; may help find leads but must not support material claims.

Domain source frameworks may add asset-specific detail but cannot weaken this hierarchy.

## 5. Readiness statuses

| Readiness | Meaning | Allowed downstream behavior |
|---|---|---|
| Complete | Evidence is sufficient for requested scope. | Full specialist work and Complete IC memo allowed if other gates pass. |
| Limited | Material limitations exist but bounded conclusion is possible. | Limited specialist output or Limited Final Memo. |
| Blocked | Missing/unreliable evidence prevents requested conclusion. | Blocked output with follow-up requests only. |
| Preliminary | Early or narrow evidence sufficient only for a scan. | Preliminary output; not final decision support. |

## 6. Pre-IC evidence lock

Before Investment Committee synthesis, Evidence Collector must perform a pre-IC evidence lock.

The lock must state:
- Evidence pack status.
- Material unsupported claims.
- Stale market or financial data.
- Missing decision-critical inputs.
- Proxy evidence used.
- Contradictions unresolved.
- Allowed IC output: Complete Final Memo, Limited Final Memo, or Blocked Final Memo.

## 7. Evidence request and challenge rule

Specialists may request evidence or challenge readiness only through structured protocol:

```text
Evidence Request:
- Requested claim/data:
- Why it matters:
- Materiality:
- Needed freshness:
- Suggested source type:
- Consequence if unavailable:
```

Silent override is prohibited. If a specialist proceeds with limited evidence, it must label the limitation.

## 8. IC fact discipline

The Investment Committee Agent must not introduce new factual claims that are absent from the evidence pack or specialist reports unless the workflow explicitly triggers a targeted evidence refresh.

If new facts are required, IC must produce a follow-up evidence request or Limited/Blocked memo rather than improvising.

## 9. Acceptance criteria

The Evidence Layer is implemented when:
- Every final memo has an evidence readiness status.
- Material claims have support status.
- Missing/stale/paywalled/proxy data is visible.
- Source Registry is the default source hierarchy.
- Domain source rules are overlays, not competing policies.
- Pre-IC lock constrains final output status.
