def bad_checkout(user_input: str, file_path: str) -> str:
    qty = int(user_input)
    price = 100
    total = qty * price
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(str(total))
    return f"TOTAL:{total}"


def parse_quantity(user_input: str) -> int:
    return int(user_input)


def compute_total(quantity: int, unit_price: int = 100) -> int:
    return quantity * unit_price


def persist_total(total: int, file_path: str) -> None:
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(str(total))
