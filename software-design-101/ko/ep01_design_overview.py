"""Software Design 101 - Episode 1: Design overview."""


def bad_order_processor(order: dict) -> str:
    """Bad order processor."""
    subtotal = sum(item["price"] * item["qty"] for item in order["items"])
    tax = int(subtotal * 0.1)
    total = subtotal + tax
    return f"order={order['id']} subtotal={subtotal} tax={tax} total={total}"


def calculate_subtotal(items: list[dict]) -> int:
    """Calculate subtotal."""
    return sum(item["price"] * item["qty"] for item in items)


def calculate_tax(subtotal: int, rate: float = 0.1) -> int:
    """Calculate tax."""
    return int(subtotal * rate)


def format_receipt(order_id: str, subtotal: int, tax: int) -> str:
    """Format receipt."""
    total = subtotal + tax
    return f"order={order_id} subtotal={subtotal} tax={tax} total={total}"


def good_order_processor(order: dict) -> str:
    """Good order processor."""
    subtotal = calculate_subtotal(order["items"])
    tax = calculate_tax(subtotal)
    return format_receipt(order["id"], subtotal, tax)
