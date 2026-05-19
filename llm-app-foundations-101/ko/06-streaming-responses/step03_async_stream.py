"""
Step 03 — 비동기 스트리밍
======================================================
실행:
    python step03_async_stream.py

AsyncGroq와 async for를 사용해 비동기 스트리밍을 처리합니다.
FastAPI 같은 비동기 서버 환경의 기본 패턴입니다.
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
                "content": "asyncio가 웹 서버에서 왜 유리한지 설명해 주세요.",
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

    print(f"\n---\n총 글자 수: {len(''.join(parts))}")


if __name__ == "__main__":
    asyncio.run(main())
