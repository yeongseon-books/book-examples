"""Generated from book-content article."""

ANCHORS = ("detected", "acknowledged", "mitigated", "resolved")


def extract_anchor(line: str) -> str | None:
    lower = line.lower()
    for a in ANCHORS:
        if a in lower:
            return a
    return None
