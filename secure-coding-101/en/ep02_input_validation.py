"""Secure Coding 101 - Episode 2: Input validation."""

import re

from common import assert_demo

USERNAME_RE = re.compile(r"^[a-z0-9_]{3,16}$")
ROLE_ALLOWLIST = {"viewer", "editor", "admin"}


def insecure_validate(payload: dict) -> bool:
    """Insecure validate."""
    return True


def safe_validate(payload: dict) -> bool:
    """Safe validate."""
    username = payload.get("username", "")
    role = payload.get("role", "")
    if not isinstance(username, str) or not USERNAME_RE.match(username):
        return False
    return role in ROLE_ALLOWLIST


def run_demo():
    """Run demo."""
    bad = {"username": "A!", "role": "root"}
    good = {"username": "safe_user", "role": "viewer"}
    insecure_detected = insecure_validate(bad) is True
    safe_ok = safe_validate(bad) is False and safe_validate(good) is True
    return assert_demo(insecure_detected, safe_ok)
