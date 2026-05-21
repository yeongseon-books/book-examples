# LLM API Production 101 (1/6): 구조화 출력 — JSON 모드와 응답 스키마

Llm Api Production 101 시리즈 1편 예제 코드입니다.

## 학습 목표

- 자유 형식 텍스트 파싱은 운영 환경에서 왜 금방 깨질까요?
- JSON 모드는 무엇을 보장하고, 스키마 검증은 무엇을 따로 보장할까요?
- 구조화 출력 계약이 깨졌을 때 어디서 멈추고 무엇을 기록해야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_json_mode.py` | 예제 코드 |
| `step02_schema_validation.py` | 예제 코드 |
| `step03_error_handling.py` | 예제 코드 |

## 실행 방법

```bash
cd llm-api-production-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/01-structured-output/step01_json_mode.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/llm-api-production-101/ko/01-structured-output.md)
