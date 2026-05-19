"""Tests for ep07 in Incident Response 101."""

from conftest import load_module

run = load_module("ko/07-mitigation-and-resolution/step01_example.py", "ep07").run


def test_ep07_mitigation_state_machine() -> None:
    """Test ep07 mitigation state machine."""
    states = run()
    assert states == ["proposed", "applied", "verified"]
