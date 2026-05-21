"""Generated from book-content article."""

def hybrid_score(query: str, doc, alpha: float = 0.6) -> float:
    sem = semantic_score(query, doc)   # CLIP / embedding based
    lex = bm25_score(query, doc)       # lexical match
    return alpha * sem + (1 - alpha) * lex
