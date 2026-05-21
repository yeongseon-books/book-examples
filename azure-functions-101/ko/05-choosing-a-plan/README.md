# Azure Functions 101 (5/7): 어떤 플랜을 선택해야 할까 — Consumption / Flex / Premium / Dedicated

Azure Functions 101 시리즈 5편 예제 코드입니다.

## 학습 목표

- 각 플랜은 정확히 무엇을 기준으로 과금하고 무엇을 제약할까요?
- 플랜 선택에서 가격보다 콜드 스타트 허용 범위가 먼저 중요해지는 경우는 언제일까요?
- VNet 통합, Always Ready 같은 플랫폼 기능은 어떤 플랜 선택을 사실상 강제할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_plan_selector.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-functions-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/05-choosing-a-plan/step01_plan_selector.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-functions-101/ko/05-choosing-a-plan.md)
