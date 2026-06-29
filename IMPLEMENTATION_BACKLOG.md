# Implementation Backlog — Full Financial Agent System

Status: Canonical implementation-control document  
Target: Agents-first system, not a backend/UI product  
Language policy: project Markdown documents in English; user-facing chat may remain Russian

## 1. Objective

Transform the current PRD / Markdown draft corpus into an implementable agentic investment-analysis system without reducing scope to an MVP.

The implementation target is an **agents-first runtime**: canonical agent contracts, skill contracts, workflow contracts, report schemas, evidence rules, handoff rules, and acceptance tests that can be used by Codex / LLM agents or later converted into a software product.

The legacy PRD corpus is source material. The canonical build layer is this file plus the files under `implementation/`.

## 2. Canonical implementation documents

0. `implementation/00-master-rules.md` - master statuses, gates, output standards, confidence, source display, artifact naming.
1. `implementation/01-documentation-control.md` - active document set, statuses, archive rules, broken-link handling.
2. `implementation/02-canonical-architecture.md` - architecture, ownership, orchestration, statuses, decision labels.
3. `implementation/03-contract-templates.md` - templates for agents, skills, workflows, reports.
4. `implementation/04-evidence-layer.md` - evidence model, source hierarchy, readiness, pre-IC lock.
5. `implementation/05-routing-and-workflows.md` - routing model and workflow contracts.
6. `implementation/06-agent-contracts.md` - canonical contracts for routers, asset agents, specialists, discovery agents, and IC.
7. `implementation/07-investment-committee-and-report-schemas.md` - IC contract and report schemas.
8. `implementation/08-reference-library-cleanup.md` - reference-library governance and cleanup rules.
9. `implementation/09-system-acceptance-qa.md` - acceptance scenarios and QA checks.
10. `implementation/10-traceability-matrix.md` - legacy-file coverage and canonical destinations.
11. `implementation/11-skill-contracts.md` - canonical method-skill contracts.
12. `implementation/13-codex-runtime-architecture.md` - OpenAI Codex-native project structure, `AGENTS.md`, repo skills, custom subagents, and workflow runbook conventions.

Supporting / operational records:

- `TASKS.md` - operational work queue and task status tracker; `IMPLEMENTATION_BACKLOG.md` governs phase meaning and scope when they differ.
- `implementation/12-decision-log.md` - decision history and rationale; it does not override canonical implementation documents.

## 3. Phase backlog

### Phase 0 — Documentation Control

Outcome: active implementation documents are separated from draft, backup, and audit artifacts.

Work items:
- Adopt `implementation/01-documentation-control.md` as the registry.
- Assign every legacy document one implementation status: `Canonical`, `Supporting Reference`, `Draft Source`, `Archive`, `Needs Merge`, or `Needs Split`.
- Exclude `prd.backup-before-full-target-language-20260625.md` and `final-architecture-audit.md` from active source-of-truth use.
- Treat missing legacy references as non-active unless explicitly created later.
- Document source-of-truth precedence and source-issue behavior for conflicts, missing files, unreadable files, duplicate statuses, unregistered files, stale paths, and user override requests.
- Record documentation-control decisions in `implementation/12-decision-log.md` as supporting rationale, not source-of-truth authority.

Acceptance criteria:
- Active documents are obvious.
- Backup/audit files are not used as source of truth.
- Implementation precedence is documented.
- Source issues are classified as Info, Warning, or Blocking.
- P0-DOC-01 may be Done with classified non-blocking warnings or future traceability gaps, provided the source-of-truth model is clear.

### Phase 1 — Canonical Architecture Layer

Outcome: one canonical architecture model governs implementation.

Work items:
- Use `implementation/02-canonical-architecture.md` as the architecture layer.
- Treat `prd.md` as product-level draft source, not architecture truth.
- Treat `system-architecture-map.md` as architecture draft source superseded by the canonical implementation layer where conflicts exist.
- Enforce owner/contributor boundaries and workflow-controlled handoffs.
- Standardize base statuses: `Complete`, `Limited`, `Blocked`, `Preliminary`.
- Standardize decision labels: `Specialist Verdict`, `Actionability Label`, `Investment View`, `IC Action`, `Vehicle Quality Verdict`.

Acceptance criteria:
- Every agent has a category, owner boundary, and handoff role.
- Final investment decision support passes through evidence, relevant specialists, and IC synthesis.

### Phase 1A — Codex Runtime Architecture Layer

Outcome: the canonical financial-agent architecture is packaged into an OpenAI Codex-native project structure without turning legacy PRDs into runtime source of truth.

