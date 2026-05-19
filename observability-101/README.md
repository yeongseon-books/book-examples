# observability-101 예제 코드

이 저장소는 `observability-101` 시리즈의 10개 에피소드를 실행 가능한 Python 예제로 정리한 저장소입니다.

- 본 예제는 모두 메모리 기반 mock 구현입니다.
- 실제 Prometheus, Grafana, OpenTelemetry, Jaeger, Loki, PagerDuty 백엔드는 사용하지 않습니다.
- 표준 라이브러리와 `pytest`만 사용합니다.

## 구성

- `common.py`: MetricRegistry, StructuredLogger, Tracer, Dashboard, AlertEngine, OnCallRouter, SLOTracker, CardinalityAnalyzer, ObservabilityStack
- `ko/`: 한국어 에피소드 대응 스크립트 10개
- `en/`: 영어 에피소드 대응 스크립트 10개(동일 로직 미러)
- `tests/`: 에피소드별 행동 테스트

## 실행

```bash
python -m pip install -r requirements.txt
pytest -q
```

## 주의

이 저장소는 학습용 in-memory 모델이므로 실제 운영 환경 대체용이 아닙니다.
