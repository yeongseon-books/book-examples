"""Generated from book-content article."""

THRESHOLDS = {
    "violence": 0.5,
    "self-harm": 0.3,  # stricter
    "hate": 0.4,
    "sexual": 0.6,
}

def is_safe(scores: dict, thresholds: dict = THRESHOLDS) -> bool:
    for category, max_score in thresholds.items():
        if scores.get(category, 0) > max_score:
            return False
    return True
