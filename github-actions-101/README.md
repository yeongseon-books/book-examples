# github-actions-101

`github-actions-101` 시리즈의 예제 코드 저장소입니다. 모든 예제는 오프라인에서 실행 가능한 정적 워크플로우 fixture와 Python 시뮬레이터로 구성되어 있습니다.

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
python ko/01-what-is-github-actions/step01_demo.py
python en/10-real-world-cicd-pipeline/step01_demo.py
pytest -q
```

## 구성

- `common.py`: 워크플로우 파서, 검증기, 트리거 매처, DAG 분석기, 매트릭스 확장기, 린터, 시뮬레이터
- `ko/`, `en/`: 에피소드별 예제 코드와 `.github/workflows/workflow.yml` fixture
- `tests/`: 에피소드별 행동 테스트

## 주의사항

- 실제 GitHub Actions runner, API, `act`는 사용하지 않습니다.
- 예제 secret 값은 모두 mock이며 실제 키를 포함하지 않습니다.
