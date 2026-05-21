"""Generated from book-content article."""

import re

CITE_RE = re.compile(r"\[chunk-(\d+)\]")

def citation_check(answer: str, retrieved_ids: set[int]) -> dict:
    cited = {int(m.group(1)) for m in CITE_RE.finditer(answer)}
    missing = cited - retrieved_ids
    sentences = [s for s in re.split(r"(?<=[.!?])\s+", answer) if s.strip()]
    uncited = [s for s in sentences if not CITE_RE.search(s)]
    return {"missing_chunks": missing, "uncited_sentences": uncited}
