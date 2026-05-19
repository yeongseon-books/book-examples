"""Information Security 101 - Episode 6: Sql injection and xss."""

from common import SQLInjectionDetector, XSSDetector

sql = SQLInjectionDetector()
xss = XSSDetector()
print(
    {
        "sql_safe": sql.is_suspicious("alice"),
        "xss_bad": xss.is_suspicious("javascript:alert(1)"),
    }
)
