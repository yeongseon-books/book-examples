# AI Data Preparation 101 (10/10): 프로덕션 데이터 파이프라인 구축

Ai Data Preparation 101 시리즈 10편 예제 코드입니다.

## 학습 목표

- 여러 데이터 준비 단계를 실제 운영 가능한 하나의 파이프라인으로 묶으려면 어떤 시스템 속성이 필요할까요?
- DVC와 stage fingerprint는 데이터 버전 관리와 idempotency를 어떻게 함께 해결할까요?
- Airflow 같은 오케스트레이터는 단순 스케줄링 외에 어떤 운영 가치를 줄까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `data_prep.py` | 예제 코드 |
| `observability_stage.py` | 예제 코드 |
| `pipeline.py` | 예제 코드 |
| `schema_validation.py` | 예제 코드 |
| `stage.py` | 예제 코드 |
| `step01_pipeline_orchestrator.py` | 예제 코드 |

## 실행 방법

```bash
cd ai-data-preparation-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/10-production-data-pipeline/data_prep.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/ai-data-preparation-101/ko/10-production-data-pipeline.md)
