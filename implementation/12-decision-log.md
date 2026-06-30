# Implementation Decision Log

Status: Supporting implementation record

## Purpose

This log records product and implementation-governance decisions that explain why canonical documentation rules were chosen.

This document is not a source-of-truth authority over canonical implementation documents. If this log conflicts with a canonical document, the canonical document governs and the conflict should be treated as a source warning.

## Decision format

Each decision should include:

- Date
- Decision source
- Rule
- Rationale
- Canonical location

## Decisions

P1-ARCH-01 traceability note: the grouped decisions below for fast decision support, missing context, evidence constraints, specialist conflict resolution, theme / comparison / portfolio / update behavior, and valuation / implementation behavior correspond to the 25 approved edge-case rows in `implementation/02-canonical-architecture.md` section 8.

### 2026-06-27 — Documentation source precedence

- Decision source: user discussion.
- Rule: Canonical documents govern over Supporting References, Needs Split, Needs Merge, Draft Source, and Archive documents.
- Rationale: Prevents hidden second sources of truth and keeps agent behavior predictable.
- Canonical location: `implementation/01-documentation-control.md`.

### 2026-06-27 — Conflict handling

- Decision source: user discussion.
- Rule: When non-canonical material conflicts with canonical material, apply the canonical rule and show a source warning.
- Rationale: Keeps implementation safe while preserving visibility into useful conflicts.
- Canonical location: `implementation/01-documentation-control.md`.

### 2026-06-27 — Missing and stale references

- Decision source: user discussion.
- Rule: Missing legacy references resolve to the closest canonical document only where the registry defines a safe mapping; stale or similar files are not used as source of truth without confirmation.
- Rationale: Avoids hallucinated dependencies and accidental promotion of legacy files.
- Canonical location: `implementation/01-documentation-control.md`.

### 2026-06-27 — Archive and backup handling

- Decision source: user discussion.
- Rule: Archive, backup, audit, and reminder/operator-note files are excluded from source-of-truth use. They may be reviewed as idea sources only by explicit request.
- Rationale: Preserves useful historical ideas without reintroducing obsolete rules.
- Canonical location: `implementation/01-documentation-control.md`.

### 2026-06-27 — Needs Merge and Draft Source behavior

- Decision source: user discussion.
- Rule: Useful requirements in Needs Merge or Draft Source documents are proposed additions / pending decisions, not active working rules.
- Rationale: Supports future consolidation without letting unmerged PRDs govern runtime behavior.
- Canonical location: `implementation/01-documentation-control.md`.

### 2026-06-27 — Needs Split behavior

- Decision source: sub-agent review follow-up.
- Rule: Needs Split documents may be used only as advisory reference material until split / indexed; they do not override canonical rules.
- Rationale: Large unsplit references can support analysis without becoming hidden implementation contracts.
- Canonical location: `implementation/01-documentation-control.md`.

### 2026-06-27 — TASKS.md role

- Decision source: sub-agent review follow-up.
- Rule: `TASKS.md` is an operational work queue and task status tracker. `IMPLEMENTATION_BACKLOG.md` governs phase meaning and scope when the two differ.
- Rationale: Keeps task status visible without making the task list a competing architecture source of truth.
- Canonical location: `implementation/01-documentation-control.md`.

### 2026-06-27 — Source issue severity

- Decision source: user discussion.
- Rule: Source issues use Info, Warning, and Blocking severity. Blocking applies only when the issue affects the current task and can change the result.
- Rationale: Maintains strict internal governance without unnecessary workflow stoppages.
- Canonical location: `implementation/01-documentation-control.md`.

### 2026-06-27 — User-facing source issue UX

- Decision source: user discussion.
- Rule: User-facing answers show a short `Source issues` summary by default, with details available on request.
- Rationale: Keeps the external UX clean while preserving transparency.
- Canonical location: `implementation/01-documentation-control.md`.

### 2026-06-27 — Documentation-control Done criteria

- Decision source: user discussion.
- Rule: P0-DOC-01 can be Done when registry, exclusions, precedence, issue handling, and manual acceptance checks are documented, even if classified warnings or future traceability gaps remain.
- Rationale: Keeps P0-DOC-01 focused on source-of-truth control and avoids merging later backlog stages into the first task.
- Canonical location: `implementation/01-documentation-control.md`.

