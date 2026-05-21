# Azure Kubernetes Service 101 (7/7): 모니터링과 운영 — Container Insights, 로그, 알람

Azure Aks 101 시리즈 7편 예제 코드입니다.

## 학습 목표

- Container Insights는 AKS 운영에서 무엇을 가장 빠르게 보여 줄까요?
- 로그와 메트릭은 왜 같은 관측 데이터가 아니라 서로 다른 질문에 답할까요?
- Log Analytics에서 어떤 KQL 테이블과 쿼리부터 익히는 편이 좋을까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_monitoring_queries.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-aks-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/07-monitoring-and-ops/step01_monitoring_queries.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-aks-101/ko/07-monitoring-and-ops.md)
