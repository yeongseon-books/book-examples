"""Generated from book-content article."""

def classify_email(email_body: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Classify the email as high, medium, or low."},
            {"role": "user", "content": email_body},
        ],
    )
    return response.choices[0].message.content or ""
