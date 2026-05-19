"""Shared utilities and domain models for Secure Coding 101."""

from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass
class DemoResult:
    """Demo result."""

    insecure_detected: bool
    safe_ok: bool


def assert_demo(insecure_detected: bool, safe_ok: bool) -> DemoResult:
    """Assert demo."""
    assert insecure_detected, "Expected insecure pattern to be detectable"
    assert safe_ok, "Expected safe pattern to work"
    return DemoResult(insecure_detected=insecure_detected, safe_ok=safe_ok)


EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
SSN_RE = re.compile(r"\b\d{3}-\d{2}-\d{4}\b")
TOKEN_RE = re.compile(r"\b(?:tok|token|api_key|secret)[=:]\S+", re.IGNORECASE)
