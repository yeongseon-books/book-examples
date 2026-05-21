# Calculus for ML 101 (5/10): 연쇄 법칙

Calculus For Ml 101 시리즈 5편 예제 코드입니다.

## 학습 목표

- 함수가 다른 함수 안에 들어갈 때 전체 미분은 왜 단순 합이 아니라 곱으로 연결될까요?
- 바깥 함수와 안쪽 함수를 구분하는 가장 실용적인 방법은 무엇일까요?
- 단계가 여러 개인 합성함수에서 gradient는 어떤 순서로 전달될까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `2_gradient.py` | 예제 코드 |
| `snippet.py` | 예제 코드 |
| `snippet_02.py` | 예제 코드 |
| `snippet_04.py` | 예제 코드 |
| `snippet_05.py` | 예제 코드 |
| `snippet_06.py` | 예제 코드 |
| `snippet_08.py` | 예제 코드 |
| `snippet_09.py` | 예제 코드 |
| `step01_chain_rule.py` | 예제 코드 |

## 실행 방법

```bash
cd calculus-for-ml-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/05-chain-rule/2_gradient.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/calculus-for-ml-101/ko/05-chain-rule.md)
