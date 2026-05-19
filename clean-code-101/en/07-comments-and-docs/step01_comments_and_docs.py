# The payment partner sometimes returns HTTP 200 with a failed status in body,
# so this check uses payload status instead of response code.
def is_paid(response: dict[str, object]) -> bool:
    return response.get("status") == "PAID"


def discount(price: int, rate: float) -> int:
    """Return discounted price.

    Args:
        price: Integer price in KRW.
        rate: Discount rate in range 0..1.

    Returns:
        Rounded integer price.

    Raises:
        ValueError: If rate is outside 0..1.
    """
    if not 0 <= rate <= 1:
        raise ValueError("rate out of range")
    return int(price * (1 - rate))
