# LLM App Foundations 101 (3/6): 프롬프트 엔지니어링 기초 — System·User·Assistant 역할

Llm App Foundations 101 시리즈 3편 예제 코드입니다.

## 학습 목표

- system, user, assistant 역할은 각각 어떤 책임을 맡을까요?
- system message는 왜 단순한 첫 문장보다 강한 기준이 될까요?
- temperature, top_p, few-shot은 답변 안정성에 어떤 영향을 줄까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_system_effect.py` | 예제 코드 |
| `step02_multiturn_history.py` | 예제 코드 |
| `step03_temperature.py` | 예제 코드 |
| `step04_structured_prompt.py` | 예제 코드 |
| `step05_few_shot_basic.py` | 예제 코드 |

## 실행 방법

```bash
cd llm-app-foundations-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/03-prompt-engineering-basics/step01_system_effect.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/llm-app-foundations-101/ko/03-prompt-engineering-basics.md)
