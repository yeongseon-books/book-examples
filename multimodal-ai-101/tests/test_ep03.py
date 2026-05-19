"""Tests for ep03 in Multimodal Ai 101."""

from conftest import load_module

run = load_module("ko/03-vlm-architecture/step01_vlm_architecture.py", "ep03").run


def test_ep03_vlm_returns_string() -> None:
    """Test ep03 vlm returns string."""
    assert isinstance(run("table"), str)
