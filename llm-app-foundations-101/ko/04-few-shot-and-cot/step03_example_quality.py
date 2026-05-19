\
"""
Step 03 — 나쁜 예시와 좋은 예시 비교
======================================================
실행:
    python step03_example_quality.py

라벨이 흐릿한 나쁜 예시와 형식이 선명한 좋은 예시를
같은 질문에 붙여 결과 차이를 보여줍니다.
"""
import os
from typing import Any

from groq import Groq

SYSTEM_PROMPT = (
    "당신은 SaaS 고객 문의를 분류합니다. "
    "아래 형식으로만 답하세요:\n"
    "category: <billing|technical|account>\n"
    "priority: <low|medium|high>\n"
    "reason: <한 문장>"
)

TARGET = "비밀번호 재설정 메일이 오지 않아 로그인하지 못하고 있습니다."


def main() -> None:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    bad_examples: list[Any] = [
        {"role": "user", "content": "청구서 금액이 이상합니다."},
        {
            "role": "assistant",
            "content": "이건 결제 문제 같기도 하고 계정 문제 같기도 합니다. 우선 고객에게 다시 물어보세요.",
        },
        {"role": "user", "content": "로그인이 안 됩니다."},
        {
            "role": "assistant",
            "content": "priority는 급할 수도 있고 아닐 수도 있습니다. 상황마다 다릅니다.",
        },
    ]

    good_examples: list[Any] = [
        {"role": "user", "content": "결제 카드가 두 번 청구된 것 같습니다."},
        {
            "role": "assistant",
            "content": (
                "category: billing\n"
                "priority: high\n"
                "reason: 중복 청구는 금전 피해 가능성이 있어 우선 대응이 필요하다."
            ),
        },
        {"role": "user", "content": "프로필 사진 업로드 버튼을 누르면 500 오류가 납니다."},
        {
            "role": "assistant",
            "content": (
                "category: technical\n"
                "priority: medium\n"
                "reason: 기능 오류지만 계정 잠금만큼 즉시성이 높지는 않다."
            ),
        },
    ]

    bad_messages: list[Any] = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "예시를 보고 같은 형식으로 분류해 주세요."},
        *bad_examples,
        {"role": "user", "content": TARGET},
    ]
    good_messages: list[Any] = [
        {"role": "system", "content": SYSTEM_PROMPT},
        *good_examples,
        {"role": "user", "content": TARGET},
    ]

    bad_run = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=bad_messages,
        temperature=0.2,
    )
    good_run = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=good_messages,
        temperature=0.2,
    )

    print("[나쁜 예시]")
    print(bad_run.choices[0].message.content)
    print()
    print("[좋은 예시]")
    print(good_run.choices[0].message.content)


if __name__ == "__main__":
    main()
