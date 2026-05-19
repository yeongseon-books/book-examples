"""Tests for ep06 in Frontend Development 101."""

from __future__ import annotations

from conftest import load_module


def test_ep06_behavior() -> None:
    """Test ep06 behavior."""
    mod = load_module("ko/06-api-calls-and-async/step01_ep06.py", "ep06")
    result = mod.run_demo()
    assert result["result"]["status"] == "success"
    assert result["async_patterns"]["await"] >= 1
