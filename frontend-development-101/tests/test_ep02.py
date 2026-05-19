"""Tests for ep02 in Frontend Development 101."""

from __future__ import annotations

from conftest import load_module


def test_ep02_behavior() -> None:
    """Test ep02 behavior."""
    mod = load_module("ko/02-html-and-css-basics/step01_ep02.py", "ep02")
    result = mod.run_demo()
    assert result["specificity"] == (0, 1, 0)
    assert ".unused" in result["unused"]
