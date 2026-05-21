# LangGraph 101 (1/6): LangGraph 소개와 그래프 기초

Langgraph 101 시리즈 1편 예제 코드입니다.

## 학습 목표

- LangGraph는 왜 단순 체인보다 명시적인 상태 기계로 보는 편이 좋을까요?
- 노드와 엣지, state는 각각 실행 흐름에서 어떤 책임을 나눌까요?
- 첫 그래프를 실행한 뒤에는 최종 문장보다 어떤 state 값을 먼저 확인해야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_two_node_graph.py` | 예제 코드 |
| `step02_three_node_pipeline.py` | 예제 코드 |

## 실행 방법

```bash
cd langgraph-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/01-graph-basics/step01_two_node_graph.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/langgraph-101/ko/01-graph-basics.md)
