# Documentation Control Registry

Status: Canonical implementation-control document

## Purpose

This document controls which legacy PRD / Markdown documents are active implementation inputs, which are references, which require consolidation, and which are excluded from active implementation.

The canonical implementation layer is `IMPLEMENTATION_BACKLOG.md` plus the canonical implementation documents explicitly listed below. Files located under `implementation/` are not automatically canonical unless this registry lists them as canonical. `НАПОМИНАНИЕ.md` is intentionally excluded from this registry by user instruction.

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

## Implementation governance records

| Document | Record type | Role |
|---|---|---|
| `TASKS.md` | Operational control register | Active work queue and task status tracker. It controls what is currently open or done; `IMPLEMENTATION_BACKLOG.md` governs phase meaning and scope when they differ. |
| `implementation/12-decision-log.md` | Supporting decision record | Decision history and rationale. It explains why documentation-control rules were chosen, but it does not override canonical implementation documents. |
| `.codex/runtime-readiness-report.md` | Supporting operational validation record | P1A-CODEX-02 generated-runtime readiness, structural gate, validation, and idempotency record. It does not override canonical implementation documents. |
| `implementation/reference-library-index.md` | Supporting operational index | P9-REF-01 reference-library navigation, owner/used-by metadata, freshness tier, split/index state, and non-blocking review notes. It does not override the registry or canonical implementation documents. |
| `implementation/p10-qa-execution-report.md` | Supporting operational validation record | P10-QA-01 Pareto Gate, Full Regression, Live-Smoke, structural validation, source issues, and final closure evidence. It does not override canonical implementation documents. |

## Legacy document registry

