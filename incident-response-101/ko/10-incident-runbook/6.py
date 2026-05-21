"""Generated from book-content article."""

def run_incident(sev, schedule, now, summary):
    person = on_call(schedule, now)
    msg = comms("internal", sev, summary)
    return {
        "sev": SEV[sev],
        "ic": person["name"],
        "first_msg": msg,
        "step": "ack",
        "postmortem": link_postmortem("INC-001"),
    }
