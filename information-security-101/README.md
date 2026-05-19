# information-security-101

`information-security-101` 시리즈의 오프라인 학습용 예제 코드 저장소입니다. 10개 에피소드의 핵심 개념을 `common.py`와 에피소드별 스크립트로 실행할 수 있게 구성했습니다.

## 중요 경고

- 이 저장소의 일부 암호화 예제(`SymmetricCipher`)는 학습 목적의 데모 구현입니다.
- 데모 암호화 코드는 운영 환경에서 사용하면 안 됩니다.
- 실서비스에서는 검증된 표준 라이브러리와 KMS/Vault를 사용해야 합니다.

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
python ko/01-what-is-information-security.py
python en/10-incident-response.py
pytest -q
```

## 디렉토리

- `common.py`: 시리즈 공통 보안 프리미티브
- `ko/`: 한국어 에피소드별 실행 스크립트
- `en/`: 영어 에피소드별 실행 스크립트
- `tests/`: 에피소드별 행동 테스트
