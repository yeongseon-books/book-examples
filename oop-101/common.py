"""Shared utilities and domain models for Oop 101."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


def now_stamp() -> str:
    """Now stamp."""
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")


@dataclass
class Event:
    """Event."""

    name: str
    payload: dict[str, object]


class InMemoryLogger:
    """In memory logger."""

    def __init__(self) -> None:
        self.events: list[Event] = []

    def record(self, name: str, payload: dict[str, object]) -> None:
        """Record."""
        self.events.append(Event(name=name, payload=payload))
