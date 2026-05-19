"""Tests for ep08 in Pandas 101."""

from __future__ import annotations

import importlib


def test_ep08_behavior() -> None:
    """Test ep08 behavior."""
    mod = importlib.import_module("en.ep08_time_series_resample")
    out = mod.run()["ep08"]
    assert out["daily_rows"] == 40
    assert out["weekly_rows"] >= 5
    assert out["rolling_last"] > 0
