# AI Data Preparation 101 (4/10): 학습 데이터 PII 탐지와 익명화

Ai Data Preparation 101 시리즈 4편 예제 코드입니다.

## 학습 목표

- PII 처리 파이프라인을 detection, classification, anonymization, audit로 나누는 이유는 무엇일까요?
- regex만으로 잡히는 정보와 NER가 추가로 잡아내는 정보는 어떻게 다를까요?
- redact, mask, pseudonymize, synthesize는 각각 어떤 운영 목적에 맞을까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_regex_redaction.py` | 예제 코드 |

## 실행 방법

```bash
cd ai-data-preparation-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/04-pii-detection-anonymization/step01_regex_redaction.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/ai-data-preparation-101/ko/04-pii-detection-anonymization.md)
