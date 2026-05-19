"""Design Patterns 101 - Episode 5: Strategy pattern."""

from dataclasses import dataclass


class PaymentStrategy:
    """Payment strategy."""

    def pay(self, amount):
        """Pay."""
        raise NotImplementedError


class CreditCardStrategy(PaymentStrategy):
    """Credit card strategy."""

    def pay(self, amount):
        """Pay."""
        return amount


class PayPalStrategy(PaymentStrategy):
    """Pay pal strategy."""

    def pay(self, amount):
        """Pay."""
        return round(amount * 1.02, 2)


class BankTransferStrategy(PaymentStrategy):
    """Bank transfer strategy."""

    def pay(self, amount):
        """Pay."""
        if amount <= 1.5:
            raise ValueError("amount must be greater than transfer fee")
        return round(amount - 1.5, 2)


@dataclass
class PaymentProcessor:
    """Payment processor."""

    strategy: PaymentStrategy

    def set_strategy(self, strategy):
        """Set strategy."""
        self.strategy = strategy

    def checkout(self, amount):
        """Checkout."""
        return self.strategy.pay(amount)
