# Azure Container Apps Deep Dive (5/6): Dapr 사이드카 내부 — 컨테이너 옆에 뜨는 Go 프로세스

Azure Aca Deep Dive 시리즈 5편 예제 코드입니다.

## 학습 목표

- ACA에서 Dapr를 켠다는 것은 런타임에 정확히 무엇이 추가된다는 뜻일까요?
- sidecar injection은 어떤 upstream 모델로 이해하는 편이 가장 정확할까요?
- localhost 포트 3500, 50001은 왜 중요한 운영 계약일까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_dapr_sidecar.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-aca-deep-dive
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/05-dapr-sidecar-internals/step01_dapr_sidecar.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-aca-deep-dive/ko/05-dapr-sidecar-internals.md)
