"""Tests for ep04 in Pandas 101."""

from __future__ import annotations

import importlib


def test_ep04_behavior() -> None:
    """Test ep04 behavior."""
    mod = importlib.import_module("en.ep04_boolean_query")
    out = mod.run()["ep04"]
    assert out["filter_count"] >= 0
    assert out["query_count"] >= 0
    assert out["isin_count"] >= out["query_count"]
