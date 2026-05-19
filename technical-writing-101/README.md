# technical-writing-101 예제 코드

이 저장소는 `technical-writing-101` 시리즈의 에피소드별 파이썬 예제 코드를 제공합니다.

- `ko/`, `en/`: 에피소드별 린터/분석기 스크립트
- `fixtures/`: 테스트용 Markdown 샘플
- `tests/`: pytest 테스트

실행:

```bash
python -m pytest -q
```

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```
