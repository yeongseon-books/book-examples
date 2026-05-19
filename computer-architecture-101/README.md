# computer-architecture-101 예제 코드

`computer-architecture-101` 시리즈의 에피소드별 학습 예제를 오프라인에서 바로 실행하고 테스트할 수 있도록 정리한 저장소입니다.

## 구성

- `ko/01-what-is-computer-architecture.py`
- `ko/02-data-representation.py`
- `ko/03-cpu-and-instructions.py`
- `ko/04-registers-and-alu.py`
- `ko/05-memory-organization.py`
- `ko/06-cache-and-locality.py`
- `ko/07-pipelining.py`
- `ko/08-io-and-devices.py`
- `ko/09-parallelism-and-multicore.py`
- `ko/10-understanding-performance.py`
- `en/`는 `ko/`와 동일 로직을 영어 경로로 미러링했습니다.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 실행

```bash
pip install -r requirements.txt
python ko/01-what-is-computer-architecture.py
python en/10-understanding-performance.py
```

## 테스트

```bash
pytest tests/ -q
```

## 원본

- https://github.com/yeongseon-books/book-content/tree/master/content/computer-architecture-101
