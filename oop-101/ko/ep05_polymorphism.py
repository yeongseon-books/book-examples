"""Oop 101 - Episode 5: Polymorphism."""

# pyright: reportImplicitOverride=false

from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: int) -> str:
        """Pay."""
        raise NotImplementedError


class CardPayment(PaymentMethod):
    """Card payment."""

    def pay(self, amount: int) -> str:
        """Pay."""
        return f"card:{amount}"


class PointPayment(PaymentMethod):
    """Point payment."""

    def pay(self, amount: int) -> str:
        """Pay."""
        return f"point:{amount}"


def checkout(method: PaymentMethod, amount: int) -> str:
    """Checkout."""
    return method.pay(amount)


if __name__ == "__main__":
    print(checkout(CardPayment(), 12000))
