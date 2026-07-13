"""Small, general analysis functions used on any of the index series."""
from __future__ import annotations

import pandas as pd


def yoy_change(series: pd.Series) -> pd.Series:
    """Year-over-year percent change. First value is NaN, by definition."""
    return series.pct_change() * 100


def cagr(start_value: float, end_value: float, years: int) -> float:
    """Compound annual growth rate, as a percent."""
    if start_value <= 0 or years <= 0:
        raise ValueError("start_value and years must both be positive")
    return ((end_value / start_value) ** (1 / years) - 1) * 100


def recovery_ratio(series: pd.Series, drop_year: int, recovery_year: int,
                    years: pd.Series) -> float:
    """Value at recovery_year over value at drop_year, as a ratio.

    A value of 1.0 means full recovery to the drop-year level.
    Above 1.0 means the series grew past that level.
    """
    idx = pd.Index(years)
    drop_value = series[idx.get_loc(drop_year)]
    recovery_value = series[idx.get_loc(recovery_year)]
    return recovery_value / drop_value


def peak_to_trough_decline(series: pd.Series) -> float:
    """Largest percent drop from any point to a later point in the series."""
    running_max = series.cummax()
    drawdown = (series - running_max) / running_max
    return drawdown.min() * 100
