# cloud-computing-101

`cloud-computing-101` 시리즈의 예제 코드 저장소입니다. 모든 예제는 오프라인에서 실행 가능한 mock 기반으로 구성되어 있으며, 실제 클라우드 API 호출이나 자격 증명은 필요하지 않습니다.

## 요구사항

- Python 3.11+

## 설치

```bash
pip install -r requirements.txt
```

## 실행

```bash
python ko/01-what-is-cloud-computing/step01_service_models.py
python en/10-cloud-architecture-basics/step01_architecture_review.py
python3 -m pytest tests/ -q
```

## 디렉토리 맵

- `common.py` - 공통 mock 클라우드 호출 기록기
- `ko/` - 한국어 에피소드별 예제 (01-10)
- `en/` - `ko/`와 동일 로직의 영어 예제
- `tests/` - 에피소드별 동작 테스트

## 에피소드 원문 링크

1. [01-what-is-cloud-computing](https://github.com/yeongseon-books/book-content/blob/master/content/cloud-computing-101/ko/01-what-is-cloud-computing.md)
2. [02-iaas-paas-saas](https://github.com/yeongseon-books/book-content/blob/master/content/cloud-computing-101/ko/02-iaas-paas-saas.md)
3. [03-region-and-availability-zone](https://github.com/yeongseon-books/book-content/blob/master/content/cloud-computing-101/ko/03-region-and-availability-zone.md)
4. [04-compute](https://github.com/yeongseon-books/book-content/blob/master/content/cloud-computing-101/ko/04-compute.md)
5. [05-storage](https://github.com/yeongseon-books/book-content/blob/master/content/cloud-computing-101/ko/05-storage.md)
6. [06-network](https://github.com/yeongseon-books/book-content/blob/master/content/cloud-computing-101/ko/06-network.md)
7. [07-identity-and-security](https://github.com/yeongseon-books/book-content/blob/master/content/cloud-computing-101/ko/07-identity-and-security.md)
8. [08-monitoring](https://github.com/yeongseon-books/book-content/blob/master/content/cloud-computing-101/ko/08-monitoring.md)
9. [09-cost-management](https://github.com/yeongseon-books/book-content/blob/master/content/cloud-computing-101/ko/09-cost-management.md)
10. [10-cloud-architecture-basics](https://github.com/yeongseon-books/book-content/blob/master/content/cloud-computing-101/ko/10-cloud-architecture-basics.md)

## 주의사항

- 이 저장소의 코드는 학습용 mock 예제입니다.
- boto3, azure-sdk, gcp-sdk 등 실제 클라우드 SDK 호출은 포함하지 않습니다.
- 모든 테스트는 오프라인에서 재현 가능하게 설계했습니다.

## License

MIT