Work items:
- Adopt `implementation/13-codex-runtime-architecture.md` as the Codex runtime architecture layer.
- Define the intended project-root `AGENTS.md` as a concise source-of-truth navigator, not a replacement for canonical implementation documents.
- Define the intended project-root `README.md` as the human-readable project map.
- Define `.codex/agents/` as the location for project-scoped custom Codex agents, with one narrow TOML file per planned agent/router contract.
- Define `.agents/skills/` as the location for repo-scoped Codex skills, with one focused `SKILL.md` per reusable method skill.
- Map the 20 planned agent/router contracts to custom-agent files and map canonical method-skill contracts to repo skills.
- Preserve the runtime pattern: thin custom agents, deep skills, canonical implementation documents as source of truth, legacy PRDs as supporting source material only.
- Keep actual generation of individual custom agents and skills gated by stable canonical agent and skill contracts.

Acceptance criteria:
- Codex can start from `AGENTS.md` and know which canonical documents to read before using legacy source material.
- The project has a documented path for creating `AGENTS.md`, `README.md`, `.codex/agents/*.toml`, `.agents/skills/*/SKILL.md`, and workflow runbooks.
- Custom agents are defined as narrow, opinionated adapters, not full PRD copies.
- Skills are defined as focused reusable workflows with explicit triggers, inputs, outputs, guardrails, and quality checks.
- No legacy PRD becomes runtime source of truth unless routed through the canonical documentation registry and traceability matrix.

### Phase 2 — Standard Contract Templates

Outcome: all future agent/workflow/report docs use one shape.

Work items:
- Adopt `implementation/03-contract-templates.md`.
- Define normalization rules for legacy Agent PRDs, Skill PRDs, Workflow docs, and Framework docs so later P5/P5-SKL work can convert them into standard contracts.
- Define required inputs, outputs, failure states, handoffs, and success criteria fields so later normalization does not require guessing.

Acceptance criteria:
- Implementers do not have to guess responsibilities, inputs, outputs, or completion conditions.

### Phase 3 — Evidence Layer

Outcome: Evidence Collector becomes the factual-control layer.

Work items:
- Adopt `implementation/04-evidence-layer.md`.
- Use Source Registry as the default source hierarchy authority.
- Keep domain source frameworks as overlays only.
- Require material-claim support status and pre-IC evidence lock for final memos.

Acceptance criteria:
- Missing, stale, paywalled, proxy, or contradictory evidence constrains output instead of being hidden.

### Phase 4 — Router and Workflow Layer

Outcome: user requests have deterministic route selection.

Work items:
- Adopt `implementation/05-routing-and-workflows.md`.
- Normalize Master Intake, Asset Intake, Theme Intake, and direct specialist-call behavior.
- Use workflow contracts rather than improvised agent-to-agent calls.

Acceptance criteria:
- Router selects workflow and does not make investment decisions.
- Ambiguous requests have clarification or safe bounded default behavior.

### Phase 5 — Asset-Class Agent Layer

Outcome: asset-class agents are contract-ready.

Work items:
- Normalize Equity, ETF, Fixed Income, Commodity, and Crypto packages using `implementation/06-agent-contracts.md`.
- Remove repeated content between Agent PRD / Method Skill / Framework during future cleanup.
- Add missing Success Criteria and explicit input/output contracts.
- Preserve the rule that asset agents produce specialist outputs, not final IC actions.

Acceptance criteria:
- Each asset class has one lead agent.
- Each asset output can be consumed by Risk, Valuation, Portfolio Fit, and IC where relevant.

### Phase 6 — Specialist Agent Layer

Outcome: cross-functional agents strengthen workflows without overriding Evidence or IC.

Work items:
- Normalize Valuation, Risk, News, Positioning, Macro, Portfolio Fit, Market Sense, Driver Dominance, and Market Intelligence contracts.
- Clarify trigger conditions, required inputs, handoff blocks, and Limited/Blocked behavior.
- Keep each specialist inside its decision boundary.

Acceptance criteria:
- Specialist agents cannot silently override Evidence Collector readiness or IC synthesis.

### Phase 7 — Theme and Discovery Layer

Outcome: theme-first and discovery workflows are implementable.

Work items:
- Normalize Sector & Industry Analysis and Structural Winners Discovery contracts.
- Preserve discovery boundary: candidates are not investment-actionable until asset-level evidence, valuation, risk, and IC synthesis are complete.
- Define theme-to-asset handoff.

Acceptance criteria:
- Theme workflows produce maps, candidates, and monitoring plans without hidden buy/sell recommendations.

### Phase 8 — Investment Committee Layer

Outcome: IC is the final synthesis and decision-support layer.

Work items:
- Adopt `implementation/07-investment-committee-and-report-schemas.md`.
- Require evidence lock and relevant specialist reports before Complete Final Memo.
- Enforce positive-action gate.

Acceptance criteria:
- IC cannot invent facts outside evidence and specialist reports.
- Final memo is decision-oriented, not an internal transcript.

