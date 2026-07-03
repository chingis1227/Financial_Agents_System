# Financial Agent Automation Lab Roadmap

Status: Pre-production automation layer

## Purpose

Build an external automation and control layer for the Financial Agent System without moving investment logic out of the main project.

The main project remains the source of truth for rules, routing, agents, skills, validation contracts, and investment boundaries.

## Task process

Each task must define:

- goal;
- value;
- dependencies;
- scope;
- out of scope;
- implementation plan;
- test plan;
- docs synchronization note;
- review checklist;
- Definition of Done.

Implementation rule: complete one task at a time. Do not add adjacent features "while here".

## Roadmap

1. TASK-001 — Codex SDK route check scaffold — Complete
   - Historical fixture route check.
   - Live mode placeholder.
   - CLI.
   - JSON logs.
   - unittest.

2. TASK-002 — Live Codex SDK route check — Complete
   - Real Codex SDK execution.
   - Launch Codex from the Financial Agent System root.
   - Read-only route classification.
   - Strict JSON response.
   - One retry for invalid JSON.

3. TASK-003 — Data source map draft — Complete
   - Draft source maps in this Automation Lab.
   - Equity, crypto, ETF, fixed income, commodity, macro, and news.

4. TASK-004 — QUICK automation — Complete
   - Automated guarded QUICK launch.
   - Preliminary boundary preserved.

5. TASK-005 — QUICK result quality control — Complete
   - Validate status, structure, freshness limits, and no final IC Action.

6. TASK-006 — AGENT automation design — Complete
   - Design large workflow automation before implementation.
   - Preserve 5-question intake, subagent truthfulness, audit, evidence, valuation, risk, and portfolio-fit gates.

7. TASK-007 — QUICK answer public data v1 — Complete
   - Second QUICK step implemented as `quick-answer`.
   - MSFT/equity pilot.
   - Historical fixture fixture mode plus live/public mode without API keys.
   - `data_runs/quick/[timestamp]-MSFT/` snapshot with source, quality, and answer JSON files.
   - `validate-quick-answer` validator.
   - README, roadmap, and task document synchronized.

8. TASK-008 - QUICK answer asset expansion v1 - Complete
   - Expanded `quick-answer` beyond MSFT/equity.
   - Pilots: ETF/SPY, crypto/BTC, bond ETF/TLT, commodity ETF/GLD, and comparison/MSFT-SPY-BTC.
   - Historical fixture fixtures are required and tested; live mode is best-effort without API keys.
   - Asset-specific Quick Take context added while preserving one common QUICK template.
   - Provider registry remains deferred to TASK-009.

9. TASK-009 - QUICK provider registry - Complete
   - Added `quick_data/` provider registry foundation.
   - Registered public providers and disabled future API-provider slots.
   - Added source quality, freshness, fallback, provider errors, and missing-data rules to QUICK snapshots.

10. TASK-010 - QUICK output quality control v2 - Complete
   - Strengthen real QUICK output checks for sources, freshness notes, main risk, overconfidence, and hidden final-action language.
   - Added `output_quality.json`, `Source note`, `Freshness note`, risk-specificity checks, hidden-action checks, and overconfidence checks.

11. TASK-011 - AGENT equity/MSFT pilot - Complete
    - Adds `agent-intake`, `agent-run`, and `validate-agent-run`.
    - Implements the first full MSFT/equity vertical slice with intake, source preflight, evidence pack, specialist handoffs, reader-facing `investment_report.md`, and `audit/`.
    - Historical fixture path is fixture-first for deterministic tests; live mode uses public/no-key source preflight and separate Codex SDK specialist runs.
    - Live specialist execution now uses the Financial Agent System TypeScript Codex SDK CLI through `npm.cmd`, not the unavailable Python `openai_codex` bridge.

12. TASK-012 - Generalize full equity AGENT beyond MSFT - Complete
   - Generalizes `agent-run` from MSFT-only to supported equities v1: MSFT and AAPL.
   - Adds asset-parametric identity, source preflight, evidence pack, report/audit, validation, and AAPL fixture coverage while keeping unsupported assets blocked.
   - Preserves MSFT as regression baseline and keeps reader reports clean with technical details in `audit/`.

13. TASK-013 - Full global public equity AGENT cycle - Complete
   - Replaces the MSFT/AAPL whitelist with dynamic public-equity resolution and instrument classification.
   - Supports US common equities, US share classes, ADRs / foreign-issuer US listings, and direct non-US listings where public sources are sufficient.
   - Blocks private companies and complex instruments as ordinary equity.
   - Uses public/no-key sources only, with Stooq first for price/history and Yahoo/public chart fallback.
   - Adds global-equity validators, historical fixture regression coverage, live-smoke recording, and mandatory review-loop evidence.

