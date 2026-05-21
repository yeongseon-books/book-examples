# Azure Functions Deep Dive (1/6): 호스트 부팅 — `WebJobsScriptHostService`부터 따라가기

Azure Functions Deep Dive 시리즈 1편 예제 코드입니다.

## 학습 목표

- Functions Host는 정확히 어떤 프로세스이며, 어떤 순서로 부팅될까요?
- `host.json`은 단순 설정 파일일까요, 아니면 런타임 동작을 바꾸는 실제 구성 입력일까요?
- 호스트 시작 실패는 어디에 기록되고, 첫 번째 진단 지점은 어디일까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_host_bootstrap.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-functions-deep-dive
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/01-host-bootstrap/step01_host_bootstrap.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-functions-deep-dive/ko/01-host-bootstrap.md)
