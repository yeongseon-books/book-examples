from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class LikertQuestion:
    prompt: str
    weights: dict[str, float]


def clamp_likert(value: int) -> int:
    return max(1, min(5, int(value)))


def weighted_likert_score(
    answers: dict[str, int], questions: dict[str, LikertQuestion], tracks: list[str]
) -> dict[str, float]:
    totals = {track: 0.0 for track in tracks}
    for key, question in questions.items():
        centered = clamp_likert(answers.get(key, 3)) - 3
        for track, weight in question.weights.items():
            totals[track] += centered * weight
    return totals


def top_track(scores: dict[str, float]) -> str:
    return sorted(scores.items(), key=lambda item: (-item[1], item[0]))[0][0]


TRACKS = ["analyst", "scientist", "engineer"]

QUESTIONS = {
    "q1": LikertQuestion(
        "비즈니스 질문을 지표로 정리하는 일이 즐겁다",
        {"analyst": 1.0, "scientist": 0.4},
    ),
    "q2": LikertQuestion(
        "가설을 세우고 실험으로 검증하는 과정이 재미있다",
        {"scientist": 1.0, "analyst": 0.3},
    ),
    "q3": LikertQuestion(
        "데이터 파이프라인 안정성을 개선하는 일이 좋다", {"engineer": 1.0}
    ),
    "q4": LikertQuestion(
        "대시보드로 의사결정을 돕는 일에 보람을 느낀다", {"analyst": 0.9}
    ),
    "q5": LikertQuestion(
        "모델 성능과 일반화를 깊게 파고드는 편이다", {"scientist": 0.9}
    ),
    "q6": LikertQuestion(
        "배치/스트리밍 처리와 인프라에 관심이 많다", {"engineer": 0.9}
    ),
    "q7": LikertQuestion(
        "문제 정의와 이해관계자 커뮤니케이션이 자신 있다",
        {"analyst": 0.6, "scientist": 0.4},
    ),
    "q8": LikertQuestion(
        "코드 품질, 배포, 운영 자동화에 집착하는 편이다", {"engineer": 0.8}
    ),
    "q9": LikertQuestion("통계적 사고로 불확실성을 다루는 편이다", {"scientist": 0.8}),
    "q10": LikertQuestion("SQL로 빠르게 근거를 찾는 편이다", {"analyst": 0.8}),
}


def assess_career_fit(answers: dict[str, int]) -> dict[str, object]:
    scores = weighted_likert_score(answers, QUESTIONS, TRACKS)
    return {"scores": scores, "recommended_track": top_track(scores)}


if __name__ == "__main__":
    sample = {f"q{i}": 5 for i in range(1, 11)}
    print(assess_career_fit(sample))
