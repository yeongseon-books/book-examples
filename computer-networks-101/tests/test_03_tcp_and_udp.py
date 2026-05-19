"""Tests for 03 tcp and udp in Computer Networks 101."""

from tests._loader import load_ko


def test_tcp_udp_echo() -> None:
    """Test tcp udp echo."""
    ep = load_ko("03-tcp-and-udp")
    out = ep.compare_transports(b"hello")
    assert out["tcp"] == b"hello"
    assert out["udp"] == b"hello"
