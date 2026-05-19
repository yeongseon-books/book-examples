"""Tests for 06 network in Containers 101."""

from ko import _06_network as ep


def test_same_bridge_can_ping():
    """Test same bridge can ping."""
    bridge = ep.BridgeNetwork("br0", "10.20.0.0/29")
    bridge.connect("web")
    bridge.connect("db")
    assert bridge.can_ping("web", "db") is True


def test_different_bridges_cannot_ping():
    """Test different bridges cannot ping."""
    a = ep.BridgeNetwork("a", "10.30.0.0/29")
    b = ep.BridgeNetwork("b", "10.31.0.0/29")
    a.connect("api")
    b.connect("worker")
    assert a.can_ping("api", "worker") is False
