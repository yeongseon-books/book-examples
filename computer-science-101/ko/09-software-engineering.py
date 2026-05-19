"""에피소드 09: 리팩터링 + TDD 흐름 데모"""


def price_bad(order: dict) -> int:
    """Price bad."""
    total = order["price"] * order["qty"]
    if order["user"] == "vip":
        total = int(total * 0.7)
    elif order["user"] == "member":
        total = int(total * 0.9)
    if order.get("coupon"):
        total -= order["coupon"]
    if total < 0:
        total = 0
    return total


DISCOUNT = {"vip": 0.7, "member": 0.9}


def discount_price(price: int, qty: int, user: str) -> int:
    """Discount price."""
    base = price * qty
    return int(base * DISCOUNT.get(user, 1.0))


def apply_coupon(total: int, coupon: int | None) -> int:
    """Apply coupon."""
    if coupon is None:
        return total
    return max(0, total - coupon)


def price_refactored(order: dict) -> int:
    """Price refactored."""
    discounted = discount_price(order["price"], order["qty"], order["user"])
    return apply_coupon(discounted, order.get("coupon"))


if __name__ == "__main__":
    order = {"price": 100, "qty": 2, "user": "vip", "coupon": 20}
    print(price_bad(order), price_refactored(order))
