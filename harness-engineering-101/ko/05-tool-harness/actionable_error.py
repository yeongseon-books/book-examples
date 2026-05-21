"""Generated from book-content article."""

from enum import Enum
from dataclasses import dataclass

class ErrorCode(Enum):
    INVALID_INPUT = "invalid_input"
    NOT_FOUND = "not_found"
    PERMISSION_DENIED = "permission_denied"
    RATE_LIMITED = "rate_limited"
    UPSTREAM_TIMEOUT = "upstream_timeout"

@dataclass
class ToolError(Exception):
    code: ErrorCode
    what: str
    why: str
    how: str
    retryable: bool

    def to_agent_message(self) -> str:
        return f"""Tool call failed.
Code: {self.code.value}
What: {self.what}
Why: {self.why}
How to fix: {self.how}
Retryable: {self.retryable}"""

def get_user(user_id: str) -> dict:
    if not user_id.startswith("usr_"):
        raise ToolError(
            code=ErrorCode.INVALID_INPUT,
            what="user_id format is invalid",
            why=f"user_id must start with 'usr_', got: {user_id}",
            how="Call list_users to find a valid user_id, or check the format.",
            retryable=False,
        )
    raise ToolError(
        code=ErrorCode.NOT_FOUND,
        what=f"user not found: {user_id}",
        why="No user with this id exists in the database.",
        how="Verify the id with list_users, or create_user if intended.",
        retryable=False,
    )
