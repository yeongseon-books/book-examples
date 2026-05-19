from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from common.rag_pipeline import answer_with_groq
from ko.shared import CORPUS, PIPELINE_CASES

PROMPT = "다음 컨텍스트만 사용해 질문에 답하세요. 정보가 없으면 없다고 말하세요.\n\n컨텍스트:\n{context}\n\n질문:\n{question}"


def main() -> None:
    case = PIPELINE_CASES[0]
    context = "\n\n".join(doc["text"] for doc in CORPUS[:3])
    print("종단간 파이프라인 샘플")
    print(answer_with_groq(case.question, context, PROMPT))


if __name__ == "__main__":
    main()
