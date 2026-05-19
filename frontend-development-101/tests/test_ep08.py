"""Tests for ep08 in Frontend Development 101."""

from __future__ import annotations

from conftest import load_module


def test_ep08_behavior() -> None:
    """Test ep08 behavior."""
    mod = load_module("ko/08-styling-and-design-system/step01_ep08.py", "ep08")
    missing = mod.run_demo()
    assert missing == []
