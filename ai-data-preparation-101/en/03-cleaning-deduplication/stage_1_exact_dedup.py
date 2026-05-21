"""Generated from book-content article."""

import hashlib


def exact_dedup(docs: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for doc in docs:
        # Normalize before hashing (ignore whitespace differences)
        norm = re.sub(r"\s+", " ", doc.strip().lower())
        h = hashlib.sha256(norm.encode("utf-8")).hexdigest()
        if h not in seen:
            seen.add(h)
            out.append(doc)
    return out
