# design-patterns-101 예제 코드

`design-patterns-101` 시리즈의 각 에피소드를 실행 가능한 순수 표준 라이브러리 Python 예제로 정리한 저장소입니다.

## 구성

- 01-what-are-design-patterns
- 02-creational-patterns
- 03-structural-patterns
- 04-behavioral-patterns
- 05-strategy-pattern
- 06-adapter-pattern
- 07-observer-pattern
- 08-factory-and-di
- 09-avoiding-pattern-overuse
- 10-pythonic-patterns

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 실행

```bash
python ko/01-what-are-design-patterns.py
python en/10-pythonic-patterns.py
```

## 테스트

```bash
python -m pytest tests -v
```

## 원본

- https://github.com/yeongseon-books/book-content/tree/master/content/design-patterns-101
