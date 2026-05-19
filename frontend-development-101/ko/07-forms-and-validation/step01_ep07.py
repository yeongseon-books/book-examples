"""Frontend Development 101 - Episode 1: Ep07."""

from __future__ import annotations

from common import FormValidator


def run_demo(email: str, password: str) -> dict[str, str | None]:
    """Run demo."""
    validator = FormValidator()
    return {
        "email": validator.validate_email(email),
        "password": validator.validate_password(password),
    }
