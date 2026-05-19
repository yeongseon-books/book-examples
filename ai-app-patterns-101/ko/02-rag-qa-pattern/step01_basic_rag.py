"""Ai App Patterns 101 - Episode 1: Basic rag."""

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
        "source": "운영 가이드",
        "content": "RAG 시스템은 검색과 생성의 두 단계를 거칩니다. 먼저 관련 문서를 찾고, 그 결과를 프롬프트에 넣어 답변을 생성합니다.",
    },
    {
        "source": "품질 노트",
        "content": "검색 품질이 낮으면 답변 품질도 함께 낮아집니다. 청크 전략과 임베딩 모델 선택이 특히 중요합니다.",
    },
    {
        "source": "비용 메모",
        "content": "불필요하게 긴 문맥을 보내면 토큰 비용과 지연 시간이 함께 증가합니다. 상위 몇 개 문서만 보내는 것이 일반적입니다.",
    },
]


def run_basic_rag() -> None:
    """Run basic rag."""
    client = build_client()
    store = SimpleVectorStore(DOCUMENTS)
    question = "RAG에서 검색 품질이 중요한 이유를 설명해 주세요."
    retrieved = store.search(question, top_k=2)
    context = "\n\n".join(f"[{item.source}] {item.content}" for item in retrieved)

    messages = [
        {"role": "system", "content": "주어진 문맥만 근거로 한국어 답변을 작성하세요."},
        {"role": "user", "content": f"질문: {question}\n\n문맥:\n{context}"},
    ]
    response = client.chat.completions.create(
        model=DEFAULT_MODEL, messages=as_messages(messages), temperature=0.2
    )
    answer = response_text(response.choices[0].message)

    print_section("검색된 문서")
    for item in retrieved:
        print(f"- {item.source} (score={item.score:.3f})")
    print_section("RAG 답변")
    print(answer)


if __name__ == "__main__":
    run_basic_rag()
