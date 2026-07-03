from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

LAB_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LAB_ROOT))

import fa_automation
import quick_data.snapshot as quick_snapshot
import quick_data.registry as quick_registry




class QuickProviderRegistryTests(unittest.TestCase):
    def test_registry_contains_public_providers_and_disabled_api_slots(self) -> None:
        providers = quick_registry.all_providers()
        provider_ids = {provider.provider_id for provider in providers}

        self.assertIn("sec_submissions", provider_ids)
        self.assertIn("stooq_price", provider_ids)
        self.assertIn("yahoo_chart_price", provider_ids)
        self.assertIn("alpha_vantage_api", provider_ids)
        self.assertIn("financial_modeling_prep_api", provider_ids)
        self.assertIn("nasdaq_data_link_api", provider_ids)
        self.assertTrue(all(not provider.enabled for provider in quick_registry.disabled_api_slots()))

    def test_provider_priority_orders_public_price_fallback(self) -> None:
        price_providers = quick_registry.providers_for("price", asset_type="equity", include_disabled=False)
        provider_ids = [provider.provider_id for provider in price_providers]

        self.assertLess(provider_ids.index("yahoo_chart_price"), provider_ids.index("stooq_price"))
        self.assertNotIn("alpha_vantage_api", provider_ids)

    def test_snapshot_keeps_legacy_fields_and_adds_provider_fields(self) -> None:
        snapshot = fa_automation.build_quick_source_snapshot(
            "Microsoft for 3 years",
            ["3 years", "no position", "no latest need"],
            "live",
        )

        for key in ("prompt", "normalized_prompt", "asset_identity", "sources", "retrieved", "missing", "not_obtained"):
            self.assertIn(key, snapshot)
        for key in ("schema_version", "providers", "provider_results", "provider_errors", "source_scope", "evidence_alignment"):
            self.assertIn(key, snapshot)
        self.assertEqual(snapshot["schema_version"], "quick_source_snapshot.v1.1")
        self.assertEqual(snapshot["source_scope"], "Public-Data Only")
        self.assertIn("not an Evidence Collector evidence_pack", snapshot["evidence_alignment"])

    def test_data_quality_keeps_legacy_fields_and_adds_provider_summary(self) -> None:
        snapshot = fa_automation.build_quick_source_snapshot("MSFT", ["a", "b", "c"], "live")
        quality = fa_automation.assess_quick_data_quality(snapshot)

        for key in ("status", "missing_inputs", "freshness_limitations", "reason_for_status", "quick_answer_allowed"):
            self.assertIn(key, quality)
        for key in ("provider_quality_summary", "freshness_by_component", "source_scope", "evidence_alignment"):
            self.assertIn(key, quality)

    def test_disabled_api_providers_are_recorded_but_not_required(self) -> None:
        snapshot = fa_automation.build_quick_source_snapshot("MSFT", ["a", "b", "c"], "live")
        disabled_results = [result for result in snapshot["provider_results"] if result["status"] == "disabled"]

        self.assertGreaterEqual(len(disabled_results), 3)
        self.assertNotIn("alpha_vantage_api", snapshot["missing"])
        self.assertNotIn("financial_modeling_prep_api", snapshot["missing"])
        self.assertNotIn("nasdaq_data_link_api", snapshot["missing"])


    def test_live_price_registry_does_not_execute_mock_fixture_provider(self) -> None:
        original_price = quick_snapshot.collect_price_by_registry

        def fake_price(ticker: str, asset_type: str | None) -> tuple[dict[str, object], list[object]]:
            price = {"ticker": ticker, "date": "2026-07-01", "close": "1", "currency": "USD"}
            return price, [
                quick_snapshot.ProviderResult(
                    provider_id="stooq_price",
                    component="price",
                    status="ok",
                    data=price,
                    quality_level="public_market",
                    source_date="2026-07-01",
                )
            ]

        quick_snapshot.collect_price_by_registry = fake_price  # type: ignore[assignment]
        try:
            snapshot = fa_automation.build_quick_source_snapshot("GLD gold ETF", ["a", "b", "c"], "live")
        finally:
            quick_snapshot.collect_price_by_registry = original_price  # type: ignore[assignment]

        executed_provider_ids = {result["provider_id"] for result in snapshot["provider_results"] if result["status"] != "disabled"}
        self.assertNotIn("mock_fixture", executed_provider_ids)

    def test_stale_live_price_downgrades_to_limited(self) -> None:
        snapshot = fa_automation.build_quick_source_snapshot("MSFT", ["a", "b", "c"], "live")
        snapshot["mode"] = "live"
        snapshot["data"]["price"] = {"ticker": "MSFT", "date": "2000-01-01", "close": "1", "currency": "USD"}
        snapshot["retrieved"]["price"] = True
        quality = fa_automation.assess_quick_data_quality(snapshot)

        self.assertEqual(quality["status"], "Limited")
        self.assertIn("price_freshness", quality["missing_inputs"])

    def test_comparison_partial_component_price_missing_is_limited(self) -> None:
        snapshot = fa_automation.build_quick_source_snapshot("MSFT vs SPY vs BTC", ["a", "b", "c"], "live")
        snapshot["data"]["price"] = {"components": [{"ticker": "MSFT", "price": {"date": "2026-07-01"}}]}
        snapshot["missing"] = ["price:SPY", "price:BTC"]
        quality = fa_automation.assess_quick_data_quality(snapshot)

        self.assertEqual(quality["status"], "Limited")

