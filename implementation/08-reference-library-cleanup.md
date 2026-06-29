# Reference Library Cleanup Plan

Status: Canonical reference-governance document

## 1. Purpose

Reference documents support agents and workflows. They must not act as hidden PRDs, hidden agents, or conflicting source-policy documents.

P9-REF-01 implements pragmatic reference governance: make references safe and navigable for runtime use without rewriting the whole corpus.

## 2. Reference authority boundary

References are advisory. They may provide:

- examples;
- taxonomies;
- diagnostic questions;
- playbooks;
- source overlays;
- domain nuance;
- analytical labels that do not imply portfolio action.

References must not govern:

- final decision support;
- evidence readiness;
- routing;
- IC Action;
- agent ownership;
- required workflow gates;
- canonical report schemas.

If a reference conflicts with a canonical implementation document, the canonical document governs and the conflict is a source warning.

## 3. Required reference metadata

Each active supporting reference should include a lightweight metadata header:

```text
Status: Supporting Reference
Owner:
Contributors:
Used by:
Primary reference for:
Supporting reference for:
Not responsible for: final decision; evidence readiness; routing; IC Action; agent ownership
Freshness sensitivity: Low / Medium / High
Last reviewed:
Review trigger:
Owner review needed:
Split/index status:
Canonical authority:
```

Use one primary owner, optional contributors, and explicit used-by routing. If ownership is unclear, assign a provisional owner by function and mark `Owner review needed`.

## 4. Central reference index

`implementation/reference-library-index.md` is the central operational index for reference navigation. It is not a higher authority than `implementation/01-documentation-control.md`.

If a file metadata header and the central index conflict:

- record a source warning;
- apply the stricter interpretation until synchronized;
- never choose the more permissive interpretation merely because it is convenient.

Examples of stricter interpretation:

- High freshness beats Medium freshness;
- narrower used-by beats wider used-by;
- unresolved owner conflict remains review-needed;
- registry status governs both header and index.

## 5. Keep as supporting references

| Reference group | Documents | Owner / used by |
|---|---|---|
| Asset driver maps | `asset-driver-maps.md` | Driver Dominance; used by Market Sense and asset agents. |
| Market patterns | `market-pattern-library.md`, `market-patterns/*.md` | Market Sense; used by Market Intelligence, Positioning, Macro, Risk, and asset agents as supporting context. |
| Commodity playbooks | `commodity-family-playbooks.md` | Commodity Agent. |
| Fixed income playbooks | `fixed-income-instrument-playbooks.md` | Fixed Income Agent. |
| Macro references | `macro-block-playbooks.md`, `macro-regime-framework.md`, `macro-sensitivity-framework.md`, `macro-g3-fx-regional-policy-overlay.md`, `macro-expectations-surprise-framework.md`, `macro-indicator-cadence-source-registry.md` | Macro Agent with Evidence Collector source-overlay contribution where relevant. |
| Source references | `source-registry-framework.md`, domain source overlays | Evidence Collector and relevant domain agents. |
| Market news references | `market-news-source-framework.md`, `market-materiality-filter.md` | Market Intelligence, News & Catalysts, Evidence Collector. |

## 6. Merge and cleanup rules

When a reference repeats Agent PRD, Method Skill, Workflow, Evidence, or Report Schema content:

- move ownership, inputs, outputs, and gates to Agent Contract;
- move procedural steps to Skill Contract;
- move final memo/report shape to IC/report schemas;
- move evidence readiness and source hierarchy authority to the Evidence Layer;
- keep examples, taxonomies, labels, diagnostic questions, and playbook logic in the reference.

Do not fully rewrite references for style during P9. Target only dangerous zones: authority-like rules, decision-like labels, source hierarchy conflicts, duplicated contract blocks, and unsafe retrieval sections.

## 7. Split and index rules

Split only when size or mixed ownership creates operational ambiguity. Do not split references just for aesthetics.

Split criteria:

1. mixed domains may cause wrong retrieval;
2. mixed owners make maintenance unclear;
3. mixed authority levels make a reference look like a contract;
4. file size makes reliable retrieval unlikely;
5. conflict risk with canonical documents is high.

`market-pattern-library.md` has been converted into an index and usage guide. Detailed pattern bodies are split under `market-patterns/` by domain area.

A `Needs Split` or unindexed reference may be used only as advisory/supporting context until split/index work is complete.

## 8. Source hierarchy consolidation

Source hierarchy belongs to the Evidence Layer and Source Registry.

Domain references may specify preferred sources, source caveats, metric limitations, and freshness nuances, but they must not downgrade the central evidence standard or bypass pre-IC evidence lock.

## 9. Labels and user-facing limitations

References may contain analytical labels such as `Crowded long`, `Value-trap risk`, `Weak confirmation`, or `High Priority for Asset-Level Review`.

References must not own decision labels such as Buy, Sell, Add, Trim, Exit, Hold, Hard Avoid, or IC Action. If a reference needs similar wording, use review-oriented language and state `Boundary: Not an IC Action` where user-facing confusion is likely.

User-facing outputs should show reference limitations only when those limitations affect conclusion strength, confidence, status, or auditability.

## 10. P9 pragmatic done criteria

P9-REF-01 is complete when:

1. all active Supporting Reference and former Needs Split references have metadata headers;
2. a central reference index exists;
3. large or ambiguous references have indexes or split files, especially `market-pattern-library.md`;
4. references include canonical authority boundaries and do not override contracts;
5. dangerous decision-like labels and hidden-agent language are normalized or constrained;
6. source overlays point back to the Evidence Layer;
7. remaining imperfections are documented as warnings/future cleanup and do not block P10-QA.

## 11. QA checks

Reference QA should include:

- metadata coverage check;
- central index coverage check;
- broken-link check for split files;
- dangerous-authority keyword scan followed by meaning-based review;
- registry/header/index consistency review;
- confirmation that remaining warnings are non-blocking.

## 12. Acceptance criteria

Reference cleanup is complete when:

- each reference has owner/used-by metadata;
- large references have indexes or are split where needed;
- no reference conflicts with canonical agent contracts;
- source rules point back to Evidence Layer and Source Registry;
- P10-QA can use references without hidden source-of-truth conflicts.
