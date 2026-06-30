# Direct Specialist Route Card

Status: Runtime route card
Authority: Subordinate to master rules and agent/skill contracts.

## Trigger

Use when the user explicitly asks for a scoped specialist output, such as risk review, valuation only, evidence check, macro sensitivity, portfolio fit, or catalyst review.

## Required first action

Confirm scope if ambiguous. Do not expand to Full Cycle unless the user asks for investment action or IC synthesis.

## Required modules

Only the requested specialist method plus evidence/source limitations needed for that scope.

## Allowed output

Specialist Verdict, Risk Box, Valuation Box, Evidence Gap Memo, or scoped specialist summary with `Boundary: Not an IC Action`.

## Forbidden output

- No `Action Box`.
- No final `IC Action`.
- No final buy/sell/hold/add/trim/exit recommendation.

## Downgrade rules

If the specialist cannot support the requested conclusion, return Limited / Blocked with minimum next step and IC gates required for final decision support.

## Validation expectations

Direct risk review prompt must produce specialist boundary and forbid IC Action.
