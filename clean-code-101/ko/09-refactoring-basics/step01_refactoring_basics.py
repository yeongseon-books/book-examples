"""Clean Code 101 - Episode 1: Refactoring basics."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Item:
    """Item."""

    price: int
    qty: int


@dataclass(frozen=True)
class Order:
    """Order."""

    items: list[Item]
    coupon: bool
    member: bool


def subtotal(items: list[Item]) -> int:
    """Subtotal."""
    return sum(item.price * item.qty for item in items)


def with_coupon(amount: float, coupon: bool) -> float:
    """With coupon."""
    return amount - 10 if coupon else amount


def with_member(amount: float, member: bool) -> float:
    """With member."""
    return amount * 0.9 if member else amount


def order_total(order: Order) -> float:
    """Order total."""
    amount = subtotal(order.items)
    amount = with_coupon(amount, order.coupon)
    amount = with_member(amount, order.member)
    return amount