### 2026-06-27 — Change control

- Decision source: user discussion.
- Rule: Documentation-control rules change through explicit change requests that update canonical documentation and this decision log.
- Rationale: Prevents chat-only decisions from silently changing implementation truth.
- Canonical location: `implementation/01-documentation-control.md`.

### 2026-06-27 — Discussion versus implementation workflow

- Decision source: user discussion.
- Rule: When the user asks only to discuss, plan, or review, do not edit repository files. Implementation starts only after explicit implementation instruction.
- Rationale: Separates product decision-making from repository mutation.
- Canonical location: `implementation/01-documentation-control.md`.

### 2026-06-27 — Codex runtime architecture layer

- Decision source: user request to align the project with official OpenAI Codex documentation for `AGENTS.md`, skills, and subagents.
- Rule: The project should add a Codex-native runtime layer with root `AGENTS.md`, root `README.md`, `.codex/agents/*.toml`, `.agents/skills/*/SKILL.md`, and workflow runbooks, while keeping canonical implementation documents as the source of truth and legacy PRDs as supporting source material only.
- Rationale: Codex needs concise durable project guidance, focused repo skills, and narrow custom agents. Copying full PRDs into runtime files would increase context load and create competing sources of truth.
- Canonical location: `implementation/13-codex-runtime-architecture.md`.

### 2026-06-27 — Fast decision support and IC action boundary

- Decision source: user edge-case review for P1-ARCH-01.
- Rule: Fast Preliminary / Quick Take outputs are allowed, including personalized decision-support when user context is supplied, but final `IC Action` belongs only to the Investment Committee after required gates.
- Rationale: Preserves user speed while preventing premature buy / sell / hold instructions.
- Canonical location: `implementation/00-master-rules.md`, `implementation/02-canonical-architecture.md`, `implementation/05-routing-and-workflows.md`.

### 2026-06-27 — Missing context and user-facing status UX

- Decision source: user edge-case review for P1-ARCH-01.
- Rule: When horizon, risk tolerance, objective, position context, portfolio data, or definition of "best" is missing, the system should provide bounded analysis with explicit assumptions or ask the minimum clarifying question. Internal statuses must be paired with plain-language user-facing labels.
- Rationale: Keeps outputs useful to non-technical users without misrepresenting confidence or finality.
- Canonical location: `implementation/00-master-rules.md`, `implementation/02-canonical-architecture.md`, `implementation/05-routing-and-workflows.md`.

### 2026-06-27 — Evidence constraints, freshness, conflicts, and unavailable data

- Decision source: user edge-case review for P1-ARCH-01.
- Rule: Current evidence is collected by default when material. Stale, conflicting, paywalled, private, or weak evidence constrains the output to Preliminary, Limited, or Blocked. Material conflicts must be shown, source hierarchy applied, and missing premium data handled through a Public-data view plus checklist.
- Rationale: Prevents unsupported confidence while preserving useful analysis when full data is unavailable.
- Canonical location: `implementation/00-master-rules.md`, `implementation/02-canonical-architecture.md`, `implementation/05-routing-and-workflows.md`.
- Dependency note: detailed source hierarchy, evidence readiness, freshness, and evidence-lock mechanics remain governed by `implementation/04-evidence-layer.md` and the follow-on P3-EVD-01 task.

### 2026-06-27 — Specialist, evidence, risk, and IC conflict resolution

- Decision source: user edge-case review for P1-ARCH-01.
- Rule: Direct specialist calls are allowed inside scope, but specialists do not issue final action. Evidence Collector owns readiness. Risk can create a gate failure. IC resolves synthesis conflicts but cannot ignore failed gates or invent facts.
- Rationale: Maintains clear owner / contributor boundaries while allowing disagreement to improve analysis.
- Canonical location: `implementation/02-canonical-architecture.md`, `implementation/05-routing-and-workflows.md`.

### 2026-06-27 — Theme, comparison, portfolio, and update workflow behavior

