import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import MockLLMJudge


def run() -> dict[str, object]:
    judge = MockLLMJudge()
    answer = "근거를 기준으로 설명하면 RAG는 검색 문서를 사용하므로 hallucination 위험이 줄어듭니다."
    scores = judge.rubric_score("RAG 설명", answer)
    verdict = (
        "PASS" if scores["correctness"] >= 4 and min(scores.values()) >= 3 else "REVIEW"
    )
    return {"scores": scores, "verdict": verdict}


if __name__ == "__main__":
    print(run())
