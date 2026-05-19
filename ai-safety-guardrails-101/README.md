# ai-safety-guardrails-101

`ai-safety-guardrails-101` 시리즈의 예제 코드 저장소입니다. 모든 예제는 오프라인에서 실행 가능한 mock 기반입니다.

## 요구사항

- Python 3.11+

## 설치

```bash
pip install -r requirements.txt
```

## 실행

```bash
python ko/02-prompt-injection-defense/step01_prompt_injection_detector.py
python en/10-production-guardrail-system/step01_guardrail_pipeline.py
python -m pytest tests/ -v
```

## 구조

- `common.py` - 가드레일 공통 유틸리티
- `ko/`, `en/` - 에피소드별 단일 실행 스크립트
- `tests/` - 에피소드별 행동 테스트
