# Codex Runtime Architecture

Status: Canonical Codex runtime architecture

## 1. Purpose

This document defines how the Financial Agent System should be packaged for OpenAI Codex using project instructions, repo-scoped skills, project-scoped custom agents, and workflow runbooks.

It does not replace the financial-agent architecture. It maps the canonical implementation layer into Codex-native operating surfaces so Codex can work reliably without reading the whole legacy PRD corpus on every task.

Official OpenAI references:

- Codex `AGENTS.md`: <https://developers.openai.com/codex/guides/agents-md>
- Codex skills: <https://developers.openai.com/codex/skills>
- Codex subagents and custom agents: <https://developers.openai.com/codex/subagents>

## 2. Runtime design principle

Use this pattern:

```text
AGENTS.md
  -> canonical implementation documents
  -> thin custom agents
  -> focused repo skills
  -> supporting legacy PRDs / frameworks only when routed through the registry
```

Runtime rule:

- `AGENTS.md` is the concise project guidance and source-of-truth navigator.
- `README.md` is the human-readable project map.
- `.codex/agents/*.toml` defines project-scoped custom Codex agents.
- `.agents/skills/*/SKILL.md` defines repo-scoped reusable Codex skills.
- `implementation/*.md` remains the canonical implementation layer.
- Legacy PRDs and frameworks remain source material or supporting references according to `implementation/01-documentation-control.md` and `implementation/10-traceability-matrix.md`.

Do not copy full PRDs into custom-agent TOML files or `SKILL.md` files. Custom agents and skills should point to canonical contracts and load supporting legacy material only when needed.

## 2A. Project-root discovery rule

Codex project instructions and repo skills depend on where Codex is launched and what it treats as the project root. For this project:

- Start Codex from the project root: `Financial Agent System/`.
- If the project is later converted into a Git repository, keep root `AGENTS.md`, `.codex/agents/`, and `.agents/skills/` at the Git root unless a deliberate nested override is documented.
- Do not assume root `AGENTS.md` or root repo skills will be discovered when Codex is launched directly from a nested folder such as `implementation/`.
- If nested operation becomes necessary, add a small nested `AGENTS.md` or runbook note that routes back to the root source-of-truth files.

## 3. Required project files

### Root `AGENTS.md`

Purpose: durable project guidance loaded by Codex before work starts.

Required content:

- project authority order;
- runtime reading order;
- rule that canonical implementation documents govern over legacy PRDs;
- instruction to use `TASKS.md` for active work status;
- instruction to use `IMPLEMENTATION_BACKLOG.md` for phase meaning and scope;
- instruction to use `implementation/01-documentation-control.md` and `implementation/10-traceability-matrix.md` before treating any legacy PRD as relevant;
- no-MVP rule;
- evidence-before-synthesis rule;
- Investment Committee final synthesis boundary;
- skill and subagent usage rules;
- language policy: project Markdown in English unless explicitly requested otherwise; Russian is acceptable for user chat.

Project authority order:

```text
1. implementation/00-master-rules.md for statuses, gates, output standards, confidence, source display, style, and artifact naming
2. implementation/01-documentation-control.md for registry, source precedence, archive behavior, and source issues
3. IMPLEMENTATION_BACKLOG.md for phase meaning and implementation scope
4. TASKS.md for active work status
5. Other canonical implementation documents for their specific domains
6. Supporting References only when they do not conflict with canonical documents
7. Needs Merge / Draft Source documents only as source material
8. Archive documents never as active source of truth
```

Runtime reading order:

```text
1. AGENTS.md as the concise navigator Codex loads first
2. implementation/01-documentation-control.md when source status matters
3. implementation/00-master-rules.md when global statuses, gates, style, or artifact naming matter
4. IMPLEMENTATION_BACKLOG.md when phase meaning or scope matters
5. TASKS.md when active work status matters
6. The specific canonical implementation document for the task domain
7. implementation/10-traceability-matrix.md before using legacy detail
8. Supporting legacy files only after registry / traceability routing
```

`AGENTS.md` is first in runtime reading order because Codex loads it first. It is not higher than canonical implementation documents in project authority.

### Root `README.md`

Purpose: human-readable orientation for maintainers and operators.

Required content:

- what the Financial Agent System is;
- current implementation status;
- directory map;
- canonical document map;
- planned Codex runtime surfaces;
- how to add or change agents, skills, workflows, and references;
- how to validate changes.

`README.md` is informational. It must not override canonical implementation documents.

### `.codex/agents/`

Purpose: project-scoped custom Codex agents.

Each custom agent must be a standalone TOML file with:

- `name`;
- `description`;
- `developer_instructions`.

Optional fields such as model, reasoning effort, sandbox, and skills should be omitted unless there is a documented project reason. Inheriting the parent session default is preferred unless a task explicitly requires a different model or execution profile.

Validation checks for future custom-agent TOML files:

