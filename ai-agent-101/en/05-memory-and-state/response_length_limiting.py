"""Generated from book-content article."""

from openai import OpenAI


class LengthControlledAgent:
    """Agent with response length control"""

    def __init__(self, api_key: str, max_context_tokens: int = 6000, max_response_tokens: int = 1000):
        self.client = OpenAI(api_key=api_key)
        self.max_context_tokens = max_context_tokens
        self.max_response_tokens = max_response_tokens
        self.memory = TokenAwareMemory(
            system_prompt="You are a helpful assistant. Keep responses concise.",
            model="gpt-4o",
            max_tokens=max_context_tokens
        )

    def run(self, user_message: str) -> str:
        """Run agent (with response length limit)"""
        self.memory.add_message("user", user_message)

        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=self.memory.get_context(),
            max_tokens=self.max_response_tokens,  # Response length limit
            temperature=0.7
        )

        assistant_message = response.choices[0].message.content
        self.memory.add_message("assistant", assistant_message)

        return assistant_message

# Usage example
agent = LengthControlledAgent(
    api_key="your-api-key",
    max_context_tokens=6000,  # 6000 tokens for context
    max_response_tokens=1000  # 1000 tokens for response
)

response = agent.run("Explain Python's advantages in detail")
# Response won't exceed 1000 tokens
