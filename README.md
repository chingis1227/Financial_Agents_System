# Financial Agent System

The Financial Agent System is an agents-first financial analysis project. It packages canonical implementation documents into Codex-native project instructions, thin custom agents, reusable repo skills, and workflow runbooks while preserving evidence discipline and Investment Committee boundaries.

## Quick start for users

Use the system from the project root and ask for one of three request modes. By canonical default, ordinary concrete-asset investment-action requests should run as a delegated workflow with relevant subagents when subagent tooling is available; `Single-agent Full Cycle` is the fallback when subagents are unavailable or are not actually spawned.

| Mode | When to use | What the system should do | Output boundary |
|---|---|---|---|
| `Quick Take` | You ask for a short, fast, preliminary view. | Give a concise `Preliminary` or `Limited` answer using only the evidence that can be handled safely in a quick pass. For today/now/latest requests, it still needs current timestamps or must be marked `Limited` / `Blocked`. | Not a final buy/sell decision and not a full Investment Committee action. |
| `Full Cycle` | You ask whether to invest, buy, add, hold, sell, or assess an asset over a multi-year horizon. | Run the full analytical sequence: intake, evidence, lead asset analysis, financial statements when material, valuation, risk, portfolio fit or limited portfolio fit, and Investment Committee synthesis. When subagent tooling is available, the canonical default is delegated execution with relevant subagents; otherwise it falls back to a single-session execution. | Gate-aware output. Audit metadata records either `Delegated Full Agent Workflow` or `Single-agent Full Cycle` based on what actually ran. |
| `Delegated Full Agent Workflow` | The workflow actually spawns relevant subagents. Concrete-asset Full Cycle should default to this mode when subagents are available; the user may also request it directly with words such as `Full Agent Workflow`, `subagents`, `delegated workflow`, or `run the relevant agents`. | Spawn the relevant available subagents, collect structured handoff artifacts or summaries, and synthesize only from those handoffs plus the evidence lock. | Audit/debug materials record `Execution mode: Delegated Full Agent Workflow`, the agents actually used, omitted agents with reasons, and the handoffs consumed. Ordinary user-facing chat hides these technical blocks unless requested. If subagents are unavailable or not actually spawned, audit metadata must say so and fall back to `Single-agent Full Cycle` or `Limited`. |

Which prompt should you use?

- Want a short preliminary view? Ask for `Quick Take`.
- Want full analysis? Ask for `Full Cycle`, or simply ask an investment-action question. The runtime should use relevant delegated subagents when available; if no subagents are actually spawned, it must record `Single-agent Full Cycle`.
- Want real spawned subagents? Explicitly ask for `Delegated Full Agent Workflow`, `подагенты`, `отдельные агенты`, or `запусти нужных агентов`.

Important distinction: `Full Cycle` is the analytical route; `Delegated Full Agent Workflow` is the runtime mode where subagents are actually spawned. A normal concrete-asset investment request should default to delegated execution when relevant subagents are available; if no subagents actually run, the audit must say `Single-agent Full Cycle`.

## Russian prompt templates

These templates are written for user-facing use. Controlled runtime labels and artifact filenames remain in English where the system expects exact names.

### Простые режимы работы

| Режим | Простыми словами |
|---|---|
| `Quick Take` | быстрый предварительный вывод. |
| `Single-agent Full Cycle` | полный анализ в одной сессии. |
| `Delegated Full Agent Workflow` | полный многоагентный запуск. |
| `decision_prep_memo.md` | мемо для подготовки решения. |

### ETF: QQQ vs SCHG

```text
полный многоагентный запуск: QQQ vs SCHG. мемо для подготовки решения: `decision_prep_memo.md`. Без финального buy/sell/hold.
```

### Commodity: золото

```text
полный многоагентный запуск по золоту. мемо для подготовки решения: `decision_prep_memo.md`.
```

### Crypto: BTC на 3 года

```text
полный многоагентный запуск: BTC на горизонт 3 года. мемо для подготовки решения: `decision_prep_memo.md`.
```

### Fixed income: TLT как bond ETF

```text
полный многоагентный запуск: TLT как bond ETF на длинные казначейские облигации США. мемо для подготовки решения: `decision_prep_memo.md`.
```

### Multi-asset: BTC, золото, QQQ и TLT

```text
полный многоагентный запуск: BTC, золото, QQQ и TLT на горизонт 3 года. мемо для подготовки решения: `decision_prep_memo.md`.
```

