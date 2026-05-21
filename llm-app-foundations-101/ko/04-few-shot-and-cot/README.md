# LLM App Foundations 101 (4/6): Few-shot과 Chain-of-Thought — 더 나은 답변 유도하기

Llm App Foundations 101 시리즈 4편 예제 코드입니다.

## 학습 목표

- few-shot은 무엇을 가르치고 chain-of-thought는 무엇을 가르칠까요?
- zero-shot, few-shot, CoT 중 언제 어떤 도구를 골라야 할까요?
- 예시 품질이 나쁘면 왜 오히려 답변을 망칠까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_few_shot_classify.py` | 예제 코드 |
| `step02_zero_vs_few_shot.py` | 예제 코드 |
| `step03_example_quality.py` | 예제 코드 |
| `step04_zero_shot_cot.py` | 예제 코드 |
| `step05_few_shot_cot.py` | 예제 코드 |
| `step06_policy_decision.py` | 예제 코드 |

## 실행 방법

```bash
cd llm-app-foundations-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/04-few-shot-and-cot/step01_few_shot_classify.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/llm-app-foundations-101/ko/04-few-shot-and-cot.md)
