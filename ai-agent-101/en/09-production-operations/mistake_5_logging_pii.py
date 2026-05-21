# Bad
logger.info("request", user_message=req.message)  # raw personal data

# Good
logger.info("request",
    user_id=hash_user_id(req.user_id),  # hashed
    message_length=len(req.message),    # length only
    message_hash=hash(req.message)      # don't store contents
)
