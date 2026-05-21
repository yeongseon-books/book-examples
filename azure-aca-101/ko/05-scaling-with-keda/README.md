# Azure Container Apps 101 (5/7): 스케일링 — KEDA scaler와 zero-to-N

Azure Aca 101 시리즈 5편 예제 코드입니다.

## 학습 목표

- Azure Container Apps는 선언형 스케일링 신호를 바탕으로 replica 수를 어떻게 결정할까요?
- 내장 HTTP/TCP 규칙과 사용자 정의 KEDA scaler의 차이는 무엇일까요?
- `min-replicas 0`(scale-to-zero)는 언제 안전하고, 언제 위험할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_keda_scaling.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-aca-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/05-scaling-with-keda/step01_keda_scaling.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-aca-101/ko/05-scaling-with-keda.md)
