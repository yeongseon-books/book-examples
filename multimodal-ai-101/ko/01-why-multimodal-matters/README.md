# Multimodal AI 101 (1/10): Multimodal AI가 중요한 이유

Multimodal Ai 101 시리즈 1편 예제 코드입니다.

## 학습 목표

- 텍스트 LLM만으로는 왜 문서 QA, 시각 검색, 화면 이해 문제에서 한계가 빠르게 드러날까요?
- 멀티모달 시스템은 어떤 종류의 업무에서 기존 OCR + 규칙 기반 파이프라인보다 강한가요?
- 여러 modality를 결합하는 early fusion, late fusion, hybrid fusion은 무엇이 다를까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `clip_cross_modal.py` | 예제 코드 |
| `multimodal_gpt_4v.py` | 예제 코드 |
| `snippet.py` | 예제 코드 |
| `step01_why_multimodal.py` | 예제 코드 |

## 실행 방법

```bash
cd multimodal-ai-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/01-why-multimodal-matters/clip_cross_modal.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/multimodal-ai-101/ko/01-why-multimodal-matters.md)
