"""Tests for ep05 in Software Design 101."""

from ko.ep05_interfaces_abstraction import MockGateway, checkout


def test_ep05_gateway_abstraction() -> None:
    """Test ep05 gateway abstraction."""
    gateway = MockGateway()
    assert checkout(500, gateway) == "mock:500:ok"
    assert gateway.calls == [500]
