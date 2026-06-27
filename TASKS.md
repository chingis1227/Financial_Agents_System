# TASKS — Financial Agent System Implementation

Source: `IMPLEMENTATION_BACKLOG.md`  
Scope: Full agents-first financial analysis system implementation.  
Rule: No MVP reduction; implementation targets agent contracts, workflow contracts, evidence rules, report schemas, handoff rules, and acceptance tests.

## Stage 0 — Documentation Control

**Goal:** Separate active implementation documents from draft, backup, archive, and audit files.

**Tasks:**
- Adopt `implementation/01-documentation-control.md` as the documentation registry.
- Assign every legacy document one implementation status: `Canonical`, `Supporting Reference`, `Draft Source`, `Archive`, `Needs Merge`, or `Needs Split`.
- Exclude `prd.backup-before-full-target-language-20260625.md` and `final-architecture-audit.md` from source-of-truth use.
- Treat missing legacy references as non-active unless explicitly created later.

**Done when:**
- Active documents are obvious.
- Backup and audit files are excluded from source-of-truth use.
- Implementation precedence is documented.

## Stage 1 — Canonical Architecture Layer

**Goal:** Establish one canonical architecture model for implementation.

**Tasks:**
- Use `implementation/02-canonical-architecture.md` as the architecture layer.
- Treat `prd.md` as product-level draft source, not architecture truth.
- Treat `system-architecture-map.md` as draft source superseded by canonical implementation docs where conflicts exist.
- Enforce owner/contributor boundaries and workflow-controlled handoffs.
- Standardize base statuses: `Complete`, `Limited`, `Blocked`, `Preliminary`.
- Standardize decision labels: `Specialist Verdict`, `Actionability Label`, `Investment View`, `IC Action`, `Vehicle Quality Verdict`.

**Done when:**
- Every agent has a category, owner boundary, and handoff role.
- Final investment decision support passes through evidence, relevant specialists, and IC synthesis.

## Stage 1A — Codex Runtime Architecture Layer

**Goal:** Package the canonical financial-agent architecture into an OpenAI Codex-native project structure.

**Tasks:**
- Adopt `implementation/13-codex-runtime-architecture.md` as the Codex runtime architecture layer.
- Define root `AGENTS.md` as the concise source-of-truth navigator for Codex.
- Define root `README.md` as the human-readable project map.
- Define `.codex/agents/` for 20 project-scoped custom Codex agents.
- Define `.agents/skills/` for repo-scoped reusable Codex skills.
- Map each planned agent/router contract to a thin custom-agent TOML file.
- Map each canonical method-skill contract to a focused `SKILL.md` file.
- Preserve canonical implementation documents as source of truth and legacy PRDs as supporting source material only.

**Done when:**
- Codex can start from `AGENTS.md` and know which canonical documents to read.
- The project has a documented path for `AGENTS.md`, `README.md`, `.codex/agents/*.toml`, `.agents/skills/*/SKILL.md`, and workflow runbooks.
- Custom agents are narrow adapters, not full PRD copies.
- Skills are focused reusable workflows with explicit triggers, inputs, outputs, guardrails, and quality checks.
- Legacy PRDs do not become runtime source of truth unless routed through the registry and traceability matrix.

## Stage 2 — Standard Contract Templates

**Goal:** Make all future agent, workflow, skill, and report documents follow one structure.

**Tasks:**
- Adopt `implementation/03-contract-templates.md`.
- Normalize legacy Agent PRDs, Skill PRDs, Workflow docs, and Framework docs into standard contracts.
- Add explicit inputs, outputs, failure states, handoffs, and success criteria where missing.

**Done when:**
- Implementers can understand responsibilities, inputs, outputs, and completion conditions without guessing.

## Stage 3 — Evidence Layer

**Goal:** Make Evidence Collector the factual-control layer.

**Tasks:**
- Adopt `implementation/04-evidence-layer.md`.
- Use Source Registry as the default source hierarchy authority.
- Keep domain source frameworks as overlays only.
- Require material-claim support status and pre-IC evidence lock for final memos.

**Done when:**
- Missing, stale, paywalled, proxy, or contradictory evidence constrains output instead of being hidden.

## Stage 4 — Router and Workflow Layer

**Goal:** Give user requests deterministic route selection.

**Tasks:**
- Adopt `implementation/05-routing-and-workflows.md`.
- Normalize Master Intake, Asset Intake, Theme Intake, and direct specialist-call behavior.
- Use workflow contracts instead of improvised agent-to-agent calls.

**Done when:**
- Router selects workflows and does not make investment decisions.
- Ambiguous requests trigger clarification or safe bounded default behavior.

## Stage 5 — Asset-Class Agent Layer

**Goal:** Make asset-class agents contract-ready.

**Tasks:**
- Normalize Equity, ETF, Fixed Income, Commodity, and Crypto packages using `implementation/06-agent-contracts.md`.
- Remove repeated content between Agent PRD, Method Skill, and Framework during future cleanup.
- Add missing success criteria and explicit input/output contracts.
- Preserve the rule that asset agents produce specialist outputs, not final IC actions.

**Done when:**
- Each asset class has one lead agent.
- Each asset output can be consumed by Risk, Valuation, Portfolio Fit, and IC where relevant.

## Stage 6 — Specialist Agent Layer

**Goal:** Ensure cross-functional agents strengthen workflows without overriding Evidence or IC.

