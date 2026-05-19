# English mirror of Korean episode example
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Token:
    kind: str
    value: object


def tokenize(source: str) -> list[Token]:
    out: list[Token] = []
    i = 0
    mapping = {
        "+": "PLUS",
        "-": "MINUS",
        "*": "STAR",
        "/": "SLASH",
        "(": "LPAREN",
        ")": "RPAREN",
    }
    while i < len(source):
        ch = source[i]
        if ch.isspace():
            i += 1
        elif ch.isdigit():
            j = i
            while j < len(source) and source[j].isdigit():
                j += 1
            out.append(Token("NUMBER", int(source[i:j])))
            i = j
        elif ch in mapping:
            out.append(Token(mapping[ch], ch))
            i += 1
        else:
            raise SyntaxError(ch)
    return out


def parse_expression(source: str) -> tuple:
    tokens = tokenize(source)
    pos = 0

    def peek() -> Token | None:
        return tokens[pos] if pos < len(tokens) else None

    def consume(kind: str) -> Token:
        nonlocal pos
        tok = peek()
        if tok is None or tok.kind != kind:
            raise SyntaxError(f"expected {kind}, got {tok}")
        pos += 1
        return tok

    def factor() -> tuple:
        tok = peek()
        if tok is None:
            raise SyntaxError("eof")
        if tok.kind == "NUMBER":
            consume("NUMBER")
            return ("num", tok.value)
        if tok.kind == "LPAREN":
            consume("LPAREN")
            node = expr()
            consume("RPAREN")
            return node
        raise SyntaxError("bad factor")

    def term() -> tuple:
        node = factor()
        while True:
            tok = peek()
            if tok and tok.kind in {"STAR", "SLASH"}:
                op = "*" if tok.kind == "STAR" else "/"
                consume(tok.kind)
                node = ("bin", op, node, factor())
            else:
                return node

    def expr() -> tuple:
        node = term()
        while True:
            tok = peek()
            if tok and tok.kind in {"PLUS", "MINUS"}:
                op = "+" if tok.kind == "PLUS" else "-"
                consume(tok.kind)
                node = ("bin", op, node, term())
            else:
                return node

    result = expr()
    if pos != len(tokens):
        raise SyntaxError("trailing")
    return result


if __name__ == "__main__":
    print(parse_expression("1 + 2 * 3"))
