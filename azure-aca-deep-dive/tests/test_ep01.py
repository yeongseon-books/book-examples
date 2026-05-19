"""Tests for ep01 in Azure Aca Deep Dive."""

from conftest import load_module

run = load_module("ko/01-aca-architecture/step01_architecture_map.py", "ep01").run


def test_ep01_architecture_contains_core_components() -> None:
    """Test ep01 architecture contains core components."""
    result = run()
    assert result["episode"] == 1
    assert result["plan"]["components"] == ["envoy", "keda", "dapr"]
    assert result["simulated"]["stdout"].startswith("az containerapp env show")