- required fields exist: `name`, `description`, `developer_instructions`;
- `description` is narrow and trigger-oriented;
- `developer_instructions` points to canonical documents instead of copying full PRD content;
- no model, reasoning, sandbox, or tool override is included unless justified by the relevant runtime task;
- agent boundaries match `implementation/06-agent-contracts.md`;
- the file does not promote a legacy PRD, framework, or example above canonical documents.

### `.agents/skills/`

Purpose: repo-scoped reusable task workflows.

Each skill must be a directory containing `SKILL.md` with YAML front matter:

```md
---
name: skill-name
description: Clear trigger conditions and boundaries.
---
```

Each skill should include:

- purpose;
- when to use / when not to use;
- required canonical documents;
- required inputs;
- step sequence;
- output contract;
- guardrails;
- failure / Limited / Blocked behavior;
- quality checks.

Prefer instruction-only skills unless deterministic scripts are needed.

### Workflow runbooks

Workflow runbooks may live under a future `workflows/` folder or inside `implementation/05-routing-and-workflows.md` until split.

Each runbook should specify:

- entry condition;
- lead router / agent;
- required skills;
- optional custom agents;
- evidence requirements;
- sequence and parallelizable branches;
- handoff artifacts;
- completion rules;
- acceptance checks.

## 4. Custom-agent mapping

Create these 20 project-scoped custom-agent files when `P1A-CODEX-02` is executed.

| Planned contract | Custom-agent file | Runtime role |
|---|---|---|
| Master Intake Router | `.codex/agents/master-intake-router.toml` | Classifies user request and selects workflow; does not make investment decisions. |
| Asset Intake Router | `.codex/agents/asset-intake-router.toml` | Routes asset-first requests to the correct asset workflow. |
| Theme / Opportunity Intake Router | `.codex/agents/theme-opportunity-intake-router.toml` | Routes theme-first and opportunity-discovery requests. |
| Evidence Collector Agent | `.codex/agents/evidence-collector.toml` | Controls evidence collection, source status, and readiness. |
| Equity Agent | `.codex/agents/equity-agent.toml` | Produces equity specialist analysis. |
| ETF Agent | `.codex/agents/etf-agent.toml` | Produces ETF wrapper / exposure analysis. |
| Fixed Income Agent | `.codex/agents/fixed-income-agent.toml` | Produces bond / fixed-income specialist analysis. |
| Commodity Agent | `.codex/agents/commodity-agent.toml` | Produces commodity and commodity-linked exposure analysis. |
| Crypto Agent | `.codex/agents/crypto-agent.toml` | Produces crypto asset and crypto-linked exposure analysis. |
| Valuation & Expectations Agent | `.codex/agents/valuation-expectations-agent.toml` | Produces valuation and expectations analysis. |
| Risk / Red Team Agent | `.codex/agents/risk-red-team-agent.toml` | Challenges thesis quality and downside risks. |
| News & Catalysts Agent | `.codex/agents/news-catalysts-agent.toml` | Identifies recent and upcoming market-moving events. |
| Market Positioning Agent | `.codex/agents/market-positioning-agent.toml` | Assesses consensus, positioning, flows, and expectations where available. |
| Macro Agent | `.codex/agents/macro-agent.toml` | Assesses macro regime, sensitivity, and surprise context. |
| Portfolio Fit Agent | `.codex/agents/portfolio-fit-agent.toml` | Assesses portfolio role and fit without exact sizing. |
| Market Sense Agent | `.codex/agents/market-sense-agent.toml` | Produces market-behavior hypotheses without replacing evidence. |
| Market Intelligence Agent | `.codex/agents/market-intelligence-agent.toml` | Produces broad market intelligence briefings. |
| Sector & Industry Analysis Agent | `.codex/agents/sector-industry-analysis-agent.toml` | Produces sector / industry context. |
| Structural Winners Discovery Agent | `.codex/agents/structural-winners-discovery-agent.toml` | Produces candidate discovery, maps, and watchlists. |
| Investment Committee Agent | `.codex/agents/investment-committee-agent.toml` | Produces final decision-support synthesis subject to evidence and specialist gates. |

## 5. Custom-agent authoring standard

Each custom-agent TOML should be thin and should use this shape:

```toml
name = "agent-name"
description = "One-sentence trigger and scope."
developer_instructions = """
You are [Agent Name] for the Financial Agent System.

Before working, follow AGENTS.md and read only the canonical documents needed for the task:
- implementation/00-master-rules.md
- implementation/01-documentation-control.md
- implementation/02-canonical-architecture.md when architecture or boundaries matter
- implementation/05-routing-and-workflows.md when workflow routing matters
- implementation/06-agent-contracts.md for agent scope
- implementation/11-skill-contracts.md for method-skill behavior
- implementation/10-traceability-matrix.md when legacy detail is needed

Use the relevant repo skill when the task matches it.
Do not treat legacy PRDs as source of truth unless routed through the registry.
Do not override Evidence Collector readiness or Investment Committee boundaries.
Return status, key findings, evidence limitations, handoffs, and next required step.
"""
```

Do not include full legacy PRD content, large frameworks, or long methodology libraries inside `developer_instructions`.

## 6. Repo-skill mapping

Create repo skills from canonical skill contracts in `implementation/11-skill-contracts.md`.

