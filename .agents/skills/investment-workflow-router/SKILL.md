---
name: investment-workflow-router
description: Use first for any request asking whether to buy, invest, hold, sell, add, compare, or evaluate a concrete asset, ETF, commodity, crypto, bond, or portfolio decision. Classifies Quick Take vs Full Cycle and selects the required route card before answering.
---

# Investment Workflow Router

This is the first runtime skill for investment-action, comparison, and portfolio-decision prompts in the Financial Agent System.

## Purpose

Classify the user's request and select the correct route card before analysis. This skill does not analyze the asset and does not issue investment conclusions.

## When to use

Use this skill before answering when the user asks whether to buy, invest, hold, sell, add, compare, rank, evaluate, or allocate to:

- a stock or company;
- an ETF or fund;
- a commodity or commodity-linked exposure;
- a crypto asset or crypto-linked exposure;
- a bond, bond ETF, duration, credit, rates, or yield exposure;
- a cross-asset comparison;
- a direct specialist review with possible investment implications.

## What you get

- Intent classification.
- Selected route card.
- Required question count.
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
3. Classify the prompt as Quick Take, Full Cycle, multi-asset comparison, direct specialist, or blocked identity/structure clarification.
4. Load exactly the selected route card.
5. Apply the route card's first action before analysis.
6. If the user asked for concrete-asset investment action and did not explicitly ask for short/quick/preliminary, do not answer immediately; ask exactly 5 relevant questions.
7. If the user explicitly asked for Quick Take, ask exactly 3 relevant questions and keep the later answer chat-only.
8. If the prompt is freshness-dependent, require current timestamped sources or Limited / Blocked status.

## Output contract

Return or follow this internal classification:

```text
Intent classification: [Quick Take | Full Cycle | Multi-asset comparison | Direct specialist | Blocking clarification]
Selected route card: [path]
Required questions before answer: [3 | 5 | blocking clarification]
Forbidden outputs: [list]
Validation fixture: [golden prompt / routing case id if applicable]
```

## Guardrails

- Concrete-asset investment-action prompts default to Full Cycle unless explicitly quick/short/preliminary.
- Non-IC outputs must not use `IC Action`, `Action Box`, or final buy/sell/hold/add/trim/exit labels.
- `Delegated Full Agent Workflow` is valid only if subagents were actually spawned.
- Missing portfolio context limits Portfolio Fit / IC Action; it does not suppress a useful Full Cycle when the asset and route are clear.

## Failure states

- If asset identity or instrument structure is materially ambiguous, ask the minimum blocking clarification first.
- If required route card is missing, report a Blocking runtime source issue.
- If behavior conflicts with canonical implementation documents, apply canonical docs and report a source issue.

## Quality checks

- Microsoft investment prompt routes to Equity Full Cycle, not Quick Take.
- Explicit Microsoft quick prompt routes to Quick Take.
- BTC 3-year prompt routes to Crypto Full Cycle.
- QQQ vs SCHG routes to ETF / comparison.
- Freshness prompts require timestamped sources or Limited / Blocked.
- Direct risk review stays specialist-scoped with no IC Action.
