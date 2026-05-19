from __future__ import annotations

from common import load_markdown_fixtures, mock_llm_answer

from ko.ep01_loader_chunking import sentence_aware_chunks
from ko.ep03_retriever_mmr import top_k_retrieve
from ko.ep04_prompt_builder import build_prompt


def run_chain(question: str, fixtures_dir: str = "fixtures") -> dict[str, str]:
    docs = load_markdown_fixtures(fixtures_dir)
    all_chunks: list[str] = []
    for content in docs.values():
        all_chunks.extend(sentence_aware_chunks(content, max_chars=100))

    retrieved = top_k_retrieve(question, all_chunks, top_k=3)
    contexts = [x[1] for x in retrieved]
    prompt = build_prompt(question, contexts, budget_chars=450)
    answer = mock_llm_answer(question, contexts)
    return {"prompt": prompt, "answer": answer}


if __name__ == "__main__":
    print(run_chain("What is overlap in chunking?"))
