"""
Step 03 — Asynchronous streaming
======================================================
Run:
    python step03_async_stream.py

Use AsyncGroq and async for to process a streaming response.
This is the baseline pattern for async server environments such as FastAPI.
"""

import asyncio
import os

from groq import AsyncGroq


async def main() -> None:
    """Main."""
    client = AsyncGroq(api_key=os.environ["GROQ_API_KEY"])

    stream = await client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": "Explain why asyncio is useful in a web server.",
            }
        ],
        temperature=0.2,
        stream=True,
    )

    parts: list[str] = []

    async for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            print(delta, end="", flush=True)
            parts.append(delta)

    print(f"\n---\ntotal chars: {len(''.join(parts))}")


if __name__ == "__main__":
    asyncio.run(main())
