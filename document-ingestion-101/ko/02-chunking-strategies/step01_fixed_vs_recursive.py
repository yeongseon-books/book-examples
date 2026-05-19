from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from shared.ingestion_examples import fixed_chunks, recursive_chunks

TEXT = """문서 수집 파이프라인은 파서, 청커, 인덱서로 나뉩니다.

파서는 원본 파일에서 텍스트와 메타데이터를 추출합니다. 청커는 긴 본문을 검색 가능한 단위로 나눕니다. 인덱서는 임베딩과 메타데이터를 함께 저장합니다.

고정 크기 청킹은 구현이 단순하지만 문장 중간에서 끊길 수 있습니다. 재귀 청킹은 문단과 문장 경계를 먼저 존중한 뒤 필요한 경우에만 더 잘게 나눕니다."""


def main() -> None:
    fixed = fixed_chunks(TEXT, size=18, overlap=4)
    recursive = recursive_chunks(TEXT, size=18, overlap=4)

    print("고정 크기 청킹 결과")
    for index, chunk in enumerate(fixed, start=1):
        print(f"{index:02d}. {chunk}")

    print()
    print("재귀 청킹 결과")
    for index, chunk in enumerate(recursive, start=1):
        print(f"{index:02d}. {chunk}")


if __name__ == "__main__":
    main()
