def discount_price(price: float, rate: float) -> float:
    if not (0 <= rate <= 1):
        raise ValueError("rate must be between 0 and 1")
    return round(price * (1 - rate), 2)


def classify_score(score: int) -> str:
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    return "D"
