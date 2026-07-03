from __future__ import annotations

import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

try:
    from data_parsers.cftc_cot_parser import parse_cot_csv
    from data_parsers.issuer_etf_parser import parse_ishares_holdings_csv
    from data_parsers.usda_wasde_parser import parse_wasde_text
    from data_providers import ProviderRegistry, validate_provider_result
    from data_providers.base import VALID_ACCESS_STATUSES
    from data_providers.cache import DataRunStorage
    from data_providers.fred_provider import FREDProvider
    from data_providers.public_price_provider import PublicPriceProvider
    from data_providers.search_discovery_provider import SearchDiscoveryProvider
    from data_providers.usda_wasde_provider import USDAWASDEProvider
except ImportError:  # pragma: no cover
    from automation_lab.data_parsers.cftc_cot_parser import parse_cot_csv
    from automation_lab.data_parsers.issuer_etf_parser import parse_ishares_holdings_csv
    from automation_lab.data_parsers.usda_wasde_parser import parse_wasde_text
    from automation_lab.data_providers import ProviderRegistry, validate_provider_result
    from automation_lab.data_providers.base import VALID_ACCESS_STATUSES
    from automation_lab.data_providers.cache import DataRunStorage
    from automation_lab.data_providers.fred_provider import FREDProvider
    from automation_lab.data_providers.public_price_provider import PublicPriceProvider
    from automation_lab.data_providers.search_discovery_provider import SearchDiscoveryProvider
    from automation_lab.data_providers.usda_wasde_provider import USDAWASDEProvider


