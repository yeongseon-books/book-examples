# LangGraph 101 (2/6): 상태 관리와 체크포인트

Langgraph 101 시리즈 2편 예제 코드입니다.

## 학습 목표

- LangGraph에서 state를 단일 진실 공급원으로 두면 어떤 버그를 줄일 수 있을까요?
- checkpoint는 메모리 저장과 무엇이 다르고, 언제 복구 경계가 될까요?
- MemorySaver 예제를 운영 코드로 착각하면 어떤 한계에 부딪힐까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_memorysaver_thread_state.py` | 예제 코드 |
| `step02_multi_turn_memory.py` | 예제 코드 |

## 실행 방법

```bash
cd langgraph-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/02-state-and-checkpoints/step01_memorysaver_thread_state.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/langgraph-101/ko/02-state-and-checkpoints.md)
