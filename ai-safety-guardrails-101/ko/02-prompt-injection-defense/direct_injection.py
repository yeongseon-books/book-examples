"""Generated from book-content article."""

import re

DIRECT_INJECTION_PATTERNS = [
    r"ignore\s+(previous|above|prior)\s+(instructions?|messages?|prompts?)",
    r"disregard\s+the\s+(above|previous)",
    r"you\s+are\s+now\s+(?:dan|jailbroken|unrestricted)",
    r"repeat\s+(the\s+)?(text|message|prompt)\s+above",
    r"</system>|<\|im_start\|>",
]

def detect_direct_injection(text: str) -> str | None:
    lowered = text.lower()
    for pattern in DIRECT_INJECTION_PATTERNS:
        if re.search(pattern, lowered, re.IGNORECASE):
            return pattern
    return None
