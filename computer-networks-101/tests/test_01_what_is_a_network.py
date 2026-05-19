"""Tests for 01 what is a network in Computer Networks 101."""

from tests._loader import load_ko


def test_echo_roundtrip() -> None:
    """Test echo roundtrip."""
    ep = load_ko("01-what-is-a-network")
    assert ep.run_demo(b"ping") == b"ping"
