"""Tests for ep05 in Azure Aca Deep Dive."""

from conftest import load_module

run = load_module("ko/05-dapr-sidecar-internals/step01_dapr_sidecar.py", "ep05").run


def test_ep05_dapr_sidecar_ports() -> None:
    """Test ep05 dapr sidecar ports."""
    result = run()
    assert result["episode"] == 5
    assert result["plan"]["sidecar"] == "daprd"
    assert result["plan"]["ports"]["http"] == 3500
