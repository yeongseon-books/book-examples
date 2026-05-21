# Calculus for ML 101 (9/10): 역전파 직관

Calculus For Ml 101 시리즈 9편 예제 코드입니다.

## 학습 목표

- 역전파는 수많은 weight의 gradient를 왜 한 번에 계산할 수 있을까요?
- 계산 그래프 관점에서 순전파와 역전파는 각각 무엇을 남길까요?
- local derivative를 저장한다는 말은 실제로 어떤 의미일까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_backprop.py` | 예제 코드 |

## 실행 방법

```bash
cd calculus-for-ml-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/09-backpropagation-intuition/step01_backprop.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/calculus-for-ml-101/ko/09-backpropagation-intuition.md)
