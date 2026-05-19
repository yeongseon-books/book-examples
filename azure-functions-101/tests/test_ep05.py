"""Tests for ep05 in Azure Functions 101."""

from conftest import run_script


def test_ep05() -> None:
    """Test ep05."""
    output = run_script("ko/05-choosing-a-plan/step01_plan_selector.py")
    assert "Flex Consumption" in output
