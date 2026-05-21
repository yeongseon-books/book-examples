# LLM App Foundations 101 (5/6): 대화 상태 관리 — 멀티턴 챗봇 만들기

Llm App Foundations 101 시리즈 5편 예제 코드입니다.

## 학습 목표

- 멀티턴 챗봇의 기억은 모델 안에 있을까요, 요청 안에 있을까요?
- 전체 이력, 슬라이딩 윈도우, 요약 압축은 언제 갈라질까요?
- context overflow를 요청 실패 전에 어떻게 감지할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_stateless_demo.py` | 예제 코드 |
| `step02_full_history.py` | 예제 코드 |
| `step03_sliding_window.py` | 예제 코드 |
| `step04_summary_compression.py` | 예제 코드 |
| `step05_token_budget_guard.py` | 예제 코드 |
| `step06_cli_chatbot.py` | 예제 코드 |

## 실행 방법

```bash
cd llm-app-foundations-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/05-conversation-state/step01_stateless_demo.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/llm-app-foundations-101/ko/05-conversation-state.md)