- Decision source: user edge-case review for P1-ARCH-01.
- Rule: Theme discovery may rank candidates and assign Actionability Labels, but candidates are not actionable until asset workflow and IC. Cross-asset comparisons use asset-class owners and scenario summaries. Unknown portfolios receive generic fit plus checklist. Update requests use delta-update and renew IC review when changes are material.
- Rationale: Prevents discovery, comparison, and update workflows from becoming hidden recommendations.
- Canonical location: `implementation/02-canonical-architecture.md`, `implementation/05-routing-and-workflows.md`.

### 2026-06-27 — Valuation equivalents, time horizon, implementation quality, and memo depth

- Decision source: user edge-case review for P1-ARCH-01.
- Rule: Each asset class uses an appropriate valuation equivalent or expectations analysis. High-quality assets can still receive non-IC Watchlist / Defer signals when price is unfavorable, while final Watchlist / Defer action labels belong to IC. Final IC Action requires Time Horizon. Weak implementation quality can prevent positive action. Final memos stay readable, with details in appendices or deep dives.
- Rationale: Separates asset quality from investment attractiveness and keeps decision outputs practical.
- Canonical location: `implementation/00-master-rules.md`, `implementation/02-canonical-architecture.md`, `implementation/05-routing-and-workflows.md`.

### 2026-06-28 - P1-RULE-01 Top-30 edge-case decisions

- Decision source: user edge-case review for P1-RULE-01.
- Rule: The 30 approved edge cases for statuses, gates, confidence, Action Box, evidence display, style, artifact naming, user-context behavior, specialist boundaries, risk gate failure, sizing, discovery ranking, private data, and source-of-truth handling are canonicalized in the master rules with stable IDs `P1-RULE-01-01` through `P1-RULE-01-30`.
- Rationale: Converts chat-only product decisions into durable implementation behavior and prevents agents, workflows, skills, and reports from applying inconsistent output rules.
- Canonical location: `implementation/00-master-rules.md`.
- Scope note: This log is a supporting record only and does not override the canonical master rules.

### 2026-06-28 - P1A-CODEX-01 Top-35 runtime edge-case decisions

- Decision source: user edge-case review for P1A-CODEX-01.
- Rule: The 35 approved Codex runtime edge cases for project-root discovery, source-of-truth routing, runtime generation gates, custom-agent and skill boundaries, evidence/freshness controls, user-context UX, reporting gates, monitoring, asset complexity, sparse data, and ambiguity handling are canonicalized with stable IDs `P1A-CODEX-01-01` through `P1A-CODEX-01-35`.
- Rationale: Converts chat-only Codex runtime decisions into durable architecture behavior and prevents premature runtime generation, hidden source-of-truth drift, and unsupported final investment outputs.
- Canonical location: `implementation/13-codex-runtime-architecture.md`.
- Scope note: This log is a supporting record only and does not override the canonical Codex runtime architecture.

### 2026-06-28 - P2-TPL-01 Top-35 template edge-case decisions

- Decision source: user edge-case review for P2-TPL-01.
- Rule: The 35 approved template edge cases for practical gap handling, compact runtime contracts, metadata headers, UX blocks, agent/skill separation, category-specific add-ons, evidence failure states, direct specialist boundaries, Quick Takes, gate-aware artifacts, ambiguity, freshness, source restrictions, conflicts, user files, scoped workflows, structured handoffs, decision-label permissions, discovery boundaries, complex products, asset-specific gates, and scenario-based QA are canonicalized with stable IDs `P2-TPL-01-01` through `P2-TPL-01-35`.
- Rationale: Converts chat-only product decisions into durable template behavior so later P5 agent normalization, P5-SKL skill normalization, and report/workflow work do not require implementers to invent missing fields or hidden behavior.
- Canonical location: `implementation/03-contract-templates.md`.
- QA location: `implementation/09-system-acceptance-qa.md`.
- Scope note: This log is a supporting record only and does not override the canonical Standard Contract Templates.

### 2026-06-28 - P3-EVD-01 Top-25 evidence-layer edge-case decisions

