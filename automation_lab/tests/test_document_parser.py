from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest import mock

LAB_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LAB_ROOT))

from agent_data.document_parser import parse_document
from agent_data.pdf_parser import parse_pdf_file


FIXTURES = Path(__file__).resolve().parent / "fixtures" / "parser"


def _write_minimal_text_pdf(path: Path, text: str) -> None:
    escaped = text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
    objects = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >>",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
    ]
    stream = f"BT /F1 12 Tf 72 720 Td ({escaped}) Tj ET".encode("latin-1")
    objects.append(b"<< /Length " + str(len(stream)).encode("ascii") + b" >>\nstream\n" + stream + b"\nendstream")
    payload = bytearray(b"%PDF-1.4\n")
    offsets = [0]
    for index, obj in enumerate(objects, start=1):
        offsets.append(len(payload))
        payload.extend(f"{index} 0 obj\n".encode("ascii"))
        payload.extend(obj)
        payload.extend(b"\nendobj\n")
    xref_offset = len(payload)
    payload.extend(f"xref\n0 {len(objects) + 1}\n".encode("ascii"))
    payload.extend(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        payload.extend(f"{offset:010d} 00000 n \n".encode("ascii"))
    payload.extend(
        (
            f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\n"
            f"startxref\n{xref_offset}\n%%EOF\n"
        ).encode("ascii")
    )
    path.write_bytes(bytes(payload))


class DocumentParserTests(unittest.TestCase):
    def test_html_parser_extracts_title_date_body_tables_and_numbers(self) -> None:
        result = parse_document(str(FIXTURES / "sample_earnings_release.html"), source_tier="Tier 1", company="ExampleCo")

        self.assertEqual(result["schema_version"], "document_parser_result.v1")
        self.assertEqual(result["source"]["title"], "ExampleCo Reports Q2 FY2026 Results")
        self.assertEqual(result["source"]["published_at"], "2026-07-01")
        self.assertEqual(result["source"]["document_type"], "html_article")
        self.assertTrue(result["text_blocks"])
        self.assertTrue(result["tables"])
        metrics = {claim["metric"] for claim in result["extracted_claims"]}
        self.assertIn("Revenue", metrics)
        self.assertIn("Adjusted EPS", metrics)
        self.assertIn("Gross margin", metrics)
        self.assertIn("Guidance", metrics)
        revenue = next(claim for claim in result["extracted_claims"] if claim["metric"] == "Revenue")
        growth = next(claim for claim in result["extracted_claims"] if claim["metric"] == "Growth")
        eps = next(claim for claim in result["extracted_claims"] if claim["metric"] == "Adjusted EPS")
        self.assertEqual(revenue["value"], 15.2)
        self.assertEqual(revenue["unit"], "USD billions")
        self.assertEqual(growth["value"], 18.0)
        self.assertEqual(growth["unit"], "percent")
        self.assertEqual(eps["value"], 2.31)
        self.assertEqual(eps["unit"], "USD per share")

    def test_raw_text_parser_extracts_financial_claims(self) -> None:
        result = parse_document(str(FIXTURES / "sample_earnings_release.txt"), source_tier="Tier 1", company="ExampleCo")

        self.assertEqual(result["source"]["document_type"], "raw_text")
        self.assertGreaterEqual(len(result["extracted_claims"]), 4)
        revenue = next(claim for claim in result["extracted_claims"] if claim["metric"] == "Revenue")
        self.assertEqual(revenue["value"], 15.2)
        self.assertEqual(revenue["unit"], "USD billions")

    def test_no_financial_data_returns_zero_claims_and_warning(self) -> None:
        result = parse_document(str(FIXTURES / "sample_no_financial_data.html"), source_tier="Tier 3")

        self.assertEqual(result["extracted_claims"], [])
        self.assertIn("No financial claims found", result["warnings"])

    def test_pdf_parser_extracts_text_with_page_number_when_pypdf_available(self) -> None:
        try:
            import pypdf  # type: ignore  # noqa: F401
        except Exception:
            self.skipTest("pypdf not installed")
        with self.subTest("generated_pdf"):
            pdf_path = FIXTURES / "generated_sample.pdf"
            _write_minimal_text_pdf(pdf_path, "Revenue was $1.0 billion in FY2026.")
            result = parse_pdf_file(pdf_path)
            self.assertEqual(result["source"]["document_type"], "pdf")
            self.assertEqual(result["source"]["access_status"], "Available")
            self.assertEqual(result["text_blocks"][0]["page"], 1)
            self.assertIn("Revenue was $1.0 billion", result["text_blocks"][0]["text"])
            pdf_path.unlink(missing_ok=True)

    def test_missing_pypdf_gives_graceful_unsupported_status(self) -> None:
        with mock.patch.dict(sys.modules, {"pypdf": None}):
            result = parse_pdf_file(FIXTURES / "sample_no_financial_data.html")

        self.assertEqual(result["source"]["access_status"], "Unsupported")
        self.assertIn("PDF parser unavailable: pypdf not installed", result["warnings"])


if __name__ == "__main__":
    unittest.main()
