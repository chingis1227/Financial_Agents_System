"""CFTC COT parser and normalization."""

from __future__ import annotations

from typing import Any

from .csv_parser import parse_csv_text
from .normalization import first_present, to_float

GRAIN_MARKET_ALIASES = {
    "corn": ["CORN"],
    "wheat": ["WHEAT", "CHICAGO SRW WHEAT", "KC HRW WHEAT"],
    "soybeans": ["SOYBEANS", "SOYBEAN"],
}


def parse_cot_csv(text: str, *, market_filter: str | None = None) -> list[dict[str, Any]]:
    rows = parse_csv_text(text)
    normalized: list[dict[str, Any]] = []
    filters = [
        item.upper()
        for item in GRAIN_MARKET_ALIASES.get(str(market_filter or "").lower(), [str(market_filter or "").upper()])
        if item
    ]
    for row in rows:
        market = first_present(row, ["Market_and_Exchange_Names", "Market and Exchange Names", "market"]) or ""
        if filters and not any(item in str(market).upper() for item in filters):
            continue
        managed_long = to_float(first_present(row, ["M_Money_Positions_Long_All", "Managed Money Long", "managed_money_long"]))
        managed_short = to_float(first_present(row, ["M_Money_Positions_Short_All", "Managed Money Short", "managed_money_short"]))
        normalized.append(
            {
                "market_name": str(market).strip(),
                "exchange": first_present(row, ["Exchange", "exchange"]),
                "report_date": first_present(row, ["Report_Date_as_YYYY-MM-DD", "Report Date", "report_date"]),
                "open_interest": to_float(first_present(row, ["Open_Interest_All", "Open Interest", "open_interest"])),
                "managed_money_long": managed_long,
                "managed_money_short": managed_short,
                "managed_money_spreading": to_float(
                    first_present(row, ["M_Money_Positions_Spread_All", "Managed Money Spreading", "managed_money_spreading"])
                ),
                "producer_merchant_long": to_float(
                    first_present(row, ["Prod_Merc_Positions_Long_All", "Producer/Merchant Long", "producer_merchant_long"])
                ),
                "producer_merchant_short": to_float(
                    first_present(row, ["Prod_Merc_Positions_Short_All", "Producer/Merchant Short", "producer_merchant_short"])
                ),
                "swap_dealer_long": to_float(first_present(row, ["Swap_Positions_Long_All", "Swap Dealer Long", "swap_dealer_long"])),
                "swap_dealer_short": to_float(
                    first_present(row, ["Swap__Positions_Short_All", "Swap_Positions_Short_All", "Swap Dealer Short", "swap_dealer_short"])
                ),
                "nonreportable_long": to_float(
                    first_present(row, ["NonRept_Positions_Long_All", "Nonreportable Long", "nonreportable_long"])
                ),
                "nonreportable_short": to_float(
                    first_present(row, ["NonRept_Positions_Short_All", "Nonreportable Short", "nonreportable_short"])
                ),
                "net_managed_money": (managed_long - managed_short)
                if managed_long is not None and managed_short is not None
                else None,
                "position_percentile": None,
            }
        )
    return normalized
