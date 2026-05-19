from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


@dataclass(frozen=True)
class Event:
    timestamp: datetime
    kind: str
    deployment_id: str
    metadata: dict[str, object]


class EventLog:
    def __init__(self, events: list[Event] | None = None) -> None:
        self._events = sorted(events or [], key=lambda e: e.timestamp)

    def add(self, event: Event) -> None:
        self._events.append(event)
        self._events.sort(key=lambda e: e.timestamp)

    def by_kind(self, kind: str) -> list[Event]:
        return [event for event in self._events if event.kind == kind]

    @property
    def events(self) -> list[Event]:
        return list(self._events)


class MockCommandRunner:
    def __init__(self, outcomes: dict[str, tuple[int, str, str]] | None = None) -> None:
        self.outcomes = outcomes or {}
        self.calls: list[str] = []

    def run(self, command: str) -> tuple[int, str, str]:
        self.calls.append(command)
        return self.outcomes.get(command, (0, "ok", ""))


def parse_iso(value: str) -> datetime:
    return datetime.fromisoformat(value)
