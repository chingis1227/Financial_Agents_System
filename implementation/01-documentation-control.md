# Documentation Control Registry

Status: Canonical implementation-control document

## Purpose

This document controls which legacy PRD / Markdown documents are active implementation inputs, which are references, which require consolidation, and which are excluded from active implementation.

The canonical implementation layer is `IMPLEMENTATION_BACKLOG.md` plus the canonical implementation documents explicitly listed below. Files located under `implementation/` are not automatically canonical unless this registry lists them as canonical. Legacy PRD and draft-source files have been removed from the project root and retained under `archive/legacy-prd/`; active advisory references live under `references/`. `НАПОМИНАНИЕ.md` is intentionally excluded from this registry by user instruction.

## Status definitions

| Status | Meaning |
|---|---|
| Canonical | Active source of truth for implementation. |
| Supporting Reference | Usable reference, playbook, source policy, or schema support. It does not override canonical contracts. |
| Draft Source | Useful source material, but not directly executable as implementation truth. |
| Archive | Historical, backup, or audit artifact. Do not use as source of truth. |
| Needs Merge | Contains useful requirements that must be merged into a canonical contract. |
| Needs Split | Too broad or large for direct operational use; requires indexing or modularization. |

## Canonical implementation documents

| Document | Status | Role |
|---|---|---|
| `IMPLEMENTATION_BACKLOG.md` | Canonical | Main phase-level implementation backlog. |
| `implementation/00-master-rules.md` | Canonical | Master statuses, gates, output standards, confidence, source display, style, artifact naming. |
| `implementation/01-documentation-control.md` | Canonical | Active document registry and status control. |
| `implementation/02-canonical-architecture.md` | Canonical | Architecture, ownership, orchestration, statuses, labels. |
| `implementation/03-contract-templates.md` | Canonical | Templates for agents, skills, workflows, and reports. |
| `implementation/04-evidence-layer.md` | Canonical | Evidence model, source hierarchy, readiness, pre-IC lock. |
| `implementation/05-routing-and-workflows.md` | Canonical | Routing and workflow contracts. |
| `implementation/06-agent-contracts.md` | Canonical | Canonical agent contracts. |
| `implementation/07-investment-committee-and-report-schemas.md` | Canonical | IC contract and report schemas. |
| `implementation/08-reference-library-cleanup.md` | Canonical | Reference ownership and cleanup rules. |
| `implementation/09-system-acceptance-qa.md` | Canonical | Acceptance scenarios and QA checks. |
| `implementation/10-traceability-matrix.md` | Canonical | Legacy file coverage and canonical destinations. |
| `implementation/11-skill-contracts.md` | Canonical | Canonical method-skill contracts. |
| `implementation/13-codex-runtime-architecture.md` | Canonical | Codex-native runtime architecture, `AGENTS.md`, repo skills, custom subagents, and workflow runbook conventions. |
| `implementation/14-language-and-style.md` | Canonical | User-facing language selection, Russian language policy, and investment-analytical presentation style. |

## Implementation governance records