### Phase 9 — Reference Library Cleanup

Outcome: references support agents without becoming hidden PRDs.

Work items:
- Adopt `implementation/08-reference-library-cleanup.md`.
- Add Owner / Used by metadata during future cleanup.
- Split large libraries only where navigation or ownership is unclear.

Acceptance criteria:
- References are modular, searchable, and non-conflicting.

### Phase 10 — System Acceptance and QA

Outcome: the system can be tested as a full agentic system.

Work items:
- Adopt `implementation/09-system-acceptance-qa.md`.
- Run acceptance scenarios across asset, theme, direct specialist, market, and IC workflows.

Acceptance criteria:
- Router, evidence, specialists, reports, statuses, and IC gates behave consistently across scenarios.

## 3A. Operational work-item register

| ID | Work item | Depends on | Owner | Done criteria |
|---|---|---|---|---|
| P0-DOC-01 | Establish documentation registry and source-of-truth precedence. | None | Documentation control | Registry lists included legacy files, excludes archive/reminder files, documents precedence, and defines source-issue handling. |
| P0-DOC-02 | Add traceability matrix from legacy corpus to canonical docs. | P0-DOC-01 | Documentation control | Every included legacy file maps to canonical destination and remaining gap. |
| P1-ARCH-01 | Finalize canonical architecture and owner/contributor model. | P0-DOC-01 | Architecture | Agent categories, orchestration rule, and decision boundaries are explicit. |
| P1-RULE-01 | Centralize statuses, gates, confidence, Action Box, evidence display, style, and artifact naming. | P1-ARCH-01 | Architecture | `implementation/00-master-rules.md` is the master rule authority. |
| P1A-CODEX-01 | Define Codex-native runtime architecture and packaging rules. | P1-ARCH-01 | Codex runtime architecture | `implementation/13-codex-runtime-architecture.md` defines `AGENTS.md`, `README.md`, `.codex/agents`, `.agents/skills`, workflow runbooks, and source-of-truth routing rules. |
| P1A-CODEX-02 | Create Codex-native project files and directories from canonical contracts. | P1A-CODEX-01; P1A structural runtime readiness gate in `implementation/13-codex-runtime-architecture.md` | Codex runtime architecture | Root `AGENTS.md` and `README.md` exist; 20 custom-agent TOML files and repo skill folders are generated from canonical contracts without copying full legacy PRDs; `.codex/runtime-readiness-report.md` records structural readiness; P5-AGT-01 is now normalized and runtime adapters are resynchronized, while broader P5-SKL-01 method-skill normalization is now complete. |
| P2-TPL-01 | Standardize Agent, Skill, Workflow, and Report templates. | P1-RULE-01 | Documentation control | Implementers can normalize all PRDs without inventing fields. |
| P3-EVD-01 | Canonicalize evidence model, source hierarchy, readiness, and pre-IC lock. | P1-RULE-01 | Evidence Collector | Evidence layer defines claim support, freshness, missing data, and allowed IC status. |
| P4-RTE-01 | Canonicalize master, asset, theme, and direct-specialist routing. | P1-ARCH-01; P3-EVD-01 | Router layer | Every request family has deterministic route and safe fallback. |
| P5-AGT-01 | Normalize router, evidence, asset, specialist, discovery, and IC agent contracts. | P2-TPL-01; P4-RTE-01 | Agent layer | Each agent has inputs, outputs, evidence, handoffs, Limited/Blocked rules, success criteria. |
| P5-SKL-01 | Normalize all method-skill contracts. | P2-TPL-01; P5-AGT-01 | Skill layer | `implementation/11-skill-contracts.md` contains 19 Template v2 method skills with output core, guardrails, failure states, QA coverage, and synchronized runtime `.agents/skills/*/SKILL.md` adapters. |
| P8-IC-01 | Canonicalize IC memo and report schemas. | P3-EVD-01; P5-AGT-01 | IC layer | Final memo uses `final_investment_memo.md`, Action Box, confidence, gates, and source limits. |
| P9-REF-01 | Govern reference libraries and split/index large references where needed. | P0-DOC-02 | Reference layer | Supporting references have governance metadata, `implementation/reference-library-index.md` provides central navigation, `market-pattern-library.md` is split/indexed under `market-patterns/`, and references remain advisory without overriding contracts, evidence, routing, or IC Action. |
| P10-QA-01 | Run full acceptance and failure scenarios. | P3-EVD-01; P4-RTE-01; P5-AGT-01; P8-IC-01 | QA | All route/evidence/agent/IC invariants pass. |

## 4. Defaults

- No MVP framing.
- Agents-first implementation, not backend/UI.
- Canonical docs should be created before editing all legacy PRDs.
- Project Markdown documents should be in English unless explicitly requested otherwise.
- Russian remains acceptable for user chat.