| Legacy document | Status | Implementation role |
|---|---|---|
| `asset-driver-maps.md` | Supporting Reference | Reference/playbook/schema source; supports canonical contracts. |
| `asset-intake-router-prd.md` | Needs Merge | Normalize into canonical agent/skill/workflow contract. |
| `commodity-agent-prd.md` | Needs Merge | Normalize into canonical agent/skill/workflow contract. |
| `commodity-analysis-framework.md` | Supporting Reference | Reference/playbook/schema source; supports canonical contracts. |
| `commodity-analysis-method-skill-prd.md` | Needs Merge | Normalize into canonical agent/skill/workflow contract. |
| `commodity-family-playbooks.md` | Supporting Reference | Reference/playbook/schema source; supports canonical contracts. |
| `crypto-agent-prd.md` | Needs Merge | Normalize into canonical agent/skill/workflow contract. |
| `crypto-analysis-framework.md` | Supporting Reference | Reference/playbook/schema source; supports canonical contracts. |
| `crypto-analysis-method-skill-prd.md` | Needs Merge | Normalize into canonical agent/skill/workflow contract. |
| `crypto-data-source-and-metric-framework.md` | Supporting Reference | Reference/playbook/schema source; supports canonical contracts. |
| `driver-dominance-analysis-skill-prd.md` | Needs Merge | Normalize into canonical agent/skill/workflow contract. |
| `equity-agent-prd.md` | Needs Merge | Normalize into canonical agent/skill/workflow contract. |
| `equity-company-analysis-framework.md` | Supporting Reference | Reference/playbook/schema source; supports canonical contracts. |
| `equity-company-analysis-method-skill-prd.md` | Needs Merge | Normalize into canonical agent/skill/workflow contract. |
| `equity-deep-dive-workflow.md` | Supporting Reference | Reference/playbook/schema source; supports canonical contracts. |
| `etf-agent-prd.md` | Needs Merge | Normalize into canonical agent/skill/workflow contract. |
| `etf-analysis-framework.md` | Supporting Reference | Reference/playbook/schema source; supports canonical contracts. |
| `etf-analysis-method-skill-prd.md` | Needs Merge | Normalize into canonical agent/skill/workflow contract. |
| `evidence-collection-method-skill-prd.md` | Needs Merge | Normalize into canonical agent/skill/workflow contract. |
| `evidence-collector-agent-prd.md` | Needs Merge | Normalize into canonical agent/skill/workflow contract. |
| `evidence-pack-framework.md` | Supporting Reference | Reference/playbook/schema source; supports canonical contracts. |
| `evidence-request-protocol.md` | Supporting Reference | Reference/playbook/schema source; supports canonical contracts. |
| `final-architecture-audit.md` | Archive | Historical backup/audit artifact; not active source of truth. |
| `financial-statement-analysis-skill-prd.md` | Needs Merge | Normalize into canonical agent/skill/workflow contract. |
| `fixed-income-agent-prd.md` | Needs Merge | Normalize into canonical agent/skill/workflow contract. |
| `fixed-income-analysis-method-skill-prd.md` | Needs Merge | Normalize into canonical agent/skill/workflow contract. |
| `fixed-income-framework.md` | Supporting Reference | Reference/playbook/schema source; supports canonical contracts. |
| `fixed-income-instrument-playbooks.md` | Supporting Reference | Reference/playbook/schema source; supports canonical contracts. |
| `full-agent-system-build-roadmap.md` | Draft Source | Source material to harvest into canonical implementation docs. |
| `investment-committee-agent-prd.md` | Needs Merge | Normalize into canonical agent/skill/workflow contract. |
| `investment-committee-memo-framework.md` | Supporting Reference | Reference/playbook/schema source; supports canonical contracts. |
| `investment-committee-synthesis-method-skill-prd.md` | Needs Merge | Normalize into canonical agent/skill/workflow contract. |
| `macro-agent-prd.md` | Needs Merge | Normalize into canonical agent/skill/workflow contract. |
| `macro-analysis-method-skill-prd.md` | Needs Merge | Normalize into canonical agent/skill/workflow contract. |
| `macro-block-playbooks.md` | Supporting Reference | Reference/playbook/schema source; supports canonical contracts. |
| `macro-expectations-surprise-framework.md` | Supporting Reference | Reference/playbook/schema source; supports canonical contracts. |
| `macro-g3-fx-regional-policy-overlay.md` | Supporting Reference | Reference/playbook/schema source; supports canonical contracts. |
| `macro-indicator-cadence-source-registry.md` | Supporting Reference | Reference/playbook/schema source; supports canonical contracts. |
| `macro-regime-framework.md` | Supporting Reference | Reference/playbook/schema source; supports canonical contracts. |
| `macro-sensitivity-framework.md` | Supporting Reference | Reference/playbook/schema source; supports canonical contracts. |
| `market-intelligence-agent-prd.md` | Needs Merge | Normalize into canonical agent/skill/workflow contract. |
| `market-intelligence-briefing-skill-prd.md` | Needs Merge | Normalize into canonical agent/skill/workflow contract. |
| `market-materiality-filter.md` | Supporting Reference | Reference/playbook/schema source; supports canonical contracts. |
| `market-news-source-framework.md` | Supporting Reference | Reference/playbook/schema source; supports canonical contracts. |
| `market-pattern-library.md` | Supporting Reference | Reference index and usage guide for split market-pattern files; supports canonical contracts but does not override them. |
| `market-positioning-agent-prd.md` | Needs Merge | Normalize into canonical agent/skill/workflow contract. |
| `market-positioning-framework.md` | Supporting Reference | Reference/playbook/schema source; supports canonical contracts. |
| `market-positioning-method-skill-prd.md` | Needs Merge | Normalize into canonical agent/skill/workflow contract. |
| `market-sense-agent-prd.md` | Needs Merge | Normalize into canonical agent/skill/workflow contract. |
| `market-sense-hypothesis-engine-skill-prd.md` | Needs Merge | Normalize into canonical agent/skill/workflow contract. |
| `master-intake-router-prd.md` | Needs Merge | Normalize into canonical agent/skill/workflow contract. |
| `news-catalysts-agent-prd.md` | Needs Merge | Normalize into canonical agent/skill/workflow contract. |
| `news-catalysts-framework.md` | Supporting Reference | Reference/playbook/schema source; supports canonical contracts. |
| `news-catalysts-method-skill-prd.md` | Needs Merge | Normalize into canonical agent/skill/workflow contract. |
| `portfolio-fit-agent-prd.md` | Needs Merge | Normalize into canonical agent/skill/workflow contract. |
| `portfolio-fit-framework.md` | Supporting Reference | Reference/playbook/schema source; supports canonical contracts. |
| `portfolio-fit-method-skill-prd.md` | Needs Merge | Normalize into canonical agent/skill/workflow contract. |
| `prd.backup-before-full-target-language-20260625.md` | Archive | Historical backup/audit artifact; not active source of truth. |
| `prd.md` | Draft Source | Source material to harvest into canonical implementation docs. |
| `risk-red-team-agent-prd.md` | Needs Merge | Normalize into canonical agent/skill/workflow contract. |
| `risk-red-team-framework.md` | Supporting Reference | Reference/playbook/schema source; supports canonical contracts. |
| `risk-red-team-method-skill-prd.md` | Needs Merge | Normalize into canonical agent/skill/workflow contract. |
| `sector-industry-analysis-agent-prd.md` | Needs Merge | Normalize into canonical agent/skill/workflow contract. |
| `sector-industry-analysis-framework.md` | Supporting Reference | Reference/playbook/schema source; supports canonical contracts. |
| `sector-industry-analysis-method-skill-prd.md` | Needs Merge | Normalize into canonical agent/skill/workflow contract. |
| `source-registry-framework.md` | Supporting Reference | Reference/playbook/schema source; supports canonical contracts. |
| `structural-winner-discovery-framework.md` | Supporting Reference | Reference/playbook/schema source; supports canonical contracts. |
| `structural-winner-discovery-method-skill-prd.md` | Needs Merge | Normalize into canonical agent/skill/workflow contract. |
| `structural-winners-discovery-agent-prd.md` | Needs Merge | Normalize into canonical agent/skill/workflow contract. |
| `system-architecture-map.md` | Draft Source | Source material to harvest into canonical implementation docs. |
| `theme-opportunity-intake-router-prd.md` | Needs Merge | Normalize into canonical agent/skill/workflow contract. |
| `valuation-expectations-agent-prd.md` | Needs Merge | Normalize into canonical agent/skill/workflow contract. |
| `valuation-expectations-framework.md` | Supporting Reference | Reference/playbook/schema source; supports canonical contracts. |
| `valuation-expectations-method-skill-prd.md` | Needs Merge | Normalize into canonical agent/skill/workflow contract. |


