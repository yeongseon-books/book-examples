"""Generated from book-content article."""

{
    "name": "get_customer_profile",
    "description": "Retrieves customer profile information (name, email, signup date) by customer ID. Does not include customer history or order records.",
    "parameters": {
        "type": "object",
        "properties": {
            "customer_id": {
                "type": "string",
                "description": "Unique customer identifier (e.g., CUST-12345)"
            }
        },
        "required": ["customer_id"]
    }
}
