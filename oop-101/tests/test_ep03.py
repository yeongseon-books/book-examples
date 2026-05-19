import pytest
from ko.ep03_encapsulation import BankAccount


def test_ep03_bank_account_behavior() -> None:
    account = BankAccount("kim", 100)
    account.deposit(50)
    account.withdraw(30)
    assert account.balance == 120
    with pytest.raises(ValueError):
        account.withdraw(1000)
