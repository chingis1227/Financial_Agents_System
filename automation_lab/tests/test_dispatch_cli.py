from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

LAB_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LAB_ROOT))

import fa_automation
from agent_data.equity_resolver import resolve_equity_request


RU_ANALYZE_MSFT = "\u041f\u0440\u043e\u0430\u043d\u0430\u043b\u0438\u0437\u0438\u0440\u0443\u0439 Microsoft \u043d\u0430 3 \u0433\u043e\u0434\u0430"
RU_BUY_MSFT = "\u043a\u0443\u043f\u0438\u0442\u044c Microsoft \u043d\u0430 3 \u0433\u043e\u0434\u0430"
RU_INVEST_MSFT = "\u0441\u0442\u043e\u0438\u0442 \u043b\u0438 \u0438\u043d\u0432\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0432 Microsoft"
RU_RISK_MSFT = "\u043a\u0430\u043a\u0438\u0435 \u0440\u0438\u0441\u043a\u0438 \u0443 Microsoft"
RU_QUICK_MSFT = "\u0431\u044b\u0441\u0442\u0440\u043e \u0433\u043b\u044f\u043d\u044c Microsoft"
RU_MSFT_3Y = "Microsoft \u043d\u0430 3 \u0433\u043e\u0434\u0430"
RU_FABRYNET_3_5Y = "\u041f\u0440\u043e\u0430\u043d\u0430\u043b\u0438\u0437\u0438\u0440\u0443\u0439 Fabrynet \u043d\u0430 3-5 \u043b\u0435\u0442"
RU_FABRYNS_INVEST_3_5Y = "\u041f\u0440\u043e\u0430\u043d\u0430\u043b\u0438\u0437\u0438\u0440\u0443\u0439 Fabryns \u043a\u0430\u043a \u0438\u043d\u0432\u0435\u0441\u0442\u0438\u0446\u0438\u044e \u043d\u0430 3-5 \u043b\u0435\u0442"


