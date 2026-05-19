# azure-aks-deep-dive

`azure-aks-deep-dive` 시리즈의 예제 코드 저장소입니다. 모든 예제는 오프라인에서 실행 가능한 mock-only 구조로 작성했으며, `az`/`kubectl` 명령은 문자열 예시로만 제공합니다.

## 요구사항

- Python 3.11+

## 설치

```bash
pip install -r requirements.txt
```

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 실행

```bash
python ko/01-control-plane-anatomy/step01_control_plane_boundary.py
python en/06-keda-internals/step01_keda_scaledobject_flow.py
python3 -m pytest tests/ -q
```

## 디렉토리 맵

- `common.py` - YAML/명령 문자열 공용 유틸리티
- `ko/` - 한국어 에피소드별 예제 (01-06)
- `en/` - `ko/`와 동일 로직의 영어 예제
- `tests/` - 에피소드별 동작 검증 테스트

## 에피소드 인덱스

1. [01-control-plane-anatomy](https://github.com/yeongseon-books/book-content/blob/master/content/azure-aks-deep-dive/ko/01-control-plane-anatomy.md)
2. [02-kubelet-and-containerd](https://github.com/yeongseon-books/book-content/blob/master/content/azure-aks-deep-dive/ko/02-kubelet-and-containerd.md)
3. [03-cni-and-azure-cni-overlay](https://github.com/yeongseon-books/book-content/blob/master/content/azure-aks-deep-dive/ko/03-cni-and-azure-cni-overlay.md)
4. [04-scheduler-and-pod-placement](https://github.com/yeongseon-books/book-content/blob/master/content/azure-aks-deep-dive/ko/04-scheduler-and-pod-placement.md)
5. [05-hpa-and-cluster-autoscaler-internals](https://github.com/yeongseon-books/book-content/blob/master/content/azure-aks-deep-dive/ko/05-hpa-and-cluster-autoscaler-internals.md)
6. [06-keda-internals](https://github.com/yeongseon-books/book-content/blob/master/content/azure-aks-deep-dive/ko/06-keda-internals.md)

## 주의사항

- 이 저장소는 학습용 예제이며 클라우드 리소스를 실제 호출하지 않습니다.
- HTTP 예제는 FastAPI `TestClient`로 오프라인 검증합니다.

## License

MIT