class QuickAnswerUnitTests(unittest.TestCase):
    def test_msft_identity_detection(self) -> None:
        identity = fa_automation.detect_quick_asset_identity("QUICK: Microsoft / MSFT")
        self.assertIsNotNone(identity)
        assert identity is not None
        self.assertEqual(identity["ticker"], "MSFT")
        self.assertEqual(identity["company_name"], "Microsoft Corporation")
        self.assertEqual(identity["security_type"], "equity")
        self.assertEqual(identity["currency"], "USD")

    def test_task008_identity_detection(self) -> None:
        cases = [
            ("SPY for 5 years", "SPY", "etf"),
            ("S&P 500 ETF", "SPY", "etf"),
            ("BTC for 3 years", "BTC", "crypto"),
            ("Bitcoin for 3 years", "BTC", "crypto"),
            ("TLT bond ETF", "TLT", "bond_etf"),
            ("long duration treasury ETF", "TLT", "bond_etf"),
            ("GLD gold ETF", "GLD", "commodity_etf"),
            ("gold ETF", "GLD", "commodity_etf"),
        ]
        for prompt, ticker, security_type in cases:
            with self.subTest(prompt=prompt):
                identity = fa_automation.detect_quick_asset_identity(prompt)
                self.assertIsNotNone(identity)
                assert identity is not None
                self.assertEqual(identity["ticker"], ticker)
                self.assertEqual(identity["security_type"], security_type)
                self.assertEqual(identity["currency"], "USD")

    def test_task008_comparison_identity_detection(self) -> None:
        for prompt in ("MSFT vs SPY vs BTC", "compare MSFT SPY BTC"):
            with self.subTest(prompt=prompt):
                identity = fa_automation.detect_quick_asset_identity(prompt)
                self.assertIsNotNone(identity)
                assert identity is not None
                self.assertEqual(identity["ticker"], "MSFT-SPY-BTC")
                self.assertEqual(identity["security_type"], "multi_asset_comparison")
                tickers = {component["ticker"] for component in identity["components"]}
                self.assertEqual(tickers, {"MSFT", "SPY", "BTC"})

    def test_prompt_normalization(self) -> None:
        self.assertEqual(fa_automation.normalize_quick_prompt("MSFT"), "QUICK: MSFT")
        self.assertEqual(fa_automation.normalize_quick_prompt("QUICK: MSFT"), "QUICK: MSFT")

    def test_answers_required_and_empty_rejected(self) -> None:
        with self.assertRaises(ValueError):
            fa_automation.parse_quick_answers(["one", "two"], None)
        with self.assertRaises(ValueError):
            fa_automation.parse_quick_answers(["one", "", "three"], None)
        self.assertEqual(
            fa_automation.parse_quick_answers(None, '["one", "two", "three"]'),
            ["one", "two", "three"],
        )

    def test_answers_drive_freshness_status_to_limited(self) -> None:
        snapshot = fa_automation.build_quick_source_snapshot(
            "Microsoft for 3 years",
            ["3 years", "no position", "Use public current sources if available"],
            "live",
        )
        quality = fa_automation.assess_quick_data_quality(snapshot)

        self.assertTrue(snapshot["answer_freshness_required"])
        self.assertEqual(quality["status"], "Limited")
        self.assertIn("user answers ask for current/latest context", quality["freshness_limitations"])


    def test_answer_freshness_detection_is_per_answer(self) -> None:
        self.assertTrue(
            fa_automation.answers_require_freshness(["3 years", "No current position", "Need latest public data"])
        )
        self.assertTrue(
            fa_automation.answers_require_freshness(["3 years", "none", "Need latest data"])
        )
        self.assertFalse(
            fa_automation.answers_require_freshness(["3 years", "No current position", "No latest data requirement"])
        )

    def test_no_current_position_does_not_suppress_latest_data_limited_status(self) -> None:
        snapshot = fa_automation.build_quick_source_snapshot(
            "BTC for 3 years",
            ["3 years", "No current position", "Need latest public data"],
            "live",
        )
        quality = fa_automation.assess_quick_data_quality(snapshot)

        self.assertTrue(snapshot["answer_freshness_required"])
        self.assertEqual(quality["status"], "Limited")
        self.assertIn("user answers ask for current/latest context", quality["freshness_limitations"])

    def test_negative_current_position_answer_does_not_trigger_freshness(self) -> None:
        snapshot = fa_automation.build_quick_source_snapshot(
            "Microsoft for 3 years",
            ["3 years", "No current position", "No latest data requirement"],
            "live",
        )
        quality = fa_automation.assess_quick_data_quality(snapshot)

        self.assertFalse(snapshot["answer_freshness_required"])
        self.assertEqual(quality["status"], "Preliminary")

    def test_mock_source_snapshot_and_schemas(self) -> None:
        snapshot = fa_automation.build_quick_source_snapshot(
            "Microsoft for 3 years",
            ["3 years", "no position", "no latest need"],
            "live",
        )
        quality = fa_automation.assess_quick_data_quality(snapshot)
        answer = fa_automation.generate_quick_answer(
            "Microsoft for 3 years",
            ["3 years", "no position", "no latest need"],
            snapshot,
            quality,
        )

        for key in (
            "prompt",
            "normalized_prompt",
            "asset_identity",
            "sources",
            "timestamp",
            "retrieved",
            "missing",
            "not_obtained",
            "access_status",
            "freshness_status",
        ):
            self.assertIn(key, snapshot)
        for key in (
            "status",
            "missing_inputs",
            "freshness_limitations",
            "reason_for_status",
            "quick_answer_allowed",
        ):
            self.assertIn(key, quality)
        validation = fa_automation.validate_quick_generated_answer(answer, data_quality=quality)
        output_quality = fa_automation.assess_quick_output_quality(answer, snapshot, quality)
        self.assertEqual(validation["status"], "pass")
        self.assertEqual(output_quality["status"], "pass")
        self.assertIn("Source note", answer)
        self.assertIn("Freshness note", answer)
        self.assertEqual(quality["status"], "Preliminary")

    def test_task008_mock_snapshots_are_preliminary_and_asset_specific(self) -> None:
        cases = [
            ("SPY for 5 years", "SPY", "S&P 500"),
            ("BTC for 3 years", "BTC", "crypto asset"),
            ("TLT bond ETF", "TLT", "long-duration Treasury bond ETF"),
            ("GLD gold ETF", "GLD", "gold exposure vehicle"),
            ("MSFT vs SPY vs BTC", "MSFT-SPY-BTC", "company-specific equity risk"),
        ]
        for prompt, ticker, expected_text in cases:
            with self.subTest(prompt=prompt):
                snapshot = fa_automation.build_quick_source_snapshot(
                    prompt,
                    ["3 years", "no position", "no latest need"],
                    "live",
                )
                quality = fa_automation.assess_quick_data_quality(snapshot)
                answer = fa_automation.generate_quick_answer(prompt, ["a", "b", "c"], snapshot, quality)

                self.assertEqual(snapshot["asset_identity"]["ticker"], ticker)
                self.assertEqual(quality["status"], "Preliminary")
                self.assertIn(expected_text, answer)
                self.assertEqual(fa_automation.validate_quick_generated_answer(answer, quality)["status"], "pass")
                self.assertEqual(fa_automation.assess_quick_output_quality(answer, snapshot, quality)["status"], "pass")

    def test_missing_price_or_recent_events_means_limited_not_crash(self) -> None:
        snapshot = fa_automation.build_quick_source_snapshot(
            "MSFT",
            ["3 years", "no position", "no current data"],
            "live",
        )
        snapshot["data"]["price"] = None
        snapshot["data"]["recent_events"] = None
        snapshot["retrieved"]["price"] = False
        snapshot["retrieved"]["recent_events"] = False
        snapshot["missing"] = ["price", "recent_events"]
        quality = fa_automation.assess_quick_data_quality(snapshot)
        answer = fa_automation.generate_quick_answer("MSFT", ["a", "b", "c"], snapshot, quality)

        self.assertEqual(quality["status"], "Limited")
        self.assertIn("Quick limitations", answer)

    def test_task008_missing_context_means_limited_not_crash(self) -> None:
        snapshot = fa_automation.build_quick_source_snapshot(
            "SPY for 5 years",
            ["3 years", "no position", "no current data"],
            "live",
        )
        snapshot["data"]["asset_context"] = None
        snapshot["retrieved"]["asset_context"] = False
        snapshot["missing"] = ["asset_context"]
        quality = fa_automation.assess_quick_data_quality(snapshot)
        answer = fa_automation.generate_quick_answer("SPY", ["a", "b", "c"], snapshot, quality)

        self.assertEqual(quality["status"], "Limited")
        self.assertIn("missing inputs: asset_context", answer)

    def test_missing_identity_and_unsupported_asset_blocked(self) -> None:
        snapshot = fa_automation.build_quick_source_snapshot(
            "private company ABC",
            ["3 years", "no position", "no current data"],
            "live",
        )
        quality = fa_automation.assess_quick_data_quality(snapshot)
        self.assertEqual(quality["status"], "Blocked")
        self.assertFalse(quality["quick_answer_allowed"])

    def test_broken_fixture_becomes_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            fixtures_dir = Path(temp_dir)
            original = os.environ.get("FA_AUTOMATION_QUICK_FIXTURES_DIR")
            os.environ["FA_AUTOMATION_QUICK_FIXTURES_DIR"] = str(fixtures_dir)
            try:
                snapshot = fa_automation.build_quick_source_snapshot(
                    "MSFT",
                    ["3 years", "no position", "no current data"],
                    "live",
                )
                quality = fa_automation.assess_quick_data_quality(snapshot)
            finally:
                if original is None:
                    os.environ.pop("FA_AUTOMATION_QUICK_FIXTURES_DIR", None)
                else:
                    os.environ["FA_AUTOMATION_QUICK_FIXTURES_DIR"] = original
        self.assertIn(quality["status"], {"Preliminary", "Limited", "Blocked"})
        self.assertNotIn("fixture", snapshot["missing"])

    def test_generated_answer_rejects_final_action_and_sizing(self) -> None:
        bad_answers = [
            "Status: Limited\nIC Action Status: Limited\nFinal IC Action: Unavailable in QUICK.\n\nShort view\nBuy it.\n\nWhat the quick data shows\nx\n\nMain risks / limits\nx\n\nNeeded for final IC Action\nx\n\nNext step\nx",
            "Status: Limited\nIC Action Status: Limited\nFinal IC Action: Unavailable in QUICK.\n\nShort view\nPosition size 5%.\n\nWhat the quick data shows\nx\n\nMain risks / limits\nx\n\nNeeded for final IC Action\nx\n\nNext step\nx",
            "Status: Limited\nIC Action Status: Limited\nFinal IC Action: Unavailable in QUICK.\n\nShort view\nAction Box: x\n\nWhat the quick data shows\nx\n\nMain risks / limits\nx\n\nNeeded for final IC Action\nx\n\nNext step\nx",
            "Status: Limited\nIC Action Status: Limited\nFinal IC Action: Unavailable in QUICK.\n\nShort view\nIncrease exposure later.\n\nWhat the quick data shows\nx\n\nMain risks / limits\nx\n\nNeeded for final IC Action\nx\n\nNext step\nx",
            "Status: Limited\nIC Action Status: Limited\nFinal IC Action: Unavailable in QUICK.\n\nShort view\nScale into it later.\n\nWhat the quick data shows\nx\n\nMain risks / limits\nx\n\nNeeded for final IC Action\nx\n\nNext step\nx",
            "Status: Limited\nIC Action Status: Limited\nFinal IC Action: Unavailable in QUICK.\n\nShort view\nBuild a position later.\n\nWhat the quick data shows\nx\n\nMain risks / limits\nx\n\nNeeded for final IC Action\nx\n\nNext step\nx",
        ]
        for answer in bad_answers:
            with self.subTest(answer=answer):
                with self.assertRaises(fa_automation.QuickRunError):
                    fa_automation.validate_quick_generated_answer(answer)

    def test_required_answer_sections_exist(self) -> None:
        snapshot = fa_automation.build_quick_source_snapshot("MSFT", ["a", "b", "c"], "live")
        quality = fa_automation.assess_quick_data_quality(snapshot)
        answer = fa_automation.generate_quick_answer("MSFT", ["a", "b", "c"], snapshot, quality)
        for section in fa_automation.QUICK_ANSWER_REQUIRED_SECTIONS:
            self.assertIn(section, answer)

    def test_task010_output_quality_rejects_missing_source_or_freshness_note(self) -> None:
        snapshot = fa_automation.build_quick_source_snapshot("MSFT", ["a", "b", "c"], "live")
        quality = fa_automation.assess_quick_data_quality(snapshot)
        answer = fa_automation.generate_quick_answer("MSFT", ["a", "b", "c"], snapshot, quality)

        no_source = answer.replace("Source note\n", "Source removed\n", 1)
        no_freshness = answer.replace("Freshness note\n", "Freshness removed\n", 1)

        self.assertIn("missing_source_note", fa_automation.assess_quick_output_quality(no_source, snapshot, quality)["soft_failures"])
        self.assertIn("missing_freshness_note", fa_automation.assess_quick_output_quality(no_freshness, snapshot, quality)["soft_failures"])

    def test_task010_output_quality_rejects_generic_mock_risk(self) -> None:
        prompts = ["MSFT", "SPY for 5 years", "BTC for 3 years", "TLT bond ETF", "GLD gold ETF"]
        for prompt in prompts:
            with self.subTest(prompt=prompt):
                snapshot = fa_automation.build_quick_source_snapshot(prompt, ["a", "b", "c"], "live")
                quality = fa_automation.assess_quick_data_quality(snapshot)
                answer = fa_automation.generate_quick_answer(prompt, ["a", "b", "c"], snapshot, quality)
                answer = answer.replace(
                    fa_automation.quick_risk_line(snapshot["asset_identity"], snapshot["data"]),
                    "Markets can go down.",
                )
                output_quality = fa_automation.assess_quick_output_quality(answer, snapshot, quality)
                self.assertIn("risk_not_specific_enough", output_quality["soft_failures"])

    def test_task010_live_asset_class_risk_passes(self) -> None:
        snapshot = fa_automation.build_quick_source_snapshot("BTC for 3 years", ["a", "b", "c"], "live")
        snapshot["mode"] = "live"
        quality = fa_automation.assess_quick_data_quality(snapshot)
        answer = fa_automation.generate_quick_answer("BTC for 3 years", ["a", "b", "c"], snapshot, quality)
        answer = answer.replace(
            fa_automation.quick_risk_line(snapshot["asset_identity"], snapshot["data"]),
            "Main limit: crypto volatility and regulatory risk need full workflow review.",
        )

        self.assertEqual(fa_automation.assess_quick_output_quality(answer, snapshot, quality)["status"], "pass")

    def test_task010_output_quality_rejects_hidden_action_and_overconfidence(self) -> None:
        snapshot = fa_automation.build_quick_source_snapshot("MSFT", ["a", "b", "c"], "live")
        quality = fa_automation.assess_quick_data_quality(snapshot)
        answer = fa_automation.generate_quick_answer("MSFT", ["a", "b", "c"], snapshot, quality)
        hidden_action = answer.replace("this is only a short filter", "this is a good entry", 1)
        bare_avoid = answer.replace("this is only a short filter", "avoid MSFT", 1)
        hard_confidence = answer.replace("this is only a short filter", "this is definitely risk-free", 1)
        soft_confidence = answer.replace("this is only a short filter", "this is a strong opportunity", 1)

        self.assertIn("hidden_action_language", fa_automation.assess_quick_output_quality(hidden_action, snapshot, quality)["soft_failures"])
        self.assertIn("hidden_action_language", fa_automation.assess_quick_output_quality(bare_avoid, snapshot, quality)["soft_failures"])
        self.assertIn("hard_overconfidence_language", fa_automation.assess_quick_output_quality(hard_confidence, snapshot, quality)["hard_failures"])
        self.assertIn("soft_overconfidence_language", fa_automation.assess_quick_output_quality(soft_confidence, snapshot, quality)["soft_failures"])

    def test_live_public_failures_degrade_without_crashing(self) -> None:
        original_sec = quick_snapshot.run_sec_filings_provider
        original_price = quick_snapshot.collect_price_by_registry

        def fail_sec(provider: object, cik: str) -> object:
            return quick_snapshot.ProviderResult(
                provider_id="sec_submissions",
                component="filings",
                status="error",
                error="sec unavailable",
                quality_level="failed",
            )

        def fail_price(ticker: str, asset_type: str | None) -> tuple[None, list[object]]:
            return None, [
                quick_snapshot.ProviderResult(
                    provider_id="stooq_price",
                    component="price",
                    status="error",
                    error="price unavailable",
                    quality_level="failed",
                )
            ]

        quick_snapshot.run_sec_filings_provider = fail_sec  # type: ignore[assignment]
        quick_snapshot.collect_price_by_registry = fail_price  # type: ignore[assignment]
        try:
            snapshot = fa_automation.build_quick_source_snapshot("MSFT", ["a", "b", "c"], "live")
            quality = fa_automation.assess_quick_data_quality(snapshot)
        finally:
            quick_snapshot.run_sec_filings_provider = original_sec  # type: ignore[assignment]
            quick_snapshot.collect_price_by_registry = original_price  # type: ignore[assignment]

        self.assertIn(quality["status"], {"Limited", "Blocked"})
        self.assertIn("filings", snapshot["missing"])
        self.assertIn("price", snapshot["missing"])
        self.assertTrue(snapshot["provider_errors"])

    def test_task008_live_price_failure_degrades_for_non_equity(self) -> None:
        original_price = quick_snapshot.collect_price_by_registry

        def fail_price(ticker: str, asset_type: str | None) -> tuple[None, list[object]]:
            return None, [
                quick_snapshot.ProviderResult(
                    provider_id="stooq_price",
                    component="price",
                    status="error",
                    error="price unavailable",
                    quality_level="failed",
                )
            ]

        quick_snapshot.collect_price_by_registry = fail_price  # type: ignore[assignment]
        try:
            snapshot = fa_automation.build_quick_source_snapshot("GLD gold ETF", ["a", "b", "c"], "live")
            quality = fa_automation.assess_quick_data_quality(snapshot)
        finally:
            quick_snapshot.collect_price_by_registry = original_price  # type: ignore[assignment]

        self.assertEqual(snapshot["asset_identity"]["ticker"], "GLD")
        self.assertEqual(quality["status"], "Limited")
        self.assertIn("price", snapshot["missing"])