| Document | Record type | Role |
|---|---|---|
| `TASKS.md` | Operational control register | Active work queue and task status tracker. It controls what is currently open or done; `IMPLEMENTATION_BACKLOG.md` governs phase meaning and scope when they differ. |
| `implementation/12-decision-log.md` | Supporting decision record | Decision history and rationale. It explains why documentation-control rules were chosen, but it does not override canonical implementation documents. |
| `implementation/remaining-requirements.md` | Supporting residual-requirement register | Candidate requirement inventory after root legacy cleanup. It records residual items to evaluate and may not override domain canonical documents unless an item is promoted through canonical change control. |
| `.codex/runtime-readiness-report.md` | Supporting operational validation record | P1A-CODEX-02 generated-runtime readiness, structural gate, validation, and idempotency record. It does not override canonical implementation documents. |
| `implementation/runtime-baseline-report.md` | Supporting operational validation record | Session 01 baseline audit record for runtime hardening and uncommitted-state provenance. It does not override canonical implementation documents. |
| `implementation/reference-library-index.md` | Supporting operational index | P9-REF-01 reference-library navigation, owner/used-by metadata, freshness tier, split/index state, and non-blocking review notes. It does not override the registry or canonical implementation documents. |
| `implementation/p10-qa-execution-report.md` | Supporting operational validation record | P10-QA-01 Pareto Gate, Full Regression, Live-Smoke, structural validation, source issues, and final closure evidence. It does not override canonical implementation documents. |
| `implementation/final-system-audit-report.md` | Supporting operational validation record | Session 11 final system audit for root cleanup, workflow docs, agents, skills, handoff artifacts, README prompts, QA, Microsoft smoke test, blockers, warnings, residual tasks, and regular-use readiness. It does not override canonical implementation documents. |
| `workflows/equity_full_cycle.md` | Runtime runbook | Executable Equity Full Cycle runbook. It is subordinate to canonical implementation documents and must not override `implementation/00-master-rules.md`, `implementation/05-routing-and-workflows.md`, `implementation/06-agent-contracts.md`, `implementation/07-investment-committee-and-report-schemas.md`, or `implementation/13-codex-runtime-architecture.md`. |
| `workflows/etf_full_cycle.md` | Runtime runbook | Executable ETF Full Cycle runbook. It is subordinate to canonical implementation documents and must not override master rules, routing contracts, agent contracts, IC schemas, or Codex runtime architecture. |
| `workflows/commodity_full_cycle.md` | Runtime runbook | Executable Commodity Full Cycle runbook. It is subordinate to canonical implementation documents and must not override master rules, routing contracts, agent contracts, IC schemas, or Codex runtime architecture. |
| `workflows/crypto_full_cycle.md` | Runtime runbook | Executable Crypto Full Cycle runbook. It is subordinate to canonical implementation documents and must not override master rules, routing contracts, agent contracts, IC schemas, or Codex runtime architecture. |
| `workflows/fixed_income_full_cycle.md` | Runtime runbook | Executable Fixed Income Full Cycle runbook. It is subordinate to canonical implementation documents and must not override master rules, routing contracts, agent contracts, IC schemas, or Codex runtime architecture. |
| `workflows/multi_asset_full_agent_workflow.md` | Runtime runbook | Executable multi-asset comparison runbook. It is subordinate to canonical implementation documents and must not override master rules, routing contracts, agent contracts, IC schemas, or Codex runtime architecture. |
| `workflows/handoff_artifact_standard.md` | Runtime standard | Mandatory handoff artifact field standard for Full Cycle and Delegated Full Agent Workflow runs. It is subordinate to canonical implementation documents and must not override master status/gate rules, evidence rules, agent contracts, routing contracts, IC schemas, or Codex runtime architecture. |

## Legacy document registry

This registry records the post-cleanup location and authority of former root-level legacy Markdown files. Original root-level paths are retired; use the current paths below. Archived files preserve provenance only. Residual candidate requirements from retired PRD / draft sources are centralized in `implementation/remaining-requirements.md`.

