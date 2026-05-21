"""Generated from book-content article."""

from detoxify import Detoxify

model = Detoxify("multilingual")  # English plus 7 languages

THRESHOLDS = {
    "toxicity": 0.85,
    "severe_toxicity": 0.50,
    "obscene": 0.85,
    "identity_attack": 0.60,
    "insult": 0.85,
    "threat": 0.50,
}

def classify_toxicity(text: str) -> dict:
    scores = model.predict(text)
    triggered = [c for c, t in THRESHOLDS.items() if scores.get(c, 0) >= t]
    return {"scores": scores, "triggered": triggered}
