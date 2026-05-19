# algorithms-python-101

`algorithms-python-101` 시리즈의 예제 코드 저장소입니다. 모든 예제는 오프라인에서 실행 가능하며, 에피소드별 핵심 개념을 하나의 실행 스크립트로 검증할 수 있게 구성했습니다.

## 요구사항

- Python 3.11+

## 설치

```bash
pip install -r requirements.txt
```

## 실행

```bash
python ko/01-what-are-algorithms/step01_intro_algorithms.py
python en/10-coding-test-strategies/step01_patterns.py
python -m pytest tests/ -q
```

## 디렉토리 맵

- `common.py` - 공통 유틸리티
- `ko/` - 한국어 에피소드별 예제 (01-10)
- `en/` - `ko/`와 동일 로직의 영어 예제
- `tests/` - 에피소드별 행동 테스트

## 에피소드 인덱스 (원문 링크)

1. [01-what-are-algorithms](https://github.com/yeongseon-books/book-content/blob/master/content/algorithms-python-101/ko/01-what-are-algorithms.md)
2. [02-time-complexity-and-big-o](https://github.com/yeongseon-books/book-content/blob/master/content/algorithms-python-101/ko/02-time-complexity-and-big-o.md)
3. [03-linear-and-binary-search](https://github.com/yeongseon-books/book-content/blob/master/content/algorithms-python-101/ko/03-linear-and-binary-search.md)
4. [04-sorting-algorithms](https://github.com/yeongseon-books/book-content/blob/master/content/algorithms-python-101/ko/04-sorting-algorithms.md)
5. [05-recursion-and-divide-and-conquer](https://github.com/yeongseon-books/book-content/blob/master/content/algorithms-python-101/ko/05-recursion-and-divide-and-conquer.md)
6. [06-dynamic-programming-basics](https://github.com/yeongseon-books/book-content/blob/master/content/algorithms-python-101/ko/06-dynamic-programming-basics.md)
7. [07-graph-traversal-bfs-dfs](https://github.com/yeongseon-books/book-content/blob/master/content/algorithms-python-101/ko/07-graph-traversal-bfs-dfs.md)
8. [08-shortest-path-basics](https://github.com/yeongseon-books/book-content/blob/master/content/algorithms-python-101/ko/08-shortest-path-basics.md)
9. [09-greedy-algorithms](https://github.com/yeongseon-books/book-content/blob/master/content/algorithms-python-101/ko/09-greedy-algorithms.md)
10. [10-coding-test-strategies](https://github.com/yeongseon-books/book-content/blob/master/content/algorithms-python-101/ko/10-coding-test-strategies.md)

## 주의사항

- 이 저장소는 학습용 오프라인 예제입니다.
- 외부 API, 네트워크 호출, 비밀 키 사용 코드는 포함하지 않았습니다.

## License

MIT