| Current document | Original root document | Status | Implementation role |
|---|---|---|---|
| `references/asset-driver-maps.md` | `asset-driver-maps.md` | Supporting Reference | Advisory reference/playbook/source-overlay material; subordinate to canonical implementation documents. |
| `archive/legacy-prd/asset-intake-router-prd.md` | `asset-intake-router-prd.md` | Archive | Retired legacy source; residual candidate requirements are captured in `implementation/remaining-requirements.md` and must be promoted through canonical change control before active use. |
| `archive/legacy-prd/commodity-agent-prd.md` | `commodity-agent-prd.md` | Archive | Retired legacy source; residual candidate requirements are captured in `implementation/remaining-requirements.md` and must be promoted through canonical change control before active use. |
| `references/commodity-analysis-framework.md` | `commodity-analysis-framework.md` | Supporting Reference | Advisory reference/playbook/source-overlay material; subordinate to canonical implementation documents. |
| `archive/legacy-prd/commodity-analysis-method-skill-prd.md` | `commodity-analysis-method-skill-prd.md` | Archive | Retired legacy source; residual candidate requirements are captured in `implementation/remaining-requirements.md` and must be promoted through canonical change control before active use. |
| `references/commodity-family-playbooks.md` | `commodity-family-playbooks.md` | Supporting Reference | Advisory reference/playbook/source-overlay material; subordinate to canonical implementation documents. |
| `archive/legacy-prd/crypto-agent-prd.md` | `crypto-agent-prd.md` | Archive | Retired legacy source; residual candidate requirements are captured in `implementation/remaining-requirements.md` and must be promoted through canonical change control before active use. |
| `references/crypto-analysis-framework.md` | `crypto-analysis-framework.md` | Supporting Reference | Advisory reference/playbook/source-overlay material; subordinate to canonical implementation documents. |
| `archive/legacy-prd/crypto-analysis-method-skill-prd.md` | `crypto-analysis-method-skill-prd.md` | Archive | Retired legacy source; residual candidate requirements are captured in `implementation/remaining-requirements.md` and must be promoted through canonical change control before active use. |
| `references/crypto-data-source-and-metric-framework.md` | `crypto-data-source-and-metric-framework.md` | Supporting Reference | Advisory reference/playbook/source-overlay material; subordinate to canonical implementation documents. |
| `archive/legacy-prd/driver-dominance-analysis-skill-prd.md` | `driver-dominance-analysis-skill-prd.md` | Archive | Retired legacy source; residual candidate requirements are captured in `implementation/remaining-requirements.md` and must be promoted through canonical change control before active use. |
| `archive/legacy-prd/equity-agent-prd.md` | `equity-agent-prd.md` | Archive | Retired legacy source; residual candidate requirements are captured in `implementation/remaining-requirements.md` and must be promoted through canonical change control before active use. |
| `references/equity-company-analysis-framework.md` | `equity-company-analysis-framework.md` | Supporting Reference | Advisory reference/playbook/source-overlay material; subordinate to canonical implementation documents. |
| `archive/legacy-prd/equity-company-analysis-method-skill-prd.md` | `equity-company-analysis-method-skill-prd.md` | Archive | Retired legacy source; residual candidate requirements are captured in `implementation/remaining-requirements.md` and must be promoted through canonical change control before active use. |
| `references/equity-deep-dive-workflow.md` | `equity-deep-dive-workflow.md` | Supporting Reference | Advisory reference/playbook/source-overlay material; subordinate to canonical implementation documents. |
| `archive/legacy-prd/etf-agent-prd.md` | `etf-agent-prd.md` | Archive | Retired legacy source; residual candidate requirements are captured in `implementation/remaining-requirements.md` and must be promoted through canonical change control before active use. |
| `references/etf-analysis-framework.md` | `etf-analysis-framework.md` | Supporting Reference | Advisory reference/playbook/source-overlay material; subordinate to canonical implementation documents. |
| `archive/legacy-prd/etf-analysis-method-skill-prd.md` | `etf-analysis-method-skill-prd.md` | Archive | Retired legacy source; residual candidate requirements are captured in `implementation/remaining-requirements.md` and must be promoted through canonical change control before active use. |
| `archive/legacy-prd/evidence-collection-method-skill-prd.md` | `evidence-collection-method-skill-prd.md` | Archive | Retired legacy source; residual candidate requirements are captured in `implementation/remaining-requirements.md` and must be promoted through canonical change control before active use. |
| `archive/legacy-prd/evidence-collector-agent-prd.md` | `evidence-collector-agent-prd.md` | Archive | Retired legacy source; residual candidate requirements are captured in `implementation/remaining-requirements.md` and must be promoted through canonical change control before active use. |
| `references/evidence-pack-framework.md` | `evidence-pack-framework.md` | Supporting Reference | Advisory reference/playbook/source-overlay material; subordinate to canonical implementation documents. |
| `references/evidence-request-protocol.md` | `evidence-request-protocol.md` | Supporting Reference | Advisory reference/playbook/source-overlay material; subordinate to canonical implementation documents. |
| `archive/legacy-prd/final-architecture-audit.md` | `final-architecture-audit.md` | Archive | Historical backup/audit artifact; retained for provenance only and never active source of truth. |
| `archive/legacy-prd/financial-statement-analysis-skill-prd.md` | `financial-statement-analysis-skill-prd.md` | Archive | Retired legacy source; residual candidate requirements are captured in `implementation/remaining-requirements.md` and must be promoted through canonical change control before active use. |
| `archive/legacy-prd/fixed-income-agent-prd.md` | `fixed-income-agent-prd.md` | Archive | Retired legacy source; residual candidate requirements are captured in `implementation/remaining-requirements.md` and must be promoted through canonical change control before active use. |
| `archive/legacy-prd/fixed-income-analysis-method-skill-prd.md` | `fixed-income-analysis-method-skill-prd.md` | Archive | Retired legacy source; residual candidate requirements are captured in `implementation/remaining-requirements.md` and must be promoted through canonical change control before active use. |
| `references/fixed-income-framework.md` | `fixed-income-framework.md` | Supporting Reference | Advisory reference/playbook/source-overlay material; subordinate to canonical implementation documents. |
| `references/fixed-income-instrument-playbooks.md` | `fixed-income-instrument-playbooks.md` | Supporting Reference | Advisory reference/playbook/source-overlay material; subordinate to canonical implementation documents. |
| `archive/legacy-prd/full-agent-system-build-roadmap.md` | `full-agent-system-build-roadmap.md` | Archive | Retired legacy source; residual candidate requirements are captured in `implementation/remaining-requirements.md` and must be promoted through canonical change control before active use. |
| `archive/legacy-prd/investment-committee-agent-prd.md` | `investment-committee-agent-prd.md` | Archive | Retired legacy source; residual candidate requirements are captured in `implementation/remaining-requirements.md` and must be promoted through canonical change control before active use. |
| `references/investment-committee-memo-framework.md` | `investment-committee-memo-framework.md` | Supporting Reference | Advisory reference/playbook/source-overlay material; subordinate to canonical implementation documents. |
| `archive/legacy-prd/investment-committee-synthesis-method-skill-prd.md` | `investment-committee-synthesis-method-skill-prd.md` | Archive | Retired legacy source; residual candidate requirements are captured in `implementation/remaining-requirements.md` and must be promoted through canonical change control before active use. |
| `archive/legacy-prd/macro-agent-prd.md` | `macro-agent-prd.md` | Archive | Retired legacy source; residual candidate requirements are captured in `implementation/remaining-requirements.md` and must be promoted through canonical change control before active use. |
| `archive/legacy-prd/macro-analysis-method-skill-prd.md` | `macro-analysis-method-skill-prd.md` | Archive | Retired legacy source; residual candidate requirements are captured in `implementation/remaining-requirements.md` and must be promoted through canonical change control before active use. |
| `references/macro-block-playbooks.md` | `macro-block-playbooks.md` | Supporting Reference | Advisory reference/playbook/source-overlay material; subordinate to canonical implementation documents. |
| `references/macro-expectations-surprise-framework.md` | `macro-expectations-surprise-framework.md` | Supporting Reference | Advisory reference/playbook/source-overlay material; subordinate to canonical implementation documents. |
| `references/macro-g3-fx-regional-policy-overlay.md` | `macro-g3-fx-regional-policy-overlay.md` | Supporting Reference | Advisory reference/playbook/source-overlay material; subordinate to canonical implementation documents. |
| `references/macro-indicator-cadence-source-registry.md` | `macro-indicator-cadence-source-registry.md` | Supporting Reference | Advisory reference/playbook/source-overlay material; subordinate to canonical implementation documents. |
| `references/macro-regime-framework.md` | `macro-regime-framework.md` | Supporting Reference | Advisory reference/playbook/source-overlay material; subordinate to canonical implementation documents. |
| `references/macro-sensitivity-framework.md` | `macro-sensitivity-framework.md` | Supporting Reference | Advisory reference/playbook/source-overlay material; subordinate to canonical implementation documents. |
| `archive/legacy-prd/market-intelligence-agent-prd.md` | `market-intelligence-agent-prd.md` | Archive | Retired legacy source; residual candidate requirements are captured in `implementation/remaining-requirements.md` and must be promoted through canonical change control before active use. |
| `archive/legacy-prd/market-intelligence-briefing-skill-prd.md` | `market-intelligence-briefing-skill-prd.md` | Archive | Retired legacy source; residual candidate requirements are captured in `implementation/remaining-requirements.md` and must be promoted through canonical change control before active use. |
| `references/market-materiality-filter.md` | `market-materiality-filter.md` | Supporting Reference | Advisory reference/playbook/source-overlay material; subordinate to canonical implementation documents. |
| `references/market-news-source-framework.md` | `market-news-source-framework.md` | Supporting Reference | Advisory reference/playbook/source-overlay material; subordinate to canonical implementation documents. |
| `references/market-pattern-library.md` | `market-pattern-library.md` | Supporting Reference | Advisory reference/playbook/source-overlay material; subordinate to canonical implementation documents. |
| `archive/legacy-prd/market-positioning-agent-prd.md` | `market-positioning-agent-prd.md` | Archive | Retired legacy source; residual candidate requirements are captured in `implementation/remaining-requirements.md` and must be promoted through canonical change control before active use. |
| `references/market-positioning-framework.md` | `market-positioning-framework.md` | Supporting Reference | Advisory reference/playbook/source-overlay material; subordinate to canonical implementation documents. |
| `archive/legacy-prd/market-positioning-method-skill-prd.md` | `market-positioning-method-skill-prd.md` | Archive | Retired legacy source; residual candidate requirements are captured in `implementation/remaining-requirements.md` and must be promoted through canonical change control before active use. |
| `archive/legacy-prd/market-sense-agent-prd.md` | `market-sense-agent-prd.md` | Archive | Retired legacy source; residual candidate requirements are captured in `implementation/remaining-requirements.md` and must be promoted through canonical change control before active use. |
| `archive/legacy-prd/market-sense-hypothesis-engine-skill-prd.md` | `market-sense-hypothesis-engine-skill-prd.md` | Archive | Retired legacy source; residual candidate requirements are captured in `implementation/remaining-requirements.md` and must be promoted through canonical change control before active use. |
| `archive/legacy-prd/master-intake-router-prd.md` | `master-intake-router-prd.md` | Archive | Retired legacy source; residual candidate requirements are captured in `implementation/remaining-requirements.md` and must be promoted through canonical change control before active use. |
| `archive/legacy-prd/news-catalysts-agent-prd.md` | `news-catalysts-agent-prd.md` | Archive | Retired legacy source; residual candidate requirements are captured in `implementation/remaining-requirements.md` and must be promoted through canonical change control before active use. |
| `references/news-catalysts-framework.md` | `news-catalysts-framework.md` | Supporting Reference | Advisory reference/playbook/source-overlay material; subordinate to canonical implementation documents. |
| `archive/legacy-prd/news-catalysts-method-skill-prd.md` | `news-catalysts-method-skill-prd.md` | Archive | Retired legacy source; residual candidate requirements are captured in `implementation/remaining-requirements.md` and must be promoted through canonical change control before active use. |
| `archive/legacy-prd/portfolio-fit-agent-prd.md` | `portfolio-fit-agent-prd.md` | Archive | Retired legacy source; residual candidate requirements are captured in `implementation/remaining-requirements.md` and must be promoted through canonical change control before active use. |
| `references/portfolio-fit-framework.md` | `portfolio-fit-framework.md` | Supporting Reference | Advisory reference/playbook/source-overlay material; subordinate to canonical implementation documents. |
| `archive/legacy-prd/portfolio-fit-method-skill-prd.md` | `portfolio-fit-method-skill-prd.md` | Archive | Retired legacy source; residual candidate requirements are captured in `implementation/remaining-requirements.md` and must be promoted through canonical change control before active use. |
| `archive/legacy-prd/prd.backup-before-full-target-language-20260625.md` | `prd.backup-before-full-target-language-20260625.md` | Archive | Historical backup/audit artifact; retained for provenance only and never active source of truth. |
| `archive/legacy-prd/prd.md` | `prd.md` | Archive | Retired legacy source; residual candidate requirements are captured in `implementation/remaining-requirements.md` and must be promoted through canonical change control before active use. |
| `archive/legacy-prd/risk-red-team-agent-prd.md` | `risk-red-team-agent-prd.md` | Archive | Retired legacy source; residual candidate requirements are captured in `implementation/remaining-requirements.md` and must be promoted through canonical change control before active use. |
| `references/risk-red-team-framework.md` | `risk-red-team-framework.md` | Supporting Reference | Advisory reference/playbook/source-overlay material; subordinate to canonical implementation documents. |
| `archive/legacy-prd/risk-red-team-method-skill-prd.md` | `risk-red-team-method-skill-prd.md` | Archive | Retired legacy source; residual candidate requirements are captured in `implementation/remaining-requirements.md` and must be promoted through canonical change control before active use. |
| `archive/legacy-prd/sector-industry-analysis-agent-prd.md` | `sector-industry-analysis-agent-prd.md` | Archive | Retired legacy source; residual candidate requirements are captured in `implementation/remaining-requirements.md` and must be promoted through canonical change control before active use. |
| `references/sector-industry-analysis-framework.md` | `sector-industry-analysis-framework.md` | Supporting Reference | Advisory reference/playbook/source-overlay material; subordinate to canonical implementation documents. |
| `archive/legacy-prd/sector-industry-analysis-method-skill-prd.md` | `sector-industry-analysis-method-skill-prd.md` | Archive | Retired legacy source; residual candidate requirements are captured in `implementation/remaining-requirements.md` and must be promoted through canonical change control before active use. |
| `references/source-registry-framework.md` | `source-registry-framework.md` | Supporting Reference | Advisory reference/playbook/source-overlay material; subordinate to canonical implementation documents. |
| `references/structural-winner-discovery-framework.md` | `structural-winner-discovery-framework.md` | Supporting Reference | Advisory reference/playbook/source-overlay material; subordinate to canonical implementation documents. |
| `archive/legacy-prd/structural-winner-discovery-method-skill-prd.md` | `structural-winner-discovery-method-skill-prd.md` | Archive | Retired legacy source; residual candidate requirements are captured in `implementation/remaining-requirements.md` and must be promoted through canonical change control before active use. |
| `archive/legacy-prd/structural-winners-discovery-agent-prd.md` | `structural-winners-discovery-agent-prd.md` | Archive | Retired legacy source; residual candidate requirements are captured in `implementation/remaining-requirements.md` and must be promoted through canonical change control before active use. |
| `archive/legacy-prd/system-architecture-map.md` | `system-architecture-map.md` | Archive | Retired legacy source; residual candidate requirements are captured in `implementation/remaining-requirements.md` and must be promoted through canonical change control before active use. |
| `archive/legacy-prd/theme-opportunity-intake-router-prd.md` | `theme-opportunity-intake-router-prd.md` | Archive | Retired legacy source; residual candidate requirements are captured in `implementation/remaining-requirements.md` and must be promoted through canonical change control before active use. |
| `archive/legacy-prd/valuation-expectations-agent-prd.md` | `valuation-expectations-agent-prd.md` | Archive | Retired legacy source; residual candidate requirements are captured in `implementation/remaining-requirements.md` and must be promoted through canonical change control before active use. |
| `references/valuation-expectations-framework.md` | `valuation-expectations-framework.md` | Supporting Reference | Advisory reference/playbook/source-overlay material; subordinate to canonical implementation documents. |
| `archive/legacy-prd/valuation-expectations-method-skill-prd.md` | `valuation-expectations-method-skill-prd.md` | Archive | Retired legacy source; residual candidate requirements are captured in `implementation/remaining-requirements.md` and must be promoted through canonical change control before active use. |

