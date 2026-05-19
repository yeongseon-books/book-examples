"""Tests for ep01 in Incident Response 101."""

from conftest import load_module

run = load_module("ko/01-what-is-incident/step01_example.py", "ep01").run


def test_ep01_incident_classification() -> None:
    """Test ep01 incident classification."""
    result = run()
    assert result["classification"] == "incident"
