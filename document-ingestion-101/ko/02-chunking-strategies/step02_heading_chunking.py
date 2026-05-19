"""Document Ingestion 101 - Episode 2: Heading chunking."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from shared.ingestion_examples import heading_chunks

MARKDOWN = """# 문서 수집 설계

도입부는 시스템 전체 목적을 설명합니다.

## PDF 파싱

PyMuPDF는 페이지별 텍스트와 메타데이터를 함께 제공합니다.

## 청킹 전략

고정 크기 청킹은 단순하고 빠릅니다.
재귀 청킹은 의미 단위를 더 잘 보존합니다.

## 증분 인덱싱

파일 해시를 저장해 변경된 파일만 다시 처리합니다.
"""


def main() -> None:
    """Main."""
    chunks = heading_chunks(MARKDOWN)
    print("헤딩 기반 청킹 결과")
    for chunk in chunks:
        print(f"- heading={chunk['heading']}, slug={chunk['slug']}")
        print(chunk["text"])
        print()


if __name__ == "__main__":
    main()
