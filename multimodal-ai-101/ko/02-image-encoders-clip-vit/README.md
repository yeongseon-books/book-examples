# Multimodal AI 101 (2/10): Image Encoder: CLIP과 ViT

Multimodal Ai 101 시리즈 2편 예제 코드입니다.

## 학습 목표

- 왜 멀티모달 입문에서 image encoder부터 이해하는 편이 전체 구조를 가장 빠르게 잡게 해 줄까요?
- ViT는 이미지를 어떤 방식으로 token sequence로 바꾸고, CNN과 무엇이 다를까요?
- CLIP은 어떻게 텍스트와 이미지를 같은 embedding space에 맞추고 zero-shot을 가능하게 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `1_zero_shot.py` | 예제 코드 |
| `2_image_embedding_vector_db.py` | 예제 코드 |
| `clip_text_image.py` | 예제 코드 |
| `step01_image_encoder.py` | 예제 코드 |
| `vit_token_sequence.py` | 예제 코드 |

## 실행 방법

```bash
cd multimodal-ai-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/02-image-encoders-clip-vit/1_zero_shot.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/multimodal-ai-101/ko/02-image-encoders-clip-vit.md)
