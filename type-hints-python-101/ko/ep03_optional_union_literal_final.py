from typing import Final, Literal

VERSION: Final[str] = "1.0"


def parse_maybe_int(value: int | str | None) -> int | None:
    if value is None:
        return None
    if isinstance(value, int):
        return value
    return int(value) if value.isdigit() else None


def traffic_action(light: Literal["red", "yellow", "green"]) -> str:
    mapping = {"red": "stop", "yellow": "slow", "green": "go"}
    return mapping[light]
