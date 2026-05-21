# Azure Functions 101 (7/7): 모니터링과 운영 기초

Azure Functions 101 시리즈 7편 예제 코드입니다.

## 학습 목표

- Application Insights와 Log Analytics는 Azure Functions 운영에서 어떤 역할로 나뉠까요?
- 함수별 지연, 실패율, 의존성 호출을 보려면 어떤 쿼리를 먼저 갖고 있어야 할까요?
- Live Metrics와 stream logs는 언제 각각 더 유리할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_monitoring_queries.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-functions-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/07-monitoring-and-ops/step01_monitoring_queries.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-functions-101/ko/07-monitoring-and-ops.md)
