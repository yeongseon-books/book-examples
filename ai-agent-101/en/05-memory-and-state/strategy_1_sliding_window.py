"""Generated from book-content article."""

from typing import Dict, List


class SlidingWindowMemory:
    """Sliding window: retain only recent N messages"""

    def __init__(self, system_prompt: str, max_messages: int = 10):
        self.system_prompt = system_prompt
        self.max_messages = max_messages  # excluding system prompt
        self.messages: list[dict[str, str]] = [
            {"role": "system", "content": system_prompt}
        ]

    def add_message(self, role: str, content: str):
        """Add message"""
        self.messages.append({"role": role, "content": content})

        # Keep only recent N messages (excluding system prompt)
        if len(self.messages) - 1 > self.max_messages:
            # Keep system prompt, remove oldest 2 messages (user + assistant pair)
            self.messages = [self.messages[0]] + self.messages[3:]

    def get_context(self) -> list[dict[str, str]]:
        """Return current context"""
        return self.messages

# Usage example
memory = SlidingWindowMemory(system_prompt="You are a helpful assistant.", max_messages=4)

memory.add_message("user", "Question 1")
memory.add_message("assistant", "Answer 1")
memory.add_message("user", "Question 2")
memory.add_message("assistant", "Answer 2")
memory.add_message("user", "Question 3")  # Question 1, Answer 1 removed

print(f"Message count: {len(memory.get_context())}")  # 5 (system + recent 4)
