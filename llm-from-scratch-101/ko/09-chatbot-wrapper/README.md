# LLM from Scratch 101 (9/9): 직접 만든 LLM을 챗봇으로 — FastAPI + 스트리밍

Llm From Scratch 101 시리즈 9편 예제 코드입니다.

## 학습 목표

- 챗봇은 모델 외에 어떤 구성 요소를 더 필요로 할까요?
- multi-turn prompt format은 왜 직접 설계해야 할까요?
- FastAPI lifespan으로 모델을 한 번만 로드하면 무엇이 좋아질까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `episode.py` | 예제 코드 |
| `eventsource.html` | 예제 코드 |
| `server.py` | 예제 코드 |

## 실행 방법

```bash
cd llm-from-scratch-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/09-chatbot-wrapper/episode.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/llm-from-scratch-101/ko/09-chatbot-wrapper.md)
