"""Tests for ep07 in Frontend Development 101."""

from __future__ import annotations

from conftest import load_module


def test_ep07_behavior() -> None:
    """Test ep07 behavior."""
    mod = load_module("ko/07-forms-and-validation/step01_ep07.py", "ep07")
    result = mod.run_demo("bad", "123")
    assert result["email"] == "invalid email"
    assert result["password"] == "password too short"