class DispatchClassificationTests(unittest.TestCase):
    def test_dispatch_routes_ordinary_russian_investment_actions_to_agent(self) -> None:
        for prompt in [RU_ANALYZE_MSFT, RU_BUY_MSFT, RU_INVEST_MSFT]:
            with self.subTest(prompt=prompt):
                decision = fa_automation.classify_dispatch_prompt(prompt)
                self.assertEqual(decision.selected_dispatch, "AGENT")
                self.assertEqual(decision.selected_route, "equity_full_cycle")
                self.assertEqual(decision.target_command, "agent-intake")
                self.assertEqual(decision.normalized_prompt, f"AGENT: {prompt}")

    def test_dispatch_routes_ordinary_english_investment_action_to_agent(self) -> None:
        decision = fa_automation.classify_dispatch_prompt("Should I invest in Microsoft for 3 years?")
        self.assertEqual(decision.selected_dispatch, "AGENT")
        self.assertEqual(decision.selected_route, "equity_full_cycle")
        self.assertEqual(decision.target_command, "agent-intake")

    def test_dispatch_routes_fabrinet_aliases_to_equity_agent(self) -> None:
        for prompt in [
            "Проанализируй Fabrinet на 3-5 лет",
            RU_FABRYNET_3_5Y,
            RU_FABRYNS_INVEST_3_5Y,
            "Should I invest in FN for 3-5 years?",
        ]:
            with self.subTest(prompt=prompt):
                decision = fa_automation.classify_dispatch_prompt(prompt)
                self.assertEqual(decision.selected_dispatch, "AGENT")
                self.assertEqual(decision.selected_route, "equity_full_cycle")
                self.assertEqual(decision.target_command, "agent-intake")
                self.assertEqual(decision.normalized_prompt, f"AGENT: {prompt}")

    def test_equity_resolver_does_not_treat_horizon_range_as_ticker(self) -> None:
        for prompt in ["AGENT: Проанализируй на 3-5 лет", "AGENT: Analyze on 3–5 years"]:
            with self.subTest(prompt=prompt):
                resolved = resolve_equity_request(prompt, mode="mock")
                self.assertEqual(resolved["ticker"], "UNRESOLVED")
                self.assertNotIn(resolved["ticker"], {"3-5", "3", "5"})

    def test_dispatch_routes_quick_russian_and_english_prompts_to_quick(self) -> None:
        for prompt in [RU_QUICK_MSFT, "quick look at Microsoft"]:
            with self.subTest(prompt=prompt):
                decision = fa_automation.classify_dispatch_prompt(prompt)
                self.assertEqual(decision.selected_dispatch, "QUICK")
                self.assertEqual(decision.selected_route, "quick_take")
                self.assertEqual(decision.target_command, "quick-run")
                self.assertTrue(decision.normalized_prompt.startswith("QUICK:"))

    def test_dispatch_routes_risk_only_prompt_to_one_risk_specialist(self) -> None:
        decision = fa_automation.classify_dispatch_prompt(RU_RISK_MSFT)
        self.assertEqual(decision.selected_dispatch, "SPECIALIST")
        self.assertEqual(decision.selected_route, "direct_specialist")
        self.assertEqual(decision.target_command, "specialist-run")
        self.assertTrue(decision.target_prompt.startswith("RISK:"))

    def test_dispatch_preserves_explicit_specialist_prefix(self) -> None:
        decision = fa_automation.classify_dispatch_prompt("RISK: Microsoft")
        self.assertEqual(decision.selected_dispatch, "SPECIALIST")
        self.assertEqual(decision.selected_route, "direct_specialist")
        self.assertEqual(decision.target_command, "specialist-run")
        self.assertEqual(decision.target_prompt, "RISK: Microsoft")


    def test_dispatch_preserves_sense_specialist_prefix(self) -> None:
        decision = fa_automation.classify_dispatch_prompt("SENSE: why did BTC fall today?")
        self.assertEqual(decision.selected_dispatch, "SPECIALIST")
        self.assertEqual(decision.selected_route, "direct_specialist")
        self.assertEqual(decision.target_command, "specialist-run")
        self.assertEqual(decision.target_prompt, "SENSE: why did BTC fall today?")

    def test_dispatch_unknown_asset_needs_clarification_without_fake_workflow(self) -> None:
        for prompt in [
            "Should I buy UnknownAssetXYZ for 3 years?",
            "Проанализируй непонятную компанию XZYZZ",
        ]:
            with self.subTest(prompt=prompt):
                decision = fa_automation.classify_dispatch_prompt(prompt)
                self.assertEqual(decision.selected_dispatch, "NEEDS_CLARIFICATION")
                self.assertEqual(decision.selected_route, "needs_clarification")
                self.assertEqual(decision.target_command, "needs-clarification")


