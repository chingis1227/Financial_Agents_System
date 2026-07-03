from __future__ import annotations

import re
import unittest
from pathlib import Path

LAB_ROOT = Path(__file__).resolve().parents[1]
DATA_SOURCES = LAB_ROOT / "data_sources"

EXPECTED_FILES = [
    "equity.md",
    "crypto.md",
    "etf.md",
    "fixed_income.md",
    "commodity.md",
    "macro.md",
    "news.md",
]

REQUIRED_FIELD_LABELS = [
    "What it provides",
    "Freshness",
    "Free/paid",
    "Automatable",
    "Fallback if unavailable",
]


class DataSourceMapTests(unittest.TestCase):
    def test_expected_data_source_files_exist(self) -> None:
        for file_name in EXPECTED_FILES:
            with self.subTest(file_name=file_name):
                self.assertTrue((DATA_SOURCES / file_name).is_file())

    def test_each_source_block_has_required_bullet_fields(self) -> None:
        for file_name in EXPECTED_FILES:
            text = (DATA_SOURCES / file_name).read_text(encoding="utf-8")
            source_blocks = re.split(r"(?m)^## Source: ", text)[1:]
            with self.subTest(file_name=file_name, check="has source blocks"):
                self.assertGreaterEqual(len(source_blocks), 1)

            for index, block in enumerate(source_blocks, start=1):
                for label in REQUIRED_FIELD_LABELS:
                    with self.subTest(file_name=file_name, source_block=index, label=label):
                        self.assertRegex(block, rf"(?m)^- {re.escape(label)}:")

    def test_readme_states_non_canonical_boundary(self) -> None:
        text = (DATA_SOURCES / "README.md").read_text(encoding="utf-8")
        self.assertIn("Financial Agent System remains the source of truth", text)
        self.assertIn("do not redefine source authority", text)

    def test_markdown_has_no_literal_newline_escape_artifacts(self) -> None:
        markdown_files = [LAB_ROOT / "README.md", LAB_ROOT / "ROADMAP.md", *DATA_SOURCES.glob("*.md")]
        for path in markdown_files:
            with self.subTest(path=path.name):
                text = path.read_text(encoding="utf-8")
                self.assertNotIn("`r`n", text)
                self.assertNotIn("``r``n", text)

    def test_no_authority_ranking_section_in_draft_maps(self) -> None:
        for path in DATA_SOURCES.glob("*.md"):
            with self.subTest(path=path.name):
                text = path.read_text(encoding="utf-8").lower()
                self.assertNotIn("## authority ranking", text)


if __name__ == "__main__":
    unittest.main()
