class Account:
    def __init__(self, owner: str, balance: int = 0) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: int) -> None:
        self.balance += amount

    def withdraw(self, amount: int) -> None:
        self.balance -= amount

    def __str__(self) -> str:
        return f"Account(owner={self.owner}, balance={self.balance})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Account):
            return False
        return self.owner == other.owner and self.balance == other.balance


def main() -> None:
    account = Account("민수", 100)
    account.deposit(50)
    print(account)


if __name__ == "__main__":
    main()
