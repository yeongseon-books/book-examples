# Calculus for ML 101 (8/10): 최적화

Calculus For Ml 101 시리즈 8편 예제 코드입니다.

## 학습 목표

- plain gradient descent는 실제 딥러닝 학습에서 어떤 약점을 드러낼까요?
- momentum은 왜 관성이라는 비유로 설명하는 편이 가장 이해가 쉬울까요?
- RMSProp과 Adam은 좌표별 gradient scale 차이를 어떻게 완화할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `2_gradient.py` | 예제 코드 |
| `adam_momentum_rmsprop.py` | 예제 코드 |
| `momentum.py` | 예제 코드 |
| `rmsprop_scale.py` | 예제 코드 |
| `schedule.py` | 예제 코드 |
| `snippet.py` | 예제 코드 |
| `snippet_08.py` | 예제 코드 |
| `step01_optimization.py` | 예제 코드 |

## 실행 방법

```bash
cd calculus-for-ml-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/08-optimization/2_gradient.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/calculus-for-ml-101/ko/08-optimization.md)
