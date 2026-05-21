"""Generated from book-content article."""

def trim_messages(messages):
    # Always keep system prompt
    system_msg = messages[0]
    recent_msgs = messages[-5:]
    
    if system_msg not in recent_msgs:
        return [system_msg] + recent_msgs
    return recent_msgs
