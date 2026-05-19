# azure-app-service-101

`azure-app-service-101` 시리즈의 예제 코드 저장소입니다. 모든 예제는 오프라인에서 실행 가능한 mock 기반 학습 코드입니다.

## 요구사항

- Python 3.11+

## 설치

```bash
pip install -r requirements.txt
```

## 실행

```bash
python ko/01-what-is-app-service/step01_three_planes.py
python en/07-scaling-101/step01_scaling_strategy.py
python3 -m pytest tests/ -q
```

## 디렉토리 맵

- `common.py`: 공통 Azure CLI 명령 빌더
- `ko/`: 한국어 에피소드별 예제 (01-07)
- `en/`: `ko/`와 동일 로직의 영어 예제
- `tests/`: 에피소드별 동작 검증 테스트

## 오프라인 실행 원칙

- 이 저장소는 Azure API를 실제 호출하지 않습니다.
- `az` 명령은 문자열/페이로드 예시로만 다룹니다.
- HTTP 예제는 FastAPI + TestClient로 로컬에서만 검증합니다.

## 에피소드 인덱스

1. [01-what-is-app-service.md](https://github.com/yeongseon-books/book-content/blob/master/content/azure-app-service-101/ko/01-what-is-app-service.md)
2. [02-request-lifecycle.md](https://github.com/yeongseon-books/book-content/blob/master/content/azure-app-service-101/ko/02-request-lifecycle.md)
3. [03-hosting-models.md](https://github.com/yeongseon-books/book-content/blob/master/content/azure-app-service-101/ko/03-hosting-models.md)
4. [04-first-deploy.md](https://github.com/yeongseon-books/book-content/blob/master/content/azure-app-service-101/ko/04-first-deploy.md)
5. [05-configuration.md](https://github.com/yeongseon-books/book-content/blob/master/content/azure-app-service-101/ko/05-configuration.md)
6. [06-logging-monitoring.md](https://github.com/yeongseon-books/book-content/blob/master/content/azure-app-service-101/ko/06-logging-monitoring.md)
7. [07-scaling-101.md](https://github.com/yeongseon-books/book-content/blob/master/content/azure-app-service-101/ko/07-scaling-101.md)

## License

MIT
