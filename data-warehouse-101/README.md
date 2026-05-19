# data-warehouse-101 예제 코드

stdlib sqlite3로 데이터 웨어하우스 핵심 개념(스타 스키마, ETL, 마트)을 실행 가능한 예제로 보여줍니다.

## 구성

- `ko/01-what-is-data-warehouse.py` ~ `ko/10-warehouse-design-example.py`
- `en/01-what-is-data-warehouse.py` ~ `en/10-warehouse-design-example.py`
- `common.py`: 공통 sqlite3 스키마/시드/타이밍 유틸리티
- `tests/`: 에피소드별 행동 테스트

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 실행

```bash
python ko/01-what-is-data-warehouse.py
python en/10-warehouse-design-example.py
```

## 테스트

```bash
python -m pytest -v
```

## 원본

https://github.com/yeongseon-books/book-content/tree/master/content/data-warehouse-101
