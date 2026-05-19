\
"""
Step 05 — few-shot 예시를 messages 배열에 넣기
======================================================
실행:
    python step05_few_shot_basic.py

user와 assistant 예시 쌍을 앞에 배치해 원하는 답변 패턴을
모델에게 보여주는 기본 few-shot 예제입니다.
"""
import os
from typing import Any

from groq import Groq


def main() -> None:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    messages: list[Any] = [
        {
            "role": "system",
            "content": "당신은 파이썬 개념을 한 줄 정의와 한 줄 비유로 설명하는 튜터입니다.",
        },
        {"role": "user", "content": "클래스가 무엇인가요?"},
        {
            "role": "assistant",
            "content": (
                "정의: 클래스는 객체를 만들기 위한 설계도입니다.\n"
                "비유: 같은 모양의 붕어빵을 찍어내는 틀과 비슷합니다."
            ),
        },
        {"role": "user", "content": "상속이 무엇인가요?"},
        {
            "role": "assistant",
            "content": (
                "정의: 상속은 기존 클래스의 속성과 동작을 이어받아 새 클래스를 만드는 방식입니다.\n"
                "비유: 기본 템플릿을 복사해 필요한 부분만 덧붙이는 것과 비슷합니다."
            ),
        },
        {"role": "user", "content": "데코레이터가 무엇인가요?"},
    ]

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        temperature=0.2,
    )

    print(completion.choices[0].message.content)


if __name__ == "__main__":
    main()
