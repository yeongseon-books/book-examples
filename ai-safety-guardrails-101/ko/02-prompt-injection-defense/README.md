# AI Safety & Guardrails 101 (2/10): Prompt Injection 방어

Ai Safety Guardrails 101 시리즈 2편 예제 코드입니다.

## 학습 목표

- Prompt injection은 언제 데이터가 지시로 바뀌면서 시작될까요?
- 직접 injection과 간접 injection은 방어 위치가 어떻게 다를까요?
- Red team 사례를 regression set으로 남기려면 무엇을 기록해야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `direct_injection.py` | 예제 코드 |
| `llm_judge.py` | 예제 코드 |
| `red_team.py` | 예제 코드 |
| `snippet.py` | 예제 코드 |
| `snippet_06.py` | 예제 코드 |
| `snippet_07.py` | 예제 코드 |
| `step01_prompt_injection_detector.py` | 예제 코드 |

## 실행 방법

```bash
cd ai-safety-guardrails-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/02-prompt-injection-defense/direct_injection.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/ai-safety-guardrails-101/ko/02-prompt-injection-defense.md)