14. Full live AGENT Complete hardening - Complete
   - Production live specialist timeout default is `900` seconds per Codex SDK subprocess attempt; full run hard wall-clock budget default is `7200` seconds and caps remaining specialist attempts/retries.
   - Live AGENT execution is staged: evidence first, parallel non-IC specialist fan-out, then IC only after all upstream handoffs are successful.
   - Parallel fan-out defaults to `FA_AUTOMATION_AGENT_MAX_PARALLEL_SPECIALISTS=3` and writes isolated specialist audit folders.
   - Complete semantics require all route-required specialists to succeed, real live `sdk_thread_id` values for completed live specialists, IC ownership, IC consumption of all upstream handoffs, non-Blocked source/evidence readiness, and report validation.
   - Timeout/failure paths remain honest Limited outputs and never fabricate thread/run ids or IC consumption.


15. TASK-014 - Full non-equity AGENT smoke coverage - Complete
   - Adds validated AGENT smoke paths for ETF/fund, fixed income, crypto, commodity, and multi-asset comparison.
   - Each path creates `investment_report.md`, `audit/`, source preflight, provider results, evidence pack, specialist handoffs, run manifest, and validation files.
   - Preserves Financial Agent System route cards as the source of truth; Automation Lab remains execution/orchestration only.
   - Historical fixture path is deterministic for regression; live mode uses the existing staged Codex SDK specialist launcher and stays Limited when live specialists or source gates fail.


