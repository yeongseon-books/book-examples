"""Tests for ep02 in Pandas 101."""

from __future__ import annotations

import importlib


def test_ep02_behavior() -> None:
    """Test ep02 behavior."""
    mod = importlib.import_module("en.ep02_series_dataframe_ops")
    out = mod.run()["ep02"]
    assert isinstance(out["loc_name"], str)
    assert out["iloc_score"] >= 55
    assert out["high_count"] >= 1
