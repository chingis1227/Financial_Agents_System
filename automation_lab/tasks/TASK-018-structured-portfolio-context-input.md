# TASK-018 - Structured portfolio-context input

## Goal

Add a practical structured portfolio-context input path to Automation Lab `agent-run` without moving investment policy out of the Financial Agent System.

## Value

Portfolio Fit can use user-supplied holdings, cash, risk limits, horizon, constraints, existing exposure, and objective instead of treating every run as generic/no-context.

## Scope

- Add `--portfolio-context-json` and `--portfolio-context-file` to `agent-run`.
- Normalize and audit supported fields: `holdings`, `cash`, `risk_limits`, `horizon`, `constraints`, `existing_exposure`, and `objective`.
- Save `audit/portfolio_context.json`.
- Propagate context status into `intake.json`, specialist handoffs, `run_manifest.json`, reader report text, and `agent_run_validation.json`.
- Preserve the rule that context does not by itself unlock final buy/sell/hold/add/trim/exit action or exact sizing.

## Out of scope

- No portfolio optimizer.
- No tax, suitability, or personalized sizing engine.
- No hidden broker/account ingestion.
- No change to Financial Agent System route-card authority.

## Test plan

- Portfolio context JSON path creates report/audit and validates.
- Portfolio context file path creates report/audit and validates.
- Empty structured context is rejected and creates no report.
- Existing no-context AGENT runs remain valid and Limited/preparatory.

## Definition of Done

- CLI accepts JSON and file context paths.
- `portfolio_context.json` is present in AGENT audit packages.
- Validation checks portfolio context truthfulness and confirms no personal action unlock.
- README and ROADMAP document the new path.
