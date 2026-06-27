# Traceability Matrix

Status: Canonical implementation-control document

## Purpose

This matrix maps every registered legacy document from `implementation/01-documentation-control.md` to the canonical implementation document(s) where its requirements are harvested. It records the primary destination, secondary destinations, file availability, and the remaining thematic cleanup gap.

`implementation/01-documentation-control.md` remains the source of truth for document status. This matrix reflects registry status; it does not change registry status or create new source-of-truth authority.

Current verification date: 2026-06-27.

## Coverage summary

| Check | Result |
|---|---|
| Registered legacy files covered | 74 |
| Missing registered files | None. |
| Status authority | `implementation/01-documentation-control.md` |
| Section-level traceability | Not in scope for P0-DOC-02 |
| Unregistered root Markdown handling | Listed separately; not mapped until registry review |

## Coverage table

| Legacy file | Registry status | File availability | Primary destination | Secondary destinations | Remaining gap / next cleanup |
|---|---|---|---|---|---|
| `asset-driver-maps.md` | Supporting Reference | Present | `implementation/08-reference-library-cleanup.md` | `implementation/06-agent-contracts.md`; `implementation/11-skill-contracts.md` | Driver maps need owner/used-by metadata and runtime indexing before direct use. |
| `asset-intake-router-prd.md` | Needs Merge | Present | `implementation/05-routing-and-workflows.md` | `implementation/06-agent-contracts.md` | Asset-intake branching and safe fallback details remain to normalize into workflow contracts. |
| `commodity-agent-prd.md` | Needs Merge | Present | `implementation/06-agent-contracts.md` | `implementation/11-skill-contracts.md`; `implementation/07-investment-committee-and-report-schemas.md`; `implementation/08-reference-library-cleanup.md` | Commodity family playbook details remain supporting reference material. |
| `commodity-analysis-framework.md` | Supporting Reference | Present | `implementation/11-skill-contracts.md` | `implementation/06-agent-contracts.md`; `implementation/07-investment-committee-and-report-schemas.md`; `implementation/08-reference-library-cleanup.md` | Commodity method modules and family-specific examples remain to normalize. |
| `commodity-analysis-method-skill-prd.md` | Needs Merge | Present | `implementation/11-skill-contracts.md` | `implementation/06-agent-contracts.md`; `implementation/07-investment-committee-and-report-schemas.md`; `implementation/08-reference-library-cleanup.md` | Commodity method steps and output labels remain to consolidate with playbooks. |
| `commodity-family-playbooks.md` | Supporting Reference | Present | `implementation/08-reference-library-cleanup.md` | `implementation/06-agent-contracts.md`; `implementation/11-skill-contracts.md` | Commodity family playbooks need reference ownership, indexing, and used-by metadata. |
| `crypto-agent-prd.md` | Needs Merge | Present | `implementation/06-agent-contracts.md` | `implementation/11-skill-contracts.md`; `implementation/07-investment-committee-and-report-schemas.md`; `implementation/04-evidence-layer.md` | Crypto source, on-chain metric, and risk overlays remain to normalize. |
| `crypto-analysis-framework.md` | Supporting Reference | Present | `implementation/11-skill-contracts.md` | `implementation/06-agent-contracts.md`; `implementation/07-investment-committee-and-report-schemas.md`; `implementation/04-evidence-layer.md` | Crypto-specific analysis modules and metric definitions remain to normalize. |
| `crypto-analysis-method-skill-prd.md` | Needs Merge | Present | `implementation/11-skill-contracts.md` | `implementation/06-agent-contracts.md`; `implementation/07-investment-committee-and-report-schemas.md`; `implementation/04-evidence-layer.md` | Crypto method steps and output schema details remain to consolidate. |
| `crypto-data-source-and-metric-framework.md` | Supporting Reference | Present | `implementation/04-evidence-layer.md` | `implementation/08-reference-library-cleanup.md`; `implementation/06-agent-contracts.md`; `implementation/11-skill-contracts.md` | Crypto source hierarchy, freshness, proxy, and metric overlays remain domain evidence detail. |
| `driver-dominance-analysis-skill-prd.md` | Needs Merge | Present | `implementation/11-skill-contracts.md` | `implementation/06-agent-contracts.md`; `implementation/08-reference-library-cleanup.md`; `implementation/07-investment-committee-and-report-schemas.md` | Driver dominance inputs and labels need alignment with indexed market pattern references. |
| `equity-agent-prd.md` | Needs Merge | Present | `implementation/06-agent-contracts.md` | `implementation/11-skill-contracts.md`; `implementation/07-investment-committee-and-report-schemas.md` | Equity examples and appendix-style analysis detail remain source material. |
| `equity-company-analysis-framework.md` | Supporting Reference | Present | `implementation/11-skill-contracts.md` | `implementation/06-agent-contracts.md`; `implementation/07-investment-committee-and-report-schemas.md` | Company-analysis framework modules and examples remain to normalize into skills. |
| `equity-company-analysis-method-skill-prd.md` | Needs Merge | Present | `implementation/11-skill-contracts.md` | `implementation/06-agent-contracts.md`; `implementation/07-investment-committee-and-report-schemas.md` | Equity method steps and output wording remain to consolidate. |
| `equity-deep-dive-workflow.md` | Supporting Reference | Present | `implementation/05-routing-and-workflows.md` | `implementation/06-agent-contracts.md`; `implementation/11-skill-contracts.md`; `implementation/07-investment-committee-and-report-schemas.md` | Deep-dive workflow sequencing and handoff detail remain to normalize. |
| `etf-agent-prd.md` | Needs Merge | Present | `implementation/06-agent-contracts.md` | `implementation/11-skill-contracts.md`; `implementation/07-investment-committee-and-report-schemas.md` | ETF structure, liquidity, and index-construction edge cases remain source detail. |
| `etf-analysis-framework.md` | Supporting Reference | Present | `implementation/11-skill-contracts.md` | `implementation/06-agent-contracts.md`; `implementation/07-investment-committee-and-report-schemas.md` | ETF framework modules and edge-case rules remain to normalize. |
| `etf-analysis-method-skill-prd.md` | Needs Merge | Present | `implementation/11-skill-contracts.md` | `implementation/06-agent-contracts.md`; `implementation/07-investment-committee-and-report-schemas.md` | ETF method steps and output schema details remain to consolidate. |
| `evidence-collection-method-skill-prd.md` | Needs Merge | Present | `implementation/11-skill-contracts.md` | `implementation/04-evidence-layer.md`; `implementation/07-investment-committee-and-report-schemas.md` | Evidence collection steps must stay aligned with claim support and lock rules. |
| `evidence-collector-agent-prd.md` | Needs Merge | Present | `implementation/06-agent-contracts.md` | `implementation/04-evidence-layer.md`; `implementation/07-investment-committee-and-report-schemas.md` | Evidence Collector role details must stay bounded by canonical evidence policy. |
| `evidence-pack-framework.md` | Supporting Reference | Present | `implementation/04-evidence-layer.md` | `implementation/07-investment-committee-and-report-schemas.md`; `implementation/08-reference-library-cleanup.md` | Evidence pack fields and source-display examples remain to consolidate. |
| `evidence-request-protocol.md` | Supporting Reference | Present | `implementation/04-evidence-layer.md` | `implementation/05-routing-and-workflows.md`; `implementation/07-investment-committee-and-report-schemas.md` | Evidence request handoffs and missing-data behavior remain protocol detail. |
| `final-architecture-audit.md` | Archive | Present | Excluded / not harvested | `implementation/01-documentation-control.md` | Historical audit only; do not use as source of truth. |
| `financial-statement-analysis-skill-prd.md` | Needs Merge | Present | `implementation/11-skill-contracts.md` | `implementation/06-agent-contracts.md`; `implementation/07-investment-committee-and-report-schemas.md` | Accounting adjustments, statement-analysis examples, and output wording remain to normalize. |
| `fixed-income-agent-prd.md` | Needs Merge | Present | `implementation/06-agent-contracts.md` | `implementation/11-skill-contracts.md`; `implementation/07-investment-committee-and-report-schemas.md`; `implementation/08-reference-library-cleanup.md`; `implementation/04-evidence-layer.md` | Instrument playbook and data-source details remain supporting material. |
| `fixed-income-analysis-method-skill-prd.md` | Needs Merge | Present | `implementation/11-skill-contracts.md` | `implementation/06-agent-contracts.md`; `implementation/07-investment-committee-and-report-schemas.md`; `implementation/08-reference-library-cleanup.md` | Fixed-income method steps and instrument-specific modules remain to consolidate. |
| `fixed-income-framework.md` | Supporting Reference | Present | `implementation/11-skill-contracts.md` | `implementation/06-agent-contracts.md`; `implementation/07-investment-committee-and-report-schemas.md`; `implementation/08-reference-library-cleanup.md` | Fixed-income framework modules and instrument logic remain to normalize. |
| `fixed-income-instrument-playbooks.md` | Supporting Reference | Present | `implementation/08-reference-library-cleanup.md` | `implementation/06-agent-contracts.md`; `implementation/11-skill-contracts.md` | Instrument playbooks need reference ownership, indexing, and used-by metadata. |
| `full-agent-system-build-roadmap.md` | Draft Source | Present | `IMPLEMENTATION_BACKLOG.md` | `implementation/02-canonical-architecture.md`; `implementation/13-codex-runtime-architecture.md` | Product roadmap harvested; no direct implementation authority. |
| `investment-committee-agent-prd.md` | Needs Merge | Present | `implementation/06-agent-contracts.md` | `implementation/07-investment-committee-and-report-schemas.md`; `implementation/11-skill-contracts.md`; `implementation/00-master-rules.md` | IC role boundaries and memo examples remain to align with gates and schemas. |
| `investment-committee-memo-framework.md` | Supporting Reference | Present | `implementation/07-investment-committee-and-report-schemas.md` | `implementation/00-master-rules.md`; `implementation/06-agent-contracts.md` | Memo wording examples and decision-support presentation detail remain to consolidate. |
| `investment-committee-synthesis-method-skill-prd.md` | Needs Merge | Present | `implementation/11-skill-contracts.md` | `implementation/07-investment-committee-and-report-schemas.md`; `implementation/06-agent-contracts.md`; `implementation/00-master-rules.md` | IC synthesis steps and final memo schema details remain to align. |
| `macro-agent-prd.md` | Needs Merge | Present | `implementation/06-agent-contracts.md` | `implementation/11-skill-contracts.md`; `implementation/08-reference-library-cleanup.md`; `implementation/04-evidence-layer.md` | Macro playbooks, cadence, and regime overlays remain supporting detail. |
| `macro-analysis-method-skill-prd.md` | Needs Merge | Present | `implementation/11-skill-contracts.md` | `implementation/06-agent-contracts.md`; `implementation/08-reference-library-cleanup.md`; `implementation/04-evidence-layer.md` | Macro method steps and source cadence details remain to consolidate. |
| `macro-block-playbooks.md` | Supporting Reference | Present | `implementation/08-reference-library-cleanup.md` | `implementation/06-agent-contracts.md`; `implementation/11-skill-contracts.md`; `implementation/04-evidence-layer.md` | Macro block playbooks need reference ownership, indexing, and used-by metadata. |
| `macro-expectations-surprise-framework.md` | Supporting Reference | Present | `implementation/11-skill-contracts.md` | `implementation/06-agent-contracts.md`; `implementation/04-evidence-layer.md`; `implementation/08-reference-library-cleanup.md` | Expected-vs-actual surprise logic and examples remain to normalize. |
| `macro-g3-fx-regional-policy-overlay.md` | Supporting Reference | Present | `implementation/08-reference-library-cleanup.md` | `implementation/06-agent-contracts.md`; `implementation/11-skill-contracts.md`; `implementation/04-evidence-layer.md` | G3, FX, and regional policy overlays need reference ownership and indexing. |
| `macro-indicator-cadence-source-registry.md` | Supporting Reference | Present | `implementation/04-evidence-layer.md` | `implementation/08-reference-library-cleanup.md`; `implementation/06-agent-contracts.md`; `implementation/11-skill-contracts.md` | Macro source cadence and freshness overlays remain domain evidence detail. |
| `macro-regime-framework.md` | Supporting Reference | Present | `implementation/11-skill-contracts.md` | `implementation/06-agent-contracts.md`; `implementation/08-reference-library-cleanup.md`; `implementation/04-evidence-layer.md` | Regime definitions and examples remain to normalize into skills and references. |
| `macro-sensitivity-framework.md` | Supporting Reference | Present | `implementation/11-skill-contracts.md` | `implementation/06-agent-contracts.md`; `implementation/08-reference-library-cleanup.md`; `implementation/04-evidence-layer.md` | Sensitivity mapping and scenario examples remain to normalize. |
| `market-intelligence-agent-prd.md` | Needs Merge | Present | `implementation/06-agent-contracts.md` | `implementation/11-skill-contracts.md`; `implementation/08-reference-library-cleanup.md`; `implementation/04-evidence-layer.md` | Briefing, materiality, and source details remain supporting material. |
| `market-intelligence-briefing-skill-prd.md` | Needs Merge | Present | `implementation/11-skill-contracts.md` | `implementation/06-agent-contracts.md`; `implementation/08-reference-library-cleanup.md`; `implementation/04-evidence-layer.md` | Briefing workflow and source/materiality filters remain to consolidate. |
| `market-materiality-filter.md` | Supporting Reference | Present | `implementation/11-skill-contracts.md` | `implementation/06-agent-contracts.md`; `implementation/08-reference-library-cleanup.md` | Materiality thresholds and examples remain reference-backed method detail. |
| `market-news-source-framework.md` | Supporting Reference | Present | `implementation/04-evidence-layer.md` | `implementation/08-reference-library-cleanup.md`; `implementation/06-agent-contracts.md`; `implementation/11-skill-contracts.md` | Market-news source hierarchy and freshness overlays remain domain evidence detail. |
| `market-pattern-library.md` | Needs Split | Present | `implementation/08-reference-library-cleanup.md` | `implementation/11-skill-contracts.md`; `implementation/06-agent-contracts.md` | Must be indexed/split before reliable runtime use. |
| `market-positioning-agent-prd.md` | Needs Merge | Present | `implementation/06-agent-contracts.md` | `implementation/11-skill-contracts.md`; `implementation/07-investment-committee-and-report-schemas.md`; `implementation/08-reference-library-cleanup.md` | Positioning labels, examples, and reference inputs remain to normalize. |
| `market-positioning-framework.md` | Supporting Reference | Present | `implementation/11-skill-contracts.md` | `implementation/06-agent-contracts.md`; `implementation/07-investment-committee-and-report-schemas.md`; `implementation/08-reference-library-cleanup.md` | Positioning framework labels and examples remain to consolidate. |
| `market-positioning-method-skill-prd.md` | Needs Merge | Present | `implementation/11-skill-contracts.md` | `implementation/06-agent-contracts.md`; `implementation/07-investment-committee-and-report-schemas.md` | Positioning method steps and verdict/output labels remain to align. |
| `market-sense-agent-prd.md` | Needs Merge | Present | `implementation/06-agent-contracts.md` | `implementation/11-skill-contracts.md`; `implementation/08-reference-library-cleanup.md` | Market-sense hypotheses depend on pattern library split/index work. |
| `market-sense-hypothesis-engine-skill-prd.md` | Needs Merge | Present | `implementation/11-skill-contracts.md` | `implementation/06-agent-contracts.md`; `implementation/08-reference-library-cleanup.md` | Hypothesis engine examples depend on indexed market pattern references. |
| `master-intake-router-prd.md` | Needs Merge | Present | `implementation/05-routing-and-workflows.md` | `implementation/06-agent-contracts.md` | Master intake clarification, routing, and fallback details remain to normalize. |
| `news-catalysts-agent-prd.md` | Needs Merge | Present | `implementation/06-agent-contracts.md` | `implementation/11-skill-contracts.md`; `implementation/07-investment-committee-and-report-schemas.md`; `implementation/04-evidence-layer.md` | Catalyst taxonomy, source handling, and output examples remain to normalize. |
| `news-catalysts-framework.md` | Supporting Reference | Present | `implementation/11-skill-contracts.md` | `implementation/06-agent-contracts.md`; `implementation/07-investment-committee-and-report-schemas.md`; `implementation/04-evidence-layer.md` | Catalyst framework taxonomy and evidence treatment remain to consolidate. |
| `news-catalysts-method-skill-prd.md` | Needs Merge | Present | `implementation/11-skill-contracts.md` | `implementation/06-agent-contracts.md`; `implementation/07-investment-committee-and-report-schemas.md`; `implementation/04-evidence-layer.md` | Catalyst method steps and output labels remain to align. |
| `portfolio-fit-agent-prd.md` | Needs Merge | Present | `implementation/06-agent-contracts.md` | `implementation/11-skill-contracts.md`; `implementation/07-investment-committee-and-report-schemas.md` | Portfolio-fit questionnaires and suitability examples remain source detail. |
| `portfolio-fit-framework.md` | Supporting Reference | Present | `implementation/11-skill-contracts.md` | `implementation/06-agent-contracts.md`; `implementation/07-investment-committee-and-report-schemas.md`; `implementation/08-reference-library-cleanup.md` | Portfolio-fit framework questionnaires and examples remain to normalize. |
| `portfolio-fit-method-skill-prd.md` | Needs Merge | Present | `implementation/11-skill-contracts.md` | `implementation/06-agent-contracts.md`; `implementation/07-investment-committee-and-report-schemas.md` | Portfolio-fit method steps and output wording remain to align. |
| `prd.backup-before-full-target-language-20260625.md` | Archive | Present | Excluded / not harvested | `implementation/01-documentation-control.md` | Historical backup only; do not use as source of truth. |
| `prd.md` | Draft Source | Present | `implementation/02-canonical-architecture.md` | `IMPLEMENTATION_BACKLOG.md`; `implementation/13-codex-runtime-architecture.md` | Product-level vision harvested; no direct implementation authority. |
| `risk-red-team-agent-prd.md` | Needs Merge | Present | `implementation/06-agent-contracts.md` | `implementation/11-skill-contracts.md`; `implementation/07-investment-committee-and-report-schemas.md` | Risk labels, escalation rules, and examples remain to normalize. |
| `risk-red-team-framework.md` | Supporting Reference | Present | `implementation/11-skill-contracts.md` | `implementation/06-agent-contracts.md`; `implementation/07-investment-committee-and-report-schemas.md` | Risk framework scenarios and challenge templates remain to consolidate. |
| `risk-red-team-method-skill-prd.md` | Needs Merge | Present | `implementation/11-skill-contracts.md` | `implementation/06-agent-contracts.md`; `implementation/07-investment-committee-and-report-schemas.md` | Risk method steps and verdict/output labels remain to align. |
| `sector-industry-analysis-agent-prd.md` | Needs Merge | Present | `implementation/06-agent-contracts.md` | `implementation/11-skill-contracts.md`; `implementation/07-investment-committee-and-report-schemas.md`; `implementation/05-routing-and-workflows.md` | Standalone vs embedded theme-analysis behavior remains to normalize. |
| `sector-industry-analysis-framework.md` | Supporting Reference | Present | `implementation/11-skill-contracts.md` | `implementation/06-agent-contracts.md`; `implementation/07-investment-committee-and-report-schemas.md`; `implementation/08-reference-library-cleanup.md` | Sector/industry framework modules and examples remain to consolidate. |
| `sector-industry-analysis-method-skill-prd.md` | Needs Merge | Present | `implementation/11-skill-contracts.md` | `implementation/06-agent-contracts.md`; `implementation/07-investment-committee-and-report-schemas.md`; `implementation/05-routing-and-workflows.md` | Sector/industry method steps and handoff detail remain to align. |
| `source-registry-framework.md` | Supporting Reference | Present | `implementation/04-evidence-layer.md` | `implementation/08-reference-library-cleanup.md`; `implementation/07-investment-committee-and-report-schemas.md` | Source hierarchy overlays and source-display details remain to consolidate. |
| `structural-winner-discovery-framework.md` | Supporting Reference | Present | `implementation/11-skill-contracts.md` | `implementation/06-agent-contracts.md`; `implementation/07-investment-committee-and-report-schemas.md`; `implementation/05-routing-and-workflows.md` | Discovery framework naming and theme-to-asset handoff details remain to standardize. |
| `structural-winner-discovery-method-skill-prd.md` | Needs Merge | Present | `implementation/11-skill-contracts.md` | `implementation/06-agent-contracts.md`; `implementation/07-investment-committee-and-report-schemas.md`; `implementation/05-routing-and-workflows.md` | Discovery method steps and candidate-output boundaries remain to align. |
| `structural-winners-discovery-agent-prd.md` | Needs Merge | Present | `implementation/06-agent-contracts.md` | `implementation/11-skill-contracts.md`; `implementation/07-investment-committee-and-report-schemas.md`; `implementation/05-routing-and-workflows.md` | Naming should standardize to Structural Winners Discovery; handoff detail remains. |
| `system-architecture-map.md` | Draft Source | Present | `implementation/02-canonical-architecture.md` | `implementation/00-master-rules.md`; `implementation/05-routing-and-workflows.md`; `implementation/13-codex-runtime-architecture.md` | Architecture harvested; no direct implementation authority. |
| `theme-opportunity-intake-router-prd.md` | Needs Merge | Present | `implementation/05-routing-and-workflows.md` | `implementation/06-agent-contracts.md` | Theme intake branching and discovery fallback details remain to normalize. |
| `valuation-expectations-agent-prd.md` | Needs Merge | Present | `implementation/06-agent-contracts.md` | `implementation/11-skill-contracts.md`; `implementation/07-investment-committee-and-report-schemas.md` | Sector-specific valuation modules and labels remain source detail. |
| `valuation-expectations-framework.md` | Supporting Reference | Present | `implementation/11-skill-contracts.md` | `implementation/06-agent-contracts.md`; `implementation/07-investment-committee-and-report-schemas.md` | Valuation framework modules and sector-specific examples remain to normalize. |
| `valuation-expectations-method-skill-prd.md` | Needs Merge | Present | `implementation/11-skill-contracts.md` | `implementation/06-agent-contracts.md`; `implementation/07-investment-committee-and-report-schemas.md` | Valuation method steps and output labels remain to align. |