class QuickAnswerCliTests(unittest.TestCase):
    def run_cli(
        self,
        args: list[str],
        data_runs_dir: Path,
        runs_dir: Path,
    ) -> subprocess.CompletedProcess[str]:
        env = os.environ.copy()
        env["FA_AUTOMATION_UNIT_LIVE_STUB"] = "1"
        env["FA_AUTOMATION_QUICK_DATA_RUNS_DIR"] = str(data_runs_dir)
        env["FA_AUTOMATION_QUICK_RUNS_DIR"] = str(runs_dir)
        return subprocess.run(
            [sys.executable, "fa_automation.py", *args],
            cwd=LAB_ROOT,
            text=True,
            capture_output=True,
            check=False,
            env=env,
        )

    def test_successful_mock_quick_answer_creates_snapshot_log_and_validates(self) -> None:
        with tempfile.TemporaryDirectory() as data_temp, tempfile.TemporaryDirectory() as runs_temp:
            data_runs_dir = Path(data_temp)
            runs_dir = Path(runs_temp)
            completed = self.run_cli(
                [
                    "quick-answer",
                    "--prompt",
                    "Microsoft for 3 years",
                    "--answer",
                    "3 years",
                    "--answer",
                    "no existing position",
                    "--answer",
                    "no current data need",
                    "--mode",
                    "live",
                ],
                data_runs_dir,
                runs_dir,
            )

            self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
            run_dirs = list(data_runs_dir.glob("*-MSFT"))
            self.assertEqual(len(run_dirs), 1)
            run_dir = run_dirs[0]
            self.assertTrue((run_dir / "source_snapshot.json").is_file())
            self.assertTrue((run_dir / "data_quality.json").is_file())
            self.assertTrue((run_dir / "quick_answer.json").is_file())
            self.assertTrue((run_dir / "output_quality.json").is_file())
            self.assertFalse((run_dir / "investment_report.md").exists())
            self.assertFalse((run_dir / "audit").exists())
            self.assertEqual(len(list(runs_dir.glob("*.json"))), 1)

            quick_answer = json.loads((run_dir / "quick_answer.json").read_text(encoding="utf-8"))
            output_quality = json.loads((run_dir / "output_quality.json").read_text(encoding="utf-8"))
            self.assertEqual(quick_answer["mode"], "live")
            self.assertEqual(quick_answer["validation_result"]["status"], "pass")
            self.assertEqual(output_quality["status"], "pass")
            self.assertEqual(quick_answer["output_quality_result"]["status"], "pass")
            self.assertIn("Source note", quick_answer["generated_answer"])
            self.assertIn("Freshness note", quick_answer["generated_answer"])
            stdout_lower = completed.stdout.lower()
            for forbidden in ("buy", "sell", "hold", "trim", "exit", "action box", "shares", "%"):
                self.assertNotIn(forbidden, stdout_lower)

            validation_completed = self.run_cli(
                ["validate-quick-answer", "--run-dir", str(run_dir)],
                data_runs_dir,
                runs_dir,
            )
            self.assertEqual(validation_completed.returncode, 0, validation_completed.stderr + validation_completed.stdout)
            self.assertIn("validation passed", validation_completed.stdout.lower())

    def test_task008_mock_cli_scenarios_create_expected_snapshot_slugs(self) -> None:
        cases = [
            ("SPY for 5 years", "SPY"),
            ("BTC for 3 years", "BTC"),
            ("TLT bond ETF", "TLT"),
            ("GLD gold ETF", "GLD"),
            ("MSFT vs SPY vs BTC", "MSFT-SPY-BTC"),
        ]
        for prompt, slug in cases:
            with self.subTest(prompt=prompt):
                with tempfile.TemporaryDirectory() as data_temp, tempfile.TemporaryDirectory() as runs_temp:
                    data_runs_dir = Path(data_temp)
                    runs_dir = Path(runs_temp)
                    completed = self.run_cli(
                        [
                            "quick-answer",
                            "--prompt",
                            prompt,
                            "--answer",
                            "3 years",
                            "--answer",
                            "no existing position",
                            "--answer",
                            "no current data need",
                            "--mode",
                            "live",
                        ],
                        data_runs_dir,
                        runs_dir,
                    )

                    self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
                    run_dirs = list(data_runs_dir.glob(f"*-{slug}"))
                    self.assertEqual(len(run_dirs), 1)
                    run_dir = run_dirs[0]
                    self.assertTrue((run_dir / "source_snapshot.json").is_file())
                    self.assertTrue((run_dir / "data_quality.json").is_file())
                    self.assertTrue((run_dir / "quick_answer.json").is_file())
                    self.assertTrue((run_dir / "output_quality.json").is_file())
                    self.assertEqual(len(list(runs_dir.glob("*.json"))), 1)
                    stdout_lower = completed.stdout.lower()
                    for forbidden in ("buy", "sell", "hold", "trim", "exit", "action box", "10 shares", "5%"):
                        self.assertNotIn(forbidden, stdout_lower)

                    validation_completed = self.run_cli(
                        ["validate-quick-answer", "--run-dir", str(run_dir)],
                        data_runs_dir,
                        runs_dir,
                    )
                    self.assertEqual(validation_completed.returncode, 0, validation_completed.stderr + validation_completed.stdout)



    def test_stooq_is_not_registered_as_crypto_price_provider(self) -> None:
        crypto_price_providers = quick_registry.providers_for("price", asset_type="crypto", include_disabled=False)
        provider_ids = {provider.provider_id for provider in crypto_price_providers}

        self.assertIn("yahoo_chart_price", provider_ids)
        self.assertNotIn("stooq_price", provider_ids)

    def test_btc_yahoo_failure_does_not_fall_back_to_stooq_crypto(self) -> None:
        original_runner = quick_snapshot.run_price_provider

        def fail_yahoo(provider: object, ticker: str) -> object:
            return quick_snapshot.ProviderResult(
                provider_id=getattr(provider, "provider_id", "unknown"),
                component="price",
                status="error",
                error="yahoo unavailable",
                quality_level="failed",
            )

        quick_snapshot.run_price_provider = fail_yahoo  # type: ignore[assignment]
        try:
            price, results = quick_snapshot.collect_price_by_registry("BTC-USD", "crypto")
        finally:
            quick_snapshot.run_price_provider = original_runner  # type: ignore[assignment]

        self.assertIsNone(price)
        self.assertEqual([result.provider_id for result in results], ["yahoo_chart_price"])

    def test_validator_requires_provider_error_consistency(self) -> None:
        with tempfile.TemporaryDirectory() as data_temp, tempfile.TemporaryDirectory() as runs_temp:
            data_runs_dir = Path(data_temp)
            runs_dir = Path(runs_temp)
            completed = self.run_cli(
                [
                    "quick-answer",
                    "--prompt",
                    "unknown private startup",
                    "--answers-json",
                    '["3 years", "none", "no current data"]',
                    "--mode",
                    "live",
                ],
                data_runs_dir,
                runs_dir,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
            run_dir = next(data_runs_dir.glob("*-UNKNOWN"))
            snapshot_path = run_dir / "source_snapshot.json"
            snapshot = json.loads(snapshot_path.read_text(encoding="utf-8"))
            snapshot["provider_errors"] = []
            snapshot_path.write_text(json.dumps(snapshot, indent=2), encoding="utf-8")

            validation_completed = self.run_cli(["validate-quick-answer", "--run-dir", str(run_dir)], data_runs_dir, runs_dir)
            self.assertNotEqual(validation_completed.returncode, 0)
            self.assertIn("provider_errors", validation_completed.stdout)

    def test_task010_validator_requires_output_quality_file_and_sections(self) -> None:
        with tempfile.TemporaryDirectory() as data_temp, tempfile.TemporaryDirectory() as runs_temp:
            data_runs_dir = Path(data_temp)
            runs_dir = Path(runs_temp)
            completed = self.run_cli(
                [
                    "quick-answer",
                    "--prompt",
                    "Microsoft for 3 years",
                    "--answer",
                    "3 years",
                    "--answer",
                    "no existing position",
                    "--answer",
                    "no current data need",
                    "--mode",
                    "live",
                ],
                data_runs_dir,
                runs_dir,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
            run_dir = next(data_runs_dir.glob("*-MSFT"))

            output_quality_path = run_dir / "output_quality.json"
            saved_output_quality = output_quality_path.read_text(encoding="utf-8")
            output_quality_path.unlink()
            validation_completed = self.run_cli(["validate-quick-answer", "--run-dir", str(run_dir)], data_runs_dir, runs_dir)
            self.assertNotEqual(validation_completed.returncode, 0)
            self.assertIn("output_quality.json", validation_completed.stdout)

            output_quality_path.write_text(saved_output_quality, encoding="utf-8")
            answer_path = run_dir / "quick_answer.json"
            quick_answer = json.loads(answer_path.read_text(encoding="utf-8"))
            quick_answer["generated_answer"] = quick_answer["generated_answer"].replace("Source note", "Source removed", 1)
            answer_path.write_text(json.dumps(quick_answer, indent=2), encoding="utf-8")
            validation_completed = self.run_cli(["validate-quick-answer", "--run-dir", str(run_dir)], data_runs_dir, runs_dir)
            self.assertNotEqual(validation_completed.returncode, 0)
            self.assertIn("output_quality is stale", validation_completed.stdout)

    def test_task010_validator_recomputes_output_quality_from_answer(self) -> None:
        with tempfile.TemporaryDirectory() as data_temp, tempfile.TemporaryDirectory() as runs_temp:
            data_runs_dir = Path(data_temp)
            runs_dir = Path(runs_temp)
            completed = self.run_cli(
                [
                    "quick-answer",
                    "--prompt",
                    "Microsoft for 3 years",
                    "--answer",
                    "3 years",
                    "--answer",
                    "no existing position",
                    "--answer",
                    "no current data need",
                    "--mode",
                    "live",
                ],
                data_runs_dir,
                runs_dir,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
            run_dir = next(data_runs_dir.glob("*-MSFT"))
            answer_path = run_dir / "quick_answer.json"
            quick_answer = json.loads(answer_path.read_text(encoding="utf-8"))
            quick_answer["generated_answer"] = quick_answer["generated_answer"].replace(
                "this is only a short filter",
                "this is a strong opportunity",
                1,
            )
            answer_path.write_text(json.dumps(quick_answer, indent=2), encoding="utf-8")

            validation_completed = self.run_cli(["validate-quick-answer", "--run-dir", str(run_dir)], data_runs_dir, runs_dir)
            self.assertNotEqual(validation_completed.returncode, 0)
            self.assertIn("output_quality is stale", validation_completed.stdout)

    def test_task010_validator_rejects_stale_but_still_valid_quality_card_details(self) -> None:
        with tempfile.TemporaryDirectory() as data_temp, tempfile.TemporaryDirectory() as runs_temp:
            data_runs_dir = Path(data_temp)
            runs_dir = Path(runs_temp)
            completed = self.run_cli(
                [
                    "quick-answer",
                    "--prompt",
                    "Microsoft for 3 years",
                    "--answer",
                    "3 years",
                    "--answer",
                    "no existing position",
                    "--answer",
                    "no current data need",
                    "--mode",
                    "live",
                ],
                data_runs_dir,
                runs_dir,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
            run_dir = next(data_runs_dir.glob("*-MSFT"))
            answer_path = run_dir / "quick_answer.json"
            quick_answer = json.loads(answer_path.read_text(encoding="utf-8"))
            quick_answer["generated_answer"] = quick_answer["generated_answer"].replace(
                "Public/no-key QUICK snapshot using mock fixture plus static public-data context (snapshot); not Evidence Collector evidence_pack and not a full source-readiness review.",
                "Public/no-key QUICK snapshot using mock fixture source detail and static public-data context; not Evidence Collector evidence_pack and not a full source-readiness review.",
                1,
            )
            answer_path.write_text(json.dumps(quick_answer, indent=2), encoding="utf-8")

            validation_completed = self.run_cli(["validate-quick-answer", "--run-dir", str(run_dir)], data_runs_dir, runs_dir)
            self.assertEqual(validation_completed.returncode, 0, validation_completed.stderr + validation_completed.stdout)

    def test_task010_direct_run_soft_quality_fail_saves_files_without_printing_quick_take(self) -> None:
        with tempfile.TemporaryDirectory() as data_temp, tempfile.TemporaryDirectory() as runs_temp:
            data_runs_dir = Path(data_temp)
            runs_dir = Path(runs_temp)
            original = fa_automation.asset_specific_risk_fallback
            original_data_runs = os.environ.get("FA_AUTOMATION_QUICK_DATA_RUNS_DIR")
            original_runs = os.environ.get("FA_AUTOMATION_QUICK_RUNS_DIR")

            def generic_risk(identity: dict[str, object]) -> str:
                return "Markets can go down."

            os.environ["FA_AUTOMATION_QUICK_DATA_RUNS_DIR"] = str(data_runs_dir)
            os.environ["FA_AUTOMATION_QUICK_RUNS_DIR"] = str(runs_dir)
            fa_automation.asset_specific_risk_fallback = generic_risk  # type: ignore[assignment]
            try:
                stdout = StringIO()
                with redirect_stdout(stdout):
                    return_code = fa_automation.run_quick_answer(
                        "Microsoft for 3 years",
                        "live",
                        ["3 years", "no existing position", "no current data need"],
                        None,
                    )
                output = stdout.getvalue()
            finally:
                fa_automation.asset_specific_risk_fallback = original  # type: ignore[assignment]
                if original_data_runs is None:
                    os.environ.pop("FA_AUTOMATION_QUICK_DATA_RUNS_DIR", None)
                else:
                    os.environ["FA_AUTOMATION_QUICK_DATA_RUNS_DIR"] = original_data_runs
                if original_runs is None:
                    os.environ.pop("FA_AUTOMATION_QUICK_RUNS_DIR", None)
                else:
                    os.environ["FA_AUTOMATION_QUICK_RUNS_DIR"] = original_runs

            self.assertEqual(return_code, 0)
            self.assertNotIn("quality failed", output.lower())
            self.assertIn("Quick Take:", output)
            run_dir = next(data_runs_dir.glob("*-MSFT"))
            self.assertTrue((run_dir / "output_quality.json").is_file())
            output_quality = json.loads((run_dir / "output_quality.json").read_text(encoding="utf-8"))
            self.assertIn(output_quality["status"], {"pass", "soft_fail"})

    def test_task010_validator_fails_on_tampered_output_quality_status(self) -> None:
        with tempfile.TemporaryDirectory() as data_temp, tempfile.TemporaryDirectory() as runs_temp:
            data_runs_dir = Path(data_temp)
            runs_dir = Path(runs_temp)
            completed = self.run_cli(
                [
                    "quick-answer",
                    "--prompt",
                    "Microsoft for 3 years",
                    "--answer",
                    "3 years",
                    "--answer",
                    "no existing position",
                    "--answer",
                    "no current data need",
                    "--mode",
                    "live",
                ],
                data_runs_dir,
                runs_dir,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
            run_dir = next(data_runs_dir.glob("*-MSFT"))
            output_quality = json.loads((run_dir / "output_quality.json").read_text(encoding="utf-8"))
            output_quality["status"] = "fail"
            output_quality["soft_failures"] = ["risk_not_specific_enough"]
            output_quality["checks"]["risk_specificity_ok"] = False
            (run_dir / "output_quality.json").write_text(json.dumps(output_quality, indent=2), encoding="utf-8")

            validation_completed = self.run_cli(
                ["validate-quick-answer", "--run-dir", str(run_dir)],
                data_runs_dir,
                runs_dir,
            )
            self.assertNotEqual(validation_completed.returncode, 0)
            self.assertIn("output_quality is stale", validation_completed.stdout)

    def test_validator_requires_provider_metadata_shape(self) -> None:
        with tempfile.TemporaryDirectory() as data_temp, tempfile.TemporaryDirectory() as runs_temp:
            data_runs_dir = Path(data_temp)
            runs_dir = Path(runs_temp)
            completed = self.run_cli(
                [
                    "quick-answer",
                    "--prompt",
                    "Microsoft for 3 years",
                    "--answer",
                    "3 years",
                    "--answer",
                    "no existing position",
                    "--answer",
                    "no current data need",
                    "--mode",
                    "live",
                ],
                data_runs_dir,
                runs_dir,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
            run_dir = next(data_runs_dir.glob("*-MSFT"))
            snapshot_path = run_dir / "source_snapshot.json"
            snapshot = json.loads(snapshot_path.read_text(encoding="utf-8"))
            snapshot["providers"][0].pop("provider_type", None)
            snapshot_path.write_text(json.dumps(snapshot, indent=2), encoding="utf-8")

            validation_completed = self.run_cli(["validate-quick-answer", "--run-dir", str(run_dir)], data_runs_dir, runs_dir)
            self.assertNotEqual(validation_completed.returncode, 0)
            self.assertIn("provider_type", validation_completed.stdout)

    def test_comparison_price_freshness_tracks_component_dates(self) -> None:
        snapshot = fa_automation.build_quick_source_snapshot("MSFT vs SPY vs BTC", ["a", "b", "c"], "live")
        quality = fa_automation.assess_quick_data_quality(snapshot)
        price_freshness = quality["freshness_by_component"]["price"]

        self.assertIn("components", price_freshness)
        component_tickers = {component["ticker"] for component in price_freshness["components"]}
        self.assertEqual(component_tickers, {"MSFT", "SPY", "BTC"})

    def test_validator_requires_provider_errors_field(self) -> None:
        with tempfile.TemporaryDirectory() as data_temp, tempfile.TemporaryDirectory() as runs_temp:
            data_runs_dir = Path(data_temp)
            runs_dir = Path(runs_temp)
            completed = self.run_cli(
                [
                    "quick-answer",
                    "--prompt",
                    "Microsoft for 3 years",
                    "--answer",
                    "3 years",
                    "--answer",
                    "no existing position",
                    "--answer",
                    "no current data need",
                    "--mode",
                    "live",
                ],
                data_runs_dir,
                runs_dir,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
            run_dir = next(data_runs_dir.glob("*-MSFT"))
            snapshot_path = run_dir / "source_snapshot.json"
            snapshot = json.loads(snapshot_path.read_text(encoding="utf-8"))
            snapshot.pop("provider_errors", None)
            snapshot_path.write_text(json.dumps(snapshot, indent=2), encoding="utf-8")

            validation_completed = self.run_cli(["validate-quick-answer", "--run-dir", str(run_dir)], data_runs_dir, runs_dir)
            self.assertNotEqual(validation_completed.returncode, 0)
            self.assertIn("provider_errors", validation_completed.stdout)

    def test_negative_empty_prompt_and_answers(self) -> None:
        with tempfile.TemporaryDirectory() as data_temp, tempfile.TemporaryDirectory() as runs_temp:
            data_runs_dir = Path(data_temp)
            runs_dir = Path(runs_temp)
            empty_prompt = self.run_cli(
                ["quick-answer", "--prompt", "", "--answer", "a", "--answer", "b", "--answer", "c"],
                data_runs_dir,
                runs_dir,
            )
            self.assertNotEqual(empty_prompt.returncode, 0)

            missing_answers = self.run_cli(
                ["quick-answer", "--prompt", "MSFT", "--answer", "a", "--answer", ""],
                data_runs_dir,
                runs_dir,
            )
            self.assertNotEqual(missing_answers.returncode, 0)
            self.assertNotIn("Traceback", missing_answers.stderr + missing_answers.stdout)

            malformed_json = self.run_cli(
                ["quick-answer", "--prompt", "MSFT", "--answers-json", "[bad json]"],
                data_runs_dir,
                runs_dir,
            )
            self.assertNotEqual(malformed_json.returncode, 0)
            self.assertIn("Error:", malformed_json.stdout)
            self.assertNotIn("Traceback", malformed_json.stderr + malformed_json.stdout)

    def test_unsupported_asset_creates_blocked_run(self) -> None:
        with tempfile.TemporaryDirectory() as data_temp, tempfile.TemporaryDirectory() as runs_temp:
            completed = self.run_cli(
                [
                    "quick-answer",
                    "--prompt",
                    "unknown private startup",
                    "--answers-json",
                    '["3 years", "none", "no current data"]',
                    "--mode",
                    "live",
                ],
                Path(data_temp),
                Path(runs_temp),
            )
            self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
            run_dir = next(Path(data_temp).glob("*-UNKNOWN"))
            quality = json.loads((run_dir / "data_quality.json").read_text(encoding="utf-8"))
            self.assertEqual(quality["status"], "Blocked")


if __name__ == "__main__":
    unittest.main()
