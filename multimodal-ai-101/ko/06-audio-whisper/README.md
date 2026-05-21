# Multimodal AI 101 (6/10): 오디오 처리와 Whisper STT

Multimodal Ai 101 시리즈 6편 예제 코드입니다.

## 학습 목표

- 왜 Whisper가 오픈소스 STT의 사실상 기본값처럼 자리 잡았을까요?
- Whisper 아키텍처는 어떤 방식으로 30초 오디오를 텍스트와 timestamp로 바꿀까요?
- 로컬 추론, faster-whisper, OpenAI API 호출은 각각 어떤 상황에서 유리할까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `30_chunking_timestamping.py` | 예제 코드 |
| `api.py` | 예제 코드 |
| `openai_api.py` | 예제 코드 |
| `openai_whisper_30.py` | 예제 코드 |
| `production_faster_whisper.py` | 예제 코드 |
| `srt.py` | 예제 코드 |
| `step01_audio_encoder.py` | 예제 코드 |
| `streaming.py` | 예제 코드 |

## 실행 방법

```bash
cd multimodal-ai-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/06-audio-whisper/30_chunking_timestamping.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/multimodal-ai-101/ko/06-audio-whisper.md)
