"""Tests for ep06 in Azure Aca Deep Dive."""

from conftest import load_module

run = load_module("ko/06-envoy-ingress-path/step01_ingress_path.py", "ep06").run


def test_ep06_ingress_routing_headers() -> None:
    """Test ep06 ingress routing headers."""
    result = run()
    assert result["episode"] == 6
    assert result["status_code"] == 200
    assert result["result"]["proto"] == "https"
    assert result["result"]["revision"] == "orders--green"