## Reference split-file registry

These files were created during P9-REF-01 and moved under `references/market-patterns/` during root cleanup. They are Supporting References and inherit the same advisory boundary: they do not govern final decisions, evidence readiness, routing, IC Action, or agent ownership.

| Reference split file | Status | Implementation role |
|---|---|---|
| `references/market-patterns/event-reactions-and-earnings.md` | Supporting Reference | Detailed event-reaction and earnings pattern bodies. |
| `references/market-patterns/expectations-and-narratives.md` | Supporting Reference | Detailed expectations, narrative, and valuation-reset pattern bodies. |
| `references/market-patterns/positioning-and-flows.md` | Supporting Reference | Detailed positioning, crowding, squeeze, and flow pattern bodies. |
| `references/market-patterns/macro-rates-liquidity.md` | Supporting Reference | Detailed macro, rates, and liquidity pattern bodies. |
| `references/market-patterns/cross-asset-regimes.md` | Supporting Reference | Detailed cross-asset and regime pattern bodies. |
| `references/market-patterns/stress-and-deleveraging.md` | Supporting Reference | Detailed stress and deleveraging pattern bodies. |
| `references/market-patterns/commodities-and-geopolitics.md` | Supporting Reference | Detailed commodity and geopolitical pattern bodies. |
| `references/market-patterns/examples-and-source-map.md` | Supporting Reference | Market-pattern examples, optional future patterns, and source-map references. |

