"""Type Hints Python 101 - Episode 3: Optional union literal final."""

from typing import Final, Literal

VERSION: Final[str] = "1.0"


def parse_maybe_int(value: int | str | None) -> int | None:
    """Parse maybe int."""
    if value is None:
        return None
    if isinstance(value, int):
        return value
    return int(value) if value.isdigit() else None


def traffic_action(light: Literal["red", "yellow", "green"]) -> str:
    """Traffic action."""
    mapping = {"red": "stop", "yellow": "slow", "green": "go"}
    return mapping[light]
