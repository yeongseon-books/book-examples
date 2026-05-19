# devops-101 예제 코드

`devops-101` 시리즈의 에피소드별 실습 코드를 담은 저장소이며, Docker/클라우드 없이 순수 Python으로 DevOps 개념을 시뮬레이션합니다.

## 구성

- `common.py`: 공통 이벤트/명령 실행 유틸리티
- `ko/01-what-is-devops.py`
- `ko/02-ci-pipeline.py`
- `ko/03-cd-and-deployment.py`
- `ko/04-environments-and-config.py`
- `ko/05-infrastructure-as-code.py`
- `ko/06-containers-and-build.py`
- `ko/07-monitoring-and-alerting.py`
- `ko/08-logging-and-analysis.py`
- `ko/09-incident-and-oncall.py`
- `ko/10-operable-devops-flow.py`
- `en/`: 동일한 예제를 영어 경로로 미러링한 파일
- `tests/`: 에피소드별 pytest

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 실행

```bash
python ko/01-what-is-devops.py
python en/10-operable-devops-flow.py
```

## 테스트

```bash
pip install -r requirements.txt
pytest -q
```

## 원본

- https://github.com/yeongseon-books/book-content/tree/master/content/devops-101
