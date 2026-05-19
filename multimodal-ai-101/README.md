# multimodal-ai-101

`multimodal-ai-101` 시리즈 예제 코드 저장소입니다. 모든 예제는 오프라인에서 실행되는 mock 기반 구현입니다.

## 핵심 원칙

- mock encoders만 사용합니다.
- 모델 다운로드가 없습니다.
- GPU가 필요하지 않습니다.
- `torch`, `transformers`, `openai`를 사용하지 않습니다.

## 설치

```bash
pip install -r requirements.txt
```

## 실행

```bash
python ko/05-multimodal-rag/step01_multimodal_rag.py
python en/10-production-multimodal-app/step01_production_app.py
pytest -q
```
