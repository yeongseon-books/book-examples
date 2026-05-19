"""Tests for ep01 in Pandas 101."""

from __future__ import annotations

import importlib


def test_ep01_behavior() -> None:
    """Test ep01 behavior."""
    mod = importlib.import_module("en.ep01_pandas_overview")
    out = mod.run()["ep01"]
    assert out["shape"] == (4, 3)
    assert "qty" in out["dtypes"]
    assert out["describe_mean_qty"] > 4.0
