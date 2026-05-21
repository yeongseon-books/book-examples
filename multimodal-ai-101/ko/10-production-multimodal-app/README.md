# Multimodal AI 101 (10/10): Production Multimodal Application 구축

Multimodal Ai 101 시리즈 10편 예제 코드입니다.

## 학습 목표

- production 멀티모달 앱은 어떤 end-to-end 구성 요소를 반드시 분리해서 설계해야 할까요?
- FastAPI 입구, inference worker, cache, object storage, observability는 어떤 순서로 연결되는 편이 안정적일까요?
- 동기 처리와 비동기 처리 경계는 어떤 기준으로 나누는 것이 현실적일까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `2_fastapi.py` | 예제 코드 |
| `3_inference_worker_vllm_triton.py` | 예제 코드 |
| `4_caching_layer.py` | 예제 코드 |
| `6_observability_feedback_loop.py` | 예제 코드 |
| `step01_production_app.py` | 예제 코드 |

## 실행 방법

```bash
cd multimodal-ai-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/10-production-multimodal-app/2_fastapi.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/multimodal-ai-101/ko/10-production-multimodal-app.md)