16. TASK-015 - Direct specialist execution - Complete
   - Adds `specialist-run` and `validate-specialist-run` for direct specialist prefixes.
   - Maps each supported prefix to exactly one specialist and saves `specialist_report.md` plus `audit/` under `Financial Agent Reports\_specialists\`.
   - Requires `Boundary: Not an IC Action`, forbids final action language, and keeps live thread-id truthfulness for single-specialist runs.


17. TASK-016 - Live readiness doctor - Complete
   - Adds `live-doctor` to check Automation Lab and Financial Agent System Codex SDK live prerequisites before long runs.
   - Verifies project roots, built SDK CLI, `.venv`, report-root writability, timeout/env settings, prompt-file transport, and public/no-key source assumptions.
   - Writes JSON readiness logs under `runs/live-doctor/` for auditability.


18. TASK-017 - Live acceptance manifest - Complete
   - Adds `live-acceptance` to audit current QUICK, AGENT, specialist, and live-doctor artifacts.
   - Separates deterministic smoke coverage from real live `sdk_thread_id` evidence.
   - Supports `--require-live` to fail when complete live evidence is missing.

19. TASK-018 - Structured portfolio-context input - Complete
   - Adds `--portfolio-context-json` and `--portfolio-context-file` to `agent-run`.
   - Records holdings, cash, risk limits, horizon, constraints, existing exposure, and objective in `audit/portfolio_context.json`.
   - Propagates context status into intake, specialist handoffs, run manifest, reader report, and validation while preserving the no-final-action/no-exact-sizing boundary.

20. TASK-019 - Live usage-limit guardrail - Complete
   - Detects Codex SDK usage-limit errors during live specialist attempts.
   - Stops AGENT live retry when the error is quota-related and records the reset hint in audit.
   - Adds `usage_limit_gaps` to `live-acceptance` so quota-limited live gaps are visible separately from smoke gaps.

21. TASK-020 - Full live acceptance completion - Complete
   - Completed real live AGENT packages for equity, ETF/fund, fixed income, crypto, commodity, and multi-asset comparison.
   - Completed real live direct specialist runs for every supported prefix.
   - Confirmed `live-acceptance --require-live` passes with no smoke gaps, live gaps, or usage-limit gaps.

## Current notes

TASK-001 did not change the Financial Agent System repository.

TASK-002 did not change the Financial Agent System repository.

TASK-003 did not change the Financial Agent System repository. If a future task changes the main project, run its required validators.

TASK-004 did not change the Financial Agent System repository. QUICK automation lives in this lab and preserves the Quick Take Preliminary/Limited boundary.

TASK-005 did not change the Financial Agent System repository. QUICK quality control now validates first-line status, numbered three-question structure, freshness-dependent Limited status, freshness/current-source intake visibility, and forbidden final-action/report/audit/subagent markers.

TASK-006 did not change the Financial Agent System repository. AGENT automation design now exists as a design-only historical fixture command that validates five-question intake, source-of-truth boundary, route-card existence, planned-versus-actual subagent truthfulness, evidence/freshness, lead-asset, material-context, valuation, risk, implementation/vehicle-quality, portfolio-fit, audit, and IC synthesis gates before any future implementation.

TASK-007 did not change the Financial Agent System repository. QUICK answer execution now lives in this lab: `quick-run` remains the three-question intake, while `quick-answer` consumes the prompt plus answers, collects a minimal public MSFT/equity snapshot, writes source and quality JSON files, validates the answer boundary, and keeps final IC decisions locked.

TASK-008 did not change the Financial Agent System repository. QUICK answer now supports the agreed pilot set while preserving the same Preliminary/Limited/Blocked boundary, no report/audit artifacts, no final IC Action, and no exact sizing.


TASK-009 did not change the Financial Agent System repository. QUICK data collection now uses an Automation Lab provider registry and writes provider metadata/errors into snapshots while preserving the same QUICK boundaries and CLI UX. The QUICK snapshot is not an Evidence Collector evidence pack; full evidence control remains in the main AGENT workflow.

TASK-010 did not change the Financial Agent System repository. QUICK answer now writes `output_quality.json`, requires source/freshness notes in the Quick Take, validates hidden action language and overconfidence, requires risk specificity, and fails validation when output quality is weak.

TASK-011 did not move canonical investment logic out of the Financial Agent System. Automation Lab now executes the MSFT/equity AGENT vertical slice while preserving the main project as source of truth. Reader reports are saved outside both repositories under `Financial Agent Reports`; technical status labels, raw specialist outputs, source registers, and validators remain in `audit/`.

TASK-012 did not move canonical investment logic out of the Financial Agent System. Automation Lab generalized the supported-equity AGENT workflow for MSFT and AAPL; TASK-013 later expanded public-equity resolution and TASK-014 added validated non-equity smoke paths.

TASK-013 does not move canonical investment logic out of the Financial Agent System. Automation Lab now resolves public listed equities by instrument class, supports US/share-class/ADR/non-US public-source paths, blocks private companies or complex instruments as ordinary equity, records provider/source/evidence audit artifacts, and completed the mandatory review loop at 9/10. Main project validators are only required if the main Financial Agent System changes.

Full live AGENT Complete hardening does not migrate to the OpenAI Agents SDK and does not add queue/dashboard/scheduler behavior. Automation Lab remains the dispatcher, the Financial Agent System remains the source-of-truth brain/rules layer, and the Codex SDK CLI remains the launch engine.

TASK-014 does not move canonical investment logic out of the Financial Agent System. Automation Lab now executes validated smoke AGENT packages for ETF/fund, fixed income, crypto, commodity, and multi-asset comparison using the same route → intake → source preflight → evidence pack → specialists → IC synthesis → report → audit → validation pattern. Live mode still requires real Codex SDK specialist completion for Complete; otherwise outputs remain Limited and audit records the gap.

TASK-015 does not move canonical investment logic out of the Financial Agent System. It operationalizes the existing direct-specialist route card in Automation Lab: one prefix maps to one specialist, output remains `Boundary: Not an IC Action`, and validation rejects final-action language or multi-specialist expansion.

TASK-016 does not execute investment analysis. It is a live-readiness guardrail that proves the local execution layer can reach the Financial Agent System Codex SDK doctor and write audited readiness logs before long live specialist runs.

TASK-017 does not run analysis or upgrade historical fixture evidence to live evidence. It records an acceptance manifest that makes the remaining live gaps explicit by route and specialist prefix, including missing `sdk_thread_id` evidence.

TASK-018 does not fabricate portfolio context and does not unlock personal final action. It gives Portfolio Fit a structured input path when the user provides holdings/cash/risk/objective data, and keeps reports Limited/preparatory when context or IC gates remain incomplete.

TASK-019 does not treat quota failures as successful live evidence. It makes quota blockage explicit, prevents wasteful immediate retries after a usage-limit response, and keeps `live-acceptance --require-live` failing until missing routes have real `sdk_thread_id` evidence.

TASK-020 records the first complete live-acceptance pass for the supported runtime matrix. It does not remove future source/freshness limits; each individual run can still be Limited or Blocked if public sources, user context, or live specialist execution fail, but the runtime now has proven live completion evidence across the required route and direct-specialist matrix.
