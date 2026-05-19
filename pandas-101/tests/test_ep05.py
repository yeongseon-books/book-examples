"""Tests for ep05 in Pandas 101."""

from __future__ import annotations

import importlib


def test_ep05_behavior() -> None:
    """Test ep05 behavior."""
    mod = importlib.import_module("en.ep05_missing_values")
    out = mod.run()["ep05"]
    assert out["na_count"] == 4
    assert out["mean_fill_nulls"] == 0
    assert out["interpolate_nulls"] == 0
