from typing import Protocol


class PaymentGateway(Protocol):
    def charge(self, amount: int) -> str: ...


class StripeGateway:
    def charge(self, amount: int) -> str:
        return f"stripe:{amount}:ok"


class MockGateway:
    def __init__(self) -> None:
        self.calls: list[int] = []

    def charge(self, amount: int) -> str:
        self.calls.append(amount)
        return f"mock:{amount}:ok"


def checkout(amount: int, gateway: PaymentGateway) -> str:
    return gateway.charge(amount)
