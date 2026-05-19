from __future__ import annotations

from common import (
    DEFAULT_MODEL,
    as_messages,
    build_client,
    print_section,
    response_text,
)

DOCUMENT = """
회의 제목: 5월 결제 전환 개선 리뷰
참석자: 지민, 현우, 수아
핵심 내용:
- 모바일 결제 이탈률이 지난달보다 12% 증가했습니다.
- 원인 후보는 주소 입력 단계 지연, 카드 인증 실패, 쿠폰 적용 혼란입니다.
- 다음 주까지 주소 자동완성 실험과 인증 오류 로그 점검을 진행합니다.
""".strip()


def run_document_assistant() -> None:
    client = build_client()

    summary_messages = [
        {"role": "system", "content": "문서를 3문장으로 한국어 요약하세요."},
        {"role": "user", "content": DOCUMENT},
    ]
    summary_response = client.chat.completions.create(
        model=DEFAULT_MODEL, messages=as_messages(summary_messages), temperature=0.1
    )

    extract_messages = [
        {
            "role": "system",
            "content": "문서에서 action item만 한국어 불릿으로 추출하세요. 담당자와 마감이 보이면 함께 적으세요.",
        },
        {"role": "user", "content": DOCUMENT},
    ]
    extract_response = client.chat.completions.create(
        model=DEFAULT_MODEL, messages=as_messages(extract_messages), temperature=0.1
    )

    print_section("문서 요약")
    print(response_text(summary_response.choices[0].message))
    print_section("추출 결과")
    print(response_text(extract_response.choices[0].message))


if __name__ == "__main__":
    run_document_assistant()
