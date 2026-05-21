# Azure Functions 101 (3/7): Host와 Worker — 함수는 누가 실행하는가

Azure Functions 101 시리즈 3편 예제 코드입니다.

## 학습 목표

- Functions Host와 언어 Worker는 왜 같은 프로세스가 아니라 분리된 프로세스일까요?
- Host와 Worker 사이의 gRPC 채널에서는 어떤 메시지 흐름이 오갈까요?
- 한 Worker 프로세스는 동시에 몇 개의 함수 호출을 처리할 수 있을까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_host_worker_flow.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-functions-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/03-host-and-worker/step01_host_worker_flow.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-functions-101/ko/03-host-and-worker.md)
