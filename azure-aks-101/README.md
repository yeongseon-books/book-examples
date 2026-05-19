# azure-aks-101

`azure-aks-101` 시리즈의 예제 코드 저장소입니다. 모든 예제는 오프라인에서 실행 가능한 mock 기반이며, Azure 계정 자격 증명 없이 AKS 핵심 개념을 재현하도록 구성했습니다.

## 요구사항

- Python 3.11+

## 설치

```bash
pip install -r requirements.txt
```

## 실행

```bash
python ko/01-what-is-aks/step01_aks_summary.py
python en/07-monitoring-and-ops/step01_monitoring_queries.py
python -m pytest tests/ -q
```

## 디렉토리 맵

- `common.py` - az/kubectl 예제 토큰, YAML 빌더, mock 유틸리티
- `ko/` - 한국어 에피소드별 예제 (01-07)
- `en/` - `ko/`와 동일 로직의 영어 미러 예제
- `tests/` - 에피소드별 행동 검증 테스트

## 에피소드 인덱스

- 01: https://github.com/yeongseon-books/book-content/blob/master/content/azure-aks-101/ko/01-what-is-aks.md
- 02: https://github.com/yeongseon-books/book-content/blob/master/content/azure-aks-101/ko/02-cluster-architecture.md
- 03: https://github.com/yeongseon-books/book-content/blob/master/content/azure-aks-101/ko/03-first-cluster-and-deploy.md
- 04: https://github.com/yeongseon-books/book-content/blob/master/content/azure-aks-101/ko/04-pod-deployment-service.md
- 05: https://github.com/yeongseon-books/book-content/blob/master/content/azure-aks-101/ko/05-networking-and-ingress.md
- 06: https://github.com/yeongseon-books/book-content/blob/master/content/azure-aks-101/ko/06-scaling-hpa-ca-keda.md
- 07: https://github.com/yeongseon-books/book-content/blob/master/content/azure-aks-101/ko/07-monitoring-and-ops.md

## 주의사항

- 이 저장소는 학습용 오프라인 mock 예제입니다.
- 실제 `az`/`kubectl` 명령은 실행하지 않으며, 명령 토큰과 매니페스트 구조만 검증합니다.
- 실제 Azure 리소스 생성, 인증서 발급, 네트워크 구성은 포함하지 않습니다.

## License

MIT
