# sql-101 예제 코드

sqlite3 기반으로 sql-101 시리즈(EP01~EP10)의 핵심 SQL 문법을 실행 가능한 파이썬 코드로 정리한 저장소입니다.

- `common.py`: 공통 스키마/시드 데이터
- `ko/`, `en/`: 에피소드별 예제 스크립트(미러 구조)
- `tests/`: 에피소드별 pytest

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```
