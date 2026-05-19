"""
Step 02 — 첫 번째 API 호출
======================================================
실행:
    python step02_first_call.py

Groq 클라이언트를 만들고 llama-3.1-8b-instant에
메시지를 보낸 뒤 응답 본문을 출력합니다.
"""

import os

from groq import Groq


def main() -> None:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": "파이썬 리스트 컴프리헨션을 한 문단으로 설명해 주세요.",
            }
        ],
    )

    print(completion.choices[0].message.content)


if __name__ == "__main__":
    main()
