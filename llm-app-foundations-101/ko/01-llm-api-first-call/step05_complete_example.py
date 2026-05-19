"""
Step 05 — 완성 예제
======================================================
실행:
    python step05_complete_example.py

01편 전체 내용을 한 파일로 모은 완성 예제입니다.
system 메시지, user 메시지, 응답 본문, 사용량 메타데이터를 함께 출력합니다.
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
                "content": "당신은 간결하게 설명하는 파이썬 튜터입니다.",
            },
            {
                "role": "user",
                "content": (
                    "파이썬 초급자에게 함수와 메서드의 차이를 다섯 문장 이내로 설명하고, "
                    "짧은 예시 한 줄을 덧붙여 주세요."
                ),
            },
        ],
    )

    content = completion.choices[0].message.content or ""
    usage = completion.usage
    if usage is None:
        raise RuntimeError("usage 정보를 받지 못했습니다.")

    print("=== 답변 ===")
    print(content)
    print()
    print("=== 메타데이터 ===")
    print(f"model: {completion.model}")
    print(f"finish_reason: {completion.choices[0].finish_reason}")
    print(f"prompt_tokens: {usage.prompt_tokens}")
    print(f"completion_tokens: {usage.completion_tokens}")
    print(f"total_tokens: {usage.total_tokens}")


if __name__ == "__main__":
    main()
