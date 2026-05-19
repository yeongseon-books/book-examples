"""Tests for ep06 in Azure Functions 101."""

from conftest import run_script


def test_ep06() -> None:
    """Test ep06."""
    output = run_script("ko/06-scaling-and-cold-start/step01_scale_simulator.py")
    assert "'instances': 5" in output
