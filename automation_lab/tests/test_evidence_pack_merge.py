from __future__ import annotations

import unittest
import sys
from pathlib import Path

LAB_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LAB_ROOT))

from agent_data.document_parser import parse_document
from agent_data.evidence_pack_merge import merge_parsed_document_into_evidence_pack


FIXTURES = Path(__file__).resolve().parent / "fixtures" / "parser"


class EvidencePackMergeTests(unittest.TestCase):
    def base_pack(self) -> dict:
        return {
            "schema_version": "agent_evidence_pack.v1",
            "claim_support_matrix": [],
            "conflict_register": [],
            "missing_weak_evidence_register": [],
        }

    def test_merge_adds_claim_level_rows_and_source_inventory(self) -> None:
        parsed = parse_document(str(FIXTURES / "sample_earnings_release.txt"), source_tier="Tier 1", company="ExampleCo")
        pack = merge_parsed_document_into_evidence_pack(self.base_pack(), parsed)

        self.assertTrue(pack["source_inventory"])
        self.assertTrue(pack["claim_support_matrix"])
        row = pack["claim_support_matrix"][0]
        self.assertIn("location", row)
        self.assertEqual(row["access"], "Available")
        self.assertEqual(row["source_tier"], "Tier 1")

    def test_conflicting_values_for_same_metric_period_create_register_entry(self) -> None:
        pack = self.base_pack()
        parsed_a = parse_document(str(FIXTURES / "sample_conflicting_values_a.txt"), source_tier="Tier 1")
        parsed_b = parse_document(str(FIXTURES / "sample_conflicting_values_b.txt"), source_tier="Tier 1")
        merge_parsed_document_into_evidence_pack(pack, parsed_a)
        merge_parsed_document_into_evidence_pack(pack, parsed_b)

        self.assertTrue(pack["conflict_register"])
        self.assertEqual(pack["conflict_register"][0]["current_treatment"], "Contradicted")

    def test_missing_financial_claims_create_missing_weak_row(self) -> None:
        parsed = parse_document(str(FIXTURES / "sample_no_financial_data.html"), source_tier="Tier 3")
        pack = merge_parsed_document_into_evidence_pack(self.base_pack(), parsed)

        self.assertTrue(pack["missing_weak_evidence_register"])
        self.assertEqual(pack["missing_weak_evidence_register"][0]["observed_status"], "Not Found")


if __name__ == "__main__":
    unittest.main()