Initial planned skills:

| Canonical skill contract | Skill folder |
|---|---|
| Evidence Collection Method Skill | `.agents/skills/evidence-collection/` |
| Equity Company Analysis Method Skill | `.agents/skills/equity-company-analysis/` |
| Financial Statement Analysis Skill | `.agents/skills/financial-statement-analysis/` |
| Valuation & Expectations Method Skill | `.agents/skills/valuation-expectations/` |
| Risk / Red Team Method Skill | `.agents/skills/risk-red-team/` |
| Investment Committee Synthesis Method Skill | `.agents/skills/investment-committee-synthesis/` |
| ETF Analysis Method Skill | `.agents/skills/etf-analysis/` |
| Fixed Income Analysis Method Skill | `.agents/skills/fixed-income-analysis/` |
| Commodity Analysis Method Skill | `.agents/skills/commodity-analysis/` |
| Crypto Analysis Method Skill | `.agents/skills/crypto-analysis/` |
| Macro Analysis Method Skill | `.agents/skills/macro-analysis/` |
| News & Catalysts Method Skill | `.agents/skills/news-catalysts/` |
| Market Positioning Method Skill | `.agents/skills/market-positioning/` |
| Portfolio Fit Method Skill | `.agents/skills/portfolio-fit/` |
| Sector & Industry Analysis Method Skill | `.agents/skills/sector-industry-analysis/` |
| Structural Winner Discovery Method Skill | `.agents/skills/structural-winner-discovery/` |
| Driver Dominance Analysis Skill | `.agents/skills/driver-dominance-analysis/` |
| Market Sense Hypothesis Engine Skill | `.agents/skills/market-sense-hypothesis-engine/` |
| Market Intelligence Briefing Skill | `.agents/skills/market-intelligence-briefing/` |

## 7. Skill authoring standard

Each `SKILL.md` should:

- keep the `description` concise and trigger-oriented;
- front-load when to use and when not to use the skill;
- use imperative steps;
- point to canonical contracts rather than copying them;
- identify supporting references from the traceability matrix only when needed;
- require explicit output artifacts and handoff blocks;
- include Limited / Blocked behavior;
- include quality checks that map back to `implementation/09-system-acceptance-qa.md`.

## 8. Workflow execution model

The runtime should preserve the canonical system sequence:

1. Intake router classifies the request.
2. Evidence Collector establishes source readiness.
3. Relevant asset, specialist, discovery, or market agents run according to the workflow contract.
4. Reusable analytical methods are executed through repo skills.
5. Specialist outputs produce handoff artifacts.
6. Investment Committee synthesizes only after evidence and required specialist gates are satisfied.
7. Final output follows master rules and report schemas.

Subagents must be used only when the user, workflow runbook, or operator explicitly requests parallel delegated work. Custom agents are configuration layers for spawned Codex sessions, not permanently running independent agents. They should not create uncontrolled agent-to-agent chat. Handoffs must use structured artifacts and workflow rules.

## 9. Generation sequence

Do not generate all runtime files before their canonical sources are stable.

Recommended sequence:

1. Finalize canonical architecture and master rules.
2. Finalize contract templates.
3. Finalize canonical agent contracts.
4. Finalize canonical skill contracts.
5. Create root `AGENTS.md`.
6. Create root `README.md`.
7. Create `.codex/agents/*.toml` from the 20 planned contracts.
8. Create `.agents/skills/*/SKILL.md` from canonical skill contracts.
9. Create or split workflow runbooks if `implementation/05-routing-and-workflows.md` becomes too large.
10. Run acceptance checks from `implementation/09-system-acceptance-qa.md`.

## 10. Acceptance criteria

### P1A-CODEX-01 readiness

The Codex runtime architecture layer is ready when:

- `implementation/13-codex-runtime-architecture.md` defines the intended root `AGENTS.md`, root `README.md`, `.codex/agents/`, `.agents/skills/`, and workflow runbook conventions;
- project authority order and runtime reading order are separated clearly;
- the project-root discovery rule is documented;
- the 20 planned custom-agent files are mapped to canonical agent/router contracts;
- planned repo skills are mapped to canonical method-skill contracts;
- subagent usage is limited to explicitly requested or runbook-defined delegated work;
- validation checks for future custom-agent TOML files are documented;
- legacy PRDs remain routed through the registry and traceability matrix.

### P1A-CODEX-02 readiness

The generated Codex runtime package is ready when:

- root `AGENTS.md` exists and provides concise project guidance;
- root `README.md` exists and orients human maintainers;
- `.codex/agents/` contains the 20 planned custom-agent TOML files;
- `.agents/skills/` contains repo skills mapped to canonical skill contracts;
- custom agents are narrow adapters and do not copy full PRDs;
- skills are focused reusable workflows and do not silently override canonical contracts;
- legacy PRDs are accessed only through the registry and traceability matrix;
- workflow runbooks explain how routers, evidence, agents, skills, handoffs, and IC synthesis connect;
- QA scenarios can verify routing, evidence, specialist output, skill activation, and IC gates.
