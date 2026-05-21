# Azure Container Apps 101 (7/7): 모니터링과 운영 — Log Analytics와 Application Insights

Azure Aca 101 시리즈 7편 예제 코드입니다.

## 학습 목표

- ACA 관측성은 어떤 계층 구조로 나뉠까요?
- `ContainerAppConsoleLogs_CL`와 `ContainerAppSystemLogs_CL`는 무엇이 다를까요?
- Log Analytics에서 Revision 기준으로 로그를 묶는 KQL 쿼리는 어떻게 작성할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_observability_queries.py` | 예제 코드 |

## 실행 방법

```bash
cd azure-aca-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/07-monitoring-and-ops/step01_observability_queries.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/azure-aca-101/ko/07-monitoring-and-ops.md)