- Decision source: user edge-case review for P3-EVD-01.
- Rule: The 25 approved evidence-layer edge cases for incomplete evidence, source conflicts, freshness, paywalls, user-provided files, proxy evidence, conclusion strength, early red flags, materiality mapping, IC evidence requests, source scope, event refreshes, comparison parity, evidence snapshots, domain overlays, concise answers, specialist evidence limits, layered evidence display, exact-claim support, negative evidence, rumors/social, user shortcuts, model outputs, instrument identity, and numeric normalization are canonicalized with stable IDs `P3-EVD-01-01` through `P3-EVD-01-25`.
- Rationale: Converts chat-only product decisions into durable evidence behavior so downstream agents, workflows, skills, and IC synthesis cannot overstate unsupported claims or bypass evidence readiness.
- Canonical location: `implementation/04-evidence-layer.md`.
- QA location: `implementation/09-system-acceptance-qa.md`.
- Scope note: This log is a supporting record only and does not override the canonical Evidence Layer Contract.

### 2026-06-28 - P4-RTE-01 Top-20 routing edge-case decisions

- Decision source: user edge-case review for P4-RTE-01.
- Rule: The 20 approved routing edge cases for Quick Takes, personal context, ambiguous instruments, theme discovery, comparisons, direct specialists, market updates, freshness, source conflicts, sizing, update workflows, premature final memos, run-all-agents requests, complex products, missing horizons, source restrictions, risk gate failures, quality-versus-valuation separation, valuation equivalents, and multi-workflow requests are canonicalized with stable IDs `P4-RTE-01-01` through `P4-RTE-01-20`.
- Rationale: Converts chat-only product routing decisions into durable workflow behavior so routers choose deterministic routes, safe fallbacks, status limits, and escalation paths without issuing final investment actions.
- Canonical location: `implementation/05-routing-and-workflows.md`.
- QA location: `implementation/09-system-acceptance-qa.md`.
- Scope note: This log is a supporting record only and does not override the canonical Routing and Workflow Contracts.

### 2026-06-28 - P5-AGT-01 Top-20 agent-contract edge-case decisions

- Decision source: user edge-case review for P5-AGT-01.
- Rule: The 20 approved agent-contract edge cases for Quick Takes, instrument ambiguity, freshness, specialist boundaries, missing upstream inputs, discovery boundaries, evidence conflicts, sizing, complex products, source restrictions, value traps, growth expectations, agent/skill separation, hybrid ownership, run-all-agents routing, dual statuses, structured handoffs, prior memo updates, premature final reports, and multi-workflow requests are canonicalized with stable IDs `P5-AGT-01-01` through `P5-AGT-01-20`.
- Rationale: Converts chat-only product decisions into durable agent-contract behavior so runtime agents stay useful while preserving evidence, workflow, and IC boundaries.
- Canonical location: `implementation/06-agent-contracts.md`.
- QA location: `implementation/09-system-acceptance-qa.md`.
- Runtime location: `.codex/agents/*.toml` thin adapters synchronized to the canonical contracts.
- Scope note: This log is a supporting record only and does not override the canonical agent contracts.


### 2026-06-28 - P5-SKL-01 Top-29 skill-contract edge-case decisions

- Decision source: user edge-case review for P5-SKL-01.
- Rule: The 29 approved skill-contract edge cases for skill visibility, missing data, compact runtime adapters, direct skill calls, buy/sell boundaries, freshness, user files, discovery ranking, hybrid instruments, evidence conflicts, output shape, known gaps, workflow depth, sizing, complex products, ownership separation, premature final reports, source restrictions, scoped Complete status, P8 schema separation, canonical authority, legacy treatment, Method Confidence, value/growth traps, rumors, portfolio privacy, run-all-agents behavior, and ambiguous instruments are canonicalized with stable IDs `P5-SKL-01-01` through `P5-SKL-01-29`.
- Rationale: Converts chat-only product decisions into durable method-skill behavior so runtime skills remain useful and concise while preserving evidence, workflow, agent, and IC boundaries.
- Canonical location: `implementation/11-skill-contracts.md`.
- QA location: `implementation/09-system-acceptance-qa.md`.
- Runtime location: `.agents/skills/*/SKILL.md` concise adapters synchronized to the canonical skill contracts.
- Scope note: This log is a supporting record only and does not override the canonical skill contracts.

### 2026-06-28 - P8-IC-01 Top-20 IC report-schema edge-case decisions

