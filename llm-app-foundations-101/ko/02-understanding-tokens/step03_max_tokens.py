"""
Step 03 — max_tokens로 출력 길이 제어
======================================================
실행:
    python step03_max_tokens.py

max_tokens를 작게 설정해 응답을 의도적으로 자른 뒤
completion_tokens와 finish_reason을 확인합니다.
"""

import os

from groq import Groq


def call_with_max_tokens(client: Groq, max_tokens: int) -> None:
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": "파이썬 제너레이터와 리스트의 차이를 예제와 함께 자세히 설명해 주세요.",
            }
        ],
        max_tokens=max_tokens,
    )
    usage = completion.usage
    if usage is None:
        raise RuntimeError("usage 정보를 받지 못했습니다.")

    print(f"\n=== max_tokens={max_tokens} ===")
    print(completion.choices[0].message.content)
    print(f"completion_tokens={usage.completion_tokens}")
    print(f"finish_reason={completion.choices[0].finish_reason}")

    if completion.choices[0].finish_reason == "length":
        print("경고: 출력이 길이 제한에 걸려 중간에서 끝났습니다.")


def main() -> None:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    call_with_max_tokens(client, max_tokens=40)
    call_with_max_tokens(client, max_tokens=300)


if __name__ == "__main__":
    main()
