"""Tests for ep05 in Azure App Service Deep Dive."""

from conftest import load_module

evaluate = load_module(
    "ko/05-scaling-internals/step01_autoscale_loop.py", "ep05"
).evaluate


def test_ep05_autoscale_loop_behaviors() -> None:
    """Test ep05 autoscale loop behaviors."""
    assert evaluate(80.0, 0.0) == "scale_out"
    assert evaluate(20.0, 0.0) == "scale_in"
    assert evaluate(45.0, 20.0) == "hold"
