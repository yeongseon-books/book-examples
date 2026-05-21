# AI App Patterns 101 (1/6): 챗봇 패턴 — 대화 이력과 상태 관리

Ai App Patterns 101 시리즈 1편 예제 코드입니다.

## 학습 목표

- 모델이 이전 대화를 기억하지 않는다면 챗봇의 “기억”은 어디에 있어야 할까요?
- 대화 이력을 계속 붙이면 언제 비용과 지연 시간이 먼저 문제가 될까요?
- 세션별 이력은 언제 메모리에 두고 언제 외부 저장소로 옮겨야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_session_chatbot.py` | 예제 코드 |
| `step02_summary_chatbot.py` | 예제 코드 |

## 실행 방법

```bash
cd ai-app-patterns-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/01-chatbot-pattern/step01_session_chatbot.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/ai-app-patterns-101/ko/01-chatbot-pattern.md)
