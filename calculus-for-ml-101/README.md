# calculus-for-ml-101

`calculus-for-ml-101` 시리즈 예제 코드 저장소입니다. 모든 예제는 오프라인에서 실행 가능한 mock-only 학습 코드로 구성되어 있습니다.

## 요구사항

- Python 3.11+

## 설치

```bash
pip install -r requirements.txt
```

## 실행

```bash
python ko/01-what-is-derivative/step01_derivative.py
python en/10-calculus-in-deep-learning/step01_training_loop.py
python3 -m pytest tests/ -q
```

## 에피소드 인덱스

1. [01 미분이란 무엇인가](https://github.com/yeongseon-books/book-content/blob/master/content/calculus-for-ml-101/ko/01-what-is-derivative.md)
2. [02 함수와 기울기](https://github.com/yeongseon-books/book-content/blob/master/content/calculus-for-ml-101/ko/02-functions-and-slope.md)
3. [03 편미분](https://github.com/yeongseon-books/book-content/blob/master/content/calculus-for-ml-101/ko/03-partial-derivatives.md)
4. [04 Gradient](https://github.com/yeongseon-books/book-content/blob/master/content/calculus-for-ml-101/ko/04-gradient.md)
5. [05 연쇄 법칙](https://github.com/yeongseon-books/book-content/blob/master/content/calculus-for-ml-101/ko/05-chain-rule.md)
6. [06 손실 함수](https://github.com/yeongseon-books/book-content/blob/master/content/calculus-for-ml-101/ko/06-loss-function.md)
7. [07 경사하강법](https://github.com/yeongseon-books/book-content/blob/master/content/calculus-for-ml-101/ko/07-gradient-descent.md)
8. [08 최적화](https://github.com/yeongseon-books/book-content/blob/master/content/calculus-for-ml-101/ko/08-optimization.md)
9. [09 역전파 직관](https://github.com/yeongseon-books/book-content/blob/master/content/calculus-for-ml-101/ko/09-backpropagation-intuition.md)
10. [10 딥러닝에서의 미분](https://github.com/yeongseon-books/book-content/blob/master/content/calculus-for-ml-101/ko/10-calculus-in-deep-learning.md)

## 디렉토리 맵

- `ko/` - 한국어 에피소드별 예제 (01-10)
- `en/` - `ko/`와 동일 로직의 영어 예제
- `tests/` - 에피소드별 행동 테스트

## 주의사항

- 이 저장소는 학습용 mock-only 예제입니다.
- 외부 API 호출, 네트워크 의존, 온라인 서비스 연동은 포함하지 않았습니다.

## License

MIT
