# compilers-101 예제 코드

`compilers-101` 시리즈의 핵심 개념을 에피소드별로 실행 가능한 Python 예제로 정리한 저장소입니다.

## 구성

- 01. What Is a Compiler?
- 02. lexical analysis
- 03. parsing and AST
- 04. semantic analysis
- 05. symbol table and scope
- 06. intermediate representation
- 07. optimization basics
- 08. code generation
- 09. JIT vs AOT
- 10. Building a Tiny Interpreter

## 실행

```bash
pip install -r requirements.txt
python ko/01-what-is-a-compiler.py
```

## 테스트

```bash
pytest tests/ -q
```

## 원본

- https://github.com/yeongseon-books/book-content/tree/master/content/compilers-101
