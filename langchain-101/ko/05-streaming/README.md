# LangChain 101 (5/6): Streaming — 실시간 출력 처리

Langchain 101 시리즈 5편 예제 코드입니다.

## 학습 목표

- `stream()`과 `astream()`은 사용자 경험과 서버 구조를 어떻게 다르게 만들까요?
- 청크를 다시 모을 때 빈 chunk와 중간 오류를 어떻게 다뤄야 할까요?
- FastAPI 스트리밍 엔드포인트에서는 어떤 경계에서 backpressure와 예외를 처리해야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_sync_stream.py` | 예제 코드 |
| `step02_async_stream.py` | 예제 코드 |

## 실행 방법

```bash
cd langchain-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/05-streaming/step01_sync_stream.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/langchain-101/ko/05-streaming.md)
