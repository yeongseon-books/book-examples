# AI Evaluation 101 (5/10): Rubric 기반 채점 설계

Ai Evaluation 101 시리즈 5편 예제 코드입니다.

## 학습 목표

- 단일 점수 하나로 LLM 품질을 말하면 어떤 고장 위치가 가려질까요?
- 좋은 rubric 차원은 어떻게 서로 겹치지 않게 나눠야 할까요?
- rubric 점수를 집계할 때 평균만 보면 어떤 위험을 놓칠까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_rubric_scoring.py` | 예제 코드 |

## 실행 방법

```bash
cd ai-evaluation-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/05-rubric-based-scoring/step01_rubric_scoring.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/ai-evaluation-101/ko/05-rubric-based-scoring.md)
