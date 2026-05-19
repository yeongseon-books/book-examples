# computer-science-101 예제 코드

`computer-science-101` 시리즈의 핵심 개념을 에피소드별로 실행 가능한 Python 예제로 정리한 저장소입니다.

## 구성

- 01 what-is-computer-science: 튜링 기계 기반 이진수 증가 시뮬레이션
- 02 computation-and-programs: 같은 계산의 명령형/재귀/함수형 표현
- 03 data-representation: 이진수 변환, UTF-8 바이트, 부동소수점 오차
- 04 algorithms-and-complexity: 선형 탐색 vs 이진 탐색 비교 횟수
- 05 computer-architecture: 스택 머신 VM 바이트코드 실행
- 06 operating-systems: FCFS/SJF/RR 스케줄링 평균 대기시간
- 07 networks: 메모리 기반 패킷 스위칭/드롭 시뮬레이션
- 08 databases: in-memory Table select/where/join 엔진
- 09 software-engineering: 리팩터링 전후 동작 동일성 검증
- 10 ai-and-data-science: 경사하강법 기반 선형 회귀 학습

`ko/`와 `en/`은 동일한 예제를 한국어/영어 설명으로 제공합니다.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 실행

```bash
pip install -r requirements.txt
python ko/01-what-is-computer-science.py
python en/10-ai-and-data-science.py
```

## 테스트

```bash
pytest tests/ -q
```

## 원본

https://github.com/yeongseon-books/book-content/tree/master/content/computer-science-101
