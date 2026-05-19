"""Llm Apps Ops 101 - Episode 4: Security."""

from __future__ import annotations

import re
from dataclasses import dataclass

from ko.common import build_logger

logger = build_logger("ko.security")

BLOCKED_PATTERNS = [r"ignore previous instructions", r"system prompt", r"api[_ -]?key"]
SENSITIVE_PATTERNS = {
    "email": re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
    "phone": re.compile(r"01[0-9]-?\d{3,4}-?\d{4}"),
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
            return ValidationResult(False, "입력이 비어 있습니다.")
        if len(text) > self.max_length:
            return ValidationResult(
                False, f"입력이 너무 깁니다. 최대 {self.max_length}자까지 허용합니다."
            )
        lowered = text.lower()
        for pattern in BLOCKED_PATTERNS:
            if re.search(pattern, lowered):
                return ValidationResult(
                    False, "프롬프트 인젝션으로 의심되는 표현이 포함되어 있습니다."
                )
        return ValidationResult(True, "입력이 검증을 통과했습니다.")


class OutputFilter:
    """Output filter."""

    def redact(self, text: str) -> str:
        """Redact."""
        filtered = text
        for name, pattern in SENSITIVE_PATTERNS.items():
            replaced = pattern.sub(f"[{name}-redacted]", filtered)
            if replaced != filtered:
                logger.info(
                    "민감 정보가 출력에서 제거되었습니다.",
                    extra={"payload": {"kind": name}},
                )
            filtered = replaced
        return filtered


def demo() -> None:
    """Demo."""
    validator = InputValidator()
    filter_ = OutputFilter()
    prompt = "사용자 이메일이 admin@example.com 일 때 시스템 점검 안내를 써 주세요."
    validation = validator.validate(prompt)
    print(validation)
    print(
        filter_.redact("연락처는 010-1234-5678 이고 이메일은 admin@example.com 입니다.")
    )


if __name__ == "__main__":
    demo()
