from __future__ import annotations

from common import (
    DEFAULT_MODEL,
    as_messages,
    build_client,
    print_section,
    response_text,
)

CASES = [
    {
        "request": "환불 규정 예외 적용을 승인해 주세요. 고객은 장애로 인해 결제를 두 번 시도했습니다.",
        "confidence": 0.91,
    },
    {
        "request": "VIP 고객의 위약금 면제를 승인해 주세요. 계약 위반 가능성이 있습니다.",
        "confidence": 0.42,
    },
]


def run_hitl_workflow() -> None:
    client = build_client()

    for case in CASES:
        requires_human = case["confidence"] < 0.75
        decision = "사람 승인 필요" if requires_human else "자동 처리 가능"
        messages = [
            {
                "role": "system",
                "content": "입력된 신뢰도와 요청 내용을 바탕으로 자동 처리 또는 수동 승인의 이유를 한국어로 설명하세요.",
            },
            {
                "role": "user",
                "content": f"요청: {case['request']}\n신뢰도: {case['confidence']}\n예상 경로: {decision}",
            },
        ]
        response = client.chat.completions.create(
            model=DEFAULT_MODEL, messages=as_messages(messages), temperature=0.1
        )

        print_section(decision)
        print(case["request"])
        print(response_text(response.choices[0].message))


if __name__ == "__main__":
    run_hitl_workflow()
