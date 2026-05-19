"""Tests for ep04 in Docker 101."""

# pyright: reportAny=false
from conftest import load_module

run = load_module("ko/04-volume-and-network/step01_volume_network_sim.py", "ep04").run


def test_ep04() -> None:
    """Test ep04."""
    result = run()
    assert result["success"] is True
    assert "db" in result["bridge_dns"]
