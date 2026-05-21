"""Generated from book-content article."""

from collections.abc import Callable
from dataclasses import dataclass

@dataclass
class Tool:
    name: str
    description: str
    handler: Callable
    danger_level: int  # 0 (safe) to 5 (destructive)

class ToolRegistry:
    """Registers all tools and filters them per task."""

    def __init__(self):
        self._tools: dict[str, Tool] = {}

    def register(self, tool: Tool) -> None:
        self._tools[tool.name] = tool

    def expose(self, allowed_names: set[str], max_danger: int = 2) -> list[Tool]:
        """Expose only allowed tools within the danger threshold."""
        return [
            t for name, t in self._tools.items()
            if name in allowed_names and t.danger_level <= max_danger
        ]

registry = ToolRegistry()
registry.register(Tool("read_db", "Query DB", lambda q: ..., danger_level=0))
registry.register(Tool("write_db", "Modify DB", lambda r: ..., danger_level=4))
registry.register(Tool("send_email", "Send email", lambda m: ..., danger_level=3))

# Task: produce an analytical report — read only
exposed = registry.expose(allowed_names={"read_db"}, max_danger=2)
assert all(t.name == "read_db" for t in exposed)
