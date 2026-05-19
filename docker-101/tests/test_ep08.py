"""Tests for ep08 in Docker 101."""

# pyright: reportAny=false
from conftest import load_module

run = load_module("ko/08-database-with-app/step01_db_compose_check.py", "ep08").run


def test_ep08() -> None:
    """Test ep08."""
    result = run()
    assert result["success"] is True
    assert result["issues"] == []