class DispatchCliTests(unittest.TestCase):
    def run_cli(self, args: list[str], base: Path) -> subprocess.CompletedProcess[str]:
        env = os.environ.copy()
        env["FA_AUTOMATION_AGENT_REPORTS_ROOT"] = str(base / "reports")
        env["FA_AUTOMATION_AGENT_RUNS_DIR"] = str(base / "agent-runs")
        env["FA_AUTOMATION_SPECIALIST_RUNS_DIR"] = str(base / "specialist-runs")
        env["FA_AUTOMATION_DISPATCH_RUNS_DIR"] = str(base / "dispatch-runs")
        env["FA_AUTOMATION_QUICK_RUNS_DIR"] = str(base / "quick-runs")
        env["FA_AUTOMATION_QUICK_DATA_RUNS_DIR"] = str(base / "quick-data")
        return subprocess.run(
            [sys.executable, "fa_automation.py", *args],
            cwd=LAB_ROOT,
            text=True,
            capture_output=True,
            env=env,
            check=False,
        )

    def latest_dispatch_log(self, base: Path) -> dict[str, object]:
        logs = sorted((base / "dispatch-runs").glob("*.json"))
        self.assertTrue(logs)
        return json.loads(logs[-1].read_text(encoding="utf-8"))

    def test_dispatch_cli_agent_intake_writes_required_log(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            base = Path(temp_dir)
            completed = self.run_cli(["dispatch", "--prompt", RU_ANALYZE_MSFT, "--mode", "mock"], base)
            self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
            self.assertIn("AGENT intake", completed.stdout)
            payload = self.latest_dispatch_log(base)
            self.assertEqual(payload["selected_dispatch"], "AGENT")
            self.assertEqual(payload["selected_route"], "equity_full_cycle")
            self.assertEqual(payload["target_command"], "agent-intake")
            self.assertEqual(payload["mode"], "mock")
            self.assertFalse(payload["executed"])
            self.assertEqual(payload["validation_status"], "pass")

    def test_dispatch_cli_quick_does_not_create_report_or_audit(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            base = Path(temp_dir)
            completed = self.run_cli(["dispatch", "--prompt", RU_QUICK_MSFT, "--mode", "mock"], base)
            self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
            self.assertIn("QUICK", completed.stdout)
            self.assertFalse(list((base / "reports").glob("**/investment_report.md")))
            self.assertFalse(list((base / "reports").glob("**/audit")))
            payload = self.latest_dispatch_log(base)
            self.assertEqual(payload["selected_dispatch"], "QUICK")
            self.assertEqual(payload["selected_route"], "quick_take")
            self.assertEqual(payload["target_command"], "quick-run")

    def test_dispatch_cli_risk_only_runs_one_specialist_with_boundary(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            base = Path(temp_dir)
            completed = self.run_cli(["dispatch", "--prompt", RU_RISK_MSFT, "--mode", "mock"], base)
            self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
            reports = list((base / "reports" / "_specialists").glob("*/specialist_report.md"))
            self.assertEqual(len(reports), 1)
            self.assertIn("Boundary: Not an IC Action", reports[0].read_text(encoding="utf-8"))
            payload = self.latest_dispatch_log(base)
            self.assertEqual(payload["selected_dispatch"], "SPECIALIST")
            self.assertEqual(payload["selected_route"], "direct_specialist")
            self.assertEqual(payload["target_command"], "specialist-run")

    def test_dispatch_cli_unknown_asset_returns_clarification_and_no_workflow(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            base = Path(temp_dir)
            completed = self.run_cli(
                ["dispatch", "--prompt", "Should I buy UnknownAssetXYZ for 3 years?", "--mode", "mock"],
                base,
            )
            self.assertNotEqual(completed.returncode, 0)
            self.assertIn("needs_clarification", completed.stdout)
            self.assertFalse(list((base / "reports").glob("**/investment_report.md")))
            payload = self.latest_dispatch_log(base)
            self.assertEqual(payload["selected_dispatch"], "NEEDS_CLARIFICATION")
            self.assertEqual(payload["validation_status"], "needs_clarification")

    def test_dispatch_cli_execute_with_baseline_creates_report_without_real_subagent_claim(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            base = Path(temp_dir)
            completed = self.run_cli(
                ["dispatch", "--prompt", RU_MSFT_3Y, "--mode", "mock", "--execute", "--continue-with-baseline"],
                base,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
            payload = self.latest_dispatch_log(base)
            self.assertEqual(payload["selected_dispatch"], "AGENT")
            self.assertEqual(payload["target_command"], "agent-run")
            self.assertTrue(payload["report_path"])
            manifest_path = Path(str(payload["report_path"])).parent / "audit" / "run_manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            self.assertFalse(manifest["production_real_subagents"])
            self.assertIn("Mock specialist outputs", manifest["mock_mode_notice"])


if __name__ == "__main__":
    unittest.main()
