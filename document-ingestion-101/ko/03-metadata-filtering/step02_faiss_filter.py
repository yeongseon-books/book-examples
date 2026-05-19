"""Document Ingestion 101 - Episode 2: Faiss filter."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from shared.ingestion_examples import build_faiss_index, search_faiss


def main() -> None:
    """Main."""
    records = [
        {
            "text": "PDF 파서는 페이지 번호와 제목을 함께 저장합니다.",
            "metadata": {"team": "platform", "doc_type": "guide", "language": "ko"},
        },
        {
            "text": "운영 런북은 장애 대응 절차를 포함합니다.",
            "metadata": {"team": "ops", "doc_type": "runbook", "language": "ko"},
        },
        {
            "text": "청킹 전략은 검색 품질에 직접 영향을 줍니다.",
            "metadata": {"team": "platform", "doc_type": "guide", "language": "ko"},
        },
    ]
    index, items = build_faiss_index(records)
    hits = search_faiss(
        index, items, "청킹과 PDF 파싱", top_k=2, filters={"team": "platform"}
    )

    print("platform 팀 문서만 필터링한 검색 결과")
    for hit in hits:
        print(f"score={hit.score:.4f} text={hit.metadata['text']}")
        print(f"metadata={hit.metadata['metadata']}")


if __name__ == "__main__":
    main()
