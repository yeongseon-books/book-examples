# Multimodal AI 101 (5/10): Multimodal RAG: 이미지와 텍스트를 함께 검색하기

Multimodal Ai 101 시리즈 5편 예제 코드입니다.

## 학습 목표

- 텍스트 RAG는 왜 이미지, 표, 레이아웃 정보가 중요한 질문에서 곧바로 성능 한계를 드러낼까요?
- 멀티모달 검색을 위해 원본 이미지, caption/OCR, dual index를 쓰는 세 가지 전략은 어떻게 다를까요?
- 검색 결과를 최종 답변 단계에서 VLM에 넘길 때 어떤 입력 조합이 가장 실용적일까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `1_image_embedding.py` | 예제 코드 |
| `2_caption_ocr.py` | 예제 코드 |
| `3_hybrid_image_vector_text_vector.py` | 예제 코드 |
| `multimodal_rag.py` | 예제 코드 |
| `step01_multimodal_rag.py` | 예제 코드 |
| `vlm.py` | 예제 코드 |

## 실행 방법

```bash
cd multimodal-ai-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/05-multimodal-rag/1_image_embedding.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/multimodal-ai-101/ko/05-multimodal-rag.md)
