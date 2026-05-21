# AI Safety & Guardrails 101 (10/10): 운영 가드레일 시스템 구축

Ai Safety Guardrails 101 시리즈 10편 예제 코드입니다.

## 학습 목표

- 운영 guardrail 시스템은 왜 단일 필터가 아니라 경계별 파이프라인이어야 할까요?
- fail-open과 fail-closed는 어떤 위험 기준으로 선택해야 할까요?
- 성능 예산, observability, CI regression을 한 시스템에 어떻게 묶어야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `ci.py` | 예제 코드 |
| `pipeline_audit.json` | 예제 코드 |
| `snippet.py` | 예제 코드 |
| `snippet_03.py` | 예제 코드 |
| `snippet_04.py` | 예제 코드 |
| `step01_guardrail_pipeline.py` | 예제 코드 |

## 실행 방법

```bash
cd ai-safety-guardrails-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/10-production-guardrail-system/ci.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/ai-safety-guardrails-101/ko/10-production-guardrail-system.md)
