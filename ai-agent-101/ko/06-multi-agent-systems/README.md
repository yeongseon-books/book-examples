# AI Agent 101 (6/10): Multi-Agent 시스템

Ai Agent 101 시리즈 6편 예제 코드입니다.

## 학습 목표

- single agent로 충분한 업무와 multi-agent가 필요한 업무는 어디서 갈라질까요?
- supervisor, worker, handoff 계약은 각각 어떤 책임을 가져야 할까요?
- agent를 여러 개로 나눌수록 비용과 실패 지점은 어떻게 늘어날까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `handoff.py` | 예제 코드 |
| `orchestrator.py` | 예제 코드 |
| `peer_to_peer.py` | 예제 코드 |
| `step01_supervisor_handoff.py` | 예제 코드 |

## 실행 방법

```bash
cd ai-agent-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/06-multi-agent-systems/handoff.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/ai-agent-101/ko/06-multi-agent-systems.md)
