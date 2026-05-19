# incident-response-101

`incident-response-101` 시리즈 예제 코드 저장소입니다. 모든 코드는 오프라인에서 동작하는 순수 Python in-memory 시뮬레이션으로 구성했습니다.

## 요구사항

- Python 3.11+

## 설치

```bash
pip install -r requirements.txt
```

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 실행

```bash
python ko/01-what-is-incident/step01_example.py
python en/10-incident-runbook/step01_example.py
pytest -q
```

## 구성

- `common.py`: Incident 도메인 공통 프리미티브
- `ko/`, `en/`: 10개 에피소드별 실행 스크립트(동일 로직 미러)
- `tests/`: 에피소드별 행동 테스트

## 주의사항

- 외부 API(PagerDuty, Slack, Jira 등) 연동은 포함하지 않았습니다.
- 모든 동작은 결정적(deterministic)이며 메모리 내부에서만 실행됩니다.
