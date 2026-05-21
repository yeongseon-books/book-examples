# Multimodal AI 101 (8/10): Multimodal Embedding과 Cross-modal 검색

Multimodal Ai 101 시리즈 8편 예제 코드입니다.

## 학습 목표

- Multimodal embedding은 텍스트 임베딩과 무엇이 다르고, 왜 cross-modal search의 핵심일까요?
- CLIP, SigLIP, ImageBind는 어떤 공통점과 차이를 가지며 무엇을 기준으로 선택해야 할까요?
- OpenCLIP으로 벡터를 추출할 때 preprocessing과 normalization은 왜 계약 수준으로 중요할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `3_openclip_embedding.py` | 예제 코드 |
| `4_faiss_cross_modal_index.py` | 예제 코드 |
| `4_faiss_cross_modal_index_04.py` | 예제 코드 |
| `5_imagebind_audio.py` | 예제 코드 |
| `6_1_embedding_bm25_ensemble.py` | 예제 코드 |
| `step01_multimodal_embeddings.py` | 예제 코드 |

## 실행 방법

```bash
cd multimodal-ai-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/08-multimodal-embeddings/3_openclip_embedding.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/multimodal-ai-101/ko/08-multimodal-embeddings.md)
