"""Generated from book-content article."""

from dataclasses import dataclass
from enum import Enum

class FailureMode(Enum):
    TRANSIENT = "transient"
    DETERMINISTIC = "deterministic"
    REASONING = "reasoning"

@dataclass
class FailureClassification:
    mode: FailureMode
    feedback: str
    retry_after: float = 0.0

def classify_failure(error: Exception) -> FailureClassification:
    if isinstance(error, TimeoutError):
        return FailureClassification(FailureMode.TRANSIENT, "", retry_after=1.0)
    if isinstance(error, ToolError) and error.code == ErrorCode.RATE_LIMITED:
        return FailureClassification(FailureMode.TRANSIENT, "", retry_after=5.0)
    if isinstance(error, ToolError) and error.code == ErrorCode.INVALID_INPUT:
        return FailureClassification(FailureMode.REASONING, error.to_agent_message())
    if isinstance(error, PolicyViolation):
        return FailureClassification(FailureMode.REASONING, f"Policy violation: {error}. Try a different approach.")
    return FailureClassification(FailureMode.DETERMINISTIC, str(error))
