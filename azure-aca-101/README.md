# azure-aca-101

`azure-aca-101` 시리즈의 예제 코드 저장소입니다. 모든 예제는 오프라인 실행 가능한 mock 기반으로 구성되어 있으며, Azure Container Apps 핵심 개념을 에피소드별로 작게 검증할 수 있게 설계했습니다.

예제는 실제 Azure 리소스를 만들지 않습니다. az 명령은 문자열로 구성하여 출력하거나 mock으로 검증합니다.

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
python ko/01-what-is-aca/step01_aca_positioning.py
python en/07-monitoring-and-ops/step01_observability_queries.py
python -m pytest tests/ -q
```

## 디렉토리 맵

- `common.py` - 공통 mock Azure CLI 명령 생성, 스케일/트래픽 보조 유틸리티
- `ko/` - 한국어 에피소드별 예제 (01-07)
- `en/` - `ko/`와 동일 로직의 영어 예제
- `tests/` - 에피소드별 행동 테스트

## 에피소드 인덱스

- 01. [Azure Container Apps란? — Kubernetes 없이 컨테이너 운영하기](https://github.com/yeongseon-books/book-content/blob/master/content/azure-aca-101/ko/01-what-is-aca.md)
- 02. [Environment·Container App·Revision — 세 단어로 보는 ACA](https://github.com/yeongseon-books/book-content/blob/master/content/azure-aca-101/ko/02-environment-app-revision.md)
- 03. [첫 앱 배포하기 — Python/FastAPI](https://github.com/yeongseon-books/book-content/blob/master/content/azure-aca-101/ko/03-first-deploy.md)
- 04. [Ingress와 트래픽 분할 — Revision 기반 배포 전략](https://github.com/yeongseon-books/book-content/blob/master/content/azure-aca-101/ko/04-ingress-and-traffic-split.md)
- 05. [스케일링 — KEDA scaler와 0-to-N](https://github.com/yeongseon-books/book-content/blob/master/content/azure-aca-101/ko/05-scaling-with-keda.md)
- 06. [Dapr 통합 — 사이드카로 얻는 것](https://github.com/yeongseon-books/book-content/blob/master/content/azure-aca-101/ko/06-dapr-integration.md)
- 07. [모니터링과 운영 — Log Analytics와 Application Insights](https://github.com/yeongseon-books/book-content/blob/master/content/azure-aca-101/ko/07-monitoring-and-ops.md)

## 주의사항

- 이 저장소는 학습용 mock 예제입니다.
- 실제 Azure API 호출, az CLI 실행, 인증 자격 증명은 필요하지 않습니다.

## License

MIT
