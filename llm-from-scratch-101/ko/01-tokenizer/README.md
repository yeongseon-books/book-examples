# LLM from Scratch 101 (1/9): 글자를 숫자로 바꾸기

Llm From Scratch 101 시리즈 1편 예제 코드입니다.

## 학습 목표

- 모델은 왜 문자열 대신 정수 시퀀스를 입력으로 받아야 할까요?
- 문자 단위, 단어 단위, 서브워드 토큰화는 각각 무엇을 얻고 무엇을 잃을까요?
- BPE는 실제로 어떤 식으로 어휘를 조금씩 키워 갈까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `episode.py` | 예제 코드 |
| `gpt_2.py` | 예제 코드 |
| `snippet.py` | 예제 코드 |
| `tinyshakespeare.py` | 예제 코드 |

## 실행 방법

```bash
cd llm-from-scratch-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/01-tokenizer/episode.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/llm-from-scratch-101/ko/01-tokenizer.md)
