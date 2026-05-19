"""Oop 101 - Episode 9: Oop design example."""

from dataclasses import dataclass


@dataclass
class Product:
    """Product."""

    sku: str
    price: int


class Inventory:
    """Inventory."""

    def __init__(self, stock: dict[str, int]) -> None:
        self.stock = stock

    def reserve(self, sku: str, qty: int) -> bool:
        """Reserve."""
        current = self.stock.get(sku, 0)
        if qty <= 0 or current < qty:
            return False
        self.stock[sku] = current - qty
        return True


class PaymentProcessor:
    """Payment processor."""

    def pay(self, amount: int) -> bool:
        """Pay."""
        return amount > 0


class OrderService:
    """Order service."""

    def __init__(self, inventory: Inventory, payment: PaymentProcessor) -> None:
        self.inventory = inventory
        self.payment = payment

    def order(self, product: Product, qty: int) -> str:
        """Order."""
        if not self.inventory.reserve(product.sku, qty):
            return "out_of_stock"
        total = product.price * qty
        return "ordered" if self.payment.pay(total) else "payment_failed"


if __name__ == "__main__":
    service = OrderService(Inventory({"P-1": 3}), PaymentProcessor())
    result = service.order(Product("P-1", 7000), 2)
    print(result)
