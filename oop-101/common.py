from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


def now_stamp() -> str:
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")


@dataclass
class Event:
    name: str
    payload: dict[str, object]


class InMemoryLogger:
    def __init__(self) -> None:
        self.events: list[Event] = []

    def record(self, name: str, payload: dict[str, object]) -> None:
        self.events.append(Event(name=name, payload=payload))
