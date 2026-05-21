# Azure Functions Deep Dive (3/6): gRPC 이벤트 스트림 — 호스트와 워커는 무엇을 주고받는가

Azure Functions Deep Dive 시리즈 3편 예제 코드입니다.

## 학습 목표

- 호스트-워커 gRPC 스트림에는 어떤 메시지가 어떤 방식으로 실릴까요?
- 스트림이 끊기면 호스트와 워커는 각각 무엇을 가정할까요?
- 큰 페이로드는 이 스트림 위를 어떻게 지나가며, 어디에서 한계가 드러날까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_grpc_stream.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-functions-deep-dive
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/03-grpc-event-stream/step01_grpc_stream.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-functions-deep-dive/ko/03-grpc-event-stream.md)
