from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: int) -> str:
        raise NotImplementedError


class CardPayment(PaymentMethod):
    def pay(self, amount: int) -> str:
        return f"card:{amount}"


class PointPayment(PaymentMethod):
    def pay(self, amount: int) -> str:
        return f"point:{amount}"


def checkout(method: PaymentMethod, amount: int) -> str:
    return method.pay(amount)


if __name__ == "__main__":
    print(checkout(CardPayment(), 12000))
