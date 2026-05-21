# API Design 101 (6/10): Pagination과 filtering

Api Design 101 시리즈 6편 예제 코드입니다.

## 학습 목표

- offset / limit 방식은 어디까지 단순하고 어디서부터 한계가 드러날까요?
- cursor 기반 pagination은 어떤 문제를 해결하며 어떤 것을 포기할까요?
- sorting, filtering, searching은 어떤 규칙으로 분리해야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `cursor.json` | 예제 코드 |
| `cursor.py` | 예제 코드 |
| `offset.json` | 예제 코드 |
| `pagination_example.py` | 예제 코드 |
| `snippet.py` | 예제 코드 |
| `snippet.sql` | 예제 코드 |
| `snippet_02.sql` | 예제 코드 |
| `step01_pagination_filter.py` | 예제 코드 |

## 실행 방법

```bash
cd api-design-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/06-pagination-and-filtering/cursor.json
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/api-design-101/ko/06-pagination-and-filtering.md)
