from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

LAB_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LAB_ROOT))

import fa_automation

EXPECTED_PROJECT_ROOT = r"C:\Users\ShumeikoYe\OneDrive\Documents\Financial Agent System"
EXPECTED_REPORTS_ROOT = r"C:\Users\ShumeikoYe\OneDrive\Documents\Financial Agent Reports"


class AgentDesignCliTests(unittest.TestCase):
    def run_cli(self, args: list[str], runs_dir: Path) -> subprocess.CompletedProcess[str]:
        env = os.environ.copy()
        env["FA_AUTOMATION_UNIT_LIVE_STUB"] = "1"
        env["FA_AUTOMATION_AGENT_DESIGN_RUNS_DIR"] = str(runs_dir)
        return subprocess.run(
            [sys.executable, "fa_automation.py", *args],
            cwd=LAB_ROOT,
            text=True,
            capture_output=True,
            check=False,
            env=env,
        )

    def test_mock_agent_design_creates_valid_json_log(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            runs_dir = Path(temp_dir)
            completed = self.run_cli(
                ["agent-design", "--prompt", "Microsoft for 3 years", "--mode", "live"],
                runs_dir,
            )

            self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
            created = sorted(runs_dir.glob("*.json"), key=lambda path: path.stat().st_mtime)
            self.assertEqual(len(created), 1, "Expected exactly one AGENT design JSON log")

            payload = json.loads(created[-1].read_text(encoding="utf-8"))
            self.assertEqual(payload["mode"], "live")
            self.assertEqual(payload["workflow"], "agent_automation_design")
            self.assertEqual(payload["project_root"], EXPECTED_PROJECT_ROOT)
            self.assertEqual(payload["prompt"], "Microsoft for 3 years")
            self.assertEqual(payload["normalized_prompt"], "AGENT: Microsoft for 3 years")
            self.assertEqual(payload["selected_route"], "equity_full_cycle")
            self.assertEqual(payload["validation"]["status"], "pass")
            self.assertEqual(payload["validation"]["question_count"], 5)
            self.assertTrue(payload["validation"]["quality_checks"]["design_only"])
            self.assertTrue(payload["validation"]["quality_checks"]["exactly_five_questions"])
            self.assertTrue(payload["validation"]["quality_checks"]["planned_not_claimed_subagents"])
            self.assertIn("evidence_freshness", payload["validation"]["required_gates_present"])
            self.assertIn("lead_asset_analysis", payload["validation"]["required_gates_present"])
            self.assertIn("implementation_vehicle_quality", payload["validation"]["required_gates_present"])
            self.assertEqual(payload["design"]["actual_subagents_run"], [])
            self.assertEqual(payload["design"]["artifact_plan"]["reports_root"], EXPECTED_REPORTS_ROOT)
            self.assertEqual(payload["design"]["artifact_plan"]["run_folder_pattern"], "[ASSET] yyyy-mm-dd hhmm")
            self.assertEqual(payload["design"]["artifact_plan"]["report_file"], "investment_report.md")
            self.assertEqual(payload["design"]["artifact_plan"]["audit_directory"], "audit")
            self.assertIn("Prompt: captured in run log", completed.stdout)

    def test_agent_route_card_map_exactly_covers_valid_routes(self) -> None:
        self.assertEqual(set(fa_automation.AGENT_ROUTE_CARDS), fa_automation.VALID_ROUTES)

    def test_agent_prefix_is_not_duplicated(self) -> None:
        result = fa_automation.build_mock_agent_design("AGENT: BTC")
        self.assertEqual(result.normalized_prompt, "AGENT: BTC")

    def test_mock_agent_design_routes_crypto_and_plans_relevant_subagents(self) -> None:
        result = fa_automation.build_mock_agent_design("BTC latest news for 3 years")
        validation = fa_automation.validate_agent_design(result.design)

        self.assertEqual(result.selected_route, "crypto_full_cycle")
        self.assertEqual(validation.question_count, 5)
        self.assertIn("crypto-agent", result.design["planned_subagents"])
        self.assertIn("evidence-collector", result.design["planned_subagents"])
        self.assertIn("investment-committee-agent", result.design["planned_subagents"])
        self.assertIn(
            "timestamped sources",
            result.design["first_action"]["questions"][4],
        )

    def test_agent_design_uses_russian_questions_for_russian_prompt(self) -> None:
        result = fa_automation.build_mock_agent_design("MSFT последние новости")

        self.assertEqual(result.selected_route, "equity_full_cycle")
        self.assertIn(
            "датированные источники",
            result.design["first_action"]["questions"][4],
        )

    def test_validate_agent_design_rejects_missing_gate(self) -> None:
        result = fa_automation.build_mock_agent_design("Microsoft")
        bad_design = json.loads(json.dumps(result.design, ensure_ascii=False))
        bad_design["required_gates"].remove("risk_red_team")

        with self.assertRaises(ValueError):
            fa_automation.validate_agent_design(bad_design)

    def test_validate_agent_design_rejects_omitted_canonical_ic_gate(self) -> None:
        result = fa_automation.build_mock_agent_design("Microsoft")
        bad_design = json.loads(json.dumps(result.design, ensure_ascii=False))
        bad_design["required_gates"].remove("implementation_vehicle_quality")

        with self.assertRaises(ValueError):
            fa_automation.validate_agent_design(bad_design)

    def test_validate_agent_design_rejects_extra_gate(self) -> None:
        result = fa_automation.build_mock_agent_design("Microsoft")
        bad_design = json.loads(json.dumps(result.design, ensure_ascii=False))
        bad_design["required_gates"].append("unapproved_gate")

        with self.assertRaises(ValueError):
            fa_automation.validate_agent_design(bad_design)

    def test_validate_agent_design_rejects_duplicate_gate(self) -> None:
        result = fa_automation.build_mock_agent_design("Microsoft")
        bad_design = json.loads(json.dumps(result.design, ensure_ascii=False))
        bad_design["required_gates"].append("risk_red_team")

        with self.assertRaises(ValueError):
            fa_automation.validate_agent_design(bad_design)

    def test_validate_agent_design_rejects_route_card_mismatch(self) -> None:
        result = fa_automation.build_mock_agent_design("Microsoft")
        bad_design = json.loads(json.dumps(result.design, ensure_ascii=False))
        bad_design["route_card"] = "workflows/route_cards/crypto_full_cycle.md"

        with self.assertRaises(ValueError):
            fa_automation.validate_agent_design(bad_design)

    def test_route_card_for_selected_route_fails_for_missing_mapping(self) -> None:
        original = fa_automation.AGENT_ROUTE_CARDS.pop("equity_full_cycle")
        try:
            with self.assertRaises(fa_automation.AgentDesignError):
                fa_automation.route_card_for_selected_route("equity_full_cycle")
        finally:
            fa_automation.AGENT_ROUTE_CARDS["equity_full_cycle"] = original

    def test_validate_agent_design_rejects_wrong_question_count(self) -> None:
        result = fa_automation.build_mock_agent_design("Microsoft")
        bad_design = json.loads(json.dumps(result.design, ensure_ascii=False))
        bad_design["first_action"]["questions"] = bad_design["first_action"]["questions"][:4]

        with self.assertRaises(ValueError):
            fa_automation.validate_agent_design(bad_design)

    def test_validate_agent_design_rejects_subagent_execution_claim(self) -> None:
        result = fa_automation.build_mock_agent_design("Microsoft")
        bad_design = json.loads(json.dumps(result.design, ensure_ascii=False))
        bad_design["subagent_truthfulness_policy"] = "subagents completed review"

        with self.assertRaises(ValueError):
            fa_automation.validate_agent_design(bad_design)

    def test_validate_agent_design_rejects_named_agent_execution_claim(self) -> None:
        result = fa_automation.build_mock_agent_design("Microsoft")
        bad_design = json.loads(json.dumps(result.design, ensure_ascii=False))
        bad_design["subagent_truthfulness_policy"] = "evidence-collector completed"

        with self.assertRaises(ValueError):
            fa_automation.validate_agent_design(bad_design)

    def test_validate_agent_design_rejects_broader_execution_claims(self) -> None:
        bad_claims = [
            "subagents finished",
            "agent outputs delivered",
            "analyst packet received",
            "review completed by evidence-collector",
        ]
        for claim in bad_claims:
            with self.subTest(claim=claim):
                result = fa_automation.build_mock_agent_design("Microsoft")
                bad_design = json.loads(json.dumps(result.design, ensure_ascii=False))
                bad_design["subagent_truthfulness_policy"] = claim

                with self.assertRaises(ValueError):
                    fa_automation.validate_agent_design(bad_design)

    def test_validate_agent_design_rejects_actual_subagents_in_design_mode(self) -> None:
        result = fa_automation.build_mock_agent_design("Microsoft")
        bad_design = json.loads(json.dumps(result.design, ensure_ascii=False))
        bad_design["actual_subagents_run"] = ["evidence-collector"]

        with self.assertRaises(ValueError):
            fa_automation.validate_agent_design(bad_design)

    def test_agent_design_rejects_unroutable_mock_prompt(self) -> None:
        with self.assertRaises(fa_automation.AgentDesignError):
            fa_automation.build_mock_agent_design("unidentified private asset")

    def test_validate_agent_design_rejects_unknown_planned_subagent(self) -> None:
        result = fa_automation.build_mock_agent_design("Microsoft")
        bad_design = json.loads(json.dumps(result.design, ensure_ascii=False))
        bad_design["planned_subagents"].append("unknown-agent")

        with self.assertRaises(ValueError):
            fa_automation.validate_agent_design(bad_design)

    def test_validate_agent_design_rejects_report_root_inside_lab_repo(self) -> None:
        result = fa_automation.build_mock_agent_design("Microsoft")
        bad_design = json.loads(json.dumps(result.design, ensure_ascii=False))
        bad_design["artifact_plan"]["reports_root"] = str(LAB_ROOT / "reports")

        with self.assertRaises(ValueError):
            fa_automation.validate_agent_design(bad_design)

    def test_validate_agent_design_rejects_report_root_inside_main_project(self) -> None:
        result = fa_automation.build_mock_agent_design("Microsoft")
        bad_design = json.loads(json.dumps(result.design, ensure_ascii=False))
        bad_design["artifact_plan"]["reports_root"] = EXPECTED_PROJECT_ROOT

        with self.assertRaises(ValueError):
            fa_automation.validate_agent_design(bad_design)

    def test_validate_agent_design_rejects_invalid_run_folder_pattern(self) -> None:
        result = fa_automation.build_mock_agent_design("Microsoft")
        bad_design = json.loads(json.dumps(result.design, ensure_ascii=False))
        bad_design["artifact_plan"]["run_folder_pattern"] = "asset-folder"

        with self.assertRaises(ValueError):
            fa_automation.validate_agent_design(bad_design)


if __name__ == "__main__":
    unittest.main()
