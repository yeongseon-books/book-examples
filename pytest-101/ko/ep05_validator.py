"""Pytest 101 - Episode 5: Validator."""


def is_valid_password(password: str) -> bool:
    """Is valid password."""
    return (
        len(password) >= 8
        and any(ch.isupper() for ch in password)
        and any(ch.islower() for ch in password)
        and any(ch.isdigit() for ch in password)
    )
