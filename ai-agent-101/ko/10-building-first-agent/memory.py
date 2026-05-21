"""Generated from book-content article."""

class ConversationMemory:
    """Sliding window conversation memory."""

    def __init__(self, system_prompt: str, max_messages: int = 20):
        self.system_prompt = system_prompt
        self.max_messages = max_messages
        self.messages: list[dict[str, Any]] = []

    def add(self, role: str, content: str, **extra: Any) -> None:
        """Append a message."""
        msg = {"role": role, "content": content, **extra}
        self.messages.append(msg)
        if len(self.messages) > self.max_messages:
            self.messages = self.messages[-self.max_messages:]

    def to_openai(self) -> list[dict[str, Any]]:
        """Return messages in OpenAI Chat Completions format."""
        return [{"role": "system", "content": self.system_prompt}] + self.messages
