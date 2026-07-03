"""Issuer ETF page/holdings parsers."""

from __future__ import annotations

from typing import Any

from .csv_parser import parse_csv_text
from .normalization import first_present, to_float


def parse_ishares_holdings_csv(text: str, *, ticker: str | None = None) -> dict[str, Any]:
    # iShares CSV files often include metadata lines before the holdings header.
    lines = [line for line in text.splitlines() if line.strip()]
    header_index = 0
    for index, line in enumerate(lines):
        lowered = line.lower()
        if "ticker" in lowered and ("name" in lowered or "holding" in lowered or "market value" in lowered):
            header_index = index
            break
    rows = parse_csv_text("\n".join(lines[header_index:])) if lines else []
    holdings = []
    as_of = None
    for row in rows:
        name = first_present(row, ["Name", "Holding Name", "Security Name"])
        if not name:
            continue
        holding_ticker = first_present(row, ["Ticker", "Local Ticker"])
        weight = to_float(first_present(row, ["Weight (%)", "Weight", "% Weight"]))
        market_value = to_float(first_present(row, ["Market Value", "Market Value USD"]))
        maturity = first_present(row, ["Maturity", "Maturity Date"])
        coupon = to_float(first_present(row, ["Coupon", "Coupon (%)"]))
        as_of = as_of or first_present(row, ["As Of", "As Of Date"])
        holdings.append(
            {
                "name": name,
                "ticker": holding_ticker,
                "weight_percent": weight,
                "market_value": market_value,
                "maturity": maturity,
                "coupon": coupon,
                "asset_class": first_present(row, ["Asset Class", "Sector"]),
            }
        )
    return {"ticker": ticker, "as_of_date": as_of, "holdings": holdings, "holding_count": len(holdings)}
