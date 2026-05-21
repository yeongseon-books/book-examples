# Azure Container Apps Deep Dive (3/6): Revision과 트래픽 분할 — Envoy 가중치는 어디에서 오는가

Azure Aca Deep Dive 시리즈 3편 예제 코드입니다.

## 학습 목표

- 어떤 변경은 새 Revision을 만들고, 어떤 변경은 만들지 않을까요?
- single revision mode와 multiple revision mode는 운영상 무엇을 바꿀까요?
- label과 traffic weight는 각각 어떤 다른 라우팅 문제를 풀까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_revision_split.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-aca-deep-dive
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/03-revision-and-traffic-split/step01_revision_split.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-aca-deep-dive/ko/03-revision-and-traffic-split.md)
