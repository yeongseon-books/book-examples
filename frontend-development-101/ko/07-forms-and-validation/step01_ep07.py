"""Frontend Development 101 - 7편: forms and validation 예제."""

from __future__ import annotations

from common import FormValidator


def run_demo(email: str, password: str) -> dict[str, str | None]:
    """데모를 실행합니다."""
    validator = FormValidator()
    return {
        "email": validator.validate_email(email),
        "password": validator.validate_password(password),
    }