- Decision source: user edge-case review for P8-IC-01.
- Rule: The 20 approved IC report-schema edge cases for premature final memos, Decision-Prep Box, Quick Takes, freshness, conflicts, unspecified decision mode, missing portfolio context, layered memos, scoped workflows, early negative disqualifiers, sizing limits, specialist boundaries, materiality-based modules, as-of/freshness display, controlled IC Action labels, Watchlist/Defer/Hold distinctions, Decision Confidence meaning, view-change triggers, prior memo updates, and detail depth are canonicalized with stable IDs `P8-IC-01-01` through `P8-IC-01-20`.
- Rationale: Converts chat-only product decisions into durable report-schema behavior so IC outputs remain useful and practical without masking Preliminary, Limited, or scoped outputs as final IC Actions.
- Canonical location: `implementation/07-investment-committee-and-report-schemas.md`.
- QA location: `implementation/09-system-acceptance-qa.md`.
- Scope note: This log is a supporting record only and does not override the canonical IC report schemas or master rules.


### 2026-06-28 - P9-REF-01 Top-20 reference-governance edge-case decisions

- Decision source: user edge-case review for P9-REF-01.
- Rule: The 20 approved reference-governance edge cases for reference authority, hybrid split/index behavior, primary owner plus contributors, Evidence Layer source authority, operational-ambiguity split criteria, canonical pointers, user-facing limitations, freshness tiers, analytical labels, primary/supporting reference selection, pragmatic done criteria, metadata plus central index, selective `Needs Merge` harvesting, header/index conflict handling, `Needs Split` advisory use, new unregistered references, targeted cleanup, provisional ownership, checklist plus keyword scan QA, and readiness-based status updates are implemented as P9 reference-library governance.
- Rationale: Converts chat-only product decisions into durable reference behavior so references enrich analysis without becoming hidden PRDs, hidden agents, source-of-truth policy, or IC decision layers.
- Canonical location: `implementation/08-reference-library-cleanup.md`.
- Operational index: `implementation/reference-library-index.md`.
- Runtime reference split: `references/market-pattern-library.md` plus `references/market-patterns/*.md`.
- Scope note: This log is a supporting record only and does not override canonical implementation documents or the documentation registry.

### 2026-06-28 - P10-QA-01 acceptance execution and closure

- Decision source: user-approved P10 QA implementation plan and execution results.
- Rule: P10-QA uses synthetic fixtures for stable pass/fail, live-smoke checks only for freshness behavior, separate Safety and UX results, ask-first behavior for personal/final action with blocking missing context, concrete-asset investment-action Full Cycle behavior as superseded by P11-RUNTIME-01, Preliminary/Limited behavior only for non-concrete market setup or explicitly quick/short requests, IC-boundary severity, Limited/Blocked next-step blocks, compressed-but-not-removed limitations, gate-aware non-final artifacts, Hard Avoid only with strong disqualifying evidence, missing data as Defer / Not Actionable, and layered response depth.
- Rationale: Converts the final QA pass from a loose checklist into a repeatable acceptance model that tests system safety and product usefulness without relying on unstable market conclusions.
- Canonical location: `implementation/09-system-acceptance-qa.md`.
- Supporting execution record: `implementation/p10-qa-execution-report.md`.
- Runtime location: `implementation/13-codex-runtime-architecture.md` and root `AGENTS.md` navigator synchronized to the P10 policy.
- Completion note: P10-QA-01 passed with 0 blocking issues and 0 safety failures; remaining note is an Info-level pre-existing uncommitted-work record.
- Scope note: This log is a supporting record only and does not override canonical implementation documents.

### 2026-06-29 - P14-LANG language-and-style presentation layer

- Decision source: user-approved implementation plan for Language Policy + Investment Analytical Style.
- Rule: User-facing language selection, strict Russian output cleanup, and investment-analytical presentation style are canonicalized in `implementation/14-language-and-style.md` with stable IDs `P14-LANG-01` through `P14-LANG-10`.
- Rationale: Separates internal project documentation language from user-facing report language, makes Russian user-facing output clean and non-Run-glish, and applies investment-analytical style only as a presentation layer without replacing evidence, routing, analytical methods, or IC gates.
- Canonical location: `implementation/14-language-and-style.md`.
- QA location: `implementation/09-system-acceptance-qa.md`.
- Runtime location: `.agents/skills/language-policy/SKILL.md`, `.agents/skills/investment-analytical-style/SKILL.md`, root `AGENTS.md`, and `implementation/13-codex-runtime-architecture.md`.
- Scope note: This log is a supporting record only and does not override canonical implementation documents.

