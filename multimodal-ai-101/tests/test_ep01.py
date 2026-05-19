"""Tests for ep01 in Multimodal Ai 101."""

from conftest import load_module

run = load_module("ko/01-why-multimodal-matters/step01_why_multimodal.py", "ep01").run


def test_ep01_runs() -> None:
    """Test ep01 runs."""
    result = run()
    assert result["shape"] == (8, 8)
