from __future__ import annotations

# pyright: reportArgumentType=false, reportUnusedCallResult=false


def tokenize(src: str) -> list[tuple[str, object]]:
    out: list[tuple[str, object]] = []
    i = 0
    while i < len(src):
        ch = src[i]
        if ch.isspace():
            i += 1
        elif ch.isdigit():
            j = i
            while j < len(src) and src[j].isdigit():
                j += 1
            out.append(("NUM", int(src[i:j])))
            i = j
        elif ch.isalpha() or ch == "_":
            j = i
            while j < len(src) and (src[j].isalnum() or src[j] == "_"):
                j += 1
            out.append(("ID", src[i:j]))
            i = j
        elif ch in "+-*/=();":
            out.append((ch, ch))
            i += 1
        else:
            raise SyntaxError(ch)
    out.append(("EOF", None))
    return out


def run(src: str) -> int:
    tokens = tokenize(src)
    pos = 0
    env: dict[str, int] = {}

    def peek():
        return tokens[pos]

    def eat(kind: str):
        nonlocal pos
        tok = tokens[pos]
        if tok[0] != kind:
            raise SyntaxError(f"expected {kind}, got {tok}")
        pos += 1
        return tok

    def factor() -> int:
        tok = peek()
        if tok[0] == "NUM":
            eat("NUM")
            return int(tok[1])
        if tok[0] == "ID":
            eat("ID")
            name = str(tok[1])
            if name not in env:
                raise NameError(name)
            return env[name]
        if tok[0] == "(":
            eat("(")
            v = expr()
            eat(")")
            return v
        raise SyntaxError("bad factor")

    def term() -> int:
        v = factor()
        while peek()[0] in {"*", "/"}:
            op = eat(peek()[0])[0]
            r = factor()
            v = v * r if op == "*" else v // r
        return v

    def expr() -> int:
        v = term()
        while peek()[0] in {"+", "-"}:
            op = eat(peek()[0])[0]
            r = term()
            v = v + r if op == "+" else v - r
        return v

    def statement() -> int:
        if peek()[0] == "ID" and tokens[pos + 1][0] == "=":
            name = eat("ID")[1]
            eat("=")
            value = expr()
            env[str(name)] = value
            return value
        return expr()

    last = 0
    while peek()[0] != "EOF":
        last = statement()
        if peek()[0] == ";":
            eat(";")
    return last


if __name__ == "__main__":
    print(run("x = 5; x * 2"))
