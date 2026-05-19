"""Tests for ep09 in Oop 101."""

from ko.ep09_oop_design_example import (
    Inventory,
    OrderService,
    PaymentProcessor,
    Product,
)


def test_ep09_integrated_order_flow() -> None:
    """Test ep09 integrated order flow."""
    service = OrderService(Inventory({"A": 2}), PaymentProcessor())
    assert service.order(Product("A", 700), 1) == "ordered"
    assert service.order(Product("A", 700), 5) == "out_of_stock"
