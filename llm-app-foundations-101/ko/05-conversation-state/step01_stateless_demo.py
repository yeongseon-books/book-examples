"""
Step 01 — stateless 확인
======================================================
실행:
    python step01_stateless_demo.py

첫 요청에서 이름을 알려준 뒤, 두 번째 요청에서
이력을 보내지 않으면 모델이 기억하지 못함을 보여줍니다.
"""

import os

from groq import Groq


def main() -> None:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    first = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": "내 이름은 민준이야. 기억해 줘."}],
        temperature=0.0,
    )
    print("[1턴 — 이름 전달]")
    print(first.choices[0].message.content)
    print()

    second = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": "내 이름이 뭐였지?"}],
        temperature=0.0,
    )
    print("[2턴 — 이력 없이 재질문]")
    print(second.choices[0].message.content)
    print()
    print("모델은 이전 요청을 자동으로 기억하지 않습니다.")


if __name__ == "__main__":
    main()
