from __future__ import annotations

import os
import tempfile
import unittest
from pathlib import Path

from langgraph_runtime.financial_agent_graph import build_graph, run_financial_agent
from langgraph_runtime.routing import classify_request


class LangGraphRuntimeTests(unittest.TestCase):
    def test_natural_language_intake_routing_examples(self) -> None:
        cases = [
            ("Проанализируй Microsoft на 3 года, позиции нет", "full_agent_workflow", "equity_full_cycle", "Microsoft", "equity"),
            ("Стоит ли покупать Nvidia?", "full_agent_workflow", "equity_full_cycle", "Nvidia", "equity"),
            ("Быстро глянь Apple", "quick_take", "quick_take", "Apple", "equity"),
            ("Оцени риски Tesla", "direct_specialist", "direct_specialist", "Tesla", "equity"),
            ("Почему сегодня упал Bitcoin?", "market_news_update", "market_news_update", "Bitcoin", "crypto"),
            ("QQQ или SCHG что лучше?", "comparison", "multi_asset_comparison", "QQQ vs SCHG", "etf"),
        ]
        for prompt, intent, route, asset, asset_class in cases:
            with self.subTest(prompt=prompt):
                decision = classify_request(prompt)
                self.assertEqual(decision.detected_intent, intent)
                self.assertEqual(decision.route, route)
                self.assertEqual(decision.asset_identity, asset)
                self.assertEqual(decision.asset_class, asset_class)

    def test_explicit_prefix_routing(self) -> None:
        cases = [
            ("AGENT: Microsoft for 3 years, no current position", "full_agent_workflow", "equity_full_cycle", ""),
            ("QUICK: Apple", "quick_take", "quick_take", ""),
            ("RISK: Tesla", "direct_specialist", "direct_specialist", "risk-red-team-agent"),
        ]
        for prompt, intent, route, target_agent in cases:
            with self.subTest(prompt=prompt):
                decision = classify_request(prompt)
                self.assertEqual(decision.detected_intent, intent)
                self.assertEqual(decision.route, route)
                if target_agent:
                    self.assertEqual(decision.target_agent, target_agent)


    def test_blocked_intake_category_exists(self) -> None:
        decision = classify_request("BLOCKED: cannot route this request")
        self.assertEqual(decision.detected_intent, "blocked")
        self.assertEqual(decision.route, "blocked")

    def test_equity_full_cycle_dry_run_creates_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result = run_financial_agent(
                "AGENT: Microsoft for 3 years, no current position",
                dry_run=True,
                output_dir=tmp,
                allow_interrupts=False,
            )
            self.assertEqual(result["detected_intent"], "full_agent_workflow")
            self.assertEqual(result["route"], "equity_full_cycle")
            self.assertEqual(result["final_status"], "Limited")
            report = Path(result["report_path"])
            audit = Path(result["audit_path"])
            self.assertTrue(report.exists())
            for rel in [
                "run_metadata.md",
                "intake.md",
                "sources.md",
                "evidence_plan.md",
                "evidence_pack.md",
                "gates.md",
                "ic_synthesis.md",
                "specialists/equity_company_analysis.md",
                "specialists/valuation_expectations.md",
                "specialists/risk_red_team.md",
                "specialists/portfolio_fit.md",
            ]:
                self.assertTrue((audit / rel).exists(), rel)


    def test_non_equity_full_routes_do_not_run_equity_subgraph(self) -> None:
        prompts = [
            ("AGENT: BTC for 3 years, should I invest?", "crypto_full_cycle", "crypto_asset_analysis"),
            ("AGENT: should I buy TLT as a bond ETF?", "fixed_income_full_cycle", "fixed_income_analysis"),
        ]
        for prompt, route, expected_key in prompts:
            with self.subTest(prompt=prompt), tempfile.TemporaryDirectory() as tmp:
                result = run_financial_agent(prompt, dry_run=True, output_dir=tmp, allow_interrupts=False)
                self.assertEqual(result["route"], route)
                self.assertIn(expected_key, result["specialist_outputs"])
                self.assertNotIn("equity_company_analysis", result["specialist_outputs"])
                self.assertTrue(Path(result["report_path"]).exists())

    def test_missing_context_interrupt(self) -> None:
        result = run_financial_agent("Стоит ли покупать Nvidia?", dry_run=True, allow_interrupts=True)
        self.assertIn("__interrupt__", result)
        self.assertEqual(result["route"], "equity_full_cycle")
        payload = result["__interrupt__"][0].value
        self.assertEqual(payload["kind"], "missing_context")
        self.assertIn("horizon", payload["missing_context"])

    def test_blocked_evidence_gate(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result = run_financial_agent(
                "AGENT: Microsoft for 3 years, no current position, without evidence",
                dry_run=True,
                output_dir=tmp,
                allow_interrupts=False,
            )
            self.assertEqual(result["final_status"], "Blocked")
            self.assertEqual(result["gate_statuses"]["evidence_readiness"]["status"], "Blocked")
            self.assertTrue(Path(result["report_path"]).exists())


    def test_risk_gate_interrupt_when_enabled(self) -> None:
        result = run_financial_agent(
            "AGENT: Microsoft for 3 years, no current position",
            dry_run=True,
            allow_interrupts=True,
        )
        self.assertIn("__interrupt__", result)
        payload = result["__interrupt__"][0].value
        self.assertEqual(payload["kind"], "risk_gate_failed")

    def test_no_positive_ic_action_when_gates_fail(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result = run_financial_agent(
                "AGENT: Microsoft for 3 years, no current position",
                dry_run=True,
                output_dir=tmp,
                allow_interrupts=False,
            )
            self.assertEqual(result["ic_synthesis"]["ic_action_status"], "Not an IC Action")
            report_text = Path(result["report_path"]).read_text(encoding="utf-8-sig")
            self.assertIn("No positive final IC Action", report_text)
            self.assertNotIn("IC Action Status: Buy", report_text)
            self.assertNotIn("Action Box", report_text)

    def test_graph_builds_with_checkpointer(self) -> None:
        graph = build_graph()
        self.assertIsNotNone(graph)

    def test_live_mode_requires_key_before_api_call(self) -> None:
        old_key = os.environ.pop("OPENAI_API_KEY", None)
        try:
            with self.assertRaisesRegex(RuntimeError, "OPENAI_API_KEY is required"):
                run_financial_agent("AGENT: Microsoft for 3 years, no current position", live=True)
        finally:
            if old_key is not None:
                os.environ["OPENAI_API_KEY"] = old_key


if __name__ == "__main__":
    unittest.main()

