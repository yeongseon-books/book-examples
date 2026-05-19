# azure-aca-deep-dive

`azure-aca-deep-dive` 시리즈의 예제 코드 저장소입니다. 모든 예제는 오프라인에서 실행 가능한 mock-only 코드이며, Azure API 호출이나 `az` CLI 실제 실행 없이 ACA 동작을 재현 가능한 형태로 검증합니다.

## 요구사항

- Python 3.11+

## 설치

```bash
pip install -r requirements.txt
```

## 실행

```bash
python ko/01-aca-architecture/step01_architecture_map.py
python en/06-envoy-ingress-path/step01_ingress_path.py
python -m pytest tests/ -q
```

## 디렉토리 맵

- `common.py` - 공통 dry-run 도우미(`subprocess`)와 payload 유틸리티
- `ko/` - 한국어 에피소드별 예제 (01-06)
- `en/` - `ko/`와 동일 로직의 영어 예제
- `tests/` - 에피소드별 행동 검증 테스트

## 에피소드 인덱스

1. [01-aca-architecture.md](https://github.com/yeongseon-books/book-content/blob/master/content/azure-aca-deep-dive/ko/01-aca-architecture.md)
2. [02-environment-internals.md](https://github.com/yeongseon-books/book-content/blob/master/content/azure-aca-deep-dive/ko/02-environment-internals.md)
3. [03-revision-and-traffic-split.md](https://github.com/yeongseon-books/book-content/blob/master/content/azure-aca-deep-dive/ko/03-revision-and-traffic-split.md)
4. [04-keda-in-aca.md](https://github.com/yeongseon-books/book-content/blob/master/content/azure-aca-deep-dive/ko/04-keda-in-aca.md)
5. [05-dapr-sidecar-internals.md](https://github.com/yeongseon-books/book-content/blob/master/content/azure-aca-deep-dive/ko/05-dapr-sidecar-internals.md)
6. [06-envoy-ingress-path.md](https://github.com/yeongseon-books/book-content/blob/master/content/azure-aca-deep-dive/ko/06-envoy-ingress-path.md)

## 주의사항

- 이 저장소는 학습용 오프라인 mock-only 예제입니다.
- 실제 Azure 구독, 자격 증명, 리소스 생성이 필요하지 않습니다.
- `az` 명령은 문자열/서브프로세스 dry-run으로만 다룹니다.

## License

MIT
