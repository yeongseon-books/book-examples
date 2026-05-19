# ai-evaluation-101

`ai-evaluation-101` 시리즈의 예제 코드 저장소입니다. 모든 예제는 오프라인 실행 가능한 mock 기반으로 구성되어 있으며, 평가의 핵심 개념을 에피소드별로 작게 검증할 수 있게 설계했습니다.

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
python ko/01-why-evaluate-llm-apps/step01_eval_basics.py
python en/10-production-evaluation/step01_continuous_eval.py
python -m pytest tests/ -v
```
