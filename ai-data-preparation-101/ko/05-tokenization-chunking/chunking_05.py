"""Generated from book-content article."""

def recursive_chunk(text: str, max_tokens: int = 500,
                    separators: list[str] | None = None,
                    token_count=count_tokens) -> list[str]:
    separators = separators or ["\n\n", "\n", ". ", " ", ""]
    if token_count(text) <= max_tokens:
        return [text]
    sep = separators[0]
    if not sep:
        # base case: forced length-based split
        mid = len(text) // 2
        return recursive_chunk(text[:mid], max_tokens, separators[1:]) + \
               recursive_chunk(text[mid:], max_tokens, separators[1:])
    parts = text.split(sep)
    chunks, current = [], ""
    for p in parts:
        candidate = current + sep + p if current else p
        if token_count(candidate) > max_tokens:
            if current:
                chunks.append(current)
            if token_count(p) > max_tokens:
                chunks.extend(recursive_chunk(p, max_tokens, separators[1:]))
                current = ""
            else:
                current = p
        else:
            current = candidate
    if current:
        chunks.append(current)
    return chunks
