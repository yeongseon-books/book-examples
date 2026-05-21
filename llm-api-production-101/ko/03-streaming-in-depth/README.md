# LLM API Production 101 (3/6): 스트리밍 심화 — 청크 처리와 오류 복구

Llm Api Production 101 시리즈 3편 예제 코드입니다.

## 학습 목표

- 스트리밍은 최종 문자열 하나가 아니라 왜 부분 상태를 가진 세션으로 봐야 할까요?
- 텍스트가 없는 chunk와 중간 실패는 어떤 상태로 다뤄야 할까요?
- 스트리밍 실패 뒤 재시도할 때 무엇을 보존하고 무엇을 다시 만들어야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_chunk_loop.py` | 예제 코드 |
| `step02_timeout_and_recovery.py` | 예제 코드 |

## 실행 방법

```bash
cd llm-api-production-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/03-streaming-in-depth/step01_chunk_loop.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/llm-api-production-101/ko/03-streaming-in-depth.md)