**Tasks:**
- Normalize Valuation, Risk, News, Positioning, Macro, Portfolio Fit, Market Sense, Driver Dominance, and Market Intelligence contracts.
- Clarify trigger conditions, required inputs, handoff blocks, and Limited/Blocked behavior.
- Keep each specialist inside its decision boundary.

**Done when:**
- Specialist agents cannot silently override Evidence Collector readiness or IC synthesis.

## Stage 7 — Theme and Discovery Layer

**Goal:** Make theme-first and discovery workflows implementable.

**Tasks:**
- Normalize Sector & Industry Analysis and Structural Winners Discovery contracts.
- Preserve discovery boundary: candidates are not investment-actionable until asset-level evidence, valuation, risk, and IC synthesis are complete.
- Define theme-to-asset handoff.

**Done when:**
- Theme workflows produce maps, candidates, and monitoring plans without hidden buy/sell recommendations.

## Stage 8 — Investment Committee Layer

**Goal:** Make IC the final synthesis and decision-support layer.

**Tasks:**
- Adopt `implementation/07-investment-committee-and-report-schemas.md`.
- Require evidence lock and relevant specialist reports before Complete Final Memo.
- Enforce positive-action gate.

**Done when:**
- IC cannot invent facts outside evidence and specialist reports.
- Final memo is decision-oriented, not an internal transcript.

## Stage 9 — Reference Library Cleanup

**Goal:** Ensure references support agents without becoming hidden PRDs.

**Tasks:**
- Adopt `implementation/08-reference-library-cleanup.md`.
- Add Owner / Used by metadata during future cleanup.
- Split large libraries only where navigation or ownership is unclear.

**Done when:**
- References are modular, searchable, and non-conflicting.

## Stage 10 — System Acceptance and QA

**Goal:** Test the system as a full agentic system.

**Tasks:**
- Adopt `implementation/09-system-acceptance-qa.md`.
- Run acceptance scenarios across asset, theme, direct specialist, market, and IC workflows.

**Done when:**
- Router, evidence, specialists, reports, statuses, and IC gates behave consistently across scenarios.

## Operational Work Register

| ID | Stage | Status | Work item | Depends on | Owner | Done criteria |
|---|---:|---|---|---|---|---|
| P0-DOC-01 | 0 | Done | Establish documentation registry and source-of-truth precedence. | None | Documentation control | Registry lists included legacy files, excludes archive/reminder files, documents precedence, and defines source-issue handling. |
| P0-DOC-02 | 0 | Done | Add traceability matrix from legacy corpus to canonical docs. | P0-DOC-01 | Documentation control | Every included legacy file maps to canonical destination and remaining gap. |
| P1-ARCH-01 | 1 | Done | Finalize canonical architecture and owner/contributor model. | P0-DOC-01 | Architecture | Agent categories, orchestration rule, and decision boundaries are explicit. |
| P1-RULE-01 | 1 | Done | Centralize statuses, gates, confidence, Action Box, evidence display, style, and artifact naming. | P1-ARCH-01 | Architecture | `implementation/00-master-rules.md` is the master rule authority. |
| P1A-CODEX-01 | 1A | Open | Define Codex-native runtime architecture and packaging rules. | P1-ARCH-01 | Codex runtime architecture | `implementation/13-codex-runtime-architecture.md` defines `AGENTS.md`, `README.md`, `.codex/agents`, `.agents/skills`, workflow runbooks, and source-of-truth routing rules. |
| P1A-CODEX-02 | 1A | Open | Create Codex-native project files and directories from canonical contracts. | P1A-CODEX-01; P5-AGT-01; P5-SKL-01 | Codex runtime architecture | Root `AGENTS.md` and `README.md` exist; 20 custom-agent TOML files and repo skill folders are generated from canonical contracts without copying full legacy PRDs. |
| P2-TPL-01 | 2 | Open | Standardize Agent, Skill, Workflow, and Report templates. | P1-RULE-01 | Documentation control | Implementers can normalize all PRDs without inventing fields. |
| P3-EVD-01 | 3 | Open | Canonicalize evidence model, source hierarchy, readiness, and pre-IC lock. | P1-RULE-01 | Evidence Collector | Evidence layer defines claim support, freshness, missing data, and allowed IC status. |
| P4-RTE-01 | 4 | Open | Canonicalize master, asset, theme, and direct-specialist routing. | P1-ARCH-01; P3-EVD-01 | Router layer | Every request family has deterministic route and safe fallback. |
| P5-AGT-01 | 5–7 | Open | Normalize router, evidence, asset, specialist, discovery, and IC agent contracts. | P2-TPL-01; P4-RTE-01 | Agent layer | Each agent has inputs, outputs, evidence, handoffs, Limited/Blocked rules, success criteria. |
| P5-SKL-01 | 2, 5–7 | Open | Normalize all method-skill contracts. | P2-TPL-01; P5-AGT-01 | Skill layer | Each method skill has trigger, inputs, steps, output, guardrails, quality checks. |
| P8-IC-01 | 8 | Open | Canonicalize IC memo and report schemas. | P3-EVD-01; P5-AGT-01 | IC layer | Final memo uses `final_investment_memo.md`, Action Box, confidence, gates, and source limits. |
| P9-REF-01 | 9 | Open | Govern reference libraries and split/index large references where needed. | P0-DOC-02 | Reference layer | References have owner/used-by metadata and do not override contracts. |
| P10-QA-01 | 10 | Open | Run full acceptance and failure scenarios. | P3-EVD-01; P4-RTE-01; P5-AGT-01; P8-IC-01 | QA | All route/evidence/agent/IC invariants pass. |
