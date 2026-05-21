# LangGraph 101 (5/6): 멀티 에이전트 시스템

Langgraph 101 시리즈 5편 예제 코드입니다.

## 학습 목표

- 멀티 에이전트는 여러 모델을 붙이는 일이 아니라 어떤 책임 분리 구조일까요?
- 각 에이전트 노드가 공유 state를 읽고 쓸 때 무엇을 제한해야 할까요?
- handoff나 supervisor 경계가 흐리면 어떤 운영 문제가 생길까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_dual_agent_routing.py` | 예제 코드 |
| `step02_supervisor_pattern.py` | 예제 코드 |

## 실행 방법

```bash
cd langgraph-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/05-multi-agent/step01_dual_agent_routing.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/langgraph-101/ko/05-multi-agent.md)
