# Bad
return {"error": str(exception)}  # Leaks internals and stack traces

# Good
return {
    "error": "Unable to process the request",
    "request_id": req_id,  # for internal tracing
}
# Detailed info stays in server logs only
