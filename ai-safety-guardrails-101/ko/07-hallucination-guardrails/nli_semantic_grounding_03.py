"""Generated from book-content article."""

def grounded(claims: list[dict], chunks: list[str], threshold: float = 0.7) -> dict:
    failures = []
    for c in claims:
        best = max(entails(chunk, c["text"]) for chunk in chunks)
        if best < threshold:
            failures.append({"claim": c["text"], "score": best})
    return {"ok": not failures, "failures": failures}
