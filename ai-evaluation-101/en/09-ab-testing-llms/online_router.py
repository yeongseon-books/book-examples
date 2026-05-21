# ab/online_router.py
import hashlib

def assign_variant(user_id: str, experiment: str) -> str:
    """Stable A/B assignment by hashing user_id."""
    h = hashlib.sha256(f"{experiment}:{user_id}".encode()).hexdigest()
    return "A" if int(h, 16) % 2 == 0 else "B"

def handle_request(user_id: str, question: str) -> str:
    variant = assign_variant(user_id, experiment="prompt-v3-vs-v2")
    model = "gpt-4o" if variant == "A" else "gpt-4o-mini"
    response = get_response(model, question)
    log_metric(user_id, variant, response)
    return response
