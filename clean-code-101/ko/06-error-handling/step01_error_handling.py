"""Clean Code 101 - Episode 1: Error handling."""

import random
import time
from dataclasses import dataclass


class ConfigError(Exception):
    """Config error."""

    pass


@dataclass(frozen=True)
class Result:
    """Result."""

    ok: bool
    value: object = None
    error: str = ""


def parse_int(text: str) -> Result:
    """Parse int."""
    try:
        return Result(True, int(text))
    except ValueError as err:
        return Result(False, error=str(err))


def transfer(amount: int) -> str:
    """Transfer."""
    if amount <= 0:
        raise ValueError("amount must be positive")
    return "ok"


def with_retry(fn, attempts: int = 3):
    """With retry."""
    for index in range(attempts):
        try:
            return fn()
        except TimeoutError:
            if index == attempts - 1:
                raise
            time.sleep((2**index) + random.random())
