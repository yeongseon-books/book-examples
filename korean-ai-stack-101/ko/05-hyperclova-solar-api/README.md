# Korean AI Stack 101 (5/6): HyperCLOVA X와 Solar API 사용하기

Korean Ai Stack 101 시리즈 5편 예제 코드입니다.

## 학습 목표

- 프롬프트 튜닝보다 먼저 고정해야 할 API 계약은 무엇일까요?
- HyperCLOVA X나 Solar 같은 한국어 생성 API를 도입할 때는 무엇부터 검증해야 할까요?
- 실행 예제가 왜 Groq `llama-3.1-8b-instant`를 대체 모델로 쓰는 걸까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_korean_text_generation.py` | 예제 코드 |
| `step02_summary_and_classification.py` | 예제 코드 |

## 실행 방법

```bash
cd korean-ai-stack-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/05-hyperclova-solar-api/step01_korean_text_generation.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/korean-ai-stack-101/ko/05-hyperclova-solar-api.md)
