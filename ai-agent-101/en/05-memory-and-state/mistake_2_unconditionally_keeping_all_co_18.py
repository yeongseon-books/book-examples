"""Generated from book-content article."""

class MemoryWithLimit:
    def __init__(self, max_messages=10):
        self.messages = []
        self.max_messages = max_messages

    def add_message(self, role, content):
        self.messages.append({"role": role, "content": content})

        # Apply sliding window when exceeding limit
        if len(self.messages) > self.max_messages:
            self.messages = self.messages[-self.max_messages:]
