"""Generated from book-content article."""

from dataclasses import dataclass
from datetime import datetime, timezone

@dataclass
class TimelineEvent:
    ts: str
    kind: str  # fact | note
    source: str
    text: str


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def make_event(kind: str, source: str, text: str) -> TimelineEvent:
    return TimelineEvent(ts=utc_now(), kind=kind, source=source, text=text)


def to_line(event: TimelineEvent) -> str:
    return f"{event.ts} {event.kind}: [{event.source}] {event.text}"