## Broken or legacy references

The following referenced names are not active files in the current corpus and must not be treated as implementation dependencies unless explicitly created later. These are current non-blocking source warnings unless a future task explicitly depends on one of them.

`AGENTS.md` and `SKILL.md` in this list refer to unresolved legacy placeholder references only. They do not prohibit the future root `AGENTS.md` or repo skill files planned by `implementation/13-codex-runtime-architecture.md`.

- `intake.md`
- `industry.md`
- `workflow.md`
- `company.md`
- `macro.md`
- `AGENTS.md`
- `SKILL.md`
- `expected-vs-actual-reaction-framework.md`
- `narrative-analysis-framework.md`
- generic placeholders such as `agent-prd.md`, `framework.md`, and `method-skill-prd.md`

Handling rule: if a legacy document points to one of these names, use the closest canonical implementation document instead. Routing references resolve to `implementation/05-routing-and-workflows.md`; architecture references resolve to `implementation/02-canonical-architecture.md`; evidence/source references resolve to `implementation/04-evidence-layer.md`.


### P5-AGT-01 legacy agent PRD treatment

After P5-AGT-01, the agent-contract portions of legacy `*-agent-prd.md` and router PRD files have been normalized into `implementation/06-agent-contracts.md`. Their former `Needs Merge` status is preserved as residual-requirement context in `implementation/remaining-requirements.md` only, such as method-skill detail, report-schema examples, workflow examples, reference/playbook detail, or source-policy overlays that belong to later P5-SKL-01, P8-IC-01, P9-REF-01, or related cleanup tasks.

