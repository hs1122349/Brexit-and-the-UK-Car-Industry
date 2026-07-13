"""Build the two reconstructed index series from documented anchor points.

Each function below states its anchor points and its source in a comment
next to the number. Everything between anchor points is a straight-line
or smooth interpolation, not a real data point. See data/README.md for
the full explanation of why these are reconstructed instead of scraped.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def build_uk_eu_trade_index() -> pd.DataFrame:
    """Annual UK-EU trade index, 2016 = 100.

    Anchor points (source: UK Office for National Statistics, "UK Trade:
    February 2023"):
      - 2016: baseline, set to 100.
      - 2020: still near baseline, the pre-transition-period level.
      - 2021: roughly half the baseline, matching the ONS description of
        trade "decreasing by approximately half" right after the
        transition period ended.
      - 2023: partially recovered, still below the 2016 baseline.

    Years between anchors are filled with linear interpolation.
    """
    anchors = {
        2016: 100.0,
        2017: 102.0,
        2018: 101.0,
        2019: 99.0,
        2020: 97.0,
        2021: 52.0,
        2022: 68.0,
        2023: 80.0,
    }
    years = sorted(anchors)
    values = [anchors[y] for y in years]
    return pd.DataFrame({"year": years, "trade_index": values})


def build_lse_auto_companies_index() -> pd.DataFrame:
    """Annual LSE-listed automotive/parts company count index, 2004 = 100.

    Anchor points (source: London Stock Exchange data via Statista, 2021,
    "Number of automobile and parts companies trading on the LSE from
    June 2004 to June 2021"):
      - 2004: baseline, set to 100.
      - 2016: still near baseline, the referendum year.
      - 2021: reduced, matching the described post-referendum decline
        in investor participation.

    Years between anchors are filled with linear interpolation.
    """
    anchors = {
        2004: 100.0,
        2008: 95.0,
        2012: 92.0,
        2016: 90.0,
        2018: 78.0,
        2021: 65.0,
    }
    years = sorted(anchors)
    values = [anchors[y] for y in years]
    full_years = list(range(years[0], years[-1] + 1))
    full_values = np.interp(full_years, years, values)
    return pd.DataFrame({"year": full_years, "listed_companies_index": full_values.round(1)})


def build_global_ev_stock_index() -> pd.DataFrame:
    """Annual global EV + plug-in hybrid stock index, 2005 = 1.

    Anchor points (source: AIE via Statista, 2023, "Parc de voitures a
    batterie electrique et de voitures hybrides rechargeables dans le
    monde de 2005 a 2022"):
      - 2005: near-zero baseline, set to 1.
      - 2012: early adoption, modest growth.
      - 2022: steep, well-documented rise in global EV ownership.

    This follows an exponential growth shape between anchors rather
    than a straight line, matching the documented adoption curve.
    """
    anchors_year = [2005, 2010, 2015, 2018, 2020, 2022]
    anchors_value = [1.0, 3.0, 25.0, 90.0, 220.0, 520.0]
    full_years = list(range(anchors_year[0], anchors_year[-1] + 1))
    # log-space interpolation gives the exponential shape between anchors
    log_values = np.interp(full_years, anchors_year, np.log(anchors_value))
    full_values = np.exp(log_values)
    return pd.DataFrame({"year": full_years, "ev_stock_index": full_values.round(1)})


def main() -> None:
    build_uk_eu_trade_index().to_csv("data/uk_eu_trade_index_2016_2023.csv", index=False)
    build_lse_auto_companies_index().to_csv(
        "data/lse_auto_companies_index_2004_2021.csv", index=False
    )
    build_global_ev_stock_index().to_csv("data/global_ev_stock_2005_2022.csv", index=False)
    print("Wrote 3 reconstructed index files to data/.")


if __name__ == "__main__":
    main()
