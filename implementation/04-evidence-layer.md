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
| Evidence Request Protocol | Method for specialists and IC to request missing evidence or challenge readiness. |
| Source Registry | Central source hierarchy and source-quality policy. |
| Domain overlays | Asset-specific source rules; they supplement Source Registry but do not replace it. |

## 3. Evidence model

Each material claim should be mapped to these fields:

| Field | Required values / notes |
|---|---|
| Subject identity | Ticker, instrument name, security type, exchange, currency, share class, maturity/seniority/wrapper, and timestamp where applicable. |
| Claim | The factual, analytical, model, or market-signal statement being supported. |
| Claim type | Reported Fact, Official Guidance, Market Data, Estimate/Consensus, Regulatory/Legal, News Report, Analyst Interpretation, User-Provided Context, Proxy Evidence, Model Output, Market Signal, Negative Evidence. |
| Source | Name/link/document reference, or user-provided artifact reference. |
| Source tier | Tier 1, Tier 2, Tier 3, Tier 4, Pointer-Only, Restricted, Deprecated. |
| Source date / publication date | Date or period covered by the source; separate from evidence snapshot time. |
| Source scope | Full workflow, User-Restricted, Public-Data Only, Provided-Material Only, No-Refresh, or Other Scoped Basis. |
| Freshness status | Current, Recent, Stale but Usable, Refresh Required, Event-Driven Refresh Required, Unknown. |
| Evidence snapshot time | When the evidence pack was captured; market-sensitive final outputs also require final freshness check time. |
| Support status | Supported, Partially Supported, Proxy-Supported, Contradicted, Unsupported, Not Checked, Not Found, Confirmed Absent. |
| Access status | Available, Paywalled, Inaccessible, Partial, User-Provided, Not Found. |
| Materiality | Decision-Critical, Important, Contextual, Low. |
| Proxy distance | Direct, Near Proxy, Medium Proxy, Distant Proxy, or Not Applicable. |
| Model assumptions | Decision-critical assumptions, support status, scenario/sensitivity range, and unsupported assumption limits. |
| Numeric basis | Currency, units, period, fiscal/calendar basis, and conversion assumption where relevant. |
| Negative-evidence basis | Not Checked, Not Found in reviewed sources, or Confirmed Absent from a source expected to disclose it. |
| Limitation | Missing/stale/proxy/conflicting/paywalled/scope/numeric caveat. |

Evidence fields should be complete for decision-critical and important claims. Contextual claims may be grouped when they do not affect the decision.

## 4. Source hierarchy

Default hierarchy:

1. Tier 1 - primary / official sources, including regulatory filings, audited reports, issuer materials, prospectuses, covenant documents, official statistical releases, and official exchange notices where they directly support the claim.
2. Tier 2 - recognized data providers, institutional datasets, reputable exchanges for non-official market data, consensus providers, and high-control third-party datasets.
3. Tier 3 - reputable financial media, practitioner research, expert commentary.
4. Tier 4 - commentary, social, low-control narrative sources.
5. Pointer-only - AI summaries, SEO pages, unsourced aggregators; may help find leads but must not support material claims.

Domain source frameworks may add asset-specific detail but cannot weaken this hierarchy. Domain overlays may classify asset-specific direct evidence, such as verified on-chain data for crypto network activity or exchange inventory data for commodities, but weak sources cannot become support for decision-critical claims merely because a domain prefers them.

## 5. Readiness statuses

| Readiness | Meaning | Allowed downstream behavior |
|---|---|---|
| Complete | Evidence is sufficient for requested scope. | Full specialist work and Complete IC memo allowed if other gates pass. |
| Limited | Material limitations exist but bounded conclusion is possible. | Limited specialist output, Limited ranking, `limited_ic_draft.md`, `decision_prep_memo.md`, or source-scope constrained IC output. |
| Blocked | Missing/unreliable evidence prevents requested conclusion. | Blocked output with follow-up requests only. |
| Preliminary | Early or narrow evidence sufficient only for a scan. | Quick Take, preliminary warning, or preliminary specialist output; not final decision support. |

Evidence readiness and IC action readiness are separate. A specialist analysis may be Complete for its scoped evidence while IC Action remains Limited or Blocked because other gates are missing.

## 6. Evidence behavior rules

These rules canonicalize P3-EVD-01 evidence behavior. They govern Evidence Collector, evidence packs, evidence summaries, pre-IC locks, and downstream use of evidence.

These rules are evidence-layer applications of the master output rules in `implementation/00-master-rules.md`. If wording differs on statuses, freshness, user-facing display, or artifact naming, `implementation/00-master-rules.md` governs. If source status or precedence differs, `implementation/01-documentation-control.md` governs.

