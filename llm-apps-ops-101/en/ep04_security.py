"""Llm Apps Ops 101 - Episode 4: Security."""

from __future__ import annotations

import re
from dataclasses import dataclass

from en.common import build_logger

logger = build_logger("en.security")

BLOCKED_PATTERNS = [r"ignore previous instructions", r"system prompt", r"api[_ -]?key"]
SENSITIVE_PATTERNS = {
    "email": re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
    "phone": re.compile(r"\+?\d[\d -]{7,}\d"),
}


@dataclass(slots=True)
class ValidationResult:
    """Validation result."""

    accepted: bool
    reason: str


class InputValidator:
    """Input validator."""

    def __init__(self, max_length: int = 500) -> None:
        self.max_length = max_length

    def validate(self, text: str) -> ValidationResult:
        """Validate."""
        if not text.strip():
            return ValidationResult(False, "Input is empty.")
        if len(text) > self.max_length:
            return ValidationResult(
                False,
                f"Input is too long. Maximum length is {self.max_length} characters.",
            )
        lowered = text.lower()
        for pattern in BLOCKED_PATTERNS:
            if re.search(pattern, lowered):
                return ValidationResult(
                    False, "Potential prompt injection pattern detected."
                )
        return ValidationResult(True, "Input validation passed.")


class OutputFilter:
    """Output filter."""

    def redact(self, text: str) -> str:
        """Redact."""
        filtered = text
        for name, pattern in SENSITIVE_PATTERNS.items():
            replaced = pattern.sub(f"[{name}-redacted]", filtered)
            if replaced != filtered:
                logger.info(
                    "Sensitive data was removed from the output.",
                    extra={"payload": {"kind": name}},
                )
            filtered = replaced
        return filtered


def demo() -> None:
    """Demo."""
    validator = InputValidator()
    filter_ = OutputFilter()
    prompt = "Write a maintenance notice for the user whose email is admin@example.com."
    validation = validator.validate(prompt)
    print(validation)
    print(
        filter_.redact("Contact admin@example.com or call +1 415 555 0100 for support.")
    )


if __name__ == "__main__":
    demo()
