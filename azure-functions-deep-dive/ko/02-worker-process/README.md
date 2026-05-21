# Azure Functions Deep Dive (2/6): Worker 프로세스 — 한 호스트에서 여러 언어 런타임이 같이 사는 법

Azure Functions Deep Dive 시리즈 2편 예제 코드입니다.

## 학습 목표

- 워커 프로세스 모델은 언어마다 어떻게 다르며, 운영적으로 무엇을 뜻할까요?
- 워커는 상태가 없다고 봐야 할까요, 아니면 인프로세스 상태를 어느 정도 믿어도 될까요?
- 워커가 OOM이나 hang에 빠지면 호스트는 어떤 신호로 그것을 감지할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_worker_process.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-functions-deep-dive
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/02-worker-process/step01_worker_process.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-functions-deep-dive/ko/02-worker-process.md)
