# rag-deep-dive 예제 코드

`rag-deep-dive` 시리즈(총 6화)의 에피소드별 실행 가능한 Python 예제입니다.

- `ko/`, `en/`에 동일한 구조로 에피소드 스크립트를 제공합니다.
- 외부 LLM/임베딩 API 없이 `numpy` 기반 mock 임베딩/검색으로 동작합니다.
- 테스트는 `pytest -q`로 실행합니다.

## 실행

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```
