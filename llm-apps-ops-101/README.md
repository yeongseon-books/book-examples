# llm-apps-ops-101

LLM 앱 운영 101 시리즈를 위한 예제 코드 저장소입니다. `ko/`는 한국어 로그 메시지·프롬프트·샘플 텍스트를 사용하고, `en/`은 동일 로직을 영어로 제공합니다.

## Structure

- `ko/ep01_monitoring_and_logging.py`: 구조화 로거 + 계측 래퍼
- `ko/ep02_cost_tracking.py`: 토큰 비용 계산 + TTL 캐시
- `ko/ep03_evaluation.py`: LLM-as-judge 평가기 + 배치 평가
- `ko/ep04_security.py`: 입력 검증 + 출력 필터
- `ko/ep05_deployment.py`: FastAPI LLM 서버
- `ko/ep06_ops_complete.py`: 통합 운영 서버
- `en/`: English counterparts with the same logic

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export GROQ_API_KEY=your_key_here
```

## Run examples

```bash
python3 -m py_compile ko/*.py en/*.py
python3 ko/ep01_monitoring_and_logging.py
python3 en/ep02_cost_tracking.py
uvicorn ko.ep05_deployment:app --reload
uvicorn en.ep06_ops_complete:app --reload
```

## Notes

- The code reads `GROQ_API_KEY` from the environment and does not hardcode secrets.
- FastAPI examples keep request/response payloads simple and avoid `model_dump()`.
