"""Unit tests for the analysis functions. Small synthetic series only.

Run with: pytest tests/
"""
import pandas as pd
import pytest

from src.analysis import cagr, peak_to_trough_decline, recovery_ratio, yoy_change


def test_yoy_change_basic():
    series = pd.Series([100, 110, 99])
    result = yoy_change(series)
    assert result.iloc[1] == pytest.approx(10.0)
    assert result.iloc[2] == pytest.approx(-10.0)
    assert pd.isna(result.iloc[0])


def test_cagr_doubling_over_one_year():
    assert cagr(100, 200, 1) == pytest.approx(100.0)


def test_cagr_flat_series_is_zero():
    assert cagr(100, 100, 5) == pytest.approx(0.0)


def test_cagr_rejects_non_positive_start():
    with pytest.raises(ValueError):
        cagr(0, 100, 5)


def test_recovery_ratio_full_recovery():
    series = pd.Series([100.0, 50.0, 100.0])
    years = pd.Series([2020, 2021, 2022])
    ratio = recovery_ratio(series, drop_year=2021, recovery_year=2022, years=years)
    assert ratio == pytest.approx(2.0)


def test_peak_to_trough_decline():
    series = pd.Series([100.0, 120.0, 60.0, 90.0])
    decline = peak_to_trough_decline(series)
    assert decline == pytest.approx(-50.0)
