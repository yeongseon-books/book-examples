"""Software Design 101 - Episode 5: Interfaces abstraction."""

from typing import Protocol


class PaymentGateway(Protocol):
    """Payment gateway."""

    def charge(self, amount: int) -> str: ...


class StripeGateway:
    """Stripe gateway."""

    def charge(self, amount: int) -> str:
        """Charge."""
        return f"stripe:{amount}:ok"


class MockGateway:
    """Mock gateway."""

    def __init__(self) -> None:
        self.calls: list[int] = []

    def charge(self, amount: int) -> str:
        """Charge."""
        self.calls.append(amount)
        return f"mock:{amount}:ok"


def checkout(amount: int, gateway: PaymentGateway) -> str:
    """Checkout."""
    return gateway.charge(amount)
