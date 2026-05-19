"""Tests for ep07 in Azure Functions 101."""

from conftest import run_script


def test_ep07() -> None:
    """Test ep07."""
    output = run_script("ko/07-monitoring-and-ops/step01_monitoring_queries.py")
    assert "requests | where timestamp > ago(1h)" in output
