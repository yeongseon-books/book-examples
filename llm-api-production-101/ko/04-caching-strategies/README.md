# LLM API Production 101 (4/6): 캐싱 전략 — 비용과 지연 시간 줄이기

Llm Api Production 101 시리즈 4편 예제 코드입니다.

## 학습 목표

- LLM 캐시는 응답 저장소가 아니라 왜 요청 동일성 계약으로 봐야 할까요?
- 캐시 키에는 프롬프트 외에 어떤 값이 들어가야 할까요?
- 어떤 경로는 비용이 커도 캐시하지 않는 편이 안전할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_ttl_cache.py` | 예제 코드 |

## 실행 방법

```bash
cd llm-api-production-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/04-caching-strategies/step01_ttl_cache.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/llm-api-production-101/ko/04-caching-strategies.md)
