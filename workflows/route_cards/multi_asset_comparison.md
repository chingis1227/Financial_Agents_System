# Multi-Asset Comparison Route Card

Status: Runtime route card
Authority: Subordinate to `workflows/multi_asset_full_agent_workflow.md` and canonical implementation documents.

## Trigger

Use when the user compares assets across classes, such as BTC vs gold vs QQQ vs TLT, or asks for the best asset without a single asset-class route being sufficient.

## Required first action

Ask exactly 5 comparison questions in one block and wait, unless the user explicitly requests Quick Take.

## Required modules

- evidence collection and source scope
- common role-based criteria
- asset-class-specific analysis for each included asset
- macro context
- valuation / expectations equivalent by asset class
- risk / red-team review
- portfolio fit / limited portfolio fit
- IC synthesis or decision-prep comparison

## Allowed output

Scenario-based comparison, role-based winners, and gate-aware decision-prep output.

## Forbidden output

No universal winner or final allocation without user objective, portfolio context, evidence, risk, valuation, and IC gates.

## Downgrade rules

If criteria are undefined, use default criteria but label the output Limited and scenario-based.

## Validation expectations

QQQ vs SCHG and BTC/gold/QQQ/TLT prompts must route to comparison or ETF route with no premature final action.
