"""Tests for ep02 in Azure Functions 101."""

from conftest import run_script


def test_ep02() -> None:
    """Test ep02."""
    output = run_script("ko/02-triggers-and-bindings/step01_queue_to_invoice.py")
    assert "'amount': 35000" in output
