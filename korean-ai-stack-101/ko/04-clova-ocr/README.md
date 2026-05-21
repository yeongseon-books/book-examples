# Korean AI Stack 101 (4/6): CLOVA OCR API로 문서 텍스트 추출

Korean Ai Stack 101 시리즈 4편 예제 코드입니다.

## 학습 목표

- OCR을 붙일 때는 텍스트 정확도부터 봐야 할까요, 아니면 응답 구조부터 봐야 할까요?
- bounding box와 `lineBreak` 힌트는 후처리에서 왜 그렇게 중요할까요?
- 실제 API 키가 없어도 OCR 파이프라인의 대부분을 왜 검증할 수 있을까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_ocr_mock.py` | 예제 코드 |
| `step02_ocr_postprocess.py` | 예제 코드 |

## 실행 방법

```bash
cd korean-ai-stack-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/04-clova-ocr/step01_ocr_mock.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/korean-ai-stack-101/ko/04-clova-ocr.md)
