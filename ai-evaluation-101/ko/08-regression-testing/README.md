# AI Evaluation 101 (8/10): 회귀 테스트 — 어제 잘 되던 게 오늘 망가지지 않게

Ai Evaluation 101 시리즈 8편 예제 코드입니다.

## 학습 목표

- 회귀 테스트는 왜 LLM 평가를 배포 전 행사가 아니라 PR 방어선으로 옮겨야 할까요?
- golden dataset과 threshold는 어떤 변경을 막아야 할까요?
- non-determinism 때문에 eval이 흔들릴 때 어떤 tolerance와 fail policy가 필요할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_regression_gate.py` | 예제 코드 |

## 실행 방법

```bash
cd ai-evaluation-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/08-regression-testing/step01_regression_gate.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/ai-evaluation-101/ko/08-regression-testing.md)
