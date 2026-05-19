from dataclasses import dataclass
import random
import time


class ConfigError(Exception):
    pass


@dataclass(frozen=True)
class Result:
    ok: bool
    value: object = None
    error: str = ""


def parse_int(text: str) -> Result:
    try:
        return Result(True, int(text))
    except ValueError as err:
        return Result(False, error=str(err))


def transfer(amount: int) -> str:
    if amount <= 0:
        raise ValueError("amount must be positive")
    return "ok"


def with_retry(fn, attempts: int = 3):
    for index in range(attempts):
        try:
            return fn()
        except TimeoutError:
            if index == attempts - 1:
                raise
            time.sleep((2**index) + random.random())
