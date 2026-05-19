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
        "source": "Operations guide",
        "content": "A RAG system has two phases: retrieve relevant documents first, then generate an answer grounded in that context.",
    },
    {
        "source": "Quality note",
        "content": "If retrieval quality is poor, answer quality usually drops too. Chunking strategy and embedding choice matter a lot.",
    },
    {
        "source": "Cost memo",
        "content": "Sending unnecessary context increases both token cost and latency. Most systems pass only the top few documents.",
    },
]


def run_basic_rag() -> None:
    client = build_client()
    store = SimpleVectorStore(DOCUMENTS)
    question = "Why is retrieval quality so important in RAG?"
    retrieved = store.search(question, top_k=2)
    context = "\n\n".join(f"[{item.source}] {item.content}" for item in retrieved)

    messages = [
        {
            "role": "system",
            "content": "Answer in English using only the provided context.",
        },
        {"role": "user", "content": f"Question: {question}\n\nContext:\n{context}"},
    ]
    response = client.chat.completions.create(
        model=DEFAULT_MODEL, messages=as_messages(messages), temperature=0.2
    )
    answer = response_text(response.choices[0].message)

    print_section("Retrieved documents")
    for item in retrieved:
        print(f"- {item.source} (score={item.score:.3f})")
    print_section("RAG answer")
    print(answer)


if __name__ == "__main__":
    run_basic_rag()
