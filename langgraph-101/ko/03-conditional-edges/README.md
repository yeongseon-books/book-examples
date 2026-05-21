# LangGraph 101 (3/6): 조건부 엣지와 분기 흐름

Langgraph 101 시리즈 3편 예제 코드입니다.

## 학습 목표

- 조건부 엣지는 단순 if문과 무엇이 다르게 그래프 실행을 통제할까요?
- 분기 함수가 예상하지 못한 값을 돌려주면 어떤 실패가 생길까요?
- default route를 코드로 고정해 두면 운영에서 어떤 디버깅이 쉬워질까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_router_function.py` | 예제 코드 |
| `step02_sentiment_branch_graph.py` | 예제 코드 |

## 실행 방법

```bash
cd langgraph-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/03-conditional-edges/step01_router_function.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/langgraph-101/ko/03-conditional-edges.md)
