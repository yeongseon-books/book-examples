"""Clean Code 101 - Episode 1: Naming."""

SECONDS_PER_DAY = 86_400


def first_completed_order(orders: list[dict[str, object]]) -> dict[str, object]:
    """First completed order."""
    return orders[0]


def calculate_invoice_subtotal(line_items: list[dict[str, int]]) -> int:
    """Calculate invoice subtotal."""
    return sum(item["price"] * item["qty"] for item in line_items)


def is_empty(values: list[object]) -> bool:
    """Is empty."""
    return len(values) == 0
