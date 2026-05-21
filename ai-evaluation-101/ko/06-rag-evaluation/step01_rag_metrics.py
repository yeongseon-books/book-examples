"""Ai Evaluation 101 - 6편: rag evaluation 예제."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import precision_at_k, recall_at_k


def run() -> dict[str, float]:
    """Run."""
    retrieved = ["doc_rag_intro", "doc_vector_db", "doc_unrelated"]
    relevant = {"doc_rag_intro", "doc_vector_db"}
    answer = "RAG는 검색과 생성을 결합합니다."
    relevance = 1.0 if "검색" in answer and "생성" in answer else 0.0
    return {
        "precision_at_2": precision_at_k(retrieved, relevant, 2),
        "recall_at_2": recall_at_k(retrieved, relevant, 2),
        "answer_relevance": relevance,
    }


if __name__ == "__main__":
    print(run())
