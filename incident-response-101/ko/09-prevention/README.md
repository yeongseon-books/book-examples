# Incident Response 101 (9/10): 재발 방지

Incident Response 101 시리즈 9편 예제 코드입니다.

## 학습 목표

- 사후 분석 뒤에 왜 같은 incident가 다시 반복될까요?
- 후속 조치 추적이 없으면 어떤 문제가 생길까요?
- 회귀 테스트는 왜 재발 방지의 핵심일까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `3_guardrail.py` | 예제 코드 |
| `snippet.py` | 예제 코드 |
| `step01_example.py` | 예제 코드 |
| `toxiproxy.py` | 예제 코드 |

## 실행 방법

```bash
cd incident-response-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/09-prevention/3_guardrail.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/incident-response-101/ko/09-prevention.md)
