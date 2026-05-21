"""Generated from book-content article."""

async def safe_full(prompt: str) -> str:
    response = await llm.complete(prompt)
    if moderate(response)["flagged"]:
        return "Sorry, I could not produce an appropriate response."
    return response
