"""Generated from book-content article."""

def choose_alpha(query: str) -> float:
    visual_terms = ["looks like", "icon", "shape", "color", "layout"]
    return 0.7 if any(t in query.lower() for t in visual_terms) else 0.2
