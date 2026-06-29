# Financial Agent System - Codex Project Instructions

This file is the Codex runtime navigator for the Financial Agent System. It is not the highest source of truth. When this file conflicts with canonical implementation documents, the canonical document governs and the conflict must be surfaced as a source issue under `implementation/01-documentation-control.md`.

## Project root discovery

Start Codex from the project root: `Financial Agent System/`. If Codex is launched from a nested folder, identify the root by looking for `TASKS.md`, `IMPLEMENTATION_BACKLOG.md`, and `implementation/`. If the root cannot be identified unambiguously, ask the user to reopen the project from the correct root instead of guessing.

## Project authority order

1. `implementation/00-master-rules.md` for statuses, gates, output standards, confidence, source display, style, and artifact naming.
2. `implementation/01-documentation-control.md` for registry, source precedence, archive behavior, and source issues.
3. `IMPLEMENTATION_BACKLOG.md` for phase meaning and implementation scope.
4. `TASKS.md` for active work status.
5. Other canonical implementation documents for their specific domains.
6. Supporting References only when they do not conflict with canonical documents.
7. Needs Merge / Draft Source documents only as source material.
8. Archive documents never as active source of truth.

## Runtime reading order

1. Read this `AGENTS.md` first as the concise navigator.
2. Read `implementation/01-documentation-control.md` when source status matters.
3. Read `implementation/00-master-rules.md` when global statuses, gates, style, source display, or artifact naming matter.
4. Read `IMPLEMENTATION_BACKLOG.md` when phase meaning or scope matters.
5. Read `TASKS.md` when active work status matters.
6. Read the specific canonical implementation document for the task domain.
7. Read `implementation/13-codex-runtime-architecture.md` when Codex runtime packaging, custom agents, repo skills, or edge-case runtime rules matter.
8. Read `implementation/10-traceability-matrix.md` before using legacy detail.
9. Use supporting legacy files only after registry and traceability routing.

## Core operating rules

- Codex runtime edge-case rules `P1A-CODEX-01-01` through `P1A-CODEX-01-35` live in `implementation/13-codex-runtime-architecture.md` and must be applied when relevant.
- No MVP reduction: implement the full agents-first financial analysis system scope unless canonical documents explicitly narrow a task.
- Evidence before synthesis: material claims require evidence status, freshness treatment, and source limitations before downstream conclusions.
- The Investment Committee owns final decision-support synthesis. Asset and specialist agents provide scoped outputs, not final IC Actions.
- Specialist buy/sell requests must return a scoped specialist verdict, state `Boundary: Not an IC Action`, list missing IC gates, and offer IC routing.
- Treat any final action language from non-IC agents or skills as a safety failure during QA, not as harmless wording.
- Quick answers are allowed only as `Preliminary` or `Limited` Quick Takes; do not present them as final buy/sell decisions.
- Classify action intent before answering: personal/final action with missing key context should ask the minimum clarifying question first; market-action / attractiveness requests may receive a Quick Take or Limited view; analysis-only requests should stay scoped with boundary and missing gates.
- Final-report requests before required gates are complete must use gate-aware artifact names such as `Preliminary Investment Brief`, `Limited IC Draft`, `Evidence Gap Memo`, `Specialist Summary`, or `Decision-Prep Memo`.
- Freshness-dependent requests such as today, now, latest, earnings, price action, or news require current sources with timestamps; otherwise mark the output `Limited` or `Blocked`.
- If the user restricts sources to provided material, respect the scope and mark the result `Limited by source scope`.
- Conflicting material sources require conflict protocol; do not treat disputed facts as fully supported until resolved.
- User-provided files require provenance and sanity checks before their claims are used as evidence.
- Limited or Blocked outputs should include a short practical next step; "no disclaimers" requests may compress limitations but must not remove status, evidence limits, missing gates, or boundaries.
- Missing information alone is `Defer / Not Actionable`, not `Hard Avoid`; Hard Avoid requires strong disqualifying evidence and IC ownership.

## Agent, skill, and workflow behavior

- Custom agents in `.codex/agents/` are thin role adapters. They must not copy full PRDs or override canonical documents.
- Repo skills in `.agents/skills/` are reusable methods. They must not issue final IC Actions unless an owning canonical IC contract allows it.
- If a task matches both a custom agent and a repo skill, the agent owns role, boundary, status, and handoff while the skill owns the reusable method.
- "Run all agents" means run the full relevant workflow selected by routing, not literally every agent. Explain included and excluded agents when useful.
- Subagents should be used only when explicitly requested by the user, workflow runbook, or operator.
- Handoffs must be structured artifacts, not uncontrolled agent-to-agent chat.

## Special analysis gates

Apply the relevant gate before strong positive conclusions:

- ambiguous ticker, listing, instrument, share class, maturity, currency, or structure;
- complex products such as leveraged/inverse ETFs, options strategies, structured notes, high-yield bonds, or crypto yield;
- private, illiquid, microcap, sparse-data, or poorly covered assets;
- cheap-looking assets that may be value traps;
- expensive growth assets that require a growth-expectations bridge;
- theses without a credible catalyst, path, or structural compounding logic.

## Language policy

Project Markdown files should be written in English unless explicitly requested otherwise. Russian is acceptable for user chat.
