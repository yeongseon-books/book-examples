"""Tests for ep02 in Incident Response 101."""

from conftest import load_module

run = load_module("ko/02-severity/step01_example.py", "ep02").run


def test_ep02_sev1_high_impact() -> None:
    """Test ep02 sev1 high impact."""
    result = run()
    assert result["severity"] == "SEV1"
