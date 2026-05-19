# kubernetes-101

`kubernetes-101` 시리즈의 예제 코드 저장소입니다. 모든 예제는 오프라인 mock 시뮬레이션으로 동작하며, 실제 클러스터 없이 Kubernetes 핵심 개념을 학습할 수 있게 구성했습니다.

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
python ko/01-what-is-kubernetes/step01.py
python en/10-kubernetes-in-operation/step01.py
pytest -q
```

## 구성

- `common.py`: ManifestParser, Validator/Simulator, ClusterStateSimulator 공통 로직
- `ko/`, `en/`: 에피소드별 정적 Kubernetes manifest YAML + 실행 스크립트
- `tests/`: 에피소드별 동작 검증 테스트

## 주의사항

- 이 저장소는 학습용 오프라인 시뮬레이션입니다.
- `kubectl`, `helm`, 클러스터 API 호출은 포함하지 않습니다.
