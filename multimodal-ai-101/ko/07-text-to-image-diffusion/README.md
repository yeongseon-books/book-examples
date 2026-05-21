# Multimodal AI 101 (7/10): Diffusion으로 Text-to-Image 생성

Multimodal Ai 101 시리즈 7편 예제 코드입니다.

## 학습 목표

- 왜 diffusion이 GAN을 빠르게 밀어내고 시각 생성의 기본 구조가 되었을까요?
- forward process와 reverse process를 어떤 멘탈 모델로 이해하면 가장 실용적일까요?
- Stable Diffusion의 text encoder, UNet, VAE는 각각 어떤 역할을 맡을까요?

## 자산 목록

| 파일 | 설명 |
|------|------|
| `controlnet.py` | 예제 코드 |
| `dall_e_api.py` | 예제 코드 |
| `diffusers_30.py` | 예제 코드 |
| `inpainting_image_to_image.py` | 예제 코드 |
| `step01_text_to_image.py` | 예제 코드 |

## 실행 방법

```bash
cd multimodal-ai-101
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python ko/07-text-to-image-diffusion/controlnet.py
```

## 관련 글

- [본문 보기](https://github.com/yeongseon-books/book-content/blob/main/content/multimodal-ai-101/ko/07-text-to-image-diffusion.md)
