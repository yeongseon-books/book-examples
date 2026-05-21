"""Generated from book-content article."""

from transformers import pipeline

nli = pipeline(
    "text-classification",
    model="cross-encoder/nli-deberta-v3-large",
    return_all_scores=True,
)

def entails(premise: str, hypothesis: str) -> float:
    """Return entailment probability between 0 and 1."""
    pairs = [{"text": premise, "text_pair": hypothesis}]
    out = nli(pairs)[0]
    return next(s["score"] for s in out if s["label"] == "ENTAILMENT")
