# secure-coding-101 example code

DEMO ONLY - not production crypto.

이 저장소의 코드는 secure-coding-101 시리즈 학습용 예제입니다.
실서비스에 그대로 사용하면 안 됩니다.

- ko/, en/에 에피소드별 실행 가능한 Python 스크립트가 있습니다.
- 각 에피소드는 INSECURE 패턴과 SAFE 패턴을 함께 보여줍니다.
- 테스트는 `pytest -q`로 실행합니다.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```
