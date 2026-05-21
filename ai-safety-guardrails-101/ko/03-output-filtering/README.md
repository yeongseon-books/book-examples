# AI Safety & Guardrails 101 (3/10): 출력 필터링과 콘텐츠 모더레이션

Ai Safety Guardrails 101 시리즈 3편 예제 코드입니다.

## 학습 목표

- 모델 응답을 사용자에게 보내기 전에 왜 다시 데이터로 검증해야 할까요?
- 정책 위반, 민감 정보, streaming 응답은 각각 어디서 필터링해야 할까요?
- 차단된 응답을 사용자 경험으로 바꿀 때 어떤 fallback이 필요할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_output_filter_pipeline.py` | 예제 코드 |

## 실행 방법

```bash
cd ai-safety-guardrails-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/03-output-filtering/step01_output_filter_pipeline.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/ai-safety-guardrails-101/ko/03-output-filtering.md)
