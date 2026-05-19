"""
Step 02 — assistant 메시지로 멀티턴 이력 구성
======================================================
실행:
    python step02_multiturn_history.py

1턴 응답을 assistant 메시지로 배열에 추가한 뒤
2턴 요청에서 이전 맥락을 이어가는 패턴을 보여줍니다.
"""

import os
from typing import Any

from groq import Groq


def main() -> None:
    """Main."""
    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    messages: list[Any] = [
        {
            "role": "system",
            "content": "당신은 파이썬 학습 도우미입니다. 짧고 정확하게 설명하세요.",
        },
        {
            "role": "user",
            "content": "파이썬 리스트와 튜플 차이를 한 문단으로 설명해 주세요.",
        },
    ]

    first = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        temperature=0.2,
    )
    assistant_text = first.choices[0].message.content or ""
    print("[1턴]")
    print(assistant_text)
    print()

    messages.append({"role": "assistant", "content": assistant_text})
    messages.append(
        {
            "role": "user",
            "content": "방금 설명에 다섯 줄 이하 예제 코드를 덧붙여 주세요.",
        }
    )

    second = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        temperature=0.2,
    )
    print("[2턴]")
    print(second.choices[0].message.content)


if __name__ == "__main__":
    main()