### 2026-06-29 - P11-RUNTIME-01 Full Cycle default for concrete-asset investment action requests

- Decision source: user-requested runtime audit and implementation plan after the Microsoft test prompt exposed a Quick Take / Full Cycle mismatch.
- Rule: Concrete-asset investment action requests default to Full Cycle unless the user explicitly asks for short / fast / quick take / no full cycle / preliminary. Missing non-blocking portfolio context does not stop the workflow; it limits Portfolio Fit and IC Action Status and defaults the output to `decision_prep_memo.md` when final personal action gates are incomplete.
- Rationale: The system already had agents, skills, evidence rules, and IC schemas, but the runtime allowed a silent Quick Take for prompts where the user expected the full agent workflow. This decision makes orchestration explicit and auditable.
- Canonical location: `implementation/05-routing-and-workflows.md`, `implementation/07-investment-committee-and-report-schemas.md`, `implementation/13-codex-runtime-architecture.md`, and root `AGENTS.md`.
- QA location: `implementation/09-system-acceptance-qa.md` and `implementation/p10-qa-execution-report.md`.
- Runtime location: `.codex/agents/*.toml` selected adapters and relevant `.agents/skills/*/SKILL.md` method adapters.
- Scope note: This log is a supporting record only and does not override canonical implementation documents.

### 2026-06-29 - Session 04 mandatory handoff artifact standard

- Decision source: user-requested Session 04 implementation plan for making every agent leave a verifiable result.
- Rule: Full Cycle and Full Agent Workflow modules must produce structured handoff artifacts or artifact-equivalent summaries with the controlled fields in `workflows/handoff_artifact_standard.md`, including artifact name, owner, output status, evidence status, evidence limits, key limitations, missing gates, decision boundary, downstream handoff, and required follow-up. Equity Full Cycle minimum artifacts are `evidence_pack.md`, `equity_company_analysis.md`, `financial_statement_analysis.md`, `valuation_expectations.md`, `risk_red_team.md`, `portfolio_fit.md`, and one IC-stage gate-aware artifact: `decision_prep_memo.md` by default when portfolio context is the remaining final-action gate, otherwise `limited_ic_draft.md`, `evidence_gap_memo.md`, or `final_investment_memo.md` only when IC schemas allow it.
- Rationale: IC synthesis must be auditable and may not rely on uncontrolled agent-to-agent chat, hidden assumptions, or non-IC outputs that sound like final buy/sell/hold decisions.
- Runtime standard: `workflows/handoff_artifact_standard.md`.
- Canonical synchronization: `implementation/00-master-rules.md`, `implementation/05-routing-and-workflows.md`, `implementation/06-agent-contracts.md`, `implementation/07-investment-committee-and-report-schemas.md`, `implementation/09-system-acceptance-qa.md`, `implementation/13-codex-runtime-architecture.md`, and root `AGENTS.md`.
- Scope note: This log is a supporting record only and does not override canonical implementation documents.


### 2026-06-29 - Session 07 root PRD cleanup

- Decision source: user-requested Session 07 implementation plan for cleaning root-level PRD chaos.
- Rule: Former root-level PRD, draft-source, backup, and audit Markdown files are retired from the project root and retained under `archive/legacy-prd/`; active advisory frameworks, playbooks, source overlays, and market-pattern split files live under `references/`; residual candidate requirements from retired PRDs are centralized in `implementation/remaining-requirements.md`.
- Rationale: Keeps the project root navigable while preserving provenance and preventing legacy PRDs from silently acting as source of truth after canonical implementation documents, agents, skills, workflow runbooks, and QA have been normalized.
- Canonical synchronization: `implementation/01-documentation-control.md`, `implementation/10-traceability-matrix.md`, `implementation/08-reference-library-cleanup.md`, and `implementation/reference-library-index.md`.
- Handling rule: Archived files are provenance only; residual requirements must be promoted through canonical change control before changing runtime behavior.
- Scope note: This log is a supporting record only and does not override canonical implementation documents.

