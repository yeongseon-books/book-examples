"""Ai App Patterns 101 - Episode 1: Session chatbot."""

from __future__ import annotations

from common import (
    DEFAULT_MODEL,
    as_messages,
    build_client,
    print_section,
    response_text,
)

SYSTEM_PROMPT = (
    "당신은 한국어로 답하는 친절한 AI 튜터입니다. 맥락을 이어서 짧고 명확하게 답하세요."
)


def run_session_chatbot() -> None:
    """Run session chatbot."""
    client = build_client()
    sessions: dict[str, list[dict[str, str]]] = {
        "demo-user": [
            {"role": "system", "content": SYSTEM_PROMPT},
        ]
    }

    user_turns = [
        "FastAPI와 Flask의 차이를 두 문장으로 설명해 주세요.",
        "그러면 학습용 프로젝트에는 무엇이 더 쉬운가요?",
    ]

    for turn in user_turns:
        sessions["demo-user"].append({"role": "user", "content": turn})
        response = client.chat.completions.create(
            model=DEFAULT_MODEL,
            messages=as_messages(sessions["demo-user"]),
            temperature=0.2,
        )
        answer = response_text(response.choices[0].message)
        sessions["demo-user"].append({"role": "assistant", "content": answer})

        print_section("사용자 질문")
        print(turn)
        print_section("챗봇 답변")
        print(answer)

    print_section("세션 저장 메시지 수")
    print(len(sessions["demo-user"]))


if __name__ == "__main__":
    run_session_chatbot()
