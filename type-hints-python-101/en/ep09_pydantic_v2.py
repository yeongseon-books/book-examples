"""Type Hints Python 101 - Episode 9: Pydantic v2."""

from pydantic import BaseModel, ValidationError, field_validator


class Product(BaseModel):
    """Product."""

    name: str
    price: float
    quantity: int

    @field_validator("price")
    @classmethod
    def price_must_be_positive(cls, value: float) -> float:
        """Price must be positive."""
        if value <= 0:
            raise ValueError("price must be positive")
        return value


def safe_create_product(data: dict) -> tuple[bool, str]:
    """Safe create product."""
    try:
        product = Product(**data)
        return True, f"{product.name}:{product.price}:{product.quantity}"
    except ValidationError as exc:
        return False, str(exc).splitlines()[0]
