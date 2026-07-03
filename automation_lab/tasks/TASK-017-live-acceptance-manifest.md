# TASK-017 — Live acceptance manifest

Status: Complete

## Goal

Create an audited manifest that shows current live acceptance evidence across QUICK, AGENT routes, direct specialist prefixes, and live-doctor status.

## Value

The system should not confuse deterministic smoke readiness with real live completion. `live-acceptance` makes the distinction explicit: validated smoke artifacts prove executable coverage, while Complete live readiness still requires real `sdk_thread_id` evidence for live specialist runs.

## Scope

- Add `live-acceptance` CLI command.
- Collect current QUICK answer artifacts, AGENT run manifests, direct specialist manifests, and latest live-doctor log.
- Report smoke gaps separately from live gaps.
- Support `--require-live` to fail when live evidence is missing.
- Write JSON acceptance logs under `runs/live-acceptance/`.

## Out of scope

- Running live investment analysis.
- Treating historical fixture outputs as live evidence.
- Closing live gaps without real Codex SDK thread ids.

## Test plan

```powershell
.\.venv\Scripts\python.exe -m unittest tests.test_agent_run_cli.AgentRunTask011Tests.test_live_acceptance_manifest_tracks_smoke_and_live_gaps
.\.venv\Scripts\python.exe fa_automation.py live-acceptance
.\.venv\Scripts\python.exe -m unittest discover -s tests -p "test_*.py"
```

## Definition of Done

- Acceptance manifest includes QUICK, AGENT route, specialist prefix, and live-doctor coverage.
- Manifest distinguishes smoke coverage from real live `sdk_thread_id` evidence.
- `--require-live` fails while live gaps remain.
- README and ROADMAP document usage and limitation.
