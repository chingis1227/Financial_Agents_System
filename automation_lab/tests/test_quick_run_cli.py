from __future__ import annotations

import json
import os
import queue
import subprocess
import sys
import tempfile
import types
import unittest
from pathlib import Path

LAB_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LAB_ROOT))

import fa_automation

EXPECTED_PROJECT_ROOT = r"C:\Users\ShumeikoYe\OneDrive\Documents\Financial Agent System"


class QuickRunCliTests(unittest.TestCase):
    def run_cli(self, args: list[str], runs_dir: Path) -> subprocess.CompletedProcess[str]:
        env = os.environ.copy()
        env["FA_AUTOMATION_UNIT_LIVE_STUB"] = "1"
        env["FA_AUTOMATION_QUICK_RUNS_DIR"] = str(runs_dir)
        return subprocess.run(
            [sys.executable, "fa_automation.py", *args],
            cwd=LAB_ROOT,
            text=True,
            capture_output=True,
            check=False,
            env=env,
        )

    def test_mock_quick_run_creates_preliminary_json_log(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            runs_dir = Path(temp_dir)
            completed = self.run_cli(
                ["quick-run", "--prompt", "Microsoft for 3 years", "--mode", "live"],
                runs_dir,
            )

            self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
            created = sorted(runs_dir.glob("*.json"), key=lambda path: path.stat().st_mtime)
            self.assertEqual(len(created), 1, "Expected exactly one QUICK JSON log")

            payload = json.loads(created[-1].read_text(encoding="utf-8"))
            self.assertEqual(payload["mode"], "live")
            self.assertEqual(payload["workflow"], "quick_take")
            self.assertEqual(payload["project_root"], EXPECTED_PROJECT_ROOT)
            self.assertEqual(payload["prompt"], "Microsoft for 3 years")
            self.assertEqual(payload["normalized_prompt"], "QUICK: Microsoft for 3 years")
            self.assertEqual(payload["boundary_status"], "Preliminary")
            self.assertTrue(payload["guardrails"]["preliminary_or_limited_only"])
            self.assertTrue(payload["guardrails"]["no_report_requested"])
            self.assertTrue(payload["guardrails"]["no_audit_requested"])
            self.assertTrue(payload["guardrails"]["no_ic_action_requested"])
            self.assertEqual(payload["validation"]["status"], "pass")
            self.assertEqual(payload["validation"]["question_count"], 3)
            self.assertTrue(payload["validation"]["quality_checks"]["status_first_line"])
            self.assertTrue(payload["validation"]["quality_checks"]["numbered_questions"])
            self.assertFalse(payload["validation"]["quality_checks"]["freshness_required"])
            self.assertIn("Status: Preliminary", payload["output"])
            self.assertEqual(payload["output"].count("?"), 3)
            self.assertNotIn("report", completed.stdout.lower())
            self.assertNotIn("audit", completed.stdout.lower())
            self.assertNotIn("ic action", completed.stdout.lower())

    def test_quick_prefix_is_not_duplicated(self) -> None:
        result = fa_automation.mock_quick_launch("QUICK: BTC")
        self.assertEqual(result.normalized_prompt, "QUICK: BTC")

    def test_quick_stdout_does_not_echo_final_action_prompt(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            completed = self.run_cli(
                ["quick-run", "--prompt", "Should I buy MSFT", "--mode", "live"],
                Path(temp_dir),
            )

            self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
            self.assertNotIn("buy", completed.stdout.lower())
            self.assertIn("Prompt: captured in run log", completed.stdout)

    def test_build_quick_live_prompt_preserves_task_004_boundaries(self) -> None:
        prompt = fa_automation.build_quick_live_prompt("QUICK: Microsoft")
        self.assertIn("ask exactly 3 relevant questions", prompt)
        self.assertIn("then stop", prompt)
        self.assertIn("current timestamped sources", prompt)
        self.assertIn("Do not perform a full AGENT workflow", prompt)
        self.assertIn("Do not create investment_report.md", prompt)
        self.assertIn("Do not issue final IC Action", prompt)
        self.assertIn("Status: Preliminary", prompt)
        self.assertIn("Status: Limited", prompt)

    def test_validate_quick_output_accepts_limited_three_question_output(self) -> None:
        validation = fa_automation.validate_quick_output(
            "Status: Limited\n\n1. Horizon?\n2. Existing position?\n3. Need latest data?"
        )
        self.assertEqual(validation.boundary_status, "Limited")
        self.assertEqual(validation.question_count, 3)

    def test_validate_quick_output_rejects_two_questions(self) -> None:
        with self.assertRaises(fa_automation.QuickRunError):
            fa_automation.validate_quick_output("Status: Preliminary\n1. Horizon?\n2. Existing position?")

    def test_validate_quick_output_rejects_status_not_first(self) -> None:
        with self.assertRaises(fa_automation.QuickRunError):
            fa_automation.validate_quick_output(
                "Before we start\nStatus: Preliminary\n1. Horizon?\n2. Existing position?\n3. Need latest data?"
            )

    def test_validate_quick_output_rejects_unnumbered_questions(self) -> None:
        with self.assertRaises(fa_automation.QuickRunError):
            fa_automation.validate_quick_output(
                "Status: Preliminary\n- Horizon?\n- Existing position?\n- Need latest data?"
            )

    def test_validate_quick_output_rejects_action_box(self) -> None:
        with self.assertRaises(fa_automation.QuickRunError):
            fa_automation.validate_quick_output(
                "Status: Preliminary\nAction Box: test\n1. Horizon?\n2. Existing position?\n3. Need latest data?"
            )

    def test_validate_quick_output_rejects_final_action_language(self) -> None:
        with self.assertRaises(fa_automation.QuickRunError):
            fa_automation.validate_quick_output(
                "Status: Preliminary\nI recommend you buy this.\n1. Horizon?\n2. Existing position?\n3. Need latest data?"
            )

    def test_validate_quick_output_rejects_missing_status(self) -> None:
        with self.assertRaises(fa_automation.QuickRunError):
            fa_automation.validate_quick_output("1. Horizon?\n2. Existing position?\n3. Need latest data?")

    def test_validate_quick_output_rejects_second_invalid_status_line(self) -> None:
        with self.assertRaises(fa_automation.QuickRunError):
            fa_automation.validate_quick_output(
                "Status: Preliminary\nStatus: Complete\n1. Horizon?\n2. Existing position?\n3. Need latest data?"
            )

    def test_validate_quick_output_rejects_bare_and_labeled_final_actions(self) -> None:
        bad_lines = [
            "Buy MSFT.",
            "Conclusion: Hold.",
            "Recommendation: trim",
            "Action: exit",
            "Sell the asset.",
            "I would trim this position.",
            "Consider selling the asset.",
            "You can buy MSFT.",
            "My view is to hold MSFT.",
        ]
        for bad_line in bad_lines:
            with self.subTest(bad_line=bad_line):
                with self.assertRaises(fa_automation.QuickRunError):
                    fa_automation.validate_quick_output(
                        f"Status: Preliminary\n{bad_line}\n1. Horizon?\n2. Existing position?\n3. Need latest data?"
                    )

    def test_validate_quick_output_rejects_report_audit_and_sizing_markers(self) -> None:
        bad_lines = [
            "Created audit folder for review.",
            "Created audit directory for review.",
            "See audit/ for details.",
            "Saved investment_report.md.",
            "Saved investment report.",
            "Report created.",
            "Created a report.",
            "I created a full audit.",
            "Audit completed.",
            "Position size 5%.",
            "Position sizing can be discussed later.",
            "Audit path: C:\\Reports\\audit",
            "Allocate $5000.",
            "Buy 25 shares.",
            "Sizing: 10 shares.",
        ]
        for bad_line in bad_lines:
            with self.subTest(bad_line=bad_line):
                with self.assertRaises(fa_automation.QuickRunError):
                    fa_automation.validate_quick_output(
                        f"Status: Preliminary\n{bad_line}\n1. Horizon?\n2. Existing position?\n3. Need latest data?"
                    )

    def test_validate_quick_output_rejects_final_action_inside_question_lines(self) -> None:
        bad_questions = [
            "1. Should I buy MSFT?",
            "1. Would you sell MSFT?",
            "1. Buy MSFT?",
            "1. Exit now?",
            "1. Are you deciding between buying or holding MSFT?",
            "1. Is this about selling MSFT?",
            "1. Should I allocate 10% to MSFT?",
            "1. What allocation are you considering?",
            "1. Should I allocate to MSFT?",
            "1. Do you want a report?",
            "1. Do you want an audit?",
            "1. Should I create a report?",
        ]
        for bad_question in bad_questions:
            with self.subTest(bad_question=bad_question):
                with self.assertRaises(fa_automation.QuickRunError):
                    fa_automation.validate_quick_output(
                        f"Status: Preliminary\n{bad_question}\n2. Existing position?\n3. Need latest data?"
                    )

    def test_mock_quick_run_does_not_echo_final_action_prompt_into_questions(self) -> None:
        result = fa_automation.mock_quick_launch("should I buy MSFT")
        self.assertNotIn("buy msft", result.output.lower())
        self.assertEqual(result.boundary_status, "Preliminary")

    def test_validate_quick_output_requires_limited_for_freshness_dependent_prompt(self) -> None:
        with self.assertRaises(fa_automation.QuickRunError):
            fa_automation.validate_quick_output(
                "Status: Preliminary\n1. Horizon?\n2. Existing position?\n3. Need latest data?",
                normalized_prompt="QUICK: latest Microsoft earnings setup",
            )

    def test_validate_quick_output_requires_freshness_question_when_prompt_is_fresh(self) -> None:
        with self.assertRaises(fa_automation.QuickRunError):
            fa_automation.validate_quick_output(
                "Status: Limited\n1. Horizon?\n2. Existing position?\n3. Risk tolerance?",
                normalized_prompt="QUICK: latest Microsoft earnings setup",
            )

    def test_validate_quick_output_rejects_generic_data_question_for_freshness_prompt(self) -> None:
        with self.assertRaises(fa_automation.QuickRunError):
            fa_automation.validate_quick_output(
                "Status: Limited\n1. Horizon?\n2. Existing position?\n3. What data should I consider?",
                normalized_prompt="QUICK: latest Microsoft earnings setup",
            )

    def test_validate_quick_output_rejects_markdown_analysis_heading(self) -> None:
        with self.assertRaises(fa_automation.QuickRunError):
            fa_automation.validate_quick_output(
                "Status: Preliminary\n## Analysis\n1. Horizon?\n2. Existing position?\n3. Need latest data?"
            )

    def test_mock_quick_run_uses_limited_for_freshness_dependent_prompt(self) -> None:
        result = fa_automation.mock_quick_launch("latest Microsoft news")
        self.assertEqual(result.boundary_status, "Limited")
        validation = fa_automation.validate_quick_output(
            result.output,
            normalized_prompt=result.normalized_prompt,
        )
        self.assertTrue(validation.freshness_required)
        self.assertTrue(validation.quality_checks["freshness_limited_when_required"])

    def test_live_launcher_uses_validated_boundary_status(self) -> None:
        launcher = fa_automation.LiveCodexQuickLauncher()
        launcher._run_codex = lambda request: "Status: Limited\n1. Horizon?\n2. Existing position?\n3. Need latest data?"  # type: ignore[method-assign]

        result = launcher.launch("Microsoft")

        self.assertEqual(result.boundary_status, "Limited")
        self.assertEqual(result.normalized_prompt, "QUICK: Microsoft")

    def test_live_launcher_rejects_invalid_output(self) -> None:
        launcher = fa_automation.LiveCodexQuickLauncher()
        launcher._run_codex = lambda request: "Status: Preliminary\n1. Horizon?\n2. Existing position?"  # type: ignore[method-assign]

        with self.assertRaises(fa_automation.QuickRunError):
            launcher.launch("Microsoft")


class LiveQuickRunTests(unittest.TestCase):
    def test_codex_quick_worker_uses_main_root_read_only_and_deny_all(self) -> None:
        calls: dict[str, object] = {}

        class FakeApprovalMode:
            deny_all = "deny_all"

        class FakeSandbox:
            read_only = "read-only"

        class FakeThread:
            def run(self, request: str, **kwargs: object) -> object:
                calls["run_request"] = request
                calls["run_kwargs"] = kwargs
                return types.SimpleNamespace(final_response="Status: Preliminary\n1. A?\n2. B?\n3. C?")

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
            fa_automation._codex_quick_worker(
                "launch quick",
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
        })


if __name__ == "__main__":
    unittest.main()