Do not treat the archived legacy files or residual-requirement rows as evidence that P5-AGT-01 is incomplete. For active agent role, boundary, input/output, handoff, and status behavior, `implementation/06-agent-contracts.md` is canonical.

### P5-SKL-01 legacy method-skill PRD treatment

After P5-SKL-01, the method-contract portions of legacy `*-method-skill-prd.md` and `*-skill-prd.md` files have been normalized into `implementation/11-skill-contracts.md`. Their former `Needs Merge` status is preserved as residual-requirement context in `implementation/remaining-requirements.md` only, such as report-schema examples, workflow examples, reference/playbook detail, source-policy overlays, or later P8-IC-01, P9-REF-01, P10-QA-01, or related cleanup tasks.

Do not treat the archived legacy files or residual-requirement rows as evidence that P5-SKL-01 is incomplete. For active method triggers, inputs, steps, output core, guardrails, failure states, quality checks, and runtime skill-adapter behavior, `implementation/11-skill-contracts.md` is canonical.


### P8-IC-01 legacy report-schema treatment

After P8-IC-01, the IC memo and report-schema portions of legacy report frameworks, agent PRDs, method-skill PRDs, and supporting analysis frameworks that route to `implementation/07-investment-committee-and-report-schemas.md` have been normalized into that canonical report-schema contract. Their former `Needs Merge` or Supporting Reference treatment is preserved as residual-requirement or advisory-reference context only, such as reference/playbook detail, source-policy overlays, workflow examples, future P9-REF-01 reference cleanup, P10-QA-01 execution, or later maintenance.

