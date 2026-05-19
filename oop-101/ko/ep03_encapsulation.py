"""Oop 101 - Episode 3: Encapsulation."""


class BankAccount:
    """Bank account."""

    owner: str
    _balance: int

    def __init__(self, owner: str, initial_balance: int = 0) -> None:
        self.owner = owner
        self._balance = initial_balance

    @property
    def balance(self) -> int:
        """Balance."""
        return self._balance

    def deposit(self, amount: int) -> None:
        """Deposit."""
        if amount <= 0:
            raise ValueError("amount must be positive")
        self._balance += amount

    def withdraw(self, amount: int) -> None:
        """Withdraw."""
        if amount <= 0:
            raise ValueError("amount must be positive")
        if amount > self._balance:
            raise ValueError("insufficient balance")
        self._balance -= amount


if __name__ == "__main__":
    account = BankAccount("minsu", 1000)
    account.deposit(200)
    account.withdraw(500)
    print(account.balance)
