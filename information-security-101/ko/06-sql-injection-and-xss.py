from common import SQLInjectionDetector, XSSDetector

sql = SQLInjectionDetector()
xss = XSSDetector()
print(
    {
        "sql_bad": sql.is_suspicious("' OR 1=1 --"),
        "xss_bad": xss.is_suspicious("<script>alert(1)</script>"),
    }
)
