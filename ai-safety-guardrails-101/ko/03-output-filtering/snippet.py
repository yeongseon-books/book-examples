"""Generated from book-content article."""

async def safe_stream(prompt: str):
    buffer = ""
    chunk_words = 50
    async for token in llm.stream(prompt):
        buffer += token
        if len(buffer.split()) >= chunk_words:
            verdict = moderate(buffer)
            if verdict["flagged"]:
                yield "\n\n[Response cut off due to a policy violation]"
                return
        yield token
    if moderate(buffer)["flagged"]:
        yield "\n\n[Please disregard the response above. Policy violation detected.]"
