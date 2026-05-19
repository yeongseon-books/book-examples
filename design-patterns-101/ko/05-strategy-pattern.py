from dataclasses import dataclass

class PaymentStrategy:
    def pay(self, amount): raise NotImplementedError
class CreditCardStrategy(PaymentStrategy):
    def pay(self, amount): return amount
class PayPalStrategy(PaymentStrategy):
    def pay(self, amount): return round(amount * 1.02, 2)
class BankTransferStrategy(PaymentStrategy):
    def pay(self, amount): return round(amount - 1.5, 2)

@dataclass
class PaymentProcessor:
    strategy: PaymentStrategy
    def set_strategy(self, strategy): self.strategy = strategy
    def checkout(self, amount): return self.strategy.pay(amount)
