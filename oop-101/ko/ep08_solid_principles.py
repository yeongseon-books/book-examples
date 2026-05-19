"""Oop 101 - Episode 8: Solid principles."""

# pyright: reportImplicitOverride=false

from abc import ABC, abstractmethod


class PaymentGateway(ABC):
    @abstractmethod
    def charge(self, amount: int) -> bool:
        """Charge."""
        raise NotImplementedError


class FakeGateway(PaymentGateway):
    """Fake gateway."""

    should_succeed: bool

    def __init__(self, should_succeed: bool) -> None:
        self.should_succeed = should_succeed

    def charge(self, amount: int) -> bool:
        """Charge."""
        return self.should_succeed and amount > 0


class OrderService:
    """Order service."""

    gateway: PaymentGateway

    def __init__(self, gateway: PaymentGateway) -> None:
        self.gateway = gateway

    def place_order(self, amount: int) -> str:
        """Place order."""
        return "paid" if self.gateway.charge(amount) else "failed"


if __name__ == "__main__":
    service = OrderService(FakeGateway(True))
    print(service.place_order(15000))
