"""Software Design 101 - Episode 8: Reduce change impact."""


def bad_total(quantity: int) -> int:
    """Bad total."""
    return quantity * 137 + 12


PRICE_PER_ITEM = 137
HANDLING_FEE = 12


def good_total(quantity: int, config: dict[str, int] | None = None) -> int:
    """Good total."""
    cfg = config or {"price": PRICE_PER_ITEM, "fee": HANDLING_FEE}
    return quantity * cfg["price"] + cfg["fee"]


def change_points_bad() -> int:
    """Change points bad."""
    return 2


def change_points_good() -> int:
    """Change points good."""
    return 1
