# data-science-101 예제 코드

`data-science-101` 시리즈의 에피소드별 실행 가능한 Python 예제와 테스트를 모아둔 저장소입니다.

## 구성

- `common.py`: 공통 합성 데이터 생성 및 유틸리티
- `ko/01-what-is-data-science.py`
- `ko/02-problem-to-data-problem.py`
- `ko/03-data-collection.py`
- `ko/04-data-cleaning.py`
- `ko/05-exploratory-data-analysis.py`
- `ko/06-visualization.py`
- `ko/07-modeling.py`
- `ko/08-evaluation.py`
- `ko/09-result-interpretation.py`
- `ko/10-data-project-end-to-end.py`
- `en/`: `ko/`와 동일 로직의 영어 미러 예제
- `tests/`: 에피소드별 동작 검증 테스트

## 설치

```bash
pip install -r requirements.txt
```

## 실행

```bash
python ko/01-what-is-data-science.py
```

## 테스트

```bash
pytest tests/ -q
```

## 원본

- https://github.com/yeongseon-books/book-content/tree/master/content/data-science-101
