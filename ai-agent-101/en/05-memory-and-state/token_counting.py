"""Generated from book-content article."""

import tiktoken
from typing import List, Dict

class TokenAwareMemory:
    """Token-tracking memory"""
    
    def __init__(self, system_prompt: str, model: str = "gpt-4o", max_tokens: int = 8000):
        self.model = model
        self.max_tokens = max_tokens
        self.encoding = tiktoken.encoding_for_model(model)
        self.messages: List[Dict[str, str]] = [
            {"role": "system", "content": system_prompt}
        ]
    
    def count_tokens(self, text: str) -> int:
        """Calculate text token count"""
        return len(self.encoding.encode(text))
    
    def get_total_tokens(self) -> int:
        """Get total token count of current context"""
        total = 0
        for msg in self.messages:
            total += self.count_tokens(msg["content"])
            total += 4  # message structure overhead (role, content separators, etc.)
        return total
    
    def can_add_message(self, content: str) -> bool:
        """Check if message can be added"""
        new_tokens = self.count_tokens(content) + 4
        return self.get_total_tokens() + new_tokens <= self.max_tokens
    
    def add_message(self, role: str, content: str):
        """Add message (check token limit)"""
        if not self.can_add_message(content):
            # Remove old messages when exceeding token limit
            self._trim_messages()
        
        self.messages.append({"role": role, "content": content})
    
    def _trim_messages(self):
        """Remove old messages (keep system prompt)"""
        if len(self.messages) > 1:
            # Remove oldest user-assistant pair
            self.messages = [self.messages[0]] + self.messages[3:]
    
    def get_context(self) -> List[Dict[str, str]]:
        """Return current context"""
        return self.messages

# Usage example
memory = TokenAwareMemory(
    system_prompt="You are a helpful assistant.",
    model="gpt-4o",
    max_tokens=8000
)

memory.add_message("user", "long question" * 1000)  # very long message
print(f"Total tokens: {memory.get_total_tokens()}")

# Check token limit
if memory.can_add_message("next question"):
    memory.add_message("user", "next question")
else:
    print("Token limit exceeded, old messages will be removed.")