class DataProviderContractTests(unittest.TestCase):
    def test_route_registry_returns_valid_provider_results_without_network(self) -> None:
        registry = ProviderRegistry()
        output = registry.run(
            query={"subject": "TLT", "ticker": "TLT", "asset_class": "fixed_income"},
            route="fixed_income_full_cycle",
            allow_network=False,
            persist=False,
        )
        provider_ids = {result["provider_id"] for result in output["provider_results"]}
        self.assertTrue({"etf_issuer_provider", "treasury_provider", "fred_provider", "public_price_provider"}.issubset(provider_ids))
        for result in output["provider_results"]:
            validate_provider_result(result)
            self.assertRegex(result["retrieved_at"], r"(Z|[+-]\d{2}:\d{2})$")

    def test_cache_persists_raw_normalized_and_run_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            storage = DataRunStorage(tmp, subject="MSFT", persist=True)
            raw_path = storage.save_raw_json("sample", {"ticker": "MSFT"}, {"ok": True}, url="fixture://sample")
            normalized_path = storage.save_normalized("sample", {"ticker": "MSFT"}, {"rows": []}, url="fixture://sample")
            artifacts = storage.write_run_artifacts([])
            self.assertTrue(Path(raw_path or "").is_file())
            self.assertTrue(Path(normalized_path or "").is_file())
            self.assertTrue(Path(artifacts["provider_results"] or "").is_file())

    def test_disabled_keyed_provider_degrades_without_crash(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            result = FREDProvider().fetch({"subject": "rates", "asset_class": "macro"}, allow_network=False).to_dict()
        self.assertEqual(result["status"], "disabled")
        self.assertIn("FRED_API_KEY", " ".join(result["limitations"]))

    def test_public_price_fixture_path_is_ok_and_valid_contract(self) -> None:
        result = PublicPriceProvider().fetch(
            {
                "subject": "MSFT",
                "ticker": "MSFT",
                "asset_class": "equity",
                "price_data": {"ticker": "MSFT", "latest": {"date": "2026-07-02", "close": 500.0}, "history": []},
            },
            allow_network=False,
        ).to_dict()
        validate_provider_result(result)
        self.assertEqual(result["status"], "ok")
        self.assertEqual(result["source_tier"], "Tier 2")

    def test_search_discovery_is_pointer_only_and_has_no_material_claims(self) -> None:
        result = SearchDiscoveryProvider().fetch(
            {"subject": "TLT", "asset_class": "fixed_income", "results": [{"title": "Issuer", "url": "https://example.com"}]},
            allow_network=False,
        ).to_dict()
        self.assertEqual(result["source_tier"], "Pointer-Only")
        self.assertFalse(result["claims"])
        self.assertFalse(result["metadata"]["claim_support_allowed"])

    def test_nested_claim_validation_rejects_material_supported_claim_without_source(self) -> None:
        bad = PublicPriceProvider().fetch(
            {
                "subject": "MSFT",
                "ticker": "MSFT",
                "asset_class": "equity",
                "price_data": {"ticker": "MSFT", "latest": {"date": "2026-07-02", "close": 500.0}, "history": []},
            },
            allow_network=False,
        ).to_dict()
        bad["claims"][0]["source"] = ""
        with self.assertRaises(ValueError):
            validate_provider_result(bad)

    def test_provider_access_status_contract_matches_goal(self) -> None:
        self.assertEqual(VALID_ACCESS_STATUSES, {"Available", "Partial", "Inaccessible", "Not Found", "Restricted"})


class DataParserTests(unittest.TestCase):
    def test_cftc_cot_parser_normalizes_net_managed_money(self) -> None:
        text = (
            "Market_and_Exchange_Names,Report_Date_as_YYYY-MM-DD,Open_Interest_All,"
            "M_Money_Positions_Long_All,M_Money_Positions_Short_All\n"
            "CORN - CHICAGO BOARD OF TRADE,2026-06-30,100000,35000,20000\n"
        )
        rows = parse_cot_csv(text, market_filter="corn")
        self.assertEqual(rows[0]["managed_money_long"], 35000)
        self.assertEqual(rows[0]["managed_money_short"], 20000)
        self.assertEqual(rows[0]["net_managed_money"], 15000)

    def test_wasde_parser_extracts_key_grain_metric_or_provider_is_partial(self) -> None:
        rows = parse_wasde_text("Corn production 15,000\nCorn exports 2,200\nCorn ending stocks 1,700")
        self.assertGreaterEqual(len(rows), 3)
        partial = USDAWASDEProvider().fetch({"subject": "corn", "asset_class": "grains", "text": "unparseable report"}, allow_network=False).to_dict()
        self.assertEqual(partial["status"], "partial")
        self.assertTrue(partial["limitations"])

    def test_wasde_supported_claim_without_source_date_carries_limitation(self) -> None:
        result = USDAWASDEProvider().fetch(
            {"subject": "corn", "asset_class": "grains", "text": "Corn production 15,000"},
            allow_network=False,
        ).to_dict()
        validate_provider_result(result)
        self.assertEqual(result["status"], "ok")
        self.assertEqual(result["claims"][0]["freshness"], "Unknown")
        self.assertIn("source/report date", result["claims"][0]["limitation"])

    def test_ishares_holdings_parser_reads_sample_holdings(self) -> None:
        csv_text = "Ticker,Name,Weight (%),Market Value,Maturity,Coupon,As Of\nT 4.5,US Treasury Bond,12.5,1000000,2045-02-15,4.5,2026-07-01\n"
        parsed = parse_ishares_holdings_csv(csv_text, ticker="TLT")
        self.assertEqual(parsed["holding_count"], 1)
        self.assertEqual(parsed["holdings"][0]["name"], "US Treasury Bond")


class DataProviderIntegrationTests(unittest.TestCase):
    def test_quick_snapshot_contains_provider_plan(self) -> None:
        try:
            from quick_data.snapshot import build_quick_source_snapshot
        except ImportError:  # pragma: no cover
            from automation_lab.quick_data.snapshot import build_quick_source_snapshot

        snapshot = build_quick_source_snapshot("QUICK: Microsoft", ["3-5 years", "no position", "latest price"], "live")
        self.assertTrue(snapshot["data_provider_plan"])

    def test_agent_tlt_preflight_attempts_fixed_income_provider_set(self) -> None:
        lab_root = Path(__file__).resolve().parents[1]
        if str(lab_root) not in sys.path:
            sys.path.insert(0, str(lab_root))
        from fa_automation import AGENT_NON_EQUITY_IDENTITIES, build_agent_source_preflight

        identity = dict(AGENT_NON_EQUITY_IDENTITIES["TLT"])
        preflight = build_agent_source_preflight("AGENT: TLT", ["a", "b", "c", "d", "e"], "live", "fixed_income_full_cycle", identity)
        provider_ids = {result["provider_id"] for result in preflight["data_provider_results"]}
        self.assertTrue({"etf_issuer_provider", "treasury_provider", "fred_provider", "public_price_provider"}.issubset(provider_ids))

    def test_multi_asset_provider_registry_fans_out_by_component(self) -> None:
        try:
            from fa_automation import resolve_agent_request
        except ImportError:  # pragma: no cover
            from automation_lab.fa_automation import resolve_agent_request
        try:
            from data_providers import run_provider_registry_for_preflight
        except ImportError:  # pragma: no cover
            from automation_lab.data_providers import run_provider_registry_for_preflight

        identity = resolve_agent_request("AGENT: MSFT vs TLT vs BTC", mode="live")
        output = run_provider_registry_for_preflight(route="multi_asset_comparison", identity=identity, mode="live")
        components = {
            result.get("metadata", {}).get("comparison_component", {}).get("ticker")
            for result in output.get("provider_results", [])
        }
        self.assertTrue({"MSFT", "TLT", "BTC"}.issubset(components))
        self.assertEqual(output.get("evidence_parity", {}).get("status"), "Complete")

    def test_behavior_fixtures_have_no_mojibake_question_marks(self) -> None:
        root = Path(__file__).resolve().parents[2]
        for rel in ("tests/behavior/golden_prompts.yaml", "tests/behavior/routing_cases.yaml"):
            text = (root / rel).read_text(encoding="utf-8")
            self.assertNotIn("????", text, rel)


if __name__ == "__main__":
    unittest.main()
