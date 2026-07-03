"""Graceful PDF table/text extraction wrapper."""

from __future__ import annotations

from pathlib import Path
from typing import Any


def parse_pdf_tables(path: str | Path) -> dict[str, Any]:
    try:
        from agent_data.pdf_parser import parse_pdf_file  # type: ignore
    except Exception as exc:  # pragma: no cover
        return {"status": "Unsupported", "tables": [], "text": "", "limitations": [f"PDF parser unavailable: {exc}"]}
    parsed = parse_pdf_file(path)
    text_blocks = parsed.get("text_blocks") or []
    return {
        "status": parsed.get("source", {}).get("access_status", "Partial"),
        "tables": [],
        "text": "\n".join(block.get("text", "") for block in text_blocks),
        "limitations": parsed.get("warnings") or ["Table structure is not preserved by the lightweight parser."],
    }
