"""Generated from book-content article."""

from dataclasses import dataclass


@dataclass
class ScopedDataAccess:
    """Restricts data access to the task's scope."""
    user_id: str
    region: str
    allowed_tables: set[str]

    def query(self, sql: str) -> list[dict]:
        """Validates SQL and enforces scope."""
        self._validate_tables(sql)
        scoped_sql = self._inject_filters(sql)
        return self._execute(scoped_sql)

    def _validate_tables(self, sql: str) -> None:
        # Naive check — use a real SQL parser in production
        for table in ["users", "orders", "payments"]:
            if table in sql.lower() and table not in self.allowed_tables:
                raise ScopeViolation(f"table not allowed: {table}")

    def _inject_filters(self, sql: str) -> str:
        # Inject region filter into WHERE clause
        if "where" in sql.lower():
            return sql + f" AND region = '{self.region}'"
        return sql + f" WHERE region = '{self.region}'"

    def _execute(self, sql: str) -> list[dict]:
        return []

class ScopeViolation(Exception):
    pass
