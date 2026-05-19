"""Tests for ep03 in Incident Response 101."""

from conftest import load_module

run = load_module("ko/03-initial-response/step01_example.py", "ep03").run


def test_ep03_sev1_routes_to_senior_oncall() -> None:
    """Test ep03 sev1 routes to senior oncall."""
    result = run()
    assert "senior-ic" in result["responders"]
