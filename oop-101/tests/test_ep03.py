"""Tests for ep03 in Oop 101."""

import pytest
from ko.ep03_encapsulation import BankAccount


def test_ep03_bank_account_behavior() -> None:
    """Test ep03 bank account behavior."""
    account = BankAccount("kim", 100)
    account.deposit(50)
    account.withdraw(30)
    assert account.balance == 120
    with pytest.raises(ValueError):
        account.withdraw(1000)
