from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def build_chunks() -> list[dict[str, object]]:
    return [
        {
            "text": "PDF 파서가 페이지별 텍스트를 추출합니다.",
            "metadata": {
                "source": "handbook.pdf",
                "page": 1,
                "section": "pdf-parsing",
                "doc_type": "guide",
                "team": "platform",
                "language": "ko",
            },
        },
        {
            "text": "증분 인덱서는 변경된 파일만 다시 처리합니다.",
            "metadata": {
                "source": "runbook.pdf",
                "page": 4,
                "section": "incremental-indexing",
                "doc_type": "runbook",
                "team": "ops",
                "language": "ko",
            },
        },
    ]


def main() -> None:
    print("청크 메타데이터 스키마 예시")
    for chunk in build_chunks():
        print(chunk)


if __name__ == "__main__":
    main()
