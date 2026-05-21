# Model Evaluation 101 (4/10): 정밀도와 재현율

Model Evaluation 101 시리즈 4편 예제 코드입니다.

## 학습 목표

- 정밀도와 재현율를 운영 관점에서 볼 때 먼저 어떤 경계를 확인해야 할까요?
- 정밀도와 재현율에서 예제나 다이어그램으로 검증해야 할 핵심 신호는 무엇일까요?
- 정밀도와 재현율를 실제 시스템에 적용할 때 어떤 실패를 먼저 막아야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_threshold_tradeoff.py` | 예제 코드 |

## 실행 방법

```bash
cd model-evaluation-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/04-precision-and-recall/step01_threshold_tradeoff.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/model-evaluation-101/ko/04-precision-and-recall.md)
