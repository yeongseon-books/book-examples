# model-evaluation-101

`model-evaluation-101` 시리즈의 에피소드별 예제 코드 저장소입니다.

모든 예제는 `scikit-learn`과 `numpy` 기반의 합성 데이터만 사용하며, 동일 시드로 항상 재현 가능합니다.

## 요구사항

- Python 3.11+

## 설치

```bash
pip install -r requirements.txt
```

## 실행

```bash
python ko/01-why-evaluation-is-hard/step01_leakage_demo.py
python en/10-evaluation-report/step01_evaluation_report.py
pytest -q
```

## 디렉토리

- `common.py`: 공통 데이터/평가 유틸리티입니다.
- `ko/`: 한국어 에피소드 기준 예제 코드입니다.
- `en/`: 영어 미러 예제 코드입니다.
- `tests/`: 에피소드별 행동 검증 테스트입니다.
