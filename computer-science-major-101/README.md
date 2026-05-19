# computer-science-major-101 예제 코드

`computer-science-major-101` 시리즈의 학습용 예제 코드 저장소이며, 각 에피소드의 핵심 내용을 파이썬으로 작게 실행하고 검증할 수 있도록 구성했습니다.

## 구성

- `ko/01-what-cs-majors-learn.py` - 전공 영역 선수 관계 정렬기
- `ko/02-first-year-subjects.py` - 1학년 기초 수학 미니 데모
- `ko/03-data-structures-and-algorithms.py` - 연결 리스트와 BST 구현
- `ko/04-systems-subjects.py` - 라운드 로빈 스케줄러 시뮬레이터
- `ko/05-database-and-network.py` - TCP 기반 인메모리 KV 저장소
- `ko/06-ai-and-data-science.py` - 표준 라이브러리 로지스틱 회귀
- `ko/07-project-subjects.py` - 프로젝트 스캐폴드 생성기
- `ko/08-how-to-study-cs.py` - SM-2 간격 반복 스케줄러
- `ko/09-build-your-portfolio.py` - 포트폴리오 README 검증기
- `ko/10-skills-before-graduation.py` - 졸업 역량 자가 진단 리포트
- `en/` - `ko/`와 동일 로직의 영어 주석 버전
- `tests/` - 에피소드별 동작 테스트

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 실행

```bash
pip install -r requirements.txt
python ko/01-what-cs-majors-learn.py
python en/10-skills-before-graduation.py
```

## 테스트

```bash
pytest tests/ -q
```

## 원본

https://github.com/yeongseon-books/book-content/tree/master/content/computer-science-major-101
