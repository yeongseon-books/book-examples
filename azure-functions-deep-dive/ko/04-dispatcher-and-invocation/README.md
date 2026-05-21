# Azure Functions Deep Dive (4/6): Dispatcher와 Invocation — 함수 호출이 워커에 도달하기까지

Azure Functions Deep Dive 시리즈 4편 예제 코드입니다.

## 학습 목표

- dispatcher는 한 번의 invocation을 어떤 단계로 나눠 처리할까요?
- invocation context는 어디서 만들어지고 누가 해제할까요?
- `maxConcurrentRequests`, `batchSize` 같은 동시성 제어는 어디에서 실제로 영향을 줄까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_dispatcher.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-functions-deep-dive
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/04-dispatcher-and-invocation/step01_dispatcher.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-functions-deep-dive/ko/04-dispatcher-and-invocation.md)
