from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from common.models import BenchmarkConfig
from common.rag_pipeline import result_to_json, run_pipeline_benchmark
from ko.shared import CORPUS, PIPELINE_CASES


def main() -> None:
    print("종단간 평가 실행")
    config = BenchmarkConfig(
        name="e2e-ko",
        embedding_model="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
        top_k=3,
        answer_prompt="다음 컨텍스트만 사용해 질문에 답하세요. 정보가 없으면 없다고 말하세요.\n\n컨텍스트:\n{context}\n\n질문:\n{question}",
    )
    result = run_pipeline_benchmark("ko", CORPUS, PIPELINE_CASES, config)
    print(result_to_json(result))


if __name__ == "__main__":
    main()
