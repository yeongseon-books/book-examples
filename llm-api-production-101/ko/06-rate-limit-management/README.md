# LLM API Production 101 (6/6): 속도 제한 관리 — Rate Limit 대응 패턴

Llm Api Production 101 시리즈 6편 예제 코드입니다.

## 학습 목표

- rate limit 대응은 429 뒤에 처리하는 일일까요, 429 전에 흐름을 조절하는 일일까요?
- 토큰 버킷과 슬라이딩 윈도우는 각각 어떤 트래픽에 맞을까요?
- provider 429를 받은 뒤에도 애플리케이션은 무엇을 해야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_rate_limiters.py` | 예제 코드 |

## 실행 방법

```bash
cd llm-api-production-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/06-rate-limit-management/step01_rate_limiters.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/llm-api-production-101/ko/06-rate-limit-management.md)
