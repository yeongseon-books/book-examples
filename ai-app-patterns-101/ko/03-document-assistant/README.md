# AI App Patterns 101 (3/6): 문서 어시스턴트 — 요약, 추출, 분류

Ai App Patterns 101 시리즈 3편 예제 코드입니다.

## 학습 목표

- 문서 어시스턴트에서 요약, 추출, 분류는 왜 서로 다른 출력 계약이 필요할까요?
- 긴 문서는 언제 Map-Reduce 요약처럼 단계적으로 나눠야 할까요?
- 추출과 분류 결과를 운영 코드가 믿으려면 어떤 검증이 필요할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_summary_extract.py` | 예제 코드 |
| `step02_document_classifier.py` | 예제 코드 |

## 실행 방법

```bash
cd ai-app-patterns-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/03-document-assistant/step01_summary_extract.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/ai-app-patterns-101/ko/03-document-assistant.md)
