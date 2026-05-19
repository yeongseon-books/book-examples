"""Secure Coding 101 - Episode 3: Authentication."""

import hashlib
import secrets

from common import assert_demo


def insecure_hash(password: str) -> str:
    """Insecure hash."""
    return hashlib.sha256(password.encode()).hexdigest()


def safe_hash(password: str, salt: bytes) -> bytes:
    """Safe hash."""
    return hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 200_000)


def issue_session_token() -> str:
    """Issue session token."""
    return secrets.token_urlsafe(32)


def run_demo():
    """Run demo."""
    insecure_detected = insecure_hash("pw") == insecure_hash("pw")
    salt = secrets.token_bytes(16)
    safe_ok = (
        safe_hash("pw", salt) == safe_hash("pw", salt)
        and len(issue_session_token()) > 20
    )
    return assert_demo(insecure_detected, safe_ok)
