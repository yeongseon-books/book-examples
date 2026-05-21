# LLM from Scratch 101 (3/9): 어떤 토큰을 얼마나 볼지 스스로 정하기

Llm From Scratch 101 시리즈 3편 예제 코드입니다.

## 학습 목표

- Q, K, V는 왜 같은 입력에서 나오지만 서로 다른 역할을 가질까요?
- 어텐션 점수는 왜 `Q · K^T / sqrt(d)` 형태로 계산할까요?
- causal mask가 없으면 자기회귀 학습에서 정확히 무엇이 망가질까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `episode.py` | 예제 코드 |

## 실행 방법

```bash
cd llm-from-scratch-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/03-attention/episode.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/llm-from-scratch-101/ko/03-attention.md)
