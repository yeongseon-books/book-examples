# harness-engineering-101

`harness-engineering-101` 시리즈의 예제 코드 저장소입니다.
모든 예제는 오프라인, 결정론적 mock 기반으로 동작합니다.

## 요구사항

- Python 3.11+

## 설치

```bash
pip install -r requirements.txt
```

## 실행

```bash
python ko/01-what-is-harness-engineering/step01_example.py
python en/10-production-harness/step01_example.py
pytest -q
```

## 구성

- `common.py`: Harness primitives (`MockLLM`, `TaskHarness`, `ContextHarness`, `ConstraintHarness`, `ToolHarness`, `TestHarness`, `FeedbackLoop`, `ApprovalGate`, `Observability`, `ProductionHarness`)
- `ko/`, `en/`: 10개 에피소드 미러 구조 예제
- `tests/`: 에피소드별 행위 테스트
