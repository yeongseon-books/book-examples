from abc import ABC, abstractmethod


class PaymentGateway(ABC):
    @abstractmethod
    def charge(self, amount: int) -> bool:
        raise NotImplementedError


class FakeGateway(PaymentGateway):
    def __init__(self, should_succeed: bool) -> None:
        self.should_succeed = should_succeed

    def charge(self, amount: int) -> bool:
        return self.should_succeed and amount > 0


class OrderService:
    def __init__(self, gateway: PaymentGateway) -> None:
        self.gateway = gateway

    def place_order(self, amount: int) -> str:
        return "paid" if self.gateway.charge(amount) else "failed"


if __name__ == "__main__":
    service = OrderService(FakeGateway(True))
    print(service.place_order(15000))
