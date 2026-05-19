# machine-learning-101 예제 코드

이 저장소는 `machine-learning-101` 시리즈의 10개 에피소드를 실행 가능한 Python 예제로 정리한 저장소입니다.

- `scikit-learn` + `numpy` 기반으로 구성했습니다.
- 모든 예제는 고정 시드(`random_state=42`)를 사용해 재현 가능합니다.
- 데이터는 합성 데이터 또는 scikit-learn 내장 데이터만 사용합니다.
- 인터넷 연결이나 외부 데이터 다운로드 없이 실행 가능합니다.

## 구조

- `ko/`: 한국어 경로 예제 스크립트
- `en/`: 영어 경로 예제 스크립트
- `episodes/`: 실제 학습/평가 로직
- `common.py`: 공통 데이터/평가 헬퍼
- `tests/`: 에피소드별 동작 테스트

## 실행

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```
