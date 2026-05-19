"""에피소드 08: 메모리 기반 미니 관계형 엔진"""


class Table:
    def __init__(self, rows: list[dict]):
        self.rows = rows

    def select(self, *columns: str) -> "Table":
        return Table([{c: row[c] for c in columns} for row in self.rows])

    def where(self, predicate):
        return Table([row for row in self.rows if predicate(row)])

    def join(self, other: "Table", left_key: str, right_key: str, prefix_right: str = "r_") -> "Table":
        index: dict[object, list[dict]] = {}
        for row in other.rows:
            index.setdefault(row[right_key], []).append(row)
        out = []
        for left in self.rows:
            for right in index.get(left[left_key], []):
                merged = dict(left)
                for k, v in right.items():
                    merged[k if k not in merged else prefix_right + k] = v
                out.append(merged)
        return Table(out)


if __name__ == "__main__":
    users = Table([{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}])
    orders = Table([{"order_id": 10, "user_id": 1, "amount": 50}])
    result = users.join(orders, "id", "user_id").where(lambda r: r["amount"] >= 50)
    print(result.rows)
