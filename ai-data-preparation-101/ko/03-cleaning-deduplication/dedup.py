"""Generated from book-content article."""

import hashlib

def exact_dedup(docs: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for doc in docs:
        # hashing (ignore whitespace differences) 전 정규화
        norm = re.sub(r"\s+", " ", doc.strip().lower())
        h = hashlib.sha256(norm.encode("utf-8")).hexdigest()
        if h not in seen:
            seen.add(h)
            out.append(doc)
    return out
