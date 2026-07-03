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
            ("Microsoft for 3-5 years", "full_agent_workflow", "equity_full_cycle", "Microsoft", "equity"),
            ("Analyze Microsoft for 3-5 years", "full_agent_workflow", "equity_full_cycle", "Microsoft", "equity"),
            ("Проанализируй Fabrynet на 3-5 лет", "full_agent_workflow", "equity_full_cycle", "Fabrinet", "equity"),
            ("Fabrinet for 3-5 years", "full_agent_workflow", "equity_full_cycle", "Fabrinet", "equity"),
            ("Проанализируй Fabryns как инвестицию на 3-5 лет", "full_agent_workflow", "equity_full_cycle", "Fabrinet", "equity"),
            ("Should I invest in FN for 3-5 years?", "full_agent_workflow", "equity_full_cycle", "Fabrinet", "equity"),
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
            ("SENSE: why did BTC fall today?", "direct_specialist", "direct_specialist", "market-sense-agent"),
        ]
        for prompt, intent, route, target_agent in cases:
            with self.subTest(prompt=prompt):
                decision = classify_request(prompt)
                self.assertEqual(decision.detected_intent, intent)
                self.assertEqual(decision.route, route)
                if target_agent:
                    self.assertEqual(decision.target_agent, target_agent)

    def test_russian_tactical_prompt_sets_material_market_modules(self) -> None:
        decision = classify_request("AGENT: Nvidia стоит покупать сегодня после движения цены?")
        self.assertEqual(decision.route, "equity_full_cycle")
        self.assertIn(decision.decision_mode, {"Tactical setup", "Market reaction"})
        self.assertEqual(decision.materiality_plan["News & Catalysts"]["status"], "Include")
        self.assertEqual(decision.materiality_plan["Market Positioning"]["status"], "Include")
        self.assertEqual(decision.materiality_plan["Market Sense / Driver Dominance"]["status"], "Include")


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
            report_text = report.read_text(encoding="utf-8-sig")
            for forbidden in [
                "Artifact Type",
                "Analysis Status",
                "IC Action Status",
                "Gate status",
                "Mode:",
                "Route:",
                "Boundary: Not an IC Action",
                "Portfolio Fit is Limited",
                "Missing gates",
                "Limited",
                "Blocked",
                "module status",
                "handoff",
                "gate failed",
                "not personalized gate",
                "agent",
                "evidence pack",
                "source tier",
                "provider failed",
                "not found",
                "paywall",
                "premium data",
                "runtime",
            ]:
                self.assertNotIn(forbidden, report_text)
            self.assertIn("## Portfolio role", report_text)
            self.assertIn("Portfolio role is described in general terms because personal portfolio context was not provided.", report_text)
            gates_text = (audit / "gates.md").read_text(encoding="utf-8-sig")
            portfolio_text = (audit / "specialists/portfolio_fit.md").read_text(encoding="utf-8-sig")
            self.assertIn("Portfolio Fit: Limited / not personalized", gates_text)
            self.assertIn("General Portfolio Role Mode", gates_text)
            self.assertIn("Analysis Status: Limited", portfolio_text)


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

    def test_russian_report_uses_portfolio_role_language(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result = run_financial_agent(
                "Проанализируй Microsoft на 3 года, позиции нет",
                dry_run=True,
                output_dir=tmp,
                allow_interrupts=False,
            )
            report_text = Path(result["report_path"]).read_text(encoding="utf-8-sig")
            self.assertIn("# Инвестиционный отчёт", report_text)
            self.assertIn("## Портфельная роль", report_text)
            self.assertIn("в общем виде", report_text)
            self.assertIn("контекст не указан", report_text)
            self.assertIn("## \u0418\u043d\u0432\u0435\u0441\u0442\u0438\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u0432\u0437\u0433\u043b\u044f\u0434", report_text)
            self.assertIn("## \u041a\u0430\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0440\u043e\u0442\u0438\u0432 \u0442\u043e\u0447\u043a\u0438 \u0432\u0445\u043e\u0434\u0430", report_text)
            self.assertIn("## \u041a\u043b\u044e\u0447\u0435\u0432\u044b\u0435 \u0432\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043f\u0440\u043e\u0442\u0438\u0432\u043e\u0440\u0435\u0447\u0438\u044f", report_text)
            self.assertIn("## \u0427\u0442\u043e \u0438\u0437\u043c\u0435\u043d\u0438\u0442 \u0432\u0437\u0433\u043b\u044f\u0434", report_text)
            self.assertIn("## \u0427\u0442\u043e \u043e\u0442\u0441\u043b\u0435\u0436\u0438\u0432\u0430\u0442\u044c", report_text)
            self.assertNotIn("???", report_text)
            self.assertNotRegex(report_text, r"\?{3,}")
            self.assertNotIn("## Portfolio role", report_text)
            for forbidden in [
                "Artifact Type",
                "Analysis Status",
                "IC Action Status",
                "Gate status",
                "Mode:",
                "Route:",
                "Boundary: Not an IC Action",
                "Portfolio Fit is Limited",
                "Missing gates",
                "Limited",
                "Blocked",
                "module status",
                "handoff",
            ]:
                self.assertNotIn(forbidden, report_text)

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
            report_text = Path(result["report_path"]).read_text(encoding="utf-8-sig")
            self.assertTrue(Path(result["report_path"]).exists())
            self.assertNotIn("Blocked", report_text)
            self.assertNotIn("Limited", report_text)
            self.assertIn("not enough for a decision-oriented conclusion", report_text)
            audit = Path(result["audit_path"])
            self.assertIn("status: Blocked", (audit / "gates.md").read_text(encoding="utf-8-sig"))


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
            self.assertIn("final positive action is not available", report_text)
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