### Output naming rules in short

- Use `decision_prep_memo.md` when missing portfolio context is the remaining final-action gate.
- Use `evidence_gap_memo.md` when evidence or freshness gaps drive the limitation.
- Use `limited_ic_draft.md` when the analysis is useful but one or more non-portfolio gates remain open.
- Use `final_investment_memo.md` only when the Investment Committee gates pass under the canonical schemas.

## Current implementation status

- Active work is tracked in `TASKS.md`.
- Phase meaning and full implementation scope are tracked in `IMPLEMENTATION_BACKLOG.md`.
- Codex runtime packaging is governed by `implementation/13-codex-runtime-architecture.md`.
- Equity Full Cycle runtime execution is described in `workflows/equity_full_cycle.md`.
- Handoff artifacts are governed by `workflows/handoff_artifact_standard.md`.
- Runtime files are generated conservatively: navigation files are safe to use, while agents and skills are runtime-ready only when their canonical contracts pass readiness gates.

## Directory map

| Path | Purpose |
|---|---|
| `AGENTS.md` | Concise Codex navigator and runtime instruction entrypoint. |
| `README.md` | Human-readable project map and user prompt templates. |
| `TASKS.md` | Active work register and task status. |
| `IMPLEMENTATION_BACKLOG.md` | Phase scope and implementation roadmap. |
| `implementation/` | Canonical implementation layer and supporting control documents. |
| `references/` | Advisory frameworks, playbooks, source overlays, and split reference libraries. |
| `archive/legacy-prd/` | Retired PRDs, drafts, backups, and audit artifacts retained for provenance only. |
| `.codex/agents/` | Project-scoped thin custom-agent TOML files. |
| `.agents/skills/` | Repo-scoped reusable Codex skills. |
| `workflows/` | Executable workflow runbooks and handoff standards subordinate to canonical documents. |

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
| Residual candidate requirements | `implementation/remaining-requirements.md` |
| Skill contracts | `implementation/11-skill-contracts.md` |
| Decision history | `implementation/12-decision-log.md` |
| Codex runtime architecture | `implementation/13-codex-runtime-architecture.md` |
| User-facing language and presentation style | `implementation/14-language-and-style.md` |

## Runtime surfaces

Executable runtime workflow files live under `workflows/` when deliberately split out by a canonical task. Current runtime files include `workflows/equity_full_cycle.md` and `workflows/handoff_artifact_standard.md`; both remain subordinate to the canonical implementation documents.

- Custom agents are narrow adapters that point to canonical contracts and return status, key findings, limitations, handoffs, and next required steps.
- Repo skills are focused reusable workflows with triggers, inputs, steps, outputs, guardrails, Limited/Blocked behavior, and quality checks.
- Presentation skills under `.agents/skills/language-policy/` and `.agents/skills/investment-analytical-style/` control user-facing language cleanup and investment-analytical style; they do not replace analytical method skills or IC gates.
- Archived legacy PRDs under `archive/legacy-prd/` are provenance only; advisory frameworks and playbooks live under `references/` and are usable only through the documentation registry and traceability matrix.

## How to add or change runtime assets

1. Update or confirm the relevant canonical implementation document first.
2. Check `implementation/01-documentation-control.md` and `implementation/10-traceability-matrix.md` before using legacy detail.
3. Keep custom-agent TOML files thin; do not copy full PRDs or methodology libraries.
4. Keep skills focused on reusable method steps; do not let skills override agent, evidence, workflow, or IC boundaries.
5. If a runtime file conflicts with canonical documents, preserve the canonical rule and surface a source issue.
6. Use diff-aware, idempotent updates; do not silently overwrite manual edits.

## How to validate changes

- Confirm required runtime paths exist: `AGENTS.md`, `README.md`, `.codex/agents/`, `.agents/skills/`, and `workflows/`.
- Validate custom-agent TOML fields: `name`, `description`, and `developer_instructions`.
- Confirm custom agents remain thin and canonical-doc-driven.
- Confirm skills include YAML front matter and the required skill contract sections.
- Confirm README prompt templates preserve the three user-facing modes: `Quick Take`, `Full Cycle`, and `Delegated Full Agent Workflow`.
- Confirm Russian prompt templates render as Cyrillic UTF-8, not replacement question marks or mojibake.
- Run acceptance scenarios from `implementation/09-system-acceptance-qa.md`, especially routing, evidence readiness, specialist boundaries, freshness, conflict handling, ambiguity handling, and IC gates.
