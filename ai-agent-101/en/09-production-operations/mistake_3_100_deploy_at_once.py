# Bad
def deploy_v2():
    global agent
    agent = AgentV2()  # all traffic switches instantly

# Good
def deploy_v2():
    router.register("canary", AgentV2())
    router.adjust_canary(0.05)  # start at 5%
    # monitor and ramp up gradually