Do not treat archived legacy files or residual-requirement rows as evidence that P8-IC-01 is incomplete. For active final IC memo structure, non-final IC artifacts, Action Box / Decision-Prep Box behavior, controlled IC Action labels, freshness/source display, report metadata, and report-schema edge cases, `implementation/07-investment-committee-and-report-schemas.md` is canonical.


### P9-REF-01 reference-library treatment

After P9-REF-01, registered Supporting References and the former `Needs Split` market pattern library have governance metadata headers, central index coverage in `implementation/reference-library-index.md`, and explicit advisory boundaries. The `references/market-pattern-library.md` parent file is now an index and usage guide, while detailed pattern bodies live under `references/market-patterns/`.

Reference files remain subordinate to canonical implementation documents. They may provide examples, taxonomies, diagnostic questions, source overlays, and playbook detail, but they do not control evidence readiness, routing, agent ownership, report schemas, or IC Action.

New unregistered reference files default to Draft Source / Advisory only until registered. If a reference header and the central reference index conflict, record a warning and apply the stricter interpretation until synchronized.

## Source-of-truth precedence

1. Canonical implementation documents.
2. Supporting References, when they do not conflict with canonical implementation documents.
3. Supporting residual-requirement registers, only as candidate requirement inventory until promoted through canonical change control.
4. Needs Split / Needs Merge / Draft Source documents, only if introduced in future registry updates and only as advisory or proposed additions under their status.
5. Archive documents, never as active source of truth.

If a legacy PRD conflicts with the canonical implementation layer, the canonical implementation layer governs.

## Documentation-control behavior rules

These rules define how agents and implementers should behave when the registry, file corpus, or user request is ambiguous.

### Conflict handling

| Situation | Required behavior |
|---|---|
| Legacy, Draft Source, Needs Merge, or Supporting Reference conflicts with a canonical document. | Apply the canonical rule and record a source warning. |
| Needs Split document is relevant to the task. | Use only as advisory reference material until split / indexed; it does not override canonical rules. |
| Two Needs Merge / Draft Source documents conflict. | Do not choose either as a working rule; record a pending decision. |
| Canonical documents conflict with each other. | Use fixed canonical priority and record a source warning. `implementation/00-master-rules.md` governs master statuses, gates, output standards, confidence, source display, style, and artifact naming. `implementation/01-documentation-control.md` governs registry and precedence. More specific canonical documents govern their local domain only when they do not conflict with these master authorities. |
| Decision log conflicts with a canonical document. | Canonical document governs; decision log remains historical rationale and the conflict is a warning. |

### Non-canonical document handling

| Document condition | Required behavior |
|---|---|
| New unregistered document appears. | Treat as Draft Source by default and warn that it is not source of truth until registered. |
| Needs Merge document contains a useful rule. | Do not apply as a working rule; capture as a proposed addition / pending decision. |
| Needs Merge or Draft Source contains `MUST`, `SHOULD`, or `MAY`. | Interpret the modal word only within that document's status. It is candidate material, not an active system rule. |
| Non-canonical document contains examples. | Examples may be used as reference or inspiration if they do not change canonical rules. |
| Legacy detail expands a broad canonical rule without changing it. | Use as advisory detail only; canonical rule remains governing. |
| User asks to use an archive or backup document. | Read only as a source of ideas by explicit request; do not treat as source of truth. |
| User asks to follow a legacy PRD instead of canonical rules. | Treat as a change request to canonical documentation, not as a silent override. |

