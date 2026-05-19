"""
Step 01 — system 메시지 유무 비교
======================================================
실행:
    python step01_system_effect.py

같은 질문을 system 없이 또는 system과 함께 보내서
응답 스타일 차이를 확인합니다.
"""

import os

from groq import Groq


def main() -> None:
    """Main."""
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    question = "파이썬의 딕셔너리와 리스트 차이를 설명해 주세요."

    without_system = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": question}],
        temperature=0.2,
    )

    with_system = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": (
                    "당신은 파이썬 입문자를 돕는 기술 튜터입니다. "
                    "항상 한국어로 답하고, 먼저 한 문단 요약을 쓴 뒤 "
                    "마지막에 불릿 세 개로 핵심 차이를 정리하세요. "
                    "추측하지 말고 초급자 눈높이를 유지하세요."
                ),
            },
            {"role": "user", "content": question},
        ],
        temperature=0.2,
    )

    print("[system 메시지 없음]")
    print(without_system.choices[0].message.content)
    print()
    print("[system 메시지 있음]")
    print(with_system.choices[0].message.content)


if __name__ == "__main__":
    main()
