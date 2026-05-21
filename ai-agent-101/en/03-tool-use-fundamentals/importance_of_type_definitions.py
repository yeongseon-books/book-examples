# Bad: Undefined type details
{
    "parameters": {
        "type": "object",
        "properties": {
            "date": {"type": "string"}  # What format? YYYY-MM-DD? DD/MM/YYYY?
        }
    }
}

# Good: Explicit format specification
{
    "parameters": {
        "type": "object",
        "properties": {
            "date": {
                "type": "string",
                "description": "Date in YYYY-MM-DD format (e.g., 2024-03-15)",
                "pattern": "^\\d{4}-\\d{2}-\\d{2}$"
            }
        }
    }
}
