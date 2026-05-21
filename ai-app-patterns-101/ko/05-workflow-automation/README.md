# AI App Patterns 101 (5/6): 워크플로 자동화 — 다단계 체인 설계

Ai App Patterns 101 시리즈 5편 예제 코드입니다.

## 학습 목표

- 다단계 체인은 언제 단순 순차 실행이고 언제 라우팅이 필요할까요?
- 중간 결과의 타입을 고정하지 않으면 다음 단계에서 어떤 문제가 생길까요?
- 워크플로 자동화에서 실패를 한 번에 숨기지 않으려면 어디에 로그를 남겨야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_sequential_chain.py` | 예제 코드 |
| `step02_routing_workflow.py` | 예제 코드 |

## 실행 방법

```bash
cd ai-app-patterns-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/05-workflow-automation/step01_sequential_chain.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/ai-app-patterns-101/ko/05-workflow-automation.md)
