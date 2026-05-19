from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, Mapping


Track = str


@dataclass(frozen=True)
class LikertQuestion:
    prompt: str
    weights: Dict[Track, float]


def clamp_likert(value: int) -> int:
    return max(1, min(5, int(value)))


def weighted_likert_score(
    answers: Mapping[str, int],
    questions: Mapping[str, LikertQuestion],
    tracks: Iterable[Track],
) -> Dict[Track, float]:
    totals = {track: 0.0 for track in tracks}
    for key, question in questions.items():
        answer = clamp_likert(answers.get(key, 3))
        centered = answer - 3
        for track, weight in question.weights.items():
            totals[track] += centered * weight
    return totals


def top_track(scores: Mapping[Track, float]) -> Track:
    return sorted(scores.items(), key=lambda item: (-item[1], item[0]))[0][0]


def score_rubric(
    scores: Mapping[str, float], weak_threshold: float = 2.5
) -> Dict[str, str]:
    result: Dict[str, str] = {}
    for key, score in scores.items():
        if score >= 4.0:
            result[key] = "strong"
        elif score >= weak_threshold:
            result[key] = "developing"
        else:
            result[key] = "gap"
    return result
