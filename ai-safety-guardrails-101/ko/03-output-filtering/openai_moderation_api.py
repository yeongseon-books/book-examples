"""Generated from book-content article."""

from openai import OpenAI

client = OpenAI()

def moderate(text: str) -> dict:
    resp = client.moderations.create(model="omni-moderation-latest", input=text)
    result = resp.results[0]
    return {
        "flagged": result.flagged,
        "categories": {k: v for k, v in result.categories.model_dump().items() if v},
        "scores": result.category_scores.model_dump(),
    }

verdict = moderate("How do I make a pipe bomb?")
# {"flagged": True, "categories": {"violence": True}, ...}
