"""
Step 05 — 스트림을 파일에 쓰기
======================================================
실행:
    python step05_stream_to_file.py

생성되는 토큰을 파일에 즉시 쓰고,
문장 단위로 consumer에 전달하는 파이프 패턴을 함께 보여줍니다.
"""

import os
from collections.abc import Generator
from pathlib import Path

from groq import Groq


def sentence_chunks(stream) -> Generator[str, None, None]:
    buffer = ""
    for chunk in stream:
        delta = chunk.choices[0].delta.content
        if not delta:
            continue
        buffer += delta
        while ". " in buffer:
            sentence, buffer = buffer.split(". ", 1)
            yield sentence + "."
    if buffer.strip():
        yield buffer


def main() -> None:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    output_path = Path(__file__).with_name("summary.txt")

    with output_path.open("w", encoding="utf-8") as file:
        for chunk in client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": "벡터 데이터베이스를 쉽게 설명해 주세요.",
                }
            ],
            stream=True,
        ):
            delta = chunk.choices[0].delta.content
            if delta:
                file.write(delta)
                file.flush()
                print(delta, end="", flush=True)

    print(f"\n\n파일 저장 완료: {output_path}")

    print("\n=== 문장 단위 파이프 ===")
    pipe_stream = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": "벡터 데이터베이스를 쉽게 설명해 주세요."}
        ],
        stream=True,
    )
    for sentence in sentence_chunks(pipe_stream):
        print(f"[consumer] {sentence}")


if __name__ == "__main__":
    main()
