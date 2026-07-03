"""Small standard-library HTML table parser."""

from __future__ import annotations

from html.parser import HTMLParser
from typing import Any


class _TableParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.tables: list[list[list[str]]] = []
        self._table: list[list[str]] | None = None
        self._row: list[str] | None = None
        self._cell: list[str] | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "table":
            self._table = []
        elif tag == "tr" and self._table is not None:
            self._row = []
        elif tag in {"td", "th"} and self._row is not None:
            self._cell = []

    def handle_data(self, data: str) -> None:
        if self._cell is not None:
            self._cell.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag in {"td", "th"} and self._cell is not None and self._row is not None:
            self._row.append(" ".join(" ".join(self._cell).split()))
            self._cell = None
        elif tag == "tr" and self._row is not None and self._table is not None:
            if any(cell for cell in self._row):
                self._table.append(self._row)
            self._row = None
        elif tag == "table" and self._table is not None:
            self.tables.append(self._table)
            self._table = None


def parse_html_tables(html: str) -> list[list[dict[str, Any]]]:
    parser = _TableParser()
    parser.feed(html)
    parsed: list[list[dict[str, Any]]] = []
    for table in parser.tables:
        if not table:
            continue
        headers = table[0]
        rows = []
        for row in table[1:]:
            rows.append({headers[index] if index < len(headers) else f"col_{index}": value for index, value in enumerate(row)})
        parsed.append(rows)
    return parsed
