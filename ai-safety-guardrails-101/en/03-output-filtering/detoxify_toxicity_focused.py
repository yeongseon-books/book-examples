"""Generated from book-content article."""

from detoxify import Detoxify

detox = Detoxify("original")  # or "multilingual"

def detox_score(text: str) -> dict:
    return detox.predict(text)  # {"toxicity": 0.02, "severe_toxicity": 0.001, ...}

scores = detox_score("You're an idiot")
# toxicity: 0.92
