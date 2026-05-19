from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from common.rag_pipeline import answer_with_groq
from en.shared import CORPUS, PIPELINE_CASES

PROMPT = "Answer the question using only the context below. If the answer is missing, say so clearly.\n\nContext:\n{context}\n\nQuestion:\n{question}"


def main() -> None:
    case = PIPELINE_CASES[0]
    context = "\n\n".join(doc["text"] for doc in CORPUS[:3])
    print("End-to-end pipeline sample")
    print(answer_with_groq(case.question, context, PROMPT))


if __name__ == "__main__":
    main()
