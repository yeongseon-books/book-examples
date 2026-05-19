# linear-algebra-101 예제 코드

이 저장소는 linear-algebra-101 시리즈의 10개 에피소드를 실행 가능한 NumPy 예제로 정리한 프로젝트입니다.

- `en/`, `ko/`에 동일한 에피소드 구조를 제공합니다.
- 각 에피소드는 `step01_example.py`를 실행하면 핵심 계산과 검증 출력을 확인할 수 있습니다.
- 공통 유틸리티는 `common.py`에 모아 두었습니다.
- 검증은 `pytest -q`로 실행하며, 에피소드별 동작 테스트를 포함합니다.

## 실행 방법

```bash
pip install -r requirements.txt
pytest -q
```

