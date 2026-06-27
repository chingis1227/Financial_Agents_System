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

### 2026-06-28 ? P1-RULE-01 Top-30 edge-case decisions

- Decision source: user edge-case review for P1-RULE-01.
- Rule: The 30 approved edge cases for statuses, gates, confidence, Action Box, evidence display, style, artifact naming, user-context behavior, specialist boundaries, risk gate failure, sizing, discovery ranking, private data, and source-of-truth handling are canonicalized in the master rules.
- Rationale: Converts chat-only product decisions into durable implementation behavior and prevents agents, workflows, skills, and reports from applying inconsistent output rules.
- Canonical location: `implementation/00-master-rules.md`.
- Scope note: This log is a supporting record only and does not override the canonical master rules.

