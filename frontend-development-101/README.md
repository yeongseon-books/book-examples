# frontend-development-101

`frontend-development-101` 시리즈의 예제 코드 저장소입니다. 모든 예제는 오프라인 실행 가능한 Python 기반 검증/시뮬레이션으로 구성했습니다.

## 요구사항

- Python 3.11+

## 설치

```bash
pip install -r requirements.txt
```

## 실행

```bash
python ko/01-what-is-frontend-development/step01_ep01.py
python en/10-building-a-small-frontend-app/step01_ep10.py
python -m pytest tests/ -v
```

## 디렉토리 맵

- `common.py` - HTML/CSS/JS 분석기와 시뮬레이터 유틸리티입니다.
- `ko/` - 한국어 에피소드별 예제(01-10)입니다.
- `en/` - `ko/`와 동일 구조의 영어 예제입니다.
- `tests/` - 에피소드별 행동 테스트입니다.

## 주의사항

- 브라우저 실행, npm/node 연동 없이 정적 자산 분석과 mock 시뮬레이션만 포함합니다.
- 학습 목적의 오프라인 예제이며 외부 API 키/서비스 의존성은 없습니다.

## License

MIT
