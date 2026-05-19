from __future__ import annotations

from common import DEFAULT_MODEL, as_messages, build_client, print_section, response_text
from retrieval import SimpleVectorStore


DOCUMENTS = [
    {
        "source": "Internal wiki: indexing",
        "content": "In a frequently changing corpus, incremental indexing matters. Full reindexing is expensive and can hurt freshness.",
    },
    {
        "source": "Internal wiki: evaluation",
        "content": "RAG evaluation needs more than answer correctness. Retrieval hit rate and grounding fidelity also matter.",
    },
    {
        "source": "Operations retrospective",
        "content": "Showing sources makes answers easier to verify and helps teams catch wrong answers faster.",
    },
]


def run_rag_with_sources() -> None:
    client = build_client()
    store = SimpleVectorStore(DOCUMENTS)
    question = "Why is source attribution important in a production RAG service?"
    retrieved = store.search(question, top_k=3)
    context = "\n\n".join(f"Source: {item.source}\nContent: {item.content}" for item in retrieved)

    messages = [
        {
            "role": "system",
            "content": "Answer in English and end with a bullet list named 'Sources used'.",
        },
        {"role": "user", "content": f"Question: {question}\n\nReference context:\n{context}"},
    ]
    response = client.chat.completions.create(model=DEFAULT_MODEL, messages=as_messages(messages), temperature=0.2)
    answer = response_text(response.choices[0].message)

    print_section("Question")
    print(question)
    print_section("Answer")
    print(answer)


if __name__ == "__main__":
    run_rag_with_sources()
