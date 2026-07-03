from __future__ import annotations

import unittest
import sys
from pathlib import Path

LAB_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LAB_ROOT))

from agent_data.financial_claim_extractor import extract_financial_claims


class FinancialClaimExtractorTests(unittest.TestCase):
    def test_extracts_revenue_eps_margin_and_guidance(self) -> None:
        blocks = [
            {
                "text": (
                    "ExampleCo reported revenue of $15,200 million in Q2 FY2026. "
                    "Adjusted EPS was $2.31 in Q2 FY2026. "
                    "Gross margin was 64% in Q2 FY2026. "
                    "Management expects revenue guidance of $16.0 billion for Q3 FY2026."
                ),
                "page": None,
                "section": "Raw text",
            }
        ]
        claims, warnings = extract_financial_claims(blocks, source_tier="Tier 1", company="ExampleCo")
        metrics = {claim["metric"] for claim in claims}

        self.assertFalse(warnings)
        self.assertIn("Revenue", metrics)
        self.assertIn("Adjusted EPS", metrics)
        self.assertIn("Gross margin", metrics)
        self.assertIn("Guidance", metrics)
        revenue = next(claim for claim in claims if claim["metric"] == "Revenue")
        self.assertEqual(revenue["value"], 15.2)
        self.assertEqual(revenue["unit"], "USD billions")
        self.assertEqual(revenue["period"], "Q2 FY2026")
        guidance = next(claim for claim in claims if claim["metric"] == "Guidance")
        self.assertEqual(guidance["claim_type"], "Official Guidance")

    def test_revenue_and_yoy_growth_in_same_sentence_bind_to_correct_numbers(self) -> None:
        claims, warnings = extract_financial_claims(
            [{"text": "ExampleCo reported revenue of $15.2 billion in Q2 FY2026, up 18% YoY."}],
            source_tier="Tier 1",
        )
        self.assertFalse(warnings)
        revenue = next(claim for claim in claims if claim["metric"] == "Revenue")
        growth = next(claim for claim in claims if claim["metric"] == "Growth")
        self.assertEqual(revenue["value"], 15.2)
        self.assertEqual(revenue["unit"], "USD billions")
        self.assertEqual(growth["value"], 18.0)
        self.assertEqual(growth["unit"], "percent")

    def test_revenue_and_eps_in_same_sentence_bind_to_nearest_values(self) -> None:
        claims, warnings = extract_financial_claims(
            [{"text": "Revenue was $15.2 billion and adjusted EPS was $2.31 in Q2 FY2026."}],
            source_tier="Tier 1",
        )
        self.assertFalse(warnings)
        revenue = next(claim for claim in claims if claim["metric"] == "Revenue")
        eps = next(claim for claim in claims if claim["metric"] == "Adjusted EPS")
        self.assertEqual(revenue["value"], 15.2)
        self.assertEqual(revenue["unit"], "USD billions")
        self.assertEqual(eps["value"], 2.31)
        self.assertEqual(eps["unit"], "USD per share")
        self.assertNotIn("Adjusted/non-GAAP basis detected near metric in source text", revenue["limitations"])

    def test_revenue_guidance_sentence_can_support_both_metrics(self) -> None:
        claims, warnings = extract_financial_claims(
            [{"text": "Management expects revenue guidance of $16.0 billion for Q3 FY2026."}],
            source_tier="Tier 1",
        )
        self.assertFalse(warnings)
        revenue = next(claim for claim in claims if claim["metric"] == "Revenue")
        guidance = next(claim for claim in claims if claim["metric"] == "Guidance")
        self.assertEqual(revenue["value"], 16.0)
        self.assertEqual(guidance["value"], 16.0)
        self.assertEqual(guidance["claim_type"], "Official Guidance")

    def test_sentence_wide_non_gaap_preamble_marks_revenue_limitation(self) -> None:
        claims, warnings = extract_financial_claims(
            [{"text": "The following non-GAAP measures are presented for comparability: revenue was $15.2 billion in Q2 FY2026."}],
            source_tier="Tier 1",
        )
        self.assertFalse(warnings)
        revenue = next(claim for claim in claims if claim["metric"] == "Revenue")
        self.assertIn("Adjusted/non-GAAP basis applies to this metric in source text", revenue["limitations"])

    def test_non_gaap_basis_after_metric_or_value_marks_revenue_limitation(self) -> None:
        examples = [
            "Revenue was $15.2 billion in Q2 FY2026 on a non-GAAP basis.",
            "Revenue for Q2 FY2026, which management presents on a non-GAAP basis, was $15.2 billion.",
        ]
        for text in examples:
            with self.subTest(text=text):
                claims, warnings = extract_financial_claims([{"text": text}], source_tier="Tier 1")
                self.assertFalse(warnings)
                revenue = next(claim for claim in claims if claim["metric"] == "Revenue")
                self.assertIn("Adjusted/non-GAAP basis applies to this metric in source text", revenue["limitations"])

    def test_non_gaap_suffix_on_later_adjusted_eps_does_not_taint_revenue(self) -> None:
        claims, warnings = extract_financial_claims(
            [{"text": "Revenue was $15.2 billion in Q2 FY2026 and adjusted EPS was $2.31 on a non-GAAP basis."}],
            source_tier="Tier 1",
        )
        self.assertFalse(warnings)
        revenue = next(claim for claim in claims if claim["metric"] == "Revenue")
        eps = next(claim for claim in claims if claim["metric"] == "Adjusted EPS")
        self.assertFalse(revenue["limitations"])
        self.assertEqual(eps["value"], 2.31)

    def test_prior_adjusted_metric_non_gaap_suffix_does_not_taint_later_revenue(self) -> None:
        examples = [
            "Adjusted EPS was $2.31 on a non-GAAP basis and revenue was $15.2 billion in Q2 FY2026.",
            "Adjusted EBITDA was $4.0 billion on a non-GAAP basis and revenue was $15.2 billion in Q2 FY2026.",
        ]
        for text in examples:
            with self.subTest(text=text):
                claims, warnings = extract_financial_claims([{"text": text}], source_tier="Tier 1")
                self.assertFalse(warnings)
                revenue = next(claim for claim in claims if claim["metric"] == "Revenue")
                self.assertFalse(revenue["limitations"])

    def test_ambiguous_units_lower_confidence_and_add_limitation(self) -> None:
        claims, warnings = extract_financial_claims(
            [{"text": "Revenue was 15.2 billion.", "section": "Raw text"}],
            source_tier="Tier 3",
        )

        self.assertFalse(warnings)
        self.assertEqual(len(claims), 1)
        self.assertEqual(claims[0]["confidence"], "Low")
        self.assertIn("Unit or currency scale is ambiguous", claims[0]["limitations"])
        self.assertIn("Period not explicit near claim", claims[0]["limitations"])

    def test_no_financial_data_returns_warning_not_invented_claim(self) -> None:
        claims, warnings = extract_financial_claims([{"text": "The company hosted a community day."}])

        self.assertEqual(claims, [])
        self.assertIn("No financial claims found", warnings)

    def test_parser_does_not_emit_final_action_language(self) -> None:
        claims, warnings = extract_financial_claims(
            [{"text": "Revenue was $1.0 billion in FY2026."}],
            source_tier="Tier 1",
        )
        rendered = " ".join(str(item) for item in claims + warnings)
        forbidden = ["IC Action", "buy", "sell", "hold", "trim", "exit"]
        for token in forbidden:
            with self.subTest(token=token):
                self.assertNotIn(token, rendered)


if __name__ == "__main__":
    unittest.main()
