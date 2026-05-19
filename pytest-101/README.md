# pytest-101 예제 코드

이 저장소는 pytest-101 시리즈의 메타 예제 저장소입니다.

- 각 에피소드마다 작은 SUT 모듈과 테스트를 제공합니다.
- `ko/`와 `en/`은 동일한 구조로 미러링됩니다.
- 실제 학습은 `tests/`에서 pytest 기능 중심으로 진행합니다.

빠른 실행:

```bash
pip install -r requirements.txt
pytest -q
```

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```
