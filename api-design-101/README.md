# api-design-101

`api-design-101` 시리즈의 예제 코드 저장소입니다. 모든 예제는 오프라인 실행 가능한 mock 기반으로 구성되어 있으며, API 설계의 핵심 개념을 에피소드별로 작게 검증할 수 있게 설계했습니다.

## 요구사항

- Python 3.11+

## 설치

```bash
pip install -r requirements.txt
```

## 실행

```bash
python ko/01-what-is-an-api/step01_api_contract.py
python en/10-writing-good-api-docs/step01_docs_quality.py
python -m pytest tests/ -v
```

## 디렉토리 맵

- `common.py` - 공통 TestClient 팩토리, cursor 유틸리티, problem 응답 유틸리티
- `ko/` - 한국어 에피소드별 예제 (01-10)
- `en/` - `ko/`와 동일 로직의 영어 예제
- `tests/` - 에피소드별 스모크/행동 테스트

## 에피소드 인덱스

- [01-what-is-an-api](https://github.com/yeongseon-books/book-content/blob/master/content/api-design-101/ko/01-what-is-an-api.md)
- [02-rest-basics](https://github.com/yeongseon-books/book-content/blob/master/content/api-design-101/ko/02-rest-basics.md)
- [03-resource-design](https://github.com/yeongseon-books/book-content/blob/master/content/api-design-101/ko/03-resource-design.md)
- [04-http-methods-and-status](https://github.com/yeongseon-books/book-content/blob/master/content/api-design-101/ko/04-http-methods-and-status.md)
- [05-request-and-response-schema](https://github.com/yeongseon-books/book-content/blob/master/content/api-design-101/ko/05-request-and-response-schema.md)
- [06-pagination-and-filtering](https://github.com/yeongseon-books/book-content/blob/master/content/api-design-101/ko/06-pagination-and-filtering.md)
- [07-error-response-design](https://github.com/yeongseon-books/book-content/blob/master/content/api-design-101/ko/07-error-response-design.md)
- [08-openapi-and-swagger](https://github.com/yeongseon-books/book-content/blob/master/content/api-design-101/ko/08-openapi-and-swagger.md)
- [09-api-versioning](https://github.com/yeongseon-books/book-content/blob/master/content/api-design-101/ko/09-api-versioning.md)
- [10-writing-good-api-docs](https://github.com/yeongseon-books/book-content/blob/master/content/api-design-101/ko/10-writing-good-api-docs.md)

## 주의사항

- 이 저장소는 학습용 mock 예제입니다.
- 실서비스 연동(API Key, 외부 결제, 실제 데이터베이스)은 포함하지 않았습니다.

## License

MIT
