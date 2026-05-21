# Multimodal AI 101 (9/10): Video 이해 - Frame Sampling에서 Video-LLaVA까지

Multimodal Ai 101 시리즈 9편 예제 코드입니다.

## 학습 목표

- 왜 비디오 이해에서 frame sampling이 가장 먼저 결정해야 할 핵심 변수일까요?
- PyAV와 scene change 기반 keyframe extraction은 각각 어떤 장면에서 유용할까요?
- VideoMAE, TimeSformer, X-CLIP 같은 video encoder는 어떤 trade-off를 보여 줄까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `step01_video_understanding.py` | 예제 코드 |

## 실행 방법

```bash
cd multimodal-ai-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/09-video-understanding/step01_video_understanding.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/multimodal-ai-101/ko/09-video-understanding.md)