## Out of scope / intentionally not mapped

| Category / file | Reason | Handling |
|---|---|---|
| `implementation/*.md` canonical documents | Canonical implementation layer, not legacy corpus. | Do not map to themselves; use as destinations only. |
| `IMPLEMENTATION_BACKLOG.md` | Canonical phase-level backlog. | Destination for harvested roadmap/scope only. |
| `TASKS.md` | Operational work register. | Tracks task status; not part of legacy traceability. |
| `.scratch_macro_prompts/` files | Scratch / temporary prompt material. | Out of scope unless explicitly registered later. |
| `НАПОМИНАНИЕ.md` | Explicitly excluded by registry / user instruction. | Do not include in the main matrix. |

## Unregistered files found

| File | Availability | Handling |
|---|---|---|
| `НАПОМИНАНИЕ.md` | Present | Intentionally excluded by registry / user instruction; not mapped until registry changes. |

## Coverage and handling rules

- `implementation/01-documentation-control.md` is the only source of truth for registry status.
- If registry status and this matrix ever differ, registry status governs and this matrix should be corrected.
- Registered files that are physically missing remain in the matrix with `File availability = Missing` and an explicit gap.
- Files present in the repository but absent from the registry are not added to the main matrix; list them under `Unregistered files found` until registry review.
- Archive / backup / audit files remain visible, but use `Primary destination = Excluded / not harvested` and must not be used as source of truth.
- Draft Source documents may show where product or architecture ideas were harvested, but they have no direct implementation authority.
- `Needs Split` documents are advisory reference material until indexed or split; they do not override canonical contracts.
- Canonical documents always override conflicting legacy content; conflicts should be recorded as warnings or thematic gaps, not silently applied.
- Primary destination identifies the main canonical home. Secondary destinations preserve important cross-layer relationships without creating multiple status authorities.
- `Remaining gap / next cleanup` is intentionally thematic, not section-level; detailed normalization belongs to later implementation stages.

## Acceptance use

Before implementing an agent, workflow, skill, evidence policy, report, or reference cleanup, use this matrix to identify:

1. the canonical build destination;
2. secondary canonical layers that must remain aligned;
3. whether the source is present, missing, archived, draft, reference, merge-needed, or split-needed;
4. the thematic cleanup still expected in future stages.