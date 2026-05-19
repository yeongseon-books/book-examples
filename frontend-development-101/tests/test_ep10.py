"""Tests for ep10 in Frontend Development 101."""

from __future__ import annotations

from conftest import load_module


def test_ep10_behavior() -> None:
    """Test ep10 behavior."""
    mod = load_module("ko/10-building-a-small-frontend-app/step01_ep10.py", "ep10")
    result = mod.run_demo()
    assert result["route"] == "1"
    assert result["email_error"] is None
    assert result["bundle_size"] > 0
