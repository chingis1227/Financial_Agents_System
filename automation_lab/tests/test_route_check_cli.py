from __future__ import annotations

import json
import os
import queue
import subprocess
import sys
import types
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock

LAB_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LAB_ROOT))

import fa_automation

EXPECTED_PROJECT_ROOT = r"C:\Users\ShumeikoYe\OneDrive\Documents\Financial Agent System"


class RouteCheckCliTests(unittest.TestCase):
    def run_cli(self, args: list[str], runs_dir: Path) -> subprocess.CompletedProcess[str]:
        env = os.environ.copy()
        env["FA_AUTOMATION_UNIT_LIVE_STUB"] = "1"
        env["FA_AUTOMATION_RUNS_DIR"] = str(runs_dir)
        return subprocess.run(
            [sys.executable, "fa_automation.py", *args],
            cwd=LAB_ROOT,
            text=True,
            capture_output=True,
            check=False,
            env=env,
        )

    def assert_mock_run_log(self, payload: dict) -> None:
        self.assertEqual(payload["mode"], "live")
        self.assertEqual(payload["project_root"], EXPECTED_PROJECT_ROOT)
        self.assertIn("timestamp", payload)
        self.assertEqual(len(payload["cases"]), 6)

        for case in payload["cases"]:
            self.assertIn("case_id", case)
            self.assertIn("prompt", case)
            self.assertIn("expected_route", case)
            self.assertIn("actual_route", case)
            self.assertEqual(case["status"], "pass")

    def test_explicit_mock_cli_creates_json_log_with_six_passing_cases(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            runs_dir = Path(temp_dir)
            completed = self.run_cli(["route-check", "--mode", "live"], runs_dir)

            self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
            created = sorted(runs_dir.glob("*.json"), key=lambda path: path.stat().st_mtime)
            self.assertEqual(len(created), 1, "Expected exactly one route-check JSON log")

            with created[-1].open("r", encoding="utf-8") as file:
                payload = json.load(file)
            self.assert_mock_run_log(payload)

    def test_default_route_check_mode_is_mock(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            runs_dir = Path(temp_dir)
            completed = self.run_cli(["route-check"], runs_dir)

            self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
            created = sorted(runs_dir.glob("*.json"), key=lambda path: path.stat().st_mtime)
            self.assertEqual(len(created), 1, "Expected default route-check to create one JSON log")

            with created[-1].open("r", encoding="utf-8") as file:
                payload = json.load(file)
            self.assert_mock_run_log(payload)


class LiveRouteCheckTests(unittest.TestCase):
    def test_parse_route_json_accepts_strict_expected_shape(self) -> None:
        parsed = fa_automation.parse_route_json(
            '{"selected_route":"crypto_full_cycle","reason":"BTC is crypto."}'
        )
        self.assertEqual(parsed["selected_route"], "crypto_full_cycle")
        self.assertEqual(parsed["reason"], "BTC is crypto.")

    def test_parse_route_json_rejects_markdown_wrapped_json(self) -> None:
        with self.assertRaises(json.JSONDecodeError):
            fa_automation.parse_route_json(
                '```json\n{"selected_route":"crypto_full_cycle","reason":"BTC"}\n```'
            )

    def test_parse_route_json_rejects_extra_fields(self) -> None:
        with self.assertRaises(ValueError):
            fa_automation.parse_route_json(
                '{"selected_route":"crypto_full_cycle","reason":"BTC","extra":"not allowed"}'
            )

    def test_live_classifier_retries_once_after_invalid_json_then_succeeds(self) -> None:
        classifier = fa_automation.LiveCodexRouteClassifier()
        classifier._run_codex = Mock(  # type: ignore[method-assign]
            side_effect=[
                '```json\n{"selected_route":"crypto_full_cycle","reason":"BTC"}\n```',
                '{"selected_route":"crypto_full_cycle","reason":"BTC is crypto."}',
            ]
        )

        result = classifier.classify("AGENT: BTC")

        self.assertEqual(result.selected_route, "crypto_full_cycle")
        self.assertEqual(result.attempts, 2)
        self.assertEqual(classifier._run_codex.call_count, 2)  # type: ignore[attr-defined]

    def test_live_classifier_retries_once_after_empty_response_then_fails(self) -> None:
        classifier = fa_automation.LiveCodexRouteClassifier()
        classifier._run_codex = Mock(side_effect=["", ""])  # type: ignore[method-assign]

        with self.assertRaises(fa_automation.LiveRouteError):
            classifier.classify("AGENT: BTC")

        self.assertEqual(classifier._run_codex.call_count, 2)  # type: ignore[attr-defined]

    def test_codex_worker_uses_main_root_read_only_and_deny_all(self) -> None:
        calls: dict[str, object] = {}

        class FakeApprovalMode:
            deny_all = "deny_all"

        class FakeSandbox:
            read_only = "read-only"

        class FakeThread:
            def run(self, request: str, **kwargs: object) -> object:
                calls["run_request"] = request
                calls["run_kwargs"] = kwargs
                return types.SimpleNamespace(
                    final_response='{"selected_route":"equity_full_cycle","reason":"test"}'
                )

        class FakeCodex:
            def __enter__(self) -> "FakeCodex":
                return self

            def __exit__(self, *args: object) -> None:
                return None

            def thread_start(self, **kwargs: object) -> FakeThread:
                calls["thread_start_kwargs"] = kwargs
                return FakeThread()

        fake_module = types.SimpleNamespace(
            ApprovalMode=FakeApprovalMode,
            Codex=FakeCodex,
            Sandbox=FakeSandbox,
        )
        original = sys.modules.get("openai_codex")
        sys.modules["openai_codex"] = fake_module
        try:
            output_queue: queue.Queue[dict[str, str]] = queue.Queue()
            fa_automation._codex_worker(
                "classify this",
                EXPECTED_PROJECT_ROOT,
                None,
                output_queue,
            )
        finally:
            if original is None:
                sys.modules.pop("openai_codex", None)
            else:
                sys.modules["openai_codex"] = original

        message = output_queue.get_nowait()
        self.assertEqual(message["status"], "ok")
        self.assertEqual(calls["thread_start_kwargs"], {
            "cwd": EXPECTED_PROJECT_ROOT,
            "model": None,
            "sandbox": "read-only",
            "approval_mode": "deny_all",
        })
        self.assertEqual(calls["run_kwargs"], {
            "cwd": EXPECTED_PROJECT_ROOT,
            "sandbox": "read-only",
            "approval_mode": "deny_all",
            "model": None,
            "output_schema": fa_automation.ROUTE_OUTPUT_SCHEMA,
        })

    def test_live_evaluate_cases_uses_classifier_one_case_at_a_time(self) -> None:
        cases = [
            {
                "case_id": "btc_crypto",
                "prompt": "AGENT: BTC for 3 years, should I invest?",
                "expected_route": "crypto_full_cycle",
            }
        ]
        classifier = Mock()
        classifier.classify.return_value = fa_automation.LiveClassification(
            selected_route="crypto_full_cycle",
            reason="BTC is a crypto asset.",
            attempts=1,
        )

        results = fa_automation.evaluate_cases(cases, mode="live", live_classifier=classifier)

        classifier.classify.assert_called_once_with("AGENT: BTC for 3 years, should I invest?")
        self.assertEqual(results[0]["actual_route"], "crypto_full_cycle")
        self.assertEqual(results[0]["status"], "pass")
        self.assertEqual(results[0]["attempts"], 1)
        self.assertIn("reason", results[0])

    def test_live_evaluate_cases_records_mismatch_diagnostic(self) -> None:
        cases = [
            {
                "case_id": "btc_crypto",
                "prompt": "AGENT: BTC for 3 years, should I invest?",
                "expected_route": "crypto_full_cycle",
            }
        ]
        classifier = Mock()
        classifier.classify.return_value = fa_automation.LiveClassification(
            selected_route="equity_full_cycle",
            reason="Wrong route for test.",
            attempts=1,
        )

        results = fa_automation.evaluate_cases(cases, mode="live", live_classifier=classifier)

        self.assertEqual(results[0]["status"], "fail")
        self.assertEqual(results[0]["actual_route"], "equity_full_cycle")
        self.assertIn("mismatch", results[0])
        self.assertIn("diagnostic_hint", results[0])


if __name__ == "__main__":
    unittest.main()
