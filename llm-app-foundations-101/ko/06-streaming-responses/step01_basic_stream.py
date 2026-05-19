"""
Step 01 — stream=True 기본 패턴
======================================================
실행:
    python step01_basic_stream.py

stream=True를 추가하고 for chunk in stream으로 순회해
각 청크 객체를 그대로 출력합니다.
"""
import os

from groq import Groq


def main() -> None:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    stream = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "당신은 간결한 파이썬 튜터입니다."},
            {
                "role": "user",
                "content": "파이썬 제너레이터를 다섯 문장 안에서 설명해 주세요.",
            },
        ],
        temperature=0.3,
        stream=True,
    )

    for chunk in stream:
        print(chunk)


if __name__ == "__main__":
    main()
