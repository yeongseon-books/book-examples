"""Generated from book-content article."""

import time
from dataclasses import dataclass, field

@dataclass
class ResourceMeter:
    """Tracks resource use and enforces caps."""
    max_tokens: int = 50_000
    max_tool_calls: int = 20
    max_wall_seconds: float = 60.0

    used_tokens: int = 0
    used_tool_calls: int = 0
    started_at: float = field(default_factory=time.time)

    def record_tokens(self, n: int) -> None:
        self.used_tokens += n
        if self.used_tokens > self.max_tokens:
            raise ResourceExhausted(f"token budget exceeded: {self.used_tokens}/{self.max_tokens}")

    def record_tool_call(self) -> None:
        self.used_tool_calls += 1
        if self.used_tool_calls > self.max_tool_calls:
            raise ResourceExhausted(f"tool call budget exceeded: {self.used_tool_calls}/{self.max_tool_calls}")

    def check_wall_clock(self) -> None:
        elapsed = time.time() - self.started_at
        if elapsed > self.max_wall_seconds:
            raise ResourceExhausted(f"wall clock exceeded: {elapsed:.1f}s")

class ResourceExhausted(Exception):
    pass
