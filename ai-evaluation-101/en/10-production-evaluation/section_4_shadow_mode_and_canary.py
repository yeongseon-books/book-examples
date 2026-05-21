"""Generated from book-content article."""

async def shadow_call(input_text: str):
    """Serve from the primary model, log a shadow call to the candidate."""
    primary = await call_model("gpt-4o", input_text)
    asyncio.create_task(log_shadow(input_text, primary))
    return primary

async def log_shadow(input_text: str, primary_output: str):
    shadow = await call_model("gpt-4o-mini", input_text)
    await db.insert_shadow_comparison({
        "input": input_text,
        "primary": primary_output,
        "shadow": shadow,
        "timestamp": datetime.utcnow(),
    })
