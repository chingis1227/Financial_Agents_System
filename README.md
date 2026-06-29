# Financial Agent System

The Financial Agent System is an agents-first financial analysis project. It packages canonical implementation documents into Codex-native project instructions, thin custom agents, reusable repo skills, and workflow runbooks while preserving evidence discipline and Investment Committee boundaries.

## Current implementation status

- Active work is tracked in `TASKS.md`.
- Phase meaning and full implementation scope are tracked in `IMPLEMENTATION_BACKLOG.md`.
- Codex runtime packaging is governed by `implementation/13-codex-runtime-architecture.md`.
- Runtime files are generated conservatively: navigation files are safe to use, while agents and skills are runtime-ready only when their canonical contracts pass readiness gates.

## Directory map

| Path | Purpose |
|---|---|
| `AGENTS.md` | Concise Codex navigator and runtime instruction entrypoint. |
| `README.md` | Human-readable project map. |
| `TASKS.md` | Active work register and task status. |
| `IMPLEMENTATION_BACKLOG.md` | Phase scope and implementation roadmap. |
| `implementation/` | Canonical implementation layer and supporting control documents. |
| `.codex/agents/` | Project-scoped thin custom-agent TOML files. |
| `.agents/skills/` | Repo-scoped reusable Codex skills. |

## Canonical document map

| Need | Canonical source |
|---|---|
| Statuses, gates, confidence, source display, style, artifact naming | `implementation/00-master-rules.md` |
| Registry, precedence, archive behavior, source issues | `implementation/01-documentation-control.md` |
| Architecture and owner/contributor boundaries | `implementation/02-canonical-architecture.md` |
| Standard contract templates | `implementation/03-contract-templates.md` |
| Evidence model and readiness | `implementation/04-evidence-layer.md` |
| Routing and workflow behavior | `implementation/05-routing-and-workflows.md` |
| Agent contracts | `implementation/06-agent-contracts.md` |
| IC memo and report schemas | `implementation/07-investment-committee-and-report-schemas.md` |
| Reference cleanup rules | `implementation/08-reference-library-cleanup.md` |
| System acceptance and QA | `implementation/09-system-acceptance-qa.md` |
| Legacy routing and traceability | `implementation/10-traceability-matrix.md` |
| Skill contracts | `implementation/11-skill-contracts.md` |
| Decision history | `implementation/12-decision-log.md` |
| Codex runtime architecture | `implementation/13-codex-runtime-architecture.md` |

## Runtime surfaces

Workflow runbooks currently live in `implementation/05-routing-and-workflows.md` until a future `workflows/` folder is deliberately split out by a canonical task.

- Custom agents are narrow adapters that point to canonical contracts and return status, key findings, limitations, handoffs, and next required steps.
- Repo skills are focused reusable workflows with triggers, inputs, steps, outputs, guardrails, Limited/Blocked behavior, and quality checks.
- Legacy PRDs and frameworks are source material only when routed through the documentation registry and traceability matrix.

## How to add or change runtime assets

1. Update or confirm the relevant canonical implementation document first.
2. Check `implementation/01-documentation-control.md` and `implementation/10-traceability-matrix.md` before using legacy detail.
3. Keep custom-agent TOML files thin; do not copy full PRDs or methodology libraries.
4. Keep skills focused on reusable method steps; do not let skills override agent, evidence, workflow, or IC boundaries.
5. If a runtime file conflicts with canonical documents, preserve the canonical rule and surface a source issue.
6. Use diff-aware, idempotent updates; do not silently overwrite manual edits.

## How to validate changes

- Confirm required runtime paths exist: `AGENTS.md`, `README.md`, `.codex/agents/`, and `.agents/skills/`.
- Validate custom-agent TOML fields: `name`, `description`, and `developer_instructions`.
- Confirm custom agents remain thin and canonical-doc-driven.
- Confirm skills include YAML front matter and the required skill contract sections.
- Run acceptance scenarios from `implementation/09-system-acceptance-qa.md`, especially routing, evidence readiness, specialist boundaries, freshness, conflict handling, ambiguity handling, and IC gates.
