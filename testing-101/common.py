from typing import Callable


def clamp(value: float, min_value: float, max_value: float) -> float:
    return max(min_value, min(value, max_value))


def safe_int(text: str, default: int = 0) -> int:
    try:
        return int(text)
    except (TypeError, ValueError):
        return default


def run_with_exit_code(fn: Callable[[], bool]) -> int:
    return 0 if fn() else 1
