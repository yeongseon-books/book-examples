# capstone-project-101

`capstone-project-101` 시리즈의 예제 코드 저장소입니다. 모든 예제는 오프라인에서 실행 가능한 mock 기반이며, 외부 네트워크/API 호출 없이 핵심 개념을 에피소드별로 검증할 수 있게 구성했습니다.

## 요구사항
- Python 3.11+

## 설치
```bash
pip install -r requirements.txt
```

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 실행
```bash
python ko/01-what-is-capstone/step01_capstone_definition.py
python en/10-project-retrospective/step01_retro_kpt.py
python3 -m pytest tests/ -q
```

## 디렉토리 맵
- `common.py` - 공통 유틸리티(점수 계산, 오프라인 검증, 회고 검증)
- `ko/` - 한국어 에피소드별 예제 (01-10)
- `en/` - `ko/`와 동일 로직의 영어 미러 예제
- `tests/` - 에피소드별 동작 테스트

## 에피소드 원문 링크
1. [01-what-is-capstone](https://github.com/yeongseon-books/book-content/blob/master/content/capstone-project-101/ko/01-what-is-capstone.md)
2. [02-choosing-a-topic](https://github.com/yeongseon-books/book-content/blob/master/content/capstone-project-101/ko/02-choosing-a-topic.md)
3. [03-defining-the-problem](https://github.com/yeongseon-books/book-content/blob/master/content/capstone-project-101/ko/03-defining-the-problem.md)
4. [04-organizing-requirements](https://github.com/yeongseon-books/book-content/blob/master/content/capstone-project-101/ko/04-organizing-requirements.md)
5. [05-splitting-team-roles](https://github.com/yeongseon-books/book-content/blob/master/content/capstone-project-101/ko/05-splitting-team-roles.md)
6. [06-designing-the-mvp](https://github.com/yeongseon-books/book-content/blob/master/content/capstone-project-101/ko/06-designing-the-mvp.md)
7. [07-choosing-the-tech-stack](https://github.com/yeongseon-books/book-content/blob/master/content/capstone-project-101/ko/07-choosing-the-tech-stack.md)
8. [08-schedule-management](https://github.com/yeongseon-books/book-content/blob/master/content/capstone-project-101/ko/08-schedule-management.md)
9. [09-presentation-materials](https://github.com/yeongseon-books/book-content/blob/master/content/capstone-project-101/ko/09-presentation-materials.md)
10. [10-project-retrospective](https://github.com/yeongseon-books/book-content/blob/master/content/capstone-project-101/ko/10-project-retrospective.md)

## 오프라인 실행 정책
- 이 저장소는 offline mock-only 예제입니다.
- 실제 네트워크/API 호출은 금지하며 포함하지 않았습니다.

## License
MIT
