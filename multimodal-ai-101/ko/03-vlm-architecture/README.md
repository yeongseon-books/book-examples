# Multimodal AI 101 (3/10): Vision-Language Model 아키텍처

Multimodal Ai 101 시리즈 3편 예제 코드입니다.

## 학습 목표

- VLM은 어떤 경로로 image encoder의 출력을 LLM 입력으로 연결할까요?
- Vision Encoder + Adapter + LLM이라는 공통 뼈대는 왜 대부분의 모델에서 반복될까요?
- LLaVA, BLIP-2, Flamingo는 각각 어떤 trade-off를 선택한 설계일까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `1_llava_mlp_projection.py` | 예제 코드 |
| `2_blip_2_q_former_token.py` | 예제 코드 |
| `3_flamingo_llm_cross_attention_layer.py` | 예제 코드 |
| `llava.py` | 예제 코드 |
| `step01_vlm_architecture.py` | 예제 코드 |

## 실행 방법

```bash
cd multimodal-ai-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/03-vlm-architecture/1_llava_mlp_projection.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/multimodal-ai-101/ko/03-vlm-architecture.md)
