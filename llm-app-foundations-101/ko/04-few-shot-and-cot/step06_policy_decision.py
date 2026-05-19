"""
Step 06 — few-shot CoT와 정책 판정
======================================================
실행:
    python step06_policy_decision.py

환불 정책을 policy_check, decision, reason 형식으로
판정하는 few-shot CoT 완성 예제입니다.
"""

import os

from groq import Groq
from groq.types.chat import ChatCompletionMessageParam

POLICY = (
    "환불 정책:\n"
    "- 결제 후 7일 이내이고 시청률 20% 미만이면 전액 환불\n"
    "- 결제 후 7일 이내이고 시청률 20% 이상이면 환불 불가\n"
    "- 결제 후 7일 초과면 시청률과 무관하게 환불 불가"
)


def build_messages(case: str) -> list[ChatCompletionMessageParam]:
    return [
        {
            "role": "system",
            "content": (
                "당신은 온라인 강의 서비스의 환불 심사 도우미입니다. "
                "항상 1) policy_check 2) decision 3) reason 형식으로 답하세요."
            ),
        },
        {"role": "user", "content": POLICY},
        {
            "role": "user",
            "content": "결제 후 3일 지났고 시청률은 10%입니다. 환불 가능 여부를 판단해 주세요.",
        },
        {
            "role": "assistant",
            "content": (
                "policy_check:\n"
                "1) 결제 후 7일 이내입니다.\n"
                "2) 시청률이 20% 미만입니다.\n"
                "decision: approved\n"
                "reason: 기간과 시청률 조건을 모두 충족해 전액 환불 대상입니다."
            ),
        },
        {
            "role": "user",
            "content": "결제 후 5일 지났고 시청률은 35%입니다. 환불 가능 여부를 판단해 주세요.",
        },
        {
            "role": "assistant",
            "content": (
                "policy_check:\n"
                "1) 결제 후 7일 이내입니다.\n"
                "2) 시청률이 20% 이상입니다.\n"
                "decision: denied\n"
                "reason: 기간 조건은 맞지만 시청률 기준을 넘어 환불할 수 없습니다."
            ),
        },
        {"role": "user", "content": case},
    ]


def main() -> None:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    cases = [
        "결제 후 10일 지났고 시청률은 0%입니다. 환불 가능 여부를 판단해 주세요.",
        "결제 후 2일 지났고 시청률은 5%입니다. 환불 가능 여부를 판단해 주세요.",
    ]

    for case in cases:
        print(f"[사례] {case}")
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=build_messages(case),
            temperature=0.0,
        )
        print(completion.choices[0].message.content)
        print()


if __name__ == "__main__":
    main()
