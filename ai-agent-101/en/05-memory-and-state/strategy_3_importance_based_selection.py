"""Generated from book-content article."""

from typing import Dict, List, Tuple


class ImportanceBasedMemory:
    """Importance-based memory: retain only important messages"""

    def __init__(self, system_prompt: str, max_messages: int = 10):
        self.system_prompt = system_prompt
        self.max_messages = max_messages
        self.messages: list[tuple[dict[str, str], float]] = []  # (message, importance_score)

    def _calculate_importance(self, content: str) -> float:
        """Calculate message importance (simple heuristic)"""
        importance = 0.5  # base score

        # Tool call results are important
        if "tool_calls" in content or "function_call" in content:
            importance += 0.3

        # Questions are important
        if "?" in content or "how" in content.lower() or "what" in content.lower():
            importance += 0.2

        # Short messages are less important
        if len(content) < 20:
            importance -= 0.1

        return min(1.0, max(0.0, importance))

    def add_message(self, role: str, content: str):
        """Add message (calculate importance score)"""
        message = {"role": role, "content": content}
        importance = self._calculate_importance(content)

        self.messages.append((message, importance))

        # Remove low-importance messages when too many
        if len(self.messages) > self.max_messages:
            # Sort by importance
            self.messages.sort(key=lambda x: x[1], reverse=True)
            # Keep top max_messages only
            self.messages = self.messages[:self.max_messages]
            # Re-sort by time (maintain conversation flow)
            self.messages.sort(key=lambda x: self.messages.index(x))

    def get_context(self) -> list[dict[str, str]]:
        """Return current context"""
        return [
            {"role": "system", "content": self.system_prompt}
        ] + [msg for msg, _ in self.messages]

# Usage example
memory = ImportanceBasedMemory(system_prompt="You are a helpful assistant.", max_messages=5)

memory.add_message("user", "Hi")  # Low importance (short)
memory.add_message("assistant", "Hello!")  # Low importance
memory.add_message("user", "How to call APIs in Python?")  # High importance (question)
memory.add_message("assistant", "Use requests library: import requests...")  # Medium importance
memory.add_message("user", "tool_calls: search_api")  # High importance (tool call)
memory.add_message("assistant", "Search results: ...")  # Medium importance
memory.add_message("user", "Thanks")  # Low importance (short) → likely to be removed

context = memory.get_context()
print(f"Retained messages: {len(context) - 1}")  # excluding system
