"""Containers 101 - Episode 8: Container security."""

from __future__ import annotations

import re

SECRET_PATTERN = re.compile(r"(PASSWORD|SECRET|TOKEN)=\S+", re.IGNORECASE)


def scan_security(dockerfile: str, manifest_ref: str) -> list[str]:
    """Scan security."""
    issues: list[str] = []
    upper = dockerfile.upper()
    if "USER " not in upper:
        issues.append("Missing USER directive")
    if "USER ROOT" in upper:
        issues.append("Container runs as root")
    if ":LATEST" in upper or manifest_ref.endswith(":latest"):
        issues.append("Using latest tag harms reproducibility")
    if "EXPOSE 22" in upper or "EXPOSE 2375" in upper:
        issues.append("Sensitive port exposed")
    if SECRET_PATTERN.search(dockerfile):
        issues.append("Potential hardcoded secret in ENV")
    return issues
