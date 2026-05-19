from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    is_active: bool
    is_member: bool


@dataclass(frozen=True)
class Product:
    price: int
    in_stock: bool


def price(user: User | None, product: Product | None) -> float | None:
    if user is None or not user.is_active:
        return None
    if product is None or not product.in_stock:
        return None
    rate = 0.9 if user.is_member else 1.0
    return product.price * rate


GRADES = [(90, "A"), (80, "B"), (70, "C"), (0, "F")]


def grade(score: int) -> str:
    return next(letter for min_score, letter in GRADES if score >= min_score)
