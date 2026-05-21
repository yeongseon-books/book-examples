# LLM App Foundations 101 (1/6): LLM API 첫걸음 — 모델에게 첫 번째 요청 보내기

Llm App Foundations 101 시리즈 1편 예제 코드입니다.

## 학습 목표

- LLM API 호출은 SDK 아래에서 어떤 요청-응답 구조로 움직일까요?
- API 키와 모델 ID, 메시지 형식 중 첫 실패에서 어디부터 봐야 할까요?
- 응답에서 본문, 사용량, 모델명을 어떻게 읽어야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_check_env.py` | 예제 코드 |
| `step02_first_call.py` | 예제 코드 |
| `step03_inspect_response.py` | 예제 코드 |
| `step04_sync_vs_async.py` | 예제 코드 |
| `step05_complete_example.py` | 예제 코드 |

## 실행 방법

```bash
cd llm-app-foundations-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/01-llm-api-first-call/step01_check_env.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/llm-app-foundations-101/ko/01-llm-api-first-call.md)
