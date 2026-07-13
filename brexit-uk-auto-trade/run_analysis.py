"""Compute year-over-year change, CAGR, and recovery ratios on the three
reconstructed index files, and print the UK production and FTA facts
alongside them.

Usage:
    python run_build_data.py   # first, if data/*_index_*.csv don't exist
    python run_analysis.py
"""
import pandas as pd

from src.analysis import cagr, peak_to_trough_decline, recovery_ratio, yoy_change


def report_series(path: str, year_col: str, value_col: str, label: str) -> None:
    df = pd.read_csv(path)
    df["yoy_pct"] = yoy_change(df[value_col])

    start, end = df[value_col].iloc[0], df[value_col].iloc[-1]
    years_span = df[year_col].iloc[-1] - df[year_col].iloc[0]
    growth = cagr(start, end, years_span)
    decline = peak_to_trough_decline(df[value_col])

    print(f"\n=== {label} ===")
    print(df.round(2).to_string(index=False))
    print(f"CAGR over {years_span} years: {growth:.1f}%")
    print(f"Largest peak-to-trough decline: {decline:.1f}%")


def main():
    report_series("data/uk_eu_trade_index_2016_2023.csv", "year", "trade_index",
                   "UK-EU trade index (2016 = 100), reconstructed")
    report_series("data/lse_auto_companies_index_2004_2021.csv", "year",
                   "listed_companies_index", "LSE-listed automotive companies index (2004 = 100), reconstructed")
    report_series("data/global_ev_stock_2005_2022.csv", "year", "ev_stock_index",
                   "Global EV + plug-in hybrid stock index (2005 = 1), reconstructed")

    trade = pd.read_csv("data/uk_eu_trade_index_2016_2023.csv")
    ratio = recovery_ratio(trade["trade_index"], drop_year=2021, recovery_year=2023,
                            years=trade["year"])
    print(f"\nUK-EU trade recovery ratio, 2021 to 2023: {ratio:.2f} "
          f"({'above' if ratio > 1 else 'below'} the 2021 level)")

    print("\n=== UK production, 2022 (official, SMMT 2023) ===")
    print(pd.read_csv("data/uk_production_2022.csv").to_string(index=False))

    print("\n=== Post-Brexit free trade agreements ===")
    print(pd.read_csv("data/fta_count_post_brexit.csv").to_string(index=False))


if __name__ == "__main__":
    main()
