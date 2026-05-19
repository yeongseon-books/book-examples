# pyright: reportAny=false
from conftest import load_module


run = load_module("ko/04-volume-and-network/step01_volume_network_sim.py", "ep04").run


def test_ep04() -> None:
    result = run()
    assert result["success"] is True
    assert "db" in result["bridge_dns"]
