# AI Safety & Guardrails 101 (4/10): PII 감지와 마스킹

Ai Safety Guardrails 101 시리즈 4편 예제 코드입니다.

## 학습 목표

- PII 보호는 왜 모델에 보내는 정보와 내부에 보관하는 정보를 분리해야 할까요?
- regex, Presidio, reversible tokenization은 각각 어떤 단계에서 유용할까요?
- 응답 outbound 단계에서 다시 검사하지 않으면 어떤 유출이 생길까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_pii_redaction.py` | 예제 코드 |

## 실행 방법

```bash
cd ai-safety-guardrails-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/04-pii-detection-redaction/step01_pii_redaction.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/ai-safety-guardrails-101/ko/04-pii-detection-redaction.md)
