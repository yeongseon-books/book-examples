"""Tests for ep03 in Frontend Development 101."""

from __future__ import annotations

from conftest import load_module


def test_ep03_behavior() -> None:
    """Test ep03 behavior."""
    mod = load_module("ko/03-javascript-basics/step01_ep03.py", "ep03")
    result = mod.run_demo()
    assert result["decls"]["var"] == 0
    assert "App" in result["components"]
