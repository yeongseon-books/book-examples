"""Generated from book-content article."""

from dataclasses import dataclass


@dataclass
class ContextBudget:
    """Token budget allocation for the context window."""
    total_tokens: int = 200_000
    system_prompt: int = 2_000
    task_spec: int = 1_000
    conversation_history: int = 5_000
    retrieved_context: int = 10_000
    tool_schemas: int = 3_000
    response_buffer: int = 4_000  # Leave room for the response

    def remaining(self) -> int:
        used = (
            self.system_prompt
            + self.task_spec
            + self.conversation_history
            + self.retrieved_context
            + self.tool_schemas
            + self.response_buffer
        )
        return self.total_tokens - used

budget = ContextBudget()
assert budget.remaining() > 0, "Budget exceeds the window"
