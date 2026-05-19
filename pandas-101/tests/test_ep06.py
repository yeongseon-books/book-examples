"""Tests for ep06 in Pandas 101."""

from __future__ import annotations

import importlib


def test_ep06_behavior() -> None:
    """Test ep06 behavior."""
    mod = importlib.import_module("en.ep06_groupby_agg")
    out = mod.run()["ep06"]
    assert out["group_shape"][1] == 3
    assert 0.99 <= out["share_sum"] <= 1.01
