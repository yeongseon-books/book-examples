"""
Step 04 — 지시와 컨텍스트, 출력 형식 분리
======================================================
실행:
    python step04_structured_prompt.py

user 메시지를 지시, 컨텍스트, 출력 형식 세 블록으로 나눠
재현성 높은 프롬프트 구조를 보여줍니다.
"""

import os

from groq import Groq


def main() -> None:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": (
                    "당신은 백엔드 입문자를 돕는 파이썬 튜터입니다. "
                    "설명은 한국어로 하고, 추측하지 마세요."
                ),
            },
            {
                "role": "user",
                "content": (
                    "지시: dataclass가 무엇인지 설명해 주세요.\n"
                    "컨텍스트: 독자는 파이썬 문법은 알지만 dataclass는 처음입니다.\n"
                    "출력 형식: 1) 두 문장 설명 2) 여섯 줄 이하 코드 예제 3) 언제 쓰면 좋은지 한 줄"
                ),
            },
        ],
        temperature=0.2,
    )

    print(completion.choices[0].message.content)


if __name__ == "__main__":
    main()