### Missing, unreadable, or inconsistent files

| Situation | Required behavior |
|---|---|
| Legacy document references a missing file. | Use the closest canonical implementation document when one is defined in this registry and record a source warning. |
| Canonical registry entry points to a missing file. | Blocking if required for the current task; otherwise warning. Do not substitute a legacy file as source of truth. |
| Registry path is stale but a similar file exists. | Mention the possible match, but do not use it as source of truth without confirmation / registry update. |
| Document exists but is unreadable, empty, damaged, or has unusable encoding. | Record an access issue; do not infer requirements from it. |
| Same document appears twice in the registry with different statuses. | Blocking if needed for the current task; otherwise warning. Do not choose by row order. |
| Registry status conflicts with the status or title inside a file. | Registry status governs; record a warning if the mismatch could confuse implementation. |
| File name is unclear or displayed with encoding artifacts. | Identify by exact filesystem path; treat naming/display problems as cleanup issues, not status changes. |

### User-facing source issue levels

| Level | Meaning | Examples |
|---|---|---|
| Info | Non-blocking condition that does not change the answer or implementation path. | Unclear file name, cosmetic display issue, old naming alias. |
| Warning | Non-blocking source-control issue that should be visible and may need later review. | Legacy conflict, missing non-critical reference, unregistered draft, pending decision. |
| Blocking | Current task cannot safely continue because the issue can change the result. | Missing required canonical file, unreadable required source, ambiguous duplicate status for a required document. |

Source issues become Blocking only when they affect the current task and could change the result. Otherwise they remain Info or Warning.

### User-facing source issue format

User-facing answers should not expose internal diagnostics unless needed. Use a short summary:

```text
Source issues: 2 warnings, 0 blocking. Details available on request.
```

Show only user-significant limitations in normal answers. Detailed source diagnostics should be available on request or when an issue is Blocking.

### Routing to canonical documents

Use this routing table before answering implementation-rule questions:

| Question type | Primary canonical source |
|---|---|
| Statuses, gates, confidence, Action Box, evidence display, style, artifact naming | `implementation/00-master-rules.md` |
| Registry, source precedence, archive behavior, source issues | `implementation/01-documentation-control.md` |
| Architecture, ownership, orchestration, decision boundaries | `implementation/02-canonical-architecture.md` |
| Agent / skill / workflow / report template shape | `implementation/03-contract-templates.md` |
| Evidence model, source hierarchy, freshness, evidence lock | `implementation/04-evidence-layer.md` |
| Routing and workflow behavior | `implementation/05-routing-and-workflows.md` |
| Agent contracts | `implementation/06-agent-contracts.md` |
| IC memo and report schemas | `implementation/07-investment-committee-and-report-schemas.md` |
| Reference-library governance | `implementation/08-reference-library-cleanup.md` |
| QA and acceptance scenarios | `implementation/09-system-acceptance-qa.md` |
| Legacy coverage / remaining gaps | `implementation/10-traceability-matrix.md` |
| Method-skill contracts | `implementation/11-skill-contracts.md` |
| Codex-native runtime structure, `AGENTS.md`, repo skills, custom subagents, workflow runbooks | `implementation/13-codex-runtime-architecture.md` |
| User-facing language selection, Russian language policy, and investment-analytical presentation style | `implementation/14-language-and-style.md` |

`TASKS.md` controls the active work queue. `IMPLEMENTATION_BACKLOG.md` controls phase meaning and scope when the two documents differ.

## Change control

Documentation-control rules may change only through an explicit change request that updates the relevant canonical document and the decision log. A chat instruction alone is not a persistent source-of-truth change until reflected in canonical documentation.

For project work, discussion and implementation are separate modes of work. Do not edit repository files when the user explicitly asks only to discuss, plan, or review.

## Manual acceptance checks for P0-DOC-01

P0-DOC-01 is Done when:

- Registry lists active canonical implementation documents and included legacy documents.
- Backup, audit, archive, and personal/operator reminder files are excluded from active source-of-truth use.
- Every included legacy document has one primary implementation status.
- Source-of-truth precedence is documented.
- Source issue handling is documented for conflicts, missing files, unreadable files, stale paths, duplicate registry entries, unregistered files, and user override requests.
- Source issue severity levels are documented as Info, Warning, and Blocking.
- User-facing `Source issues` summary behavior is documented.
- Remaining warnings or gaps are classified and do not block the source-of-truth model.
