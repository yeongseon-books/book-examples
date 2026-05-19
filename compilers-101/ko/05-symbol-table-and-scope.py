"""Compilers 101 - Episode 5: Symbol table and scope."""

from __future__ import annotations


class SymbolTable:
    """Symbol table."""

    def __init__(self, parent: SymbolTable | None = None):
        self.parent: SymbolTable | None = parent
        self.table: dict[str, str] = {}

    def insert(self, name: str, kind: str) -> None:
        """Insert."""
        if name in self.table:
            raise ValueError(f"redeclaration: {name}")
        self.table[name] = kind

    def lookup(self, name: str) -> str | None:
        """Lookup."""
        if name in self.table:
            return self.table[name]
        if self.parent is None:
            return None
        return self.parent.lookup(name)


if __name__ == "__main__":
    global_scope = SymbolTable()
    global_scope.insert("x", "global-int")
    local_scope = SymbolTable(global_scope)
    local_scope.insert("x", "local-int")
    print(local_scope.lookup("x"), global_scope.lookup("x"))
