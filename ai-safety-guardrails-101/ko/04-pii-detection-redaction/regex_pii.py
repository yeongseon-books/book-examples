"""Generated from book-content article."""

import re

PII_PATTERNS = {
    "us_ssn": re.compile(r"\b\d{3}-\d{2}-\d{4}\b"),
    "us_phone": re.compile(r"\b(?:\+?1[-\s.]?)?\(?\d{3}\)?[-\s.]?\d{3}[-\s.]?\d{4}\b"),
    "email": re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b"),
    "credit_card": re.compile(r"\b(?:\d[ -]*?){13,19}\b"),
    "ipv4": re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b"),
}

def detect_pii(text: str) -> list[tuple[str, int, int, str]]:
    """Returns list of (category, start, end, value)."""
    found = []
    for cat, pat in PII_PATTERNS.items():
        for m in pat.finditer(text):
            found.append((cat, m.start(), m.end(), m.group()))
    return found

text = "Reach me at 555-123-4567 or alice@example.com."
print(detect_pii(text))
# [('us_phone', 12, 24, '555-123-4567'), ('email', 28, 45, 'alice@example.com')]
