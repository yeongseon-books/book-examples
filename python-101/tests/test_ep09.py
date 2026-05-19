"""Tests for ep09 in Python 101."""

from en.ep09_classes import Account


def test_account_equality_and_balance() -> None:
    """Test account equality and balance."""
    a = Account("Alex", 10)
    b = Account("Alex", 10)
    a.deposit(5)
    a.withdraw(2)
    assert a.balance == 13
    assert b == Account("Alex", 10)
