# Azure Container Apps 101 (4/7): Ingress와 트래픽 분할 — revision 기반 배포 전략

Azure Aca 101 시리즈 4편 예제 코드입니다.

## 학습 목표

- ACA의 관리형 Ingress는 무엇을 책임지고(TLS, external/internal 노출, Revision 라우팅), 무엇은 책임지지 않을까요?
- `external`, `internal`, `disabled` ingress mode의 차이는 정확히 무엇일까요?
- Single mode와 Multiple mode는 트래픽 분배 동작을 어떻게 바꿀까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_ingress_split.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-aca-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/04-ingress-and-traffic-split/step01_ingress_split.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-aca-101/ko/04-ingress-and-traffic-split.md)
