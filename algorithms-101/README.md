# algorithms-101

`algorithms-101` 시리즈의 예제 코드 저장소입니다. 모든 예제는 오프라인에서 바로 실행 가능한 순수 Python 코드로 구성되어 있으며, 에피소드별 핵심 알고리즘 개념을 한 파일씩 검증할 수 있게 설계했습니다.

## 요구사항

- Python 3.11+

## 설치

```bash
pip install -r requirements.txt
```

## 실행

```bash
python ko/01-what-is-an-algorithm/step01_algorithm_basics.py
python en/10-problem-solving-strategies/step01_problem_solving_playbook.py
python -m pytest tests/ -q
```

## 에피소드 인덱스

- 01. 알고리즘이란 무엇인가?  
  https://github.com/yeongseon-books/book-content/blob/master/content/algorithms-101/ko/01-what-is-an-algorithm.md
- 02. 시간 복잡도와 공간 복잡도  
  https://github.com/yeongseon-books/book-content/blob/master/content/algorithms-101/ko/02-time-and-space-complexity.md
- 03. 탐색 알고리즘  
  https://github.com/yeongseon-books/book-content/blob/master/content/algorithms-101/ko/03-search-algorithms.md
- 04. 정렬 알고리즘  
  https://github.com/yeongseon-books/book-content/blob/master/content/algorithms-101/ko/04-sorting-algorithms.md
- 05. 재귀와 분할 정복  
  https://github.com/yeongseon-books/book-content/blob/master/content/algorithms-101/ko/05-recursion-and-divide-and-conquer.md
- 06. 동적 계획법  
  https://github.com/yeongseon-books/book-content/blob/master/content/algorithms-101/ko/06-dynamic-programming.md
- 07. 그리디 알고리즘  
  https://github.com/yeongseon-books/book-content/blob/master/content/algorithms-101/ko/07-greedy-algorithms.md
- 08. 그래프 알고리즘  
  https://github.com/yeongseon-books/book-content/blob/master/content/algorithms-101/ko/08-graph-algorithms.md
- 09. 문자열 알고리즘 기초  
  https://github.com/yeongseon-books/book-content/blob/master/content/algorithms-101/ko/09-string-algorithms.md
- 10. 알고리즘 문제 풀이 전략  
  https://github.com/yeongseon-books/book-content/blob/master/content/algorithms-101/ko/10-problem-solving-strategies.md

## 디렉토리 맵

- `common.py` - 시간 측정, 랜덤 리스트 생성, 정렬 검증 유틸리티
- `ko/` - 한국어 에피소드별 예제 (01-10)
- `en/` - `ko/`와 동일 로직의 영어 예제
- `tests/` - 에피소드별 행동 테스트

## 주의사항

- 이 저장소는 학습용 예제입니다.
- 외부 API 호출이나 네트워크 의존성 없이 동작합니다.

## License

MIT
