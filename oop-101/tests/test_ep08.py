"""Tests for ep08 in Oop 101."""

from ko.ep08_solid_principles import FakeGateway, OrderService


def test_ep08_dependency_inversion_like() -> None:
    """Test ep08 dependency inversion like."""
    assert OrderService(FakeGateway(True)).place_order(1000) == "paid"
    assert OrderService(FakeGateway(False)).place_order(1000) == "failed"
