"""Generated from book-content article."""

from typing import List, Dict

class ShortTermMemory:
    """Short-term memory: retained only during current session"""

    def __init__(self, system_prompt: str):
        self.messages: List[Dict[str, str]] = [
            {"role": "system", "content": system_prompt}
        ]

    def add_user_message(self, content: str):
        """Add user message"""
        self.messages.append({"role": "user", "content": content})

    def add_assistant_message(self, content: str):
        """Add agent response"""
        self.messages.append({"role": "assistant", "content": content})

    def get_context(self) -> List[Dict[str, str]]:
        """Return current context"""
        return self.messages

    def clear(self):
        """Clear memory on session end"""
        system_msg = self.messages[0]
        self.messages = [system_msg]

# Usage example
memory = ShortTermMemory(system_prompt="You are a helpful assistant.")

memory.add_user_message("What's the weather today?")
memory.add_assistant_message("Today's weather in Seoul is sunny.")

memory.add_user_message("How about tomorrow?")
# Agent remembers previous conversation ("weather today") and understands "tomorrow" refers to weather

print(f"Message count: {len(memory.get_context())}")  # 4 (system + user + assistant + user)
