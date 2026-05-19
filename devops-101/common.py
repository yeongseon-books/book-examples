"""Shared utilities and domain models for Devops 101."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone


def now_iso() -> str:
    """Now iso."""
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


@dataclass(frozen=True)
class Event:
    """Event."""

    timestamp: datetime
    kind: str
    deployment_id: str
    metadata: dict[str, object]


class EventLog:
    """Event log."""

    def __init__(self, events: list[Event] | None = None) -> None:
        self._events = sorted(events or [], key=lambda e: e.timestamp)

    def add(self, event: Event) -> None:
        """Add."""
        self._events.append(event)
        self._events.sort(key=lambda e: e.timestamp)

    def by_kind(self, kind: str) -> list[Event]:
        """By kind."""
        return [event for event in self._events if event.kind == kind]

    @property
    def events(self) -> list[Event]:
        """Events."""
        return list(self._events)


class MockCommandRunner:
    """Mock command runner."""

    def __init__(self, outcomes: dict[str, tuple[int, str, str]] | None = None) -> None:
        self.outcomes = outcomes or {}
        self.calls: list[str] = []

    def run(self, command: str) -> tuple[int, str, str]:
        """Run."""
        self.calls.append(command)
        return self.outcomes.get(command, (0, "ok", ""))


def parse_iso(value: str) -> datetime:
    """Parse iso."""
    return datetime.fromisoformat(value)
