# AI Data Preparation 101 (7/10): 합성 데이터 생성 — Self-Instruct부터 Distillation까지

Ai Data Preparation 101 시리즈 7편 예제 코드입니다.

## 학습 목표

- 도메인 파인튜닝용 synthetic batch는 어떤 입력에서 시작해 어떤 산출물로 끝나야 할까요?
- Self-Instruct, Evol-Instruct, RAG eval, distillation은 어느 시점에 선택해야 할까요?
- 생성된 JSON 산출물은 어떤 검증 게이트를 통과해야 실제 데이터셋에 편입할 수 있을까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_self_instruct_mock.py` | 예제 코드 |

## 실행 방법

```bash
cd ai-data-preparation-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/07-synthetic-data-generation/step01_self_instruct_mock.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/ai-data-preparation-101/ko/07-synthetic-data-generation.md)
