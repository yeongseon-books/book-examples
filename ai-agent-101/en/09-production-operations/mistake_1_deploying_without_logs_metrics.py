# Bad
def handle_request(req):
    return agent.run(req)  # zero logging, zero metrics

# Good
def handle_request(req):
    req_id = str(uuid.uuid4())
    logger.info("request_received", request_id=req_id, user=req["user"])
    start = time.time()
    try:
        result = agent.run(req)
        metrics.timing("agent.duration", (time.time() - start) * 1000)
        metrics.increment("agent.success")
        return result
    except Exception as e:
        logger.error("request_failed", request_id=req_id, error=str(e))
        metrics.increment("agent.error")
        raise
