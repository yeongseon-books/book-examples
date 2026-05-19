from __future__ import annotations

from common import (
    DEFAULT_MODEL,
    as_messages,
    build_client,
    print_section,
    response_text,
)

REQUEST = "고객이 가격은 유지하면서도 도입 시간을 줄이고 싶어 합니다. AI 문서 검색 도입 제안 메일 초안을 작성해 주세요."


def run_sequential_chain() -> None:
    client = build_client()

    analyze_messages = [
        {"role": "system", "content": "요청 의도를 한국어로 세 줄 이하로 정리하세요."},
        {"role": "user", "content": REQUEST},
    ]
    analysis = response_text(
        client.chat.completions.create(
            model=DEFAULT_MODEL, messages=as_messages(analyze_messages), temperature=0.1
        )
        .choices[0]
        .message
    )

    draft_messages = [
        {
            "role": "system",
            "content": "입력된 분석을 바탕으로 짧은 한국어 제안 메일을 작성하세요.",
        },
        {"role": "user", "content": f"요청: {REQUEST}\n\n분석: {analysis}"},
    ]
    draft = response_text(
        client.chat.completions.create(
            model=DEFAULT_MODEL, messages=as_messages(draft_messages), temperature=0.3
        )
        .choices[0]
        .message
    )

    print_section("의도 분석")
    print(analysis)
    print_section("메일 초안")
    print(draft)


if __name__ == "__main__":
    run_sequential_chain()
