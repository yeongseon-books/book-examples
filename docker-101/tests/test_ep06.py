"""Tests for ep06 in Docker 101."""

# pyright: reportAny=false
from conftest import load_module

run = load_module("ko/06-env-and-config/step01_env_config_validate.py", "ep06").run


def test_ep06() -> None:
    """Test ep06."""
    result = run()
    assert result["success"] is True
    assert result["env"]["LOG_LEVEL"] == "INFO"
