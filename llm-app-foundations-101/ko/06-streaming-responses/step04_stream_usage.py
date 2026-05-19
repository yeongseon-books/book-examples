"""
Step 04 — 마지막 청크에서 사용량 읽기
======================================================
실행:
    python step04_stream_usage.py

마지막 청크를 추적해 x_groq.usage에서
토큰 사용량을 읽는 패턴입니다.
"""

import os

from groq import Groq


def main() -> None:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    stream = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": "파이썬 데코레이터를 설명해 주세요."}],
        stream=True,
    )

    parts: list[str] = []
    last_chunk = None

    for chunk in stream:
        last_chunk = chunk
        delta = chunk.choices[0].delta.content
        if delta:
            parts.append(delta)
            print(delta, end="", flush=True)

    print("\n---")
    print("".join(parts))

    usage = None
    if last_chunk is not None:
        groq_meta = getattr(last_chunk, "x_groq", None)
        if groq_meta is not None:
            usage = getattr(groq_meta, "usage", None)

    if usage is not None:
        print(f"prompt_tokens: {usage.prompt_tokens}")
        print(f"completion_tokens: {usage.completion_tokens}")
        print(f"total_tokens: {usage.total_tokens}")
    else:
        print("마지막 청크에 usage 메타데이터가 없었습니다.")


if __name__ == "__main__":
    main()
