"""PDF parsing utilities for the Evidence Document Parser layer."""

from __future__ import annotations

from io import BytesIO
from pathlib import Path
from typing import Any, BinaryIO

from .source_fetchers import now_iso


PYPDF_MISSING_MESSAGE = "PDF parser unavailable: pypdf not installed"


def _reader_from_stream(stream: BinaryIO):
    try:
        from pypdf import PdfReader  # type: ignore
    except Exception as exc:  # pragma: no cover - exact import failure is environment-specific
        raise ImportError(PYPDF_MISSING_MESSAGE) from exc
    return PdfReader(stream)


def parse_pdf_stream(
    stream: BinaryIO,
    *,
    source_url: str | None = None,
    local_path: str | None = None,
) -> dict[str, Any]:
    """Extract page text from a PDF stream, preserving page numbers."""

    try:
        reader = _reader_from_stream(stream)
    except ImportError as exc:
        return {
            "source": {
                "url": source_url,
                "local_path": local_path,
                "title": Path(local_path).name if local_path else source_url,
                "publisher": None,
                "published_at": None,
                "retrieved_at": now_iso(),
                "document_type": "pdf",
                "access_status": "Unsupported",
            },
            "text_blocks": [],
            "tables": [],
            "warnings": [str(exc)],
        }

    text_blocks: list[dict[str, Any]] = []
    warnings: list[str] = []
    for index, page in enumerate(reader.pages, start=1):
        try:
            text = page.extract_text() or ""
        except Exception as exc:  # pragma: no cover - corrupt PDFs vary by parser version
            warnings.append(f"Page {index} text extraction failed: {exc}")
            text = ""
        if text.strip():
            text_blocks.append(
                {
                    "text": text.strip(),
                    "page": index,
                    "section": f"Page {index}",
                    "location_hint": f"page {index}",
                }
            )
    access_status = "Available" if text_blocks else "Unsupported"
    if not text_blocks:
        warnings.append("PDF appears scanned/image-only or has no extractable text")
    return {
        "source": {
            "url": source_url,
            "local_path": local_path,
            "title": Path(local_path).name if local_path else source_url,
            "publisher": None,
            "published_at": None,
            "retrieved_at": now_iso(),
            "document_type": "pdf",
            "access_status": access_status,
        },
        "text_blocks": text_blocks,
        "tables": [],
        "warnings": warnings,
    }


def parse_pdf_bytes(
    payload: bytes,
    *,
    source_url: str | None = None,
    local_path: str | None = None,
) -> dict[str, Any]:
    return parse_pdf_stream(BytesIO(payload), source_url=source_url, local_path=local_path)


def parse_pdf_file(path: str | Path) -> dict[str, Any]:
    pdf_path = Path(path)
    with pdf_path.open("rb") as stream:
        return parse_pdf_stream(stream, local_path=str(pdf_path))
