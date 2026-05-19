from common import clamp


def calculate_final_price(base_price: float, discount_rate: float) -> float:
    rate = clamp(discount_rate, 0.0, 1.0)
    return round(base_price * (1.0 - rate), 2)
