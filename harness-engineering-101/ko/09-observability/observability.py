"""Generated from book-content article."""

import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class Span:
    span_id: str
    trace_id: str
    parent_id: str | None
    name: str
    started_at: datetime
    ended_at: datetime | None = None
    attributes: dict[str, Any] = field(default_factory=dict)
    events: list[dict] = field(default_factory=list)
    status: str = "ok"
