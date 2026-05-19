"""Tests for ep09 in Docker 101."""

# pyright: reportAny=false
from conftest import load_module

run = load_module(
    "ko/09-image-optimization/step01_image_optimization_sim.py", "ep09"
).run


def test_ep09() -> None:
    """Test ep09."""
    result = run()
    assert result["success"] is True
    assert result["estimate"]["saved"] > 0
