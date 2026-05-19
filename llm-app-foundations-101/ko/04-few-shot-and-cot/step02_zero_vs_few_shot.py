"""
Step 02 — zero-shot과 few-shot 비교
======================================================
실행:
    python step02_zero_vs_few_shot.py

같은 티켓을 zero-shot과 few-shot으로 각각 보내
출력 형식 안정성 차이를 비교합니다.
"""

import os

from groq import Groq

SYSTEM_PROMPT = (
    "당신은 SaaS 고객 문의를 분류하는 운영 도우미입니다. "
    "반드시 아래 형식으로만 답하세요:\n"
    "category: <billing|technical|account>\n"
    "priority: <low|medium|high>\n"
    "reason: <한 문장>"
)

TICKET = "팀 요금제인데 이번 달 청구 금액이 예상보다 두 배 가까이 높습니다."


def main() -> None:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    zero_shot = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": TICKET},
        ],
        temperature=0.2,
    )

    few_shot = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": "환불이 아직 카드 명세서에 반영되지 않았어요."},
            {
                "role": "assistant",
                "content": (
                    "category: billing\n"
                    "priority: medium\n"
                    "reason: 환불 반영 지연은 결제 후속 처리 문제다."
                ),
            },
            {
                "role": "user",
                "content": "2단계 인증 코드를 받아도 로그인이 되지 않습니다.",
            },
            {
                "role": "assistant",
                "content": (
                    "category: account\n"
                    "priority: high\n"
                    "reason: 계정 접근 실패는 사용자의 업무를 바로 막을 수 있다."
                ),
            },
            {"role": "user", "content": TICKET},
        ],
        temperature=0.2,
    )

    print("[zero-shot]")
    print(zero_shot.choices[0].message.content)
    print()
    print("[few-shot]")
    print(few_shot.choices[0].message.content)


if __name__ == "__main__":
    main()