## Reference split-file registry

These files were created during P9-REF-01 to make `market-pattern-library.md` safe for retrieval. They are Supporting References and inherit the same advisory boundary: they do not govern final decisions, evidence readiness, routing, IC Action, or agent ownership.

| Reference split file | Status | Implementation role |
|---|---|---|
| `market-patterns/event-reactions-and-earnings.md` | Supporting Reference | Detailed event-reaction and earnings pattern bodies. |
| `market-patterns/expectations-and-narratives.md` | Supporting Reference | Detailed expectations, narrative, and valuation-reset pattern bodies. |
| `market-patterns/positioning-and-flows.md` | Supporting Reference | Detailed positioning, crowding, squeeze, and flow pattern bodies. |
| `market-patterns/macro-rates-liquidity.md` | Supporting Reference | Detailed macro, rates, and liquidity pattern bodies. |
| `market-patterns/cross-asset-regimes.md` | Supporting Reference | Detailed cross-asset and regime pattern bodies. |
| `market-patterns/stress-and-deleveraging.md` | Supporting Reference | Detailed stress and deleveraging pattern bodies. |
| `market-patterns/commodities-and-geopolitics.md` | Supporting Reference | Detailed commodity and geopolitical pattern bodies. |
| `market-patterns/examples-and-source-map.md` | Supporting Reference | Market-pattern examples, optional future patterns, and source-map references. |

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

After P5-AGT-01, the agent-contract portions of legacy `*-agent-prd.md` and router PRD files have been normalized into `implementation/06-agent-contracts.md`. Their registry status remains `Needs Merge` only for residual non-agent-contract material, such as method-skill detail, report-schema examples, workflow examples, reference/playbook detail, or source-policy overlays that belong to later P5-SKL-01, P8-IC-01, P9-REF-01, or related cleanup tasks.

Do not treat the remaining `Needs Merge` status on those legacy files as evidence that P5-AGT-01 is incomplete. For active agent role, boundary, input/output, handoff, and status behavior, `implementation/06-agent-contracts.md` is canonical.

### P5-SKL-01 legacy method-skill PRD treatment

After P5-SKL-01, the method-contract portions of legacy `*-method-skill-prd.md` and `*-skill-prd.md` files have been normalized into `implementation/11-skill-contracts.md`. Their registry status remains `Needs Merge` only for residual non-method-contract material, such as report-schema examples, workflow examples, reference/playbook detail, source-policy overlays, or later P8-IC-01, P9-REF-01, P10-QA-01, or related cleanup tasks.

Do not treat the remaining `Needs Merge` status on those legacy method-skill files as evidence that P5-SKL-01 is incomplete. For active method triggers, inputs, steps, output core, guardrails, failure states, quality checks, and runtime skill-adapter behavior, `implementation/11-skill-contracts.md` is canonical.


### P8-IC-01 legacy report-schema treatment

After P8-IC-01, the IC memo and report-schema portions of legacy report frameworks, agent PRDs, method-skill PRDs, and supporting analysis frameworks that route to `implementation/07-investment-committee-and-report-schemas.md` have been normalized into that canonical report-schema contract. Their registry status remains `Needs Merge` or `Supporting Reference` only for residual non-report-schema material, such as reference/playbook detail, source-policy overlays, workflow examples, future P9-REF-01 reference cleanup, P10-QA-01 execution, or later maintenance.

Do not treat the remaining `Needs Merge` status on those legacy files as evidence that P8-IC-01 is incomplete. For active final IC memo structure, non-final IC artifacts, Action Box / Decision-Prep Box behavior, controlled IC Action labels, freshness/source display, report metadata, and report-schema edge cases, `implementation/07-investment-committee-and-report-schemas.md` is canonical.


### P9-REF-01 reference-library treatment

After P9-REF-01, registered Supporting References and the former `Needs Split` market pattern library have governance metadata headers, central index coverage in `implementation/reference-library-index.md`, and explicit advisory boundaries. The `market-pattern-library.md` parent file is now an index and usage guide, while detailed pattern bodies live under `market-patterns/`.

Reference files remain subordinate to canonical implementation documents. They may provide examples, taxonomies, diagnostic questions, source overlays, and playbook detail, but they do not control evidence readiness, routing, agent ownership, report schemas, or IC Action.

New unregistered reference files default to Draft Source / Advisory only until registered. If a reference header and the central reference index conflict, record a warning and apply the stricter interpretation until synchronized.

## Source-of-truth precedence

1. Canonical implementation documents.
2. Supporting References, when they do not conflict with canonical implementation documents.
3. Needs Split documents, only as advisory reference material until split / indexed.
4. Needs Merge / Draft Source documents, only as source material or proposed additions.
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
