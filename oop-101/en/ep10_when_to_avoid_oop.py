from dataclasses import dataclass


@dataclass
class CartItem:
    name: str
    price: int
    quantity: int


class Cart:
    def __init__(self, items: list[CartItem]) -> None:
        self.items = items

    def total(self) -> int:
        return sum(item.price * item.quantity for item in self.items)


def total_functional(items: list[dict[str, int]]) -> int:
    return sum(item["price"] * item["quantity"] for item in items)


if __name__ == "__main__":
    oop_total = Cart([CartItem("pen", 1000, 2)]).total()
    func_total = total_functional([{"price": 1000, "quantity": 2}])
    print(oop_total, func_total)
