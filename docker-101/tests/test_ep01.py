"""Tests for ep01 in Docker 101."""

# pyright: reportAny=false
from conftest import load_module

run = load_module("ko/01-what-is-docker/step01_manual_loop.py", "ep01").run


def test_ep01() -> None:
    """Test ep01."""
    result = run()
    assert result["success"] is True
    assert "image" in result["report"]["keywords"]
