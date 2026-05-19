"""Tests for 07 case interview in Data Science Career 101."""

from __future__ import annotations

from .conftest import load_module

mod = load_module("ko/07-case-interview.py")


def test_case_framework_contains_required_components() -> None:
    """Test case framework contains required components."""
    framework = mod.build_case_framework("DAU dropped 20%")
    assert mod.is_complete_framework(framework)
    assert framework["north_star_metric"] == "DAU"
