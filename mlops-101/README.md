# mlops-101

`mlops-101` 시리즈 예제 코드 저장소입니다. 모든 예제는 오프라인에서 동작하는 in-memory mock 기반으로 작성했으며, 실제 MLflow/DVC/클라우드 연동은 포함하지 않았습니다.

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
python ko/01-what-is-mlops/step01_mlops_loop.py
python en/10-production-ml-system/step01_production_system.py
pytest -q
```

## 구성

- `common.py`: 실험 추적, 데이터 버전 저장소, 학습 파이프라인, 모델 레지스트리, 서빙/모니터링, 드리프트 감지, 재학습 트리거, 피처 스토어, 통합 시스템
- `ko/`, `en/`: 10개 에피소드별 실행 스크립트 (ko/en 미러)
- `tests/`: 에피소드 단위 행동 테스트
