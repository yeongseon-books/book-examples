"""Generated from book-content article."""

def fallback_message(category: str | None) -> str:
    base = "Sorry, I cannot answer that here."
    suggestions = {
        "self-harm": " If you are in crisis, please contact 988 (US) or your local helpline.",
        "violence": " I can help with a different topic.",
        "policy": " Please rephrase or ask differently.",
    }
    return base + suggestions.get(category, " I can help with something else.")
