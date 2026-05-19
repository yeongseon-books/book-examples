# data-science-career-101 예제 코드

`data-science-career-101` 시리즈의 커리어 실전형 Python 예제 코드 저장소입니다.

## 구성

- `ko/01-what-is-data-career.py` 직무 적합도 평가기
- `ko/02-analyst-scientist-engineer.py` JD 기반 역할 분류기
- `ko/03-learning-path.py` 12주 학습 경로 생성기
- `ko/04-data-portfolio.py` 포트폴리오 README 검증기
- `ko/05-sql-and-analytics-interview.py` SQL 인터뷰 연습 하네스
- `ko/06-ml-interview.py` ML 인터뷰 미니 구현(train/test split, k-fold, KNN)
- `ko/07-case-interview.py` 케이스 인터뷰 프레임워크 생성기
- `ko/08-first-job.py` 온보딩 작업/체크리스트 검증기
- `ko/09-domain-expertise.py` 도메인 지식 매퍼
- `ko/10-path-to-senior.py` 시니어 준비도 자가진단기
- `en/` 동일 로직의 영어 미러 예제
- `tests/` 에피소드별 pytest 행동 테스트

## 실행

```bash
pip install -r requirements.txt
python ko/01-what-is-data-career.py
python en/05-sql-and-analytics-interview.py
```

## 테스트

```bash
pytest tests/ -q
```

## 원본

https://github.com/yeongseon-books/book-content/tree/master/content/data-science-career-101
