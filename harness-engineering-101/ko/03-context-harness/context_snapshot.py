"""Generated from book-content article."""

import hashlib
import json
from datetime import datetime
from dataclasses import dataclass, field

@dataclass
class ContextSnapshot:
    """Complete snapshot of context just before inference."""
    timestamp: str
    task_id: str
    messages: list[dict]
    tools: list[dict]
    model: str
    temperature: float
    snapshot_hash: str = ""

    def __post_init__(self) -> None:
        payload = json.dumps(
            {"messages": self.messages, "tools": self.tools, "model": self.model},
            sort_keys=True,
        )
        self.snapshot_hash = hashlib.sha256(payload.encode()).hexdigest()[:16]

def capture_snapshot(task_id: str, messages: list[dict], tools: list[dict], model: str) -> ContextSnapshot:
    return ContextSnapshot(
        timestamp=datetime.utcnow().isoformat(),
        task_id=task_id,
        messages=messages,
        tools=tools,
        model=model,
        temperature=0.0,
    )
