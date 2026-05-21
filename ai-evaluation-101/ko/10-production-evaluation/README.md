# AI Evaluation 101 (10/10): 운영 환경에서의 지속적 평가

Ai Evaluation 101 시리즈 10편 예제 코드입니다.

## 학습 목표

- 운영 평가는 배포 전 평가를 어떤 지속 루프로 닫아야 할까요?
- production trace sampling, drift detection, shadow mode는 각각 어떤 신호를 잡을까요?
- 운영 평가 비용을 통제하면서 실패를 regression set으로 되돌리는 기준은 무엇일까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `2_online_metric.py` | 예제 코드 |
| `4_shadow_mode_canary.py` | 예제 코드 |
| `6.py` | 예제 코드 |
| `7_production_failure.py` | 예제 코드 |
| `baseline.py` | 예제 코드 |
| `kl_divergence.py` | 예제 코드 |
| `output_drift.py` | 예제 코드 |
| `snippet.py` | 예제 코드 |
| `step01_continuous_eval.py` | 예제 코드 |
| `stratified_sampling.py` | 예제 코드 |
| `uniform_sampling.py` | 예제 코드 |

## 실행 방법

```bash
cd ai-evaluation-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/10-production-evaluation/2_online_metric.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/ai-evaluation-101/ko/10-production-evaluation.md)
