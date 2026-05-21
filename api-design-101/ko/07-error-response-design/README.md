# API Design 101 (7/10): Error response 설계

Api Design 101 시리즈 7편 예제 코드입니다.

## 학습 목표

- 좋은 error response는 어떤 요소로 이루어질까요?
- RFC 7807 `application/problem+json`은 왜 유용할까요?
- validation error는 어떤 모양으로 표현해야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `before_after.json` | 예제 코드 |
| `before_after_02.json` | 예제 코드 |
| `rfc_7807_problem_details_for_http_apis.json` | 예제 코드 |
| `snippet.json` | 예제 코드 |
| `snippet.py` | 예제 코드 |
| `snippet_07.json` | 예제 코드 |
| `snippet_09.py` | 예제 코드 |
| `snippet_10.py` | 예제 코드 |
| `snippet_11.json` | 예제 코드 |
| `step01_problem_json.py` | 예제 코드 |

## 실행 방법

```bash
cd api-design-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/07-error-response-design/snippet.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/api-design-101/ko/07-error-response-design.md)
