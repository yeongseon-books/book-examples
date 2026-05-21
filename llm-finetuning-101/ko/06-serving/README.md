# LLM Fine-tuning 101 (6/6): 모델 서빙

Llm Finetuning 101 시리즈 6편 예제 코드입니다.

## 학습 목표

- 파인튜닝된 작은 모델을 FastAPI 엔드포인트 뒤에 두기 위한 최소 구조는 무엇일까요?
- 서빙 코드에서 학습과 추론의 경계는 어디에 그어야 할까요?
- 브라우저를 열지 않고도 엔드포인트를 어떻게 검증할 수 있을까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_fastapi_mock_server.py` | 예제 코드 |
| `step02_inference_optimization_simulation.py` | 예제 코드 |

## 실행 방법

```bash
cd llm-finetuning-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/06-serving/step01_fastapi_mock_server.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/llm-finetuning-101/ko/06-serving.md)
