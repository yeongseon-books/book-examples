# docker-101

`docker-101` 시리즈의 예제 코드 저장소입니다. 모든 예제는 Docker CLI/daemon 없이 오프라인에서 동작하는 파서/검증기/시뮬레이터 기반으로 구성했습니다.

## 요구사항

- Python 3.11+

## 설치

```bash
pip install -r requirements.txt
```

## 실행

```bash
python ko/01-what-is-docker/step01_manual_loop.py
python en/10-production-docker/step01_production_policy_check.py
python -m pytest tests/ -v
```

## 디렉토리 맵

- `common.py` - Dockerfile/Compose 파서, lint/검증기, 레이어 시뮬레이터
- `ko/` - 한국어 에피소드별 예제 (01-10)
- `en/` - `ko/`와 동일 로직의 영어 예제
- `tests/` - 에피소드별 동작 테스트

## 주의사항

- 이 저장소는 학습용 오프라인 mock 예제입니다.
- 실제 Docker 엔진 호출 없이 정적 아티팩트 검증만 수행합니다.

## License

MIT
