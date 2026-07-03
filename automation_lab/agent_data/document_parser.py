"""Unified Evidence Document Parser entrypoint."""

from __future__ import annotations

import hashlib
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

from .article_parser import parse_html_content
from .financial_claim_extractor import extract_financial_claims
from .pdf_parser import parse_pdf_bytes, parse_pdf_file
from .source_fetchers import now_iso


USER_AGENT = "Financial Agent Evidence Document Parser contact: local@example.com"


def _source_id(value: str) -> str:
    return "doc_" + hashlib.sha1(value.encode("utf-8", errors="ignore")).hexdigest()[:12]


def _blank_result(
    *,
    source: str,
    document_type: str,
    access_status: str,
    warning: str,
    source_tier: str,
) -> dict[str, Any]:
    return {
        "schema_version": "document_parser_result.v1",
        "source": {
            "source_id": _source_id(source),
            "url": source if source.startswith(("http://", "https://")) else None,
            "local_path": source if not source.startswith(("http://", "https://")) else None,
            "title": None,
            "publisher": None,
            "published_at": None,
            "retrieved_at": now_iso(),
            "document_type": document_type,
            "access_status": access_status,
            "source_tier": source_tier,
        },
        "text_blocks": [],
        "tables": [],
        "extracted_claims": [],
        "warnings": [warning],
    }


def _fetch_url(url: str, timeout: int = 20) -> tuple[bytes, str | None]:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/html,application/pdf,text/plain,*/*"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read(), response.headers.get_content_type()


def _is_html_text(text: str) -> bool:
    lowered = text[:1000].lower()
    return "<html" in lowered or "<body" in lowered or "<table" in lowered or "</p>" in lowered


def _merge_source_metadata(parsed: dict[str, Any], *, source: str, source_tier: str, document_type: str | None = None) -> dict[str, Any]:
    source_meta = parsed.get("source", {})
    source_meta.setdefault("source_id", _source_id(source))
    if source.startswith(("http://", "https://")):
        source_meta.setdefault("url", source)
        source_meta.setdefault("local_path", None)
    else:
        source_meta.setdefault("local_path", source)
        source_meta.setdefault("url", None)
    if document_type:
        source_meta["document_type"] = document_type
    source_meta["source_tier"] = source_tier
    parsed["source"] = source_meta
    return parsed


def _finalize(
    parsed: dict[str, Any],
    *,
    source: str,
    source_tier: str,
    default_claim_type: str,
    company: str | None,
    document_type: str | None = None,
) -> dict[str, Any]:
    parsed = _merge_source_metadata(parsed, source=source, source_tier=source_tier, document_type=document_type)
    claims, claim_warnings = extract_financial_claims(
        parsed.get("text_blocks", []),
        source_tier=source_tier,
        default_claim_type=default_claim_type,
        company=company,
    )
    parsed["schema_version"] = "document_parser_result.v1"
    parsed["extracted_claims"] = claims
    warnings = list(parsed.get("warnings") or [])
    warnings.extend(claim_warnings)
    parsed["warnings"] = list(dict.fromkeys(warnings))
    return parsed


def parse_document(
    source: str,
    *,
    source_tier: str = "Tier 3",
    default_claim_type: str = "Reported Fact",
    publisher: str | None = None,
    company: str | None = None,
    timeout: int = 20,
) -> dict[str, Any]:
    """Parse URL, local file path, HTML content, PDF path, or raw text into structured evidence."""

    source_text = str(source)
    try:
        if source_text.startswith(("http://", "https://")):
            try:
                payload, content_type = _fetch_url(source_text, timeout=timeout)
            except (urllib.error.URLError, TimeoutError, ValueError) as exc:
                return _blank_result(
                    source=source_text,
                    document_type="unknown",
                    access_status="Inaccessible",
                    warning=f"Document URL inaccessible: {exc}",
                    source_tier=source_tier,
                )
            is_pdf = content_type == "application/pdf" or source_text.lower().split("?")[0].endswith(".pdf")
            if is_pdf:
                parsed = parse_pdf_bytes(payload, source_url=source_text)
                return _finalize(parsed, source=source_text, source_tier=source_tier, default_claim_type=default_claim_type, company=company, document_type="pdf")
            html = payload.decode("utf-8", errors="replace")
            parsed = parse_html_content(html, source_url=source_text, publisher=publisher)
            return _finalize(parsed, source=source_text, source_tier=source_tier, default_claim_type=default_claim_type, company=company)

        path = Path(source_text)
        if path.exists():
            if path.suffix.lower() == ".pdf":
                parsed = parse_pdf_file(path)
                return _finalize(parsed, source=str(path), source_tier=source_tier, default_claim_type=default_claim_type, company=company, document_type="pdf")
            text = path.read_text(encoding="utf-8", errors="replace")
            if path.suffix.lower() in {".html", ".htm"} or _is_html_text(text):
                parsed = parse_html_content(text, source_url=None, publisher=publisher)
                return _finalize(parsed, source=str(path), source_tier=source_tier, default_claim_type=default_claim_type, company=company)
            parsed = {
                "source": {
                    "title": path.name,
                    "publisher": publisher,
                    "published_at": None,
                    "retrieved_at": now_iso(),
                    "document_type": "raw_text",
                    "access_status": "Available",
                },
                "text_blocks": [{"text": text, "page": None, "section": "Raw text", "location_hint": str(path)}],
                "tables": [],
                "warnings": [],
            }
            return _finalize(parsed, source=str(path), source_tier=source_tier, default_claim_type=default_claim_type, company=company, document_type="raw_text")

        if _is_html_text(source_text):
            parsed = parse_html_content(source_text, source_url=None, publisher=publisher)
            return _finalize(parsed, source="inline_html", source_tier=source_tier, default_claim_type=default_claim_type, company=company)

        parsed = {
            "source": {
                "source_id": _source_id(source_text[:500]),
                "url": None,
                "local_path": None,
                "title": "raw text",
                "publisher": publisher,
                "published_at": None,
                "retrieved_at": now_iso(),
                "document_type": "raw_text",
                "access_status": "Available",
                "source_tier": source_tier,
            },
            "text_blocks": [{"text": source_text, "page": None, "section": "Raw text", "location_hint": "inline raw text"}],
            "tables": [],
            "warnings": [],
        }
        return _finalize(parsed, source=source_text[:500], source_tier=source_tier, default_claim_type=default_claim_type, company=company, document_type="raw_text")
    except Exception as exc:  # parser must be evidence-safe, not workflow-fatal
        return _blank_result(
            source=source_text[:500],
            document_type="unknown",
            access_status="Partial",
            warning=f"Document parser failed safely: {exc}",
            source_tier=source_tier,
        )
