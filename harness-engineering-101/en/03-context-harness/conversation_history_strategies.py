"""Generated from book-content article."""

from dataclasses import dataclass
from typing import Literal


@dataclass
class Message:
    role: Literal["user", "assistant", "tool"]
    content: str
    tokens: int

class HistoryManager:
    """Manages conversation history within a token budget."""

    def __init__(self, max_tokens: int, strategy: str = "summarize"):
        self.max_tokens = max_tokens
        self.strategy = strategy
        self.messages: list[Message] = []
        self.summary: str = ""

    def add(self, msg: Message) -> None:
        self.messages.append(msg)
        self._compact()

    def _compact(self) -> None:
        total = sum(m.tokens for m in self.messages)
        if total <= self.max_tokens:
            return

        if self.strategy == "sliding":
            while sum(m.tokens for m in self.messages) > self.max_tokens:
                self.messages.pop(0)
        elif self.strategy == "summarize":
            old = self.messages[: len(self.messages) // 2]
            self.summary = self._summarize(old)
            self.messages = self.messages[len(self.messages) // 2 :]

    def _summarize(self, messages: list[Message]) -> str:
        # In practice, summarize with an LLM
        return f"[Summary: {len(messages)} turns]"

    def to_context(self) -> list[dict]:
        result = []
        if self.summary:
            result.append({"role": "system", "content": self.summary})
        result.extend({"role": m.role, "content": m.content} for m in self.messages)
        return result
