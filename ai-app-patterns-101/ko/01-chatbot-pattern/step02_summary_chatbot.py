from __future__ import annotations

from common import (
    DEFAULT_MODEL,
    as_messages,
    build_client,
    print_section,
    response_text,
)

SYSTEM_PROMPT = "당신은 한국어로 답하는 AI 코치입니다. 기존 대화 요약을 참고해 연속성 있게 답하세요."


def summarize_history(client, history: list[dict[str, str]]) -> str:
    summary_messages = [
        {
            "role": "system",
            "content": "대화 이력을 5문장 이내의 한국어 요약으로 압축하세요.",
        },
        {"role": "user", "content": str(history)},
    ]
    response = client.chat.completions.create(
        model=DEFAULT_MODEL,
        messages=as_messages(summary_messages),
        temperature=0.1,
    )
    return response_text(response.choices[0].message)


def run_summary_chatbot() -> None:
    client = build_client()
    history: list[dict[str, str]] = [{"role": "system", "content": SYSTEM_PROMPT}]
    rolling_summary = "아직 요약 없음"

    user_turns = [
        "RAG와 일반 검색의 차이를 설명해 주세요.",
        "비용 관점에서는 어떤 점을 주의해야 하나요?",
        "지금까지 내용을 한 번 더 이어서, 작은 팀에 추천 전략도 알려 주세요.",
    ]

    for idx, turn in enumerate(user_turns, start=1):
        if len(history) > 5:
            rolling_summary = summarize_history(client, history[1:])
            history = [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "system", "content": f"대화 요약: {rolling_summary}"},
            ]

        history.append({"role": "user", "content": turn})
        response = client.chat.completions.create(
            model=DEFAULT_MODEL,
            messages=as_messages(history),
            temperature=0.2,
        )
        answer = response_text(response.choices[0].message)
        history.append({"role": "assistant", "content": answer})

        print_section(f"대화 턴 {idx}")
        print(f"질문: {turn}")
        print(f"답변: {answer}")

    print_section("최종 요약")
    print(rolling_summary)


if __name__ == "__main__":
    run_summary_chatbot()
