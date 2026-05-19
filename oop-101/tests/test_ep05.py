"""Tests for ep05 in Oop 101."""

from ko.ep05_polymorphism import CardPayment, PointPayment, checkout


def test_ep05_polymorphism_checkout() -> None:
    """Test ep05 polymorphism checkout."""
    assert checkout(CardPayment(), 5000) == "card:5000"
    assert checkout(PointPayment(), 5000) == "point:5000"
