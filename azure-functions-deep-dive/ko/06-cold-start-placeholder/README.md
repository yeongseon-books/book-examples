# Azure Functions Deep Dive (6/6): 콜드 스타트와 Placeholder Mode — 새 인스턴스가 만들어질 때

Azure Functions Deep Dive 시리즈 6편 예제 코드입니다.

## 학습 목표

- 호스트 부팅, 워커 시작, JIT 중 어느 부분이 cold start에서 가장 비쌀까요?
- Placeholder 인스턴스는 정확히 무엇을 미리 준비해 둘까요?
- Premium의 always-ready 인스턴스는 placeholder와 무엇이 다를까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_placeholder.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-functions-deep-dive
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/06-cold-start-placeholder/step01_placeholder.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-functions-deep-dive/ko/06-cold-start-placeholder.md)
