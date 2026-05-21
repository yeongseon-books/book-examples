# Incident Response 101 (10/10): Incident Runbook 만들기

Incident Response 101 시리즈 10편 예제 코드입니다.

## 학습 목표

- incident 대응 지식을 왜 한 runbook으로 묶어야 할까요?
- severity 표와 온콜 일정은 runbook 안에서 어떻게 연결될까요?
- 커뮤니케이션 템플릿과 대응 단계는 어떤 식으로 함께 관리해야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `1_severity.py` | 예제 코드 |
| `4.py` | 예제 코드 |
| `6.py` | 예제 코드 |
| `jinja2.py` | 예제 코드 |
| `runbook.py` | 예제 코드 |
| `snippet.yaml` | 예제 코드 |
| `step01_example.py` | 예제 코드 |

## 실행 방법

```bash
cd incident-response-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/10-incident-runbook/1_severity.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/incident-response-101/ko/10-incident-runbook.md)
