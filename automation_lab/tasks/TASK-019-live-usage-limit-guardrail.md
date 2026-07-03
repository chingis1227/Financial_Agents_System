# TASK-019 - Live usage-limit guardrail

## Goal

Make live AGENT execution handle Codex SDK usage-limit responses honestly and efficiently.

## Value

When live quota is exhausted, the runtime should not waste retries or make the failure look like an ordinary specialist-quality failure. Audit and acceptance should explain that live completion is quota-blocked and preserve the missing live evidence status.

## Scope

- Detect Codex SDK messages containing usage-limit / purchase-more-credits / try-again-at wording.
- Stop AGENT live retry immediately after a usage-limit response.
- Record `usage_limit_blocked` and `usage_limit_reset_hint` in live attempt records and specialist handoffs.
- Surface quota-limited routes/prefixes as `usage_limit_gaps` in `live-acceptance`.

## Out of scope

- No bypass of Codex usage limits.
- No fabricated `sdk_thread_id` evidence.
- No automatic wait/scheduler behavior.

## Test plan

- `py_compile fa_automation.py`.
- Targeted live-acceptance and portfolio-context tests.
- Full Automation Lab unittest discovery.
- Refresh `live-acceptance` and confirm smoke gaps remain separate from usage-limit gaps.

## Definition of Done

- Usage-limit errors are classified in audit.
- Immediate AGENT retry is skipped for quota-related failures.
- `live-acceptance` includes `usage_limit_gaps`.
- Existing tests pass.
