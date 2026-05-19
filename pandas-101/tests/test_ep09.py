"""Tests for ep09 in Pandas 101."""

from __future__ import annotations

import importlib


def test_ep09_behavior() -> None:
    """Test ep09 behavior."""
    mod = importlib.import_module("en.ep09_apply_vs_vectorized")
    out = mod.run()["ep09"]
    assert out["max_diff"] < 1e-9
    assert out["same_values"] is True
