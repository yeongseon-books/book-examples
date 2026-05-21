"""Generated from book-content article."""

def classify_cause(evidence_count: int, repeated: bool) -> str:
    if evidence_count >= 3 and repeated:
        return "root_cause"
    if evidence_count >= 1:
        return "trigger_or_factor"
    return "unknown"


def actionable(text: str) -> bool:
    verbs = ("add ", "fix ", "remove ", "test ", "enforce ")
    return text.startswith(verbs)
