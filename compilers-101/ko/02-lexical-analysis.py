"""Compilers 101 - Episode 2: Lexical analysis."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Token:
    """Token."""

    kind: str
    value: object


def tokenize(source: str) -> list[Token]:
    """Tokenize."""
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
            raise SyntaxError(f"unexpected character: {ch}")
    return out


if __name__ == "__main__":
    print(tokenize("1 + 2 * (3 + 4)"))
