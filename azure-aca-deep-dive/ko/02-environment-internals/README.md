# Azure Container Apps Deep Dive (2/6): Environment 내부 — 네트워크·관측·Dapr 스코프의 경계

Azure Aca Deep Dive 시리즈 2편 예제 코드입니다.

## 학습 목표

- Environment는 왜 단순한 부모 리소스가 아니라 실제 격리 경계일까요?
- 네트워크 범위는 Revision이나 App이 아니라 왜 Environment에서 시작될까요?
- Log Analytics workspace를 Environment 수준에서 공유한다는 말은 운영상 무엇을 뜻할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_environment_boundary.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-aca-deep-dive
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/02-environment-internals/step01_environment_boundary.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-aca-deep-dive/ko/02-environment-internals.md)
