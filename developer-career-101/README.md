# developer-career-101 예제 코드

`developer-career-101` 시리즈의 커리어 도구와 기술 미니 데모를 에피소드별로 실행해 볼 수 있도록 구성한 Python 예제 저장소입니다.

## 구성

- 01 `ko/01-what-is-developer-career.py`: 커리어 단계 분류기
- 02 `ko/02-understanding-roles.py`: 직무 분류 매트릭스
- 03 `ko/03-learning-plan.py`: 12주 학습 계획 생성기
- 04 `ko/04-resume-and-portfolio.py`: 이력서 검증기
- 05 `ko/05-coding-interview.py`: 코딩 인터뷰 문제 하네스
- 06 `ko/06-system-design-interview.py`: 시스템 디자인 스펙 생성기
- 07 `ko/07-first-job.py`: 30/60/90 온보딩 계획기
- 08 `ko/08-side-projects.py`: 사이드 프로젝트 평가기
- 09 `ko/09-mentoring-networking.py`: 네트워킹 트래커
- 10 `ko/10-path-to-senior.py`: 시니어 준비도 스코어카드
- `en/`: 동일 로직의 영어 미러 스크립트
- `tests/`: 에피소드별 pytest 테스트

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 실행

```bash
pip install -r requirements.txt
python ko/01-what-is-developer-career.py
python en/10-path-to-senior.py
```

## 테스트

```bash
pytest -q
```

## 원본

https://github.com/yeongseon-books/book-content/tree/master/content/developer-career-101
