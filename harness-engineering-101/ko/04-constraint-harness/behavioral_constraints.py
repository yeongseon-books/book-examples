"""Generated from book-content article."""

import re
from typing import Protocol


class OutputPolicy(Protocol):
    def check(self, output: str) -> tuple[bool, str]:
        """Returns (passed, reason)."""
        ...

class NoSecrets:
    """Checks output contains no secrets."""
    def check(self, output: str) -> tuple[bool, str]:
        if re.search(r"sk-[a-zA-Z0-9]{20,}", output):
            return False, "API key detected"
        if re.search(r"\b\d{3}-\d{2}-\d{4}\b", output):
            return False, "SSN detected"
        return True, ""

class ApprovedTone:
    """Allows only approved tone."""
    BANNED_PHRASES = {"absolutely guaranteed", "100% safe", "no risk"}

    def check(self, output: str) -> tuple[bool, str]:
        lower = output.lower()
        for phrase in self.BANNED_PHRASES:
            if phrase in lower:
                return False, f"banned phrase: {phrase}"
        return True, ""

def enforce_policies(output: str, policies: list[OutputPolicy]) -> None:
    for p in policies:
        ok, reason = p.check(output)
        if not ok:
            raise PolicyViolation(reason)

class PolicyViolation(Exception):
    pass
