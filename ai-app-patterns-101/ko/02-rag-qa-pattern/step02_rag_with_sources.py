from __future__ import annotations

from common import (
    DEFAULT_MODEL,
    as_messages,
    build_client,
    print_section,
    response_text,
)
from retrieval import SimpleVectorStore

DOCUMENTS = [
    {
        "source": "사내 위키: 인덱싱",
        "content": "문서가 자주 바뀌는 환경에서는 증분 인덱싱이 중요합니다. 전체 재색인은 비용이 크고 최신성도 떨어질 수 있습니다.",
    },
    {
        "source": "사내 위키: 평가",
        "content": "RAG 평가는 정답 정확도만 보면 부족합니다. 검색 적중률과 근거 충실도도 함께 봐야 합니다.",
    },
    {
        "source": "운영 회고",
        "content": "출처를 함께 보여 주면 사용자는 답변을 검증하기 쉽고, 잘못된 답변도 더 빨리 발견할 수 있습니다.",
    },
]


def run_rag_with_sources() -> None:
    client = build_client()
    store = SimpleVectorStore(DOCUMENTS)
    question = "운영 중인 RAG 서비스에서 출처 표기가 왜 중요한가요?"
    retrieved = store.search(question, top_k=3)
    context = "\n\n".join(
        f"출처: {item.source}\n내용: {item.content}" for item in retrieved
    )

    messages = [
        {
            "role": "system",
            "content": "반드시 한국어로 답하고, 마지막에 '참고한 출처' 목록을 불릿으로 정리하세요.",
        },
        {"role": "user", "content": f"질문: {question}\n\n참고 문맥:\n{context}"},
    ]
    response = client.chat.completions.create(
        model=DEFAULT_MODEL, messages=as_messages(messages), temperature=0.2
    )
    answer = response_text(response.choices[0].message)

    print_section("질문")
    print(question)
    print_section("답변")
    print(answer)


if __name__ == "__main__":
    run_rag_with_sources()
