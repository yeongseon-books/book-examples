# AI Evaluation 101 (4/10): LLM-as-Judge — 모델로 모델을 평가하기

Ai Evaluation 101 시리즈 4편 예제 코드입니다.

## 학습 목표

- LLM-as-Judge는 언제 사람이 매번 평가하기 어려운 품질 판단을 도와줄까요?
- judge prompt와 rubric이 없으면 자동 채점기는 어떤 편향에 흔들릴까요?
- 사람 기준선과 agreement를 어떻게 붙여야 judge 결과를 믿을 수 있을까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `agreement.py` | 예제 코드 |
| `debias_position.py` | 예제 코드 |
| `judge_pairwise.py` | 예제 코드 |
| `judge_reference.py` | 예제 코드 |
| `judge_single.py` | 예제 코드 |
| `step01_mock_judge.py` | 예제 코드 |

## 실행 방법

```bash
cd ai-evaluation-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/04-llm-as-judge/agreement.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/ai-evaluation-101/ko/04-llm-as-judge.md)
