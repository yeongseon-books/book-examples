# Azure Functions 101 (2/7): 트리거와 바인딩 — 함수 입출력의 모든 것

Azure Functions 101 시리즈 2편 예제 코드입니다.

## 학습 목표

- 트리거와 바인딩은 근본적으로 무엇이 다르고 왜 분리되어 있을까요?
- 입력 바인딩과 출력 바인딩은 코드를 얼마나 줄여 주고, 대신 어떤 제약을 가져올까요?
- 함수 하나에 여러 트리거를 붙일 수 없다면 그 이유는 무엇일까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_queue_to_invoice.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-functions-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/02-triggers-and-bindings/step01_queue_to_invoice.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-functions-101/ko/02-triggers-and-bindings.md)
