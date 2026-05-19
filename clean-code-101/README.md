# clean-code-101

`clean-code-101` 시리즈의 예제 코드 저장소입니다. 각 에피소드 핵심 원칙을 오프라인에서 바로 실행 가능한 Python 스크립트와 pytest로 구성했습니다.

이 저장소는 학습용 예제이며 외부 API 호출 없이 동작합니다. 모든 예제는 offline mock-only 원칙을 따릅니다.

## 요구사항

- Python 3.11+

## 설치

```bash
pip install -r requirements.txt
```

## 실행

```bash
python ko/01-what-is-clean-code/step01_clean_code_basics.py
python en/10-good-code-review/step01_good_code_review.py
python3 -m pytest tests/ -q
```

## 디렉토리 맵

- `ko/` - 한국어 에피소드별 예제 (01-10)
- `en/` - `ko/`와 동일 로직의 영어 미러 예제
- `tests/` - 에피소드별 행동 검증 테스트
- `common.py` - 공통 데이터 구조 및 로더 유틸리티

## 에피소드 인덱스

1. [01-what-is-clean-code.md](https://github.com/yeongseon-books/book-content/blob/master/content/clean-code-101/ko/01-what-is-clean-code.md)
2. [02-naming.md](https://github.com/yeongseon-books/book-content/blob/master/content/clean-code-101/ko/02-naming.md)
3. [03-small-functions.md](https://github.com/yeongseon-books/book-content/blob/master/content/clean-code-101/ko/03-small-functions.md)
4. [04-simplifying-conditionals.md](https://github.com/yeongseon-books/book-content/blob/master/content/clean-code-101/ko/04-simplifying-conditionals.md)
5. [05-removing-duplication.md](https://github.com/yeongseon-books/book-content/blob/master/content/clean-code-101/ko/05-removing-duplication.md)
6. [06-error-handling.md](https://github.com/yeongseon-books/book-content/blob/master/content/clean-code-101/ko/06-error-handling.md)
7. [07-comments-and-docs.md](https://github.com/yeongseon-books/book-content/blob/master/content/clean-code-101/ko/07-comments-and-docs.md)
8. [08-testable-code.md](https://github.com/yeongseon-books/book-content/blob/master/content/clean-code-101/ko/08-testable-code.md)
9. [09-refactoring-basics.md](https://github.com/yeongseon-books/book-content/blob/master/content/clean-code-101/ko/09-refactoring-basics.md)
10. [10-good-code-review.md](https://github.com/yeongseon-books/book-content/blob/master/content/clean-code-101/ko/10-good-code-review.md)

## License

MIT
