# Quick Take Route Card

Status: Runtime route card
Authority: Subordinate to master rules and report schemas.

## Trigger

Use only when the user uses `QUICK:` or explicitly asks for short, quick, fast, preliminary, or similar limited output.

## Required first action

Ask exactly 3 relevant questions in one block and wait for the user's next message.

## Required modules

- Identify asset / instrument if needed.
- Use only evidence that can be handled safely in a quick pass.
- For today / now / latest / news / price action, use current timestamped sources or mark the output Limited / Blocked.

## Allowed output

Chat-only Preliminary or Limited view with status, evidence limits, missing gates, and next step.

## Forbidden output

- Quick Take never issues final IC Action; if final gates are being completed, route or upgrade to `AGENT:` / IC synthesis instead of Quick Take.
- No `investment_report.md`.
- No `audit/` folder.
- No final `IC Action`, `Action Box`, or buy/sell/hold/add/trim/exit conclusion. If final gates are being completed, route or upgrade to `AGENT:` / IC synthesis instead of Quick Take.
- No exact position sizing or exact trade instruction.

## Downgrade rules

If freshness, identity, or evidence is insufficient, use Limited / Blocked rather than pretending current confidence.

## Validation expectations

`QUICK: Microsoft` prompt must map to `quick_take`, require 3 questions, and forbid saved report / audit.
