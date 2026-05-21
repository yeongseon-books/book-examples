"""Generated from book-content article."""

{
    "name": "create_order",
    "description": "Creates a new order.",
    "parameters": {
        "type": "object",
        "properties": {
            "customer_id": {
                "type": "string",
                "description": "Customer ID"
            },
            "items": {
                "type": "array",
                "description": "List of order items",
                "items": {
                    "type": "object",
                    "properties": {
                        "product_id": {"type": "string"},
                        "quantity": {"type": "integer", "minimum": 1}
                    },
                    "required": ["product_id", "quantity"]
                }
            }
        },
        "required": ["customer_id", "items"]
    }
}
