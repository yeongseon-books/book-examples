from pydantic import BaseModel, ValidationError, field_validator


class Product(BaseModel):
    name: str
    price: float
    quantity: int

    @field_validator('price')
    @classmethod
    def price_must_be_positive(cls, value: float) -> float:
        if value <= 0:
            raise ValueError('price must be positive')
        return value


def safe_create_product(data: dict) -> tuple[bool, str]:
    try:
        product = Product(**data)
        return True, f'{product.name}:{product.price}:{product.quantity}'
    except ValidationError as exc:
        return False, str(exc).splitlines()[0]
