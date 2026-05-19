"""
Step 06 — FastAPI StreamingResponse
======================================================
실행:
    uvicorn step06_fastapi_stream:app --reload

브라우저나 curl에서 Groq 스트림을 SSE로 확인합니다.
"""

import os

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from groq import AsyncGroq

app = FastAPI()


def get_client() -> AsyncGroq:
    """Get client."""
    return AsyncGroq(api_key=os.environ["GROQ_API_KEY"])


@app.get("/chat/stream")
async def chat_stream(prompt: str) -> StreamingResponse:
    """Chat stream."""

    async def event_gen():
        """Event gen."""
        client = get_client()
        stream = await client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            stream=True,
        )

        async for chunk in stream:
            delta = chunk.choices[0].delta.content
            if delta:
                yield f"data: {delta}\n\n"

        yield "data: [done]\n\n"

    return StreamingResponse(event_gen(), media_type="text/event-stream")
