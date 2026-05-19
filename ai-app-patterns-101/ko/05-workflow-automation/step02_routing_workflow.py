"""Ai App Patterns 101 - Episode 2: Routing workflow."""

from __future__ import annotations

from common import (
    DEFAULT_MODEL,
    as_messages,
    build_client,
    print_section,
    response_text,
)

REQUESTS = [
    "결제 장애 공지를 고객에게 보낼 짧은 안내문을 만들어 주세요.",
    "다음 분기 실험 아이디어를 3개 제안해 주세요.",
]


def route_request(client, request: str) -> tuple[str, str]:
    """Route request."""
    classifier_messages = [
        {
            "role": "system",
            "content": "입력을 'incident' 또는 'planning' 중 하나로만 분류하세요.",
        },
        {"role": "user", "content": request},
    ]
    route = response_text(
        client.chat.completions.create(
            model=DEFAULT_MODEL,
            messages=as_messages(classifier_messages),
            temperature=0,
        )
        .choices[0]
        .message
    ).lower()

    if "incident" in route:
        writer_prompt = "고객 대상 장애 안내문을 한국어로 작성하세요. 원인 추정보다 현재 상태와 다음 공지를 우선하세요."
        label = "incident"
    else:
        writer_prompt = "실험 아이디어 제안서를 한국어 불릿으로 작성하세요."
        label = "planning"

    writer_messages = [
        {"role": "system", "content": writer_prompt},
        {"role": "user", "content": request},
    ]
    result = response_text(
        client.chat.completions.create(
            model=DEFAULT_MODEL, messages=as_messages(writer_messages), temperature=0.3
        )
        .choices[0]
        .message
    )
    return label, result


def run_routing_workflow() -> None:
    """Run routing workflow."""
    client = build_client()
    for request in REQUESTS:
        route, output = route_request(client, request)
        print_section(f"라우팅 결과: {route}")
        print(request)
        print(output)


if __name__ == "__main__":
    run_routing_workflow()
