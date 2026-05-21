# RAG Evaluation and Benchmarking 101 (6/6): RAG 벤치마크 완성

Rag Benchmark 101 시리즈 6편 예제 코드입니다.

## 학습 목표

- 벤치마크를 한 번 실행하는 스크립트에서 반복 가능한 의사결정 도구로 바꾸려면 무엇이 필요할까요?
- 자동 리포트는 평균 점수뿐 아니라 어떤 실패 사례를 보여 줘야 할까요?
- CI에 벤치마크를 붙일 때 어떤 회귀 기준을 차단선으로 삼아야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `run_full_benchmark.py` | 예제 코드 |

## 실행 방법

```bash
cd rag-benchmark-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/06-benchmark-complete/run_full_benchmark.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/rag-benchmark-101/ko/06-benchmark-complete.md)
