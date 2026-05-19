"""Tests for ep05 in Docker 101."""

# pyright: reportAny=false
from conftest import load_module

run = load_module("ko/05-docker-compose/step01_compose_validate.py", "ep05").run


def test_ep05() -> None:
    """Test ep05."""
    result = run()
    assert result["success"] is True
    assert result["issues"] == []
