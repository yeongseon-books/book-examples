# ai-data-preparation-101

`ai-data-preparation-101` 시리즈의 예제 코드 저장소입니다. 모든 예제는 오프라인 실행 가능한 mock 기반으로 구성되어 있으며, 데이터 준비의 핵심 개념을 에피소드별로 작게 검증할 수 있게 설계했습니다.

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
python ko/01-why-data-preparation-matters/step01_quality_report.py
python en/10-production-data-pipeline/step01_pipeline_orchestrator.py
python -m pytest tests/ -v
```

## 디렉토리 맵

- `common.py` - 공통 mock 데이터셋, 정제/분할/익명화 유틸리티
- `ko/` - 한국어 에피소드별 예제 (01-10)
- `en/` - `ko/`와 동일 로직의 영어 예제
- `tests/` - 에피소드별 스모크/행동 테스트

## 주의사항

- 이 저장소는 학습용 mock 예제입니다.
- 실서비스 연동(API 키, 외부 데이터 다운로드)은 포함하지 않았습니다.

## License

MIT