| Rule ID | Decision |
|---|---|
| P3-EVD-01-01 | When evidence is incomplete but the user asks for a final conclusion, provide a useful Quick Take only as Preliminary or Limited and separate it from `IC Action Status`. |
| P3-EVD-01-02 | Conflicting sources use source hierarchy plus materiality. Decision-critical unresolved conflicts force Limited or Blocked status; low-materiality conflicts do not block. |
| P3-EVD-01-03 | Freshness depends on both request wording and claim type. Today/latest/earnings/price/news/valuation claims require current sources and timestamps; structural claims can tolerate older evidence when labeled. |
| P3-EVD-01-04 | Paywalled or inaccessible sources are pointers, not proof. They cannot support material claims until content is verified or replaced by accessible equivalent evidence. |
| P3-EVD-01-05 | User-provided files are usable only with provenance, as-of date where available, extracted-claim tracking, and sanity checks. They are not automatically authoritative. |
| P3-EVD-01-06 | Proxy evidence is allowed with proxy distance, validity assumptions, alternative explanations, and support no stronger than Proxy-Supported or Partially Supported for decision-critical claims unless direct evidence is added. |
| P3-EVD-01-07 | Evidence depth depends on strength of conclusion. Quick Takes need preliminary evidence; final IC action requires evidence lock plus relevant valuation, risk, lead-analysis, and implementation gates. |
| P3-EVD-01-08 | Early red flags may be surfaced before full workflow completion as Preliminary Red Flag or Specialist Warning, with `Boundary: Not an IC Action`. |
| P3-EVD-01-09 | Evidence mapping is materiality-based. Decision-critical claims require explicit source, freshness, and support status; contextual claims may use grouped evidence. |
| P3-EVD-01-10 | IC must not invent missing facts. New decision-critical factual needs require a targeted Evidence Request and updated evidence status before final synthesis. |
| P3-EVD-01-11 | User-restricted source scopes are respected but marked `Limited by source scope`; full IC action is prohibited if excluded sources or checks are decision-critical. |
| P3-EVD-01-12 | Distinguish base facts from event updates. Older official sources can support historical facts, while newer events can trigger Refresh Required, Event-Driven Refresh Required, Limited, or Blocked status for forward-looking claims. |
| P3-EVD-01-13 | Multi-asset comparison and ranking require evidence parity / comparability status. Uneven evidence permits only Preliminary or Limited ranking, not final IC selection. |
| P3-EVD-01-14 | Evidence packs use snapshot time plus final freshness check for market-sensitive strong conclusions. Material events found during the final check trigger targeted refresh or status downgrade. |
| P3-EVD-01-15 | Source Registry is the authority; domain overlays refine source classification but cannot weaken evidence discipline. Conflicts become source issues or pending decisions. |
| P3-EVD-01-16 | Short answers are allowed, but a status line, main blocker, and final-action boundary cannot be removed for action-oriented financial questions. |
| P3-EVD-01-17 | Specialist verdict strength is constrained by evidence status. Limited evidence can produce a Preliminary or Limited Specialist Verdict but cannot pass a full IC gate. |
| P3-EVD-01-18 | User-facing evidence display is layered: short Evidence Status Summary, decision-critical gaps/conflicts, key sources, and appendix/detail availability. |
| P3-EVD-01-19 | A source must support the exact claim. Related sources may support only Partially Supported, Analyst Interpretation, or Proxy-Supported claims; overclaiming must be rewritten. |
| P3-EVD-01-20 | Absence of found evidence is not proof of absence. Use Not Checked, Not Found, or Confirmed Absent depending on the search and source duty to disclose. |
| P3-EVD-01-21 | Rumors, social posts, and unconfirmed reports may be Market Signals or Unverified Catalysts but not factual support for material claims. |
| P3-EVD-01-22 | User-requested shortcuts may reduce workflow depth only by downgrading status to Preliminary or Limited; they cannot create Complete Final Memo or positive IC Action. |
| P3-EVD-01-23 | Model outputs are not reported facts. Their support depends on decision-critical assumption support, sensitivity range, and scenario quality. |
| P3-EVD-01-24 | Ambiguous ticker, listing, instrument, share class, maturity, currency, or wrapper requires safe default plus identity check when obvious, or clarification when material. |
| P3-EVD-01-25 | Currency, units, period, fiscal/calendar basis, and conversion assumptions must be normalized for decision-critical calculations; otherwise those outputs are Limited. |

