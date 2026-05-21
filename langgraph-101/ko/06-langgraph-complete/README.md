# LangGraph 101 (6/6): LangGraph 완성

Langgraph 101 시리즈 6편 예제 코드입니다.

## 학습 목표

- 완성형 LangGraph 앱은 왜 하나의 거대한 프롬프트가 아니라 협력하는 상태 기계로 봐야 할까요?
- 체크포인트, 분기, tool call, 멀티턴 이력을 붙여도 어떤 state 계약은 끝까지 유지해야 할까요?
- 운영에서 그래프 실행을 설명하려면 어떤 로그와 검증 지점을 남겨야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_checkpoint_router_tools.py` | 예제 코드 |
| `step02_streaming_pipeline.py` | 예제 코드 |

## 실행 방법

```bash
cd langgraph-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/06-langgraph-complete/step01_checkpoint_router_tools.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/langgraph-101/ko/06-langgraph-complete.md)
