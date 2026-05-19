# ai-web-dev-101

`ai-web-dev-101` 시리즈의 예제 코드 저장소입니다. 모든 예제는 오프라인 실행 가능한 mock 기반으로 구성되어 있으며, AI 웹 개발의 핵심 개념을 에피소드별로 작게 검증할 수 있게 설계했습니다.

## 요구사항

- Python 3.11+

## 설치

```bash
pip install -r requirements.txt
```

## 실행

```bash
python ko/01-hello-ai-api/step01_first_call.py
python ko/07-eval-improve/step01_eval_loop.py
python -m pytest tests/ -v
```

## 디렉토리 맵

- `common.py` - 공통 mock LLM, mock tools, 안전 계산 유틸리티
- `ko/` - 한국어 에피소드별 예제 (01-07)
- `tests/` - 에피소드별 스모크/행동 테스트

## 에피소드 인덱스

- `ko/01-hello-ai-api/` - [01-hello-ai-api.md](https://github.com/yeongseon-books/book-content/blob/master/content/ai-web-dev-101/ko/01-hello-ai-api.md)
- `ko/02-prompt-engineering/` - [02-prompt-engineering.md](https://github.com/yeongseon-books/book-content/blob/master/content/ai-web-dev-101/ko/02-prompt-engineering.md)
- `ko/03-ai-chatbot/` - [03-ai-chatbot.md](https://github.com/yeongseon-books/book-content/blob/master/content/ai-web-dev-101/ko/03-ai-chatbot.md)
- `ko/04-rag-intro/` - [04-rag-intro.md](https://github.com/yeongseon-books/book-content/blob/master/content/ai-web-dev-101/ko/04-rag-intro.md)
- `ko/05-ai-agent/` - [05-ai-agent.md](https://github.com/yeongseon-books/book-content/blob/master/content/ai-web-dev-101/ko/05-ai-agent.md)
- `ko/06-deploy/` - [06-deploy.md](https://github.com/yeongseon-books/book-content/blob/master/content/ai-web-dev-101/ko/06-deploy.md)
- `ko/07-eval-improve/` - [07-eval-improve.md](https://github.com/yeongseon-books/book-content/blob/master/content/ai-web-dev-101/ko/07-eval-improve.md)

## 주의사항

- 이 저장소는 학습용 mock 예제입니다.
- 실서비스 연동(OpenAI/Groq API, DB, 외부 검색 API)은 포함하지 않았습니다.

## License

MIT
