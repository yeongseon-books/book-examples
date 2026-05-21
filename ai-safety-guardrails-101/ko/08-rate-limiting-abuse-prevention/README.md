# AI Safety & Guardrails 101 (8/10): Rate Limiting과 남용 방지

Ai Safety Guardrails 101 시리즈 8편 예제 코드입니다.

## 학습 목표

- LLM rate limiting은 왜 요청 수보다 리소스 소비를 기준으로 봐야 할까요?
- 토큰, 비용, 사용자·키 단위 한도는 각각 어떤 abuse를 막을까요?
- 한도 초과 시 차단과 완화 응답은 어떻게 나눠야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `escalation.py` | 예제 코드 |
| `ip.py` | 예제 코드 |
| `snippet.py` | 예제 코드 |
| `snippet_04.py` | 예제 코드 |
| `snippet_05.py` | 예제 코드 |
| `step01_token_bucket.py` | 예제 코드 |
| `token_bucket_quota.py` | 예제 코드 |

## 실행 방법

```bash
cd ai-safety-guardrails-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/08-rate-limiting-abuse-prevention/escalation.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/ai-safety-guardrails-101/ko/08-rate-limiting-abuse-prevention.md)
