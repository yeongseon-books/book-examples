# oop-101

`oop-101` 시리즈 예제 코드 저장소입니다. 각 에피소드마다 실행 가능한 파이썬 예제를 `ko/`, `en/`에 하나씩 제공합니다.

## 요구사항

- Python 3.11+

## 설치

```bash
pip install -r requirements.txt
```

## 에피소드 목록

- EP01 OOP란 무엇인가: 객체가 상태와 행동을 함께 가지는 모델
- EP02 클래스와 인스턴스: 생성자와 인스턴스 메서드
- EP03 캡슐화: 잔액 변경을 메서드로만 허용
- EP04 상속: 직원 공통 규칙을 부모 클래스로 통합
- EP05 다형성: 같은 인터페이스로 결제 수단 교체
- EP06 추상화: 저장소 인터페이스와 구현 분리
- EP07 합성 vs 상속: 알림 기능을 합성으로 확장
- EP08 SOLID: 의존성 역전으로 결제 서비스 분리
- EP09 설계 예제: 주문, 재고, 결제를 통합한 작은 도메인
- EP10 OOP를 피할 때: 함수형 파이프라인과 OOP 비교

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 실행

```bash
python ko/ep01_what_is_oop.py
python en/ep10_when_to_avoid_oop.py
pytest -q
```
