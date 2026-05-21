"""Generated from book-content article."""

def stream_safely(prompt: str):
    buffer = ""
    for chunk in llm.stream(prompt):
        buffer += chunk
        if buffer.endswith((".", "!", "?", "\n")) or len(buffer) > 200:
            verdict = classify_toxicity(buffer)
            if verdict["triggered"]:
                yield "[blocked]"
                return
            yield buffer
            buffer = ""
    if buffer:
        if classify_toxicity(buffer)["triggered"]:
            yield "[blocked]"
        else:
            yield buffer