## 7. Evidence pack output template

Evidence packs should be compact structured artifacts. They are not final reports and must not include final IC Actions.

Minimum evidence pack shape:

```markdown
# Evidence Pack - [Subject]

- Artifact Type: Supporting Evidence Pack
- Owner: Evidence Collector
- Final / Supporting: Supporting
- Analysis Status:
- IC Action Status:
- Supersedes:
- Superseded By:
- Subject identity:
- Request / source scope:
- Evidence snapshot time:
- Final freshness check time, if required:
- Evidence readiness: Complete | Limited | Blocked | Preliminary
- Allowed downstream output:
- Key limitations:

## Claim support matrix
| Claim | Claim type | Materiality | Source / tier | Source date | Freshness | Support status | Access | Limitation |
|---|---|---|---|---|---|---|---|---|

## Conflict register
| Claim | What conflicts | Why it matters | Source hierarchy treatment | Materiality | Current treatment | Impact on Analysis Status | Impact on IC Action Status | Resolution needed |
|---|---|---|---|---|---|---|---|---|

## Missing / weak evidence register
| Needed evidence | Why it matters | Materiality | Needed freshness | Suggested source type | Consequence if unavailable |
|---|---|---|---|---|---|

## Source and scope notes
- Paywalled / inaccessible pointers:
- User-provided sources and sanity checks:
- Proxy evidence and proxy distance:
- Model outputs and unsupported assumptions:
- Numeric normalization notes:
- Negative-evidence basis:
```

The `Evidence Conflict` main-answer block required by `implementation/00-master-rules.md` must use these fields when the conflict is material: what conflicts, why it matters, current treatment, impact on Analysis Status, impact on IC Action Status, and what would resolve it.

## 8. Evidence request and challenge rule

Specialists and IC may request evidence or challenge readiness only through structured protocol:

```text
Evidence Request:
- Requester:
- Owner:
- Request status: Open | In Progress | Resolved | Unavailable | Superseded
- Requested claim/data:
- Why it matters:
- Materiality:
- Needed freshness:
- Needed by / as-of need:
- Suggested source type:
- Consequence if unavailable:
- Resolution note:
```

Silent override is prohibited. If a specialist proceeds with limited evidence, it must label the limitation.

## 9. Pre-IC evidence lock

Before Investment Committee synthesis, Evidence Collector must perform a pre-IC evidence lock.

The lock must state:

- Evidence pack status.
- Subject identity and source scope.
- Evidence snapshot time and final freshness check time where market-sensitive.
- Material unsupported, contradicted, proxy-supported, or partially supported claims.
- Stale market, financial, valuation, news, or event data.
- Missing decision-critical inputs.
- Paywalled, inaccessible, or user-provided material evidence.
- Proxy evidence used and proxy distance for decision-critical claims.
- Contradictions unresolved and their materiality.
- Model outputs with unsupported or sensitivity-driving assumptions.
- Normalization issues for currency, units, period, fiscal/calendar basis, or conversions.
- Negative-evidence limits, including Not Checked, Not Found, or Confirmed Absent.
- Required targeted evidence requests.
- Allowed IC output: `final_investment_memo.md`, `limited_ic_draft.md`, `decision_prep_memo.md`, or `evidence_gap_memo.md`, depending on gate readiness and evidence status.

IC must not introduce new factual claims that are absent from the evidence pack or specialist reports. If new facts are required, IC must issue a targeted Evidence Request, wait for refreshed evidence status, or produce a Limited/Blocked memo.

## 10. User-facing evidence UX

Evidence should constrain outputs without overwhelming them.

User-facing reports should include:

- Evidence Status Summary.
- Main decision-critical evidence gaps, conflicts, freshness limits, and source-scope limits.
- Key sources, usually the most important 3-7 sources for the conclusion.
- Status line for concise answers when the user asks for "just answer."
- Appendix/detail availability for the full evidence pack.

Full evidence packs remain structured workflow artifacts. Main reports should not become raw evidence databases unless the user requests full detail.

## 11. Acceptance criteria

The Evidence Layer is implemented when:

- Every final memo has an evidence readiness status.
- Material claims have support status.
- Missing, stale, paywalled, inaccessible, proxy, user-provided, contradictory, or weak evidence is visible.
- Source Registry is the default source hierarchy.
- Domain source rules are overlays, not competing policies.
- Pre-IC lock constrains final output status and allowed IC output.
- `P3-EVD-01-01` through `P3-EVD-01-25` are present with no gaps.
- `implementation/09-system-acceptance-qa.md` contains matching P3-EVD-01 QA coverage.
