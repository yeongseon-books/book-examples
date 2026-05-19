# functional-programming-101

`functional-programming-101` 시리즈의 예제 코드 저장소입니다.
모든 예제는 Python 표준 라이브러리만 사용하며 오프라인에서 실행 가능합니다.

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
python ko/01-what-is-fp.py
python en/10-oop-and-fp-balance.py
pytest -q
```

## 디렉토리

- `common.py`: 불변 데이터, 함수 합성, 지연 스트림 등 공통 유틸리티입니다.
- `ko/`: 한국어 기준 에피소드별 실행 스크립트입니다.
- `en/`: `ko/`와 동일한 예제 스크립트입니다.
- `tests/`: 에피소드별 동작 검증 테스트입니다.
