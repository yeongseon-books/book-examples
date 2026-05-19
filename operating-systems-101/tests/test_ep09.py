"""Tests for ep09 in Operating Systems 101."""

from common import ep09_syscall_demo


def test_ep09_syscall_io_roundtrip():
    """Test ep09 syscall io roundtrip."""
    out = ep09_syscall_demo()
    assert out["data"] == "hello"
