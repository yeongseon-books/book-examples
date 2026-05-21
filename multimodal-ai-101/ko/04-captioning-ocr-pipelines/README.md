# Multimodal AI 101 (4/10): Image Captioning과 OCR 파이프라인

Multimodal Ai 101 시리즈 4편 예제 코드입니다.

## 학습 목표

- 왜 “이미지에서 텍스트만 추출하면 된다”는 접근이 실제 문서 처리에서는 자주 실패할까요?
- Captioning 모델과 VLM 기반 설명 생성은 어떤 입력에서 각각 강점과 한계를 보일까요?
- Tesseract, PaddleOCR, Document AI 계열은 어떤 기준으로 선택해야 할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `blip_style_captioning.py` | 예제 코드 |
| `cloud_api.py` | 예제 코드 |
| `ocr.py` | 예제 코드 |
| `ocr_vlm_hybrid.py` | 예제 코드 |
| `paddleocr_layout.py` | 예제 코드 |
| `step01_caption_ocr.py` | 예제 코드 |
| `tesseract.py` | 예제 코드 |
| `vlm_caption.py` | 예제 코드 |

## 실행 방법

```bash
cd multimodal-ai-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/04-captioning-ocr-pipelines/blip_style_captioning.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/multimodal-ai-101/ko/04-captioning-ocr-pipelines.md)
