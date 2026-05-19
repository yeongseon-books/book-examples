\
"""
Step 02 — delta.content 추출과 누적
======================================================
실행:
    python step02_collect_stream.py

delta.content를 읽어 즉시 출력하고,
parts 리스트에 누적해 최종 텍스트를 만드는 실용 패턴입니다.
"""
import os

from groq import Groq


def main() -> None:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    stream = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": "FastAPI와 Flask의 차이를 입문자 관점에서 설명해 주세요.",
            }
        ],
        temperature=0.2,
        stream=True,
    )

    parts: list[str] = []

    for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            print(delta, end="", flush=True)
            parts.append(delta)

    final_text = "".join(parts)
    print("\n---")
    print(f"총 글자 수: {len(final_text)}")


if __name__ == "__main__":
    main()
