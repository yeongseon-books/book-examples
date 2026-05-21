# AI Agent 101 (5/10): Memory와 State

Ai Agent 101 시리즈 5편 예제 코드입니다.

## 학습 목표

- agent memory와 state를 같은 저장소로 보면 어떤 설계 문제가 생길까요?
- short-term memory, long-term memory, execution state는 각각 언제 필요할까요?
- context window가 부족해질 때 무엇을 요약하고 무엇을 그대로 남겨야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `long_term_memory.py` | 예제 코드 |
| `short_term_memory.py` | 예제 코드 |
| `state.py` | 예제 코드 |
| `state_04.py` | 예제 코드 |
| `step01_memory_state.py` | 예제 코드 |

## 실행 방법

```bash
cd ai-agent-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/05-memory-and-state/long_term_memory.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/ai-agent-101/ko/05-memory-and-state.md)
