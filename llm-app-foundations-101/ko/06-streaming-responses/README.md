# LLM App Foundations 101 (6/6): 스트리밍 응답 처리 — 실시간으로 출력 받기

Llm App Foundations 101 시리즈 6편 예제 코드입니다.

## 학습 목표

- streaming은 응답을 더 빨리 끝내는 기술일까요, 생성 흐름을 먼저 보여주는 기술일까요?
- chunk에서 텍스트, 종료 신호, 사용량을 어떻게 읽어야 할까요?
- FastAPI 같은 서버는 모델 스트림을 사용자에게 어떻게 중계할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_basic_stream.py` | 예제 코드 |
| `step02_collect_stream.py` | 예제 코드 |
| `step03_async_stream.py` | 예제 코드 |
| `step04_stream_usage.py` | 예제 코드 |
| `step05_stream_to_file.py` | 예제 코드 |
| `step06_fastapi_stream.py` | 예제 코드 |

## 실행 방법

```bash
cd llm-app-foundations-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/06-streaming-responses/step01_basic_stream.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/llm-app-foundations-101/ko/06-streaming-responses.md)
