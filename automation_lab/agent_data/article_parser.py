"""HTML/article parsing utilities for the Evidence Document Parser layer."""

from __future__ import annotations

from html.parser import HTMLParser
from typing import Any

from .source_fetchers import now_iso


BOILERPLATE_TOKENS = {
    "accept cookies",
    "cookie preferences",
    "privacy policy",
    "subscribe",
    "sign up",
    "advertisement",
}


class _ArticleHTMLParser(HTMLParser):
    """Small stdlib-only HTML extractor for deterministic MVP parsing."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.title_parts: list[str] = []
        self.text_parts: list[str] = []
        self.current_table: list[list[str]] = []
        self.tables: list[dict[str, Any]] = []
        self.current_row: list[str] = []
        self.current_cell_parts: list[str] = []
        self.published_at: str | None = None
        self._tag_stack: list[str] = []
        self._skip_depth = 0
        self._in_title = False
        self._in_table = False
        self._in_row = False
        self._in_cell = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        self._tag_stack.append(tag)
        attrs_dict = {name.lower(): value or "" for name, value in attrs}
        if tag in {"script", "style", "noscript", "svg", "nav", "header", "footer", "form", "button"}:
            self._skip_depth += 1
        if tag == "title":
            self._in_title = True
        if tag == "meta":
            key = (attrs_dict.get("property") or attrs_dict.get("name") or "").lower()
            if key in {"article:published_time", "published_time", "pubdate", "date", "dc.date"}:
                self.published_at = attrs_dict.get("content") or self.published_at
        if tag == "time" and attrs_dict.get("datetime") and not self.published_at:
            self.published_at = attrs_dict["datetime"]
        if tag == "table":
            self._in_table = True
            self.current_table = []
        if tag == "tr" and self._in_table:
            self._in_row = True
            self.current_row = []
        if tag in {"td", "th"} and self._in_row:
            self._in_cell = True
            self.current_cell_parts = []

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag == "title":
            self._in_title = False
        if tag in {"script", "style", "noscript", "svg", "nav", "header", "footer", "form", "button"} and self._skip_depth:
            self._skip_depth -= 1
        if tag in {"td", "th"} and self._in_cell:
            cell = " ".join(" ".join(self.current_cell_parts).split())
            self.current_row.append(cell)
            self._in_cell = False
        if tag == "tr" and self._in_row:
            if any(cell for cell in self.current_row):
                self.current_table.append(self.current_row)
            self.current_row = []
            self._in_row = False
        if tag == "table" and self._in_table:
            if self.current_table:
                self.tables.append({"title": "", "page": None, "rows": self.current_table})
            self.current_table = []
            self._in_table = False
        if self._tag_stack:
            self._tag_stack.pop()

    def handle_data(self, data: str) -> None:
        text = " ".join(data.split())
        if not text:
            return
        if self._in_title:
            self.title_parts.append(text)
        if self._skip_depth:
            return
        if self._in_cell:
            self.current_cell_parts.append(text)
        lowered = text.lower()
        if len(text) >= 3 and not any(token in lowered for token in BOILERPLATE_TOKENS):
            self.text_parts.append(text)


def parse_html_content(
    html: str,
    *,
    source_url: str | None = None,
    publisher: str | None = None,
) -> dict[str, Any]:
    """Parse HTML into source metadata, text blocks, and table-like rows."""

    parser = _ArticleHTMLParser()
    parser.feed(html)
    title = " ".join(" ".join(parser.title_parts).split()) or None
    body = "\n".join(parser.text_parts)
    text_blocks = []
    if body.strip():
        text_blocks.append(
            {
                "text": body.strip(),
                "page": None,
                "section": "HTML body",
                "location_hint": source_url or "html_content",
            }
        )
    warnings: list[str] = []
    if not text_blocks:
        warnings.append("No body text extracted from HTML document")
    return {
        "source": {
            "title": title,
            "publisher": publisher,
            "published_at": parser.published_at,
            "retrieved_at": now_iso(),
            "url": source_url,
            "document_type": "html_article",
            "access_status": "Available" if text_blocks else "Partial",
        },
        "text_blocks": text_blocks,
        "tables": parser.tables,
        "warnings": warnings,
    }
