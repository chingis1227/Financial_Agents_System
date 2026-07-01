---
name: investment-workflow-router
description: Use first for any AGENT:, QUICK:, or specialist-command request, and for any request asking whether to buy, invest, hold, sell, add, compare, or evaluate a concrete asset, ETF, commodity, crypto, bond, or portfolio decision. Classifies command shortcut vs ordinary router flow and selects the required route card before answering.
---

# Investment Workflow Router

This is the first runtime skill for command shortcuts, investment-action, comparison, and portfolio-decision prompts in the Financial Agent System.

## Purpose

Classify the user's request and select the correct route card before analysis. This skill does not analyze the asset and does not issue investment conclusions.

## When to use

Use this skill before answering when the user uses:

- `AGENT:` for the large agent workflow;
- `QUICK:` for a short preliminary answer;
- any specialist prefix in the mapping below;
- an ordinary request asking whether to buy, invest, hold, sell, add, compare, rank, evaluate, or allocate to an asset.

## Command mapping

| Prefix | Route |
|---|---|
| `AGENT:` | `investment_request_router.md` -> selected asset/comparison route card; requires relevant spawned subagents or Limited fallback in audit only |
| `QUICK:` | `quick_take.md` |

| Prefix | Target agent |
|---|---|
| `RISK:` | `risk-red-team-agent` |
| `VAL:` | `valuation-expectations-agent` |
| `MACRO:` | `macro-agent` |
| `NEWS:` | `news-catalysts-agent` |
| `PORTFOLIO:` | `portfolio-fit-agent` |
| `SECTOR:` | `sector-industry-analysis-agent` |
| `EVIDENCE:` | `evidence-collector` |
| `POSITIONING:` | `market-positioning-agent` |
| `INTEL:` | `market-intelligence-agent` |
| `EQUITY:` | `equity-agent` |
| `ETF:` | `etf-agent` |
| `COMMODITY:` | `commodity-agent` |
| `CRYPTO:` | `crypto-agent` |
| `FI:` | `fixed-income-agent` |
| `WINNERS:` | `structural-winners-discovery-agent` |
| `IC:` | `investment-committee-agent` |

## What you get

- Command / intent classification.
- Selected route card.
- Required question count.
- Target agent for specialist commands.
- Forbidden output reminders.
- Validation fixture expectation.

## What it will not do

- It does not perform evidence collection.
- It does not value assets.
- It does not write final reports.
- It does not issue `IC Action`.
- It does not claim subagents ran.

## Required steps

1. Read `PROJECT_STATE.md`.
2. Read `workflows/route_cards/investment_request_router.md`.
3. Classify the prompt as `AGENT:`, `QUICK:`, specialist command, ordinary router flow, or truly unroutable identity/structure conflict.
4. For `AGENT:`, load the selected asset/comparison route card, ask exactly 5 relevant questions, and use relevant spawned subagents when available.
5. For `QUICK:`, load `quick_take.md`, ask exactly 3 relevant questions, and keep the later answer chat-only.
6. For specialist commands, load `direct_specialist.md`, target exactly the mapped analyst, and keep the result scoped.
7. If the prompt is freshness-dependent, require current timestamped sources or Limited / Blocked status.

## Output contract

Return or follow this internal classification:

```text
Command classification: [AGENT | QUICK | SPECIALIST | ORDINARY_ROUTER | UNROUTABLE_IDENTITY_CONFLICT]
Selected route card: [path]
Target agent: [agent id or not applicable]
Required questions before answer: [3 | 5 | scope clarification | unroutable identity clarification]
Forbidden outputs: [list]
Validation fixture: [golden prompt / routing case id if applicable]
```

## Guardrails

- `AGENT:` is the only user-facing command for the large agent workflow.
- `AGENT:` must not claim agent workflow execution unless subagents were actually spawned.
- If subagents cannot be spawned after `AGENT:`, record fallback only in audit metadata and mark user-facing output Limited.
- `QUICK:` never issues final IC Action and never creates report/audit files.
- Specialist commands, including `IC:`, route to one analyst and must not use `IC Action`, `Action Box`, or final buy/sell/hold/add/trim/exit labels.
- Missing portfolio context limits Portfolio Fit / IC Action; it does not suppress a useful agent workflow when the asset and route are clear.

## Failure states

- If asset identity, ticker, instrument, currency, maturity, or structure is ambiguous, count the clarification inside the required 5-question `AGENT:` block or 3-question `QUICK:` block wherever possible. Ask a separate blocking clarification only when the request is truly unroutable, such as an unresolved ticker/share-class/instrument conflict that prevents route selection.
- If a required route card or command mapping is missing, report a Blocking runtime source issue.
- If behavior conflicts with canonical implementation documents, apply canonical docs and report a source issue.

## Quality checks

- `AGENT: Microsoft` routes to the equity route and requires 5 questions.
- `QUICK: Microsoft` routes to Quick Take and requires 3 questions.
- Every specialist prefix maps to exactly one target agent.
- BTC 3-year prompt routes to crypto route when used with `AGENT:` or ordinary router flow.
- QQQ vs SCHG routes to ETF / comparison.
- Freshness prompts require timestamped sources or Limited / Blocked.
- Direct risk review stays specialist-scoped with no IC Action.
