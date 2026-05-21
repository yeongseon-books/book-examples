# Calculus for ML 101 (10/10): 딥러닝에서의 미분

Calculus For Ml 101 시리즈 10편 예제 코드입니다.

## 학습 목표

- 딥러닝 학습 루프는 어떤 단계로 구성되고 각 단계에서 미분은 어디에 등장할까요?
- forward pass와 loss computation은 backward를 위해 무엇을 준비할까요?
- gradient 계산과 optimizer update는 어떻게 연결될까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `2_gradient.py` | 예제 코드 |
| `gradient_analytic_form.py` | 예제 코드 |
| `optimizer_step_gradient.py` | 예제 코드 |
| `snippet.py` | 예제 코드 |
| `snippet_05.py` | 예제 코드 |
| `snippet_06.py` | 예제 코드 |
| `snippet_07.py` | 예제 코드 |
| `snippet_08.py` | 예제 코드 |
| `snippet_10.py` | 예제 코드 |
| `step01_training_loop.py` | 예제 코드 |

## 실행 방법

```bash
cd calculus-for-ml-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/10-calculus-in-deep-learning/2_gradient.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/calculus-for-ml-101/ko/10-calculus-in-deep-learning.md)
