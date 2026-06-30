# Equity Full Cycle Route Card

Status: Runtime route card
Authority: Subordinate to `workflows/equity_full_cycle.md` and canonical implementation documents.

## Trigger

Use for concrete public-equity or company investment-action requests such as buy, invest, hold, sell, add, start exposure, or evaluate for a multi-year horizon.

## Required first action

Ask exactly 5 relevant equity questions in one block and wait. If the user says continue or equivalent, use approved baseline assumptions only.

## Required modules

- request intake and asset identity check
- evidence collection and freshness check
- macro context
- sector / industry context
- equity company analysis
- financial statement analysis when material
- valuation / expectations
- risk / red-team review
- portfolio fit / limited portfolio fit
- IC synthesis

## Allowed output

Saved `investment_report.md` plus `audit/`, or a gate-aware Limited / Blocked artifact if required gates cannot be completed.

## Forbidden output

- No Quick Take unless explicitly requested.
- No final buy/sell/hold/add/trim/exit language outside IC synthesis.
- No `Delegated Full Agent Workflow` claim unless subagents actually spawned.

## Downgrade rules

Missing portfolio context limits Portfolio Fit and IC Action Status. Missing freshness/evidence can require Evidence Gap Memo or Limited IC Draft.

## Validation expectations

Microsoft investment prompt must map to `equity_full_cycle`, require 5 questions, and forbid Quick Take without explicit request.
