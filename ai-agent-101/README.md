# ai-agent-101

`ai-agent-101` 시리즈의 예제 코드 저장소입니다. 모든 예제는 오프라인 실행 가능한 mock 기반으로 구성되어 있으며, 에이전트의 핵심 개념을 에피소드별로 작게 검증할 수 있게 설계했습니다.

## 요구사항

- Python 3.11+

## 설치

```bash
pip install -r requirements.txt
```

## 실행

```bash
python ko/01-what-is-an-ai-agent/step01_manual_loop.py
python en/10-building-first-agent/step01_capstone_agent.py
python -m pytest tests/ -v
```

## 디렉토리 맵

- `common.py` - 공통 mock LLM, mock tools, retry 유틸리티
- `ko/` - 한국어 에피소드별 예제 (01-10)
- `en/` - `ko/`와 동일 로직의 영어 예제
- `tests/` - 에피소드별 스모크/행동 테스트

## 주의사항

- 이 저장소는 학습용 mock 예제입니다.
- 실서비스 연동(OpenAI/Groq API, DB, 외부 검색 API)은 포함하지 않았습니다.

## License

MIT
