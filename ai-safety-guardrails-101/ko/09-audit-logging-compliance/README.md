# AI Safety & Guardrails 101 (9/10): 감사 로깅과 컴플라이언스

Ai Safety Guardrails 101 시리즈 9편 예제 코드입니다.

## 학습 목표

- 감사 로그는 일반 디버그 로그와 무엇이 달라야 compliance에 쓸 수 있을까요?
- PII masking, append-only storage, decision rationale은 각각 어떤 증거를 남길까요?
- 자동 compliance report를 만들려면 로그 schema에 무엇이 고정되어야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `append_only.py` | 예제 코드 |
| `audit_record.py` | 예제 코드 |
| `decision_rationale.py` | 예제 코드 |
| `pii.py` | 예제 코드 |
| `snippet.py` | 예제 코드 |
| `snippet_06.py` | 예제 코드 |
| `step01_append_only_audit_log.py` | 예제 코드 |

## 실행 방법

```bash
cd ai-safety-guardrails-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/09-audit-logging-compliance/append_only.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/ai-safety-guardrails-101/ko/09-audit-logging-compliance.md)
