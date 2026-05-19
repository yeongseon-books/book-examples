from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from ko.common import build_logger, call_groq

logger = build_logger('ko.evaluation')


@dataclass(slots=True)
class EvaluationCase:
    question: str
    answer: str
    reference: str


class LLMJudge:
    def __init__(self, model: str = 'llama-3.1-8b-instant') -> None:
        self.model = model

    def evaluate(self, case: EvaluationCase) -> dict[str, Any]:
        system_prompt = '당신은 LLM 응답 평가자입니다. 정답성, 충실성, 명확성을 1점부터 5점까지 채점하고 한 줄 근거를 작성하세요.'
        user_prompt = (
            f'질문: {case.question}\n'
            f'모델 답변: {case.answer}\n'
            f'기준 답변: {case.reference}\n'
            'JSON이 아니라 일반 텍스트로 score=숫자, reason=설명을 반환하세요.'
        )
        try:
            result = call_groq(system_prompt=system_prompt, user_prompt=user_prompt, model=self.model)
            score = _extract_score(result.text)
            payload = {'score': score, 'reason': result.text.strip(), 'latency_ms': round(result.latency_ms, 1)}
            logger.info('LLM 판정 평가가 완료되었습니다.', extra={'payload': payload})
            return payload
        except Exception as exc:
            logger.exception('LLM 판정이 실패하여 휴리스틱 평가로 대체합니다.', extra={'payload': {'error': str(exc)}})
            return heuristic_evaluate(case)


def _extract_score(text: str) -> int:
    for token in text.replace(',', ' ').split():
        digits = ''.join(ch for ch in token if ch.isdigit())
        if digits:
            value = int(digits)
            if 1 <= value <= 5:
                return value
    return 3


def heuristic_evaluate(case: EvaluationCase) -> dict[str, Any]:
    answer_words = set(case.answer.split())
    reference_words = set(case.reference.split())
    overlap = len(answer_words & reference_words)
    score = 5 if overlap >= 6 else 4 if overlap >= 4 else 3 if overlap >= 2 else 2
    reason = f'휴리스틱 평가: 기준 답변과 겹치는 단어 수는 {overlap}개입니다.'
    return {'score': score, 'reason': reason, 'latency_ms': 0.0}


class BatchEvaluator:
    def __init__(self, judge: LLMJudge) -> None:
        self.judge = judge

    def run(self, cases: list[EvaluationCase]) -> dict[str, Any]:
        results = [self.judge.evaluate(case) for case in cases]
        average = round(sum(item['score'] for item in results) / len(results), 2) if results else 0.0
        return {'count': len(results), 'average_score': average, 'results': results}


def demo() -> None:
    cases = [
        EvaluationCase(
            question='장애 원인을 설명해 주세요.',
            answer='캐시 키 충돌과 느린 SQL이 함께 문제를 만들었습니다.',
            reference='캐시 키 충돌과 데이터베이스 지연이 함께 발생해 장애가 커졌습니다.',
        ),
        EvaluationCase(
            question='대응 방안을 알려 주세요.',
            answer='캐시 키를 분리하고 느린 쿼리를 튜닝해야 합니다.',
            reference='캐시 키 설계를 고치고 느린 SQL을 최적화해야 합니다.',
        ),
    ]
    report = BatchEvaluator(LLMJudge()).run(cases)
    print(report)


if __name__ == '__main__':
    demo()
