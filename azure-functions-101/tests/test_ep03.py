"""Tests for ep03 in Azure Functions 101."""

from conftest import run_script


def test_ep03() -> None:
    """Test ep03."""
    output = run_script("ko/03-host-and-worker/step01_host_worker_flow.py")
    assert "worker: handled http.hello" in output
