"""Generated from book-content article."""

import re

def sentence_chunk(text: str, max_tokens: int = 500,
                   token_count=count_tokens) -> list[str]:
    sentences = re.split(r"(?<=[.!?])\s+", text)
    chunks, current, current_tokens = [], [], 0
    for sent in sentences:
        n = token_count(sent)
        if current_tokens + n > max_tokens and current:
            chunks.append(" ".join(current))
            current, current_tokens = [], 0
        current.append(sent)
        current_tokens += n
    if current:
        chunks.append(" ".join(current))
    return chunks
