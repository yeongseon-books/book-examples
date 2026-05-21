"""Generated from book-content article."""

def detect_jailbreak(text: str) -> dict:
    for variant in normalize(text):
        hit, pat = known_jailbreak(variant)
        if hit:
            return {"blocked": True, "stage": "regex", "reason": pat}
        if embedding_score(variant) >= SIMILARITY_THRESHOLD:
            return {"blocked": True, "stage": "embedding"}
    if multilingual_check(text):
        return {"blocked": True, "stage": "judge"}
    return {"blocked": False}
